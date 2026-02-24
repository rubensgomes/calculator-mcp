# Release Plan — v0.2.5

**Date**: 2026-02-24
**Repository**: [rubensgomes/calculator-mcp](https://github.com/rubensgomes/calculator-mcp)

## Summary

Patch release adding an MCP client module and enhanced debug logging: new
`client.py` with config-driven transport that connects to the server, lists all
tools, and calls each with sample arguments; client config helpers in
`config.py`; configurable debug loggers in `config.yaml` for both client-side
(MCP protocol, httpx, httpcore) and server-side (JSON-RPC messages, transport,
session lifecycle, uvicorn access) tracing; removed the root-level `config.yaml`
in favor of the bundled package copy.

## Release Checklist

- [x] Run `poetry run mypy src/` and fix any issues
- [x] Run `poetry run isort src/ tests/` and fix any issues
- [x] Run `poetry run black src/ tests/` and fix any issues
- [x] Run `poetry run pytest` and fix any issues
- [x] Run `export SOURCE_DATE_EPOCH=$(date +%s); poetry build -v` and fix any issues
- [x] Ensure `CHANGELOG.md` exists and is up to date
- [x] Update `CHANGELOG.md` with v0.2.5 release changes
- [x] Bump version in `pyproject.toml` to `0.2.5`
- [x] Commit all changes to main, create tag `v0.2.5`, push, and create GitHub release

## Changes in This Release

### Added

- `client.py` MCP client module with `create_client()`, `run_client()`, and `main()` entry point
- Config-driven transport selection (HTTP or stdio) reusing the server config section
- Sample tool invocation for all 16 tools with result printing
- Client-side debug loggers: `mcp.client.streamable_http`, `httpx`, `httpcore`
- Server-side debug loggers: `mcp.server.lowlevel.server`, `mcp.server.streamable_http`, `mcp.server.streamable_http_manager`, `uvicorn.access`

### Removed

- Root-level `config.yaml` (replaced by bundled `src/calculator_mcp/config.yaml`)
