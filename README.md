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
    transport: "http"     # "stdio" or "http"
    host: "127.0.0.1"     # Host for HTTP transport
    port: 9000            # Port for HTTP transport
    timeout: 10           # Tool execution timeout in seconds

client:
    is_oauth: false                        # Enable OAuth authentication
    url: "http://127.0.0.1:9000/mcp"       # Server URL for HTTP transport
    token_dir: "/home/user/.fastmcp"       # OAuth token storage directory
    callback_port: 10000                   # OAuth callback server port
```

The `logging` section controls Python logging via `dictConfig`.
The default configuration logs `calculator_mcp` messages at `INFO` level to
stderr.

## Running the Server

There are three ways to start the server:

**Console script** (installed by Poetry):

```bash
# requires poetry to be installed
poetry install # only needed once
poetry run calculator-mcp
```

**As a Python module:**

```bash
# requires poetry to be installed
poetry install # only needed once
eval $(poetry env activate)
python -m calculator_mcp
deactivate
```

**With a custom configuration:**

```bash
# requires poetry to be installed
poetry install # only needed once
export CALCULATOR_MCP_CONFIG=/path/to/your/config.yaml
poetry run calculator-mcp
```

## Running the Client

A sample integration test client is provided in `tests/integration/client.py`
to demonstrate the MCP protocol with the server. It lists all available tools
and calls each one with sample arguments.

**Important:** The server must be running before you start the client. See
[Running the Server](#running-the-server) above.

**Run the client:**

```bash
# requires poetry to be installed
poetry install # only needed once
eval $(poetry env activate)
python tests/integration/client.py
deactivate
```

## Add MCP Server to Claude Code

- Add the MCP server to Claude Code using project scope. The file `.mcp.json` is
  added to the project root folder:

    ```bash
    # It is assumed that the MCP server is running on http://127.0.0.1:9000
    cd $(git rev-parse --show-toplevel) || exit
    claude mcp add \
        --scope project \
        --transport http \
        calculator-mcp http://127.0.0.1:9000/mcp
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
    ├── test_config.py             # Unit tests for config module
    ├── test_main.py               # Unit tests for main module
    ├── test_server.py             # Integration tests via MCP Client
    ├── test_tools.py              # Unit tests for tool functions
    └── integration/
        ├── __init__.py
        └── client.py              # Sample MCP client with OAuth support
```

## License

See [LICENSE](LICENSE) for details.
