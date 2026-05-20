# MCP Server

This repo includes a local MCP server at `mcp/manim_server.py`.

It exposes:

- `execute_manim_code(manim_code, scene_name="", quality="low", still=false)`
- `cleanup_manim_temp_dir(directory)`

The server writes generated media under `.manim-media/` by default and returns concrete artifact paths.

## Run

```bash
uv sync
./scripts/run_mcp_server.sh
```

With an explicit Manim executable:

```bash
MANIM_EXECUTABLE=/path/to/manim ./scripts/run_mcp_server.sh
```

If `MANIM_EXECUTABLE` is not set, the server uses `uv run manim`.

## Claude Desktop-Style Config

Adjust the absolute paths:

```json
{
  "mcpServers": {
    "manim-renderer": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/aadarwal/code/repos/Manim",
        "run",
        "python",
        "mcp/manim_server.py"
      ],
      "env": {
        "MANIM_OUTPUT_DIR": "/Users/aadarwal/code/repos/Manim/.manim-media"
      }
    }
  }
}
```

## Notes

- Use `still=true` for fast layout checks.
- Provide `scene_name` when the code contains multiple scenes.
- Generated partial movie files are filtered out of the returned artifact list.
- The server does not execute untrusted code safely. Treat Manim code as local code execution.
