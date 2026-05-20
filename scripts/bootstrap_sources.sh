#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
sources="$root/.manim-sources"
mkdir -p "$sources"

clone_or_update() {
  local url="$1"
  local dir="$2"
  if [[ -d "$sources/$dir/.git" ]]; then
    git -C "$sources/$dir" fetch --all --prune
  else
    git clone "$url" "$sources/$dir"
  fi
}

clone_or_update https://github.com/ManimCommunity/manim.git manim-community
clone_or_update https://github.com/3b1b/manim.git manimgl
clone_or_update https://github.com/3b1b/videos.git 3b1b-videos
clone_or_update https://github.com/abhiemj/manim-mcp-server.git manim-mcp-server
clone_or_update https://github.com/fawxai/manim-plugin.git codex-manim-plugin-prior-art

printf 'Sources are under %s\n' "$sources"
