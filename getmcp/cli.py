import argparse
from .client import GetMCPClient, MCPServerType


def main():
    """Main entry point for the getmcp CLI."""
    parser = argparse.ArgumentParser(description="Get MCP CLI tool")
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # search command
    search_parser = subparsers.add_parser("search", help="Search for mcp servers")
    search_parser.add_argument("term", help="Term to search for")
    search_parser.add_argument("--type", type=MCPServerType, nargs='*', default=[], help="Server types")
    search_parser.add_argument("--limit", type=int, default=10, help="Max number of results")
    
    # pull command
    pull_parser = subparsers.add_parser("pull", help="Pull an mcp server")
    pull_parser.add_argument("image", help="Image to pull")
    
    # version command
    version_parser = subparsers.add_parser("version", help="Show version information")
    
    args = parser.parse_args()
    
    client = GetMCPClient()
    
    if args.command == "search":
        client.search(args.term, args.limit, args.type)
    elif args.command == "pull":
        client.pull(args.image)
    elif args.command == "version":
        print("Client:")
        print(" Version:    0.1.0")
        print(" API version: 1.0")
        print(" OS/Arch:     python")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
