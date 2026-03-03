# Release Plan v0.2.10

**Date**: 2026-03-02

## Summary

Minor maintenance release: adds `.mcp.json` project-scope MCP server
configuration for Claude Code, documents the MCP server setup in `README.md`,
adds `cookiecutter` and `uv` to `SETUP.md` prerequisites and install
instructions, removes the disclaimer header from `tests/__init__.py`, fixes
YAML indentation in the `README.md` config example, and updates `poetry.lock`.

## Checklist

- [x] Run `poetry run mypy src/` and fix any issues
- [x] Run `poetry run isort src/ tests/` and fix any issues
- [x] Run `poetry run black src/ tests/` and fix any issues
- [x] Run `poetry run pylint src/ tests/` and fix any issues
- [x] Run `poetry run pytest` and fix any issues
- [x] Run `export SOURCE_DATE_EPOCH=$(date +%s); poetry build -v` and fix any issues
- [x] Ensure `CHANGELOG.md` exists in the project root
- [x] Update `CHANGELOG.md` with the current release changes
- [x] Bump version to 0.2.10
- [ ] Commit all changes, create tag `v0.2.10`, push, and create GitHub release
