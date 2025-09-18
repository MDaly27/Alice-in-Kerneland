# Alice in Kerneland

welcome to alice in kerneland - Alice in kerneland is a fun hacker esque theme

Welcome to Alice in Kerneland — a fun, hacker-esque Obsidian theme and starter kit.

Quick start
- Install: Drag the theme and snippets folders into your vault’s `.obsidian` directory.
  - Theme: `.obsidian/themes/Alice-in-Kerneland`
  - Snippets: `.obsidian/snippets/*.css`
- Recommended community plugins: Terminal and Ollama.
- After enabling, run TaskRabbit commands with the Alice theme enabled to generate tags.

What’s in this repo
- Theme files under `theme/` and `.obsidian/themes/Alice-in-Kerneland` (for vault-friendly drop-in).
- Optional CSS snippets under `.obsidian/snippets/`.
- Demo content under `demo_pages/` with starter folders:
  - `bio/`, `bioanthropology/`, `biostats/`, `brewing/`, `hackers/`
- Droid utilities under `Droid/` including `demo.txt` (placeholder). Add your `taskrabbit` file/script here when available.

How to enable the theme in Obsidian
1) Open your Obsidian vault.
2) Copy the folders from this repo into your vault:
   - Copy `.obsidian/themes/Alice-in-Kerneland` into `<your-vault>/.obsidian/themes/`
   - Copy all files from `.obsidian/snippets/` into `<your-vault>/.obsidian/snippets/`
3) In Obsidian:
   - Settings → Appearance → Theme → select “Alice-in-Kerneland”.
   - Settings → Appearance → CSS snippets → enable the copied snippets.
4) Plugins:
   - Community Plugins → Browse → install “Terminal” and “Ollama”. Enable both.

TaskRabbit and tag generation
- Place your TaskRabbit script/binary into `Droid/taskrabbit` (or similar filename).
- With the Alice theme enabled, run your TaskRabbit command(s) to auto-generate tags across notes. Example (replace with your actual command):
  ```bash
  ./Droid/taskrabbit --vault "/path/to/your/vault" --tag-style alice
  ```

Local workflow and project notes
- Keep a local working copy under `/home/vlad/warp/alice-final` before pushing to GitHub (per team rule).
- Use `demo_pages/` to stage and share demo content. Empty folders contain `.gitkeep` so they remain in version control.
- If you don’t see your `taskrabbit` file yet, add it into `Droid/` and re-run your tag generation steps.

License
See LICENSE for details.