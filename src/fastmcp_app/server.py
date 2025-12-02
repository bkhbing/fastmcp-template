from fastmcp import FastMCP
from tools.calculator import Calculator
from resources.greetings import get_greeting
from resources.component import Component
from prompts.analysis import Analysis
from settings import settings

# Initialize the MCP server
mcp = FastMCP(settings.app_name)

# Register tools
calculator = Calculator()
calculator.register_tools(mcp)

# Register resources
mcp.resource("greeting://{name}")(get_greeting)
component = Component()
component.register_resources(mcp)

# Register prompts
analysis = Analysis()
analysis.register_prompts(mcp)

# uvicorn src.fastmcp_app.server:app --reload
app = mcp.http_app()

# if __name__ == "__main__":
#     mcp.run()
