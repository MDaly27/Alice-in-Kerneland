# System Requirements

- **Ollama** (https://ollama.com)
  - Install via: `curl -fsSL https://ollama.com/install.sh | sh`
  - Required model: `phi4`  
    Load with: `ollama pull phi4`

- **lolcat** (for colored output)
  - On Ubuntu: `sudo apt install lolcat`
  - On macOS: `brew install lolcat`

- **Build tools** (if compiling the C driver `tagrabbit.c`):
  - GCC or Clang
  - `make` (optional but useful)

- **Python 3.10+**
  - Match your system’s Ollama client libraries and requests.

