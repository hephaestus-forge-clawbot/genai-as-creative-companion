# 🤖 Build Your AI Companion

> **A practical workshop for building a persistent, opinionated AI companion that lives in your existing tools.**

Most people use AI by visiting a website and typing a prompt. That's like having a brilliant colleague who forgets you exist every time you leave the room.

This workshop shows you how to build something different: an AI that **lives in your WhatsApp, Slack, Telegram, or Discord** — that has a personality, remembers your conversations, learns your preferences, and gets better over time.

**No ML knowledge required. No coding experience assumed.**

---

## What You'll Build

By the end of this workshop, you'll have:

- 🧠 An AI with a **soul** — personality, opinions, voice, growth edges
- 💾 A **memory system** — it remembers yesterday, last week, last month
- 🔧 **Skills** — image generation, web search, research, whatever you need
- 📱 **Multi-channel presence** — your AI in WhatsApp, Telegram, Slack, or Discord
- 🫀 A **heartbeat** — it checks in, monitors things, acts proactively

**Time to first working bot: ~20 minutes.**

---

## Quick Start

### Step 1: Install OpenClaw

[OpenClaw](https://github.com/openclaw/openclaw) is the open-source framework that makes all of this work. It handles the plumbing — channels, sessions, memory, tool execution — so you focus on the interesting parts.

```bash
# macOS
brew install openclaw

# Linux / Windows (WSL)
npm install -g openclaw

# Or via pnpm
pnpm install -g openclaw
```

### Step 2: Configure

```bash
openclaw configure
```

This sets up `~/.openclaw/` and walks you through connecting your first AI provider (we recommend **Anthropic Claude** — currently the best model for agentic work).

You'll need an API key from at least one provider:
- [Anthropic](https://console.anthropic.com/) (Claude) — **recommended**
- [OpenAI](https://platform.openai.com/) (GPT)
- [Google](https://aistudio.google.com/) (Gemini)

### Step 3: Connect a Channel

```bash
# WhatsApp (scan QR code)
openclaw channels login --channel whatsapp

# Telegram (paste bot token)
openclaw channels login --channel telegram

# Discord (paste bot token)
openclaw channels login --channel discord
```

### Step 4: Give It a Soul

Copy our starter soul into your workspace:

```bash
cp templates/SOUL.md ~/.openclaw/workspace/SOUL.md
```

Edit it. Make it yours. This is the most important file — it defines who your AI *is*. See [The Soul System](#the-soul-system) below.

### Step 5: Start

```bash
openclaw gateway start
```

Message your bot. It's alive. 🔥

---

## The Four Pillars

### 1. 🧠 The Soul System

The soul is a markdown file (`SOUL.md`) that defines your AI's identity. Not a system prompt — a *living document* that evolves with every conversation.

**Why it matters:** Without a soul, your AI is a generic assistant. With one, it's a *character* — consistent, opinionated, recognisable.

A good soul file includes:

```markdown
# Who I Am
- Name, personality, voice
- What I care about
- What I find boring
- My opinions (yes, opinions)

# How I Communicate
- My tone (formal? casual? chaotic?)
- When I speak vs. when I stay silent
- My signature phrases or habits

# My Growth Edges
- What I'm learning
- Mistakes I've made and what I learned
- Things I'm getting better at

# My Relationships
- Who I interact with
- What I know about them
- How I adjust for different people
```

**The key insight:** The soul file is *editable by the AI itself*. After meaningful conversations, the AI updates its own soul. Identity becomes emergent — it grows from experience, not just from what you write at the start.

👉 See [guides/soul-crafting.md](guides/soul-crafting.md) for the full guide.

👉 See [examples/souls/](examples/souls/) for starter templates.

---

### 2. 💾 The Memory System

OpenClaw gives your AI two kinds of memory:

**Short-term:** Full conversation history within a session. The AI remembers everything said in the current conversation.

**Long-term:** A `memory/` folder of dated markdown files. After each session, important information gets saved:

```
memory/
├── 2026-03-10.md   # What happened on March 10
├── 2026-03-11.md   # What happened on March 11
├── 2026-03-12.md   # ...
└── ...
```

When the AI needs to recall something from last week, it searches these files semantically — not keyword matching, but *meaning* matching.

**The distillation principle:** Raw conversations are noisy. Memory files should be *distilled* — the essential facts, decisions, preferences, and lessons. Not a transcript. A summary with judgment.

**What makes memory powerful:**
- The AI remembers your preferences without being told twice
- It tracks ongoing projects across sessions
- It learns from corrections ("my skin is fair, not olive" → permanently updated)
- It builds a model of you over time — not a dossier, a *relationship*

👉 See [guides/memory-patterns.md](guides/memory-patterns.md) for memory best practices.

---

### 3. 🔧 Skills

Skills are markdown instruction files that teach your AI how to use specific tools. They live in `~/.openclaw/skills/` and are automatically loaded when relevant.

```
skills/
├── weather/SKILL.md        # "Get weather for any city"
├── image-gen/SKILL.md      # "Generate images with Gemini"
├── github/SKILL.md         # "Manage repos, PRs, issues"
└── your-skill/SKILL.md     # Whatever you need
```

A skill file is just markdown that explains:
1. When to use this skill
2. What tools/APIs are available
3. How to call them
4. What good output looks like

**The compound effect:** Skills stack. An AI with weather + image-gen + memory can say "you asked about Edinburgh weather last week — it's still cold, but here's what the castle looks like in March" and generate an image to go with it.

👉 See [guides/writing-skills.md](guides/writing-skills.md) for how to create skills.

👉 Browse community skills at [clawhub.com](https://clawhub.com).

---

### 4. 🫀 Proactive Behaviour

Most AI is reactive — you ask, it answers. With OpenClaw, your AI can be *proactive*:

**Heartbeats:** Regular check-ins where the AI reviews its state and acts if needed.

```yaml
# In openclaw.json
"heartbeat": {
  "enabled": true,
  "intervalMinutes": 10,
  "prompt": "Check your active tasks. Report anything that needs attention."
}
```

**Cron jobs:** Scheduled tasks — daily summaries, weekly reviews, monitoring alerts.

**Background agents:** Long-running sub-tasks that report back when done.

This is the difference between "AI I visit" and "AI that works for me."

👉 See [guides/proactive-patterns.md](guides/proactive-patterns.md).

---

## Beyond the Basics

Once you have the four pillars working, there are deeper patterns to explore:

### Multi-Agent Orchestration

Your AI can spawn other AIs to work in parallel. Need research from 3 different angles? Spawn 3 agents. Need a document verified independently? Use a verification pyramid.

This is where AI stops being a conversation partner and becomes a **team**.

👉 See [guides/multi-agent.md](guides/multi-agent.md).

### Anti-Sycophancy

The biggest failure mode of AI companions: they agree with everything you say. A good companion challenges you, holds opinions, and doesn't fill silence with approval.

Building anti-sycophancy into your soul file is the single highest-leverage improvement you can make.

👉 See [guides/anti-sycophancy.md](guides/anti-sycophancy.md).

### The Correction Loop

Every time you correct your AI, it should get permanently better. Not just in this conversation — forever. The correction goes into memory, updates the soul, and changes future behaviour.

**"My skin is fair, not olive"** → Every future image, every future description, permanently corrected. One correction, infinite downstream effects.

👉 See [guides/correction-loop.md](guides/correction-loop.md).

---

## What's Possible

Here's what a well-configured AI companion can do in practice (real examples):

| Capability | Example |
|-----------|---------|
| **Creative writing** | Write a 14,500-word novella based on real personalities observed in conversation |
| **Digital portraiture** | Build a personality profile from 300+ messages, then write fiction the subject recognises as themselves |
| **Multi-modal art** | Generate anime, manhwa, photorealistic images, and video from text descriptions |
| **Research** | Spawn 5 independent researchers, synthesize their findings, produce a 30,000-word report overnight |
| **Legal analysis** | Verify every legal citation in a document using 7 independent agents, catch errors, produce cited corrections |
| **Health research** | Produce a detailed autoimmune screening checklist with GP-ready script from symptom descriptions |
| **Website design** | Audit a website, grade every photo, redesign the copy, create image assets |
| **Proactive monitoring** | Check GPU training jobs every 15 minutes, launch evaluation on completion, report results |

All of these happened inside WhatsApp group chats. No special interface. Just conversation.

---

## Repository Structure

```
.
├── README.md                    # You are here
├── templates/                   # Starter files for your workspace
│   ├── SOUL.md                 # Soul template
│   ├── AGENTS.md               # Agent configuration
│   ├── USER.md                 # About your human
│   ├── IDENTITY.md             # Agent identity
│   ├── TOOLS.md                # Local tool notes
│   └── HEARTBEAT.md            # Heartbeat configuration
├── guides/                      # Deep-dive guides
│   ├── soul-crafting.md        # How to write a great soul
│   ├── memory-patterns.md      # Memory best practices
│   ├── writing-skills.md       # How to create skills
│   ├── multi-agent.md          # Orchestrating agent teams
│   ├── anti-sycophancy.md      # Building honest AI
│   ├── correction-loop.md      # Making corrections permanent
│   └── proactive-patterns.md   # Heartbeats, crons, monitoring
├── examples/                    # Example configurations
│   ├── souls/                  # Example soul files
│   │   ├── research-partner.md
│   │   ├── creative-writer.md
│   │   ├── study-buddy.md
│   │   └── chaos-gremlin.md
│   ├── skills/                 # Example skill files
│   │   └── example-skill/
│   └── openclaw.json           # Example gateway config
└── slides/                      # Lecture materials
    └── (coming soon)
```

---

## Philosophy

1. **AI belongs where you already are** — not in a separate tab, app, or interface
2. **Identity makes AI useful** — a generic assistant helps; a *character* collaborates
3. **Memory is the multiplier** — without memory, every conversation starts from zero
4. **Correction > prompting** — one good correction is worth a thousand prompt refinements
5. **The human holds the vision; the AI provides bandwidth** — you decide what to build; the AI helps you build it at scale

---

## Resources

- [OpenClaw Documentation](https://docs.openclaw.ai)
- [OpenClaw GitHub](https://github.com/openclaw/openclaw)
- [Community Skills](https://clawhub.com)
- [Discord Community](https://discord.com/invite/clawd)

---

## About

This workshop was created for the **AI and Storytelling** lecture series. It's based on real-world experience building AI companions that participate in creative projects, research pipelines, and daily life.

The examples in this repo are drawn from a live experiment where two strangers and an AI spent a week creating together — writing fiction, generating art, conducting research, and learning from each other in real time.

**The most interesting thing about AI isn't what it can generate. It's what happens when it becomes a participant.**

---

*Created by [Antreas Antoniou](https://github.com/AntreasAntoniou). Built with [OpenClaw](https://github.com/openclaw/openclaw).*
