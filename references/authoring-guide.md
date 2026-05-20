# Authoring Guide

## Scene Structure

Prefer this shape:

```python
from manim import *


class MyScene(Scene):
    def construct(self):
        title = Text("The idea").to_edge(UP)
        visual = VGroup(...)

        self.play(Write(title))
        self.play(Create(visual))
        self.wait()
```

Keep one main scene class per file when practical. Small helper functions and constants are fine.

## Visual Flow

Most strong explanatory scenes follow this rhythm:

1. Establish the object or question.
2. Add the axes/grid/diagram scaffold.
3. Animate the operation or relationship.
4. Preserve a clear final frame.

## Useful Primitives

- Layout: `VGroup`, `Group`, `arrange`, `next_to`, `to_edge`, `to_corner`, `align_to`
- Motion: `Transform`, `ReplacementTransform`, `FadeIn`, `FadeOut`, `Create`, `LaggedStart`
- Math visuals: `Axes`, `NumberPlane`, `ComplexPlane`, `ParametricFunction`, `Vector`
- Dynamics: `ValueTracker`, `always_redraw`, updaters
- Camera: `MovingCameraScene`, `ThreeDScene`

## Text And TeX

Use `Text` for plain labels when possible. It does not need LaTeX.

Use `MathTex` and `Tex` when formula typography matters, but check:

```bash
command -v latex
command -v dvisvgm
```

If TeX is missing, either install it or build the draft with `Text`.

## Render Discipline

Use stills before motion:

```bash
uv run manim -ql -s scenes/example.py Example
```

Then draft:

```bash
uv run manim -ql scenes/example.py Example
```

Then final:

```bash
uv run manim -qh scenes/example.py Example
```

## Style Defaults

- Background: keep Manim's default dark background unless the task calls for another style.
- Colors: use contrast intentionally, not rainbow defaults.
- Labels: keep them short and positioned with `next_to` or `to_edge`.
- Motion: prefer fewer purposeful transforms over many decorative effects.
