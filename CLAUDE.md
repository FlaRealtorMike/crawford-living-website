# Crawford Living — Website

**This repo is the website itself.** It is what visitors see. Everything else is context.

> **For everything open across all three repos, read `../crawford-living-brand/loose-ends.md`.**
> It is the single "what have I got going on" file — website, attorney mailing, brand docs, data
> pipeline, entity and eXp exit. The website items below are one section of it.

Plain static HTML today. **That is a description of what it currently is, not a constraint on
what it becomes** — see the rebuild rule directly below.

## 🔴 Taken offline 2026-08-31 — and the rebuild is not bound by what it replaced

**Mike's decision, 2026-08-31:** *"I don't want to sell eXp anymore."* The live eXp-branded site
came down that day. Two standing instructions follow, and both bind every future session:

**1. Nothing publishes until Crawford Living Realty, LLC is licensed.** The site is rebuilt
internally and held. This is the same hold that governs the attorney letters (policy 2026-08-29,
`../crawford-living-brand/loose-ends.md` item 1) — materials are built in the Crawford Living
Realty identity and distributed only once the licence issues.

**2. Do not design to the old hosting.** Mike, 2026-08-31: *"I don't want this new website
designed with constraints because the current hosting can't deliver something. Don't design a
site just because all we are serving now is a static site. I want the site to be the best and
then we can find the most cost effective (if necessary) means of hosting the site."*

> **Design what the work actually needs, then choose hosting to match.** Never the reverse.
> A dynamic requirement — IDX search against the MLS Grid feed, server-side rendering, a
> database, saved searches, auth — is a hosting question to answer *later*, never a reason to
> narrow the design *now*. "GitHub Pages can't do that" is not a design input. If a direction
> needs a real application host, say so and cost it; do not quietly shrink the idea to fit a
> static file server.


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

## ⚠️ The site is currently split across THREE design systems

The 2026-08-19 redesign was merged into `main` on **2026-08-20**, and the homepage was replaced
again by the Hybrid direction (`83669f9`). Neither pass covered every page, so the site has two
seams, not one:

**✅ Verified against the files on disk 2026-08-23:**

| Page | Stylesheet | Type |
|---|---|---|
| `index.html` | **none — styles are inline** | **Big Shoulders / Newsreader / Instrument Sans / IBM Plex Mono** |
| `search.html` | `assets/site-v2.css` | **Archivo + Inter** |
| `about.html` | `assets/site.css` | Lora + Source Sans 3 |
| `probate.html` | `assets/site.css` | Lora + Source Sans 3 |
| `attorneys.html` | `assets/site.css` | Lora + Source Sans 3 |

⚠️ **This table said `index.html` used `site-v2.css` with Archivo + Inter until 2026-08-23.**
It never did after the Hybrid landed — it loads no external stylesheet at all. The homepage and
`search.html` are **not** the same system, so "port the rest onto `site-v2.css`" is not the whole
job: decide first which of the two the site is actually standardising on.

**The navigation splits too, and that is the sharper problem:**

| Page | Nav |
|---|---|
| `index.html`, `search.html` | Buy · Sell · New Construction · Probate & Estates · Communities · Search Homes |
| `about.html`, `probate.html`, `attorneys.html` | Home · Probate · About |

**A visitor clicking Home → Probate crosses a font change, a style change, and loses four of
the six ways in** — with no route back to Buy, Sell, New Construction, Communities or Search.
That is an orientation failure, and it contradicts the rule that motion and structure never
cost the visitor their place.

This is the top outstanding defect. Finishing it means porting the three remaining pages onto
`site-v2.css` and the six-item nav — a real piece of work, not a find-and-replace. If only one
half can be done first, **do the nav**: mismatched type is a blemish, a mismatched nav is a
dead end.

Do not "fix" it by reverting the homepage. The homepage is the agreed direction.

## Branch discipline

⚠️ **The original reason for this section is gone** — there is no live domain to drift from
since 2026-08-31. Kept because the *other* half still bites: work has twice been committed to a
branch and left unmerged, and a session then rebuilt from scratch what already existed.
Before concluding the site "looks old" or rebuilding anything:

```
git log main..origin/<branch>
git branch -a
```

`claude/crawford-living-website-status-unbl05` is **merged and spent**. Do not build on it.

## Hosting — 🔴 NOTHING IS SERVED. Verified 2026-08-31.

**GitHub Pages was deleted on 2026-08-31** (`gh api -X DELETE .../pages`, run by Mike). The site
is off the internet. Verified the same day: the Pages config returns 404, and the apex, `www`
and deep links all return **404** — a visitor gets GitHub's generic *"Site not found"*, which
carries no eXp branding and no Crawford Living branding.

**A push to `main` is therefore no longer a publication.** That changes the working rules:

- **The repo is now safe to build in.** Commit and push freely while the new site is developed.
  The old hazard — every push landing on a live domain — is gone.
- **Re-enabling Pages is the publication event**, and it is gated on Crawford Living Realty, LLC
  being licensed. See the rebuild rule at the top of this file. Do not re-enable it to "preview"
  something; run `python3 -m http.server 8765` locally instead.
- ⚠️ **Nothing was ever mailed**, so no attorney holds this domain — confirmed against
  GoHighLevel, where every contact reads `Mail date: NOT YET MAILED`. That is *why* taking the
  domain dark stranded nobody, and it stops being true the moment letters go out. **If letters
  are ever mailed while the domain is dark, that is a live problem** — re-check this before any
  print run.

**What is still bound, and must not be disturbed:**

- **DNS is untouched at GoDaddy.** The apex still carries GitHub's four A records and `www`
  still CNAMEs to `flarealtormike.github.io`. Harmless — they point at a host serving 404 — and
  leaving them makes the eventual relaunch or migration simpler.
- **Never touch the MX records.** They point at Google Workspace and carry
  `mdc@crawfordliving.com`. Verified intact after the takedown. Breaking them breaks email
  silently.
- `CNAME` is still in the repo root. Keep it. It costs nothing and re-binds the domain if Pages
  is ever re-enabled here.

**The HTTPS certificate was discarded with the Pages site.** It had been approved through
2026-11-13. Re-enabling means re-adding the custom domain and waiting for a fresh Let's Encrypt
cert, which can take up to ~24h. Budget for that on launch day; it is not instant.

**Hosting is an open question, deliberately.** Do not assume the rebuild returns to GitHub Pages
— see the rebuild rule at the top of this file. IDX search against the MLS Grid feed needs
server-side fetching, caching and scheduled sync, which Pages cannot do at any price.

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

**Colour — 🔴 the palette below was SUPERSEDED 2026-08-29. Corrected here 2026-08-31.**

> This file recorded navy + ivory + "no white anywhere" as settled and used site-wide. It
> was superseded the same week by the 🔒 DECIDED block in
> `../Crawford-Living/crawford-living-brand-kit.md`, and **this stale copy actively misled a
> review on 2026-08-31** — it produced a finding that the 2026-08 canvas had "drifted" from
> the brand when the canvas was implementing the current palette correctly.

**The settled palette — brand kit, 2026-08-29:**

| Token | Name | Hex | Use |
|---|---|---|---|
| `--ink` | Crawford Black | `#1A202C` | Text, wordmark, headings, buttons, rules |
| `--surface` | Bond Paper | `#FAF9F6` | Every background |
| `--accent` | Old Brass | `#A8813C` | One emphasis per page — **rules, seals, marks** |
| `--muted` | Margin Grey | `#5E6470` | Secondary text, labels, captions |
| `--subtle` | Onion Skin | `#E6E6E1` | Panel and callout fills |

⚠️ **Old Brass is a MARK colour, not a text colour.** Computed 2026-08-31: `#A8813C` on
Bond Paper is **3.40:1** — clears the 3:1 threshold for rules and marks, fails the 4.5:1
floor for text. On Onion Skin it is **2.86:1** and fails everything, so that pairing has no
safe use at any size. Set label text in Crawford Black or Margin Grey.

**Superseded, kept only as history:** Primary Navy `#0E2A57` · Secondary Blue `#19469C` ·
Gold `#E7C870` · gold text `#8A6D2F` · ivory grounds `#EADCBC` / `#F2E9D5` / `#FCF8EC` /
`#DACBA9` · "no white anywhere". **The five live pages still use this system** — they
predate the decision. That is one more thing to settle before anything publishes.

**Type — unsettled, and the docs disagree three ways.** `DESIGN.md` documents Archivo + Inter as
the applied system; the brand kit still names Lora / Source Sans Pro; and **the homepage now runs
neither** — Big Shoulders / Newsreader / Instrument Sans (see the table above). That is
`open-decisions.md` **item 6**, and the homepage has *not* quietly decided it in practice as this
file used to claim. **Decide the real type system first, then update the kit and `DESIGN.md`
together** — writing Archivo + Inter into the kit today would enshrine something the homepage
does not use. Note the printed attorney letters are on ivory cotton stock.

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

## Required disclosures — 🔴 this rule INVERTED on 2026-08-31

**Do not add eXp attribution to the rebuild, and do not flag its absence as a defect.**

The old rule — *all advertising carries the eXp brokerage name* — applied because the site was
**published** while Mike is a Broker-Associate under eXp. It is not published any more. Nothing
being built now is advertising, because nothing is distributed, and the standing instruction for
all pre-launch work is that it is built in the **Crawford Living Realty** identity and held until
the licence issues. This matches the attorney letter, which had its eXp lockup removed on
2026-08-29 for exactly this reason.

| | While the rebuild is held | On the day it publishes |
|---|---|---|
| eXp lockup / address | **Out** | Out — the licence will have issued |
| "Crawford Living Realty, LLC" | Fine to build with | Live once DBPR registers the entity |
| Broker licence **BK3074190** | Keep — it is Mike's, not eXp's | Keep |

⚠️ **The old files still carry eXp.** All five pages in this repo still have the eXp address and
the Broker-Associate line, and `assets/exp-realty-logo-white.svg` is still referenced. That is
fine while nothing is served, but **the eXp attribution must be stripped before anything is
published**, not left for launch day to catch.

🔴 **Two conditions that would re-arm the old rule.** Re-read this before assuming eXp is out:

1. **If any surface goes live again while Mike is still under eXp**, that surface is advertising
   and must carry the eXp brokerage name. The rule is about *publication*, not about the repo.
2. **The eXp compliance e-mail is no longer needed for this site** (draft at
   `../Crawford-Living/compliance/exp-website-review-request.md`, never sent). There is nothing
   live to review. It becomes necessary again the moment condition 1 is true.

**Nothing may be branded "Crawford Living Realty, LLC" in a *published* context** until the
entity is formed and registered with DBPR. Building in that identity is exactly what is wanted;
publishing in it before the licence is not.

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
  - ✅ **A working MLS Grid DEMO feed against real Stellar MLS data is already available, set up
    2026-08-31.** Data Consumer account + Access Token live in Mike's MLS Grid account
    (`app.mlsgrid.com`, Manage Subscriptions → Crawford Living Realty LLC subscriptions.demo_display
    Subscription). This is separate from — and not blocked by — the still-open Stellar Case
    #00065984 for the production feed. **When work on `search.html`'s real search functionality
    starts, this demo feed is what to build/test against**, not a placeholder or mock data. Full
    detail in `../Crawford-Living/PROJECT_INDEX.md` under item 15. Going live for real visitors
    still requires the separate production subscription + signed Data License Agreement (Mike's
    signature, not Claude's) once ready to launch.
- **The brand line** — "Real Estate… CONSIDERED" is what shipped, on the site and on the
  printed letters. `open-decisions.md` item 1 lists an alternative; treat the shipped line as
  the default and change it only deliberately.

## Conventions

- **Never use GitHub's web editor for HTML.** CodeMirror auto-closes tags and corrupts markup.
- Record decisions with reasoning and date, in the repo they belong to, **as they are made**.
- Update this file when a structural fact changes: hosting, branch state, page inventory,
  repo roles, design-system state.
