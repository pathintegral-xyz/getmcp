import requests
from typing import List, Dict, Any, Optional
from pathlib import Path
from enum import StrEnum


class MCPServerType(StrEnum):
    """The type of mcp server."""
    DOCKER = "docker"
    PYTHON = "python"
    NODEJS = "nodejs"


class GetMCPClient:
    """A client that provides commands for searching, pulling, and managing mcp servers."""
    
    def __init__(self):
        self.registry_url = "https://getmcp.io/servers"
        self.search_url = "https://getmcp.io/api/search"
    
    def search(self, term: str, limit: int = 10, type: Optional[List[MCPServerType]] = None) -> None:
        """Search for MCP servers."""
        if type is None:
            type = []
        
        print(f"Searching for '{term}' (limit: {limit}, types: {type or 'all'})")
        print("NAME                 TYPE       DESCRIPTION")
        print("-" * 60)
        # Simulated results
        results = [
            {"name": "fastapi-server", "type": "python", "description": "FastAPI server template"},
            {"name": "express-api", "type": "nodejs", "description": "Express.js API template"},
            {"name": "nginx-proxy", "type": "docker", "description": "Nginx proxy configuration"}
        ]
        
        # Filter by type if specified
        if type:
            results = [r for r in results if r["type"] in [t.value for t in type]]
            
        # Limit results
        results = results[:limit]
        
        for result in results:
            print(f"{result['name']:<20} {result['type']:<10} {result['description']}")
    
    def pull(self, image: str) -> None:
        """Pull an MCP server."""
        print(f"Pulling MCP server: {image}")
        print(f"Downloading template...")
        print(f"Setting up server configuration...")
        print(f"MCP server '{image}' is ready to use!")
