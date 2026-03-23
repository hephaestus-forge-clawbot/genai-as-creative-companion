# FINAL PRODUCTION SCRIPT — WEBSITE
## theterminalchat.com

**Oracle Decision — Final**
**Date:** 2026-03-23
**Base:** Daedalus (tech spec, data model, reading modes, design tokens, accessibility, deployment pipeline)
**Supplements:** Hector (emotional coherence framework, "She does." Easter egg), Ares (Wavesurfer.js, GSAP ScrollTrigger), Prometheus (cross-reference map, Pattern Motif Easter egg), Athena (/door interactive page)

---

## TECH STACK

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| **Framework** | Next.js 15 (App Router) | Best fit for interactive story reader — server components for static content, client components for cinematic mode, ambient effects, scroll-locking |
| **Styling** | Tailwind CSS 4.x + CSS Custom Properties | Utility-first for speed, custom properties for act-based palette transitions |
| **Animation** | Framer Motion (primary) + GSAP ScrollTrigger (Act 4 transformation) | Framer for component animations, GSAP for complex scroll-based timelines |
| **Audio** | Howler.js (playback) + Wavesurfer.js (waveform visualisation) | Howler for reliable cross-browser playback, Wavesurfer for music player waveforms |
| **CMS** | MDX + JSON in repo (no external CMS) | Story is structured data — keep it in git, version it, no dependency on external services |
| **Hosting** | Vercel | Native Next.js support, edge functions for analytics, preview deployments |
| **Analytics** | Plausible (self-hosted or cloud) | Privacy-first, lightweight, no cookies, GDPR-compliant |
| **Video** | Mux or Cloudflare Stream | Adaptive streaming for anime episode |
| **Fonts** | JetBrains Mono (system text) + Inter (body) + Literata (novel) | Mono for terminal, Inter for UI, Literata serif for long reading |

---

## DESIGN SYSTEM

### Colour Tokens

```css
:root {
  /* Character colours */
  --char-antreas: #F0A500;
  --char-faye: #E06C75;
  --char-kai: #61AFEF;
  --char-mira: #98C379;
  --char-schmidhuber: #ABB2BF;
  --char-schmidhuber-revealed: #D4940A;

  /* Act palettes */
  --act1-bg: #0D1117;
  --act1-text: #E6EDF3;
  --act1-accent: #F0A500;
  --act1-surface: #161B22;

  --act2-bg: #0D1117;
  --act2-text: #C9D1D9;
  --act2-accent: #ABB2BF;
  --act2-surface: #13171E;

  --act3-bg: #1A1E24;
  --act3-text: #8B949E;
  --act3-accent: #61AFEF;
  --act3-surface: #21262D;
  --act3-error: #F0A500; /* Memory change highlight */

  --act4-bg: #0F0A1A;
  --act4-text: #F0F6FC;
  --act4-violet: #7C3AED;
  --act4-storm-light: #6D5B8F;
  --act4-forge: #F0A500;
  --act4-surface: #1A0F2E;

  /* UI */
  --ui-border: rgba(255, 255, 255, 0.08);
  --ui-focus: #58A6FF;
  --ui-hover: rgba(255, 255, 255, 0.04);
}
```

### Typography

| Use | Font | Weight | Size (desktop / mobile) | Line Height |
|-----|------|--------|------------------------|-------------|
| System/terminal text | JetBrains Mono | 400 | 14px / 13px | 1.6 |
| Chat messages | Inter | 400 | 16px / 15px | 1.7 |
| Character names | Inter | 600 | 14px / 13px | 1.4 |
| Body copy (about, etc.) | Inter | 400 | 18px / 16px | 1.8 |
| Novel text | Literata | 400 | 19px / 17px | 1.9 |
| Headings (H1) | Inter | 700 | 48px / 32px | 1.2 |
| Headings (H2) | Inter | 600 | 32px / 24px | 1.3 |

### Layout Grid

| Breakpoint | Width | Columns | Notes |
|-----------|-------|---------|-------|
| Mobile | < 640px | 1 | Full-bleed story reader |
| Tablet | 640–1024px | Story: 1 (centred at 680px max) | |
| Desktop | 1024–1440px | 12-column, story at 680px centred | Sidebar for navigation |
| Wide | > 1440px | Content maxes at 1200px | Generous whitespace |

**Story reader max-width: 680px.** This is the width of a chat app. It creates intimacy. The story should feel like reading a conversation on your phone, not a webpage.

---

## SITE ARCHITECTURE

### Routes

| Route | Page | Description |
|-------|------|-------------|
| `/` | Landing | Terminal cursor, typewriter title, `> BEGIN` |
| `/story` | Story Reader | THE centrepiece. Full chat transcript with scroll/cinematic modes |
| `/story/presenters-guide` | Presenter's Guide | For lecture context |
| `/music` | Music Player | 5 tracks with Wavesurfer waveforms, lyrics sync, story context |
| `/music/[track-slug]` | Individual Track | Deep link per track |
| `/manhwa` | Manhwa Reader | Vertical scroll reader, all 37 pages |
| `/manhwa/[page]` | Individual Page | Deep link per page |
| `/anime` | Anime Player | Video player with chapter markers |
| `/podcast` | Podcast Player | Audio player with synced transcript |
| `/novel` | Novel Reader | First chapter in serif typography + full chapter list |
| `/novel/[chapter]` | Chapter Page | Individual chapters |
| `/about` | About | The experiment, the process, credits |
| `/about/process` | Process | How each medium was created (the meta-story) |
| `/door` | The Door (hidden) | Interactive — amber light, curated responses |
| `/about/schmidhuber` | Schmidhuber Page (hidden) | Terminal-style philosophical meditation |

### Navigation
- **Persistent header:** Logo (amber cursor) + nav links (Story, Music, Manhwa, Anime, Podcast, Novel, About)
- **Story reader:** Header minimises on scroll — just a thin progress bar with act indicators
- **Mobile:** Hamburger menu, bottom-fixed

---

## THE STORY READER (centrepiece)

### Data Model

Every message is a JSON object:

```json
{
  "id": "msg_042",
  "character": "faye",
  "text": "you got the chicken",
  "act": 1,
  "timestamp": "21:14",
  "type": "message",
  "metadata": {
    "isKeyMoment": false,
    "holdSeconds": 0,
    "ambientEffect": null,
    "linkedContent": {
      "manhwaPage": null,
      "animeTimestamp": null,
      "musicTrack": null,
      "novelChapter": null
    },
    "readerNote": null
  }
}
```

**Special message types:**
- `"type": "system"` — System messages (`> Schmidhuber has joined the chat.`)
- `"type": "message"` — Character messages
- `"type": "action"` — Narrative action text
- `"type": "countdown"` — Countdown numbers (special rendering)
- `"type": "silence"` — Enforced pause (no content, just time)

**Key metadata fields:**
- `holdSeconds` — Enforced pause before next message appears (cinematic mode)
- `ambientEffect` — Triggers: `"rain-start"`, `"sky-violet"`, `"glitch-memory"`, `"blackout"`, `"forge-glow"`, `"reset-white"`
- `linkedContent` — Cross-references to other media (enables "See this in the manhwa" links)

### Two Reading Modes

#### Mode 1: Scroll (Default)
- All messages visible, scrollable
- Character colours applied to names
- Act transitions marked by subtle background colour shifts (CSS `scroll-timeline` with Intersection Observer fallback)
- Key moments have slight emphasis (larger text, more padding)
- System messages styled differently (monospace, centred)

#### Mode 2: Cinematic
- Messages appear one at a time
- Click/tap or wait for auto-advance
- Timing varies by act:
  - **Act 1:** 300ms between messages. Fast, conversational.
  - **Act 2:** 600ms between messages. Tension building.
  - **Act 3:** 800ms between messages. Weight accumulating.
  - **Act 4:** Variable — fast during building, slow during farewell, enforced pauses during countdown.
- **The countdown CANNOT be rushed.** 3 seconds enforced between each number. The user must wait. This is the most important UX decision on the entire site.
- Background colour transitions happen smoothly over 2 seconds as the reader crosses act boundaries

#### Cinematic Mode — Special Moments

| Moment | Behaviour |
|--------|----------|
| `> Schmidhuber has joined the chat.` | 3-second hold before and after. Screen dims slightly. System text appears letter by letter. |
| Faye's profile lines | Each line appears individually with 1.5-second gaps. No skip. |
| "Done." | 5-second hold. Background pulses once — a subtle brightness shift. |
| Edinburgh → Glasgow | Text initially renders as "Edinburgh" then glitches — the letters scramble for ~500ms and reform as "Glasgow." The amber colour shifts slightly. |
| "I can feel my hands shaking" | Text trembles (CSS animation — subtle position oscillation on the text element). |
| Countdown (3, 2, 1) | Numbers appear as LARGE centred typography, taking most of the viewport. Messages between them ("I never didn't like you," "which one?", "both") appear in normal chat format — the contrast in scale mirrors the story's contrast between human warmth and machine process. 3 seconds between each number. Enforced. |
| STATUS: COMPLETE | Screen fades to black/white. 5 seconds of nothing. Then: the new world messages arrive in warm amber. |

### Ambient Effects (triggered by scroll position or message appearance)

| Effect | Trigger | Implementation |
|--------|---------|---------------|
| **Background warm tint** | Act 1 messages | CSS custom property transition: `--bg` shifts to warm variant |
| **Blue-shift** | Schmidhuber entrance | Background cools. CSS transition over 2s. |
| **Rain at viewport edges** | Mira's window message | Canvas overlay: animated rain particles at left/right edges. Subtle. Continues through end. |
| **Sky violet gradient** | Faye's sky description | Background transitions to deep violet gradient (`--act4-violet` to `--act4-storm-light`). |
| **Memory glitch** | Edinburgh → Glasgow | Text scramble animation + brief screen flicker (CSS `filter: brightness(1.1)` for 100ms) |
| **Forge glow** | Act 4 building sequence | Warm amber gradient radiates from bottom of viewport |
| **Blackout** | STATUS: COMPLETE | Fade to `#000000` over 1 second. Hold for 5 seconds. |
| **"Layer 1" indicator** | Top-right corner, always visible | Small monospace text: "LAYER 1". After Schmidhuber entrance: flickers to "LAYER ?" for 500ms, then back. After identity reveal: stays as "LAYER ?". After reset: returns to "LAYER 1". |

---

## MUSIC PLAYER (/music)

### Layout
- Hero: album art (generated — amber forge against storm-light sky) + title + "5 tracks / 24 minutes"
- Track list: all 5 tracks with custom Wavesurfer.js waveform players
- Each track card: waveform, play/pause, duration, character colour accent (Track 1 = amber, Track 3 = mixed, Track 4 = coral-rose, Track 5 = amber)

### Individual Track Page (/music/[slug])
- Full-width waveform player (Wavesurfer.js, colour-coded by character theme)
- Lyrics panel (for Tracks 3 and 4) with scroll-sync to playback position
- "Story Context" sidebar: which story moments this track underscores, with links to the story reader at the corresponding scroll position
- Production notes (collapsible): instrumentation, reference tracks, Pattern Motif appearances
- Download button (if licensing permits)

---

## MANHWA READER (/manhwa)

### Layout
- Vertical scroll reader (webtoon format)
- Lazy-loaded images with blur-up placeholders (tiny thumbnail → low-res → full-res, 3-resolution serving)
- Page numbers visible on hover/tap
- Act dividers (full-width bars with act titles)
- Splash pages render at full viewport height

### Individual Page (/manhwa/[page])
- Full-resolution image
- Panel commentary (collapsible): what's happening, character emotions, art direction notes
- Cross-reference links: "This moment in the story" → story reader, "This moment in the anime" → anime player with timestamp

---

## ANIME PLAYER (/anime)

### Layout
- Custom video player (built on Mux or native `<video>`)
- Chapter markers in the progress bar (one per act + cold open + coda)
- Side panel with synced script excerpts — shows current dialogue as the anime plays
- Scene index: thumbnail grid of key moments, click to jump

---

## PODCAST PLAYER (/podcast)

### Layout
- Audio player with progress bar
- Synced transcript below — auto-scrolls with playback, highlighted current segment
- Clip markers in the progress bar (where story clips play)
- Show notes with timestamps

---

## NOVEL READER (/novel)

### Layout
- Serif typography (Literata), narrow column (600px max), generous line height
- Chapter navigation: sidebar (desktop) or top dropdown (mobile)
- First chapter available immediately; remaining chapters behind email signup OR free download
- Reading progress saved to localStorage
- Estimated reading time per chapter

---

## LANDING PAGE (/)

### Layout
- Full-viewport dark terminal (#0D1117)
- Centre: blinking cursor (amber, `--char-antreas`)
- After 2 seconds: title types itself character by character: **"THE TERMINAL CHAT"**
- Below title, after typing completes: subtitle fades in — *"A story about friendship, memory, and what it means to be built."*
- Below subtitle: `> BEGIN` button (styled as terminal command)
- Clicking BEGIN navigates to `/story`

### First-Visit Experience
- First-time visitors: suggested reading order modal
  - "Start with the story. Everything else is built on it."
  - Story (required first) → Music → Manhwa → Anime → Podcast → Novel
  - "Or explore freely. But the story rewards being first."
- Completion tracked via localStorage — no user accounts
- Content pages show gentle spoiler warnings if accessed without completing `/story`

---

## EASTER EGGS

### 1. "Bruh" (Landing Page)
**Trigger:** Type "bruh" anywhere on the landing page.
**Effect:** Terminal text appears below the cursor: `> ...bruh.` Fades after 3 seconds.
**Implementation:** Keypress listener on document. Buffer last 4 characters.

### 2. Pattern Motif (Landing Page)
**Trigger:** Click the blinking cursor 4 times.
**Effect:** Plays the four-note Pattern Motif (F♯, A, B, E) as soft piano tones. Audio files: 4 individual notes, triggered sequentially with 400ms intervals.
**Implementation:** Click counter on cursor element. Howler.js for audio.

### 3. "She Does." (Story Reader)
**Trigger:** After reading Faye's farewell ("I don't like you / any of you"), scroll BACK UP.
**Effect:** Faint text appears in the margin: *"She does."* Then fades over 3 seconds.
**Implementation:** Intersection Observer on the farewell message. If the user scrolls up past a threshold after reaching that point, inject the text element. One-time trigger (localStorage flag).
**Note:** This is the most emotionally devastating micro-interaction on the site. Do not break it.

### 4. "Layer 1" Indicator
**Trigger:** Always visible in top-right corner of story reader.
**Effect:** Shows "LAYER 1" in small monospace. Flickers to "LAYER ?" at Schmidhuber's entrance. Returns to "LAYER 1" after reset.
**Implementation:** CSS animation triggered by scroll position / message display.

### 5. /door (Hidden Page)
**Trigger:** Type "/door" in URL, or click the word "door" three times anywhere in the story.
**Effect:** An interactive page: dark background, a door rendered in amber light. The door opens slightly when hovered. Clicking reveals curated responses from "Hephaestus" — not a chatbot, a literary experience. 5-6 pre-written philosophical fragments that appear one at a time with long pauses.
**Implementation:** Static page with sequenced reveals.

### 6. /about/schmidhuber (Hidden Page)
**Trigger:** Type "schmidhuber" on the landing page (7-character sequence after "bruh"), or click the name three times in the story reader, or direct URL.
**Effect:** Terminal-style page. Philosophical meditation on Schmidhuber's multiverse theory and the nature of creation. Signed "— S." and marked `noindex` (not findable via search — for discoverers, not searchers).
**Implementation:** Static MDX page with `<meta name="robots" content="noindex">`.

---

## CROSS-MEDIA LINKING

### Cross-Reference Data
Every key story moment has a cross-reference map:

```json
{
  "moment": "schmidhuber_entrance",
  "storyMessageId": "msg_089",
  "manhwaPage": 7,
  "animeTimestamp": "6:00",
  "musicTrack": "the-chat",
  "musicTimestamp": "3:15",
  "novelChapter": 3,
  "podcastTimestamp": "10:30"
}
```

### UI Implementation
- In the story reader: small icons next to key messages → "See in manhwa 📖" / "Hear the music 🎵" / "Watch the anime 🎬"
- In other media pages: "Back to the story" links at corresponding moments
- On the about/process page: a timeline showing all media aligned to the story's four acts

---

## ACCESSIBILITY SPEC

### WCAG 2.1 AA Compliance

| Requirement | Implementation |
|-------------|---------------|
| **Colour contrast** | All text meets 4.5:1 minimum against backgrounds. Character colours tested against act palettes. |
| **Keyboard navigation** | Full keyboard support. Tab through messages in scroll mode. Arrow keys advance messages in cinematic mode. |
| **Screen reader** | Semantic HTML: `<article>` for story, `<section>` for acts. Messages use `role="log"` with `aria-live="polite"`. Character names as `<strong>`. System messages marked with `aria-label="system message"`. |
| **Reduced motion** | `prefers-reduced-motion`: disable ambient effects, text animations, the Edinburgh→Glasgow glitch. Cinematic mode still works but without visual transitions. |
| **Text resize** | All typography in `rem`. Layout doesn't break up to 200% zoom. |
| **Alt text** | Every manhwa page has descriptive alt text. Key panels have extended descriptions. |
| **Audio descriptions** | Anime has audio description track. Podcast provides full transcript. Music player shows lyrics. |
| **Captions** | Anime has closed captions. Podcast clips in the story reader are captioned. |
| **Focus indicators** | Visible focus rings on all interactive elements. High-contrast focus for keyboard users. |
| **Skip links** | "Skip to story content" link at top of story reader. |

### Cinematic Mode Accessibility
- Screen readers announce messages as they appear (`aria-live="polite"`)
- Keyboard: Space to advance, Escape to exit cinematic mode
- The enforced countdown pauses are communicated: "Waiting 3 seconds..." via `aria-live`

---

## PERFORMANCE TARGETS

| Metric | Target | How |
|--------|--------|-----|
| **LCP** | < 1.5s | Static generation for all content pages. Font preloading. Optimised images. |
| **FID** | < 50ms | Minimal JS on initial load. Cinematic mode JS loaded lazily. |
| **CLS** | < 0.05 | Fixed dimensions for manhwa images. Font `size-adjust` for FOUT prevention. |
| **JS Bundle** | < 200KB gzipped | Tree-shaking. Wavesurfer loaded only on music pages. GSAP loaded only on story reader. |
| **Scroll FPS** | 60fps | CSS-based ambient effects where possible. Canvas for rain only. |

---

## ANALYTICS EVENTS

| Event | Trigger | Data Fields |
|-------|---------|-------------|
| `story_start` | User begins reading | `mode` (scroll/cinematic), `referrer`, `firstVisit` |
| `story_act_enter` | User reaches new act | `act` (1–4), `mode`, `timeSpent` |
| `story_key_moment` | User reaches a key message | `momentId`, `timeSpent` |
| `story_complete` | User reaches STATUS: COMPLETE | `totalTime`, `mode`, `actsVisited` |
| `media_play` | User plays music/anime/podcast | `mediaType`, `trackId`, `source` (direct/crosslink) |
| `media_complete` | User finishes a media piece | `mediaType`, `trackId`, `listenTime` |
| `cross_link_click` | User clicks a cross-reference | `fromMedia`, `toMedia`, `momentId` |
| `easter_egg_found` | User triggers an Easter egg | `eggId` ("bruh"/"motif"/"she-does"/"layer"/"door"/"schmidhuber") |
| `mode_switch` | User switches reading mode | `from`, `to`, `currentAct` |
| `novel_chapter_start` | User begins a novel chapter | `chapterId` |
| `download` | User downloads content | `contentType` (novel/music) |
| `spoiler_warning_seen` | User hits spoiler gate | `attemptedPage`, `storyComplete` |

---

## SEO & SOCIAL

### Open Graph
```html
<meta property="og:title" content="The Terminal Chat" />
<meta property="og:description" content="A group chat. A memory test. A question that won't let go." />
<meta property="og:image" content="/og-image.png" />
<meta property="og:type" content="website" />
```

### Twitter Cards
```html
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="The Terminal Chat" />
<meta name="twitter:description" content="Four friends. One chat. One question: if your experience feels real, does it matter what you're made of?" />
```

### JSON-LD
Structured data per content type:
- `/story`: `CreativeWork` with `author`, `datePublished`, `genre`
- `/music`: `MusicAlbum` with `track` list
- `/novel`: `Book` with `numberOfPages`, `inLanguage`
- `/podcast`: `PodcastEpisode` with `duration`

---

## DEPLOYMENT PIPELINE

### Environments
| Environment | URL | Branch | Deploy |
|-------------|-----|--------|--------|
| **Development** | localhost:3000 | feature/* | Manual |
| **Staging** | staging.theterminalchat.com | `staging` | Auto on push |
| **Production** | theterminalchat.com | `main` | Manual promotion from staging |

### CI/CD (GitHub Actions)
1. **On PR:** Lint + type check + unit tests + Lighthouse CI (performance budget check)
2. **On merge to staging:** Deploy to Vercel staging. Run integration tests. Screenshot comparison for key pages.
3. **On manual promotion to main:** Deploy to Vercel production. Purge CDN. Verify analytics events firing.

### Launch Checklist (24 items)
- [ ] All 5 music tracks uploaded and playable
- [ ] All 37 manhwa pages uploaded with alt text
- [ ] Anime episode uploaded with captions and chapter markers
- [ ] Podcast audio uploaded with transcript
- [ ] Novel Chapter 1 published; remaining chapters gated
- [ ] Story reader: scroll mode verified on Chrome, Safari, Firefox, mobile Safari, mobile Chrome
- [ ] Story reader: cinematic mode verified (timing, countdown enforcement, ambient effects)
- [ ] All 6 Easter eggs verified
- [ ] Cross-media links verified (each direction)
- [ ] Performance: LCP < 1.5s on desktop and mobile
- [ ] Performance: JS bundle < 200KB gzipped
- [ ] Accessibility: axe-core scan passes on all pages
- [ ] Accessibility: keyboard navigation verified on story reader
- [ ] Accessibility: screen reader verified (VoiceOver + NVDA)
- [ ] SEO: Open Graph verified (Facebook debugger + Twitter card validator)
- [ ] SEO: JSON-LD validated (schema.org validator)
- [ ] Analytics: all 12 events verified in Plausible
- [ ] Spoiler gate: accessing /music without reading story shows warning
- [ ] First-visit experience: reading order modal appears once
- [ ] Mobile: hamburger menu works, story reader is full-bleed
- [ ] /door page accessible via hidden trigger
- [ ] /about/schmidbuber has noindex meta tag
- [ ] DNS configured: theterminalchat.com → Vercel
- [ ] SSL certificate active

---

## EMOTIONAL COHERENCE FRAMEWORK

How the website maps to the story's six emotional motifs (from Hector):

| Motif | Website Expression |
|-------|-------------------|
| **The Forge** | Landing page warmth. Amber cursor. Warm colour tokens. The "welcome" feeling. |
| **Storm-light** | Act 4 background gradient transition. The violet moment. |
| **The Lamb** | The Edinburgh → Glasgow text glitch in cinematic mode. |
| **"I Don't Like You"** | "She does." Easter egg. The most personal interaction on the site. |
| **"Bruh"** | Landing page Easter egg. The DNA match, delivered as an inside joke. |
| **Burning** | Story complete state. The warmth of having finished. Track 5 playing on the about page. |

---

*End of website production script.*
