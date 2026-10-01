# Components

Every snippet assumes `tokens.css` is loaded. Copy the CSS once per page, not per instance.
Class names are short and prefixed-free on purpose; rename freely to match a codebase.

**Contents**
1. Window (the signature container)
2. Flat-glass modal
3. Buttons: gel, solid, ghost-arrow, sticker
4. Micro labels, brackets, status dot, tags
5. Floating pill nav
6. Sticky note checklist
7. Chamfer (octagon) card
8. Spec card ("Good for / Vibes")
9. Chat / command input
10. Desktop widgets: clock, mini case card
11. Marquee
12. Sidebar (app)
13. KPI tile, table, tabs, toast
14. LCD screen
15. Cursor follower
16. Footer wordmark + status bar
17. Textures
18. Pricing & products

---

## 1. Window

The core idea of the whole system: content lives in **app windows sitting on a paper desk**.
Modern macOS traffic lights by default; the `.window--retro` variant swaps in Win-98-ish
`_ ▢ ✕` buttons when a page wants a stronger old-internet wink. Use 1–3 windows per landing-page
section; in apps, every panel is a window.

```html
<section class="window" aria-label="Inbox">
  <header class="window__bar">
    <span class="window__lights" aria-hidden="true"><i></i><i></i><i></i></span>
    <span class="window__title">inbox.app</span>
    <span class="window__meta">03:08 AM</span>
  </header>
  <div class="window__body">…</div>
</section>
```

```css
.window { background: var(--surface); border-radius: var(--r-3); box-shadow: var(--shadow-window);
  border: 1px solid var(--line); overflow: hidden; }
.window__bar { display: flex; align-items: center; gap: var(--s-3); height: 40px; padding: 0 var(--s-4);
  border-bottom: 1px solid var(--line); font: 500 var(--micro)/1 var(--font-mono);
  letter-spacing: var(--track-micro); text-transform: uppercase; color: var(--ink-2); }
.window__lights { display: flex; gap: 6px; }
.window__lights i { width: 11px; height: 11px; border-radius: 50%; background: #FF5F57; }
.window__lights i:nth-child(2) { background: #FEBC2E; }
.window__lights i:nth-child(3) { background: #28C840; }
.window__title { flex: 1; text-align: center; }
.window__body { padding: var(--s-5); }
.window--dots .window__body { background: var(--tex-dots); }  /* Berd-style canvas */

/* Retro variant: square, hard shadow, chunky bar */
.window--retro { border-radius: var(--r-1); border: 1.5px solid var(--ink); box-shadow: var(--shadow-hard); }
.window--retro .window__bar { background: var(--dialup); color: #fff; border-bottom: 1.5px solid var(--ink); }
.window--retro .window__lights { order: 3; }
.window--retro .window__lights i { width: 18px; height: 16px; border-radius: 2px; background: var(--surface);
  border: 1.5px solid var(--ink); }
```
For the retro buttons, put glyphs inside: `<i>_</i><i>▢</i><i>✕</i>` with
`font: 10px/13px var(--font-pixel); color: var(--ink); text-align:center; font-style:normal`.

## 2. Flat-glass modal

Frosted, square, no drop shadow, the yuanzuo look. Glass is **only** for things that float above
content (modal, nav, popover, toast, cookie bar). Never glass a card that sits in the flow.

```html
<div class="scrim" data-open>
  <div class="glass-modal" role="dialog" aria-modal="true" aria-labelledby="m-title">
    <header class="glass-modal__bar"><span id="m-title">New project</span>
      <button class="icon-btn" aria-label="Close">✕</button></header>
    <div class="glass-modal__body">…</div>
  </div>
</div>
```
```css
.scrim { position: fixed; inset: 0; z-index: var(--z-modal); display: grid; place-items: center;
  background: rgba(11,11,10,.18); opacity: 0; pointer-events: none; transition: opacity var(--dur-ui) var(--ease-out); }
.scrim[data-open] { opacity: 1; pointer-events: auto; }
.glass-modal { width: min(560px, calc(100vw - 32px)); background: var(--glass-bg);
  backdrop-filter: var(--glass-blur); -webkit-backdrop-filter: var(--glass-blur);
  border: var(--glass-border); border-radius: var(--r-0);
  transform: translateY(12px) scale(.98); transition: transform var(--dur-ui) var(--ease-out); }
.scrim[data-open] .glass-modal { transform: none; }
.glass-modal__bar { display: flex; justify-content: space-between; align-items: center; padding: var(--s-3) var(--s-4);
  border-bottom: 1px solid var(--line); font: 500 var(--micro)/1 var(--font-mono); letter-spacing: var(--track-micro); text-transform: uppercase; }
.glass-modal__body { padding: var(--s-5); }
```
Text on glass must stay ≥ 4.5:1; if the backdrop can be busy (photos, 3D), raise `--glass-bg`
alpha to `.8`. Close on Esc and scrim click; return focus to the opener.

## 3. Buttons

| Kind | When | Look |
|---|---|---|
| `.btn-gel` | the ONE primary action per view | Aqua gel pill, glossy highlight, white text |
| `.btn` | app actions, nav CTA | small ink pill/rect, uppercase mono or 14px sans |
| `.btn-line` | lists of links, secondary CTAs | full-width hairline row + ↗ |
| `.sticker` | playful CTA on landing pages, max one per page | round yellow, rotated, hard shadow |

```css
.btn-gel { position: relative; display: inline-flex; align-items: center; gap: 8px; height: 44px; padding: 0 22px;
  border-radius: var(--r-pill); border: 1px solid #1A22B0; color: #fff; background: var(--gel);
  font: 500 15px/1 var(--font-sans); box-shadow: 0 1px 0 rgba(255,255,255,.4) inset, 0 6px 16px -6px rgba(36,51,255,.6);
  cursor: pointer; transition: transform var(--dur-micro) var(--ease-out), filter var(--dur-micro); }
.btn-gel::before { content: ""; position: absolute; inset: 2px 10px auto; height: 45%; border-radius: var(--r-pill);
  background: var(--gel-shine); opacity: .7; pointer-events: none; }
.btn-gel:hover { filter: brightness(1.08) saturate(1.1); }
.btn-gel:active { transform: translateY(1px) scale(.98); }

.btn { display: inline-flex; align-items: center; gap: 6px; height: 32px; padding: 0 12px; border-radius: var(--r-1);
  background: var(--ink); color: var(--paper); border: 0; cursor: pointer;
  font: 500 var(--micro)/1 var(--font-mono); letter-spacing: var(--track-micro); text-transform: uppercase; }
.btn--quiet { background: transparent; color: var(--ink); border: 1px solid var(--line-strong); }
.btn--pill { height: 38px; padding: 0 18px; border-radius: var(--r-pill); }   /* nav CTA */
.btn:hover { background: var(--dialup); color: #fff; }

.btn-line { display: flex; justify-content: space-between; align-items: center; padding: 14px 0;
  border-top: 1px solid var(--line-strong); color: var(--ink); text-decoration: none;
  font: 400 var(--text-sm)/1 var(--font-mono); }
.btn-line::after { content: "↗"; transition: transform var(--dur-micro) var(--ease-out); }
.btn-line:hover::after { transform: translate(3px,-3px); }

.sticker { display: grid; place-items: center; width: 128px; aspect-ratio: 1; border-radius: 50%;
  background: var(--sticker); color: var(--on-accent); border: 1.5px solid var(--ink); box-shadow: var(--shadow-hard);
  font: 400 12px/1 var(--font-pixel); text-transform: uppercase; transform: rotate(-12deg);
  transition: transform var(--dur-ui) var(--ease-spring); cursor: pointer; }
.sticker:hover { transform: rotate(6deg) scale(1.06); }
```

## 4. Micro labels, brackets, status dot, tags

The connective tissue. Every section opens with a mono micro label; numbers get brackets or slashes.

```html
<p class="micro">[ 02 ] — Selected work</p>
<span class="status"><i></i> Online · accepting projects</span>
<ul class="tags"><li>Branding</li><li>Web</li><li>3D</li></ul>
```
```css
.micro { font: 500 var(--micro)/1.3 var(--font-mono); letter-spacing: var(--track-micro);
  text-transform: uppercase; color: var(--ink-2); }
.micro--pixel { font-family: var(--font-pixel); font-weight: 400; letter-spacing: .02em; }
.status { display: inline-flex; align-items: center; gap: 8px; font: 500 var(--micro)/1 var(--font-mono);
  letter-spacing: var(--track-micro); text-transform: uppercase; }
.status i { width: 7px; height: 7px; border-radius: 50%; background: var(--online);
  box-shadow: 0 0 0 0 rgba(25,194,107,.5); animation: ping 2s var(--ease-out) infinite; }
@keyframes ping { to { box-shadow: 0 0 0 8px rgba(25,194,107,0); } }
.tags { display: flex; flex-wrap: wrap; gap: 6px; list-style: none; padding: 0; margin: 0; }
.tags li { padding: 4px 10px; border: 1px solid var(--line-strong); border-radius: var(--r-pill);
  font: 400 var(--text-xs)/1.2 var(--font-sans); }
```
Copy style for labels: lowercase-playful file and app names (`inbox.app`, `readme.txt`,
`about_me.html`), version stamps (`v2.0.1`), counters (`0005`, `01 / 05`), coordinates/time
(`24.14° N · 03:08 AM`). It sells the "computer" feeling without costume.

## 5. Floating pill nav

```html
<nav class="pillnav">
  <a class="pillnav__brand" href="/">sent.</a>
  <ul><li><a href="#why">Why it exists</a></li><li><a href="#pricing">Pricing</a></li></ul>
  <a class="btn btn--pill" href="#start">Get started</a>
</nav>
```
```css
.pillnav { position: fixed; top: 16px; left: 50%; translate: -50% 0; z-index: var(--z-nav);
  width: min(960px, calc(100vw - 32px)); display: flex; align-items: center; gap: var(--s-5);
  padding: 6px 6px 6px 20px; border-radius: var(--r-pill); background: var(--glass-bg);
  backdrop-filter: var(--glass-blur); -webkit-backdrop-filter: var(--glass-blur); border: var(--glass-border); }
.pillnav ul { display: flex; gap: var(--s-5); margin: 0 auto; padding: 0; list-style: none; }
.pillnav a:not(.btn-gel) { color: var(--ink); text-decoration: none; font: 500 var(--text-sm)/1 var(--font-sans); }
.pillnav__brand { font: 400 22px/1 var(--font-serif) !important; }

@media (max-width: 720px) { .pillnav ul { display: none; } .pillnav { justify-content: space-between; } }
```
Alternative, editorial: no bar at all. Logo top-left, a vertical stack of tiny links top-center,
a widget top-right (milk / yuanzuo / orgnzm). Use that on portfolio-style pages.

## 6. Sticky note checklist

```html
<aside class="sticky">
  <header><b>Starter list</b><button aria-label="Dismiss">✕</button></header>
  <label><input type="checkbox"> Connect your domain</label>
  <label><input type="checkbox" checked> Invite the team</label>
</aside>
```
```css
.sticky { width: 220px; padding: 12px 14px; background: var(--sticky); color: var(--on-accent);
  border-radius: 2px; font: 400 var(--text-xs)/1.4 var(--font-sans); rotate: -1.5deg;
  box-shadow: 0 10px 20px -12px rgba(11,11,10,.35); }
.sticky header { display: flex; justify-content: space-between; margin-bottom: 8px; }
.sticky label { display: flex; gap: 8px; align-items: center; padding: 3px 0; }
.sticky input { accent-color: var(--on-accent); }
.sticky input:checked + * , .sticky label:has(input:checked) { text-decoration: line-through; opacity: .55; }
```

## 7. Chamfer card

Octagon-cut corners, black, for showcases and galleries (Berd).
```css
.chamfer { background: var(--ink); color: var(--paper); aspect-ratio: 1; display: grid; place-items: center;
  clip-path: polygon(var(--chamfer) 0, calc(100% - var(--chamfer)) 0, 100% var(--chamfer), 100% calc(100% - var(--chamfer)),
    calc(100% - var(--chamfer)) 100%, var(--chamfer) 100%, 0 calc(100% - var(--chamfer)), 0 var(--chamfer)); }
.chamfer--soft { --chamfer: 0%; border-radius: var(--r-3); }  /* alternate in a row: cut, square, cut… */
```
Caption under each: title in `--text` 500, quote-style description in `--text-sm` `--ink-2`.

## 8. Spec card

A personality card for features, team members, plans or agents.
```html
<article class="spec">
  <div class="spec__art">[3D buddy or image]</div>
  <h3>Choosey</h3>
  <p>Makes choices clearer without making them for you.</p>
  <dl><div><dt>Good for</dt><dd>getting off the fence</dd></div><div><dt>Vibes</dt><dd>deliberate, a little skeptical</dd></div></dl>
</article>
```
```css
.spec { background: var(--surface); padding: var(--s-5); width: 320px; }
.spec h3 { font: 500 var(--step-3)/1.1 var(--font-display); letter-spacing: var(--track-tight); margin: var(--s-4) 0 var(--s-2); }
.spec p { color: var(--ink); font-size: var(--text-sm); margin: 0 0 var(--s-4); }
.spec dl { display: grid; grid-template-columns: 1fr 1fr; gap: var(--s-4); margin: 0; }
.spec dl div { border-left: 1.5px solid var(--ink); padding-left: 10px; font-size: var(--text-xs); }
.spec dt { font-weight: 600; } .spec dd { margin: 0; }
```
Stack 3 spec cards fanned (center one raised and in front) for a playful carousel.

## 9. Chat / command input

```html
<form class="prompt"><input placeholder="Start a conversation" aria-label="Message">
  <button type="button" class="icon-btn" aria-label="Voice">🎙</button>
  <button class="icon-btn icon-btn--ink" aria-label="Send">↑</button></form>
```
```css
.prompt { display: flex; align-items: center; gap: 6px; padding: 6px 6px 6px 18px; background: var(--surface-2);
  border: 1px solid var(--line); border-radius: var(--r-pill); }
.prompt input { flex: 1; border: 0; background: none; font: 400 var(--text-sm)/1 var(--font-sans); color: var(--ink); outline: none; }
.icon-btn { width: 32px; height: 32px; display: grid; place-items: center; border-radius: 50%; border: 0;
  background: var(--paper-2); color: var(--ink); cursor: pointer; font-size: 14px; }
.icon-btn--ink { background: var(--ink); color: var(--paper); }
```
Prefer inline SVG icons (1.5px stroke, 16px, `currentColor`) over emoji in production.

## 10. Desktop widgets

Small, informational, slightly useless on purpose: they make a page feel like a desktop.
```html
<div class="widget"><span class="micro">Taipei, TW</span><span class="micro">Local time</span>
  <b class="widget__big" data-clock>03:08 AM</b></div>
```
```css
.widget { display: grid; grid-template-columns: 1fr auto; gap: 4px var(--s-4); padding: var(--s-4);
  background: var(--surface); min-width: 220px; }
.widget__big { grid-column: 1 / -1; font: 500 var(--step-3)/1 var(--font-mono); }
```
```js
document.querySelectorAll('[data-clock]').forEach(el => {
  const tick = () => el.textContent = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  tick(); setInterval(tick, 10_000);
});
```
Other widget ideas: analog clock (black circle, red second hand), weather glyph, "now playing",
visitor counter in pixel font (`00042 visitors`), a mini "new case" card with a thumbnail.

## 11. Marquee

```html
<div class="marquee" aria-hidden="true"><div class="marquee__track">
  <span>Let's start a conversation ✱</span><span>Let's start a conversation ✱</span></div></div>
```
```css
.marquee { overflow: hidden; white-space: nowrap; border-block: 1px solid var(--line-strong); }
.marquee__track { display: inline-flex; gap: 2ch; animation: marquee 22s linear infinite;
  font: 400 var(--step-1)/1.1 var(--font-display); letter-spacing: var(--track-display); }
.marquee:hover .marquee__track { animation-play-state: paused; }
@keyframes marquee { to { transform: translateX(-50%); } }
```
Duplicate the content so the track is 2× wide. Provide the real text elsewhere for screen readers.

## 12. Sidebar (app)

```html
<nav class="side">
  <label class="side__search"><input placeholder="Search" aria-label="Search"></label>
  <a class="side__item is-active" href="#">⌂ Home</a><a class="side__item" href="#">☺ Agents</a>
  <p class="side__group">Projects</p><a class="side__item" href="#">＋ Start a project</a>
  <a class="side__item side__foot" href="#">⚙ Settings</a>
</nav>
```
```css
.side { display: flex; flex-direction: column; gap: 2px; width: 220px; padding: 10px; background: var(--surface-2);
  border-radius: var(--r-3); font: 400 var(--text-sm)/1 var(--font-sans); }
.side__item { display: flex; gap: 10px; align-items: center; padding: 8px 10px; border-radius: var(--r-2);
  color: var(--ink); text-decoration: none; }
.side__item:hover { background: var(--paper); }
.side__item.is-active { background: var(--paper-2); font-weight: 500; }
.side__group { margin: 14px 10px 4px; color: var(--ink-2); font-size: var(--text-xs); }
.side__foot { margin-top: auto; border-top: 1px solid var(--line); border-radius: 0; padding-top: 12px; }
```

## 13. KPI tile, table, tabs, toast

```css
.kpi { background: var(--surface); border-radius: var(--r-3); padding: var(--s-4) var(--s-5); }
.kpi__value { font: 500 var(--step-2)/1 var(--font-display); letter-spacing: var(--track-display); font-variant-numeric: tabular-nums; }
.kpi__delta { font: 500 var(--text-xs)/1 var(--font-mono); padding: 3px 6px; border-radius: var(--r-1); background: var(--lcd); color: var(--lcd-ink); }
.kpi__delta--down { background: var(--sticky); color: var(--on-accent); }

.table { width: 100%; border-collapse: collapse; font: 400 var(--text-sm)/1.3 var(--font-sans); }
.table th { text-align: left; font: 500 var(--micro)/1 var(--font-mono); letter-spacing: var(--track-micro);
  text-transform: uppercase; color: var(--ink-2); padding: 10px 12px; border-bottom: 1px solid var(--line-strong); }
.table td { padding: 12px; border-bottom: 1px solid var(--line); }
.table td.num { font-family: var(--font-mono); text-align: right; font-variant-numeric: tabular-nums; }
.table tr:hover td { background: var(--paper); }

.tabs { display: inline-flex; padding: 3px; gap: 2px; background: var(--paper-2); border-radius: var(--r-pill); }
.tabs button { border: 0; background: none; padding: 6px 14px; border-radius: var(--r-pill); cursor: pointer;
  font: 500 var(--text-sm)/1 var(--font-sans); color: var(--ink-2); }
.tabs button[aria-selected="true"] { background: var(--surface-2); color: var(--ink); box-shadow: 0 1px 2px rgba(11,11,10,.12); }

.toast { position: fixed; right: 16px; bottom: 16px; z-index: var(--z-modal); display: flex; gap: 10px; align-items: center;
  padding: 10px 14px; background: var(--glass-bg); backdrop-filter: var(--glass-blur); -webkit-backdrop-filter: var(--glass-blur);
  border: var(--glass-border); font: 400 var(--text-sm)/1.3 var(--font-sans); }
```
Status pills inside tables: `lcd` = done/healthy, `sticky` = needs attention, `signal` = failing,
outline = idle. Always include a text label, never color alone.

## 14. LCD screen

Nokia-green rectangle with pixel text: for empty states, loaders, tiny notifications, quotes.
```css
.lcd { background: var(--lcd); color: var(--lcd-ink); padding: 14px 16px; border-radius: 6px;
  box-shadow: inset 0 0 0 3px rgba(34,48,10,.25), inset 0 0 24px rgba(34,48,10,.25);
  font: 400 15px/1.35 var(--font-pixel); background-image: var(--tex-scan); background-blend-mode: multiply; }
.lcd .caret::after { content: "▌"; animation: blink 1s steps(1) infinite; }
@keyframes blink { 50% { opacity: 0; } }
```
Pair with the typewriter recipe in `motion.md`.

## 15. Cursor follower

A small dot that grows into a label ("View", "Drag", "Open") over interactive media (yuanzuo, qando).
See `motion.md → Cursor follower` for the JS. Styles:
```css
.cursor { position: fixed; left: 0; top: 0; z-index: var(--z-cursor); pointer-events: none;
  width: 12px; height: 12px; border-radius: 50%; background: var(--signal); translate: -50% -50%;
  display: grid; place-items: center; transition: width var(--dur-ui) var(--ease-out), height var(--dur-ui) var(--ease-out); color: var(--on-accent); }
.cursor[data-label]::after { content: attr(data-label); font: 500 11px/1 var(--font-mono); color: var(--ink); text-transform: uppercase; }
.cursor[data-label] { width: 64px; height: 64px; }
@media (hover: none) { .cursor { display: none; } }
```

## 16. Footer wordmark + status bar

End pages with a giant wordmark that bleeds off the edges, then a thin OS-style status bar.
```html
<footer class="foot">
  <div class="foot__mark" aria-hidden="true">ailany</div>
  <div class="statusbar"><span class="status"><i></i> All systems normal</span>
    <span class="micro">© 2026 · Built on a dial-up dream</span><span class="micro" data-clock></span></div>
</footer>
```
```css
.foot { background: var(--ink); color: var(--paper); overflow: hidden; border-radius: var(--r-3) var(--r-3) 0 0; }
.foot__mark { font: 600 clamp(6rem, 24vw, 22rem)/.78 var(--font-display); letter-spacing: -.06em;
  padding-top: var(--s-8); margin-left: -.04em; white-space: nowrap; }
.statusbar { display: flex; justify-content: space-between; gap: var(--s-4); flex-wrap: wrap;
  padding: 10px var(--gutter); border-top: 1px solid rgba(232,232,227,.15); }
.statusbar .micro { color: inherit; opacity: .7; }
```

## 17. Textures
18. Pricing & products

Choose one per page and keep it subtle; it is seasoning, not a theme.
```css
.tex-dots  { background-image: var(--tex-dots); }                 /* app canvases, Berd */
.tex-grain::after { content: ""; position: fixed; inset: -50%; z-index: var(--z-texture); pointer-events: none;
  background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='.5'/%3E%3C/svg%3E");
  opacity: .08; mix-blend-mode: multiply; }                       /* editorial, monolog */
.tex-crt::after { content: ""; position: fixed; inset: 0; z-index: var(--z-texture); pointer-events: none;
  background: var(--tex-scan), radial-gradient(ellipse at center, transparent 60%, rgba(0,0,0,.25) 100%); } /* px push */
.tex-halftone { -webkit-mask-image: radial-gradient(circle, #000 0.9px, transparent 1.1px); -webkit-mask-size: 4px 4px; } /* dithered images */
```
For a dithered, early-web photo, layer the same image twice: the base, then a copy with
`.tex-halftone` and `mix-blend-mode: multiply` at 50% opacity.

## 18. Pricing & products

**Pricing = spec cards with a price line.** Plans are personalities (§8): name, one-line promise,
price in display type, `Good for / Vibes`, a hairline list of inclusions, one action. Fan three
cards (middle raised, carrying the only gel button) or lay them in a row on mobile.
```html
<article class="spec">
  <h3>Studio</h3><p>Full brand and site in about eight weeks.</p>
  <p class="price"><b>$12k</b><span class="micro">/ project</span></p>
  <ul class="incl"><li>Identity + guidelines</li><li>Up to 8 pages</li><li>3D hero buddy</li></ul>
  <button class="btn-gel">Start with Studio</button>
</article>
```
```css
.price { display: flex; align-items: baseline; gap: 8px; margin: var(--s-4) 0; }
.price b { font: 500 var(--step-2)/1 var(--font-display); letter-spacing: -0.04em; }
.price s { color: var(--ink-3); font: 400 var(--text-sm)/1 var(--font-mono); }   /* old price, pxpush-style */
.incl { list-style: none; padding: 0; margin: 0 0 var(--s-5); font: 400 var(--text-xs)/1 var(--font-mono); }
.incl li { padding: 9px 0; border-top: 1px solid var(--line); }
```

**Product card** (shop items, subscriptions): a `--surface` card with the product on a tinted
square (`--sticky`/`--lcd`/sky), name + price on one line, a tags row, a small ink "Add" button.
Optional pixel sticker (`NEW!`, `SOLD OUT`) rotated on the corner. Hover: image scales 1.03,
name scrambles.
```css
.product { background: var(--surface); padding: var(--s-3); border-radius: var(--r-3); position: relative; }
.product__img { aspect-ratio: 1; border-radius: var(--r-2); background: var(--lcd); overflow: hidden; display: grid; place-items: center; color: var(--on-accent); }
.product__img img { transition: transform var(--dur-ui) var(--ease-out); } .product:hover .product__img img { transform: scale(1.03); }
.product__row { display: flex; justify-content: space-between; align-items: baseline; padding: var(--s-3) var(--s-1) var(--s-2); }
.product__row b { font: 500 var(--text)/1.2 var(--font-display); } .product__row span { font: 500 var(--text-sm)/1 var(--font-mono); }
.product .sticker-sm { position: absolute; top: -10px; right: -10px; rotate: 12deg; }
```
