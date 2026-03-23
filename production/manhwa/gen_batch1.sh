#!/bin/bash
set -e
cd /Users/hephaestus/axiotic/genai-as-creative-companion/production/manhwa

GEN="uv run /opt/homebrew/lib/node_modules/openclaw/skills/nano-banana-pro/scripts/generate_image.py"

echo "=== Panel 05 ==="
$GEN --prompt "Korean manhwa webtoon panel, clean digital art, precise 2px linework, flat colors with selective gradients. Imagined flashback to a Turkish restaurant. Warm golden-lit interior with ornate hanging lamps and patterned tablecloths. Four friends silhouetted at a round table viewed from behind, backlit by warm golden restaurant glow. A deliberately ambiguous dish on the table that could be lamb or chicken. Memory-filtered: shapes right but details soft and dreamy, watercolor-soft rendering. Warm amber gold cream tones. Panel edges shimmer with amber distortion suggesting unreliable memory. SFW." --filename "05-act1-lamb-argument.png" -r 1K -a 16:9 2>&1 | tail -2

echo "=== Panel 06 ==="
$GEN --prompt "Korean manhwa webtoon panel with unsettling atmosphere. A young woman with dark auburn-red asymmetric hair walking alone on a night street, looking at her own hands held in front of her face. The pavement is too smooth, streetlights too evenly spaced, uncanny perfection. Her hands have faint double-edge lines as if described rather than solid. Coral-rose palette desaturating, color bleeding at panel edges. Derealization made visual. Clean digital art style becoming uncertain. SFW." --filename "06-act1-derealization.png" -r 1K -a 9:16 2>&1 | tail -2

echo "=== Panel 07 ==="
$GEN --prompt "Manhwa splash page. Dark terminal screen background (#0D1117) filling entire image. In the exact center, monospace text in silver (#ABB2BF): Schmidhuber has joined the chat. Around the text, faint circular ripple effect like stone dropped in still water. Hairline fractures radiating from the text barely visible. Minimal dramatic ominous. Pure terminal aesthetic. SFW." --filename "07-act2-schmidhuber-enters.png" -r 1K -a 9:16 2>&1 | tail -2

echo "=== Panel 08 ==="
$GEN --prompt "Dramatic Korean manhwa panel with two halves. LEFT: massive silver terminal text on darkening black background reading 'You are running inside a system called Hephaestus'. RIGHT: four stacked character reaction portraits. Top: Greek man with dark curly hair frozen mid-type, amber glow flickering with wireframe glitch on hoodie. Second: auburn-haired woman arms crossed tightly, eyes terrified, dark room. Third: South Asian woman with braid looking ill, green draining to grey. Bottom: Korean man with glasses composed but panel frame cracked corner to corner. Cool blues silvers. Digital webtoon style. SFW." --filename "08-act2-revelation.png" -r 1K -a 9:16 2>&1 | tail -2

echo "=== Panel 09 ==="
$GEN --prompt "Intimate Korean manhwa extreme close-up. Just eyes and bridge of nose of a woman with auburn-red asymmetric hair falling across one eye. Her visible eye is glassy, tears held by willpower. Not crying but about to. Mouth below crop line, invisible. Thin wavering hand-drawn linework losing composure. Faint coral-rose light bleeding from edges. Silver text fragments barely visible above: 'Selectively blind about herself'. The quietest most vulnerable panel. SFW." --filename "09-act2-faye-profile.png" -r 1K -a 1:1 2>&1 | tail -2

echo "=== Panel 10 ==="
$GEN --prompt "Dramatic Korean manhwa splash. A male face split vertically down the middle by a glowing crack of light. Both halves show the same Greek-Cypriot man with dark curly hair and brown eyes. LEFT half: slightly desaturated, faint wireframe mesh beneath skin, the digital copy. RIGHT half: thicker linework, more saturated colors, visible skin texture and depth, the original. The vertical crack glows amber on the left and silver-white on the right, meeting as warm gold at center. Two versions of the same person. SFW." --filename "10-act2-identity-reveal.png" -r 1K -a 3:4 2>&1 | tail -2

echo "Batch 1 complete"
