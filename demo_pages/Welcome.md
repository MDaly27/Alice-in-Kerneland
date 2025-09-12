---
cssclasses:
  - hk-prompts
---

#  Styleguide

Toggle effects for **this note**:

- [x] CRT lines  <!-- id matters --> <input type="checkbox" id="hk-toggle-crt">
- [x] Grid wires <input type="checkbox" id="hk-toggle-grid">
- [x] Faster motion <input type="checkbox" id="hk-toggle-fast">

## Headings
### H2 looks like this
#### H3 looks like this

## Inline components

Normal text with a <span class="hack-glow">glowing callout</span> and a <span class="hack-scan">scanning highlight</span>.
Underline variant with neon: <span class="hack-underline">underlined segment</span>.

Keyboard: press <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>.

Badge: <span class="hack-badge">alpha</span> <span class="hack-badge">beta</span> <span class="hack-badge">rc</span>

Chip: <span class="hack-chip">#kernel</span> <span class="hack-chip">#obsidian</span>

## Quotes
> This is a blockquote fit for a terminal.  
> Add meaning. Remove ceremony.

## Code

Inline `code` and a fenced block:

```python
def cheshire(x: int) -> int:
    # cached before you existed
    return (x ^ 0xC0FE) & 0xFFFF
