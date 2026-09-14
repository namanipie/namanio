---
name: namanipie-personal-site
description: Personal website / little corner of the internet — dark glassmorphism editorial site with Instrument Serif display, scroll signatures, magnetic buttons, IO reveals.
metadata:
  type: project
  platform: web
  mode: Experience / Persuade
  created: 2026-09-15
---

# nemanipie — personal site

**Product truth (not redesign intent):**
- Single-page personal site (`index.html`) + 404 (`404.html`).
- Hosted at `https://namanipie.github.io/namanio/`
- Built while learning / breaking / fixing; no commercial conversion goal — expression and craft.
- Dark-first (`color-scheme: dark`, `--ground: #0b0a0e`), glassmorphism (`glass-bg`, `glass-border`), editorial typography (`Instrument Serif` + `Inter` + `JetBrains Mono`).
- Signature scroll (name reveal on scroll), cursor states (magnetic buttons, image tilt), reduced particle field, scroll progress, glass nav with IO reveals.
- Favicon is custom SVG (`favicon.svg`). Title currently "hi lol".

**Incumbent visual authority (preserve for refinement):**
- `index.html` is the full implementation (glass nav, hero, sections, signature, footer).
- Tokens in `:root`, grain overlay, staggered CSS reveals, GSAP-driven scroll animations.
- No external framework — vanilla HTML/CSS/JS with GSAP.

**Constraints / non-negotiables from code:**
- `darkreader-lock` meta (protects dark theme).
- `overflow-x: hidden`, responsive `clamp()` gutters.
- `font-weight: 300` body, `font-family` stack locked.

**What this init does not decide (refinement / new-work keeps open):**
- Title change ("hi lol" vs. real name).
- Signature text / image content.
- Whether to extend with pages or stay single-page.

**Co-Authored-By:** Claude Code <noreply@anthropic.com>
