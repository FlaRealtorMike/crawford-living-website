# Crawford Living — Website

**This repo is the website itself.** It is what visitors see. Everything else is context.

> **For everything open across all three repos, read `../crawford-living-brand/loose-ends.md`.**
> It is the single "what have I got going on" file — website, attorney mailing, brand docs, data
> pipeline, entity and eXp exit. The website items below are one section of it.

Plain static HTML today. **That is a description of what it currently is, not a constraint on
what it becomes** — see the rebuild rule directly below.

## ✅ RESOLVED 2026-09-10 — Crawford Living Realty, LLC is licensed; the site is live again

**DBPR issued the brokerage license today: `CQ1075533`** — Crawford Living Realty, LLC's own,
distinct from Mike's individual license `BK3074190` and from eXp's brokerage license
`CQ1037043` (see `../Crawford-Living/CLAUDE.md`). GitHub Pages was re-enabled the same day.
Verified 2026-09-10: `crawfordliving.com` returns **200**, the Pages API reports
`"status":"built"`, HTTPS certificate `"approved"` (expires 2026-11-13), and a
`grep -rl "exp realty\|exp-realty\|broker-associate"` across every page returns **nothing** —
eXp attribution is fully stripped, not just planned to be.

**Instruction 1 below is satisfied, not deleted as a rule.** The hold was conditional on the
license issuing; that condition is now met. If the entity or license ever lapses, the hold
logic reapplies — re-read it rather than assuming "it published once" is permanent cover.
Instruction 2 still stands unconditionally; keep reading it.

**What this changes operationally — see the rewritten Hosting section below.** The single
most important flip: **a push to `main` is a publication again.** The 2026-08-31–2026-09-10
window where the repo was "safe to build in, push freely" is over.

The original 2026-08-31 takedown record follows, kept for context on why the site looked the
way it did for those ten days:

**Mike's decision, 2026-08-31:** *"I don't want to sell eXp anymore."* The live eXp-branded site
came down that day. Two standing instructions followed, and both bound every session during the
hold:

**1. Nothing publishes until Crawford Living Realty, LLC is licensed.** ~~The site is rebuilt
internally and held.~~ **Satisfied 2026-09-10 — see above.** This was the same hold that governed
the attorney letters (policy 2026-08-29, `../crawford-living-brand/loose-ends.md` item 1) —
materials were built in the Crawford Living Realty identity and distributed only once the
licence issued.

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

## ✅ RESOLVED 2026-09-09 — the site is one design system, no more seams

**`index.html` is rebuilt onto `crawford.css`.** The last holdout — the bespoke navy "Hybrid"
system this section spent three updates describing — is gone. All eight pages (`index.html`,
`about.html`, `probate.html`, `attorneys.html`, `search.html`, `buy.html`, `sell.html`,
`communities.html`, `community-lake-nona.html`) now share `assets/crawford.css`, the settled
palette, Archivo + IBM Plex Mono, and the same six-item nav. eXp attribution dropped from the
homepage's title/meta/footer to match the other seven.

**`assets/site.css` and `assets/site-v2.css` are now safe to delete** — nothing references
them. Left in place for one more session in case anything was missed; delete on the next
pass through this repo if still unused.

The type-scale and nav-taxonomy decision this section used to say was blocking the homepage
rebuild: **decided 2026-09-09 — migrate onto `crawford.css` as-is, rather than inventing a
new scale first.** `crawford.css`'s own header still notes type scale and radius are
"carried over, not a system" — that remains true and unresolved, but it's no longer gating
anything. The rest of this section (below) is the pre-2026-09-09 record of how the site got
here; keep it for history, don't action anything in it.

## ⚠️ The site is currently split across THREE design systems

> ## ✅ Updated 2026-09-03 — four of five pages consolidated onto ONE system
>
> **`about.html`, `probate.html`, `attorneys.html` and `search.html` now share one
> stylesheet, `assets/crawford.css`**, on the settled palette (Crawford Black · Bond Paper ·
> Old Brass · Margin Grey · Onion Skin), **Archivo + IBM Plex Mono**, the unified **six-item
> nav**, a sticky header with labels always visible, and the accent-by-role / Onion-Skin
> patterns from `../crawford-living-brand/DESIGN.md` ("Accent & mark application"). **eXp
> attribution was stripped from these four** (logo, address, "Broker-Associate" → "Florida
> broker"); they build in the Crawford Living Realty identity, licence BK3074190 kept. The
> shared illustration `assets/house-detail.svg` was retinted to match.
>
> **`index.html` was deliberately left on its bespoke navy "Hybrid" system** — its concept is
> built on the old palette, and it should be redesigned once the **type scale** and **nav
> taxonomy** (still open in DESIGN.md) are settled, not re-skinned. Until then the site has
> exactly one seam: the homepage vs. the other four.
>
> **`assets/site.css` and `assets/site-v2.css` are now unused** (index is inline; the other
> four moved to `crawford.css`). Left in place as history; safe to delete once the homepage is
> rebuilt. **Type scale and radius remain undecided** — `crawford.css` carried each page's
> existing sizes over rather than inventing a scale, and uses a restrained 2px radius as an
> interim. The rest of this section is the pre-2026-09-03 record.

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

## Hosting — ✅ LIVE again, 2026-09-10. A push to `main` now publishes.

**GitHub Pages was re-enabled 2026-09-10**, the day the brokerage license issued. Verified the
same day: `crawfordliving.com` returns **200**, `gh api repos/FlaRealtorMike/crawford-living-website/pages`
reports `"status":"built"`, and the HTTPS certificate is `"approved"` (expires 2026-11-13).

**A push to `main` is a publication again — this reverses the dark-period rule above it:**

- **Treat `main` as production.** Do not commit-and-push freely the way the
  2026-08-31–2026-09-10 hold allowed. A push goes live within roughly the normal GitHub Pages
  build lag (observed 2026-09-10: still 404 immediately after push, 200 about ten seconds
  later on the next poll).
- **Preview locally before pushing anything non-trivial:** `python3 -m http.server 8765`.
- eXp attribution is out and — since the entity is now actually licensed — there is no
  eXp-attribution *requirement* left to satisfy either. See Required disclosures below.
- For the eXp exit paperwork itself (DBPR filings, offboarding, MLS/ORRA transfer), this file
  isn't the source of truth — check `../Crawford-Living/PROJECT_INDEX.md` item 18.

**What was true during the 2026-08-31–2026-09-10 dark period, kept for history:**

GitHub Pages was deleted on 2026-08-31 (`gh api -X DELETE .../pages`, run by Mike) — the site
was off the internet, and a push to `main` was not a publication. Nothing was ever mailed during
that window, so no attorney held the domain (confirmed against GoHighLevel, every contact read
`Mail date: NOT YET MAILED`) — that stopped being a non-issue the moment letters go out, so if
letters were ever mailed while the domain was dark, re-check this section's git history.

**What is live now, and must not be disturbed:**

- **DNS at GoDaddy is doing real work again.** The apex's four A records and `www`'s CNAME to
  `flarealtormike.github.io` are what's actually resolving `crawfordliving.com` — this is no
  longer a "harmless, points at 404" leftover.
- **Never touch the MX records.** They point at Google Workspace and carry
  `mdc@crawfordliving.com`. Breaking them breaks email silently.
- `CNAME` is in the repo root and is load-bearing — it's what re-binds the domain on every
  Pages build. Do not remove it.
- **The HTTPS certificate is approved, expires 2026-11-13** (verified via
  `gh api .../pages` 2026-09-10) — renewal is GitHub/Let's Encrypt's problem, not something to
  action here unless it starts failing.

**Hosting is GitHub Pages again, as of 2026-09-10 — this is a fact about the present, not a
design constraint.** The rebuild-rule principle from the top of this file still applies looking
forward: if a future requirement needs a real application host (IDX search against MLS Grid,
server-side rendering, a database), that's a hosting decision to make *then*, at the point
something actually needs it — not a reason to avoid using Pages today, and not a reason to
under-build a static page now on the assumption Pages won't last.

## Pages

```
index.html                Home — the umbrella. Six paths: Buy, Sell, New Construction,
                          Probate & Estates, Communities, Search Homes
buy.html                  Conversational and educational — timing, what to watch for
sell.html                 Analytical and confident — pricing, marketing, reporting
probate.html              For personal representatives. Gentle, plain, no calendar, no urgency
attorneys.html            For probate attorneys. Short and direct. noindex, nofollow
about.html                Background — 20+ years, construction coordination, RENE, CPRES
communities.html          Index — lists only the communities actually written up so far
community-lake-nona.html  The pilot community page — the template for the rest
search.html               Real launch pad: the branded app + a curated intake form
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
- 🔴 **ZERO probate transactions. Mike, 2026-09-01: *"I've never transacted a real property in an
  estate."*** Nothing may imply otherwise — no count, no frequency, no "I've seen this before".
  **Two false claims are live or drafted right now:** `probate.html:64` *"I've been through the
  process enough times to know what tends to come next"*, and on the 2026-08 canvas
  *"estate property is a regular part of the work rather than an occasional one."* Both must come
  out. **CPRES is not held either.** What is true, and is enough: 20+ years a licensed broker,
  RENE, and the construction-coordination background — the house in an estate is the part he has
  actually been doing for two decades, and the legal part belongs to the attorney anyway. Full
  inventory of true / false / unverified claims:
  `../crawford-living-brand/.claude/skills/crawford-living-brand-editor/proof-points.md`.
- **The construction background is coordination, not trades.** Never claim hands-on building
  and **never publish a homes-built figure** — a "four hundred homes a year" line was live
  until 2026-08-20. It is inaccurate, invites structural questions Mike is not licensed to
  answer, and risks NAR Article 12. Always pair it with the disclaimer the deeper pages use:
  process knowledge, not structural expertise; anything technical goes to a licensed inspector
  or engineer.
- **Boutique — neither one-man-show nor corporate.** Never imply staff who do not exist; never
  read as a solo operator either. The lever is *standard*, not headcount. 🔴 **"Takes on fewer
  transactions than it could, by design" / "By design, not by default" is RETIRED, 2026-09-09,
  Mike's call** — previously the approved lever, now reclassified as scale-by-implication even
  without a literal size word. No replacement phrase is approved; don't invent one, cut the
  volume-framing sentence instead. Also retired: "deliberately small", "one person by choice",
  "you work with me, not a team", any "reaches me directly" / "not an assistant" / "not a
  gatekeeper" claim (a receptionist answers first), and any claim of sole execution through
  closing. A 2026-09-09 sweep found several of these live on `index.html`, `about.html`, and
  `attorneys.html` (including a recurrence of the separately-retired "400 homes a year" figure)
  — all fixed same day. See `../crawford-living-brand/copy-inventory.md` and that skill's
  `anti-examples.md` for the full, current list.
- **No urgency, scarcity, testimonials, counts, or ratings.** Tone is the product, and that
  category of claim is what made the page this site replaced a compliance exposure.

## Required disclosures — ✅ now in the "published, licensed" state since 2026-09-10

**eXp attribution is out, permanently, not just while the rebuild was held.** The published
site now runs under Crawford Living Realty, LLC's own license — there is no eXp affiliation
left to disclose, so this isn't "the exception still holds," it's that the rule that used to
require eXp attribution no longer applies to this brokerage at all.

| | Now, 2026-09-10 and after |
|---|---|
| eXp lockup / address | **Out** — confirmed stripped from every page, 2026-09-10 |
| "Crawford Living Realty, LLC" | **Live** — the actual licensed brokerage |
| Broker licence **BK3074190** | Kept — Mike's individual license, unaffected by the entity change |
| Brokerage licence **CQ1075533** | **New** — Crawford Living Realty, LLC's own, in the footer site-wide |

🔴 **The one condition that would re-arm an eXp disclosure requirement:** if Mike ever
transacts under eXp again (a second license, a side arrangement, anything), *that* activity
would need eXp attribution wherever it's advertised. That's a different brokerage relationship
than this site describes, not a reason to touch this site. For the state of the actual eXp
exit paperwork (DBPR filings, offboarding, MLS/ORRA transfer), check
`../Crawford-Living/PROJECT_INDEX.md` item 18 — this file only tracks what the *website* needs
to show.

## Deliberate omissions — restraint is the point

- ~~**No lead form, no email capture, no calendar embed.**~~ 🔴 **REVERSED 2026-09-01, Mike's
  call:** *"Totally forget that I said we don't want lead form signups. Those are necessary. If a
  person wants to give me their information, I certainly should have something there to take it."*
  **Lead capture is permitted.** It routes to GoHighLevel. The old reasoning — that the attorney
  letters ask for a conversation, not a funnel — is recorded here so the reversal is a decision
  rather than a drift, but it no longer binds.
  ⚠️ Still true, and unchanged: **no calendar embed**, and the form's *language* still has to pass
  the brand rubric. Intake, not a gate.
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

- ✅ **Two design systems — RESOLVED 2026-09-09.** See the top of this file.
- 🟡 **New Construction — deferred to Phase 2 (Mike, 2026-09-04).** The launch ("Phase 1")
  site is **Buy, Sell, and Probate** — enough for a robust site. New Construction stays a
  homepage path/anchor only, with no standalone page until Phase 2. When built, it remains
  the **only** home for the construction-coordination story (`page-patterns.md`).
- ✅ **Communities — BUILT 2026-09-09, third entry added 2026-09-10.** `communities.html`
  (index), `community-lake-nona.html`, `community-windermere.html`, and
  `community-winter-park.html` are live, with generated imagery following `image-style.md`.
  Each detail page leads with its own boundary-mismatch fact: Lake Nona's build-out age range,
  Windermere's incorporated-town-vs-broader-area gap, and Winter Park's two zip codes (32789
  inside the actual city line vs. 32792, a mailing address that's mostly unincorporated
  county). Only these three are written up so far — the index deliberately doesn't pad out
  the other named places (see `crawford-living-brand/loose-ends.md` for the full list) until
  there's something real to say about them. A quarterly scheduled task per community refreshes
  its market-snapshot data from a single fixed source (Redfin) into
  `data/community-<name>-market.json` (`lake-nona-market-stats`, `windermere-market-stats`,
  `winter-park-market-stats`); each commits locally but never auto-pushes. No safety/crime
  content anywhere on these pages — Mike's call, 2026-09-08, recorded in the brand-editor
  skill's `page-patterns.md`.
- 🟢 **Search Homes — BUILT 2026-09-06.** `search.html` is now a real launch-pad page, not the
  honest placeholder (superseding the 2026-09-01 "do not build it" call below, which applied to
  a full public IDX grid, not this model). Two paths: **Search it yourself** (the MLS-Touch
  Brand & Share pitch + two app buttons) and **Prefer something curated** (a full intake form —
  name/email/phone, the five counties as checkboxes, price range, beds/baths, a free-text
  must-haves field, timeline, financing status). A `#contact` band covers anyone not ready for
  either. Copy passed the brand-editor rubric; images are house-style (a screen-off phone on a
  sunlit table — deliberately no fake app UI, no logos).
  - 🟢 **Intake form wired to GoHighLevel, 2026-09-07.** The `#curated` section's form is now
    the real GHL embed (formId `sq2766ibosmcvJXZqc3L`, "Website — Search Homes Page" — sixth and
    last of the site's forms; Buy, Sell, Probate, Attorneys and About were done earlier). Fields:
    name/email/phone, "Areas you're considering" (5 counties), price low/high, bedrooms/bathrooms
    at least, "What actually matters" (free text), timeline, financing. The mailto fallback and
    its page-scoped `.finder`/`.thanks` CSS were removed — submissions now go through GHL like
    every other page, not a `mailto:` link.
  - 🟢 **Brand & Share link wired, 2026-09-08.** Mike's initial reply supplied the plain App
    Store / Google Play URLs, then corrected that there's no separate per-platform link — only
    one: `https://mls-client.com/0C1C5F73`. This is the actual personalized Brand & Share link
    (device-aware, routes to the right store/app, and is what carries his branding and reports
    activity back to him — not a generic store page). `search.html`'s `id="app"` section now has
    a single "Open the app" button pointing at it, replacing the earlier two-button iPhone/Android
    layout and the `href="#"` placeholders before that.
  - 🟡 **Updated 2026-09-05 — the plan behind this build.**
    Investigated with Mike. **Stellar MLS-Touch "Brand & Share"** is a **branded mobile app**
    (iOS/Android, free with the Stellar subscription): Mike personalizes it with his logo, shares
    it, prospects search Matrix listings, their activity flows back to him, and the branding
    carries into **OneHome**. It is **app-first — not a web/desktop search you can embed** (the
    product page confirms mobile app; a web-openable link is unconfirmed). So the site's **Search
    Homes** page becomes a **launch pad**: the Brand & Share link + App Store / Play badges, PLUS
    a short *"prefer I set one up?"* **intake form → GoHighLevel → Mike sends a OneHome invite**.
    The **OneHome invite is manual** (sign into Stellar, add the customer, send the link); lead
    capture is permitted (reversed 2026-09-01) and routes to GoHighLevel.
    - **Instant delivery is solved by the self-serve share link + a GHL auto-reply — NOT by
      automating a Stellar login.** A login bot would risk MLS ToS, is brittle, and needs an
      always-on runner (a Claude Code / Claude-in-Chrome session is interactive, not a 24/7
      server). The mobile-app share removes the need to automate anything.
    - **Blocked on Mike, updated 2026-09-08:** (a) still open — confirm with Stellar whether
      Brand & Share is anonymous or requires registration to search; (b) ✅ done — the GHL form
      is built and embedded (see above); (c) ✅ done — the Brand & Share link is
      `https://mls-client.com/0C1C5F73`, wired into `search.html`.
    - True anonymous **desktop** browsing on our own domain is still only solved by a **rented
      IDX** (iHomeFinder/IDX Broker, paid) — a later call, and still "do not build your own."
  The MLS Grid demo feed was queried and the IDX rules read in full. Two findings settle it:
  **every photo must be self-hosted** (their URLs are single-use and expire in an hour), which
  against a 40,000-request/day cap is ~**two weeks** of syncing for a first load plus ~21,600
  images/day of churn; and **it is not a search API** — only seven technical fields are
  filterable, so it is a bulk-replication source you copy into your own database. That means a
  server, a database and hundreds of GB of storage for a page with no audience yet.
  - **What replaces it: OneHome**, free with the Stellar MLS subscription, branded to Crawford
    Living, surviving the eXp exit. Invite-only, which fits *"tell us what you're looking for"*
    better than a public grid does.
  - **If it is ever genuinely needed, rent it** — iHomeFinder, IDX Broker, Showcase IDX.
    **Do not build it.**
  - ⚠️ **If this is reopened, the display rules bind the design before it is drawn:** listing
    brokerage, listing number, phone/e-mail and status must sit immediately adjacent to every
    listing, *"not smaller than the median used in the display of listing data"* — the small-grey
    attribution treatment is not permitted. Full detail:
    `../Crawford-Living/PROJECT_INDEX.md` item 15.
- Before selecting any IDX provider, check Stellar
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
