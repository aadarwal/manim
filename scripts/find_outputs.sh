#!/usr/bin/env bash
set -euo pipefail

project_dir="${1:-.}"
scene_name="${2:-}"

project_dir="$(cd "$project_dir" && pwd)"

if [[ ! -d "$project_dir/media" ]]; then
  printf 'No media directory found under %s\n' "$project_dir"
  exit 0
fi

if [[ -n "$scene_name" ]]; then
  find "$project_dir/media" -type f \( -name "${scene_name}*.mp4" -o -name "${scene_name}*.png" -o -name "${scene_name}*.gif" -o -name "${scene_name}*.webm" \) | sort
else
  find "$project_dir/media" -type f \( -name '*.mp4' -o -name '*.png' -o -name '*.gif' -o -name '*.webm' \) | sort
fi
