# Manim Plugin Ecosystem

Manim-native plugins extend Manim itself. They are not Codex plugins and not MCP servers.

The current Manim CE docs describe plugins as Python packages with an entry point group:

```toml
[project.entry-points."manim.plugins"]
"name" = "object_reference"
```

Projects enable plugins through `manim.cfg`:

```ini
[CLI]
plugins = plugin_module_name
```

or list installed plugins with:

```bash
manim plugins -l
```

## When To Pull In A Native Plugin

- Voiceover or narration timing: consider `manim-voiceover`.
- Domain-specific visuals such as chemistry, chess, or circuits: use the domain plugin if it saves real implementation time.
- Algebra transform-heavy scenes: inspect algebra plugins before hand-rolling expression matching.
- General math or proof visuals: default Manim CE is usually enough.

## Agent Rule

Do not add a dependency just because it exists. Prefer a plugin when it materially reduces fragile custom code or provides a domain-specific object model.
