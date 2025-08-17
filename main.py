# server.py
from fastmcp import FastMCP
from src.utils.logger import logger

mcp = FastMCP("CapCut Mate MCP")

@mcp.tool
async def add(a: int, b: int) -> int:
    """Add two numbers"""
    # Log a message to the client
    await ctx.info(f"Processing {a} + {b}...")
    return a + b

if __name__ == "__main__":
    logger.info("Start CapCut Mate MCP Server")
    mcp.run("sse", host="0.0.0.0", port=60000)