# server.py
import os
from fastmcp import FastMCP
from src.utils.logger import logger

mcp = FastMCP("CapCut Mate MCP")

# ------------------ 工具 ------------------
@mcp.tool
async def add(a: int, b: int, ctx) -> int:
    """Add two numbers"""
    await ctx.info(f"Processing {a} + {b}...")
    return a + b

# ------------------ 资源 ------------------
@mcp.resource("greeting://{name}")
async def get_greeting(name: str) -> str:
    """
    根据 name 返回一段欢迎文本。
    客户端可通过：
      - Claude Desktop 的 @greeting://Alice
      - 或 HTTP GET http://<host>:60000/mcp/resource?uri=greeting://Alice
    来读取。
    """
    return f"Hello, {name}! Welcome to CapCut Mate MCP 🎉"

# ------------------ 启动 ------------------
if __name__ == "__main__":
    logger.info("Start CapCut Mate MCP SSE Server")
    mcp.run("sse", host="0.0.0.0", port=60000)