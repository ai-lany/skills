# Layouts

Two page families share one system. **Landing pages** are loud, spacious, and full of motion.
**App UI / dashboards** are the same desk and windows with the volume turned down.

---

## A. Landing page anatomy

Pick sections from this list in roughly this order. Not every page needs every section, but
every page needs a hero, at least one "toy" (3D, physics, bubbles, LCD, sticker), and the footer.

| # | Section | What it looks like | Recipes |
|---|---|---|---|
| 0 | **Preloader** | Brand name rises, counter to 100, docks into nav logo | motion §1 (or §2/§3) |
| 1 | **Nav** | Floating glass pill nav, OR editorial corners (logo TL, stacked links top-center, widget TR, tiny ink CTA) | components §5, §10 |
| 2 | **Hero** | Pick one. **Desk:** giant headline on paper + 3D buddies + one window. **Sky:** serif headline on `--sky` gradient + bubbles + a device/LCD. **Wordmark:** brand name at `--step-hero` bottom-left + rotating `_word` | motion §4, §8, §10, §11 |
| 3 | **Intro statement** | 2–3 line headline that fades from ink to muted on scroll; micro label above; 3 stats with count-up below | motion §6, §12 |
| 4 | **Marquee** | One line of display text scrolling, `✱` separators | components §11 |
| 5 | **Features / services** | Numbered rows (`01`–`04`) with hairlines, title in display, short body, thumbnail that shows on hover; OR 4 columns with big numerals | components §4, motion §5 |
| 6 | **Work / showcase** | Chamfer cards in a horizontal row, or 2-col case grid with pill tags and cursor follower "View" | components §7, §15 |
| 7 | **Personalities** | 3 fanned spec cards (team, plans, agents, features as characters) | components §8 |
| 8 | **Playground** | Physics drop zone of tags/stickers, the "toy" moment | motion §9 |
| 9 | **Quote / social proof** | One huge quote on a saturated full-bleed block (`--signal`, `--dialup` or an image) with a yellow sticker CTA | components §3 |
| 10 | **CTA** | Window with chat/prompt input or a big gel button; `status` dot "Online · replies in 24h" | components §9, §4 |
| 11 | **Footer** | Ink block, giant wordmark bleeding off, OS status bar | components §16 |

### Grid & rhythm
- 12-col grid, `--gutter` gaps, max content width 1440px, edges padded `--gutter`.
- Use `padding-block: var(--section)` on sections, never the `padding: X 0` shorthand. The
  shorthand silently wipes the side gutter from `.wrap`, and headlines end up touching the
  screen edge.
- Sections are separated by `--section` vertical space, **not** by borders or alternating
  backgrounds. Use one or two full-bleed color blocks per page for drama (pxpush blue, orgnzm red).
- Asymmetry: headlines hug the left; supporting copy sits in columns 7–11; micro labels in col 1.
- Overlap is welcome: windows overlapping 3D buddies, a sticky note overlapping a window corner,
  a sticker overlapping a section edge.
- Mobile (≤ 720px): single column, hero type still ≥ 3.5rem, 3D reduced to ≤ 3 buddies or
  replaced by a static image, physics zone 320px tall, nav collapses to logo + CTA.

### Hero blueprints

**Desk hero**
```
[logo]                                   [status ● online]  [DOWNLOAD]
                 (3D buddies tumble in behind)
   ┌─ window: app.preview ──────────────────────────┐
   │ ● ● ●                                          │   ← overlaps buddies
   │  sidebar │  dot-grid canvas      [sticky note] │
   │          │          [ chat input ……… ↑ ]      │
   └────────────────────────────────────────────────┘
A better way
to build                       ← t-hero, centered or left
```

**Sky hero**
```
        ( glass pill nav: brand · links · [gel CTA] )
              160 characters.       ← Instrument Serif, navy
               Once a day.
        short lead in Geist, centered, 2 lines
  ~bubbles~        [ device or LCD window ]        ~bubbles~
  ▓▓ sky gradient fading into grass/paper, optional halftone ▓▓
```

**Wordmark hero**
```
[micro label]        Work  Expertise  Hello  Discover        [Contact]
We grow
_brands                               ← rotating word, caret blink
                         ┌────────┐
                         │ black  │  ← video/3D window
                         └────────┘     Short positioning statement
ailany                                   in 3 lines.     (scroll down)
```

---

## B. App UI / dashboard anatomy

Same paper desk, same windows, but compact density, `--text-sm` base, and nearly no motion.
The app itself is one big window on the paper; panels inside are flat surfaces.

```
paper (dot texture optional)
┌─ window ── ● ● ●  ◧  ← →                       ⌕  ⊞  🌐 ─┐
│ ┌ sidebar ┐ ┌ header: page title  [tabs] ............. [btn] ┐│
│ │ search  │ │ KPI  KPI  KPI  KPI    ← 4 tiles, display numbers ││
│ │ Home    │ │ ┌ chart window ───────────┐ ┌ sticky note ┐      ││
│ │ Agents  │ │ │                         │ │ checklist   │      ││
│ │ Skills  │ │ └─────────────────────────┘ └─────────────┘      ││
│ │Projects │ │ ┌ table ───────────────────────────────────────┐ ││
│ │ …       │ │ │ MONO HEADERS · rows · status pills           │ ││
│ │Settings │ │ └──────────────────────────────────────────────┘ ││
│ └─────────┘ └ [ chat / command input ……………………… 🎙 ↑ ] ───────┘│
└──────────────────────────────────────────────────────────────┘
status bar: ● synced · 3 agents running · v2.0.1           03:08
```

Rules:
- **Window chrome on the outer app frame** (traffic lights, back/forward, search). Inner panels
  are `--surface-2` cards with `--r-3`, no shadows, separated by 12–16px gaps.
- Sidebar 220–240px: icon + label rows, muted group headings, active row filled `--paper-2`,
  Settings pinned to the bottom.
- Page header: title in Inter Tight 500 at 28–32px, micro label above it (`[ workspace ]`),
  tabs as a segmented pill, one solid ink action button.
- KPI tiles: big display number, micro label, delta chip in `--lcd` (up) / `--sticky` (down).
- Charts: ink lines/bars on surface, one accent series in `--dialup`, gridlines `--line`;
  mono tick labels. Follow the `dataviz` skill for chart mechanics if available.
- Personality lives in: the sticky-note onboarding checklist, empty states (LCD screen with a
  typed message, or a small 3D buddy still image), friendly microcopy, the status bar, and
  file-like naming. Not in motion.
- Modals and command palettes use flat glass. Toasts glass, bottom-right.
- Density: row height 40–44px in tables, 32px buttons, 14px text. Dark mode should be supported
  in apps (`data-theme="dark"`).
- Allowed motion: window-boot on first load, 320ms modal/panel transitions, count-ups, scramble
  on sidebar hover (optional), status dot ping.

### Empty-state recipe
```html
<div class="window" style="max-width:420px;margin:auto">
  <header class="window__bar"><span class="window__lights"><i></i><i></i><i></i></span><span class="window__title">nothing_here.txt</span></header>
  <div class="window__body" style="display:grid;gap:16px;justify-items:start">
    <div class="lcd" data-type='["no projects yet","make something weird"]'><span data-out></span><span class="caret"></span></div>
    <p class="t-body">Projects you create show up here. Start one from scratch or from a template.</p>
    <button class="btn-gel">New project</button>
  </div>
</div>
```
