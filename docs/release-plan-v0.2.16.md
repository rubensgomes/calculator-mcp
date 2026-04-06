# Release Plan — v0.2.16

**Date**: 2026-04-05
**Repository**: rubensgomes/calculator-mcp

## Summary

Rename PyPI package from `calculator-mcp` to `calculator-mcp-rubens` to resolve
PyPI upload permission conflict. No functional changes.

## Checklist

- [x] Run `poetry run mypy src/` and fix any issues
- [x] Run `poetry run isort src/ tests/` and fix any issues
- [x] Run `poetry run black src/ tests/` and fix any issues
- [x] Run `poetry run pylint src/ tests/` and fix any issues
- [x] Run `poetry run pytest` and fix any issues
- [x] Run `export SOURCE_DATE_EPOCH=$(date +%s); poetry build -v` and fix any issues
- [x] Ensure `CHANGELOG.md` exists and update with current release changes
- [x] Commit all changes to main, create version tag, push, and create GitHub release
- [x] Run `poetry publish -v` as the very last step
