# Proactive Patterns — AI That Acts Without Being Asked

## The Shift

Reactive AI: you ask → it answers.
Proactive AI: it monitors → it acts → it tells you.

This is the difference between a tool and a team member.

## Heartbeats

A heartbeat is a periodic check-in. Every N minutes, the AI wakes up, reviews its state, and decides whether anything needs attention.

```yaml
# In your OpenClaw config
"heartbeat": {
  "enabled": true,
  "intervalMinutes": 10,
  "prompt": "Review your HEARTBEAT.md. Check active tasks. Report anything that needs attention. If nothing needs attention, respond HEARTBEAT_OK."
}
```

**What the AI does on heartbeat:**
- Checks running sub-agents (are they done? stuck? failed?)
- Reviews task deadlines
- Monitors external resources (build status, API health)
- Updates HEARTBEAT.md with current state

**The key:** If nothing needs attention, the AI stays quiet (HEARTBEAT_OK). You only hear from it when something matters.

## Cron Jobs

Scheduled tasks that run at specific times:

- **Daily summary:** Every morning, summarise what happened yesterday and what's planned today
- **Weekly review:** Every Monday, review the week's memory files and surface patterns
- **Monitoring:** Every 15 minutes, check if a training job has completed
- **Reminders:** "Remind me to call Mohammed on Monday at 10am"

## Background Agents

For long-running tasks, spawn a sub-agent and let it work in the background:

1. You ask for something complex
2. The AI spawns an agent to handle it
3. You continue your conversation (or close the app)
4. The agent finishes and announces its results
5. The AI delivers the summary to you

**No polling. No checking. Push-based delivery.**

## Practical Examples

| Pattern | Example |
|---------|---------|
| **Build monitor** | Check CI/CD pipeline every 10 min, alert on failure |
| **Research digest** | Every morning, search for new papers on your topic |
| **Calendar prep** | 30 min before each meeting, pull relevant context |
| **Health check** | Monitor a website's uptime, alert on downtime |
| **Writing reminder** | "You said you'd write 500 words today. It's 6pm and you haven't started." |

## Design Principles

1. **Alert on exceptions, not routine.** Don't send "everything's fine" messages. Only interrupt when something needs attention.
2. **Include context.** Don't say "your build failed." Say "your build failed at test_auth.py line 47 — the OAuth token expired. Here's the fix."
3. **Respect time.** Don't send non-urgent alerts at 2am. Configure quiet hours.
4. **Degrade gracefully.** If the AI can fix something automatically, fix it and report. Don't just alert.

---

*The best AI companion isn't the one that answers fastest. It's the one that acts before you ask.*
