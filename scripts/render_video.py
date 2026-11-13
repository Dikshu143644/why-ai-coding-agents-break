#!/usr/bin/env python3
"""
render_video.py - Render the 7-scene presentation to MP4 using OpenCV.
"""
import cv2, numpy as np, os

width, height = 1280, 720
fps = 10
output_path = os.path.join(os.path.dirname(__file__), "..", "assets", "Why_AI_Coding_Agents_BREAK.mp4")

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, float(fps), (width, height))

scenes = [
    {
        'badge': 'SCENE 1: THE HOOK (0:00 - 0:15)',
        'title': 'WHY AI CODING AGENTS BREAK AT STEP 3',
        'sub': 'Everyone tells you AI writes code 10x faster...',
        'detail': 'PROMPT 4: RecursionError - Maximum call stack size exceeded',
        'duration': 15,
        'color': (40, 40, 180)
    },
    {
        'badge': 'SCENE 2: THE TURN (0:15 - 0:40)',
        'title': 'THE 3-ANCHOR FRAMEWORK',
        'sub': 'Kill the error loop in under 90 seconds without prompt tricks',
        'detail': '1. CONTRACT (Types) | 2. BLAST RADIUS (Files) | 3. PROOF (Test)',
        'duration': 25,
        'color': (180, 120, 20)
    },
    {
        'badge': 'SCENE 3: THE CONTEXT TRAP (0:40 - 1:45)',
        'title': 'CONTEXT ROT: THE DEATH SPIRAL',
        'sub': 'By prompt 4, 8,000 tokens of apologies pollute the model',
        'detail': 'Turn 1: Apology -> Turn 2: Rewrites imports -> Turn 4: Infinite Loop',
        'duration': 65,
        'color': (20, 100, 200)
    },
    {
        'badge': 'SCENE 4: 3-ANCHOR LOCKDOWN (1:45 - 2:55)',
        'title': 'SURGICAL BLAST RADIUS',
        'sub': 'Lines 42-68 only. All imports and schema types are IMMUTABLE',
        'detail': 'Input/Output contracts are locked. Model adapts to the shape.',
        'duration': 70,
        'color': (180, 80, 120)
    },
    {
        'badge': 'SCENE 5: AUTONOMOUS SELF-HEALING (2:55 - 3:55)',
        'title': '2-STRIKE AUTOMATIC ROLLBACK',
        'sub': 'Execute Repro -> Surgical Diff -> 2-Strike Limit -> git checkout -- .',
        'detail': 'Prevents AI writing 30 lines of workaround to fix its own bug.',
        'duration': 60,
        'color': (60, 160, 60)
    },
    {
        'badge': 'SCENE 6: THE BLUEPRINT (3:55 - 4:35)',
        'title': '12-LINE AUTONOMOUS PROTOCOL',
        'sub': 'Free download: Drop .cursorrules / AGENTS.md into repository root',
        'detail': 'Forces the AI agent to resolve root cause on the first pass.',
        'duration': 40,
        'color': (160, 40, 160)
    },
    {
        'badge': 'SCENE 7: OUTRO (4:35 - 4:45)',
        'title': 'STOP WASTING 3 HOURS DEBUGGING',
        'sub': 'Download the blueprint below and subscribe for weekly deep dives',
        'detail': 'https://github.com/Dikshu143644/why-ai-coding-agents-break',
        'duration': 10,
        'color': (40, 40, 200)
    }
]

total_secs = sum(s['duration'] for s in scenes)
elapsed_sec = 0

for s_idx, sc in enumerate(scenes):
    n_frames = sc['duration'] * fps
    for f in range(n_frames):
        current_t = elapsed_sec + (f / fps)
        pct = current_t / total_secs
        
        img = np.zeros((height, width, 3), dtype=np.uint8)
        img[:] = (18, 14, 11)
        
        # Header banner
        cv2.rectangle(img, (0, 0), (width, 80), (28, 22, 18), -1)
        cv2.line(img, (0, 80), (width, 80), (60, 50, 45), 2)
        cv2.putText(img, sc['badge'], (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, sc['color'], 2, cv2.LINE_AA)
        
        mins = int(current_t // 60)
        secs = int(current_t % 60)
        cv2.putText(img, f'{mins:02d}:{secs:02d} / 04:30', (width - 250, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (180, 180, 180), 2, cv2.LINE_AA)
        
        # Center Card
        cv2.rectangle(img, (100, 140), (width - 100, height - 160), (32, 26, 22), -1)
        cv2.rectangle(img, (100, 140), (width - 100, height - 160), sc['color'], 2)
        cv2.putText(img, sc['title'], (140, 240), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 3, cv2.LINE_AA)
        cv2.putText(img, sc['detail'], (140, 340), cv2.FONT_HERSHEY_SIMPLEX, 0.85, (200, 230, 255), 2, cv2.LINE_AA)
        
        # Subtitle
        cv2.rectangle(img, (100, height - 130), (width - 100, height - 40), (10, 10, 10), -1)
        cv2.rectangle(img, (100, height - 130), (width - 100, height - 40), (70, 70, 70), 1)
        cv2.putText(img, sc['sub'], (130, height - 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (230, 230, 230), 2, cv2.LINE_AA)
        
        # Scrubber
        bar_w = int((width - 200) * pct)
        cv2.rectangle(img, (100, height - 25), (width - 100, height - 15), (40, 40, 40), -1)
        cv2.rectangle(img, (100, height - 25), (100 + bar_w, height - 15), (0, 0, 255), -1)
        
        out.write(img)
    elapsed_sec += sc['duration']

out.release()
print(f"SUCCESS! Rendered video to {output_path}")
