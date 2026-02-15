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

import httpx
from fastmcp import FastMCP

from calculator_mcp.config import get_base_url

logger = logging.getLogger(__name__)

_HOMEPAGE = "https://github.com/rubensgomes/calculator-mcp/"
_BASE_URL = get_base_url()

mcp = FastMCP(
    "Calculator MCP Server",
    version=version("calculator-mcp"),
    website_url=_HOMEPAGE,
)
logger.info("Initialized Calculator MCP Server")


async def _post(endpoint: str, payload: dict) -> float:
    """POST JSON to the calculator API and return the result."""
    url = f"{_BASE_URL}/{endpoint}"
    logger.debug("POST %s with payload %s", url, payload)
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)
        response.raise_for_status()
        result = response.json()["result"]
    logger.debug("POST %s returned result=%s", url, result)
    return result


# --- Two-operand tools ---


@mcp.tool
async def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    logger.info("add called with a=%s, b=%s", a, b)
    return await _post("add", {"a": a, "b": b})


@mcp.tool
async def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    logger.info("subtract called with a=%s, b=%s", a, b)
    return await _post("subtract", {"a": a, "b": b})


@mcp.tool
async def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    logger.info("multiply called with a=%s, b=%s", a, b)
    return await _post("multiply", {"a": a, "b": b})


@mcp.tool
async def divide(a: float, b: float) -> float:
    """Return the quotient of two numbers.

    Returns an HTTP 400 Bad Request error on division by zero.
    """
    logger.info("divide called with a=%s, b=%s", a, b)
    return await _post("divide", {"a": a, "b": b})


@mcp.tool
async def power(a: float, b: float) -> float:
    """Return a raised to the power b."""
    logger.info("power called with a=%s, b=%s", a, b)
    return await _post("power", {"a": a, "b": b})


@mcp.tool
async def nth_root(a: float, b: float) -> float:
    """Return the b-th root of a. Returns an HTTP 400 Bad Request error on invalid input."""
    logger.info("nth_root called with a=%s, b=%s", a, b)
    return await _post("nth_root", {"a": a, "b": b})


@mcp.tool
async def modulo(a: float, b: float) -> float:
    """Return a mod b. Returns an HTTP 400 Bad Request error on modulo by zero."""
    logger.info("modulo called with a=%s, b=%s", a, b)
    return await _post("modulo", {"a": a, "b": b})


@mcp.tool
async def floor_divide(a: float, b: float) -> float:
    """Return the floor division of a by b. Returns an HTTP 400 Bad Request error on division by zero."""
    logger.info("floor_divide called with a=%s, b=%s", a, b)
    return await _post("floor_divide", {"a": a, "b": b})


# --- Single-operand tools ---


@mcp.tool
async def sqrt(a: float) -> float:
    """Return the square root. Returns an HTTP 400 Bad Request error on negative input."""
    logger.info("sqrt called with a=%s", a)
    return await _post("sqrt", {"a": a})


@mcp.tool
async def absolute(a: float) -> float:
    """Return the absolute value."""
    logger.info("absolute called with a=%s", a)
    return await _post("absolute", {"a": a})


@mcp.tool
async def floor(a: float) -> float:
    """Return the floor of a."""
    logger.info("floor called with a=%s", a)
    return await _post("floor", {"a": a})


@mcp.tool
async def ceil(a: float) -> float:
    """Return the ceiling of a."""
    logger.info("ceil called with a=%s", a)
    return await _post("ceil", {"a": a})


@mcp.tool
async def log10(a: float) -> float:
    """Return the base-10 logarithm. Returns an HTTP 400 Bad Request error on non-positive input."""
    logger.info("log10 called with a=%s", a)
    return await _post("log10", {"a": a})


@mcp.tool
async def ln(a: float) -> float:
    """Return the natural logarithm. Returns an HTTP 400 Bad Request error on non-positive input."""
    logger.info("ln called with a=%s", a)
    return await _post("ln", {"a": a})


@mcp.tool
async def exp(a: float) -> float:
    """Return e raised to the power a."""
    logger.info("exp called with a=%s", a)
    return await _post("exp", {"a": a})


# --- Round tool ---


@mcp.tool
async def round_number(a: float, decimals: int = 0) -> float:
    """Return a rounded to the given number of decimal places."""
    logger.info("round_number called with a=%s, decimals=%s", a, decimals)
    return await _post("round", {"a": a, "decimals": decimals})
