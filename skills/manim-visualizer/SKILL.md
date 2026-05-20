---
name: manim-visualizer
description: Create, render, debug, or improve Manim Community Edition animations, still frames, mathematical visualizations, visual proofs, geometry/calculus/linear algebra explainers, and 3Blue1Brown-style scenes. Use when the user asks for Manim, math animation, explanatory visuals, scene generation, or an agent workflow for rendering Manim.
---

# Manim Visualizer

## Default Contract

Use Manim Community Edition for new work:

```python
from manim import *
```

Render with:

```bash
uv run manim -ql path/to/scene.py SceneName
```

Use ManimGL only when the user explicitly asks for Grant Sanderson's ManimGL workflow or old 3Blue1Brown compatibility.

## Load References As Needed

- Ecosystem and source survey: `../../references/source-survey.md`
- Scene authoring patterns: `../../references/authoring-guide.md`
- ManimGL and old-code migration: `../../references/migration-guide.md`
- MCP render workflow: `../../references/mcp-server.md`
- Native Manim plugins and when to use them: `../../references/manim-plugin-ecosystem.md`
- Examples index: `../../references/examples-index.md`

## Workflow

1. Clarify the output contract from the task: still frame, draft video, final video, scene source only, or MCP-renderable tool.
2. Reuse an existing project if present. Otherwise initialize a Manim project with `scripts/init_manim_project.sh` or copy `templates/basic_project/`.
3. Author one focused `Scene` class per file unless the project already has a different convention.
4. Render cheap first:
   - layout still: `-ql -s`
   - draft motion: `-ql`
   - final: `-qh`, `-qp`, or `-qk`
5. Report concrete artifact paths under `media/` or `.manim-media/`.

## Commands

From this plugin repo:

```bash
./scripts/check_environment.sh
./scripts/render_manim.sh --project-dir ./examples --scene-file ./examples/scenes/basic_transform.py --scene-name BasicTransform --quality low --still
./scripts/run_mcp_server.sh
```

From a generated project:

```bash
uv sync
uv run manim -ql -s scenes/main.py MainScene
uv run manim -ql scenes/main.py MainScene
```

## Authoring Rules

- Prefer Manim primitives before custom geometry: `Scene`, `ThreeDScene`, `VGroup`, `Axes`, `NumberPlane`, `ComplexPlane`, `ValueTracker`, `always_redraw`, `Transform`, `ReplacementTransform`, `TransformMatchingTex`, `MoveAlongPath`, and camera methods.
- Use `Text` for labels that do not require TeX. Use `MathTex` or `Tex` only after checking that TeX and `dvisvgm` are available.
- Keep geometry responsive to frame size by using `config.frame_width`, `config.frame_height`, `to_edge`, `arrange`, `next_to`, and `VGroup`.
- Avoid copying 3Blue1Brown video code into deliverables. Study it for structure and style, then write original Manim CE scenes.
- For dense concepts, stage the visual: introduce objects, show the relationship, transform or animate the key operation, then summarize with the final frame.

## Failure Handling

- Missing Cairo/Pango/pkg-config on macOS: run `brew install cairo pango pkgconf ffmpeg`.
- Missing TeX: avoid `MathTex`/`Tex`, install a TeX distribution, or render with Docker.
- Blank/incorrect renders: render a still first, inspect the output path, simplify camera/layout, then add motion back.
- Slow renders: use `-ql`, reduce object count, avoid heavy updaters, and cache reusable geometry.
