# Karthikeya · Portfolio

A premium, dark-mode portfolio for **Karthikeya — Junior Software Engineer (Digitalization & Automation)**, built with **React + Vite**, **Tailwind CSS**, and **GSAP** (with `ScrollTrigger`) for scroll-based reveal, parallax, and interactive motion.

Single-page scroll layout, fully responsive, accessible, and set up for one-push deployment to **GitHub Pages** via GitHub Actions.

---

## Tech stack

- **React 19** + **Vite** (fast dev / lean build)
- **Tailwind CSS** (utility-first, custom dark palette)
- **GSAP** + **ScrollTrigger** (all scroll animations; a lightweight custom word-splitter is included so no paid `SplitText` plugin is required)
- **react-icons** for tech-stack glyphs
- **GitHub Actions** → GitHub Pages deploy

## Project structure

```
karthikeya-portfolio/
├─ .github/workflows/deploy.yml
├─ public/
│  ├─ resume.pdf
│  └─ favicon.svg
├─ src/
│  ├─ App.jsx
│  ├─ main.jsx
│  ├─ index.css
│  ├─ components/
│  │  ├─ Navbar.jsx
│  │  ├─ Hero.jsx
│  │  ├─ About.jsx
│  │  ├─ Projects.jsx
│  │  ├─ Resume.jsx
│  │  ├─ Contact.jsx
│  │  └─ Footer.jsx
│  ├─ hooks/
│  │  ├─ useGsap.js
│  │  ├─ useScrollReveal.js
│  │  ├─ useSplitReveal.js
│  │  ├─ useParallax.js
│  │  ├─ useMagnetic.js
│  │  ├─ useTilt.js
│  │  └─ useCursorSpotlight.js
│  └─ data/
│     ├─ profile.js
│     ├─ projects.js
│     └─ skills.js
├─ tailwind.config.js
├─ vite.config.js
└─ package.json
```

## Getting started

```bash
npm install
npm run dev
npm run build
npm run preview
```

Open http://localhost:5173 for the dev server.

## Customising content

All copy and links live in [`src/data/`](src/data):

- **`profile.js`** — name, role, email, LinkedIn, GitHub, resume filename.
- **`projects.js`** — the three cards (RDPMS, BCS, BI Dashboard). Add `github` / `live` URLs when available.
- **`skills.js`** — tech-stack icons (react-icons).

### Replace the resume

Drop your real PDF at `public/resume.pdf`. The Hero, Resume, and Footer link to it via `${import.meta.env.BASE_URL}resume.pdf`, so both local dev and GitHub Pages URLs work automatically.

### Contact form

The form defaults to a `mailto:` handoff so it works with no backend. To use a real endpoint, swap the `handleSubmit` body in [`src/components/Contact.jsx`](src/components/Contact.jsx) for a `fetch` call to Formspree, EmailJS, Resend, or your own API.

## Sections

- **Hero** — GSAP word-by-word name reveal, staggered subtitle/tagline/CTAs, ambient floating orbs, animated scroll indicator, cursor spotlight, magnetic CTAs.
- **About** — bio + `~2.9 yrs` context, animated tech-stack grid.
- **Projects** — cards for RDPMS · BCS · BI Dashboard, each with a scroll-triggered rise, parallax halo, 3D tilt on hover, description, highlights, tags, and optional GitHub/live links.
- **Resume** — `Download Resume` button (serves `/public/resume.pdf`) plus an inline `<object>` PDF preview modal.
- **Contact** — direct email / LinkedIn / GitHub cards, plus a form that falls back to `mailto:`.

## Animations

All GSAP logic is centralised in `src/hooks/`. Highlights:

- `useScrollReveal({ selector, stagger, y, start })` — attach the ref to a section; anything matching `selector` inside animates in on scroll.
- `useSplitReveal({ trigger: 'mount' | 'scroll' })` — split-text-style reveal for a heading.
- `useParallax({ distance })` — scrub-based Y translation.
- `useMagnetic({ strength })` — CTA follows the pointer with GSAP's `quickTo`.
- `useTilt({ max })` — smooth 3D tilt on mouse-move for cards.
- `useCursorSpotlight()` — soft radial glow that tracks the cursor inside a section.

All hooks respect `prefers-reduced-motion` — motion is disabled and elements resolve to their final state.

## Deployment (GitHub Pages via GitHub Actions)

This repo ships with [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml). It:

1. Installs deps and runs `npm run build` on every push to `main`.
2. Passes `VITE_BASE_PATH=/${repo-name}/` so all built asset URLs resolve correctly under `https://<user>.github.io/<repo>/`.
3. Copies `index.html` → `404.html` so deep links (hash routes) don't break.
4. Uploads `dist/` and publishes it to GitHub Pages.

### One-time repo setup

1. Push this repo to GitHub.
2. **Settings → Pages → Build and deployment → Source:** _GitHub Actions_.
3. Push to `main`. The workflow runs automatically; the site publishes at `https://<user>.github.io/<repo>/`.

### User / org site (`<user>.github.io` repo)

If you deploy to `<user>.github.io` (no sub-path), remove the `VITE_BASE_PATH` env from the workflow (or set it to `/`) so assets resolve at the root.

### Alternative: `gh-pages` package

```bash
npm run deploy
```

You'll want to add a `homepage` field to `package.json` (e.g. `"homepage": "https://<user>.github.io/<repo>"`) and set `base` in `vite.config.js` accordingly.

## Accessibility

- Semantic landmarks (`<header>`, `<main>`, `<footer>`, `<section aria-labelledby=...>`).
- Skip link, focus-visible outlines, keyboard-navigable nav + menu.
- `aria-label` on split-text heading for screen readers.
- All decorative graphics marked `aria-hidden`.
- Motion respects `prefers-reduced-motion`.

## Performance

- Vite production build with `target: es2020` and gzip-ready output.
- `react-icons` tree-shakes to only imported glyphs.
- Fonts are preconnected and loaded with `display=swap`.
- No large image assets — decorative visuals are CSS gradients.

## License

MIT — feel free to reuse the structure and animation hooks for your own portfolio.
