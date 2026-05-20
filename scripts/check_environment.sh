#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=texlive_env.sh
source "$script_dir/texlive_env.sh"

missing=0

check_cmd() {
  local name="$1"
  if command -v "$name" >/dev/null 2>&1; then
    printf 'ok: %s -> %s\n' "$name" "$(command -v "$name")"
  else
    printf 'missing: %s\n' "$name"
    missing=1
  fi
}

check_pkg() {
  local name="$1"
  if command -v pkg-config >/dev/null 2>&1 && pkg-config --exists "$name"; then
    printf 'ok: pkg-config %s\n' "$name"
  else
    printf 'missing: pkg-config package %s\n' "$name"
    missing=1
  fi
}

check_cmd uv
check_cmd ffmpeg
check_cmd pkg-config
check_pkg cairo
check_pkg pangocairo

if command -v latex >/dev/null 2>&1 && command -v dvisvgm >/dev/null 2>&1; then
  printf 'ok: TeX and dvisvgm available\n'
  printf 'ok: latex -> %s\n' "$(command -v latex)"
  printf 'ok: dvisvgm -> %s\n' "$(command -v dvisvgm)"
else
  printf 'note: TeX/dvisvgm not fully available; use Text or Docker for TeX-heavy scenes\n'
fi

if [[ -x ".venv/bin/manim" ]]; then
  .venv/bin/manim --version
else
  printf 'note: local .venv/bin/manim not found; run uv sync\n'
fi

if [[ "$missing" -ne 0 ]]; then
  cat <<'EOF'

macOS install hint:
  brew install cairo pango pkgconf ffmpeg

Optional TeX support:
  brew install --cask mactex
or install a smaller TeX distribution and dvisvgm.
EOF
  exit 2
fi
