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

## ⚠️ The site is currently split across two design systems

The 2026-08-19 redesign was merged into `main` on **2026-08-20**. It did not cover every page,
so the site now has a visible seam:

| Page | Stylesheet | Type |
|---|---|---|
| `index.html` | `assets/site-v2.css` | **Archivo + Inter** |
| `search.html` | `assets/site-v2.css` | **Archivo + Inter** |
| `about.html` | `assets/site.css` | Lora + Source Sans 3 |
| `probate.html` | `assets/site.css` | Lora + Source Sans 3 |
| `attorneys.html` | `assets/site.css` | Lora + Source Sans 3 |

**A visitor clicking Home → Probate crosses a font and style change.** This is the top
outstanding defect. Finishing it means porting the three remaining pages onto `site-v2.css`,
which is a real piece of work, not a find-and-replace.

Do not "fix" it by reverting the homepage. The homepage is the agreed direction.

## Branch discipline

Work has twice been committed to a branch and left unmerged while the live domain drifted.
Before concluding the site "looks old" or rebuilding anything:

```
git log main..origin/<branch>
git branch -a
```

`claude/crawford-living-website-status-unbl05` is **merged and spent**. Do not build on it.

## Hosting

**GitHub Pages serves `main`, path `/`, at https://crawfordliving.com.**

- `CNAME` in the repo root binds the domain. **Do not delete or rename it.** GitHub rewrites
  it if the custom domain is changed in the Pages settings UI.
- DNS is at **GoDaddy** — apex needs GitHub's four A records; `www` CNAMEs to
  `flarealtormike.github.io`.
- **Never touch the MX records.** They point at Google Workspace and carry
  `mdc@crawfordliving.com`. Breaking them breaks email silently.
- A push is not a live site. Pages rebuilds after the push — typically under a minute — and
  the CDN can serve the old page briefly after that. Check with
  `gh api repos/FlaRealtorMike/crawford-living-website/pages/builds/latest`.

**Never push to `main` without Mike saying so explicitly.** 18 printed attorney letters point
at this domain. A push is a publication.

## Pages

```
index.html       Home — the umbrella. Six paths: Buy, Sell, New Construction,
                 Probate & Estates, Communities, Search Homes
probate.html     For personal representatives. Gentle, plain, no calendar, no urgency
attorneys.html   For probate attorneys. Short and direct. noindex, nofollow
about.html       Background — 20 years, construction coordination, RENE
search.html      Honest placeholder. Says "not ready yet" rather than faking an IDX
```

`attorneys.html` stays **out of the nav and out of search** — it is reached from the printed
letter and from a home page card.

Preview with working navigation:

```
python3 -m http.server 8765
```

## Brand

Canonical values: `../Crawford-Living/crawford-living-brand-kit.md`.
Applied system: `../crawford-living-brand/DESIGN.md`.

**Colour — settled, and used site-wide:**

- Primary Navy `#0E2A57` · Secondary Blue `#19469C` · Gold `#E7C870` (emphasis only, at most
  once per screen) · gold text `#8A6D2F`
- Ivory grounds — `#EADCBC` sunk · `#F2E9D5` page · `#FCF8EC` raised · `#DACBA9` rules
- **No white anywhere.**

**Type — the site has moved to Archivo + Inter** (`DESIGN.md`), but the brand kit still names
Lora / Source Sans Pro and has not been updated. That is `open-decisions.md` **item 6**, still
open on paper even though the homepage has decided it in practice. **Fold Archivo + Inter into
the brand kit** or the two will keep disagreeing. Note the printed attorney letters are on
ivory cotton stock.

The eXp logo in `assets/` is the brand-kit copy, recoloured to Secondary Blue rather than
eXp's stock red. Keep it that way.

## Positioning rules that bind the copy

- **Crawford Living is an umbrella brand.** Not probate-only, not a personal brand. The
  homepage sells the practice, not a biography. No single niche defines it.
- **Probate must be visible on the homepage but must never lead it.** The attorney letters
  point at the bare domain, so an attorney who types it in must find probate — but a seller
  landing there must not think probate is all this is. It is panel `04` on the homepage;
  "Some houses are sold. Others have to be untangled first." belongs on `probate.html`.
- **The construction background is coordination, not trades.** Never claim hands-on building
  and **never publish a homes-built figure** — a "four hundred homes a year" line was live
  until 2026-08-20. It is inaccurate, invites structural questions Mike is not licensed to
  answer, and risks NAR Article 12. Always pair it with the disclaimer the deeper pages use:
  process knowledge, not structural expertise; anything technical goes to a licensed inspector
  or engineer.
- **Boutique — neither one-man-show nor corporate.** Never imply staff who do not exist; never
  read as a solo operator either. The lever is *standard*, not headcount: "takes on fewer
  transactions than it could, by design." Retired: "deliberately small", "one person by
  choice", "you work with me, not a team". See `../crawford-living-brand/copy-inventory.md`.
- **No urgency, scarcity, testimonials, counts, or ratings.** Tone is the product, and that
  category of claim is what made the page this site replaced a compliance exposure.

## Required disclosures — on every page, including new ones

- Florida Broker license **BK3074190**
- **eXp Realty LLC**, 10752 Deerwood Park Blvd., Suite 100, Jacksonville, FL 32256

All advertising must carry the brokerage name while Mike is a Broker-Associate under eXp.
Nothing may be branded "Crawford Living Realty, LLC" until that entity is formed and
registered with DBPR. **Send material changes to eXp compliance before they go live** — the
page this site replaced was never reviewed, which was half the problem. *The merged redesign
has not been reviewed by eXp.*

## Deliberate omissions — restraint is the point

- **No lead form, no email capture, no calendar embed.** The letters ask for a conversation,
  not a funnel. A form here would contradict them.
- **No testimonials, counts, ratings, or "spots left."**

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

## Known gaps

- **Two design systems** — see the top of this file.
- **Communities** is a homepage panel with no page and no photography behind it.
- **Search Homes** is an honest placeholder. Before selecting any IDX provider, check Stellar
  MLS participation rules, attribution requirements, and whether eXp must approve
  (`open-decisions.md` item 5).
- **The brand line** — "Real Estate… CONSIDERED" is what shipped, on the site and on the
  printed letters. `open-decisions.md` item 1 lists an alternative; treat the shipped line as
  the default and change it only deliberately.

## Conventions

- **Never use GitHub's web editor for HTML.** CodeMirror auto-closes tags and corrupts markup.
- Record decisions with reasoning and date, in the repo they belong to, **as they are made**.
- Update this file when a structural fact changes: hosting, branch state, page inventory,
  repo roles, design-system state.
