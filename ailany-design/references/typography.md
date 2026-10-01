# Typography

Five voices, each with a strict job. The contrast between them *is* the style: a huge, modern,
tightly-tracked grotesk does the talking; tiny mono labels make it feel like software; a pixel
font and one soft serif add the early-internet memory.

| Voice | Family (Google Fonts) | Job | Never |
|---|---|---|---|
| **Display** | Inter Tight 500–600 | Hero headlines, wordmarks, section titles, big numbers | body text, all caps |
| **Sans** | Geist 400–600 | Body, UI, buttons, tables | sizes above 28px |
| **Mono** | Geist Mono 400–500 | Micro labels, metadata, counters, code, table headers, data | long sentences |
| **Serif** | Instrument Serif 400 (+ italic) | ONE soft headline per page (sky heroes), pull quotes, the wordmark of a gentle brand | UI, labels, mixing with display in the same line |
| **Pixel** | Silkscreen 400 | Stickers, LCD screens, "NEW!", visitor counters, tiny badges | anything over ~20px or longer than ~6 words |

Original-site fonts these replace (all proprietary): NB International / PP Neue Montreal /
Khteka → Inter Tight; Graphik / aktiv-grotesk → Geist; Suisse Mono / Geist Mono → Geist Mono;
the condensed serif in "sent." → Instrument Serif.

## Scale & settings

```css
.t-hero  { font: 600 var(--step-hero)/var(--lead-display) var(--font-display); letter-spacing: var(--track-display); }
.t-1     { font: 500 var(--step-1)/0.95 var(--font-display); letter-spacing: var(--track-display); }
.t-2     { font: 500 var(--step-2)/1.05 var(--font-display); letter-spacing: -0.03em; }
.t-3     { font: 500 var(--step-3)/1.15 var(--font-display); letter-spacing: var(--track-tight); }
.t-lead  { font: 400 var(--text-lg)/1.45 var(--font-sans); max-width: 38ch; }
.t-body  { font: 400 var(--text)/1.5 var(--font-sans); max-width: 62ch; }
.t-serif { font: 400 var(--step-1)/0.95 var(--font-serif); letter-spacing: -0.02em; color: var(--dialup-ink); }
.micro   { font: 500 var(--micro)/1.3 var(--font-mono); letter-spacing: var(--track-micro); text-transform: uppercase; }
.t-num   { font-family: var(--font-mono); font-variant-numeric: tabular-nums; }
```

Rules that make it look right:

1. **Go bigger than feels safe.** Hero type should fill 60–90% of the viewport width on desktop.
   Leading under 1 (0.85–0.95) and tracking around −0.045em. The size contrast with 11px
   micro labels is the point.
2. **Sentence case** for display and sans. Uppercase is reserved for mono micro labels, tiny
   buttons, and pixel stickers.
3. **Muted continuation:** in a long headline, fade the second half to `--ink-2` or `--ink-3` at
   large size (≥ 32px, so 3:1 is acceptable): *"It's a whole new level — <muted>you'll wonder how
   you managed before.</muted>"* (pxpush, orgnzm, monolog).
4. **Underscore and brackets** as typographic ornaments: `_brands`, `[ 01 ]`, `( scroll to explore )`,
   `01 / 05`, `→`, `↗`, `✱`. These are cheap and very on-brand.
5. **Numbers as heroes:** stats in display weight at `--step-1`, label in micro mono underneath.
   For a playful variant, draw numerals by hand (SVG strokes) or use "Permanent Marker"
   sparingly, one row of numerals max (Berd's 01 02 03 04).
6. **One serif moment.** On sky/Y2K pages use Instrument Serif for the main headline in
   `--dialup-ink` (navy), e.g. *"160 characters. Once a day."* Everything else stays sans.
7. Body text never goes below 15px on landing pages or 13px in dense app tables.
8. Measure: body 45–70ch; leads ≤ 40ch; headlines break by hand with `<br>` or `text-wrap: balance`.

## Pairing presets

- **Desk** (default, Berd/milk): Inter Tight + Geist + Geist Mono. Paper background.
- **Dial-up sky** (Dribbble/pxpush): Instrument Serif headline + Geist + Silkscreen accents, sky gradient.
- **Gallery** (monolog/yuanzuo): Inter Tight at hero size, condensed shouting via
  `font-stretch` is not available on Inter Tight, so for an all-caps condensed shout use
  "Archivo" with `font-variation-settings: "wdth" 62` (load `Archivo:wdth,wght@62..125,400..800`).
  Max one such line per page.
