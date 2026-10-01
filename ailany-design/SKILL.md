---
name: ailany-design
description: Ailany's house design system, "modern web with dial-up memories". A playful, motion-rich style mixing big modern grotesk type, paper-and-window desktop metaphors, flat glass, iridescent 3D toys with googly eyes, text-scramble hovers, brand-name preloaders, and Y2K accents (Aqua gel buttons, LCD screens, soap bubbles, pixel stickers). Use this skill whenever building or restyling anything visual for the web: landing pages, marketing sites, portfolios, product pages, app UI, dashboards, admin panels, components, HTML/CSS/React/Tailwind pages, or artifacts, even if the user doesn't mention the style. Also trigger on "my style", "ailany", "make it look like me", "y2k", "old internet", "retro but modern", "fun landing page", or requests for preloaders, 3D hero, glass modal, or hover text effects.
---

# Ailany design: modern web with dial-up memories

**The feeling:** booting up a friendly computer in 2001, rebuilt with 2026 craft. Calm and
spacious like a modern studio site, but with toys on the desk: things you can hover, drag, and
poke, and small reminders of the early internet (app windows, status dots, LCD screens, pixel
stickers, gel buttons, sky and bubbles). It is optimistic, a little uncanny, and never
cluttered. Nostalgia is **seasoning, not costume**: modern layout and type carry the page, and
retro details are accents.

## Before you build

1. Read `references/tokens.css` and paste it into the page. Use only its variables for color,
   type, space, radius, glass, and motion. Don't invent new hex values.
2. Then load what the job needs:
   - **Landing page / marketing / portfolio:** `references/layouts.md` (section A),
     `references/motion.md`, `references/components.md`. Start from `examples/landing.html`.
   - **App UI / dashboard / admin / tool:** `references/layouts.md` (section B),
     `references/components.md`. Start from `examples/dashboard.html`. Light motion only.
   - **A single component:** `references/components.md` (+ `typography.md` if type-heavy).
   - **Why something is the way it is:** `references/inspiration.md`.
3. Open the closest example file and adapt it. They are complete, tested, single-file pages.

## The ten rules

1. **Paper, not white.** Pages sit on warm paper `--paper` (#E6E6E1). Content lives in
   `--surface` windows/cards. Pure white is reserved for inputs and inner wells. UI colors come
   only from tokens; illustrations, 3D materials and CSS art may use lighter/darker tints of them.
2. **Huge, tight display type.** Inter Tight, leading ~0.9, tracking −0.045em, headlines far
   larger than feels safe. Pair with tiny uppercase **mono micro labels** (`[ 02 ] — Work`,
   `03:08 AM`, `v2.0.1`). This size contrast is the backbone of the look.
3. **Windows are the container.** Wrap key content in app windows with traffic lights and a
   mono file-name title (`readme.txt`, `inbox.app`). Use the retro variant sparingly.
4. **Flat glass only for things that float** (modal, nav pill, popover, toast, widgets) **or
   text that sits on top of 3D/imagery** and needs a backing. Square or pill, no drop shadow,
   `--glass-bg` + blur. Never glass an ordinary card in the flow.
5. **One lead accent per page** (`--dialup` blue is the default), with other Y2K colors as small
   sparks: lime for success/LCD, pink for notes, orange for live/cursor, yellow for one sticker.
   Orange, lime, pink and yellow always carry **ink** text, never white.
6. **Exactly one primary action per view** gets the Aqua **gel** button. Everything else is a
   small ink button, a hairline row with ↗, or a link. The fixed nav CTA is an ink pill
   (`.btn.btn--pill`) on landing pages so it never competes with the in-page gel.
7. **A brand moment on load** (landing pages only): the brand name rises and docks into the
   logo (motion §1). Under 2.5 s, skippable, once per session.
8. **At least one toy per landing page:** 3D buddies with googly eyes (motion §8), a physics
   drop zone (§9), soap bubbles (§10), or an LCD typewriter (§11). Usually one big toy plus
   one small one.
9. **Text reacts to the cursor:** nav links and list labels use the block-glyph **scramble**
   hover (motion §5); media gets a cursor-follower label ("View", "Drag").
10. **Motion respects people:** everything degrades under `prefers-reduced-motion`; contrast is
    AA (body text `--ink`/`--ink-2` only; `--ink-3` is decorative); real text exists behind
    every animated or split string (`aria-label`, `sr-only`).

## Do / don't

| Do | Don't |
|---|---|
| Lots of whitespace, few elements, big type | Dense grids of equal cards, stock "SaaS" hero |
| Asymmetric layouts, overlapping windows and stickers | Centered everything, perfectly boxed sections |
| One texture per page (dots, grain, scanlines or halftone) | Stacking textures, heavy gradients everywhere |
| File names, version stamps, status dots, local time | Fake error pop-ups, Comic Sans, under-construction GIFs |
| Original 3D from primitives, or the user's own assets | Copying logos, characters, renders or copy from the inspiration sites |
| Sentence case display; uppercase only for micro/pixel | All-caps headlines (except one condensed "shout" line max) |
| Gel button for the one main CTA | Gel/glossy on every button, or drop shadows on cards |

## Tech defaults

- Plain HTML/CSS/JS from CDN by default: GSAP 3.13 + ScrollTrigger, Lenis 1.3, Matter.js 0.20,
  three.js 0.170 via import map. Exact tags are in `motion.md §0`.
- **React/Next:** keep tokens as global CSS variables; use the same recipes inside effects with
  cleanup; three.js via `@react-three/fiber` is fine if the project already uses it.
- **Tailwind:** map tokens in `theme.extend` (`colors.paper: 'var(--paper)'`, etc.) and keep
  `tokens.css` as the source of truth; don't hard-code hex in classes.
- **Artifacts / single-file pages:** inline everything; the examples are already single-file.
- Fonts: one Google Fonts `<link>` (in the header of `tokens.css`). Only load the voices used.

## Copy voice

Short, warm, slightly funny, very human. Speak like a friendly computer: *"Less chatting, more
doing."* *"Loading good things… hang tight."* *"All systems normal."* *"Nothing here yet. Make
something weird."* Headlines are statements, not features. Microcopy can wink, but buttons stay
literal ("New project", "Get started").

## Quality check before you finish

- [ ] Paper background, tokens only, fonts loaded, AA contrast on all text.
- [ ] Hero type is genuinely huge; micro labels present; one gel CTA per view.
- [ ] Landing: preloader + at least one toy + scramble hovers + footer wordmark + status bar.
- [ ] App: window frame, sidebar, compact density, no preloader/Lenis/3D; dark mode works.
- [ ] Reduced motion: page fully readable and static. Mobile 390px: no horizontal scroll.
- [ ] No console errors; WebGL paused off-screen; only one canvas.
