# Calculator MCP Server

An MCP (Model Context Protocol) server that exposes calculator operations as
tools. Each tool delegates computation to the `calculator-lib-rubens` library.

## Features

16 calculator tools available via MCP:

**Two-operand operations**: `add`, `subtract`, `multiply`, `divide`, `power`,
`nth_root`, `modulo`, `floor_divide`

**Single-operand operations**: `sqrt`, `absolute`, `floor`, `ceil`, `log10`,
`ln`, `exp`

**Rounding**: `round_number` (with configurable decimal places)

## Prerequisites

- Python 3.14+
- [Poetry](https://python-poetry.org/) for dependency management

## Installation

```bash
poetry install
```

## Configuration

The server ships with a default `config.yaml` bundled inside the package.
To override it, set the `CALCULATOR_MCP_CONFIG` environment variable to
the absolute path of your custom configuration file:

```bash
export CALCULATOR_MCP_CONFIG=/path/to/your/config.yaml
```

When `CALCULATOR_MCP_CONFIG` is not set, the bundled default is used
automatically.

The configuration file has two sections:

```yaml
server:
  transport: "stdio"    # "stdio" or "http"
  host: "127.0.0.1"     # Host for HTTP transport
  port: 9000            # Port for HTTP transport
  timeout: 10           # Tool execution timeout in seconds
```

The `logging` section controls Python logging via `dictConfig`.
The default configuration logs `calculator_mcp` messages at `INFO` level to
stderr.

## Running the Server

There are three ways to start the server:

**Console script** (installed by Poetry):

```bash
calculator-mcp
```

**As a Python module:**

```bash
python -m calculator_mcp
```

**With a custom configuration:**

```bash
export CALCULATOR_MCP_CONFIG=/path/to/your/config.yaml
calculator-mcp
```

## Style Guide

This project follows the
[Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).
All docstrings use the Google format with `Args:`, `Returns:`, and `Raises:`
sections where applicable. Compliance is enforced via pylint, black, isort,
and mypy.

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
├── pyproject.toml                 # Project metadata, dependencies, tool config
├── src/calculator_mcp/
│   ├── __init__.py
│   ├── __main__.py                # python -m calculator_mcp entry point
│   ├── config.py                  # Loads config.yaml, configures logging
│   ├── config.yaml                # Bundled default runtime config
│   ├── main.py                    # CLI entry point, signal handling
│   └── server.py                  # FastMCP server with 16 @mcp.tool functions
└── tests/
    ├── __init__.py
    └── test_server.py
```

## License

See [LICENSE](LICENSE) for details.
