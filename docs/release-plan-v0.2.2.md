# Release Plan — v0.2.2

**Date**: 2026-02-23
**Repository**: [rubensgomes/calculator-mcp](https://github.com/rubensgomes/calculator-mcp)

## Summary

Patch release with configuration and compatibility updates: broadened Python
version requirement to `>=3.10.0`, bumped `calculator-lib-rubens` minimum to
`0.1.4`, switched default MCP transport to `http`, and updated `poetry.lock`.

## Release Checklist

- [x] Run `poetry run mypy src/` and fix any issues
- [x] Run `poetry run isort src/ tests/` and fix any issues
- [x] Run `poetry run black src/ tests/` and fix any issues
- [x] Run `poetry run pytest` and fix any issues
- [x] Run `export SOURCE_DATE_EPOCH=$(date +%s); poetry build -v` and fix any issues
- [x] Ensure `CHANGELOG.md` exists and is up to date
- [x] Update `CHANGELOG.md` with v0.2.2 release changes
- [x] Bump version in `pyproject.toml` to `0.2.2`
- [ ] Commit all changes to main, create tag `v0.2.2`, push, and create GitHub release

## Changes in This Release

### Changed

- Broadened Python version requirement from `>=3.14` to `>=3.10.0`
- Bumped `calculator-lib-rubens` minimum version from `0.1.2` to `0.1.4`
- Changed default MCP transport in `config.yaml` from `stdio` to `http`
- Updated `poetry.lock`
