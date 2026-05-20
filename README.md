# Manim Agent Plugin

This repository is an agent-ready Manim workbench: a Codex plugin, a local MCP render server, helper scripts, original example scenes, and concise references for building mathematical visualizations with Manim Community Edition.

It is not a fork of Manim. It uses the current Manim ecosystem as source material and gives agents a single, coherent entrypoint for authoring and rendering scenes.

## What It Includes

- Codex plugin manifest: `.codex-plugin/plugin.json`
- Main skill: `skills/manim-visualizer/SKILL.md`
- MCP render server: `mcp/manim_server.py`
- Scripts for setup, rendering, source bootstrapping, and output discovery
- Original example scenes under `examples/scenes/`
- A reusable starter project under `templates/basic_project/`
- Reference docs covering Manim CE, ManimGL, 3Blue1Brown examples, native Manim plugins, and MCP options

## Quick Start

Install the plugin repo tools:

```bash
uv sync
```

Check local prerequisites:

```bash
./scripts/check_environment.sh
```

If TinyTeX is installed at `/Volumes/aadarwal_vx/tools/TinyTeX`, the scripts automatically add its `bin/universal-darwin` directory to `PATH` so Manim can render `Tex` and `MathTex`. Set `MANIM_TEXLIVE_BIN` to override that binary directory.

Render an example still:

```bash
./scripts/render_manim.sh \
  --project-dir ./examples \
  --scene-file ./examples/scenes/basic_transform.py \
  --scene-name BasicTransform \
  --quality low \
  --still
```

Render an example video:

```bash
./scripts/render_manim.sh \
  --project-dir ./examples \
  --scene-file ./examples/scenes/linear_transform.py \
  --scene-name LinearTransformDemo \
  --quality low
```

Run the MCP server:

```bash
./scripts/run_mcp_server.sh
```

## Agent Usage

When an agent is pointed at this repo, start with:

- `AGENTS.md`
- `skills/manim-visualizer/SKILL.md`
- `references/source-survey.md`
- `references/authoring-guide.md`

Default to Manim Community Edition for new work. Use ManimGL and 3Blue1Brown video code as references, not as the target runtime, unless the user explicitly requests ManimGL compatibility.

## Source Material Policy

This repo contains original examples and workflow code. It does not vendor 3Blue1Brown video source because that repository is CC BY-NC-SA 4.0 and many old scenes depend on old Manim APIs.

Use:

```bash
./scripts/bootstrap_sources.sh
```

to clone upstream reference repositories into `.manim-sources/` when needed.
