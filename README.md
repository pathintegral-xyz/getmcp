# getmcp - MCP Server Management Tool

A command-line interface tool that provides functionality for searching, pulling, and managing MCP servers.

## Installation

From PyPI:

```bash
pip install getmcp
```

From source:

```bash
pip install -e .
```

## Usage

After installation, you can use either the `getmcp` or `mcpm` command (they are identical):

### Search for servers

```bash
getmcp search github
# or
mcpm search github --type python nodejs --limit 5
```

### Pull a server

```bash
getmcp pull github
# or
mcpm pull github
```

### Show version information

```bash
getmcp version
# or
mcpm version
```

## Features

- Search for MCP servers
- Pull server templates
- Filter by server type (docker, python, nodejs)
- Two command aliases: `getmcp` and `mcpm`

## Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/pathintegral-xyz/getmcp.git
cd getmcp

# Install in development mode
pip install -e .
```

### Building the Package

```bash
python -m build
```

### Publishing to PyPI

```bash
python -m twine upload dist/*
```

## Dependencies

- Python 3.11+
- requests library

## License

MIT