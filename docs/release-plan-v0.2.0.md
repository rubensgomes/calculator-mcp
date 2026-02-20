# Release Plan — v0.2.0

**Date**: 2026-02-18
**Repository**: [rubensgomes/calculator-mcp](https://github.com/rubensgomes/calculator-mcp)

## Summary

Replace the httpx-based REST API proxy architecture with direct delegation to
the `calculator-lib-rubens` library. This eliminates the runtime dependency on
an external Calculator REST API, removes `httpx` and `openapi.yaml`, and
converts all 16 tool functions from async to synchronous.

## Release Checklist

- [x] Run `poetry run mypy src/` and fix any issues
- [x] Run `poetry run isort src/ tests/` and fix any issues
- [x] Run `poetry run black src/ tests/` and fix any issues
- [x] Run `poetry run pytest` and fix any issues
- [x] Run `export SOURCE_DATE_EPOCH=$(date +%s); poetry build -v` and fix any issues
- [x] Ensure `CHANGELOG.md` exists and is up to date
- [x] Update `CHANGELOG.md` with v0.2.0 release changes
- [x] Bump version in `pyproject.toml` to `0.2.0`
- [x] Commit all changes to main, create tag `v0.2.0`, push, and create GitHub release

## Changes in This Release

### Changed

- Replaced httpx REST API proxy with direct `calculator-lib-rubens` library calls
- Converted all 16 tool functions from async to synchronous
- Changed `openWorldHint` annotation from `True` to `False` (no external HTTP calls)
- Updated tool docstrings to reference `ValueError` instead of HTTP errors
- Updated `CLAUDE.md`, `README.md`, `llms.txt` to reflect new architecture
- Simplified `config.yaml` (removed `calculator_api.base_url`)
- Simplified tests to call real library functions instead of mocking httpx

### Removed

- `openapi.yaml` (no longer proxying to a REST API)
- `httpx` dependency
- `_post()` async helper function in `server.py`
- `get_base_url()` function in `config.py`

### Added

- `calculator-lib-rubens` as a project dependency
- `LICENSE` file
- `tests/test_server.py` with 17 tests
