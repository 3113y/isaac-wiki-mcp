# isaac-wiki-mcp

MCP server providing **wiki-style full-text search** over The Binding of Isaac: Repentance modding API documentation.

Built with an llmwiki architecture — file-system-native markdown pages with `[[wikilinks]]` cross-references. Zero ML dependencies, pure Python.

## Why

When vibecoding Isaac mods, LLMs hallucinate API method names and signatures. This gives them a structured, searchable knowledge base of all 72 classes and 1,554 methods — returning **complete class pages** (not fragmented chunks) so the model has full context.

## Quick Start

```bash
pip install isaac-wiki-mcp
```

Add to your Claude Code MCP config (`~/.claude/mcp.json`):

```json
{
  "mcpServers": {
    "isaac-wiki": {
      "command": "uvx",
      "args": ["isaac-wiki-mcp"]
    }
  }
}
```

Or with Docker:

```json
{
  "mcpServers": {
    "isaac-wiki": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "ghcr.io/USER/isaac-wiki-mcp"]
    }
  }
}
```

## Tools

| Tool | Description |
|------|-------------|
| `wiki_search` | Full-text search across all wiki pages. Returns complete page content. |
| `wiki_read` | Read a full class page by name (e.g. `EntityPlayer`). |
| `wiki_list` | List pages by category (`classes`, `enums`, `tutorials`). |
| `wiki_stats` | Page counts, method counts, categories. |

## CLI

```bash
isaac-wiki search "player health" --category classes
isaac-wiki read EntityPlayer
isaac-wiki list --category classes
isaac-wiki stats
isaac-wiki build          # rebuild wiki from data sources
```

## Data

| Category | Count |
|----------|-------|
| Classes | 71 |
| Methods | 1,554 |
| Enums | 81 |
| Tutorials | 20 |
| Total pages | 173 |

Each class page includes: summary, inheritance chain, related types with `[[wikilinks]]`, all methods with cleaned signatures, DLC compatibility badges, and use cases.

## Architecture

```
src/isaac_wiki/
  wiki_builder.py   — data conversion (JSON → wiki markdown + cleaning)
  wiki_engine.py    — full-text search + page retrieval (pure Python)
  facade.py         — JSON-safe public API
  server.py         — MCP stdio server (4 tools)
  cli.py            — CLI

wiki/               — generated markdown pages (~1.3 MB)
  classes/          — 71 class pages with [[wikilinks]]
  enums/            — 81 enum reference pages
  tutorials/        — 20 how-to guides
  index.md          — global navigation
  llms.txt          — AI-consumable summary

data/               — source JSON (input for wiki_builder)
```

## Dev

```bash
pip install -e ".[dev]"
pytest tests/ -v
```
