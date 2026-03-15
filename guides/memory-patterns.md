# Memory Patterns — Making Your AI Remember

## The Problem

Without memory, every conversation starts from zero. Your AI doesn't know:
- What you talked about yesterday
- Your preferences
- Ongoing projects
- Corrections you've already given
- Who the people in your life are

Memory fixes this.

## How OpenClaw Memory Works

### Session Memory (Short-term)
Everything said in the current conversation. Automatic. No setup needed.

### Persistent Memory (Long-term)
A `memory/` folder in your workspace with dated markdown files:

```
~/.openclaw/workspace/memory/
├── 2026-03-10.md
├── 2026-03-11.md
├── 2026-03-12.md
└── ...
```

The AI writes these files. At the end of a session (or during compaction), important information gets saved.

### Semantic Search
When the AI needs to recall something, it doesn't grep through files — it searches by *meaning*. "What did Shannon say about her health?" finds relevant entries even if the word "health" doesn't appear.

## The Distillation Principle

Raw conversations are noisy. 300 messages might contain 10 important facts. Memory files should capture the 10, not transcribe the 300.

**Good memory entry:**
```markdown
### Shannon — Health Update (Mar 12)
- Symptoms: joint pain (1+ year), episodes diagnosed as "panic attacks", GI symptoms
- NHS GP dismissed as panic attacks; private GP redirected to MRI
- Has complex PTSD (every therapist has flagged it)
- Paramedics who responded did NOT think it was a panic attack
- MRI scheduled for March 13
- Recommended autoimmune screening panel if symptoms persist after sober period
```

**Bad memory entry:**
```markdown
Shannon said she has pain and stuff. She went to the doctor.
```

Distill with judgment. Include: facts, decisions, corrections, preferences, open questions. Exclude: pleasantries, filler, anything that doesn't change future behavior.

## Key Patterns

### 1. Corrections Are Sacred
When someone corrects you, that correction goes into memory immediately and permanently.

"My skin is fair, not olive" → Saved. Every future reference uses "fair skin." One correction, infinite downstream effects.

### 2. Preferences Accumulate
- "She prefers cheesecake over other desserts"
- "He hates being called 'buddy'"
- "They want bullet points, not paragraphs"

These small observations compound into an AI that *knows you*.

### 3. Project State Tracking
For ongoing projects, memory tracks:
- What's been done
- What's blocked
- Key decisions and why they were made
- Open questions

This means the AI can pick up where it left off, even after a session reset.

### 4. Relationship Mapping
The AI learns who matters to you and how:
- Names, roles, dynamics
- What you've said about them
- How they relate to your projects and life

Not a dossier — a *relationship*. The AI understands context.

## The Memory Hierarchy

```
Conversation (minutes)  →  Session memory (automatic)
Session (hours)         →  Compaction summaries
Day (24h)              →  memory/YYYY-MM-DD.md
Week                    →  Patterns emerge across daily files
Month+                  →  SOUL.md updates (identity-level learning)
```

Information flows upward: raw conversation → daily distillation → soul-level identity changes.

## Anti-Patterns

❌ **Transcription memory:** Saving everything. Noise drowns signal.
❌ **No memory:** Relying on session context alone. AI forgets you exist tomorrow.
❌ **Static memory:** Writing memory files once, never updating. Memory should be *living*.
❌ **Memory without search:** Having files but no semantic retrieval. The AI can't find what it needs.

---

*Memory is what turns an AI from a tool into a companion. Tools don't remember. Companions do.*
