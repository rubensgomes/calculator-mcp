# Release Plan — v0.2.7

**Date**: 2026-02-27
**Repository**: rubensgomes/calculator-mcp

## Summary of Changes

- Added `instructions` parameter to the FastMCP constructor describing all 16 tools
- Added `/health` custom HTTP route with logging and docstring
- Added `Request` and `PlainTextResponse` imports from Starlette in `server.py`
- Added `get_url()` config helper to read `client.url` from `config.yaml`
- Added `client` section to `config.yaml` with the client URL
- Replaced manual URL construction in `client.py` with `get_url()`
- Added health check call (`_check_health()`) as the first step in `run_client()` for HTTP transport
- Replaced custom `_shutdown_handler` with `try/except KeyboardInterrupt` in `main.py`, letting FastMCP handle its own signal cleanup
- Added `test_health_check` integration test using `httpx.ASGITransport`
- Updated README "Running the Client" section with usage instructions

## Release Checklist

- [x] Run `poetry run mypy src/` and fix any issues
- [x] Run `poetry run isort src/ tests/` and fix any issues
- [x] Run `poetry run black src/ tests/` and fix any issues
- [x] Run `poetry run pytest` and fix any issues
- [x] Run `export SOURCE_DATE_EPOCH=$(date +%s); poetry build -v` and fix any issues
- [x] Ensure `CHANGELOG.md` exists and update it with v0.2.7 changes
- [ ] Commit all changes to main, create tag `v0.2.7`, push, and create GitHub release
