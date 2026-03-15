# Multi-Agent Orchestration — Teams of AI

## The Idea

One AI is a conversation partner. Multiple AIs working in parallel is a **team**.

Your companion can spawn independent agents to work on different aspects of a problem, then synthesize their findings into a single output.

## Why Multiple Agents?

### Independent Verification
One AI might get something wrong. Three AIs working independently are unlikely to make the *same* mistake. When they converge on the same answer, confidence is high. When they diverge, that's where the interesting questions are.

### Parallel Research
Need to analyse something from multiple angles? Instead of asking one AI to consider all perspectives sequentially, spawn agents with different briefs:
- Agent 1: Analyse for technical feasibility
- Agent 2: Analyse for user experience
- Agent 3: Analyse for cost and timeline

Three perspectives in the time it takes one to think.

### The Verification Pyramid

The most powerful pattern: layers of independent work followed by synthesis.

```
Layer 1: 3 independent workers (different approaches)
    ↓
Layer 2: 2 synthesizers (merge the best of each)
    ↓
Layer 3: 1 integrator (final authoritative output)
```

Each layer sees the previous layer's output. Disagreements get resolved with reasoning. The final output has been cross-verified multiple times.

**Real example:** A legal letter was verified by 7 agents in a 3-2-1 pyramid. Three independent researchers checked every legal citation. Two synthesizers merged their findings. One integrator produced the final document. Three critical errors in the original were caught that no single agent found alone.

## Practical Tips

1. **Name your agents.** "Prometheus" is more memorable than "Agent 3." Names create accountability.
2. **Give complete context.** Sub-agents wake up blank. They need everything — the problem, the constraints, the existing work, the standards.
3. **Define success criteria.** What does a good output look like? How will you judge between agents?
4. **Let the loser review the winner.** When one agent's work is chosen, have the other review it. They just spent significant time deep in the problem — that knowledge is worth a few more minutes of review.

## When to Use Multi-Agent

✅ **Verification** — anything where being wrong has consequences (legal, medical, financial)
✅ **Research** — different perspectives on the same question
✅ **Complex creation** — large documents, codebases, designs
✅ **Comparison** — evaluating options against each other

❌ **Simple questions** — "What's the weather?" doesn't need 3 agents
❌ **Speed-critical** — agents take time to spawn and run
❌ **Low-stakes** — if being wrong doesn't matter much, one agent is fine

---

*One AI is a conversation. A team of AIs is a capability.*
