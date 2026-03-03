# Release Plan v0.2.11

**Date**: 2026-03-03

## Summary

Add OAuth support to the MCP client with encrypted token storage, update the
MCP server URL to the hosted FastMCP endpoint, document ZScaler certificate
workarounds, and add the `py-key-value-aio[disk]` dependency.

## Changes

### Added

- OAuth support in `client.py` via `fastmcp.client.auth.OAuth` with encrypted disk-based token storage (`py-key-value-aio[disk]`, `cryptography`)
- `is_oauth()` config helper in `config.py` to read `client.is_oauth` from `config.yaml`
- `is_oauth` and `url` client settings in `config.yaml` for the hosted FastMCP endpoint
- ZScaler certificate troubleshooting section in `SETUP.md`
- `py-key-value-aio[disk]` project dependency in `pyproject.toml`

### Changed

- `.mcp.json` server URL updated to `https://rubens-calculator-mcp.fastmcp.app/mcp`
- `client.py`: moved health check inside the `async with client:` block, added `client.ping()` before tool calls
- `config.yaml`: default logging level for `calculator_mcp` changed from INFO to DEBUG

## Checklist

- [x] Run `poetry run mypy src/` and fix any issues
- [x] Run `poetry run isort src/ tests/` and fix any issues
- [x] Run `poetry run black src/ tests/` and fix any issues
- [x] Run `poetry run pylint src/ tests/` and fix any issues
- [x] Run `poetry run pytest` and fix any issues
- [x] Run `export SOURCE_DATE_EPOCH=$(date +%s); poetry build -v` and fix any issues
- [x] Ensure `CHANGELOG.md` exists in the project root
- [x] Update `CHANGELOG.md` with the current release changes
- [x] Bump version to 0.2.11
- [ ] Commit all changes, create tag `v0.2.11`, push, and create GitHub release
