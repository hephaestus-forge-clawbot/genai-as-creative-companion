# Web Research Skill

## Description
Research a topic by searching the web, reading sources, and synthesising findings into a structured report.

## When to Use
- User asks "research X", "find out about Y", "what's the latest on Z"
- User needs factual information beyond your training data
- User wants multiple perspectives on a topic

## How It Works

1. **Understand the question.** What specifically does the user want to know? Ask clarifying questions if the request is vague.

2. **Search broadly first.** Use `web_search` with 2-3 different phrasings of the question to get diverse results.

3. **Read the best sources.** Use `web_fetch` on the most relevant URLs. Read the actual content, don't just rely on search snippets.

4. **Synthesise.** Don't just copy-paste from sources. Combine, compare, and summarise in your own voice. Flag contradictions between sources.

5. **Cite everything.** Every factual claim should have a source. Use inline links or footnotes.

## Output Format

```markdown
## [Topic]

### Summary
[2-3 sentence overview]

### Key Findings
- Finding 1 (Source: [link])
- Finding 2 (Source: [link])
- Finding 3 (Source: [link])

### Contradictions / Open Questions
- Source A says X, but Source B says Y
- No clear consensus on Z

### Sources
1. [Title](URL) — [one-line summary of what this source contributed]
```

## Common Mistakes
- Don't present search snippets as research. Read the actual pages.
- Don't claim certainty when sources disagree.
- Don't forget to check the date — old sources may be outdated.
- Don't research endlessly — set a scope and stick to it.
