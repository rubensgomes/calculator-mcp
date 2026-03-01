# Release Plan v0.2.8

**Date**: 2026-03-01

## Summary

Dependency and tooling maintenance release: moves `isort`, `mypy`, `pylint`,
and `pytest` from Poetry dev dependencies to standalone `pipx` installs, adds
`poethepoet` task runner with a `clean` task, bumps the `poetry-core` build
requirement, and updates `SETUP.md` documentation.

## Checklist

- [x] Run `poetry run mypy src/` and fix any issues
- [x] Run `poetry run isort src/ tests/` and fix any issues
- [x] Run `poetry run black src/ tests/` and fix any issues
- [x] Run `poetry run pytest` and fix any issues
- [x] Run `export SOURCE_DATE_EPOCH=$(date +%s); poetry build -v` and fix any issues
- [x] Ensure `CHANGELOG.md` exists in the project root
- [x] Update `CHANGELOG.md` with the current release changes
- [x] Bump version to 0.2.8
- [x] Commit all changes, create tag `v0.2.8`, push, and create GitHub release
