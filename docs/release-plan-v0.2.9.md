# Release Plan v0.2.9

**Date**: 2026-03-01

## Summary

Minor maintenance release: moves `mypy` back from standalone `pipx` install to
Poetry dev dependency, restructures `poethepoet` clean task into individual
subtasks with a sequence combiner, adds `pylint` step to the release-plan
command, and updates `SETUP.md` accordingly.

## Checklist

- [x] Run `poetry run mypy src/` and fix any issues
- [x] Run `poetry run isort src/ tests/` and fix any issues
- [x] Run `poetry run black src/ tests/` and fix any issues
- [x] Run `poetry run pylint src/ tests/` and fix any issues
- [x] Run `poetry run pytest` and fix any issues
- [x] Run `export SOURCE_DATE_EPOCH=$(date +%s); poetry build -v` and fix any issues
- [x] Ensure `CHANGELOG.md` exists in the project root
- [x] Update `CHANGELOG.md` with the current release changes
- [x] Bump version to 0.2.9
- [ ] Commit all changes, create tag `v0.2.9`, push, and create GitHub release
