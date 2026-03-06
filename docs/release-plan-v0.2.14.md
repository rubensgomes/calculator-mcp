# Release Plan — v0.2.14

## Summary

Move `client.py` from `src/calculator_mcp/` to `tests/integration/` (integration
test client only) and add comprehensive unit tests for `config.py`, `main.py`,
and the 16 server tool functions.

### Changes

- Moved `src/calculator_mcp/client.py` to `tests/integration/client.py`
- Added `tests/integration/__init__.py`
- Added `tests/test_config.py` — 14 unit tests for all config helpers
- Added `tests/test_main.py` — 3 unit tests for CLI entry point
- Added `tests/test_tools.py` — 47 unit tests for tool functions (direct calls)
- Updated `CLAUDE.md`, `README.md`, `llms.txt` project structure and references

## Checklist

- [x] Run `poetry run mypy src/` and fix any issues
- [x] Run `poetry run isort src/ tests/` and fix any issues
- [x] Run `poetry run black src/ tests/` and fix any issues
- [x] Run `poetry run pylint src/ tests/` and fix any issues
- [x] Run `poetry run pytest` and fix any issues
- [x] Run `export SOURCE_DATE_EPOCH=$(date +%s); poetry build -v` and fix any issues
- [x] Update `CHANGELOG.md` with release changes
- [x] Commit all changes, create version tag, push, and create GitHub release
