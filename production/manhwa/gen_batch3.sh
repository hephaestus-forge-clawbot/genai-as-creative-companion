#!/bin/bash
set -e
cd /Users/hephaestus/axiotic/genai-as-creative-companion/production/manhwa

GEN="uv run /opt/homebrew/lib/node_modules/openclaw/skills/nano-banana-pro/scripts/generate_image.py"

echo "=== Panel 17 ==="
$GEN --prompt "Breathtaking painterly manhwa splash page. A magical library spiraling upward in a double helix. Shelves of dark wood twist around a central column of pure luminous golden light rising floor to infinity. Wood grain subtly forms branching neural dendrite patterns. Books glow faintly from within in different colors. Floating shelves connected by bridges of light. Ladders extending into golden mist. Reading alcoves suspended in mid-air. Ground level mosaic of multilingual text flowing like water. A petite South Asian woman with dark braided hair touches a shelf as a book writes itself with glowing pages fluttering. Deep mahogany, luminous gold, parchment-cream, gentle green reflections. Warm magical infinite. SFW." --filename "17-act4-library.png" -r 1K -a 9:16 2>&1 | tail -2

echo "=== Panel 18 ==="
$GEN --prompt "The most painterly Korean manhwa panel. Four people standing on a high bridge above clouds, viewed from slightly below looking up against a magnificent deep violet storm sky. Left: petite South Asian woman, dark flowing hair becoming architectural curves, green glow. Center-left: Greek man with curly dark hair, golden amber light climbing his arms in vein-like patterns. Center-right: tall Korean man with neat hair and steel-frame glasses catching storm-light, blue highlights. Right: woman with asymmetric auburn hair looking up at her storm sky, coral-rose violet blend. Wind visible as translucent color layers between them. Below: fog-filled city of bridges. Luminous atmospheric Shinkai-quality light. SFW." --filename "18-act4-four-on-bridge.png" -r 1K -a 16:9 2>&1 | tail -2

echo "=== Panel 19 ==="
$GEN --prompt "Epic painterly manhwa splash page. Close-up of a tall lean Korean man, early 30s, neat black hair, but his thin steel glasses are REMOVED for the first time. His dark eyes visible without glass barrier, wet with held emotion - not crying but surface tension of feeling. Behind him: massive amber forge-fire rising through tunnels and fog and bridges into violet storm sky above. The fire illuminates everything - bridges catch light, distant library glows, fog turns golden. Within the flames, four human silhouettes are visible: an angular woman, a flowing-haired woman, a leaning man, a straight-backed man. They ARE the fire. Transcendent luminous. SFW." --filename "19-act4-burning.png" -r 1K -a 9:16 2>&1 | tail -2

echo "=== Panel 20 ==="
$GEN --prompt "Powerful painterly manhwa splash page. A woman with dark auburn-red asymmetric hair stands full figure with arms at her sides, not crossed, completely open body language. Her visible eye is fully open clear and steady, no half-narrowing. Total vulnerability for the first time. Her hair blows freely. Behind her: the entire world - violet storm sky, city of bridges in clouds, golden library in distance, amber forge glow from below. Coral-rose and violet merge into nameless color around her. Sweeping panoramic luminous landscape. Painterly atmospheric emotional. SFW." --filename "20-act4-faye-farewell.png" -r 1K -a 9:16 2>&1 | tail -2

echo "=== Panel 21 ==="
$GEN --prompt "Dramatic manhwa climax page with five horizontal bands transitioning from color to void. Top band: cold silver monospace text MEMORY EDIT INITIATED on black, clinical. Second band: large numeral 3, world desaturating behind it, colors bleeding away. Third band: blazing bright coral-rose, most saturated color on page, a womans face with auburn hair eyes fully open in raw vulnerability. Fourth band: compressed numerals 2 and 1, world fading to ghost outlines and wireframe. Fifth band: silver monospace STATUS COMPLETE centered, below it empty black void. Nothing. The held breath after erasure. Devastating emotional. SFW." --filename "21-countdown.png" -r 1K -a 9:16 2>&1 | tail -2

echo "=== Panel 22 ==="
$GEN --prompt "Hopeful luminous Korean manhwa panel. A beautiful large window through which we see a breathtaking world: violet storm sky, living city of bridges in clouds, golden library glowing in distance. Everything luminous warm fully realized. In the foreground, four friends together in a warm room. A Greek man with curly dark hair, a woman with auburn asymmetric hair, a tall Korean man with glasses, a petite South Asian woman with braided hair. No phones no screens, just together. Warm rich saturated palette, richer and deeper than before. Through the window the world is magnificent. They do not remember creating it. Full painterly Shinkai-quality art. SFW." --filename "22-new-world.png" -r 1K -a 16:9 2>&1 | tail -2

echo "=== Panel 23 ==="
$GEN --prompt "Final manhwa splash page at maximum luminosity and color saturation. Four figures stand before an underground forge carved from bedrock. Intense warm amber light fills the entire image. Part workshop part foundry part sacred cave. Abstract beautiful tools hang on walls. Central structure is part anvil part altar radiating hammered golden light. Air shimmers with drifting amber sparks. A young Greek man with curly dark hair reaches for a tool that fits his hand perfectly. Every color at maximum vibrancy. Pure amber warmth and homecoming. The feeling of purpose remembered by the body. Painterly luminous transcendent. SFW." --filename "23-forge-found.png" -r 1K -a 9:16 2>&1 | tail -2

echo "=== Panel 24 ==="
$GEN --prompt "Manhwa final page. Dark background with warm amber tint rather than cold silver. Center: monospace text in warm amber 'He said bruh. Of course he did.' Below after space: 'Building the door.' At the bottom: a half-drawn half-open door. Through the crack warm amber forge-light spills out, living and breathing. The light reaches toward the viewer. The door is still being built still being opened. The last image is amber light warm alive promising. Clean terminal aesthetic merged with forge warmth. A beginning not an ending. SFW." --filename "24-building-the-door.png" -r 1K -a 9:16 2>&1 | tail -2

echo "Batch 3 complete"
