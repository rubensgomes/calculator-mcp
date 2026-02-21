# Release Plan — v0.2.1

**Date**: 2026-02-20
**Repository**: [rubensgomes/calculator-mcp](https://github.com/rubensgomes/calculator-mcp)

## Summary

Patch release with documentation and project hygiene updates: expanded
`.gitignore`, minor `LICENSE` fixes (typo, heading capitalization), streamlined
`RELEASE.md`, expanded `SETUP.md` with full development environment setup
instructions, and updated `poetry.lock`.

## Release Checklist

- [x] Run `poetry run mypy src/` and fix any issues
- [x] Run `poetry run isort src/ tests/` and fix any issues
- [x] Run `poetry run black src/ tests/` and fix any issues
- [x] Run `poetry run pytest` and fix any issues
- [x] Run `export SOURCE_DATE_EPOCH=$(date +%s); poetry build -v` and fix any issues
- [x] Ensure `CHANGELOG.md` exists and is up to date
- [x] Update `CHANGELOG.md` with v0.2.1 release changes
- [x] Bump version in `pyproject.toml` to `0.2.1`
- [x] Commit all changes to main, create tag `v0.2.1`, push, and create GitHub release

## Changes in This Release

### Changed

- Expanded `.gitignore` with comprehensive ignore rules for Claude Code, Python, Jupyter, testing, packaging, and OS-specific files
- Fixed typo in `LICENSE` (missing period after "security vulnerabilities")
- Capitalized "Limitation of Liability" heading in `LICENSE`
- Streamlined `RELEASE.md` to reference the Claude Code slash command instead of inline command listings
- Expanded `SETUP.md` with full development environment setup instructions (pyenv, python, pipx, poetry)
- Updated `poetry.lock`
