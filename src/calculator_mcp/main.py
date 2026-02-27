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
# Copyright protection, if any, is limited to the original
# human contributions and modifications made to this project.
# The AI-generated portions of the code and
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

"""CLI entry point for the calculator-mcp server."""

import logging
import signal
import sys
import types

from calculator_mcp.config import get_host, get_port, get_transport
from calculator_mcp.server import mcp

logger = logging.getLogger(__name__)


def _shutdown_handler(
    signum: int,
    frame: types.FrameType | None,  # pylint: disable=unused-argument
) -> None:
    """Handle shutdown signals for graceful termination.

    Args:
        signum: The signal number received.
        frame: The current stack frame (unused).
    """
    sig_name = signal.Signals(signum).name
    logger.info("Received %s, shutting down gracefully", sig_name)
    sys.exit(0)


def main() -> None:
    """Entry point for the calculator-mcp application."""
    signal.signal(signal.SIGINT, _shutdown_handler)
    signal.signal(signal.SIGTERM, _shutdown_handler)

    transport = get_transport()
    if transport == "http":
        mcp.run(transport="http", host=get_host(), port=get_port())
    else:
        mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
