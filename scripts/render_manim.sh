#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Render a Manim scene with this plugin's environment.

Usage:
  render_manim.sh --project-dir DIR --scene-file FILE --scene-name NAME [options]

Options:
  --quality VALUE    low | medium | high | production | 4k
  --still            Render a still frame with -s
  --open             Open output after render with -p
  --renderer VALUE   cairo | opengl
  --                 Pass remaining args to Manim
EOF
}

fail() {
  printf 'error: %s\n' "$*" >&2
  exit 1
}

quality_flag() {
  case "$1" in
    low|l|-ql) printf '%s\n' "-ql" ;;
    medium|m|-qm) printf '%s\n' "-qm" ;;
    high|h|-qh) printf '%s\n' "-qh" ;;
    production|p|-qp) printf '%s\n' "-qp" ;;
    4k|k|-qk) printf '%s\n' "-qk" ;;
    *) fail "unknown quality: $1" ;;
  esac
}

plugin_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
project_dir=""
scene_file=""
scene_name=""
quality="low"
still=0
open_after=0
renderer=""
extra_args=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --project-dir) project_dir="${2:-}"; shift 2 ;;
    --scene-file) scene_file="${2:-}"; shift 2 ;;
    --scene-name) scene_name="${2:-}"; shift 2 ;;
    --quality) quality="${2:-}"; shift 2 ;;
    --still) still=1; shift ;;
    --open) open_after=1; shift ;;
    --renderer) renderer="${2:-}"; shift 2 ;;
    --) shift; extra_args+=("$@"); break ;;
    -h|--help) usage; exit 0 ;;
    *) fail "unknown argument: $1" ;;
  esac
done

[[ -n "$project_dir" ]] || fail "--project-dir is required"
[[ -n "$scene_file" ]] || fail "--scene-file is required"
[[ -n "$scene_name" ]] || fail "--scene-name is required"

project_dir="$(cd "$project_dir" && pwd)"
if [[ "$scene_file" != /* ]]; then
  scene_file="$(cd "$(dirname "$scene_file")" && pwd)/$(basename "$scene_file")"
fi
[[ -f "$scene_file" ]] || fail "scene file not found: $scene_file"

if [[ -n "${MANIM_EXECUTABLE:-}" ]]; then
  manim_cmd=("$MANIM_EXECUTABLE")
else
  if [[ ! -x "$plugin_root/.venv/bin/manim" ]]; then
    (cd "$plugin_root" && uv sync)
  fi
  manim_cmd=("$plugin_root/.venv/bin/manim")
fi

cmd=("${manim_cmd[@]}" "$(quality_flag "$quality")")
if [[ "$still" -eq 1 ]]; then
  cmd+=("-s")
fi
if [[ "$open_after" -eq 1 ]]; then
  cmd+=("-p")
fi
if [[ -n "$renderer" ]]; then
  cmd+=(--renderer "$renderer")
fi
cmd+=("$scene_file" "$scene_name")
if [[ "${#extra_args[@]}" -gt 0 ]]; then
  cmd+=("${extra_args[@]}")
fi

(cd "$project_dir" && "${cmd[@]}")

"$plugin_root/scripts/find_outputs.sh" "$project_dir" "$scene_name"
