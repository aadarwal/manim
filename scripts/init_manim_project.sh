#!/usr/bin/env bash
set -euo pipefail

project_dir="${1:-}"
[[ -n "$project_dir" ]] || {
  printf 'usage: init_manim_project.sh <project-dir>\n' >&2
  exit 2
}

mkdir -p "$project_dir/scenes" "$project_dir/assets"

if [[ ! -f "$project_dir/pyproject.toml" ]]; then
  project_name="$(basename "$project_dir" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g; s/^-+//; s/-+$//')"
  cat > "$project_dir/pyproject.toml" <<EOF
[project]
name = "${project_name:-manim-project}"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "manim>=0.20.1,<0.21",
]

[tool.uv]
package = false
EOF
fi

if [[ ! -f "$project_dir/scenes/main.py" ]]; then
  cat > "$project_dir/scenes/main.py" <<'EOF'
from manim import *


class MainScene(Scene):
    def construct(self):
        title = Text("Manim scene").to_edge(UP)
        square = Square(color=YELLOW)
        circle = Circle(color=BLUE).set_fill(BLUE, opacity=0.35)

        self.play(Write(title))
        self.play(Create(square))
        self.play(Transform(square, circle))
        self.wait()
EOF
fi

(cd "$project_dir" && uv sync)
printf 'Initialized Manim project at %s\n' "$project_dir"
