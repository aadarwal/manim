from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("manim-renderer")

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = Path(os.getenv("MANIM_OUTPUT_DIR", ROOT / ".manim-media")).resolve()
OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
TIMEOUT_SECONDS = int(os.getenv("MANIM_TIMEOUT_SECONDS", "180"))
DEFAULT_TINYTEX_BIN = Path("/Volumes/aadarwal_vx/tools/TinyTeX/bin/universal-darwin")
LEGACY_EXTERNAL_TEXLIVE_BIN = Path("/Volumes/aadarwal_vx/tools/texlive/2026/bin/universal-darwin")


def _manim_command() -> list[str]:
    executable = os.getenv("MANIM_EXECUTABLE")
    if executable:
        return [executable]
    return [sys.executable, "-m", "manim"]


def _quality_flag(quality: str) -> str:
    quality_map = {
        "low": "-ql",
        "l": "-ql",
        "medium": "-qm",
        "m": "-qm",
        "high": "-qh",
        "h": "-qh",
        "production": "-qp",
        "p": "-qp",
        "4k": "-qk",
        "k": "-qk",
    }
    if quality in quality_map:
        return quality_map[quality]
    if quality in {"-ql", "-qm", "-qh", "-qp", "-qk"}:
        return quality
    raise ValueError(f"Unsupported quality: {quality}")


def _texlive_bin() -> Path:
    configured = os.getenv("MANIM_TEXLIVE_BIN")
    if configured:
        return Path(configured).expanduser()
    if DEFAULT_TINYTEX_BIN.is_dir():
        return DEFAULT_TINYTEX_BIN
    return LEGACY_EXTERNAL_TEXLIVE_BIN


def _artifacts(directory: Path) -> list[Path]:
    media_dir = directory / "media"
    if not media_dir.exists():
        return []
    return sorted(
        path
        for path in media_dir.rglob("*")
        if path.is_file()
        and path.suffix.lower() in {".mp4", ".mov", ".gif", ".png", ".webm"}
        and "partial_movie_files" not in path.parts
    )


def _format_result(
    *,
    status: str,
    run_dir: Path,
    command: list[str],
    stdout: str,
    stderr: str,
) -> str:
    artifact_paths = _artifacts(run_dir)
    artifacts = "\n".join(str(path) for path in artifact_paths)
    if not artifacts:
        artifacts = "No media artifacts found."
    return (
        f"{status}\n"
        f"Run directory: {run_dir}\n"
        f"Command: {' '.join(command)}\n"
        f"Artifacts:\n{artifacts}\n"
        f"stdout:\n{stdout.strip()}\n"
        f"stderr:\n{stderr.strip()}"
    )


def _render(
    *,
    script_path: Path,
    run_dir: Path,
    scene_name: str,
    quality: str,
    still: bool,
    renderer: str,
) -> str:
    command = [*_manim_command(), _quality_flag(quality)]
    if still:
        command.append("-s")
    if renderer:
        command.extend(["--renderer", renderer])
    command.append(str(script_path))
    if scene_name:
        command.append(scene_name)

    env = os.environ.copy()
    texlive_bin = _texlive_bin()
    if texlive_bin.is_dir():
        env["PATH"] = f"{texlive_bin}{os.pathsep}{env.get('PATH', '')}"

    try:
        result = subprocess.run(
            command,
            cwd=run_dir,
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
            check=False,
            env=env,
        )
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout or ""
        stderr = exc.stderr or ""
        return _format_result(
            status=f"Execution timed out after {TIMEOUT_SECONDS} seconds.",
            run_dir=run_dir,
            command=command,
            stdout=stdout if isinstance(stdout, str) else stdout.decode(),
            stderr=stderr if isinstance(stderr, str) else stderr.decode(),
        )

    status = "Execution successful." if result.returncode == 0 else "Execution failed."
    return _format_result(
        status=status,
        run_dir=run_dir,
        command=command,
        stdout=result.stdout,
        stderr=result.stderr,
    )


@mcp.tool()
def execute_manim_code(
    manim_code: str,
    scene_name: str = "",
    quality: str = "low",
    still: bool = False,
    renderer: str = "",
) -> str:
    """Render Manim Community Edition source code and return media paths."""
    run_dir = Path(tempfile.mkdtemp(prefix="manim_", dir=OUTPUT_ROOT))
    script_path = run_dir / "scene.py"
    script_path.write_text(manim_code, encoding="utf-8")
    return _render(
        script_path=script_path,
        run_dir=run_dir,
        scene_name=scene_name,
        quality=quality,
        still=still,
        renderer=renderer,
    )


@mcp.tool()
def execute_manim_file(
    scene_file: str,
    scene_name: str = "",
    quality: str = "low",
    still: bool = False,
    renderer: str = "",
) -> str:
    """Render an existing Manim file and return media paths."""
    source = Path(scene_file).expanduser().resolve()
    if not source.exists():
        return f"Scene file not found: {source}"
    run_dir = Path(tempfile.mkdtemp(prefix="manim_file_", dir=OUTPUT_ROOT))
    script_path = run_dir / source.name
    shutil.copy2(source, script_path)
    return _render(
        script_path=script_path,
        run_dir=run_dir,
        scene_name=scene_name,
        quality=quality,
        still=still,
        renderer=renderer,
    )


@mcp.tool()
def list_manim_outputs() -> str:
    """List rendered media artifacts under the MCP output directory."""
    artifacts = sorted(
        path
        for path in OUTPUT_ROOT.rglob("*")
        if path.is_file()
        and path.suffix.lower() in {".mp4", ".mov", ".gif", ".png", ".webm"}
        and "partial_movie_files" not in path.parts
    )
    if not artifacts:
        return f"No rendered media found under {OUTPUT_ROOT}"
    return "\n".join(str(path) for path in artifacts)


@mcp.tool()
def cleanup_manim_temp_dir(directory: str) -> str:
    """Delete a generated Manim run directory under the MCP output root."""
    target = Path(directory).expanduser().resolve()
    try:
        target.relative_to(OUTPUT_ROOT)
    except ValueError:
        return f"Refusing to delete outside output root: {target}"
    if not target.exists():
        return f"Directory not found: {target}"
    shutil.rmtree(target)
    return f"Deleted {target}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
