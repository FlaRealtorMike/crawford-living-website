# Crawford Living — Website

**This repo is the website itself.** It is what visitors see. Everything else is context.

Plain static HTML. No build step, no framework, no dependencies.

## ⚠️ Read all three repos before designing or writing anything

Siblings under `~/Crawford Living/`. This project has repeatedly duplicated work because a
session opened one repo and never learned the other two existed.

| Repo | What it holds | Read it for |
|---|---|---|
| **`crawford-living-website`** (here) | The site. HTML/CSS at the repo root | What actually exists |
| `../crawford-living-brand` | The brief — positioning, `open-decisions.md`, `DESIGN.md`, motion research | **Why** anything is the way it is |
| `../Crawford-Living` | Operations — brand kit, attorney letters, probate data, compliance | Palette, logo, eXp facts, constraints |

Build work happens **here**. The brand repo holds decisions and studies, not shipping pages.
A file in its `drafts/` is reference — never a second website. If a draft disagrees with this
repo, this repo wins.

## ⚠️ Branch state — check this first, every time

**As of 2026-08-20 there is a full redesign sitting unmerged on
`claude/crawford-living-website-status-unbl05`** — 5 commits, ~2,000 lines: a rebuilt
umbrella homepage, drawn SVG graphics, `search.html`, and `assets/site-v2.css`.

**`main` does not have any of it.** The live site is the earlier, plainer version.

Consequences, all of which have already bitten:

- If asked "why does the site look old", run `git log main..origin/claude/crawford-living-website-status-unbl05` **before** concluding anything or rebuilding.
- Do not redesign the homepage from scratch. It has been done. It is on that branch.
- The branch carries its own `CLAUDE.md`, written before this one. Where they conflict, **this
  file describes `main`** — the branch file describes the branch.

Merging that branch is Mike's call, not a session's. It changes the live domain.

## Hosting

**GitHub Pages serves `main`, path `/`, at https://crawfordliving.com.**

- `CNAME` in the repo root binds the domain. **Do not delete or rename it.** GitHub rewrites
  it if the custom domain is changed in the Pages settings UI.
- DNS is at **GoDaddy** — apex needs GitHub's four A records; `www` CNAMEs to
  `flarealtormike.github.io`.
- **Never touch the MX records.** They point at Google Workspace and carry
  `mdc@crawfordliving.com`. Breaking them breaks email silently.

**Never push to `main` without Mike saying so explicitly.** 18 printed attorney letters point
at this domain. A push is a publication.

## Pages on `main` today

```
index.html       Home — who Mike is, the three paths, general resale/new construction
probate.html     For personal representatives. Gentle, plain, no calendar, no urgency
attorneys.html   For probate attorneys. Short and direct. noindex, nofollow
about.html       Background — 20 years, the construction company, RENE
assets/site.css  Shared stylesheet
```

Nav shows **Home / Probate / About** only. `attorneys.html` is deliberately out of the nav and
out of search — it is reached from the printed letter and from a home page card.

Preview with working navigation:

```
python3 -m http.server 8765
```

## Brand

Canonical values: `../Crawford-Living/crawford-living-brand-kit.md`.
Applied system: `../crawford-living-brand/DESIGN.md`.

**Colour — in use on `main` and settled:**

- Primary Navy `#0E2A57` · Secondary Blue `#19469C` · Gold `#E7C870` (emphasis only,
  at most once per screen) · gold text `#8A6D2F`
- Ivory grounds — `#EADCBC` sunk · `#F2E9D5` page · `#FCF8EC` raised · `#DACBA9` rules
- **No white anywhere.**

**Type — not settled. Know which side you are on:**

- `main` loads **Lora + Source Sans 3**.
- `DESIGN.md` and the unmerged branch specify **Archivo + Inter**, arguing the Lora pairing is
  a large part of the "too old" feel.
- The brand kit still names Lora / Source Sans Pro and has not been updated.

This is `open-decisions.md` **item 6** and it is open. Do not silently switch a page's fonts
in either direction — it makes pages disagree with each other. Raise it instead.

The eXp logo in `assets/` is the brand-kit copy, already recoloured to Secondary Blue rather
than eXp's stock red. Keep it that way.

## Positioning rules that bind the copy

- **Crawford Living is an umbrella brand.** Not probate-only, not a personal brand. The
  homepage sells the practice, not a biography. No single niche defines it.
- **Probate must be visible on the homepage but must never lead it.** The attorney letters
  point at the bare domain, so an attorney who types it in must find probate — but a seller
  landing there must not think probate is all this is. "Some houses are sold. Others have to
  be untangled first." belongs on `probate.html`, not `index.html`.
- **The construction background is coordination, not trades.** Never claim hands-on building
  and never publish a homes-built figure. It is inaccurate, it invites structural questions
  Mike is not licensed to answer, and it risks NAR Article 12. New Construction portal only.
- **Boutique — neither one-man-show nor corporate.** Never imply staff who do not exist; never
  read as a solo operator either. The lever is *standard*, not headcount: "by design, not by
  default." See `../crawford-living-brand/copy-inventory.md` for approved and retired language.
- **No urgency, scarcity, testimonials, counts, or ratings.** Tone is the product, and that
  category of claim is exactly what made the page this site replaced a compliance exposure.

## Required disclosures — on every page, including new ones

The footer carries both and must continue to:

- Florida Broker license **BK3074190**
- **eXp Realty LLC**, 10752 Deerwood Park Blvd., Suite 100, Jacksonville, FL 32256

All advertising must carry the brokerage name while Mike is a Broker-Associate under eXp.
Nothing may be branded "Crawford Living Realty, LLC" until that entity is formed and
registered with DBPR. **Send material changes to eXp compliance before they go live** — the
page this site replaced was never reviewed, which was half the problem.

## Deliberate omissions — restraint is the point

- **No lead form, no email capture, no calendar embed.** The letters ask for a conversation,
  not a funnel. A form here would contradict them.
- **No stock photography** on the pages that currently have none.

Adding any of these should be a considered decision, not a default.

**Imagery is Mike's call** (2026-08-19) — there is deliberately no sourcing rule. Raise the
credibility risk only when an image stands in for an actual property, a named community, or
people.

## Motion

Rules and measured values: `../crawford-living-brand/motion-notes.md` and the Motion section
of `DESIGN.md`. The two that matter most:

1. **Navigation labels stay visible whenever the header is showing.** It may hide on
   scroll-down and return on scroll-up, but never reduce to a bare hamburger.
2. **Never capture the scroll.** Animate anything; do not wheel-jack, snap-hold, or block
   advancement. Motion never costs the visitor their place.

## Before building a homepage section, check what it can point at

`open-decisions.md` items 1–5 block real work here. In particular: the brand line is
undecided (item 1), the hero buttons point at pages that do not exist (item 3), and
**Search Homes is not just a product question** — Stellar MLS IDX participation rules,
attribution requirements, and whether eXp must approve are unchecked (item 5). Do not select
an IDX provider before that.

## Conventions

- **Never use GitHub's web editor for HTML.** CodeMirror auto-closes tags and corrupts markup.
- Record decisions with reasoning and date, in the repo they belong to, **as they are made** —
  so a later session does not re-litigate a settled question or reintroduce retired copy.
- Update this file when a structural fact changes: hosting, branch state, page inventory,
  repo roles.
