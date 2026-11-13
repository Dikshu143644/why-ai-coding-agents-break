# Why AI Coding Agents BREAK at Step 3? (The 3-Anchor Framework)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Packaging Linter Score](https://img.shields.io/badge/title.py%20Score-100%2F100-brightgreen.svg)](#youtube-packaging-linter-suite)
[![Hook Score](https://img.shields.io/badge/hookscore.py-96%2F100%20(STRONG)-blue.svg)](#hook-evaluation)

> **"Everyone tells you AI writes code 10x faster, but stop: why do you waste 3 hours debugging what broke 10 lines?"**

This repository contains the complete video production package, downloadable rules protocol, and studio playback environment for the developer deep dive: **Why AI Coding Agents BREAK at Step 3?**

![YouTube Thumbnail](assets/thumbnail.jpg)

---

## ⚡ The Problem: Context Rot & The Death Spiral

When an error hits your terminal, the instinct of 90% of developers is to paste 40 lines of stack trace into chat and hit Enter.

1. **Turn 1:** The AI apologizes and writes a blind patch without understanding the type system.
2. **Turn 2:** The patch causes a new error. You paste the new traceback.
3. **Turn 3:** The model apologizes again and refactors unrelated files to make its broken patch pass.
4. **Turn 4 (The Step 3 Collapse):** The context window is flooded with 8,000+ tokens of obsolete code, contradictory variable names, and hallucinations. The agent is no longer debugging your code—it's debugging its own previous hallucinations.

---

## 🛡️ The Solution: The 3-Anchor Framework

| Anchor | Mechanism | Constraint Enforced |
| :--- | :--- | :--- |
| **1. The Contract Anchor** | Immutable Schemas | Never write code without the type definition or interface. Schema shape is fixed; logic must adapt to it. |
| **2. The Blast Radius Anchor** | Strict File Perimeter | Limit the agent to specific line ranges (e.g., lines 42–68 in `auth.ts`). Touching imports or configs is forbidden. |
| **3. The Proof Anchor** | Deterministic Repro | Provide a single isolated reproduction test command. The model only succeeds when the test passes without changing the test. |

---

## 📋 The 12-Line Protocol (`AGENTS.md` / `.cursorrules`)

Drop this into your repository root to enforce the protocol in Cursor, Antigravity, Claude Code, or Windsurf:

```markdown
# Autonomous Debugging Protocol (.cursorrules / AGENTS.md)
1. CONTRACT FIRST: Never edit code without reading the type definition. All I/O schemas are immutable.
2. BLAST RADIUS: Only modify files explicitly targeted. Never touch imports, configs, or test assertions.
3. ISOLATED REPRO: Execute the repro command first. Verify reproducible failure before writing code.
4. SURGICAL DIFF: Make minimal possible edits necessary to pass test. No stylistic refactoring.
5. 2-STRIKE ROLLBACK: If verification fails twice, execute 'git checkout -- .' and state failed hypothesis.
6. ZERO CHATTER: Output only root cause hypothesis, unified diff, and exit code. No conversational filler.
```

Files ready in [`rules/AGENTS.md`](rules/AGENTS.md) and [`rules/.cursorrules`](rules/.cursorrules).

---

## 🎬 Production Package Contents

- **Full Video:** [`assets/Why_AI_Coding_Agents_BREAK.mp4`](assets/Why_AI_Coding_Agents_BREAK.mp4) (1280x720, 10 FPS, with HUD timer, scene cards, and synchronized subtitles)
- **Interactive Playback Studio:** [`assets/video_player.html`](assets/video_player.html) (HTML5 player with speech synthesis, Web Audio SFX, and teleprompter)
- **Spoken Word Script:** [`script/transcript.md`](script/transcript.md) (678 words, ~4m 30s)
- **Packaging Suite:** [`script/packaging.md`](script/packaging.md) (100/100 linter score)
- **SEO & Chapters:** [`script/seo_metadata.md`](script/seo_metadata.md) (Chapters from 0:00, 18 tags, community post)
- **Audio Voiceover:** [`audio/`](audio/) (7 scene WAV files synthesized with Microsoft David Desktop)
- **Render Script:** [`scripts/render_video.py`](scripts/render_video.py)

---

## 🚀 Quick Start (Running the Studio)

Open the interactive playback studio in any modern web browser:

```bash
# On Windows
start assets/video_player.html

# On macOS
open assets/video_player.html

# On Linux
xdg-open assets/video_player.html
```

Use `Spacebar` to Play/Pause, `Arrow Keys` to jump between scenes, and `📋 Copy Rules` to export the 12-line protocol directly into your clipboard.

---

## 📜 License
MIT License. Free to use, adapt, and distribute.
