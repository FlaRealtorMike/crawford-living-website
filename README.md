# crawfordliving.com

The public website for Crawford Living — Michael Crawford, Broker-Associate, eXp Realty LLC.

Plain static HTML. No build step, no framework, no dependencies.

```
index.html       Home — who Mike is, the three paths, general resale/new construction
probate.html     For personal representatives. Gentle, plain, no calendar, no urgency
attorneys.html   For probate attorneys. Short and direct. noindex, nofollow
about.html       Background — 20 years, the construction company, RENE, the county map
assets/site.css  Shared stylesheet for all four pages

assets/hero-scene.svg           Home page hero — the house at dusk with a live oak, sun and walk
assets/skyline.svg              Rooftop silhouette behind the home page contact band
assets/house-elevation.svg      The house on its own, one window lit
assets/house-detail.svg         The same drawing, framed closer (probate + attorneys heroes)
assets/map-central-florida.svg  Schematic five-county map (inlined into about.html)
assets/mark.svg                 Roundel monogram used in the masthead
assets/favicon.svg              Tab icon
assets/mike-crawford.jpg        Portrait
```

*(Nav shows Home / Probate / About only. `attorneys.html` is deliberately kept out of the
nav and out of search — it's reached from the letter and from the home page card. The nav
had drifted to include it; the 2026-08-18 redesign put it back to the documented three.)*

To preview the whole site with working navigation:

```
python3 -m http.server 8765
```

then open http://localhost:8765.

**Created 2026-08-14** to replace the "Orlando Real Estate AI" Lovable test page that had
been sitting on this domain carrying fabricated testimonials and scarcity claims. See
`PROJECT_INDEX.md` in `crawford-living-brand-kit` for that history.

---

## Required disclosures — filled in 2026-08-14

The footer carries both, and both must stay on every page added later:

- Florida Broker license **BK3074190**
- eXp Realty LLC, 10752 Deerwood Park Blvd., Suite 100, Jacksonville, FL 32256

## Before it goes live

**Send it to eXp compliance.** The page it replaces was never reviewed by them, which was
half the problem. While Mike is a Broker-Associate under eXp, all advertising must carry the
brokerage name — the footer does this. Nothing here may be branded "Crawford Living Realty,
LLC" until that entity is formed and registered with DBPR.

---

## Deliberate omissions

The restraint is still the point. The site has, on purpose:

- **No lead form, no email capture, no calendar embed.** The letters ask for a conversation,
  not a funnel. A form here would contradict them.
- **No testimonials, no counts, no ratings, no "spots left."** This is the exact category of
  claim that made the previous page a compliance exposure.
- **No stock photography.** Every graphic on the site is drawn by hand as SVG.

If any of that gets added later, it should be a considered decision, not a default.

## The 2026-08-18 redesign

The first version was type and whitespace only — a deliberate reaction to the Lovable page it
replaced. That overcorrected: it read as a well-set letter rather than a website. The overhaul
added visual substance **without** touching the claims that made the old page an exposure.

What went in:

- **Drawn graphics, not stock.** A line-drawn Florida porch house with one lit window carries
  the home page; a closer crop of the same drawing heads the probate and attorney pages; a
  schematic five-county map sits on About; the item lists have drawn icons.
- **A probate timeline.** Five stages from opening the estate to closing, with the third
  highlighted in the gold/cream treatment from the brand kit. Stage labels are qualitative
  ("Once the court acts") rather than durations, and the caption says plainly it is a general
  sequence and not legal advice.
- **Paper grain.** A very low-opacity SVG noise overlay so the ivory reads as stock rather
  than a flat fill.
- **Structure:** card grids, a sticky masthead, an editorial label rail on prose sections, a
  navy contact band with a direct-line card, drop caps, pull quotes, and a footer nav.

Unchanged: the palette, the fonts, the tagline, every required disclosure, and the copy —
apart from short additions on About (Stellar MLS, the tagline paragraph) and the timeline text.

**Still no white anywhere.** Three ivory levels — `#EADCBC` sunk, `#F2E9D5` ground,
`#FCF8EC` raised, with `#DACBA9` rules.

### Home page, second pass

Mike asked for more graphics, home page only. Added:

- **`hero-scene.svg`** — the house is now in a scene rather than floating alone: a live oak
  with moss, a low sun, a neighbouring roofline set back, a hedge, mailbox, walk and grass.
  One window is lit in gold, the single warm accent.
- **Vignettes on the three entry cards** — house and key, document and pen, a rocking chair.
- **`skyline.svg`** — a rooftop-and-palm silhouette across the bottom of the navy contact
  band, which had been dead space.
- A gold diamond ornament between the lower sections.

**These are scoped to the home page on purpose.** The hero column ratio, the smaller display
size and the skyline all sit behind `.hero-scene` and `.reach.has-skyline`, so the other three
pages render exactly as they did — verified by comparing page heights before and after.

## Brand

Values come from `crawford-living-brand-kit.md` in the `crawford-living-brand-kit` repo:
Primary Navy `#0E2A57`, Secondary Blue `#19469C`, Gold `#E7C870` (used once, as the rule
under the wordmark). Lora for headlines, Source Sans for body. Tagline
"Real Estate . . . Considered". The eXp logo in `assets/` is the brand-kit copy, already
recolored to Secondary Blue rather than eXp's stock red.

## Hosting — GitHub Pages

Decided 2026-08-14. Serves straight from `main` at the repository root. The `CNAME` file
in this directory is what binds the site to the domain — **don't delete or rename it**, and
note that GitHub rewrites it if the custom domain is changed in the Pages settings UI.

DNS lives at **GoDaddy**. The apex needs GitHub's four A records:

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

and `www` needs a CNAME to `flarealtormike.github.io`.

**Two standing DNS cautions:**

1. **Never touch the MX records.** They point at Google Workspace and carry
   `mdc@crawfordliving.com`. Breaking them breaks email, silently, and mail sent in the
   meantime may bounce rather than queue.
2. The old apex A record pointing at **`185.158.133.1` (Lovable)** must be removed, or the
   domain will keep resolving to the dead test site.

After DNS propagates, tick **Enforce HTTPS** in the repository's Pages settings. It stays
greyed out until GitHub has issued the certificate, which can take up to an hour.
