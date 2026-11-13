# Full Video Transcript: Why AI Coding Agents BREAK at Step 3?

**Runtime:** ~4m 30s (678 spoken words)  
**Hook Formula:** Contrarian Flip (Score: 96/100)  

---

### [0:00 - 0:15] THE HOOK
- **[ON SCREEN]:** Cold open on IDE terminal flooded with red stack traces. Zoom in on terminal clock showing 11:42 PM.
- **[SOUND DESIGN]:** Fast mechanical typing interrupted by a harsh system error buzzer and low drone.
- **(SPOKEN):**
  > "Everyone tells you AI writes code 10x faster, but stop: why do you waste 3 hours debugging what broke 10 lines? You paste a stack trace into chat, hit Enter, and suddenly your simple endpoint has five hallucinated dependencies, two broken imports, and code that refuses to compile. The AI didn't break your codebase. Your debugging workflow did."

### [0:15 - 0:40] THE TURN
- **[ON SCREEN]:** Cut to camera or clean motion graphic replacing the messy chat with a 3-part blueprint.
- **[SOUND DESIGN]:** Clean digital swoosh into a steady tech-synth baseline.
- **(SPOKEN):**
  > "In the next four minutes, I will show you the exact mechanism causing your AI models to hallucinate while debugging, and hand you the three-anchor framework that kills the error loop in under ninety seconds. No prompt engineering tricks, no wrappers—just three rigid engineering constraints you can drop into Cursor, Claude, or Antigravity right now."

### [0:40 - 1:45] BEAT 1: THE CONTEXT TRAP
- **[ON SCREEN]:** Developer highlighting 50 lines of traceback into chat. Model replies: *"You're absolutely right! My apologies..."* and starts modifying unrelated modules.
- **[SOUND DESIGN]:** Descending glitch chime on the apology text.
- **(SPOKEN):**
  > "Here is the mistake you are repeating every afternoon: The Context Trap. When an error hits your terminal, your instinct is to copy forty lines of red stack trace, dump it into the AI prompt, and say 'fix this'. 
  > 
  > The AI looks at that stack trace without runtime context, assumes the worst, and rewrites your function. It changes a variable name. Now your test throws a new error. So you paste that new error back in. The model apologizes, generates a second patch, and quietly breaks your database schema.
  > 
  > By prompt number four, your context window is clogged with six thousand tokens of obsolete code, conflicting variable names, and polite model apologies. The AI isn't debugging your codebase anymore. It is debugging its own hallucinations from two prompts ago. Every time you feed an error message back into the same conversation thread, you are poisoning the context window and guaranteeing another hour of wasted work."

### [1:45 - 2:55] BEAT 2: THE 3-ANCHOR FRAMEWORK
- **[ON SCREEN]:** 3D animation of three steel anchors locking down: 1. CONTRACT, 2. BLAST RADIUS, 3. PROOF.
- **[SOUND DESIGN]:** Three rhythmic metallic locking impacts.
- **(SPOKEN):**
  > "To stop the bleeding, you need the 3-Anchor Framework. Before you allow an AI agent to touch a single line of broken code, you lock down three rigid boundaries.
  > 
  > Anchor number one is the Contract Anchor. You never paste raw errors without the interface definition. Feed it the TypeScript type, the Pydantic schema, or the exact function signature. You tell the model: 'This input and output contract is immutable. Adapt your logic to this shape, never change the shape.'
  > 
  > Anchor number two is the Blast Radius. When models debug in open space, they refactor files they shouldn't even know exist. You explicitly bound the perimeter: 'You may only edit lines forty-two through sixty-eight inside auth.py. Touching imports, configuration, or database models is strictly forbidden.'
  > 
  > Anchor number three is the Proof Anchor. You never ask 'Does this look right?' You provide a single deterministic repro command: an isolated unit test or a curl command. The model only wins when the test passes without altering the test itself."

### [2:55 - 3:55] BEAT 3: THE AUTONOMOUS SELF-HEALING LOOP
- **[ON SCREEN]:** System loop diagram: `[Run Repro]` -> `[Inspect Exit Code]` -> `[Surgical Diff]`. Red branch: `[2-Fail Limit]` -> `[git checkout -- .]` -> `[Hypothesis Log]`.
- **[SOUND DESIGN]:** Fast cybernetic data stream audio.
- **(SPOKEN):**
  > "Once your anchors are set, you put the model inside an Autonomous Self-Healing Loop. 
  > 
  > Instead of acting as a human copy-paste machine between your terminal and the chat window, you give your agent local tool execution with a hard stop condition. The loop runs three steps: execute the repro command, inspect the stdout, and apply a surgical diff.
  > 
  > Crucially, you enforce a two-attempt limit. If the test fails twice, the agent is forbidden from guessing a third time. The rule mandates that it runs git diff, reverts its own changes back to HEAD, and outputs a one-sentence hypothesis explaining why its assumption failed before touching code again. 
  > 
  > This single constraint prevents the death spiral where an AI writes thirty lines of workaround code to fix a bug caused by its own previous patch."

### [3:55 - 4:35] THE PAYOFF: THE BLUEPRINT
- **[ON SCREEN]:** Full-screen graphic showing the clean 12-line `.cursorrules` / `AGENTS.md` rules template.
- **(SPOKEN):**
  > "That is the entire system. And to make this effortless, I wrote the exact twelve-line rule blueprint that embeds the Contract, Blast Radius, and Self-Healing constraints directly into your editor's system rules. 
  > 
  > That is the blueprint, it is in the description below, completely free. Copy it into your project's rules file, whether you use Cursor, Antigravity, or Claude Code. Next time your build breaks, you won't touch the prompt box. The rule forces the model to stay inside the box and resolve the root cause on the first pass."

### [4:35 - 4:45] THE CLOSE
- **[ON SCREEN]:** Host on camera; GitHub repository link and Subscribe graphic appear.
- **(SPOKEN):**
  > "Drop that blueprint into your repository root today, run your next failing test through it, and subscribe if it saved your evening."
