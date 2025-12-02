# FastMCP Python Template

This is a template for building MCP servers using [FastMCP](https://gofastmcp.com/).

## Project Structure

```
mcp-python-template/
├── src/
│   └── fastmcp_app/
│       ├── server.py          # Main application entry point
│       ├── tools/             # Tool definitions
│       ├── resources/         # Resource definitions
│       └── prompts/           # Prompt definitions
├── pyproject.toml
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

### Installation

1.  Clone this repository.
2.  Install dependencies:

    ```bash
    # Using uv (recommended)
    uv sync
    ```

### Configuration

1.  Copy `.env.example` to `.env`:
    ```bash
    cp .env.example .env
    # or on Windows
    copy .env.example .env
    ```
2.  Edit `.env` to set your configuration (e.g., `APP_NAME`).

### Running the Server

use the `fastmcp` CLI for development with auto-reload:

```bash
fastmcp run src/fastmcp_app/server.py:mcp
```

Or run with `uvicorn` (useful for HTTP/SSE):

```bash
uvicorn src.fastmcp_app.server:app --reload
```

### Adding New Functionality

1.  **Tools**: Add new functions in `src/fastmcp_app/tools/` and register them in `server.py`.
2.  **Resources**: Add new functions in `src/fastmcp_app/resources/` and register them in `server.py`.
3.  **Prompts**: Add new functions in `src/fastmcp_app/prompts/` and register them in `server.py`.