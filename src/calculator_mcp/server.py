# General Disclaimer
#
# **AI Generated Content**
#
# This project's source code and documentation were generated predominantly
# by an Artificial Intelligence Large Language Model (AI LLM). The project
# lead, [Rubens Gomes](https://rubensgomes.com), provided initial prompts,
# reviewed, and made refinements to the generated output. While human review and
# refinement have occurred, users should be aware that the output may contain
# inaccuracies, errors, or security vulnerabilities
#
# **Third-Party Content Notice**
#
# This software may include components or snippets derived from third-party
# sources. The software's users and distributors are responsible for ensuring
# compliance with any underlying licenses applicable to such components.
#
# **Copyright Status Statement**
#
# Copyright protection, if any, is limited to the original human contributions and
# modifications made to this project. The AI-generated portions of the code and
# documentation are not subject to copyright and are considered to be in the
# public domain.
#
# **Limitation of liability**
#
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR
# OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE
# OR OTHER DEALINGS IN THE SOFTWARE.
#
# **No-Warranty Disclaimer**
#
# THIS SOFTWARE IS PROVIDED 'AS IS,' WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT.

import logging
from importlib.metadata import version

from calculator_lib import Calculator
from fastmcp import FastMCP

from calculator_mcp.config import get_host, get_port, get_timeout, get_transport

logger = logging.getLogger(__name__)

_HOMEPAGE = "https://github.com/rubensgomes/calculator-mcp/"
_TIMEOUT = get_timeout()

_calc = Calculator()

mcp = FastMCP(
    "Calculator MCP Server",
    version=version("calculator-mcp"),
    website_url=_HOMEPAGE,
)
logger.info("Initialized Calculator MCP Server")


# --- Two-operand tools ---


@mcp.tool(
    timeout=_TIMEOUT,
    annotations={
        "readOnlyHint": True,
        "idempotentHint": True,
        "openWorldHint": False,
    },
)
def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    logger.info("add called with a=%s, b=%s", a, b)
    return _calc.add(a, b)


@mcp.tool(
    timeout=_TIMEOUT,
    annotations={
        "readOnlyHint": True,
        "idempotentHint": True,
        "openWorldHint": False,
    },
)
def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    logger.info("subtract called with a=%s, b=%s", a, b)
    return _calc.subtract(a, b)


@mcp.tool(
    timeout=_TIMEOUT,
    annotations={
        "readOnlyHint": True,
        "idempotentHint": True,
        "openWorldHint": False,
    },
)
def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    logger.info("multiply called with a=%s, b=%s", a, b)
    return _calc.multiply(a, b)


@mcp.tool(
    timeout=_TIMEOUT,
    annotations={
        "readOnlyHint": True,
        "idempotentHint": True,
        "openWorldHint": False,
    },
)
def divide(a: float, b: float) -> float:
    """Return the quotient of two numbers.

    Raises ValueError on division by zero.
    """
    logger.info("divide called with a=%s, b=%s", a, b)
    return _calc.divide(a, b)


@mcp.tool(
    timeout=_TIMEOUT,
    annotations={
        "readOnlyHint": True,
        "idempotentHint": True,
        "openWorldHint": False,
    },
)
def power(a: float, b: float) -> float:
    """Return a raised to the power b."""
    logger.info("power called with a=%s, b=%s", a, b)
    return _calc.power(a, b)


@mcp.tool(
    timeout=_TIMEOUT,
    annotations={
        "readOnlyHint": True,
        "idempotentHint": True,
        "openWorldHint": False,
    },
)
def nth_root(a: float, b: float) -> float:
    """Return the b-th root of a. Raises ValueError on invalid input."""
    logger.info("nth_root called with a=%s, b=%s", a, b)
    return _calc.nth_root(a, b)


@mcp.tool(
    timeout=_TIMEOUT,
    annotations={
        "readOnlyHint": True,
        "idempotentHint": True,
        "openWorldHint": False,
    },
)
def modulo(a: float, b: float) -> float:
    """Return a mod b. Raises ValueError on modulo by zero."""
    logger.info("modulo called with a=%s, b=%s", a, b)
    return _calc.modulo(a, b)


@mcp.tool(
    timeout=_TIMEOUT,
    annotations={
        "readOnlyHint": True,
        "idempotentHint": True,
        "openWorldHint": False,
    },
)
def floor_divide(a: float, b: float) -> float:
    """Return the floor division of a by b. Raises ValueError on division by zero."""
    logger.info("floor_divide called with a=%s, b=%s", a, b)
    return _calc.floor_divide(a, b)


# --- Single-operand tools ---


@mcp.tool(
    timeout=_TIMEOUT,
    annotations={
        "readOnlyHint": True,
        "idempotentHint": True,
        "openWorldHint": False,
    },
)
def sqrt(a: float) -> float:
    """Return the square root. Raises ValueError on negative input."""
    logger.info("sqrt called with a=%s", a)
    return _calc.sqrt(a)


@mcp.tool(
    timeout=_TIMEOUT,
    annotations={
        "readOnlyHint": True,
        "idempotentHint": True,
        "openWorldHint": False,
    },
)
def absolute(a: float) -> float:
    """Return the absolute value."""
    logger.info("absolute called with a=%s", a)
    return _calc.absolute(a)


@mcp.tool(
    timeout=_TIMEOUT,
    annotations={
        "readOnlyHint": True,
        "idempotentHint": True,
        "openWorldHint": False,
    },
)
def floor(a: float) -> float:
    """Return the floor of a."""
    logger.info("floor called with a=%s", a)
    return _calc.floor(a)


@mcp.tool(
    timeout=_TIMEOUT,
    annotations={
        "readOnlyHint": True,
        "idempotentHint": True,
        "openWorldHint": False,
    },
)
def ceil(a: float) -> float:
    """Return the ceiling of a."""
    logger.info("ceil called with a=%s", a)
    return _calc.ceil(a)


@mcp.tool(
    timeout=_TIMEOUT,
    annotations={
        "readOnlyHint": True,
        "idempotentHint": True,
        "openWorldHint": False,
    },
)
def log10(a: float) -> float:
    """Return the base-10 logarithm. Raises ValueError on non-positive input."""
    logger.info("log10 called with a=%s", a)
    return _calc.log10(a)


@mcp.tool(
    timeout=_TIMEOUT,
    annotations={
        "readOnlyHint": True,
        "idempotentHint": True,
        "openWorldHint": False,
    },
)
def ln(a: float) -> float:
    """Return the natural logarithm. Raises ValueError on non-positive input."""
    logger.info("ln called with a=%s", a)
    return _calc.ln(a)


@mcp.tool(
    timeout=_TIMEOUT,
    annotations={
        "readOnlyHint": True,
        "idempotentHint": True,
        "openWorldHint": False,
    },
)
def exp(a: float) -> float:
    """Return e raised to the power a."""
    logger.info("exp called with a=%s", a)
    return _calc.exp(a)


# --- Round tool ---


@mcp.tool(
    timeout=_TIMEOUT,
    annotations={
        "readOnlyHint": True,
        "idempotentHint": True,
        "openWorldHint": False,
    },
)
def round_number(a: float, decimals: int = 0) -> float:
    """Return a rounded to the given number of decimal places."""
    logger.info("round_number called with a=%s, decimals=%s", a, decimals)
    return _calc.round_number(a, decimals)


if __name__ == "__main__":
    transport = get_transport()
    if transport == "http":
        mcp.run(transport="http", host=get_host(), port=get_port())
    else:
        mcp.run(transport="stdio")
