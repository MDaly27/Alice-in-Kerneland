

**Easter eggs (v0.1)**

- `Hollywood Mode`: command palette entry triggers a 2‑second ACCESS GRANTED animation, then normal.
- `panic`: flips to a calm monochrome theme.
- `kernel_map`: opens a graph note that links to hidden folders.
- `alice_whisper`: adds a tiny watermark “Alice was the model all along” in the status bar.
- `sudo_please`: 'sudo rm -rf /* is a choice on the list somehwere.
- All interactions with the ai model are gonna be alice like references. why? for fun
    
- Hidden note puzzle: three notes whose first letters spell “LLM”. Opening all three unlocks an extra command in the plugin.

---

## Task tracker 

### Core
-  USB layout finalized and scripted for Linux/macOS/Windows.
-  Demo vault seeded with easter eggs and README.
    

### Models and runtime (Matt)

-  Start with Ollama packaging on USB (`OLLAMA_MODELS` on stick).
-  Preload models: `llama3:8b-instruct`, `nomic-embed-text`.
-  Cross‑OS start/stop scripts + health check.
-  Smoke tests offline on 3 OS.
-  Explore `llama.cpp` path (perf and footprint), produce comparison notes.
    

### Obsidian plugin (Mark)

-  Plugin scaffold: health‑check Ollama, start if down.
-  Chat view with streaming + “insert to note”.
-  `Critique Note` command: outputs Signal/Noise/Gaps/Actions.
-  `Tag Note` command: YAML front‑matter tags + rationale.
-  RAG v0: chunk → embed → JSONL index → top‑k retrieve.
-  Add easter‑egg commands (`hollywood_mode`, `panic`, `bench_me`, `kernel_map`, `sudo_please`).
    

### Theme / Skin (Mark)

-  “h4cker” theme v0.1 (dark, neon, mono).    
-  Status bar styling for model/ctx/TPS.
    

### QA

-  Cold start to first token < 60 s.    
-  Model swap without restart.
-  Tagging writes valid YAML.
