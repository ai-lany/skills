# Inspiration log

Where each part of the system came from, captured October 2026 with Playwright (video, stills,
computed styles, hover bursts, and source reading). We borrow **qualities** (rhythm, motion
ideas, palette moods, interaction patterns), never logos, copy, characters, 3D models,
illustrations or proprietary fonts. Revisit these links when a decision feels off-brand.

| Source | What we took | Where it lives |
|---|---|---|
| [milknetwork.com](https://milknetwork.com/) | Preloader: giant lowercase wordmark rises from a bottom mask, then shrinks and docks into the corner logo. Rotating hero word with an underscore caret (`We grow _brands → _people`). Huge display at ~124px, tracking −0.04em, leading 0.8. Black/white restraint. | motion §1, §4; typography |
| [about.miroom.com](https://about.miroom.com/) | Preloader B: color-cycling dot (green → pink → lime) + % counter, then a grid of outlined circles fills into a chunky rounded wordmark. Accent set of electric blue `#133EFF`, pink `#FF85CE`, acid lime `#E5FF00`. | motion §2; `--dialup`, `--sticky`, `--lcd` |
| [yuanzuostudio.tw](https://yuanzuostudio.tw/) | **Flat glass**: `rgba(240,240,240,.68)` + `blur(6px)`, radius 0, no border/shadow. Orange cursor dot that grows into a "Drag" / "View" label. Pill tags. `[ PHILOSOPHY ]` bracket labels. Marquee "Let's start a conversation ✱". Giant footer wordmark on ink with rounded top corners. Matter.js. | components §2, §4, §11, §15, §16; `--signal` |
| [tsg-jpn.co.jp](https://www.tsg-jpn.co.jp/) | Fun 3D: iridescent crystals, glass lattices and clay blobs with **googly cartoon eyes** tumbling into frame (pre-rendered there; we build ours live from primitives). | motion §8 |
| [orgnzm.studio](https://orgnzm.studio/) | A single 3D object that travels with scroll; flipping red logo; desktop widgets (local time, "new case" card); words that fade from muted to ink on scroll; numbered services list; full-bleed red block. GSAP + ScrollTrigger + Lenis + Lottie + Matter. | motion §6, §12; components §10; layouts A |
| [pxpush.com](https://pxpush.com/) | Y2K-modern: CRT scanline + vignette overlay, cloud-sky hero, chrome emblem, 3D floppy disk, electric-blue full-bleed sections `#03049C`, GeistMono micro text, green "● Get started" status dot, semi-squeezed display. | `--tex-scan`, components §4, §17; typography |
| [bymonolog.com](https://bymonolog.com/) | Warm off-white `#E8E8E3` vs near-black `#080807`, film grain, condensed uppercase shouting line, three.js, muted-continuation headlines, "(scroll to explore)". | `--paper`, `--ink`, `.tex-grain`, typography rule 3 |
| [qando.co.jp](https://qando.co.jp/) | **Text scramble hover**: random letters + block glyphs `▀▁▂▃█░▒▓◧◨` resolve char-by-char in ~250ms on a cursor-following label (works_stalker.js). Square-grid icons that blink in sequence on hover. Lenis. | motion §5, §7, §12 |
| [Dribbble: "sent." by heartbeat](https://dribbble.com/shots/27187012-sent-Reconnecting-with-Y2K-nostalgia) | The emotional target: "the calm optimism of the early internet." Bliss-like sky/grass with halftone texture, glossy soap bubbles (some saturated blue), Aqua gel pill CTA, floating pill nav, navy condensed serif headline, Nokia LCD with pixel text typing messages. | sky hero, `--gel`, bubbles, LCD, Instrument Serif |
| [Berd by Block](https://berd.xyz/) ([One Page Love](https://onepagelove.com/berd)) | **App UI reference.** Warm grey paper `#E5E5E0` with dot grid; macOS-style app window with light sidebar (Home, Agents, Skills…), pink sticky-note "Starter task list", pill chat input with round icon buttons; uncanny clay toy characters; tight grotesk display; hand-drawn numerals 01–04; black chamfered octagon cards; agent "spec cards" (Good for / Vibes); small ink uppercase "DOWNLOAD" button; yellow round "CLICK ME" sticker; window-boot intro. | layouts B, components §1, §6–§9, §3 sticker, motion §3 |

## Shared tech observed
GSAP + ScrollTrigger + Lenis on 7/9 sites; Matter.js on 4; three.js on 1 (others use video or
pre-rendered stills for 3D); Splitting.js on 1; `backdrop-filter` on 3. The skill standardizes
on GSAP 3.13 + ScrollTrigger + Lenis 1.3 + Matter 0.20 + three 0.170 from CDN.

## Adding new inspiration
Put images in `assets/inspiration/` (your own references/screenshots for personal use) and add
a row above: source, what to take, and which token/recipe it changes. If a new reference
conflicts with the system, decide explicitly and update `tokens.css`, don't let pages drift.
