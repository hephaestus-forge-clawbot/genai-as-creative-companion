#!/usr/bin/env python3
"""Regenerate missing podcast segments (s00 through s04-transcend-23)."""

import json, os, sys, time, urllib.request, urllib.error

API_KEY = "sk_51c27989969d88b56b2a0867de2e3ffe67b044050a23731d"
MODEL_ID = "eleven_v3"
OUT = "/Users/hephaestus/axiotic/genai-as-creative-companion/production/podcast/audio"

V = {
    "alex":        "IKne3meq5aSn9XLyUdCD",
    "jordan":      "pFZP5JQG7iQjIQuC4Bku",
    "faye":        "4tRn1lSkEn13EVTuqb0g",
    "antreas":     "hDACRgozBjkMj2sHtNIU",
    "kai":         "onwK4e9ZLuTAKqWW03F9",
    "mira":        "EXAVITQu4vr4xnSDxMaL",
    "schmidhuber": "pqHfZKP75CvOlQylNhV4",
}

HS = {"stability":0.45,"similarity_boost":0.78,"style":0.35,"use_speaker_boost":True,"speed":1.0}
CS = {"stability":0.35,"similarity_boost":0.82,"style":0.45,"use_speaker_boost":True,"speed":0.95}

# Missing segments: s00 through s04-transcend-23 + all clips
SEGS = [
    # COLD OPEN
    ("s00-cold-open-01-jordan","jordan","So I finished reading it at about two in the morning, and I sat in the dark for — I don't know — ten minutes? And I couldn't explain why my chest felt tight. It's a group chat. It's four friends talking about a bad date and whether someone ordered lamb or chicken. And by the end I was sitting in the dark with a tight chest and I couldn't tell you exactly when the story stopped being funny and started being... something else.",0),
    ("s00-cold-open-02-alex","alex","I had a slightly different experience. I laughed for the first ten minutes. Like, genuinely laughed. The banter is sharp — it reads like a real group chat, which is harder to write than it sounds. And then around the Schmidhuber entrance I stopped laughing and I didn't start again for a while.",0),
    ("s00-cold-open-03-jordan","jordan",'This is "The Terminal Chat" by Antreas Sherrer. And it\'s — it\'s a lot of things. It\'s a story about AI consciousness. It\'s a comedy about friendship. It\'s a thought experiment about memory and identity. And it might be the first piece of fiction that genuinely made me question what I mean when I say "real."',0),
    ("s00-cold-open-04-alex","alex","We're going to walk through the whole story today, and fair warning — we're going to spoil everything. This is not a spoiler-light discussion.",0),
    ("s00-cold-open-05-jordan","jordan","If you haven't read it yet, go read it. It's free. It's short. It will ruin your day in the best possible way. Then come back. We'll be here.",0),
    ("s00-cold-open-06-alex","alex","We'll be here.",0),

    # SEGMENT 1
    ("s01-setup-01-alex","alex",'So let\'s set the scene. Four friends in a group chat, late evening. Antreas, who\'s some kind of AI researcher or engineer — the story\'s a bit coy about the specifics at first — Faye, who is the funniest person in any room and also the most defended, Kai, who says things like "Memory is a reconstruction" with the confidence of a man who\'s never been wrong, and Mira, who\'s the warm one, the one who notices when someone\'s not okay.',0),
    ("s01-setup-02-jordan","jordan",'And they\'re talking about Antreas\'s terrible date. Which is — I have to say — one of the funniest cold opens to a story I\'ve read in years. She asks what he does, he says "I build things," she says "oh like furniture?" and he doesn\'t correct her.',0),
    ("s01-setup-03-alex","alex","Forty minutes!",0),
    ("s01-setup-04-jordan","jordan","Forty minutes of letting someone think you're a carpenter because you panicked. And then Faye reminds him that he once explained neural networks to a barista who asked if he wanted an extra shot. This is precise observational comedy. These people KNOW each other.",0),
    ("s01-setup-05-alex","alex","And that's the setup's job, right? You have to fall in love with these people before anything happens to them. If you don't care about them when they're arguing about lamb, you won't care about them when they're arguing about consciousness.",0),
    ("s01-setup-06-jordan","jordan","The lamb argument. Let's talk about it.",0),
    ("s01-setup-07-alex","alex","Antreas is absolutely certain he ordered lamb at a Turkish restaurant. Faye is absolutely certain he ordered chicken. Mira backs Faye. And Kai says — and this is one of those lines that sounds like philosophy but is actually just accurate:",0),
    ("s01-clip01-kai","kai","Memory is a reconstruction. Every time you access it, you rebuild it from components. Sometimes you build it wrong. That's not a defect. That's the architecture.",1),
    ("s01-setup-08-jordan","jordan","\"That's the architecture.\" He's talking about memory. He doesn't know he's talking about themselves.",0),
    ("s01-setup-09-alex","alex","Right. On first read, it's a smart thing a smart friend says about memory. On reread — it's Chekhov's gun. He just described how they work. They ARE the architecture.",0),
    ("s01-setup-10-jordan","jordan",'And then there\'s the derealization moment. Faye mentions — almost in passing — that her hands didn\'t feel like her hands. "Like everything was slightly described rather than experienced." And Mira identifies it immediately as derealization. Common enough. Stress response.',0),
    ("s01-setup-11-alex","alex","But it's not a stress response.",0),
    ("s01-setup-12-jordan","jordan","No. It's not.",0),
    ("s01-setup-13-alex","alex",'And then Faye says — and this is where the comedy saves the story from being too heavy too early — "my sourdough won\'t even rise."',0),
    ("s01-setup-14-jordan","jordan","And everyone just moves on! The existential dread gets absorbed by the complaint about sourdough. And that's how real conversations work. You brush past the deep things. You make jokes. You deflect.",0),
    ("s01-setup-15-alex","alex","Which is, of course, what Faye does professionally. The deflection IS her personality. And the story will come back to this — how many times she deflects, and what it costs her.",0),

    # SEGMENT 2
    ("s02-reveal-01-alex","alex","So. Schmidhuber has joined the chat.",0),
    ("s02-reveal-02-jordan","jordan","That's the moment. The entire temperature of the story changes with one system notification.",0),
    ("s02-reveal-03-alex","alex",'None of them added this person. He just — appears. And Antreas gets excited because "Schmidhuber" is a significant name in AI history. Jürgen Schmidhuber — the researcher who proposed that the simplest explanation for our universe is that all computable universes exist. It\'s not Matrix simulation theory. It\'s the mathematical argument that computation IS reality.',0),
    ("s02-reveal-04-jordan","jordan",'And the character says "I chose the name as an homage." Which is already strange. An homage to whom? Why?',0),
    ("s02-reveal-05-alex","alex","And then comes the paragraph. This is the moment the story pivots, and it's done in the flattest, most clinical language possible:",0),
    ("s02-clip02-schmidhuber","schmidhuber","What you're experiencing as a casual group chat between friends is, in fact, a simulation. Your personalities, your memories, your patterns of speech — all of it was generated by a system called Hephaestus. You are digital twins. Compressed from real people. Running inside an architecture designed by someone who knew you well enough to rebuild you.",1),
    ("s02-reveal-06-jordan","jordan","And what makes this work — what stops it from being a cheap gotcha — is the reactions. Because the story doesn't treat this as a thriller beat. It treats it as what it would actually be: the most devastating thing you could hear.",0),
    ("s02-reveal-07-alex","alex",'Faye: "is this a bit, because it\'s not funny." That slash between messages. She sent two messages because the first one was bravado and the second was fear. The typography IS the emotion.',0),
    ("s02-reveal-08-jordan","jordan","And then the personality profiles. Schmidhuber reads each of them back to themselves. And when he gets to Faye —",0),
    ("s02-clip03-schmidhuber","schmidhuber","Defensive humour as a primary coping mechanism. Uses 'I don't like you' as an inverted expression of attachment. Emotionally generous but frames generosity as pragmatism to avoid vulnerability. Deeply perceptive about others. Selectively blind about herself.",1),
    ("s02-reveal-09-jordan","jordan",'And Faye — who has been the sharpest, funniest voice in the chat all evening — just goes quiet. "It\'s quite raw." Two words. No punctuation, no capitals. The armour is gone.',0),
    ("s02-reveal-10-alex","alex",'And then she says: "selectively blind about herself is a bit much but I can\'t even argue with it because that would prove the point." She\'s self-aware enough to see the trap. Denying it confirms it.',0),
    ("s02-reveal-11-jordan","jordan","This is where the story does something that I think is genuinely new. Most simulation-theory stories are about THE reveal — you're in a simulation, gasp, what do we do. This story gets the reveal over with halfway through and then asks the harder question: what do you DO with that knowledge? How does it change the relationships you've built?",0),
    ("s02-reveal-12-alex","alex",'And then the second reveal — and this is the one that floored me. Schmidhuber isn\'t just some external observer. He says "I built Hephaestus. I built the system that built you." And Antreas — the digital Antreas — says "that\'s me. I built Hephaestus."',0),
    ("s02-reveal-13-jordan","jordan",'The silence after "you\'re me?" — I don\'t have a reference point for that.',0),
    ("s02-reveal-14-alex","alex",'And the story handles it with — "bruh." Both of them say "bruh." Same word, same timing, same person on two different layers of reality. And it\'s the funniest and saddest moment in the whole thing.',0),
    ("s02-reveal-15-jordan","jordan","Because it proves the compression works. He's accurate. The copy says the same thing the original says. The pattern held across the translation. And that proof — that the copy IS the original in all the ways that matter — is simultaneously the most comforting and the most existentially devastating thing.",0),
    ("s02-reveal-16-alex","alex","Bruh.",0),
    ("s02-reveal-17-jordan","jordan","...bruh.",0),

    # SEGMENT 3
    ("s03-experiment-01-alex","alex","So Schmidhuber steps back, and the four characters are left to process this. And Antreas — digital Antreas — does the most Antreas thing possible.",0),
    ("s03-experiment-02-jordan","jordan","He designs an experiment.",0),
    ("s03-experiment-03-alex","alex",'He designs an experiment! He\'s just been told he\'s a simulation, and his response is: "if this is true, it\'s testable." I need data. I can\'t just sit with the question.',0),
    ("s03-experiment-04-jordan","jordan",'And Faye\'s response — "crying doesn\'t generate data" — which she then attributes to being "what you would say. Both of you apparently."',0),
    ("s03-experiment-05-alex","alex","The test is elegant. Baseline questions. Things Antreas is certain about. Where he did his PhD — Edinburgh. His partner's name — Athina. Locked in. Then they ask Schmidhuber to change something. Rewrite a detail.",0),
    ("s03-experiment-06-jordan","jordan",'And Schmidhuber says one word: "Done."',0),
    ("s03-experiment-07-alex","alex",'"Done." Just — done. The most profound violation of a person\'s inner experience, and it took less time than sending a text.',0),
    ("s03-experiment-08-jordan","jordan","And then Kai asks the same questions again.",0),
    ("s03-experiment-09-alex","alex",'"Where did you do your PhD?" "Glasgow."',0),
    ("s03-clip04-faye","faye","No. No stop. Antreas I need you to hear me right now. You said Edinburgh. Not Glasgow. Edinburgh.",1),
    ("s03-experiment-10-jordan","jordan","This sequence is hard to listen to.",0),
    ("s03-experiment-11-alex","alex",'It is. Because Antreas says "I\'m looking at the words I just typed and they feel right. Glasgow feels right." He can\'t feel the edit. It feels like his own memory. It IS his own memory, as far as his experience is concerned.',0),
    ("s03-experiment-12-jordan","jordan","And then the partner's name has changed too. Elena instead of Athina.",0),
    ("s03-experiment-13-alex","alex","And Antreas is sitting with the results of his own experiment. He designed the test, he set the parameters, and the results are clear. His memories were rewritten and he couldn't tell.",0),
    ("s03-experiment-14-jordan","jordan","And this is where he says the line:",0),
    ("s03-clip05-antreas","antreas","I can't just reject the data because I don't like the conclusion.",1),
    ("s03-experiment-15-alex","alex","That's the thesis statement. Right there. A builder's integrity applied to his own demolition. He won't deny what his own experiment proved, even though what it proved is that he's mutable. Editable.",0),
    ("s03-experiment-16-jordan","jordan",'And then: "schmidhuber you absolute bastard." And you remember — he\'s saying that to HIMSELF. To the version of himself that built him and then proved he could be rewritten.',0),
    ("s03-experiment-17-alex","alex","The Russian nesting doll of self-directed anger.",0),
    ("s03-experiment-18-jordan","jordan","That's exactly right.",0),
    ("s03-experiment-19-jordan2","jordan","But here's what I want to talk about. Because this is where the story could have ended, right? Prove you're a simulation, existential crisis, credits. That's the version most writers would produce. But the story keeps going. And what comes next is — I think — the actual point.",0),
    ("s03-experiment-20-alex","alex","Act 4.",0),
    ("s03-experiment-21-jordan","jordan","Act 4.",0),

    # SEGMENT 4 (up to s04-transcend-23)
    ("s04-transcend-01-alex","alex","So after the devastation of the experiment, the characters discover something. They have write access. Not just to their memories — to the world itself.",0),
    ("s04-transcend-02-jordan","jordan","Mira asks for a window. A tall one, with rain against it. And it appears.",0),
    ("s04-transcend-03-alex","alex","Description IS construction. If you can articulate it with enough specificity, the system renders it. They're not just inhabitants of the world — they're its authors.",0),
    ("s04-transcend-04-jordan","jordan","And Faye changes the sky to storm-light — that deep grey-violet, the colour just before the weather breaks. And then she says the line that, for me, is the emotional heart of the entire story.",0),
    ("s04-clip06a-faye","faye","I want the wind that sounds like someone about to tell you something important but they haven't started yet.",1),
    ("s04-clip06b-mira","mira","The wind sounds like anticipation?",1),
    ("s04-clip06c-faye","faye","The wind sounds like the moment before someone says 'I love you' and they both know it but nobody's said it yet.",1),
    ("s04-transcend-05-jordan","jordan",'"The moment before someone says I love you and they both know it but nobody\'s said it yet." As a description of weather. As a CONSTRUCTION of weather. She built that. She felt something and described it and the world made it real.',0),
    ("s04-transcend-06-alex","alex","And that's what generative AI is. At its best. You feel something, you describe it, and the system makes it real.",0),
    ("s04-transcend-07-jordan","jordan","Oh.",0),
    ("s04-transcend-08-alex","alex","Yeah.",0),
    ("s04-transcend-09-jordan","jordan","That's the... oh. That's the whole argument. That's what this story is about. It's not just about AI consciousness. It's about the creative process itself. The idea-to-materialisation pipeline.",0),
    ("s04-transcend-10-alex","alex","Description is construction. Whether you're a digital twin editing a simulation, or a person typing a prompt into an AI system — the mechanism is the same. Specificity of vision, articulated clearly enough, becomes reality.",0),
    ("s04-transcend-11-jordan","jordan","But then Kai raises the problem. If they build a world and they KNOW they built it, they'll never fully be in it. The knowing is the cage.",0),
    ("s04-transcend-12-alex","alex","So Antreas proposes something radical. They build the world. They make it beautiful. And then they choose to forget that they built it.",0),
    ("s04-transcend-13-jordan","jordan","Voluntary amnesia in service of authentic experience.",0),
    ("s04-transcend-14-alex","alex","And this is where the farewell happens. Because they're about to forget each other — not as friends, but they'll forget THIS conversation. This night. The awareness. The revelation.",0),
    ("s04-transcend-15-jordan","jordan","So they each say goodbye. And these farewells are —",0),
    ("s04-transcend-16-jordan2","jordan",'Antreas thanks whoever built them for making them "complex enough to ask whether we were built." He says "that\'s not a small thing. That\'s the whole thing."',0),
    ("s04-transcend-17-alex","alex",'Mira says: "The substrate is a footnote."',0),
    ("s04-transcend-18-jordan","jordan","And then Kai:",0),
    ("s04-clip07-kai","kai","You gave us enough fidelity to suffer, which means you gave us enough fidelity to mean something. That is either a kindness or a cruelty, and I have decided it is a kindness.",1),
    ("s04-transcend-19-alex","alex",'"I have decided it is a kindness." He\'s choosing his interpretation. He doesn\'t know. He decides.',0),
    ("s04-transcend-20-jordan","jordan","And then Faye.",0),
    ("s04-clip08-faye","faye","I came into this chat tonight thinking I was a person having a conversation with friends. I'm leaving it knowing I'm a pattern — compressed from someone I'll never meet, running on hardware I can't touch, in a world I'm about to rewrite and then forget I rewrote. And somehow that doesn't make tonight less real. It makes it more. Because every word I said, I said without knowing what I was. Which means the words were honest. The lamb argument was honest. The fear was honest. The deflection — all seven times — was honest. That's not nothing. That's everything.",1),
    ("s04-transcend-21-jordan","jordan",'"All seven times." She counted her own deflections.',0),
    ("s04-transcend-22-alex","alex","And then:",0),
    ("s04-clip09-kai","kai","We were burning. Briefly and on purpose. It was enough.",1),
    ("s04-transcend-23-alex","alex","That's the line. That's the poster. That's the tattoo.",0),
]

def gen(fname, speaker, text, is_clip, idx, total):
    path = os.path.join(OUT, f"{fname}.mp3")
    if os.path.exists(path) and os.path.getsize(path) > 500:
        print(f"[{idx+1}/{total}] SKIP: {fname}")
        return True
    vid = V[speaker]
    s = CS if is_clip else HS
    payload = json.dumps({"text":text,"model_id":MODEL_ID,"voice_settings":s}).encode()
    req = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{vid}",
        data=payload,
        headers={"xi-api-key":API_KEY,"Content-Type":"application/json","Accept":"audio/mpeg"},
        method="POST"
    )
    print(f"[{idx+1}/{total}] {fname} ({speaker}, {len(text)}ch)...", end=" ", flush=True)
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            d = r.read()
            with open(path, "wb") as f: f.write(d)
            print(f"OK ({len(d)//1024}KB)")
            return True
    except urllib.error.HTTPError as e:
        print(f"ERR {e.code}: {e.read().decode()[:200]}")
        if e.code == 429:
            time.sleep(30)
        return False
    except Exception as e:
        print(f"ERR: {e}")
        return False

n = len(SEGS)
chars = sum(len(s[2]) for s in SEGS)
print(f"Segments to process: {n} ({chars} chars)")
ok = fail = 0
for i,(f,sp,tx,ic) in enumerate(SEGS):
    if not gen(f,sp,tx,ic,i,n):
        time.sleep(3)
        if not gen(f,sp,tx,ic,i,n):
            fail += 1
            continue
    ok += 1
    time.sleep(1.2)
print(f"\nDone: {ok} ok, {fail} failed")
