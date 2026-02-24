# Release Plan — v0.2.3

**Date**: 2026-02-24
**Repository**: [rubensgomes/calculator-mcp](https://github.com/rubensgomes/calculator-mcp)

## Summary

Patch release adding graceful shutdown signal handling, a `__main__.py` module
entry point, a CLI console script (`calculator-mcp`), and README documentation
for installing and running the server.

## Release Checklist

- [x] Run `poetry run mypy src/` and fix any issues
- [x] Run `poetry run isort src/ tests/` and fix any issues
- [x] Run `poetry run black src/ tests/` and fix any issues
- [x] Run `poetry run pytest` and fix any issues
- [x] Run `export SOURCE_DATE_EPOCH=$(date +%s); poetry build -v` and fix any issues
- [x] Ensure `CHANGELOG.md` exists and is up to date
- [x] Update `CHANGELOG.md` with v0.2.3 release changes
- [x] Bump version in `pyproject.toml` to `0.2.3`
- [ ] Commit all changes to main, create tag `v0.2.3`, push, and create GitHub release

## Changes in This Release

### Added

- Signal handler for graceful shutdown (SIGINT/SIGTERM) with logging in `server.py`
- `__main__.py` module entry point for `python -m calculator_mcp` invocation
- Console script `calculator-mcp` entry point in `pyproject.toml`
- "Install and Run the Server" section in `README.md`
