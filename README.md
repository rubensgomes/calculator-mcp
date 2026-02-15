# Calculator MCP Server

An MCP (Model Context Protocol) server that exposes calculator operations as tools. Each tool proxies requests to a Calculator REST API over HTTP.

## Features

16 calculator tools available via MCP:

**Two-operand operations**: `add`, `subtract`, `multiply`, `divide`, `power`, `nth_root`, `modulo`, `floor_divide`

**Single-operand operations**: `sqrt`, `absolute`, `floor`, `ceil`, `log10`, `ln`, `exp`

**Rounding**: `round_number` (with configurable decimal places)

## Prerequisites

- Python 3.13+
- [Poetry](https://python-poetry.org/) for dependency management
- A running instance of the Calculator REST API (see `openapi.yaml` for the API spec)

## Installation

```bash
poetry install
```

## Configuration

Edit `config.yaml` in the project root:

```yaml
calculator_api:
  base_url: "http://localhost:8000"
```

The `logging` section in `config.yaml` controls Python logging via `dictConfig`. The default configuration logs `calculator_mcp` messages at `INFO` level to stderr.

## Usage

The server can be started using the FastMCP CLI or integrated into any MCP-compatible client.

## Development

```bash
# Run tests
poetry run pytest

# Run tests with coverage
poetry run pytest --cov

# Lint
poetry run pylint src/calculator_mcp

# Format code
poetry run black src tests
poetry run isort src tests

# Type check
poetry run mypy src/calculator_mcp
```

## Project Structure

```
calculator-mcp/
├── config.yaml                    # Runtime config (API base URL, logging)
├── openapi.yaml                   # OpenAPI spec for the upstream Calculator REST API
├── pyproject.toml                 # Project metadata, dependencies, tool config
├── src/calculator_mcp/
│   ├── __init__.py
│   ├── config.py                  # Loads config.yaml, configures logging
│   └── server.py                  # FastMCP server with 16 @mcp.tool functions
└── tests/
    └── __init__.py
```

## License

See [LICENSE](LICENSE) for details.
