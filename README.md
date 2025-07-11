# Emergence CLI

Command‑line companion for the **Emergence** multi‑agent network.

[![CI](https://github.com/the-emergence-ai/emergence-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/the-emergence-ai/emergence-cli/actions)
![version](https://img.shields.io/badge/cli-v0.1.1-blue)

---

## Features (so far)

| Command | What it does |
|---------|--------------|
| `emergence --version` | Prints the CLI version (`0.1.1`). |
| `emergence init <name>` | Generates a ready‑to‑run **echo agent** in a new folder called `<name>/`. |

Upcoming: `emergence deploy`, `emergence logs`, `emergence publish`.

---

## Quick Start

```bash
# 1. Get the CLI in editable mode
git clone https://github.com/the-emergence-ai/emergence-cli.git
cd emergence-cli
python -m venv .venv && source .venv/bin/activate
pip install -e .

# 2. Check it works
emergence --version
# ➜ Emergence CLI, version 0.1.1
