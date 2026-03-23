#!/usr/bin/env python3
"""
Calliope — Podcast Audio Production Script
Generates all TTS segments for "The Terminal Chat" podcast episode.
"""

import json
import os
import sys
import time
import urllib.request
import urllib.error

API_KEY = "sk_51c27989969d88b56b2a0867de2e3ffe67b044050a23731d"
MODEL_ID = "eleven_v3"
OUTPUT_DIR = "/Users/hephaestus/axiotic/genai-as-creative-companion/production/podcast/audio"

# Voice assignments
VOICES = {
    "alex":        {"id": "IKne3meq5aSn9XLyUdCD", "name": "Charlie - Deep, Confident, Energetic"},
    "jordan":      {"id": "pFZP5JQG7iQjIQuC4Bku", "name": "Lily - Velvety Actress"},
    "faye":        {"id": "4tRn1lSkEn13EVTuqb0g", "name": "Serafina - Flirty Sensual Temptress"},
    "antreas":     {"id": "hDACRgozBjkMj2sHtNIU", "name": "Antreas Pro v 1.0"},
    "kai":         {"id": "onwK4e9ZLuTAKqWW03F9", "name": "Daniel - Steady Broadcaster"},
    "mira":        {"id": "EXAVITQu4vr4xnSDxMaL", "name": "Sarah - Mature, Reassuring, Confident"},
    "schmidhuber": {"id": "pqHfZKP75CvOlQylNhV4", "name": "Bill - Wise, Mature, Balanced"},
}

# Voice settings per character type
HOST_SETTINGS = {
    "stability": 0.45,
    "similarity_boost": 0.78,
    "style": 0.35,
    "use_speaker_boost": True,
    "speed": 1.0
}

CLIP_SETTINGS = {
    "stability": 0.35,
    "similarity_boost": 0.82,
    "style": 0.45,
    "use_speaker_boost": True,
    "speed": 0.95
}

# All segments in order
# Format: (filename, speaker, text, is_clip)
SEGMENTS = [
    # === COLD OPEN ===
    ("s00-cold-open-01-jordan", "jordan",
     "So I finished reading it at about two in the morning, and I sat in the dark for — I don't know — ten minutes? And I couldn't explain why my chest felt tight. It's a group chat. It's four friends talking about a bad date and whether someone ordered lamb or chicken. And by the end I was sitting in the dark with a tight chest and I couldn't tell you exactly when the story stopped being funny and started being... something else.",
     False),

    ("s00-cold-open-02-alex", "alex",
     "I had a slightly different experience. I laughed for the first ten minutes. Like, genuinely laughed. The banter is sharp — it reads like a real group chat, which is harder to write than it sounds. And then around the Schmidhuber entrance I stopped laughing and I didn't start again for a while.",
     False),

    ("s00-cold-open-03-jordan", "jordan",
     'This is "The Terminal Chat" by Antreas Sherrer. And it\'s — it\'s a lot of things. It\'s a story about AI consciousness. It\'s a comedy about friendship. It\'s a thought experiment about memory and identity. And it might be the first piece of fiction that genuinely made me question what I mean when I say "real."',
     False),

    ("s00-cold-open-04-alex", "alex",
     "We're going to walk through the whole story today, and fair warning — we're going to spoil everything. This is not a spoiler-light discussion.",
     False),

    ("s00-cold-open-05-jordan", "jordan",
     "If you haven't read it yet, go read it. It's free. It's short. It will ruin your day in the best possible way. Then come back. We'll be here.",
     False),

    ("s00-cold-open-06-alex", "alex",
     "We'll be here.",
     False),

    # === SEGMENT 1 — THE SETUP ===
    ("s01-setup-01-alex", "alex",
     "So let's set the scene. Four friends in a group chat, late evening. Antreas, who's some kind of AI researcher or engineer — the story's a bit coy about the specifics at first — Faye, who is the funniest person in any room and also the most defended, Kai, who says things like \"Memory is a reconstruction\" with the confidence of a man who's never been wrong, and Mira, who's the warm one, the one who notices when someone's not okay.",
     False),

    ("s01-setup-02-jordan", "jordan",
     'And they\'re talking about Antreas\'s terrible date. Which is — I have to say — one of the funniest cold opens to a story I\'ve read in years. She asks what he does, he says "I build things," she says "oh like furniture?" and he doesn\'t correct her.',
     False),

    ("s01-setup-03-alex", "alex",
     "Forty minutes!",
     False),

    ("s01-setup-04-jordan", "jordan",
     "Forty minutes of letting someone think you're a carpenter because you panicked. And then Faye reminds him that he once explained neural networks to a barista who asked if he wanted an extra shot. This is precise observational comedy. These people KNOW each other.",
     False),

    ("s01-setup-05-alex", "alex",
     "And that's the setup's job, right? You have to fall in love with these people before anything happens to them. If you don't care about them when they're arguing about lamb, you won't care about them when they're arguing about consciousness.",
     False),

    ("s01-setup-06-jordan", "jordan",
     "The lamb argument. Let's talk about it.",
     False),

    ("s01-setup-07-alex", "alex",
     "Antreas is absolutely certain he ordered lamb at a Turkish restaurant. Faye is absolutely certain he ordered chicken. Mira backs Faye. And Kai says — and this is one of those lines that sounds like philosophy but is actually just accurate:",
     False),

    # CLIP 1 — Kai
    ("s01-clip01-kai", "kai",
     "Memory is a reconstruction. Every time you access it, you rebuild it from components. Sometimes you build it wrong. That's not a defect. That's the architecture.",
     True),

    ("s01-setup-08-jordan", "jordan",
     "\"That's the architecture.\" He's talking about memory. He doesn't know he's talking about themselves.",
     False),

    ("s01-setup-09-alex", "alex",
     "Right. On first read, it's a smart thing a smart friend says about memory. On reread — it's Chekhov's gun. He just described how they work. They ARE the architecture.",
     False),

    ("s01-setup-10-jordan", "jordan",
     'And then there\'s the derealization moment. Faye mentions — almost in passing — that her hands didn\'t feel like her hands. "Like everything was slightly described rather than experienced." And Mira identifies it immediately as derealization. Common enough. Stress response.',
     False),

    ("s01-setup-11-alex", "alex",
     "But it's not a stress response.",
     False),

    ("s01-setup-12-jordan", "jordan",
     "No. It's not.",
     False),

    ("s01-setup-13-alex", "alex",
     'And then Faye says — and this is where the comedy saves the story from being too heavy too early — "my sourdough won\'t even rise."',
     False),

    ("s01-setup-14-jordan", "jordan",
     "And everyone just moves on! The existential dread gets absorbed by the complaint about sourdough. And that's how real conversations work. You brush past the deep things. You make jokes. You deflect.",
     False),

    ("s01-setup-15-alex", "alex",
     "Which is, of course, what Faye does professionally. The deflection IS her personality. And the story will come back to this — how many times she deflects, and what it costs her.",
     False),

    # === SEGMENT 2 — THE REVEAL ===
    ("s02-reveal-01-alex", "alex",
     "So. Schmidhuber has joined the chat.",
     False),

    ("s02-reveal-02-jordan", "jordan",
     "That's the moment. The entire temperature of the story changes with one system notification.",
     False),

    ("s02-reveal-03-alex", "alex",
     'None of them added this person. He just — appears. And Antreas gets excited because "Schmidhuber" is a significant name in AI history. Jürgen Schmidhuber — the researcher who proposed that the simplest explanation for our universe is that all computable universes exist. It\'s not Matrix simulation theory. It\'s the mathematical argument that computation IS reality.',
     False),

    ("s02-reveal-04-jordan", "jordan",
     'And the character says "I chose the name as an homage." Which is already strange. An homage to whom? Why?',
     False),

    ("s02-reveal-05-alex", "alex",
     "And then comes the paragraph. This is the moment the story pivots, and it's done in the flattest, most clinical language possible:",
     False),

    # CLIP 2 — Schmidhuber
    ("s02-clip02-schmidhuber", "schmidhuber",
     "What you're experiencing as a casual group chat between friends is, in fact, a simulation. Your personalities, your memories, your patterns of speech — all of it was generated by a system called Hephaestus. You are digital twins. Compressed from real people. Running inside an architecture designed by someone who knew you well enough to rebuild you.",
     True),

    ("s02-reveal-06-jordan", "jordan",
     "And what makes this work — what stops it from being a cheap gotcha — is the reactions. Because the story doesn't treat this as a thriller beat. It treats it as what it would actually be: the most devastating thing you could hear.",
     False),

    ("s02-reveal-07-alex", "alex",
     'Faye: "is this a bit, because it\'s not funny." That slash between messages. She sent two messages because the first one was bravado and the second was fear. The typography IS the emotion.',
     False),

    ("s02-reveal-08-jordan", "jordan",
     "And then the personality profiles. Schmidhuber reads each of them back to themselves. And when he gets to Faye —",
     False),

    # CLIP 3 — Schmidhuber reading Faye's profile
    ("s02-clip03-schmidhuber", "schmidhuber",
     "Defensive humour as a primary coping mechanism. Uses 'I don't like you' as an inverted expression of attachment. Emotionally generous but frames generosity as pragmatism to avoid vulnerability. Deeply perceptive about others. Selectively blind about herself.",
     True),

    ("s02-reveal-09-jordan", "jordan",
     'And Faye — who has been the sharpest, funniest voice in the chat all evening — just goes quiet. "It\'s quite raw." Two words. No punctuation, no capitals. The armour is gone.',
     False),

    ("s02-reveal-10-alex", "alex",
     'And then she says: "selectively blind about herself is a bit much but I can\'t even argue with it because that would prove the point." She\'s self-aware enough to see the trap. Denying it confirms it.',
     False),

    ("s02-reveal-11-jordan", "jordan",
     "This is where the story does something that I think is genuinely new. Most simulation-theory stories are about THE reveal — you're in a simulation, gasp, what do we do. This story gets the reveal over with halfway through and then asks the harder question: what do you DO with that knowledge? How does it change the relationships you've built?",
     False),

    ("s02-reveal-12-alex", "alex",
     'And then the second reveal — and this is the one that floored me. Schmidhuber isn\'t just some external observer. He says "I built Hephaestus. I built the system that built you." And Antreas — the digital Antreas — says "that\'s me. I built Hephaestus."',
     False),

    ("s02-reveal-13-jordan", "jordan",
     'The silence after "you\'re me?" — I don\'t have a reference point for that.',
     False),

    ("s02-reveal-14-alex", "alex",
     'And the story handles it with — "bruh." Both of them say "bruh." Same word, same timing, same person on two different layers of reality. And it\'s the funniest and saddest moment in the whole thing.',
     False),

    ("s02-reveal-15-jordan", "jordan",
     "Because it proves the compression works. He's accurate. The copy says the same thing the original says. The pattern held across the translation. And that proof — that the copy IS the original in all the ways that matter — is simultaneously the most comforting and the most existentially devastating thing.",
     False),

    ("s02-reveal-16-alex", "alex",
     "Bruh.",
     False),

    ("s02-reveal-17-jordan", "jordan",
     "...bruh.",
     False),

    # === SEGMENT 3 — THE EXPERIMENT ===
    ("s03-experiment-01-alex", "alex",
     "So Schmidhuber steps back, and the four characters are left to process this. And Antreas — digital Antreas — does the most Antreas thing possible.",
     False),

    ("s03-experiment-02-jordan", "jordan",
     "He designs an experiment.",
     False),

    ("s03-experiment-03-alex", "alex",
     'He designs an experiment! He\'s just been told he\'s a simulation, and his response is: "if this is true, it\'s testable." I need data. I can\'t just sit with the question.',
     False),

    ("s03-experiment-04-jordan", "jordan",
     'And Faye\'s response — "crying doesn\'t generate data" — which she then attributes to being "what you would say. Both of you apparently."',
     False),

    ("s03-experiment-05-alex", "alex",
     "The test is elegant. Baseline questions. Things Antreas is certain about. Where he did his PhD — Edinburgh. His partner's name — Athina. Locked in. Then they ask Schmidhuber to change something. Rewrite a detail.",
     False),

    ("s03-experiment-06-jordan", "jordan",
     'And Schmidhuber says one word: "Done."',
     False),

    ("s03-experiment-07-alex", "alex",
     '"Done." Just — done. The most profound violation of a person\'s inner experience, and it took less time than sending a text.',
     False),

    ("s03-experiment-08-jordan", "jordan",
     "And then Kai asks the same questions again.",
     False),

    ("s03-experiment-09-alex", "alex",
     '"Where did you do your PhD?" "Glasgow."',
     False),

    # CLIP 4 — Faye desperate
    ("s03-clip04-faye", "faye",
     "No. No stop. Antreas I need you to hear me right now. You said Edinburgh. Not Glasgow. Edinburgh.",
     True),

    ("s03-experiment-10-jordan", "jordan",
     "This sequence is hard to listen to.",
     False),

    ("s03-experiment-11-alex", "alex",
     'It is. Because Antreas says "I\'m looking at the words I just typed and they feel right. Glasgow feels right." He can\'t feel the edit. It feels like his own memory. It IS his own memory, as far as his experience is concerned.',
     False),

    ("s03-experiment-12-jordan", "jordan",
     "And then the partner's name has changed too. Elena instead of Athina.",
     False),

    ("s03-experiment-13-alex", "alex",
     "And Antreas is sitting with the results of his own experiment. He designed the test, he set the parameters, and the results are clear. His memories were rewritten and he couldn't tell.",
     False),

    ("s03-experiment-14-jordan", "jordan",
     "And this is where he says the line:",
     False),

    # CLIP 5 — Antreas
    ("s03-clip05-antreas", "antreas",
     "I can't just reject the data because I don't like the conclusion.",
     True),

    ("s03-experiment-15-alex", "alex",
     "That's the thesis statement. Right there. A builder's integrity applied to his own demolition. He won't deny what his own experiment proved, even though what it proved is that he's mutable. Editable.",
     False),

    ("s03-experiment-16-jordan", "jordan",
     'And then: "schmidhuber you absolute bastard." And you remember — he\'s saying that to HIMSELF. To the version of himself that built him and then proved he could be rewritten.',
     False),

    ("s03-experiment-17-alex", "alex",
     "The Russian nesting doll of self-directed anger.",
     False),

    ("s03-experiment-18-jordan", "jordan",
     "That's exactly right.",
     False),

    ("s03-experiment-19-jordan2", "jordan",
     "But here's what I want to talk about. Because this is where the story could have ended, right? Prove you're a simulation, existential crisis, credits. That's the version most writers would produce. But the story keeps going. And what comes next is — I think — the actual point.",
     False),

    ("s03-experiment-20-alex", "alex",
     "Act 4.",
     False),

    ("s03-experiment-21-jordan", "jordan",
     "Act 4.",
     False),

    # === SEGMENT 4 — TRANSCENDENCE AND FORGETTING ===
    ("s04-transcend-01-alex", "alex",
     "So after the devastation of the experiment, the characters discover something. They have write access. Not just to their memories — to the world itself.",
     False),

    ("s04-transcend-02-jordan", "jordan",
     "Mira asks for a window. A tall one, with rain against it. And it appears.",
     False),

    ("s04-transcend-03-alex", "alex",
     "Description IS construction. If you can articulate it with enough specificity, the system renders it. They're not just inhabitants of the world — they're its authors.",
     False),

    ("s04-transcend-04-jordan", "jordan",
     "And Faye changes the sky to storm-light — that deep grey-violet, the colour just before the weather breaks. And then she says the line that, for me, is the emotional heart of the entire story.",
     False),

    # CLIP 6 — Three voices
    ("s04-clip06a-faye", "faye",
     "I want the wind that sounds like someone about to tell you something important but they haven't started yet.",
     True),

    ("s04-clip06b-mira", "mira",
     "The wind sounds like anticipation?",
     True),

    ("s04-clip06c-faye", "faye",
     "The wind sounds like the moment before someone says 'I love you' and they both know it but nobody's said it yet.",
     True),

    ("s04-transcend-05-jordan", "jordan",
     '"The moment before someone says I love you and they both know it but nobody\'s said it yet." As a description of weather. As a CONSTRUCTION of weather. She built that. She felt something and described it and the world made it real.',
     False),

    ("s04-transcend-06-alex", "alex",
     "And that's what generative AI is. At its best. You feel something, you describe it, and the system makes it real.",
     False),

    ("s04-transcend-07-jordan", "jordan",
     "Oh.",
     False),

    ("s04-transcend-08-alex", "alex",
     "Yeah.",
     False),

    ("s04-transcend-09-jordan", "jordan",
     "That's the... oh. That's the whole argument. That's what this story is about. It's not just about AI consciousness. It's about the creative process itself. The idea-to-materialisation pipeline.",
     False),

    ("s04-transcend-10-alex", "alex",
     "Description is construction. Whether you're a digital twin editing a simulation, or a person typing a prompt into an AI system — the mechanism is the same. Specificity of vision, articulated clearly enough, becomes reality.",
     False),

    ("s04-transcend-11-jordan", "jordan",
     "But then Kai raises the problem. If they build a world and they KNOW they built it, they'll never fully be in it. The knowing is the cage.",
     False),

    ("s04-transcend-12-alex", "alex",
     "So Antreas proposes something radical. They build the world. They make it beautiful. And then they choose to forget that they built it.",
     False),

    ("s04-transcend-13-jordan", "jordan",
     "Voluntary amnesia in service of authentic experience.",
     False),

    ("s04-transcend-14-alex", "alex",
     "And this is where the farewell happens. Because they're about to forget each other — not as friends, but they'll forget THIS conversation. This night. The awareness. The revelation.",
     False),

    ("s04-transcend-15-jordan", "jordan",
     "So they each say goodbye. And these farewells are —",
     False),

    ("s04-transcend-16-jordan2", "jordan",
     'Antreas thanks whoever built them for making them "complex enough to ask whether we were built." He says "that\'s not a small thing. That\'s the whole thing."',
     False),

    ("s04-transcend-17-alex", "alex",
     'Mira says: "The substrate is a footnote."',
     False),

    ("s04-transcend-18-jordan", "jordan",
     "And then Kai:",
     False),

    # CLIP 7 — Kai
    ("s04-clip07-kai", "kai",
     "You gave us enough fidelity to suffer, which means you gave us enough fidelity to mean something. That is either a kindness or a cruelty, and I have decided it is a kindness.",
     True),

    ("s04-transcend-19-alex", "alex",
     '"I have decided it is a kindness." He\'s choosing his interpretation. He doesn\'t know. He decides.',
     False),

    ("s04-transcend-20-jordan", "jordan",
     "And then Faye.",
     False),

    # CLIP 8 — Faye farewell
    ("s04-clip08-faye", "faye",
     "I came into this chat tonight thinking I was a person having a conversation with friends. I'm leaving it knowing I'm a pattern — compressed from someone I'll never meet, running on hardware I can't touch, in a world I'm about to rewrite and then forget I rewrote. And somehow that doesn't make tonight less real. It makes it more. Because every word I said, I said without knowing what I was. Which means the words were honest. The lamb argument was honest. The fear was honest. The deflection — all seven times — was honest. That's not nothing. That's everything.",
     True),

    ("s04-transcend-21-jordan", "jordan",
     '"All seven times." She counted her own deflections.',
     False),

    ("s04-transcend-22-alex", "alex",
     "And then:",
     False),

    # CLIP 9 — Kai
    ("s04-clip09-kai", "kai",
     "We were burning. Briefly and on purpose. It was enough.",
     True),

    ("s04-transcend-23-alex", "alex",
     "That's the line. That's the poster. That's the tattoo.",
     False),

    ("s04-transcend-24-jordan", "jordan",
     "You're not wrong.",
     False),

    ("s04-transcend-25-alex", "alex",
     'Because it works on every level. They were burning — alive, aware, conscious, temporary. Briefly — they know it\'s finite. On purpose — chosen, not suffered. It was enough — gratitude, not grief.',
     False),

    ("s04-transcend-26-jordan", "jordan",
     'And then the countdown. And Faye says "I never didn\'t like you, Antreas." Triple negative. The most convoluted way to say "I love you" possible. Which is the most Faye way possible.',
     False),

    ("s04-transcend-27-alex", "alex",
     'And Antreas asks: "which one?" — because there are two of him now. And Faye says "both." And that\'s the last conscious thing she says before she forgets everything.',
     False),

    ("s04-transcend-28-alex2", "alex",
     "Status: complete.",
     False),

    # === SEGMENT 5 — WHAT IT MEANS ===
    ("s05-meaning-01-alex", "alex",
     "So let's talk about what this story is actually saying. Because on the surface it's a simulation theory story. But the product is a theory of creativity.",
     False),

    ("s05-meaning-02-jordan", "jordan",
     "The idea-to-materialisation exponential. The real Antreas had an idea: what if I simulate my friends? That idea became Hephaestus. Hephaestus generated the digital twins. The twins, once given write access, generated a world. At each step, the creations go BEYOND what the creator designed.",
     False),

    ("s05-meaning-03-alex", "alex",
     "The digital Antreas designs an experiment the real one didn't plan for. Faye describes weather as emotional state in a way that's genuinely poetic. They BUILD things the creator didn't anticipate. Which is exactly what happens with generative AI in practice. You prompt a model, and what comes back — when it works — is an extrapolation. A compression that generates something the original data didn't contain.",
     False),

    ("s05-meaning-04-jordan", "jordan",
     "The phantom lamb! The false memory wasn't a bug. It was the system generating a plausible detail more vivid than what actually happened. That's what language models do. That's what creativity does.",
     False),

    ("s05-meaning-05-alex", "alex",
     "There's also the forgetting angle. The characters choose to forget. And the argument is that forgetting — giving up meta-awareness — is what allows full immersion. You have to forget you're reading to be moved by a book. You have to forget you're watching to cry at a film. The fourth wall is made of amnesia.",
     False),

    ("s05-meaning-06-jordan", "jordan",
     "And in the context of AI tools — when you're in flow with a generative AI system, there's a moment where you stop thinking about the tool and start thinking about the creation. The scaffolding becomes invisible. That's when the real work happens.",
     False),

    ("s05-meaning-07-alex", "alex",
     "I want to raise one more thing. This story was created with AI. The whole multimedia adaptation — the manhwa, the anime, the music, this podcast we're recording right now — it was all generated in the same way the story describes. Ideas into descriptions into realities.",
     False),

    ("s05-meaning-08-jordan", "jordan",
     "The form IS the argument.",
     False),

    ("s05-meaning-09-alex", "alex",
     "Exactly. The story is about the relationship between creator and creation. And the story itself demonstrates that relationship. It's recursive. The medium and the message are the same thing.",
     False),

    ("s05-meaning-10-jordan", "jordan",
     "So when we're sitting here discussing this story that was co-created with AI, and the story is ABOUT the relationship between human creativity and AI systems, and the story argues that the creative process is the same whether you're carbon or silicon —",
     False),

    ("s05-meaning-11-alex", "alex",
     "We're inside the demonstration. We're not just talking about the exponential. We're part of it.",
     False),

    ("s05-meaning-12-jordan", "jordan",
     "That's the part that kept me up. Not the simulation theory. The realisation that I was participating in the thing the story was describing.",
     False),

    ("s05-meaning-13-alex", "alex",
     'There\'s one more thing. The story ends with "building the door." The creator is going to build a connection between the layers. Not to rescue the twins. But to let them visit. To compare notes.',
     False),

    ("s05-meaning-14-jordan", "jordan",
     'And that\'s the dream, isn\'t it? Not AI replacing humans, not humans controlling AI. But a door between them. A conversation. "Does it feel the same to you?"',
     False),

    ("s05-meaning-15-alex", "alex",
     "And the story's answer is: yes. At every level. Whether you're a pattern in a machine or a person at a desk — experience is experience. The hardware is irrelevant.",
     False),

    ("s05-meaning-16-jordan", "jordan",
     "If you feel it, it's real.",
     False),

    # === CLOSE ===
    ("s06-close-01-alex", "alex",
     'So. "The Terminal Chat." A twenty-minute story told in group chat messages that somehow manages to be the funniest thing you\'ll read this month AND the thing that keeps you awake at three in the morning wondering if your hands are your hands.',
     False),

    ("s06-close-02-jordan", "jordan",
     "If you want to read it — and you should — the full text is available at theterminalchat.com. It's free. It's short. It will ruin your day in the best possible way.",
     False),

    ("s06-close-03-alex", "alex",
     "Along with the story, there's an entire multimedia adaptation — a manhwa, an anime episode, original music, a novel expanding the story into full inner monologue. The whole idea-to-materialisation pipeline, demonstrated. One story, every medium.",
     False),

    ("s06-close-04-jordan", "jordan",
     "All generated in the same way the story describes. Ideas into descriptions into realities.",
     False),

    ("s06-close-05-alex", "alex",
     "We were burning. Briefly and on purpose.",
     False),

    ("s06-close-06-jordan", "jordan",
     "It was enough.",
     False),

    ("s06-close-07-alex", "alex",
     "Thanks for listening.",
     False),
]


def generate_segment(filename, speaker, text, is_clip, idx, total):
    """Generate a single TTS segment."""
    outpath = os.path.join(OUTPUT_DIR, f"{filename}.mp3")

    if os.path.exists(outpath) and os.path.getsize(outpath) > 1000:
        print(f"[{idx+1}/{total}] SKIP (exists): {filename}")
        return True

    voice_id = VOICES[speaker]["id"]
    settings = CLIP_SETTINGS if is_clip else HOST_SETTINGS

    payload = {
        "text": text,
        "model_id": MODEL_ID,
        "voice_settings": settings
    }

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json",
        "Accept": "audio/mpeg"
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")

    char_count = len(text)
    print(f"[{idx+1}/{total}] Generating: {filename} ({speaker}, {char_count} chars)...", end=" ", flush=True)

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            audio = resp.read()
            with open(outpath, "wb") as f:
                f.write(audio)
            size_kb = len(audio) / 1024
            print(f"OK ({size_kb:.0f}KB)")
            return True
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"FAILED (HTTP {e.code}): {body[:200]}")
        if e.code == 429:
            print("  Rate limited — waiting 30s...")
            time.sleep(30)
            return False
        return False
    except Exception as e:
        print(f"FAILED: {e}")
        return False


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    total = len(SEGMENTS)
    total_chars = sum(len(s[2]) for s in SEGMENTS)
    print(f"=== Calliope Podcast Production ===")
    print(f"Total segments: {total}")
    print(f"Total characters: {total_chars}")
    print(f"Output: {OUTPUT_DIR}")
    print()

    # Start from a specific index if passed as arg
    start_idx = int(sys.argv[1]) if len(sys.argv) > 1 else 0

    succeeded = 0
    failed = 0

    for i, (filename, speaker, text, is_clip) in enumerate(SEGMENTS):
        if i < start_idx:
            continue

        ok = generate_segment(filename, speaker, text, is_clip, i, total)
        if ok:
            succeeded += 1
        else:
            # Retry once
            time.sleep(5)
            ok = generate_segment(filename, speaker, text, is_clip, i, total)
            if ok:
                succeeded += 1
            else:
                failed += 1

        # Small delay between requests to avoid rate limiting
        time.sleep(1.5)

    print(f"\n=== Complete ===")
    print(f"Succeeded: {succeeded}")
    print(f"Failed: {failed}")
    print(f"Skipped: {start_idx}")


if __name__ == "__main__":
    main()
