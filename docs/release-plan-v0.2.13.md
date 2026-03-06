# Release Plan — v0.2.13

## Summary

Remove `_check_health` from client, update documentation (README.md, llms.txt,
CLAUDE.md) to reflect current project state including OAuth support, client
module, and corrected config references.

## Changes

- Removed `_check_health()` function and its call from `client.py`
- Removed unused `httpx` import from `client.py`
- Fixed `"httpd"` typo to `"http"` in README.md config example
- Added `client` config section to README.md configuration example
- Added `client.py` to project structure in README.md and CLAUDE.md
- Updated client description in README.md (removed health check mention)
- Updated llms.txt: fixed config path, added client config entries, added
  `client.py` to key files, added `py-key-value-aio[disk]` dependency
- Updated CLAUDE.md: added OAuth storage to tech stack, added `__main__.py`
  and `main.py` to project structure, added architecture notes for client
  and main modules

## Checklist

- [x] Run `poetry run mypy src/` and fix any issues
- [x] Run `poetry run isort src/ tests/` and fix any issues
- [x] Run `poetry run black src/ tests/` and fix any issues
- [x] Run `poetry run pylint src/ tests/` and fix any issues
- [x] Run `poetry run pytest` and fix any issues
- [x] Run `export SOURCE_DATE_EPOCH=$(date +%s); poetry build -v` and fix any issues
- [x] Ensure `CHANGELOG.md` exists
- [x] Update `CHANGELOG.md` with current release changes
- [ ] Commit all changes, create version tag, push, and create GitHub release
