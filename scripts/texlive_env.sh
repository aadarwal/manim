#!/usr/bin/env bash

default_tinytex_bin="/Volumes/aadarwal_vx/tools/TinyTeX/bin/universal-darwin"
legacy_texlive_bin="/Volumes/aadarwal_vx/tools/texlive/2026/bin/universal-darwin"
external_texlive_bin="${MANIM_TEXLIVE_BIN:-}"

if [[ -z "$external_texlive_bin" ]]; then
  if [[ -d "$default_tinytex_bin" ]]; then
    external_texlive_bin="$default_tinytex_bin"
  else
    external_texlive_bin="$legacy_texlive_bin"
  fi
fi

if [[ -d "$external_texlive_bin" ]]; then
  case ":$PATH:" in
    *":$external_texlive_bin:"*) ;;
    *) export PATH="$external_texlive_bin:$PATH" ;;
  esac
fi
