# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.1] - 2026-02-20

### Changed

- Expanded `.gitignore` with comprehensive ignore rules for Claude Code, Python, Jupyter, testing, packaging, and OS-specific files
- Fixed typo in `LICENSE` (missing period after "security vulnerabilities")
- Capitalized "Limitation of Liability" heading in `LICENSE`
- Streamlined `RELEASE.md` to reference the Claude Code slash command instead of inline command listings
- Expanded `SETUP.md` with full development environment setup instructions (pyenv, python, pipx, poetry)
- Updated `poetry.lock`

## [0.2.0] - 2026-02-18

### Changed

- Replaced httpx REST API proxy with direct `calculator-lib-rubens` library calls
- Converted all 16 tool functions from async to synchronous
- Changed `openWorldHint` annotation from `True` to `False` (no external HTTP calls)
- Updated tool docstrings to reference `ValueError` instead of HTTP errors
- Updated `CLAUDE.md`, `README.md`, `llms.txt` to reflect new architecture
- Simplified `config.yaml` (removed `calculator_api.base_url`)
- Simplified tests to call real library functions instead of mocking httpx

### Removed

- `openapi.yaml` (no longer proxying to a REST API)
- `httpx` dependency
- `_post()` async helper function in `server.py`
- `get_base_url()` function in `config.py`

### Added

- `calculator-lib-rubens` as a project dependency
- `LICENSE` file
- `tests/test_server.py` with 17 tests

## [0.1.0] - 2026-02-15

### Added

- FastMCP server with 16 calculator tool operations
- Async HTTP client (`httpx`) for proxying requests to upstream Calculator REST API
- Configuration via `config.yaml` with logging support
- Poetry-based build system with `poetry-core` backend
- OpenAPI specification for the upstream Calculator REST API
- Project documentation (README, SETUP, CLAUDE.md)
- Dev tooling: pylint, black, isort, mypy, pytest with coverage
