# Release Plan: calculator-mcp v0.1.0

**Repository:** `rubensgomes/calculator-mcp`
**Version:** 0.1.0 (initial release)
**Date:** 2026-02-15
**Branch:** main

## Summary

This is the initial release of the Calculator MCP Server, providing 16 calculator
operations exposed as MCP tools that proxy requests to a Calculator REST API over HTTP.

## Pre-Release Checklist

- [x] **Step 1** — Run `poetry run mypy src/` and fix any issues
- [x] **Step 2** — Run `poetry run isort src/ tests/` and fix any issues
- [x] **Step 3** — Run `poetry run black src/ tests/` and fix any issues
- [x] **Step 4** — Run `poetry run pytest` and fix any issues
- [x] **Step 5** — Commit any uncommitted changes
- [x] **Step 6** — Update CHANGELOG.md with v0.1.0 release notes
- [x] **Step 7** — Save this release plan to `docs/` folder
- [ ] **Step 8** — Commit all release changes
- [ ] **Step 9** — Tag release as `v0.1.0`
- [ ] **Step 10** — Push to remote (commits + tag)

## Release Contents (v0.1.0 — Initial Release)

### Added

- FastMCP server with 16 calculator tool operations
- Async HTTP client (`httpx`) for proxying requests to upstream Calculator REST API
- Configuration via `config.yaml` with logging support
- Poetry-based build system with `poetry-core` backend
- OpenAPI specification for the upstream Calculator REST API
- Project documentation (README, SETUP, CLAUDE.md)
- Dev tooling: pylint, black, isort, mypy, pytest with coverage
