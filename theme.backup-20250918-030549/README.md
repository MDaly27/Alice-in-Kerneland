# Alice in Kerneland Theme

A dark, neon, whimsical theme inspired by Alice in Wonderland with a kernel/engineering twist. Includes CSS utilities for tags/badges, playful animations, and a preview page with coding jokes.

Quick start
- Open theme/preview.html in a browser to see the theme, tags, and rotating jokes.
- To use in your own HTML, include the stylesheet and add tag classes:

Usage
1) Include stylesheet
   <link rel="stylesheet" href="theme/alice-kerneland.css">

2) Use tags/badges
   <span class="tag mad-hatter">Mad Hatter</span>
   <span class="tag cheshire-cat">Cheshire Cat</span>
   <span class="tag white-rabbit">White Rabbit</span>
   <span class="tag queen-of-hearts">Queen of Hearts</span>

3) Optional jokes rotator (for the preview page or your own)
   <script src="theme/theme.js"></script>

Design notes
- Palette: deep midnight background with neon accents (mint, violet, cyan, tea‑gold).
- Motifs: tea party, rabbit‑hole, chess, playing cards, grins, and the occasional kernel panic.
- Components: .tag (aka .ak-badge / .ak-chip), .ak-title, .ak-code, whimsical micro‑animations (wobble, grin).
- No external dependencies; pure CSS/JS. No AI models.

Files
- theme/alice-kerneland.css — the theme stylesheet
- theme/preview.html — a self-contained demo page
- theme/theme.js — small script that rotates themed coding jokes (optional)