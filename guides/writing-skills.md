# Writing Skills — Teaching Your AI New Abilities

## What Is a Skill?

A skill is a markdown file that teaches your AI how to use a specific tool or perform a specific task. It lives in `~/.openclaw/skills/your-skill/SKILL.md`.

When a user's request matches a skill's description, the AI reads the skill file and follows its instructions.

## Anatomy of a Skill

```markdown
# Skill Name

## Description
One sentence: what does this skill do and when should it be used?

## When to Use
- Trigger phrases: "generate an image", "make me a picture"
- Context: when the user wants visual output

## How It Works
Step-by-step instructions for the AI:
1. Parse the user's request for subject, style, mood
2. Construct a prompt following these guidelines: ...
3. Call the API with: ...
4. Send the result to the user

## Examples
Input: "Make me a cyberpunk portrait"
→ Prompt construction: ...
→ API call: ...
→ Output: [image]

## Common Mistakes
- Don't: use overly long prompts (>200 words)
- Don't: forget to specify aspect ratio
- Do: always include style keywords
```

## Best Practices

1. **Be specific.** Vague skills produce vague results. "Generate images" is weak. "Generate images using Gemini's imagen model with structured prompts optimized for photorealism" is strong.

2. **Include examples.** Show the AI what good input→output looks like. Examples teach better than rules.

3. **Document failure modes.** What goes wrong? API rate limits? Content filters? Timeout behavior? Help the AI handle errors gracefully.

4. **Keep it focused.** One skill = one capability. Don't combine image generation and music generation into one skill.

5. **Test iteratively.** Write a skill, try it, see where it fails, refine. Skills improve with use.

## Finding Skills

- [ClawhHub](https://clawhub.com) — community skill marketplace
- OpenClaw built-ins: weather, GitHub, video-frames, voice-call
- Build your own for any API or workflow you use regularly

---

*Skills are how your AI goes from "I can chat" to "I can do anything."*
