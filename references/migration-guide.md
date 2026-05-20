# ManimGL And Old Code Migration

## Import Classifier

- `from manim import *`: Manim Community Edition.
- `from manimlib import *`: ManimGL.
- `from manimlib.imports import *`: older ManimCairo-era code.
- `from big_ol_pile_of_manim_imports import *`: old 3Blue1Brown-era code.

## Default Strategy

Do not mechanically port old code line by line. Recreate the scene in Manim CE with the same conceptual structure:

1. Identify the visual idea and key objects.
2. Replace old scene helpers with CE primitives.
3. Render a still frame.
4. Add animation phases.
5. Only then add polish or custom helpers.

## Common Differences

- ManimGL render command: `manimgl file.py SceneName`
- Manim CE render command: `uv run manim -ql file.py SceneName`
- ManimGL imports `manimlib`; Manim CE imports `manim`.
- Many 3Blue1Brown files use local helpers from `custom/` and `manim_imports_ext.py`.
- Older examples may depend on APIs that no longer exist or changed semantics.

## 3Blue1Brown Source Boundary

The `3b1b/videos` repository is valuable for learning production scene organization and visual style. It is not a source to copy wholesale into this plugin or into commercial deliverables unless the license is compatible.
