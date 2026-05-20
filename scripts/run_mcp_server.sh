#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"

# shellcheck source=texlive_env.sh
source "$root/scripts/texlive_env.sh"

if [[ ! -d ".venv" ]]; then
  uv sync
fi

export MANIM_OUTPUT_DIR="${MANIM_OUTPUT_DIR:-$root/.manim-media}"
uv run python mcp/manim_server.py
