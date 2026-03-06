# Release Plan v0.2.12

## Summary

Fix OAuth client token exchange for hosted FastMCP endpoint, add
config-driven OAuth settings, and add OAuth troubleshooting documentation.

### Changes

- **client.py**: Use config-driven `token_dir` and `callback_port` instead of
  hardcoded values; request `client_secret_post` auth method during OAuth
  dynamic client registration to fix CloudFront proxy 401; skip health check
  for OAuth connections (hosted endpoint requires bearer token)
- **config.py**: Added `get_token_dir()` and `get_callback_port()` helpers
- **config.yaml**: Added `token_dir` and `callback_port` client settings;
  reverted debug logging levels back to production defaults
- **SETUP.md**: Added OAuth encryption key setup and WSL browser interop
  instructions
- **docs/oauth-troubleshooting.md**: New troubleshooting guide for OAuth issues

## Checklist

- [x] Run `poetry run mypy src/` and fix any issues
- [x] Run `poetry run isort src/ tests/` and fix any issues
- [x] Run `poetry run black src/ tests/` and fix any issues
- [x] Run `poetry run pylint src/ tests/` and fix any issues
- [x] Run `poetry run pytest` and fix any issues
- [x] Run `export SOURCE_DATE_EPOCH=$(date +%s); poetry build -v` and fix any issues
- [x] Ensure `CHANGELOG.md` exists and is updated
- [x] Commit all changes, create tag, push, and create GitHub release
