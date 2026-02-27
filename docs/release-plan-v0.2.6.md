# Release Plan — v0.2.6

**Date**: 2026-02-26
**Repository**: [rubensgomes/calculator-mcp](https://github.com/rubensgomes/calculator-mcp)

## Summary

Patch release adopting the Google Python Style Guide across the codebase:
converted all docstrings to Google format with `Args:`, `Returns:`, and
`Raises:` sections; added module docstrings to `__init__.py` and test files;
added type annotations to `main.py` signal handler; wrapped `asyncio.run()` in
`todo.py` with a `__main__` guard; fixed long lines in test files; documented
the style guide in README.md and CLAUDE.md.

## Release Checklist

- [x] Run `poetry run mypy src/` and fix any issues
- [x] Run `poetry run isort src/ tests/` and fix any issues
- [x] Run `poetry run black src/ tests/` and fix any issues
- [x] Run `poetry run pytest` and fix any issues
- [x] Run `export SOURCE_DATE_EPOCH=$(date +%s); poetry build -v` and fix any issues
- [x] Ensure `CHANGELOG.md` exists and is up to date
- [x] Update `CHANGELOG.md` with v0.2.6 release changes
- [x] Bump version in `pyproject.toml` to `0.2.6`
- [x] Commit all changes to main, create tag `v0.2.6`, push, and create GitHub release

## Changes in This Release

### Changed

- Converted all docstrings to Google Python Style Guide format with `Args:`, `Returns:`, and `Raises:` sections
- Added module docstrings to `__init__.py`, `tests/__init__.py`, and `tests/test_server.py`
- Added type annotations to `_shutdown_handler()` and `main()` in `main.py`
- Wrapped `asyncio.run(main())` in `todo.py` with `if __name__ == "__main__":` guard
- Fixed long lines in `tests/__init__.py` and `tests/test_server.py`
- Added Google Python Style Guide reference to README.md and CLAUDE.md conventions
- Configured `[tool.black]` and `[tool.isort]` in `pyproject.toml` with `line-length = 80` to match pylint
