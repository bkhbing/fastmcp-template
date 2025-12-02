from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_resource

class Component(MCPMixin):
    @mcp_resource(uri="component://data",
    enabled=True,
    description="Get some data")
    def get_data(self) -> str:
        return {"data": "some data"}