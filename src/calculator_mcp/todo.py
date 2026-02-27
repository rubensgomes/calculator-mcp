"""Remote MCP client example using OAuth authentication."""

import asyncio

from fastmcp import Client
from fastmcp.client.auth import OAuth

MCP_URL = "https://rubens-calculator-mcp.fastmcp.app/mcp"


async def main():
    oauth = OAuth()  # uses OAuth 2.1 Authorization Code + PKCE
    async with Client(MCP_URL, auth=oauth) as client:
        # If not authenticated yet, this will trigger
        # the interactive browser flow
        await client.ping()
        print("Authenticated and connected!")


if __name__ == "__main__":
    asyncio.run(main())
