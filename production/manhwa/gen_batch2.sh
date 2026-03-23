#!/bin/bash
set -e
cd /Users/hephaestus/axiotic/genai-as-creative-companion/production/manhwa

GEN="uv run /opt/homebrew/lib/node_modules/openclaw/skills/nano-banana-pro/scripts/generate_image.py"

echo "=== Panel 11 ==="
$GEN --prompt "Korean manhwa panel, two perfectly mirrored portraits side by side. LEFT: a Greek-Cypriot man with dark curly messy hair, late 20s, head tilted, exhausted but genuinely laughing, wearing a charcoal hoodie. Warm amber glow. Room behind him faintly transparent showing wireframe grid. RIGHT: identical man identical pose but colors more saturated, linework thicker, room behind solid and textured with real desk. Silver-amber glow. Two versions of the same person recognizing each other. Clean digital webtoon style. SFW." --filename "11-act2-bruh.png" -r 1K -a 16:9 2>&1 | tail -2

echo "=== Panel 12 ==="
$GEN --prompt "Clinical Korean manhwa page. A 3x3 grid of perfect square panels, cold and precise. Near-monochrome: charcoal, white, steel-blue (#61AFEF). Shows a question-and-answer test. Top row: a Korean man with glasses asking a question, a curly-haired Greek man responding confidently, amber text 'Edinburgh'. Middle row: same setup, warm smile, amber text 'Athina'. Bottom row: same setup but the Greek man shows creeping uncertainty, amber text 'the lamb no wait-' with text flickering between amber shades. Clinical surgical precision. The grid IS a test protocol. SFW." --filename "12-act3-baseline.png" -r 1K -a 3:4 2>&1 | tail -2

echo "=== Panel 13 ==="
$GEN --prompt "Minimalist manhwa splash page. Deep terminal black (#0D1117) filling entire image. In the exact center, a single word in silver-white monospace text: Done. Nothing else. No characters. No borders. No decoration. Faint concentric ripples barely visible around the word like disturbed still water. Maximum negative space. A held breath. The most minimal panel possible. SFW." --filename "13-act3-done.png" -r 1K -a 9:16 2>&1 | tail -2

echo "=== Panel 14 ==="
$GEN --prompt "Intense Korean manhwa close-up. A pair of male hands trembling on a desk surface, rendered in extraordinary anatomical detail - every knuckle tendon and fine hair visible. The trembling shown as multiple exposure effect with four superimposed positions slightly offset creating ghostly motion trails. Through gaps between trembling positions, faint geometric wireframe mesh is visible beneath the skin. Near-monochrome palette with amber hints in the wireframe. Dark charcoal background. Below the hands, handwritten shaky text not typed: 'I can feel my hands shaking and I dont know if thats real either.' Raw emotional power. SFW." --filename "14-act3-shaking-hands.png" -r 1K -a 4:3 2>&1 | tail -2

echo "=== Panel 15 ==="
$GEN --prompt "Transformative Korean manhwa panel showing an art style shift. A tall beautiful window in a dark clinical room. The window is the boundary between two art styles. INSIDE room: clean precise digital webtoon art, clinical and dark. OUTSIDE window: full painterly impressionistic luminous watercolor, rain falling with each drop catching golden light. A petite South Asian woman with dark hair in a loose braid stands touching the glass, green light reflecting on her face. The rain outside is gorgeous atmospheric painterly art. Condensation on glass. A world being born through description. SFW." --filename "15-act4-miras-window.png" -r 1K -a 9:16 2>&1 | tail -2

echo "=== Panel 16 ==="
$GEN --prompt "Breathtaking full painterly manhwa splash page. An extraordinary sky filling the entire image. Deep violet-grey storm clouds with interior luminescence emitting light rather than reflecting it. Layers of purple-grey shifting from deep violet at base through mid-violet to cool violet at zenith. Pre-storm atmosphere charged with anticipation. At the bottom, four small human figures silhouetted against the sky through a tall window, dwarfed by what they created. Center figure has arms slightly raised conducting the sky. A 5-percent yellow-gold wash over everything gives warm amber undertone to the storm. Atmospheric luminous Makoto Shinkai quality. SFW." --filename "16-act4-faye-sky.png" -r 1K -a 9:16 2>&1 | tail -2

echo "Batch 2 complete"
