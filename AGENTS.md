# Agent Notes

This repository is the user's canonical Manim agent plugin/workbench.

## Purpose

Use this repo to create Manim-based mathematical animations, diagrams, still frames, and explanatory visuals. It intentionally combines:

- Codex plugin metadata
- a Manim authoring skill
- an MCP render server
- helper scripts
- original example scenes
- project templates
- ecosystem survey notes

Do not treat this repo as a fork of Manim Community Edition or 3Blue1Brown's ManimGL. Those projects are upstream references.

## First Files To Read

- `skills/manim-visualizer/SKILL.md`
- `references/source-survey.md`
- `references/authoring-guide.md`
- `references/mcp-server.md`

## Runtime Defaults

- New scenes: Manim Community Edition, `from manim import *`, render with `uv run manim`.
- ManimGL/3Blue1Brown scenes: reference only unless explicitly requested.
- Start with low-quality still renders, then draft videos, then final quality.
- Prefer `Text` when host LaTeX is unavailable; use `MathTex`/`Tex` only after checking TeX and `dvisvgm`.

## Important Commands

```bash
uv sync
./scripts/check_environment.sh
./scripts/render_manim.sh --project-dir ./examples --scene-file ./examples/scenes/basic_transform.py --scene-name BasicTransform --quality low --still
./scripts/run_mcp_server.sh
```

Generated media is ignored by Git and lands under `media/` in the relevant project, or under `.manim-media/` for MCP runs.
