# Source Survey

This repo is the canonical agent-facing workbench. The projects below are references and inspirations, not vendored dependencies.

## Main Manim Lines

- Manim Community Edition: https://github.com/ManimCommunity/manim
  - Use for new projects.
  - Package: `manim`
  - Import style: `from manim import *`
  - Docs: https://docs.manim.community/
  - Local source clone used during setup: `/Users/aadarwal/code/repos/manim-community-source`

- ManimGL: https://github.com/3b1b/manim
  - Grant Sanderson's current 3Blue1Brown engine line.
  - Package: `manimgl`
  - Import style: `from manimlib import *`
  - Local source clone: `/Users/aadarwal/code/repos/manimgl`

- 3Blue1Brown video scenes: https://github.com/3b1b/videos
  - Real production scene code.
  - License: CC BY-NC-SA 4.0.
  - Many older scenes do not run unchanged on current Manim.
  - Local source clone: `/Users/aadarwal/code/repos/3b1b-videos`

## Agent And MCP Prior Art

- `abhiemj/manim-mcp-server`: https://github.com/abhiemj/manim-mcp-server
  - Largest Manim MCP server found during setup.
  - Core idea: accept Manim code and return rendered media.
  - This repo includes a rewritten local MCP server in `mcp/manim_server.py`.

- `fawxai/manim-plugin`: https://github.com/fawxai/manim-plugin
  - Existing Codex plugin prior art.
  - Useful as confirmation that a skill-first plugin layout is reasonable.
  - Local source clone: `/Users/aadarwal/code/repos/manim-codex-plugin-prior-art`

Other smaller MCP repos found include `wstcpyt/manim-mcp`, `paulnegz/manim-mcp`, and several Claude/Desktop-oriented variants.

## Native Manim Plugin Ecosystem

Manim CE plugins are Python packages exposed through the `manim.plugins` entry point group. They are different from Codex plugins and MCP servers.

Examples found during setup:

- `ManimCommunity/manim-voiceover`: voiceover timing and narration
- `drageelr/manim-data-structures`: data-structure visuals
- `F4bbi/manim-dsa`: data structures and algorithms
- `UnMolDeQuimica/manim-Chemistry`: chemistry diagrams and animations
- `TheMathematicFanatic/MF_Algebra`: algebra expression transforms
- `foxnewsnetwork/manim-sequence-diagram`: UML sequence diagrams
- `abul4fia/manim-play-timeline`: timeline orchestration
- `codevardhan/manim-chess-plugin`: chessboards

See also:

- https://docs.manim.community/en/stable/plugins.html
- https://www.manim.community/plugin/

## Bootstrap Sources

To clone source references without creating forks:

```bash
./scripts/bootstrap_sources.sh
```

This populates `.manim-sources/` with upstream repositories for inspection.
