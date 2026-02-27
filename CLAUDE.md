# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Project Overview

Calculator MCP Server — an MCP (Model Context Protocol) server that exposes 16 calculator operations as tools. Each tool delegates to the `calculator-lib-rubens` library for computation.

## Tech Stack

- **Language**: Python 3.14+
- **MCP Framework**: FastMCP (`fastmcp` package)
- **Calculator Library**: `calculator-lib-rubens` (`calculator_lib.Calculator`)
- **Config**: PyYAML loading `config.yaml`
- **Build System**: Poetry with `poetry-core` backend
- **Linting**: pylint, black, isort, mypy

## Project Structure

```
calculator-mcp/
├── config.yaml                    # Runtime config (transport, logging)
├── pyproject.toml                 # Project metadata, dependencies, tool config
├── src/calculator_mcp/
│   ├── __init__.py
│   ├── config.py                  # Loads config.yaml, configures logging
│   └── server.py                  # FastMCP server with 16 @mcp.tool functions
└── tests/
    ├── __init__.py
    └── test_server.py
```

## Common Commands

- **Install dependencies**: `poetry install`
- **Run tests**: `poetry run pytest`
- **Run tests with coverage**: `poetry run pytest --cov`
- **Lint**: `poetry run pylint src/calculator_mcp`
- **Format**: `poetry run black src tests` and `poetry run isort src tests`
- **Type check**: `poetry run mypy src/calculator_mcp`
- **Verify module loads**: `poetry run python -c "from calculator_mcp.server import mcp; print(mcp)"`

## Architecture Notes

- `config.py` loads `config.yaml` at import time and calls `logging.config.dictConfig()` to configure logging before any logger is used.
- `server.py` imports config helpers from `config.py`, which triggers logging configuration as a side effect.
- All 16 tool functions are thin synchronous wrappers that delegate to a shared `Calculator` instance from `calculator-lib-rubens`.
- Tool docstrings serve as MCP tool descriptions.

## Conventions

- Follow the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).
- Use Google-style docstrings with `Args:`, `Returns:`, and `Raises:` sections where applicable.
- All Python source files must include the AI-generated content disclaimer header comment at the top.
- Use `logging.getLogger(__name__)` for per-module loggers.
- Tool functions log at INFO level on entry.
- Keep tool functions minimal — business logic lives in the `calculator-lib-rubens` library.
