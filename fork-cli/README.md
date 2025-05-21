# FORK-CLI

## Setup

**1 - Create python virtual environment**

```bash
python3 -m venv .venv
```

**2 - Activate python virtual environment**

On Windows:
```bash
.venv\Scripts\activate
```

On Linux/macOS:
```bash
source .venv/bin/activate
```

**3 - Install dependencies**

```bash
pip install -r requirements.txt
```

---

## Usage

### Run Tests

```bash
pytest
```

### Build Standalone Binary

```bash
make build
```
This will generate a standalone binary in the `dist/` directory using PyInstaller.

### Install Binary Globally

```bash
make install
```
This will copy the binary to `/usr/local/bin/fork-cli` (requires sudo).

### Clean Build Artifacts

```bash
make clean
```

### Run the CLI (Python)

```bash
python3 main.py
```

### Run the CLI (Binary)

After `make install`:
```bash
fork-cli
```

---

## Architecture Overview

- **cli/commands/**: All CLI commands are organized by context (root, project, graph, representation). Each command is a class inheriting from `Command` and implements a `symbol` and `execute` method.
- **cli/commander.py**: The interactive shell. Handles command parsing, history, and tab auto-completion.
- **cli/context.py**: Stores the current session state (selected project, graph, representation, etc).
- **cli/project.py**: Handles project management, including loading/saving multiple graphs per project.
- **graph/core/**: Contains the core graph, node, and edge logic.
- **graph/representation/**: Contains different graph representations (adjacency list, matrix, etc) and algorithms.
- **Makefile**: Provides tasks for building, installing, cleaning, and running the CLI.
- **main.py**: Entry point for the CLI application.

The CLI is modular and extensible: new commands can be added easily, and the architecture supports interactive workflows with command history and auto-completion.