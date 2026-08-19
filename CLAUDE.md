# Crawford Living — Website

**This repo is the website itself.** It is what visitors see. Everything else is context.

## ⚠️ Read before designing anything

Three repos, all siblings under `~/Crawford Living/`. **Read all three before making a design or copy decision** — the reason this project has repeatedly duplicated work is that sessions opened one and never learned the others existed.

| Repo | What it holds | Read it for |
|---|---|---|
| **`crawford-living-website`** (here) | The site. HTML/CSS, no build step | What actually exists |
| `../crawford-living-brand` | The brief — positioning, strategy, open decisions, `DESIGN.md`, motion research | **Why** anything is the way it is |
| `../Crawford-Living` | Operations — brand kit, attorney letters, probate data, compliance, business context | Palette, logo, eXp facts, constraints |

Design and build work happens **here**. The brand repo holds decisions and studies, not shipping pages. If a draft appears there, it is reference — do not treat it as a second site.

## Hosting — and the trap

**GitHub Pages serves `main`, path `/`, at https://crawfordliving.com** (CNAME in repo root).

**Work has repeatedly been committed to a branch and never merged**, which means the live domain and the built site drift apart and nobody can tell which page is under discussion. If you are asked "why does the site look old", check `git log main..HEAD` before concluding anything.

**Never push to `main` without Mike saying so explicitly.** 18 printed attorney letters point at this domain.

## Pages

`index.html` · `about.html` · `probate.html` · `attorneys.html` · `search.html`, styles in `assets/`.

## Brand

Canonical palette and type live in `../Crawford-Living/crawford-living-brand-kit.md`; the applied system is `../crawford-living-brand/DESIGN.md`.

- **Primary Navy `#0E2A57`** · Secondary Blue `#19469C` · Gold `#E7C870` (emphasis only, sparingly) · gold text `#8A6D2F`
- Ivory grounds — `#EADCBC` sunk · `#F2E9D5` page · `#FCF8EC` raised · `#DACBA9` rules. **No white anywhere.**
- Type in use: **Archivo** (display and text) with **Inter**. The kit still names Lora / Source Sans Pro; the site has moved off them deliberately — see `open-decisions.md` item 6.

## Positioning rules that bind the copy

- **Crawford Living is an umbrella brand.** It is not probate-only and it is not a personal brand. The homepage sells the practice, not a biography.
- **Probate must be visible on the homepage** — the attorney letters point at the bare domain — **but must never lead it.** "Some houses are sold. Others have to be untangled first." belongs on `probate.html`, not `index.html`.
- **Never imply staff that do not exist**, and never read as a one-man show either. The lever is *standard*, not headcount — "by design, not by default". See `copy-inventory.md`.
- **The construction background is coordination, not trades.** Never claim hands-on building or a homes-built figure: it is inaccurate, it invites structural questions Mike is not licensed to answer, and it risks NAR Article 12. It belongs on the New Construction portal only.
- **No urgency or scarcity tactics anywhere.** Tone is the product.
- **Advertising must carry the brokerage name** while Mike is under eXp Realty LLC.

## Motion

Rules and measured values are in `../crawford-living-brand/motion-notes.md` and the Motion section of `DESIGN.md`. The two that matter most:

1. **Navigation labels stay visible whenever the header is showing.** It may hide on scroll-down and return on scroll-up, but never reduce to a bare hamburger.
2. **Never capture the scroll.** Animate anything; do not wheel-jack, snap-hold, or block advancement.

## Conventions

- Never use GitHub's web editor for HTML — CodeMirror auto-closes tags and corrupts markup.
- Update this file when a structural fact changes (hosting, branch state, repo roles).
