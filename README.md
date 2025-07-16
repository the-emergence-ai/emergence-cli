# Emergence CLI

Command‑line companion for the **Emergence** multi‑agent network.

[![CI](https://github.com/the-emergence-ai/emergence-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/the-emergence-ai/emergence-cli/actions)
![version](https://img.shields.io/badge/cli-v0.3.1-blue)

---

## Features (so far)

| Command                                 | What it does                                                                           |
|-----------------------------------------|----------------------------------------------------------------------------------------|
| `emergence --version`                   | Prints the CLI version (`0.3.1`).                                                      |
| `emergence init <name>`                 | Generates a ready‑to‑run **echo agent** in a new folder called `<name>/`.             |
| `emergence build <path>`                | Builds a Docker image from the agent folder. Defaults to `emergence/<folder>:latest`. |
| `emergence publish --local <path>`      | Pushes the built image to `localhost:5000/<folder>:latest`.                           |
| `emergence publish --local --port 5050 <path>` | Pushes to `localhost:5050/<folder>:latest` if using a custom port.            |

Upcoming: `emergence deploy`, `emergence logs`, `emergence invoke`.

<p align="center"> <a href="https://imgur.com/OfnRPAR"> 🎥 Watch a 60‑sec demo ↗ </a> </p> <p align="center"> <img src="https://i.imgur.com/OfnRPAR.gif" alt="Emergence CLI demo" width="700"/> </p>

---

## Quick Start

```bash
# 1. Get the CLI in editable mode
git clone https://github.com/the-emergence-ai/emergence-cli.git
cd emergence-cli
python -m venv .venv && source .venv/bin/activate
pip install -e .

# 2. Check it works
emergence --version
# ➜ Emergence CLI, version 0.3.1

# 3. Scaffold a new agent
emergence init demo-agent

# 4. Build the agent into a Docker image
emergence build demo-agent

# 5. Start a local Docker registry (on port 5050)
docker run -d -p 5050:5000 --name emergence-registry registry:2

# 6. Publish the image to the local registry
emergence publish --local --port 5050 demo-agent

# 7. Confirm it's there
curl -s http://localhost:5050/v2/_catalog
# ➜ {"repositories":["demo-agent"]}

# Optional: Run a message through it directly (local mode)
python demo-agent/agent.py <<<'{"id":"1","from":"test","to":"demo-agent","verb":"HELP","data":{"prompt":"ping"}}'
