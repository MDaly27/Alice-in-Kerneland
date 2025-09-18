# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

Overview
- Minimal Python prototype of a local LLM chat loop (droid.py) that talks to an Ollama-compatible HTTP API at http://localhost:11434.
- main.py is a placeholder entrypoint stub. Additional project notes live in Ammendment_Proposal.md and Proposal-Alice-in-Kerneland.pdf.

Common commands (Arch Linux, bash)
- Create a virtual environment and install dependencies (only requests is required):
  - python -m venv .venv && source .venv/bin/activate
  - pip install --upgrade pip
  - pip install requests
- Ensure a local LLM service is running on :11434 with a model available (the script defaults to model id "phi3"). If you use Ollama, typical commands are:
  - ollama serve
  - ollama run llama3:8b-instruct  # or adjust the model name and update droid.py accordingly
- Run the chat client (reads from stdin, prints one-sentence replies):
  - Interactive: python droid.py  # then type a prompt and press Enter; Ctrl-D (EOF) to exit
  - From a pipeline: printf 'Hello there\nAnother prompt' | python droid.py
- There is no test suite or linter configuration in this repo at present.

Architecture and flow
- droid.py implements a minimal, stateful chat loop against an Ollama-compatible API.
  - Conversation state is a Python list of message dicts in OpenAI-style format: {"role": "system"|"user"|"assistant", "content": str}.
  - On start, it seeds messages with a system instruction enforcing: "answer in a single short sentence".
  - For each input line from stdin, it appends a user message, calls the chat endpoint, prints the assistant reply, then appends a follow-up system reminder reinforcing the one-sentence policy.
  - API call (POST http://localhost:11434/api/chat) sends: { model, messages, stream: false }. The code returns resp.json()["message"]["content"].
- Side effects and assumptions:
  - On startup, it overwrites file.txt with the literal string "hello, file!" (opened in write mode). Re-running will replace the file content.
  - No retry or error handling is implemented (connection failures or invalid JSON will raise). Streaming is disabled by design (stream: false).
  - Model id defaults to "phi3"; if your local runtime uses a different tag (e.g., "llama3:8b-instruct"), change the default in droid.py or edit the call site.
- Entry points:
  - droid.py is intended to be run directly from the repo root.
  - main.py defines run() but is currently a no-op placeholder.

Notes from project docs
- Ammendment_Proposal.md outlines future goals: portable/offline LLM via Ollama with preloaded models (e.g., llama3:8b-instruct, nomic-embed-text), health checks, an Obsidian plugin with commands/easter eggs, and a simple RAG v0. The current codebase is a minimal local chat loop prototype, not the full system.
- Proposal-Alice-in-Kerneland.pdf contains additional context; consult it for product direction when expanding this prototype.