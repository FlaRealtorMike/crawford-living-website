# crawfordliving.com

The public website for Crawford Living — Michael Crawford, Broker-Associate, eXp Realty LLC.

Plain static HTML. No build step, no framework, no dependencies.

```
index.html       Home — who Mike is, the three paths, general resale/new construction
probate.html     For personal representatives. Gentle, plain, no calendar, no urgency
attorneys.html   For probate attorneys. Short and direct. noindex, nofollow
about.html       Background — 20 years, the construction company, RENE
assets/site.css  Shared stylesheet for all four pages
```

*(Nav shows Home / Probate / About only. `attorneys.html` is deliberately kept out of the
nav and out of search — it's reached from the letter and from the home page card.)*

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

This page is a holding page, and the restraint is the point. It has, on purpose:

- **No lead form, no email capture, no calendar embed.** The letters ask for a conversation,
  not a funnel. A form here would contradict them.
- **No testimonials, no counts, no ratings, no "spots left."** This is the exact category of
  claim that made the previous page a compliance exposure.
- **No stock photography.** Type and whitespace only.

If any of that gets added later, it should be a considered decision, not a default.

## Brand

Values come from `crawford-living-brand-kit.md` in the `crawford-living-brand-kit` repo:
Primary Navy `#0E2A57`, Secondary Blue `#19469C`, Gold `#E7C870` (used once, as the rule
under the wordmark). Lora for headlines, Source Sans for body. Tagline
"Real Estate . . . Considered". The eXp logo in `assets/` is the brand-kit copy, already
recolored to Secondary Blue rather than eXp's stock red.

## Hosting

Not yet decided. `crawfordliving.com` currently points at Lovable (`185.158.133.1` at the
apex, GoDaddy DNS, Google Workspace MX records that **must not be touched**).

Two straightforward options for a static site:

- **GitHub Pages** — free, publishes from this repo. Needs a `CNAME` file containing
  `crawfordliving.com` plus A records at GoDaddy pointing to GitHub's IPs.
- **Netlify / Cloudflare Pages** — free, connects to this repo, handles TLS and DNS more
  gently.

Either way `www.crawfordliving.com` needs a DNS record — it currently does not resolve
at all.
