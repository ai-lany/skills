# Motion & interaction recipes

Motion is half of this style. Pages should feel like booting up a friendly computer: a brand
moment on load, text that reacts to the cursor, toys you can poke. Every recipe below is
copy-paste ready, works from CDN with no build step, and **degrades to a calm static page under
`prefers-reduced-motion`**. That's why each one checks `REDUCE` first.

**Contents**
0. Setup: libraries, Lenis, the `REDUCE` flag
1. Preloader A: Wordmark rise → dock (default)
2. Preloader B: Dot counter (playful alt)
3. Preloader C: Window boot (for app / product sites)
4. Rotating word with underscore caret
5. Text scramble hover (signature hover)
6. Line / word reveal on scroll
7. Cursor follower label
8. 3D buddies: iridescent toys with googly eyes (three.js)
9. Physics drop: draggable pills & stickers (Matter.js)
10. Soap bubbles (CSS)
11. LCD typewriter
12. Logo flip + counters + marquee speed-up
13. Budget & rules

---

## 0. Setup

```html
<!-- in <head> -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/lenis@1.3.11/dist/lenis.css">
<!-- end of <body>, only what the page uses -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.13.0/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.13.0/ScrollTrigger.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/lenis@1.3.11/dist/lenis.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/matter-js/0.20.0/matter.min.js"></script>  <!-- §9 only -->
<script type="importmap">{ "imports": {
  "three": "https://cdn.jsdelivr.net/npm/three@0.170.0/build/three.module.js",
  "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.170.0/examples/jsm/" } }</script>  <!-- §8 only -->
```
```js
const REDUCE = matchMedia('(prefers-reduced-motion: reduce)').matches;
const FINE = matchMedia('(hover: hover) and (pointer: fine)').matches;   // desktop pointer
gsap.registerPlugin(ScrollTrigger);
gsap.defaults({ ease: 'expo.out', duration: 0.9 });

let lenis = null;
if (!REDUCE) {
  lenis = new Lenis({ lerp: 0.1, smoothWheel: true });
  lenis.on('scroll', ScrollTrigger.update);
  gsap.ticker.add(t => lenis.raf(t * 1000));
  gsap.ticker.lagSmoothing(0);
}
```
In React/Next: same calls inside a `useEffect`/`useGSAP` with cleanup (`lenis.destroy()`,
`ScrollTrigger.killAll()`), or use `lenis/react` and `@gsap/react`.

## 1. Preloader A: Wordmark rise → dock

The brand name rises letter by letter out of a mask at huge size while a mono counter ticks to
100, then the wordmark **shrinks and flies into the nav logo slot** as the loader wipes away
(milk). Under 2.5 s, skippable, once per session.

```html
<div class="loader" data-loader>
  <div class="loader__bg"></div>
  <div class="loader__mark" aria-hidden="true" data-text="ailany"></div>
  <span class="loader__count micro">000</span>
  <button class="loader__skip micro" type="button">Skip ↵</button>
</div>
<!-- the real logo in the nav must carry data-logo -->
<a href="/" class="logo" data-logo>ailany</a>
```
```css
.loader { position: fixed; inset: 0; z-index: var(--z-loader); pointer-events: auto; }
.loader__bg { position: absolute; inset: 0; background: var(--paper); }
.loader__mark { position: absolute; left: var(--gutter); bottom: -0.12em; display: flex; overflow: hidden;
  font: 600 var(--step-hero)/0.9 var(--font-display); letter-spacing: var(--track-display); transform-origin: 0 0; }
.loader__mark span { display: inline-block; }
.loader__count { position: absolute; right: var(--gutter); bottom: var(--gutter); font-variant-numeric: tabular-nums; }
.loader__skip { position: absolute; right: var(--gutter); top: var(--gutter); background: none; border: 0; cursor: pointer; color: var(--ink-2); }
.is-loading { overflow: hidden; }
.logo { font: 600 22px/1 var(--font-display); letter-spacing: var(--track-display); }
```
```js
function preloaderRise() {
  const L = document.querySelector('[data-loader]');
  if (!L) return Promise.resolve();
  let seen = false;
  try { seen = sessionStorage.getItem('booted') === '1'; sessionStorage.setItem('booted', '1'); } catch {}
  if (REDUCE || seen) { L.remove(); return Promise.resolve(); }

  document.documentElement.classList.add('is-loading');
  lenis?.stop();
  const mark = L.querySelector('.loader__mark');
  mark.innerHTML = [...mark.dataset.text].map(c => `<span>${c === ' ' ? '&nbsp;' : c}</span>`).join('');  // works for multi-word names
  const letters = mark.querySelectorAll('span');
  const count = L.querySelector('.loader__count'), logo = document.querySelector('[data-logo]');
  const n = { v: 0 };
  gsap.set(logo, { opacity: 0 });

  const dock = k => {                                  // FLIP target, measured when the dock starts
    const a = mark.getBoundingClientRect(), b = logo.getBoundingClientRect();
    return { x: b.left - a.left, y: b.top - a.top, s: b.height / a.height }[k];
  };
  const tl = gsap.timeline();
  tl.from(letters, { yPercent: 110, duration: 0.9, stagger: 0.06 })            // rise: 0 → 1.2s
    .to(n, { v: 100, duration: 1.3, ease: 'power2.inOut',
             onUpdate: () => count.textContent = String(Math.round(n.v)).padStart(3, '0') }, 0)
    .to(mark, { x: () => dock('x'), y: () => dock('y'), scale: () => dock('s'),
                duration: 0.8, ease: 'expo.inOut' }, 1.45)                    // hold, then dock
    .to(L.querySelector('.loader__bg'), { yPercent: -100, duration: 0.8, ease: 'expo.inOut' }, 1.45)
    .to([count, L.querySelector('.loader__skip')], { opacity: 0, duration: 0.2 }, 1.45)
    .set(logo, { opacity: 1 })
    .to(mark, { opacity: 0, duration: 0.15 });                                // total ≈ 2.4s

  const skip = () => tl.progress(1);
  L.querySelector('.loader__skip').addEventListener('click', skip);
  addEventListener('keydown', skip, { once: true });

  return new Promise(res => tl.eventCallback('onComplete', () => {
    L.remove(); document.documentElement.classList.remove('is-loading'); lenis?.start(); res();
  }));
}
// usage:
// document.fonts.ready.then(preloaderRise).then(() => {
//   introHero(); window.__booted = true; dispatchEvent(new Event('booted')); ScrollTrigger.refresh();
// });
```

## 2. Preloader B: Dot counter

A small dot that **changes color every 120 ms** (lcd → sticky → dialup → signal) beside a
percent counter; at 100 a grid of outlined circles fills in and resolves into the headline
(miroom). Good for playful brands; pair with a chunky rounded wordmark.

```html
<div class="loader loader--dot" data-loader-dot><i class="loader__dot"></i><span class="loader__pct micro">0%</span></div>
```
```css
.loader--dot { display: flex; align-items: center; justify-content: center; gap: 12px; background: var(--paper); }
.loader__dot { width: 14px; height: 14px; border-radius: 50%; background: var(--lcd); color: var(--on-accent); }
```
```js
function preloaderDot() {
  const L = document.querySelector('[data-loader-dot]');
  if (!L || REDUCE) { L?.remove(); return Promise.resolve(); }
  const dot = L.querySelector('.loader__dot'), pct = L.querySelector('.loader__pct');
  const colors = ['--lcd', '--sticky', '--dialup', '--signal', '--sticker'].map(v => `var(${v})`);
  let i = 0; const swap = setInterval(() => dot.style.background = colors[i++ % colors.length], 120);
  const n = { v: 0 };
  return gsap.timeline()
    .to(n, { v: 100, duration: 1.4, ease: 'power3.inOut', onUpdate: () => pct.textContent = Math.round(n.v) + '%' })
    .to(dot, { scale: 140, duration: 0.7, ease: 'expo.in' })          // dot floods the screen…
    .to(L, { opacity: 0, duration: 0.3, onComplete: () => { clearInterval(swap); L.remove(); } })
    .then();
}
```
Optional finale: a `display:grid` of 36 outlined circles (`border:1px solid var(--line-strong)`)
that fill with `--ink` in a random stagger (`stagger: { each: .015, from: 'random' }`) behind
the headline.

## 3. Preloader C: Window boot

For product/app sites (Berd): an empty app window scales up from 60% in the middle of the paper,
the dot grid fades in, then one line of copy types in, then the real UI populates.

```js
function windowBoot(win /* .window element */) {
  if (REDUCE) return Promise.resolve();
  return gsap.timeline()
    .from(win, { scale: 0.6, opacity: 0, duration: 1, ease: 'expo.out' })
    .from(win.querySelector('.window__lights'), { opacity: 0, x: -6, duration: 0.4 }, '-=0.4')
    .from(win.querySelectorAll('[data-boot]'), { opacity: 0, y: 12, stagger: 0.05, duration: 0.6 }, '-=0.2')
    .then();
}
```

## 4. Rotating word with underscore caret

`We grow _brands` → deletes → `_people` → `_community` (milk). Use in hero headlines.

```html
<h1 class="hero-title">We grow <span class="rotator" data-words="brands,people,community" aria-hidden="true">brands</span>
  <span class="sr-only">brands, people and community</span></h1>
```
```css
.rotator::before { content: "_"; animation: blink 1s steps(1) infinite; }
@keyframes blink { 50% { opacity: 0; } }
.sr-only { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; }
```
```js
document.querySelectorAll('.rotator').forEach(el => {
  if (REDUCE) return;
  const words = el.dataset.words.split(','); let w = 0;
  const type = (txt, i = 0) => i <= txt.length
    ? setTimeout(() => { el.textContent = txt.slice(0, i); type(txt, i + 1); }, 55) : setTimeout(erase, 1800);
  const erase = () => el.textContent.length
    ? setTimeout(() => { el.textContent = el.textContent.slice(0, -1); erase(); }, 30)
    : type(words[w = (w + 1) % words.length]);
  setTimeout(erase, 2000);
});
```

## 5. Text scramble hover (signature)

On hover, the label dissolves into random letters and **block glyphs** (`▀▁▂▃█░▒▓◧◨`), then
resolves left-to-right into the real text in ~350 ms (qando). Use it on nav links, list rows,
buttons with mono/micro text, and the cursor-follower label. Never on body copy.

```html
<a href="/work" data-scramble>Selected work</a>
```
```js
const GLYPHS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789▀▁▂▃▄▅▆▇█▉▊▋▌▍▎▏▐░▒▓■□▢▣▤▥▦▧▨▩◧◨◩◪';
function scramble(el, text = el.dataset.text, duration = 350) {
  if (REDUCE) { el.textContent = text; return; }
  cancelAnimationFrame(el._raf);
  const start = performance.now();
  const frame = now => {
    const p = Math.min(1, (now - start) / duration), reveal = Math.floor(p * text.length);
    el.textContent = [...text].map((c, i) => c === ' ' || i < reveal ? c : GLYPHS[(Math.random() * GLYPHS.length) | 0]).join('');
    if (p < 1) el._raf = requestAnimationFrame(frame);
  };
  el._raf = requestAnimationFrame(frame);
}
document.querySelectorAll('[data-scramble]').forEach(el => {
  el.dataset.text = el.textContent.trim();
  el.setAttribute('aria-label', el.dataset.text);
  el.style.display = 'inline-block';
  el.style.minWidth = el.getBoundingClientRect().width + 'px';  // no layout jitter
  el.addEventListener('mouseenter', () => scramble(el));
  el.addEventListener('focus', () => scramble(el));
});
```
Tip: monospace text scrambles cleanest. On proportional text the `minWidth` lock prevents
shifting; set `white-space: nowrap` too.

## 6. Line / word reveal on scroll

Headlines slide up from a mask, word by word; paragraphs fade+rise. One function for both.

```css
.w-mask { display: inline-block; overflow: hidden; vertical-align: top; padding-bottom: 0.08em; margin-bottom: -0.08em; }
.w { display: inline-block; will-change: transform; }
```
```js
function splitWords(el) {
  el.setAttribute('aria-label', el.textContent.trim());
  el.innerHTML = el.textContent.trim().split(/\s+/)
    .map(w => `<span class="w-mask" aria-hidden="true"><span class="w">${w}</span></span>`).join(' ');
  return el.querySelectorAll('.w');
}
document.querySelectorAll('[data-reveal="words"]').forEach(el => {
  const words = splitWords(el);
  if (REDUCE) return;
  gsap.from(words, { yPercent: 110, duration: 1, stagger: 0.04,
    scrollTrigger: { trigger: el, start: 'top 85%' } });
});
document.querySelectorAll('[data-reveal="fade"]').forEach(el => {
  if (REDUCE) return;
  gsap.from(el, { opacity: 0, y: 24, duration: 0.9, scrollTrigger: { trigger: el, start: 'top 88%' } });
});
```
Use only on text with no inline markup (or adapt). For mixed-color headlines
(`It's <span class=muted>a whole new</span> level`) split each span separately.
Scroll-scrubbed variant (pxpush/orgnzm): set words to `opacity: .15` and scrub to 1 with
`scrollTrigger: { scrub: true, start: 'top 80%', end: 'bottom 40%' }`.

## 7. Cursor follower label

```html
<div class="cursor" aria-hidden="true"></div>
<a href="/case" data-cursor="View">…</a>   <div data-cursor="Drag">…</div>
```
```js
if (FINE && !REDUCE) {
  const c = document.querySelector('.cursor');
  const x = gsap.quickTo(c, 'x', { duration: 0.35, ease: 'power3' });
  const y = gsap.quickTo(c, 'y', { duration: 0.35, ease: 'power3' });
  addEventListener('pointermove', e => { x(e.clientX); y(e.clientY); });
  document.querySelectorAll('[data-cursor]').forEach(el => {
    el.addEventListener('pointerenter', () => { c.dataset.label = el.dataset.cursor; });
    el.addEventListener('pointerleave', () => { delete c.dataset.label; });
  });
} else document.querySelector('.cursor')?.remove();
```
Never hide the system cursor; the follower sits beside it.

## 8. 3D buddies: iridescent toys with googly eyes

The landing-page signature (TSG crystals, Berd clay toys, pxpush chrome): a handful of glossy,
iridescent primitives (crystal, rounded cube, blob, donut, pill), **each with two cartoon eyes
that follow the cursor**. They tumble in from above on load, then bob gently. Built from
primitives, no model files, so it is always original and loads instantly.

```html
<div class="buddies" data-buddies aria-hidden="true"></div>
<script type="module">
import * as THREE from 'three';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';
import { RoundedBoxGeometry } from 'three/addons/geometries/RoundedBoxGeometry.js';

const REDUCE = matchMedia('(prefers-reduced-motion: reduce)').matches;
const host = document.querySelector('[data-buddies]');
const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.toneMapping = THREE.ACESFilmicToneMapping;
host.appendChild(renderer.domElement);
const scene = new THREE.Scene();
scene.environment = new THREE.PMREMGenerator(renderer).fromScene(new RoomEnvironment(), 0.04).texture;
const camera = new THREE.PerspectiveCamera(32, 1, 0.1, 100); camera.position.set(0, 0, 14);
scene.add(new THREE.DirectionalLight(0xffffff, 1.2).translateX(3).translateY(5).translateZ(6));

// Colors: use token values. Read them from CSS so a palette change flows into 3D:
//   const tok = n => new THREE.Color(getComputedStyle(document.documentElement).getPropertyValue(n).trim());
//   mat(tok('--lcd'))   (hex literals below mirror the tokens; lighter tints are fine for materials)
const mat = (color, extra = {}) => new THREE.MeshPhysicalMaterial({ color, roughness: 0.18, metalness: 0,
  clearcoat: 1, clearcoatRoughness: 0.08, iridescence: 1, iridescenceIOR: 1.35,
  iridescenceThicknessRange: [120, 900], ...extra });
const eyeWhite = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.3 });
const eyeBlack = new THREE.MeshStandardMaterial({ color: 0x0b0b0a, roughness: 0.2 });

function eyes(r) {                      // r = how far the face surface is from center
  const g = new THREE.Group(), list = [];
  for (const sx of [-1, 1]) {
    const eye = new THREE.Group();
    eye.add(new THREE.Mesh(new THREE.SphereGeometry(0.22, 24, 16), eyeWhite));
    const pupil = new THREE.Mesh(new THREE.SphereGeometry(0.11, 16, 12), eyeBlack);
    pupil.position.z = 0.15; eye.add(pupil);
    eye.position.set(sx * 0.27, 0.15, r); g.add(eye); list.push(eye);
  }
  return { g, list };
}
const SPECS = [   // geometry, material, face distance, desktop rest position, phone rest position
  [new THREE.IcosahedronGeometry(1.25, 0), mat(0x9fd0ff, { transmission: 0.6, thickness: 1.2, flatShading: true }), 1.05, [-4.2,  0.8, 0], [-1.6, 3.4, 0]],
  [new RoundedBoxGeometry(1.9, 1.9, 1.9, 6, 0.45), mat(0xc8f560), 0.98, [-1.4, -1.0, 0.6], [1.6, 2.6, -0.5]],
  [new THREE.SphereGeometry(1.15, 48, 32), mat(0xf3c4ec), 1.12, [1.4, 0.9, -0.4], [-1.2, 0.9, -1]],
  [new THREE.TorusGeometry(0.8, 0.42, 32, 64), mat(0x2433ff), 0.42, [4.1, -0.6, 0]],
  [new THREE.CapsuleGeometry(0.55, 1.1, 8, 24), mat(0xffe600), 0.58, [0.2, 2.3, -1.2]],
];
const MOBILE = innerWidth < 700;                     // phones: 3 buddies, stacked above the headline
const buddies = SPECS.slice(0, MOBILE ? 3 : SPECS.length).map(([geo, m, r, desk, phone], i) => {
  const pos = MOBILE && phone ? phone : desk;
  const body = new THREE.Group(); body.add(new THREE.Mesh(geo, m));
  const e = eyes(r); body.add(e.g);
  body.userData = { rest: new THREE.Vector3(...pos), eyes: e.list, phase: i * 1.3 };
  body.position.set(pos[0], REDUCE ? pos[1] : pos[1] + 9 + i, pos[2]);
  scene.add(body); return body;
});

// tumble in, after the preloader has finished, so people actually see it
function drop() {
  buddies.forEach((b, i) => {
    if (REDUCE || !window.gsap) { b.position.copy(b.userData.rest); return; }
    gsap.to(b.position, { y: b.userData.rest.y, duration: 1.6, ease: 'bounce.out', delay: 0.15 * i });
    gsap.from(b.rotation, { x: Math.PI * 2, z: -Math.PI, duration: 1.8, ease: 'expo.out', delay: 0.15 * i });
  });
}
// the classic script sets window.__booted = true and dispatches 'booted' when the preloader ends
if (window.__booted || !document.querySelector('[data-loader]')) drop();
else addEventListener('booted', drop, { once: true });

// eyes follow the pointer
const target = new THREE.Vector3(0, 0, 6), ndc = new THREE.Vector2();
addEventListener('pointermove', e => {
  ndc.set((e.clientX / innerWidth) * 2 - 1, -(e.clientY / innerHeight) * 2 + 1);
  target.set(ndc.x * 9, ndc.y * 5, 6);
});

function resize() {
  const { width, height } = host.getBoundingClientRect();
  renderer.setSize(width, height, false); camera.aspect = width / height;
  camera.position.z = width < 700 ? 22 : 14; camera.updateProjectionMatrix();
}
new ResizeObserver(resize).observe(host); resize();

let visible = true;
new IntersectionObserver(([e]) => visible = e.isIntersecting).observe(host);
const clock = new THREE.Clock();
renderer.setAnimationLoop(() => {
  if (!visible) return;
  const t = clock.getElapsedTime();
  for (const b of buddies) {
    if (!REDUCE) {
      b.position.y += Math.sin(t * 1.2 + b.userData.phase) * 0.003;
      b.rotation.y += (ndc.x * 0.5 - b.rotation.y) * 0.04;
      b.rotation.x += (-ndc.y * 0.25 - b.rotation.x) * 0.04;
    }
    for (const eye of b.userData.eyes) eye.lookAt(target);
  }
  renderer.render(scene, camera);
});
</script>
```
```css
.buddies { position: absolute; inset: 0; z-index: 0; pointer-events: none; }
.buddies canvas { width: 100% !important; height: 100% !important; }
```
Variations: swap palette to all-chrome (`metalness: 1, roughness: .12, iridescence: .3`) for a
pxpush look; use 1 big buddy that follows scroll position (orgnzm rock) via
`ScrollTrigger` scrub on `position.y`; add `sunglasses` (two black rounded boxes) to one buddy.
On mobile keep max 3 buddies. Never put text on top of the canvas without a solid/ glass backing.

## 9. Physics drop: draggable pills & stickers

Labels/tags/stickers fall into a box when it scrolls into view and can be flung around
(yuanzuo, orgnzm, monolog all use Matter.js). DOM elements are synced to bodies so text stays
crisp and styleable.

```html
<div class="drop-zone" data-drop>
  <span class="drop tag-pill">Branding</span><span class="drop tag-pill tag-pill--lcd">Web</span>
  <span class="drop sticker-sm">NEW!</span>   <!-- …6–14 items -->
</div>
```
```css
.drop-zone { position: relative; height: 420px; overflow: hidden; border-radius: var(--r-3); background: var(--surface); touch-action: pan-y; }
.drop { position: absolute; left: 0; top: 0; user-select: none; cursor: grab; will-change: transform; }
.tag-pill { padding: 12px 22px; border-radius: var(--r-pill); border: 1.5px solid var(--ink); background: var(--surface-2);
  font: 500 clamp(16px, 2vw, 28px)/1 var(--font-display); letter-spacing: var(--track-tight); }
.tag-pill--lcd { background: var(--lcd); color: var(--on-accent); } .tag-pill--sticky { background: var(--sticky); color: var(--on-accent); } .tag-pill--ink { background: var(--ink); color: var(--paper); }
.sticker-sm { width: 84px; height: 84px; border-radius: 50%; display: grid; place-items: center; background: var(--sticker);
  border: 1.5px solid var(--ink); font: 400 12px/1 var(--font-pixel); color: var(--on-accent); }
```
```js
function physicsDrop(zone) {
  const { Engine, Runner, Bodies, Composite, Mouse, MouseConstraint } = Matter;
  const W = zone.clientWidth, H = zone.clientHeight, els = [...zone.querySelectorAll('.drop')];
  const engine = Engine.create(); engine.gravity.y = 1.1;
  const wall = { isStatic: true };
  Composite.add(engine.world, [
    Bodies.rectangle(W / 2, H + 50, W * 2, 100, wall),
    Bodies.rectangle(-50, H / 2, 100, H * 4, wall), Bodies.rectangle(W + 50, H / 2, 100, H * 4, wall)]);
  const items = els.map((el, i) => {
    const w = el.offsetWidth, h = el.offsetHeight, round = Math.abs(w - h) < 2;
    const opts = { restitution: 0.3, friction: 0.25, angle: (Math.random() - 0.5) * 0.8 };
    const b = round ? Bodies.circle(Math.random() * (W - w) + w / 2, -h - i * 70, w / 2, opts)
                    : Bodies.rectangle(Math.random() * (W - w) + w / 2, -h - i * 70, w, h, { ...opts, chamfer: { radius: h / 2 - 1 } });
    Composite.add(engine.world, b); return { el, b, w, h };
  });
  if (FINE) {                                       // drag on desktop; touch keeps page scroll
    const mouse = Mouse.create(zone);
    mouse.element.removeEventListener('wheel', mouse.mousewheel);
    mouse.element.removeEventListener('DOMMouseScroll', mouse.mousewheel);
    Composite.add(engine.world, MouseConstraint.create(engine, { mouse, constraint: { stiffness: 0.2, render: { visible: false } } }));
  }
  const runner = Runner.create(); Runner.run(runner, engine);
  (function sync() {
    for (const { el, b, w, h } of items)
      el.style.transform = `translate(${b.position.x - w / 2}px, ${b.position.y - h / 2}px) rotate(${b.angle}rad)`;
    requestAnimationFrame(sync);
  })();
}
document.querySelectorAll('[data-drop]').forEach(zone => {
  if (REDUCE) {                                     // static, tidy pile instead
    zone.classList.add('is-static'); return;
  }
  ScrollTrigger.create({ trigger: zone, start: 'top 75%', once: true, onEnter: () => physicsDrop(zone) });
});
```
```css
.drop-zone.is-static { display: flex; flex-wrap: wrap; align-content: flex-end; gap: 8px; padding: 16px; }
.drop-zone.is-static .drop { position: static; }
```

## 10. Soap bubbles

Glossy bubbles drifting over a sky hero (the Dribbble "sent." feel). Pure CSS.

```html
<i class="bubble" style="--size:140px; left:8%;  top:40%; --dur:13s"></i>
<i class="bubble bubble--blue" style="--size:96px; right:12%; top:18%; --dur:17s"></i>
```
```css
.bubble { position: absolute; width: var(--size, 120px); aspect-ratio: 1; border-radius: 50%; pointer-events: none;
  background:
    radial-gradient(circle at 30% 26%, rgba(255,255,255,.95) 0 5%, transparent 6.5%),
    radial-gradient(circle at 68% 74%, rgba(255,255,255,.45) 0 6%, transparent 22%),
    radial-gradient(circle, rgba(190,220,255,.08) 52%, rgba(140,190,255,.45) 68%, rgba(255,190,240,.35) 84%, rgba(255,255,255,.75) 100%);
  box-shadow: inset 0 0 18px rgba(255,255,255,.55);
  animation: drift var(--dur, 14s) ease-in-out infinite alternate; }
.bubble--blue { background:
    radial-gradient(circle at 30% 26%, rgba(255,255,255,.95) 0 6%, transparent 8%),
    radial-gradient(circle at 50% 60%, #8EC5FF 0%, #3D7BFF 70%, #1F4FE0 100%); box-shadow: inset -8px -10px 20px rgba(10,30,120,.35); }
@keyframes drift { 0% { transform: translate(0,0) } 50% { transform: translate(14px,-22px) } 100% { transform: translate(-10px,-8px) } }
```

## 11. LCD typewriter

```html
<div class="lcd" data-type='["how did you end up here?","the sky looks good today","lol wait the ball broke"]'>
  <span data-out></span><span class="caret"></span></div>
```
```js
document.querySelectorAll('[data-type]').forEach(box => {
  const lines = JSON.parse(box.dataset.type), out = box.querySelector('[data-out]');
  if (REDUCE) { out.textContent = lines[0]; return; }
  let l = 0;
  const type = (s, i = 0) => i <= s.length
    ? setTimeout(() => { out.textContent = s.slice(0, i); type(s, i + 1); }, 60 + Math.random() * 60)
    : setTimeout(() => type(lines[l = (l + 1) % lines.length]), 2200);
  type(lines[0]);
});
```

## 12. Small delights

- **Logo flip** (orgnzm): a flat logo shape rotates on Y every few seconds.
  `.logo-flip { animation: flip 4s var(--ease-inout) infinite; } @keyframes flip { 0%,70% { transform: rotateY(0) } 100% { transform: rotateY(360deg) } }`
- **Count-up numbers** on enter: `gsap.from(el, { textContent: 0, snap: { textContent: 1 }, duration: 1.4, ease: 'power2.out', scrollTrigger: { trigger: el, start: 'top 85%' } })`.
- **Marquee speeds up with scroll**: `ScrollTrigger.create({ onUpdate: s => track.style.animationDuration = Math.max(6, 22 - Math.abs(s.getVelocity()) / 150) + 's' })`.
- **Square-blink icons** (qando): a 2×2 grid of squares inside a button; on hover animate each
  square's opacity with `animation-delay: 0s, .125s, .25s, .375s`.
- **Sticker wobble** on hover: `transition: transform var(--dur-ui) var(--ease-spring)` + rotate.
- **Window open**: modals and new panels `from({ scale: .96, opacity: 0, duration: .32 })`.

## 13. Budget & rules

- One preloader per site, max 2.5 s, skippable, once per session; never on app screens.
- At most **one** WebGL canvas per page; pause it off-screen; DPR ≤ 2.
- Hovers resolve in ≤ 400 ms; reveals ≤ 1 s; nothing loops faster than 2 s except carets.
- Everything respects `REDUCE`: no preloader, no smooth scroll, no tumbling, static piles,
  final text shown immediately.
- Motion must never hide content from no-JS users: set initial hidden states in JS (`gsap.from`),
  not in CSS.
- Dashboards/app UI: only §3 window boot (first load), §5 scramble on nav, §12 count-ups,
  window-open transitions, toasts. No Lenis, no 3D, no physics.
