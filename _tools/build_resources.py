#!/usr/bin/env python3
"""Refresh everything that depends on the articles in resources/.

Run from the repo root after adding or editing an article:

    python3 _tools/build_resources.py            # update files
    python3 _tools/build_resources.py --check    # report problems only, change nothing

What it does, for every resources/<slug>.html (except index.html):
  1. Checks the article: title, description, dates, section, at least one source,
     no {{placeholders}} left, and no mention of AI in the visible text.
  2. Writes the byline (author + published / updated dates) from the structured data.
  3. Copies the Sources list into the Article structured data as "citation".
Then it rebuilds:
  - resources/index.html   the article list and its ItemList structured data
  - resources/feed.xml     RSS feed, newest first (the newsletter's "Michael's Musings"
                           corner uses the newest five)
  - sitemap.xml            adds or updates each article URL and the index
  - llms.txt               the "Articles" section
Finally it prints a plain-text "Michael's Musings" block (newest five) for the newsletter.
The newsletter must not carry clickable links to crawfordliving.com for now, so the
block names the address as plain text.

Standard library only. No network access.
"""
import datetime as dt
import html
import json
import re
import sys
from email.utils import format_datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RES = ROOT / "resources"
SITE = "https://crawfordliving.com"
SECTIONS = {"Probate & inherited homes", "Selling a home", "Local market"}
MUSINGS_COUNT = 5

LD_RE = re.compile(r'(<script type="application/ld\+json" id="article-ld">)(.*?)(</script>)', re.S)


def between(text, name, new):
    """Replace the content between <!--name--> and <!--/name--> markers."""
    pat = re.compile(r"(<!--%s-->)(.*?)(<!--/%s-->)" % (name, name), re.S)
    if not pat.search(text):
        raise SystemExit("marker <!--%s--> missing" % name)
    return pat.sub(lambda m: m.group(1) + new + m.group(3), text, count=1)


def nice_date(iso):
    d = dt.date.fromisoformat(iso)
    return "%s %d, %d" % (d.strftime("%B"), d.day, d.year)


def visible_text(page):
    body = page.split("<body", 1)[-1]
    body = re.sub(r"<script.*?</script>|<!--.*?-->", " ", body, flags=re.S)
    return html.unescape(re.sub(r"<[^>]+>", " ", body))


def load(path):
    page = path.read_text(encoding="utf-8")
    problems = []
    m = LD_RE.search(page)
    if not m:
        return page, None, ["no <script id=\"article-ld\"> block"]
    try:
        ld = json.loads(m.group(2))
    except ValueError as e:
        return page, None, ["structured data is not valid JSON: %s" % e]

    slug = path.stem
    url = "%s/resources/%s.html" % (SITE, slug)
    for key in ("headline", "description", "datePublished", "dateModified", "articleSection"):
        if not str(ld.get(key, "")).strip():
            problems.append("missing %s" % key)
    if "{{" in page:
        problems.append("unfilled {{placeholder}} left in the page")
    if ld.get("articleSection") not in SECTIONS:
        problems.append("articleSection must be one of: %s" % ", ".join(sorted(SECTIONS)))
    for key in ("datePublished", "dateModified"):
        try:
            dt.date.fromisoformat(ld.get(key, ""))
        except ValueError:
            problems.append("%s must be YYYY-MM-DD" % key)
    if ld.get("mainEntityOfPage") != url:
        problems.append("mainEntityOfPage should be %s" % url)
    if re.search(r"\b(AI|A\.I\.|artificial intelligence|ChatGPT|chatbot)\b", visible_text(page)):
        problems.append("visible text mentions AI (not allowed on public pages)")

    src = re.search(r'<ol class="sources">(.*?)</ol>', page, re.S)
    cites = []
    if src:
        for li in re.finditer(r"<li[^>]*>(.*?)</li>", src.group(1), re.S):
            a = re.search(r'<a href="([^"]+)"', li.group(1))
            if not a:
                continue
            name = html.unescape(re.sub(r"<[^>]+>", "", li.group(1)))
            name = re.sub(r"\s+", " ", name).strip()
            cites.append({"@type": "CreativeWork", "name": name, "url": a.group(1)})
    if not cites:
        problems.append("no sources listed in <ol class=\"sources\">")
    ld["citation"] = cites
    ld["_slug"] = slug
    ld["_url"] = url
    return page, ld, problems


def write_article(path, page, ld):
    pub, mod = ld["datePublished"], ld["dateModified"]
    line = '<p class="byline">By <a href="/about.html">Michael Crawford</a>, RENE, CPRES · Central Florida real estate broker: buying, selling &amp; probate · Crawford Living Realty, LLC<br>' \
           'Published <time datetime="%s">%s</time>' % (pub, nice_date(pub))
    if mod != pub:
        line += ' &middot; Updated <time datetime="%s">%s</time>' % (mod, nice_date(mod))
    line += "</p>"
    page = between(page, "byline", line)
    clean = {k: v for k, v in ld.items() if not k.startswith("_")}
    page = LD_RE.sub(lambda m: m.group(1) + "\n" + json.dumps(clean, indent=2, ensure_ascii=False) + "\n" + m.group(3), page, count=1)
    path.write_text(page, encoding="utf-8")


def esc(s):
    return html.escape(s, quote=True)


def build_index(arts):
    idx = RES / "index.html"
    page = idx.read_text(encoding="utf-8")
    if arts:
        items = []
        for a in arts:
            items.append(
                '        <li>\n'
                '          <p class="article-meta">%s &middot; <time datetime="%s">%s</time></p>\n'
                '          <h2><a href="/resources/%s.html">%s</a></h2>\n'
                '          <p>%s</p>\n'
                '        </li>' % (esc(a["articleSection"]), a["datePublished"], nice_date(a["datePublished"]),
                                   a["_slug"], esc(a["headline"]), esc(a["description"])))
        listing = '\n        <ol class="article-list">\n' + "\n".join(items) + "\n        </ol>\n"
        robots = ""
    else:
        listing = "\n        <p>The first article is on its way.</p>\n"
        robots = '\n<meta name="robots" content="noindex">\n'
    ld = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "@id": SITE + "/resources/#page",
        "name": "Resources",
        "url": SITE + "/resources/",
        "publisher": {"@id": SITE + "/#brokerage"},
        "mainEntity": {
            "@type": "ItemList",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "url": a["_url"], "name": a["headline"]}
                for i, a in enumerate(arts)
            ],
        },
    }
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Resources", "item": SITE + "/resources/"}]}
    ldtxt = "\n<script type=\"application/ld+json\">%s</script>\n<script type=\"application/ld+json\">%s</script>\n" % (
        json.dumps(ld, ensure_ascii=False), json.dumps(crumbs, ensure_ascii=False))
    page = between(page, "articles", listing)
    page = between(page, "robots", robots)
    page = between(page, "listld", ldtxt)
    idx.write_text(page, encoding="utf-8")


def build_feed(arts):
    def rfc(iso):
        d = dt.date.fromisoformat(iso)
        return format_datetime(dt.datetime(d.year, d.month, d.day, 8, 0, tzinfo=dt.timezone(dt.timedelta(hours=-5))))
    items = []
    for a in arts:
        items.append(
            "    <item>\n"
            "      <title>%s</title>\n"
            "      <link>%s</link>\n"
            "      <guid isPermaLink=\"true\">%s</guid>\n"
            "      <pubDate>%s</pubDate>\n"
            "      <dc:creator>Michael Crawford</dc:creator>\n"
            "      <category>%s</category>\n"
            "      <description>%s</description>\n"
            "    </item>" % (esc(a["headline"]), a["_url"], a["_url"], rfc(a["datePublished"]),
                             esc(a["articleSection"]), esc(a["description"])))
    last = rfc(arts[0]["datePublished"]) if arts else format_datetime(dt.datetime.now(dt.timezone.utc))
    feed = ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<rss version="2.0" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:atom="http://www.w3.org/2005/Atom">\n'
            "  <channel>\n"
            "    <title>Crawford Living Resources</title>\n"
            "    <link>%s/resources/</link>\n"
            '    <atom:link href="%s/resources/feed.xml" rel="self" type="application/rss+xml"/>\n'
            "    <description>Articles by Michael Crawford, broker of Crawford Living Realty, LLC, on selling a home, inherited homes and probate, and the Central Florida market.</description>\n"
            "    <language>en-us</language>\n"
            "    <lastBuildDate>%s</lastBuildDate>\n"
            "%s\n"
            "  </channel>\n"
            "</rss>\n") % (SITE, SITE, last, "\n".join(items))
    (RES / "feed.xml").write_text(feed, encoding="utf-8")


def build_sitemap(arts):
    sm = ROOT / "sitemap.xml"
    text = sm.read_text(encoding="utf-8")
    want = [(a["_url"], a["dateModified"]) for a in arts]
    if arts:
        want.append((SITE + "/resources/", max(a["dateModified"] for a in arts)))
    for url, mod in want:
        line = "  <url><loc>%s</loc><lastmod>%s</lastmod></url>" % (url, mod)
        pat = re.compile(r"  <url><loc>%s</loc>.*?</url>" % re.escape(url))
        if pat.search(text):
            text = pat.sub(line, text, count=1)
        else:
            text = text.replace("</urlset>", line + "\n</urlset>")
    sm.write_text(text, encoding="utf-8")


def build_llms(arts):
    p = ROOT / "llms.txt"
    text = p.read_text(encoding="utf-8")
    start, end = "<!-- articles -->", "<!-- /articles -->"
    body = ""
    if arts:
        body = "\n## Articles\n\n- [Resources](%s/resources/): all articles, newest first\n" % SITE
        body += "".join("- [%s](%s): %s\n" % (a["headline"], a["_url"], a["description"]) for a in arts)
    block = start + "\n" + body + end
    if not arts and start not in text:
        return
    if start in text:
        text = re.sub(re.escape(start) + ".*?" + re.escape(end), lambda m: block, text, flags=re.S)
    else:
        text = text.rstrip("\n") + "\n\n" + block + "\n"
    p.write_text(text, encoding="utf-8")


def musings(arts):
    print("\nMICHAEL'S MUSINGS (newest %d) — paste into the newsletter\n" % MUSINGS_COUNT)
    if not arts:
        print("  (no articles yet)")
        return
    for a in arts[:MUSINGS_COUNT]:
        print("- %s (%s)\n  %s\n" % (a["headline"], nice_date(a["datePublished"]), a["description"]))
    print("Read them all at crawfordliving.com/resources")


def main():
    check = "--check" in sys.argv
    loaded, bad = [], False
    for path in sorted(RES.glob("*.html")):
        if path.name == "index.html":
            continue
        page, ld, problems = load(path)
        if problems:
            bad = True
            print("PROBLEM in resources/%s:" % path.name)
            for p in problems:
                print("  - " + p)
        if ld:
            loaded.append((path, page, ld))
    if bad:
        raise SystemExit("\nFix the problems above; nothing was changed.")
    arts = sorted((ld for _, _, ld in loaded), key=lambda a: (a["datePublished"], a["_slug"]), reverse=True)
    print("%d article(s) OK." % len(arts))
    if check:
        return
    for path, page, ld in loaded:
        write_article(path, page, ld)
    build_index(arts)
    build_feed(arts)
    build_sitemap(arts)
    build_llms(arts)
    musings(arts)


if __name__ == "__main__":
    main()
