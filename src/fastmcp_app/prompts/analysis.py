from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_prompt

class Analysis(MCPMixin):
    @mcp_prompt(
        name="analysis_prompt",
        title="Data Analysis Prompt",
        description="Analyzes data patterns",
        meta={"complexity": "high", "domain": "analytics", "requires_context": True}
    )
    def analysis_prompt_method(self, dataset: str):
        return f"Analyze the patterns in {dataset}"
