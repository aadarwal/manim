#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

"$root/scripts/render_manim.sh" --project-dir "$root/examples" --scene-file "$root/examples/scenes/basic_transform.py" --scene-name BasicTransform --quality low --still
"$root/scripts/render_manim.sh" --project-dir "$root/examples" --scene-file "$root/examples/scenes/linear_transform.py" --scene-name LinearTransformDemo --quality low --still
"$root/scripts/render_manim.sh" --project-dir "$root/examples" --scene-file "$root/examples/scenes/function_story.py" --scene-name FunctionStory --quality low --still
"$root/scripts/render_manim.sh" --project-dir "$root/examples" --scene-file "$root/examples/scenes/attention_flow.py" --scene-name AttentionFlow --quality low --still
