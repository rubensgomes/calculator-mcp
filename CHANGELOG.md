# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.9] - 2026-03-01

### Changed

- Moved `mypy` back from standalone `pipx` install to Poetry dev dependency
- Restructured `poethepoet` clean task into individual subtasks with a sequence combiner
- Added `pylint` step to the release-plan slash command
- Removed `mypy` from `SETUP.md` prerequisites and `pipx` install/upgrade lists
- Added `mypy` to `SETUP.md` dev dependencies section
- Suppressed `unused-argument` pylint warning on `health_check` route handler

## [0.2.8] - 2026-03-01

### Changed

- Moved `isort`, `mypy`, `pylint`, and `pytest` from Poetry dev dependencies to standalone `pipx` installs
- Reverted `poetry-core` build requirement from `>=2.3.2` to `>=2.3.1` (latest available)
- Alphabetized prerequisites and sorted remaining dev dependencies in `pyproject.toml`
- Updated `SETUP.md` prerequisites list and install instructions to include `isort`, `mypy`, and `poethepoet`

### Added

- `poethepoet` task runner with a `clean` task in `pyproject.toml`

### Removed

- `isort`, `mypy`, `pylint`, `pytest`, and `pipx` from Poetry dev dependency group

## [0.2.7] - 2026-02-27

### Added

- `instructions` parameter on the FastMCP constructor describing all 16 tools
- `/health` custom HTTP route returning plain-text `OK` with logging
- `get_url()` config helper to read `client.url` from `config.yaml`
- `client` section in `config.yaml` with the client URL for HTTP transport
- Health check call (`_check_health()`) as the first step in `run_client()` for HTTP transport
- `test_health_check` integration test using `httpx.ASGITransport`
- "Running the Client" section in `README.md` with usage instructions

### Changed

- Replaced manual URL construction in `client.py` with `get_url()` from config
- Replaced custom `_shutdown_handler` / `sys.exit(0)` in `main.py` with `try/except KeyboardInterrupt`, letting FastMCP handle its own signal cleanup

### Removed

- `_shutdown_handler()` function and `signal`, `sys`, `types` imports from `main.py`

## [0.2.6] - 2026-02-26

### Changed

- Adopted the Google Python Style Guide across the codebase
- Converted all docstrings to Google format with `Args:`, `Returns:`, and `Raises:` sections
- Added module docstrings to `__init__.py`, `tests/__init__.py`, and `tests/test_server.py`
- Added type annotations to `_shutdown_handler()` and `main()` in `main.py`
- Wrapped `asyncio.run(main())` in `todo.py` with `if __name__ == "__main__":` guard
- Fixed long lines in `tests/__init__.py` and `tests/test_server.py`
- Added Google Python Style Guide reference to `README.md` and `CLAUDE.md`
- Configured `[tool.black]` and `[tool.isort]` in `pyproject.toml` with `line-length = 80` to match pylint

## [0.2.5] - 2026-02-24

### Added

- `client.py` MCP client module with `create_client()`, `run_client()`, and `main()` entry point
- Config-driven transport selection (HTTP or stdio) reusing the server config section
- Sample tool invocation for all 16 tools with result printing
- Client-side debug loggers in `config.yaml`: `mcp.client.streamable_http`, `httpx`, `httpcore`
- Server-side debug loggers in `config.yaml`: `mcp.server.lowlevel.server`, `mcp.server.streamable_http`, `mcp.server.streamable_http_manager`, `uvicorn.access`

### Removed

- Root-level `config.yaml` (replaced by bundled `src/calculator_mcp/config.yaml`)

## [0.2.4] - 2026-02-24

### Added

- `main.py` module with signal handling and server startup logic
- Bundled `config.yaml` inside the package for reliable deployed resolution
- `CALCULATOR_MCP_CONFIG` environment variable to override the default config path

### Changed

- Refactored `server.py` to contain only FastMCP instance and tool definitions
- Updated `__main__.py` and console script entry point to use `main:main`
- Config resolution uses `importlib.resources` with env var fallback
- Added explicit `encoding="utf-8"` to `open()` call in `config.py` (PEP 8)
- Removed trailing blank lines from `server.py` (PEP 8)
- Updated README with server running instructions and config documentation

## [0.2.3] - 2026-02-24

### Added

- Signal handler for graceful shutdown (SIGINT/SIGTERM) with logging in `server.py`
- `__main__.py` module entry point for `python -m calculator_mcp` invocation
- Console script `calculator-mcp` entry point in `pyproject.toml`
- "Install and Run the Server" section in `README.md`

## [0.2.2] - 2026-02-23

### Changed

- Broadened Python version requirement from `>=3.14` to `>=3.10.0`
- Bumped `calculator-lib-rubens` minimum version from `0.1.2` to `0.1.4`
- Changed default MCP transport in `config.yaml` from `stdio` to `http`
- Updated `poetry.lock`

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
