# Release Plan — v0.2.4

**Date**: 2026-02-24
**Repository**: [rubensgomes/calculator-mcp](https://github.com/rubensgomes/calculator-mcp)

## Summary

Patch release with project restructuring and PEP 8 compliance fixes: extracted
initialization and startup logic from `server.py` into a new `main.py`, bundled
`config.yaml` inside the package with `importlib.resources` for reliable
deployment, added `CALCULATOR_MCP_CONFIG` environment variable override, fixed
PEP 8 violations (missing `encoding` parameter, trailing newlines), and updated
README documentation.

## Release Checklist

- [x] Run `poetry run mypy src/` and fix any issues
- [x] Run `poetry run isort src/ tests/` and fix any issues
- [x] Run `poetry run black src/ tests/` and fix any issues
- [x] Run `poetry run pytest` and fix any issues
- [x] Run `export SOURCE_DATE_EPOCH=$(date +%s); poetry build -v` and fix any issues
- [x] Ensure `CHANGELOG.md` exists and is up to date
- [x] Update `CHANGELOG.md` with v0.2.4 release changes
- [x] Bump version in `pyproject.toml` to `0.2.4`
- [ ] Commit all changes to main, create tag `v0.2.4`, push, and create GitHub release

## Changes in This Release

### Added

- `main.py` module with signal handling and server startup logic
- Bundled `config.yaml` inside the package for reliable deployed resolution
- `CALCULATOR_MCP_CONFIG` environment variable to override the default config path

### Changed

- Refactored `server.py` to contain only FastMCP instance and tool definitions
- Updated `__main__.py` and console script entry point to use `main:main`
- Config resolution uses `importlib.resources` with env var fallback
- Added explicit `encoding="utf-8"` to `open()` call in `config.py` (PEP 8)
- Removed trailing blank lines from `server.py` (PEP 8)
- Updated README with server running instructions and config documentation
