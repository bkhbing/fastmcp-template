from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool

class Calculator(MCPMixin):

    @mcp_tool(name="add",
    description="Add two numbers",
    enabled=True
    )
    def add(self, a: int, b: int) -> int:
        return a + b
