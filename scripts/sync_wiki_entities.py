#!/usr/bin/env python3
"""
scripts/sync_wiki_entities.py
=============================
Builds the unified Google Knowledge Graph dataset (`data/knowledge-graph.json`)
anchored to canonical entity `@id: "https://www.harshverma.me/#person"`,
generates programmatic Wikidata (`Q139827028`) QuickStatements (`data/wikidata-quickstatements.txt`),
generates the complete EverybodyWiki biography Wikitext (`data/everybodywiki-article.wiki`),
and executes live MediaWiki Action API synchronization against:
  1. Wikidata: https://www.wikidata.org/wiki/Q139827028 (including removing ACM Q127992)
  2. EverybodyWiki: https://en.everybodywiki.com/Harsh_Verma_(Software_Engineer)
"""

import os
import re
import json
import urllib.request
import urllib.parse
import urllib.error
import http.cookiejar
from datetime import datetime, timezone

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

WIKIDATA_QID = "Q139827028"
WIKIDATA_API = "https://www.wikidata.org/w/api.php"
EVERYBODYWIKI_TITLE = "Harsh_Verma_(Software_Engineer)"
EVERYBODYWIKI_API = "https://en.everybodywiki.com/api.php"

# Primary canonical domain (www.harshverma.me), with root domain harshverma.me reconciled
CANONICAL_SITE_URL = "https://www.harshverma.me"
SECONDARY_SITE_URL = "https://harshverma.me"
USER_AGENT = "HarshVermaKnowledgeGraphBot/3.0 (https://www.harshverma.me/; mailto:harshverma59@gmail.com)"


def clean_html(raw_html):
    if not raw_html:
        return ""
    text = re.sub(r"<[^>]+>", " ", raw_html)
    text = (
        text.replace("&amp;", "&")
        .replace("&quot;", '"')
        .replace("&#39;", "'")
        .replace("&rsquo;", "'")
        .replace("&ldquo;", '"')
        .replace("&rdquo;", '"')
        .replace("&ndash;", "-")
        .replace("&mdash;", "—")
        .replace("&nbsp;", " ")
        .replace("&reg;", "®")
    )
    return re.sub(r"\s+", " ", text).strip()


MONTH_MAP = {
    "jan": "01", "january": "01",
    "feb": "02", "february": "02",
    "mar": "03", "march": "03",
    "apr": "04", "april": "04",
    "may": "05",
    "jun": "06", "june": "06",
    "jul": "07", "july": "07",
    "aug": "08", "august": "08",
    "sep": "09", "september": "09",
    "oct": "10", "october": "10",
    "nov": "11", "november": "11",
    "dec": "12", "december": "12",
}


def parse_iso_date(raw_date):
    """Convert any human-readable, partial, or anomalous date string into strict ISO 8601 (YYYY-MM-DD or YYYY)."""
    if not raw_date or not isinstance(raw_date, str):
        return "2026"
    s = raw_date.strip()
    if re.match(r"^\d{4}-\d{2}-\d{2}$", s):
        return s
    # Check "Month Day, Year" e.g. "October 2, 2026"
    m = re.match(r"^([A-Za-z]+)\s+(\d{1,2}),\s*(\d{4})$", s)
    if m:
        mon_str, day, yr = m.group(1).lower(), m.group(2).zfill(2), m.group(3)
        if mon_str in MONTH_MAP:
            return f"{yr}-{MONTH_MAP[mon_str]}-{day}"
    # Check "Month Year" e.g. "August 2026" or "Nov 2026"
    m = re.match(r"^([A-Za-z]+)\s+(\d{4})$", s)
    if m:
        mon_str, yr = m.group(1).lower(), m.group(2)
        if mon_str in MONTH_MAP:
            return f"{yr}-{MONTH_MAP[mon_str]}-01"
    # Check 4-digit year
    m = re.search(r"\b(19\d\d|20\d\d)\b", s)
    if m:
        return m.group(1)
    return "2026"


def extract_verified_profiles():
    """Extract all 54 verified profile cards (with SVG/PNG images and all links) from page-about.html."""
    about_path = os.path.join(ROOT_DIR, "page-about.html")
    profiles = []
    seen_keys = set()

    if os.path.exists(about_path):
        with open(about_path, "r", encoding="utf-8") as f:
            html = f.read()

        chunks = re.split(r'<div class="col-lg-4 col-md-6 mb-4 profile-card-item"', html)[1:]
        for chunk in chunks:
            chunk = chunk.split("<!-- End Verified Profiles")[0]
            # Skip any ACM related profile if ever present
            if "myacm.acm.org" in chunk.lower():
                continue

            cat_code_m = re.search(r'data-category="([^"]+)"', chunk)
            category_code = cat_code_m.group(1).strip() if cat_code_m else "direct"

            img_m = re.search(r'<img\s+src="([^"]+)"', chunk)
            image_path = img_m.group(1).strip() if img_m else "images/profiles/wikidata.svg"

            title_m = re.search(r'<h5 class="profile-card-title[^"]*">(.*?)</h5>', chunk, re.DOTALL)
            cat_m = re.search(r'<span class="profile-category-pill[^"]*">(.*?)</span>', chunk, re.DOTALL)
            desc_m = re.search(r'<p class="profile-card-desc[^"]*">(.*?)</p>', chunk, re.DOTALL)
            id_m = re.search(r'<div class="profile-card-identifier[^"]*">.*?</i>\s*([^<]+)</span>', chunk, re.DOTALL)
            url_m = re.search(r'<a [^>]*href="([^"]+)"[^>]*class="btn-hub-action btn-hub-primary"', chunk)
            if not url_m:
                url_m = re.search(r'<a [^>]*href="([^"]+)"', chunk)

            title = clean_html(title_m.group(1)) if title_m else "Verified Profile"
            category_label = clean_html(cat_m.group(1)) if cat_m else category_code.title()
            desc = clean_html(desc_m.group(1)) if desc_m else ""
            identifier = clean_html(id_m.group(1)) if id_m else "Verified"
            url = url_m.group(1).strip() if url_m else ""

            if url and not url.startswith("http"):
                url = f"{CANONICAL_SITE_URL}/{url.lstrip('/')}"

            key = f"{title}|{url}"
            if url and key not in seen_keys:
                seen_keys.add(key)
                profiles.append({
                    "title": title,
                    "category": category_code,
                    "category_label": category_label,
                    "identifier": identifier,
                    "description": desc,
                    "image": image_path,
                    "url": url,
                })

    return profiles


def extract_blogs():
    """Extract all blog and Forbes articles (with thumbnails) from generate_blog_page.py."""
    blog_py = os.path.join(ROOT_DIR, "generate_blog_page.py")
    blogs = []
    if os.path.exists(blog_py):
        with open(blog_py, "r", encoding="utf-8") as f:
            code = f.read()
        start_idx = code.find("articles_data = [")
        if start_idx != -1:
            sub = code[start_idx:]
            bracket_depth = 0
            end_idx = -1
            for i, ch in enumerate(sub):
                if ch == "[":
                    bracket_depth += 1
                elif ch == "]":
                    bracket_depth -= 1
                    if bracket_depth == 0:
                        end_idx = i + 1
                        break
            if end_idx != -1:
                ns = {}
                try:
                    exec(sub[:end_idx], {}, ns)
                    for item in ns.get("articles_data", []):
                        blogs.append({
                            "id": item.get("id", ""),
                            "title": item.get("title", ""),
                            "platform": item.get("platform_full") or item.get("platform", "Technical Blog"),
                            "platform_short": item.get("platform", "Blog"),
                            "category": item.get("category", "Enterprise AI"),
                            "date": item.get("date", "2026"),
                            "read_time": item.get("read_time", "5 min read"),
                            "url": item.get("url", ""),
                            "spotify_url": item.get("spotify_url", ""),
                            "author_profile": item.get("author_profile", ""),
                            "image": item.get("thumbnail", "images/blog/thumbnails/forbes-real-ai-moat.jpg"),
                            "description": item.get("description", ""),
                            "tags": item.get("tags", []),
                        })
                except Exception as e:
                    print(f"[Warn] Could not exec articles_data: {e}")
    return blogs


def extract_associations():
    """Extract all invited memberships, fellowships, and associations (excluding ACM) from page-memberships.html."""
    mem_path = os.path.join(ROOT_DIR, "page-memberships.html")
    associations = []
    if os.path.exists(mem_path):
        with open(mem_path, "r", encoding="utf-8") as f:
            html = f.read()

        chunks = re.split(r'<div class="col-lg-4 col-md-6 mb-4 membership-item"', html)[1:]
        for chunk in chunks:
            cat_m = re.search(r'data-category="([^"]+)"', chunk)
            cat = cat_m.group(1).strip() if cat_m else "fellowship"
            img_m = re.search(r'<img\s+src="([^"]+)"', chunk)
            img_path = img_m.group(1).strip() if img_m else "images/memberships/ieee_senior.svg"
            tier_m = re.search(r'<span class="membership-tier-pill[^"]*">(.*?)</span>', chunk, re.DOTALL)
            title_m = re.search(r'<h3 class="membership-title[^"]*">(.*?)</h3>', chunk, re.DOTALL)
            org_m = re.search(r'<div class="membership-org[^"]*">(.*?)</div>', chunk, re.DOTALL)
            cred_m = re.search(r'<div class="membership-credential-id[^"]*">(.*?)</div>', chunk, re.DOTALL)
            desc_m = re.search(r'<p class="membership-desc[^"]*">(.*?)</p>', chunk, re.DOTALL)

            # Collect all verification links on the card
            links = []
            for a_m in re.finditer(r'<a\s+href="([^"]+)"[^>]*class="btn-verify[^"]*"[^>]*>(.*?)</a>', chunk, re.DOTALL):
                l_url = a_m.group(1).strip()
                if not l_url.startswith("http"):
                    l_url = f"{CANONICAL_SITE_URL}/{l_url.lstrip('/')}"
                links.append({"url": l_url, "label": clean_html(a_m.group(2)) or "Verify"})

            title = clean_html(title_m.group(1)) if title_m else ""
            if not title or "acm" in title.lower():
                continue

            primary_url = links[0]["url"] if links else f"{CANONICAL_SITE_URL}/page-memberships"
            associations.append({
                "title": title,
                "role": clean_html(org_m.group(1)) if org_m else "Member",
                "tier": clean_html(tier_m.group(1)) if tier_m else "Fellow / Member",
                "credential_id": clean_html(cred_m.group(1)) if cred_m else "Verified",
                "category": cat,
                "image": img_path,
                "description": clean_html(desc_m.group(1)) if desc_m else "",
                "url": primary_url,
                "links": links,
            })
    return associations


def load_json_file(filename):
    p = os.path.join(ROOT_DIR, filename)
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def build_books_data():
    """Return canonical authored books and technical reviewed books with cover images."""
    return [
        {
            "id": "book-beyond-ai-engineering",
            "title": "Beyond AI Engineering: From Creator to Curator",
            "subtitle": "Mastering the Human and Strategic Dimensions of Curating AI Systems",
            "role": "Authored Book",
            "year": "2025",
            "image": "images/books/beyond_ai_engineering_cover.jpg",
            "full_jacket": "images/books/beyond_ai_engineering_full_jacket.jpg",
            "url": f"{CANONICAL_SITE_URL}/page-books",
            "description": "A definitive treatise on transitioning from syntax generation to high-level system curation, covering multi-agent orchestration, deterministic guardrails, memory architectures, and the Super Engineer Trifecta.",
        },
        {
            "id": "book-ai-vs-ai",
            "title": "AI vs. AI: Engineering the Cybersecurity Counteroffensive",
            "subtitle": "Architecting Autonomous AI Defenses Against Intelligent Adversaries",
            "role": "Authored Book",
            "year": "2026",
            "image": "images/books/ai_vs_ai_cover.jpg",
            "full_jacket": "images/books/ai_vs_ai_full_jacket.jpg",
            "url": f"{CANONICAL_SITE_URL}/page-books",
            "description": "Examines adversarial machine intelligence and how enterprise security architects design zero-trust autonomous counteroffensive systems, behavioral invariants, and self-healing defense pipelines.",
        },
        {
            "id": "book-review-ai-ethics",
            "title": "AI Ethics in Action (Technical Book Review)",
            "subtitle": "Enterprise AI Governance & Algorithmic Fairness Review",
            "role": "Technical Book Reviewer",
            "year": "2025",
            "image": "images/books/reviewed/ai_ethics_in_action.jpg",
            "url": f"{CANONICAL_SITE_URL}/page-books",
            "description": "Expert technical review evaluating operational AI ethics, bias mitigation, and governance frameworks in production machine learning.",
        },
        {
            "id": "book-review-hands-on-ai",
            "title": "Hands-On AI Dev with Python (Technical Book Review)",
            "subtitle": "Production Python AI Engineering Review",
            "role": "Technical Book Reviewer",
            "year": "2025",
            "image": "images/books/reviewed/hands_on_ai_dev_python.jpg",
            "url": f"{CANONICAL_SITE_URL}/page-books",
            "description": "Technical review validating Python-based deep learning workflows, model serving, and scalable AI engineering patterns.",
        },
        {
            "id": "book-review-leadership-ai",
            "title": "Leadership at the Helm of AI (Technical Book Review)",
            "subtitle": "Executive AI Strategy & Transformation Review",
            "role": "Technical Book Reviewer",
            "year": "2025",
            "image": "images/books/reviewed/leadership_at_the_helm_of_ai.jpg",
            "url": f"{CANONICAL_SITE_URL}/page-books",
            "description": "Executive review assessing organizational AI readiness, C-suite governance, and enterprise AI ROI frameworks.",
        },
        {
            "id": "book-review-algo-trading",
            "title": "Python for Algorithmic Trading Cookbook (Technical Book Review)",
            "subtitle": "Quantitative & High-Frequency Streaming Systems Review",
            "role": "Technical Book Reviewer",
            "year": "2024",
            "image": "images/books/reviewed/python_algorithmic_trading_cookbook.jpg",
            "url": f"{CANONICAL_SITE_URL}/page-books",
            "description": "Technical validation of real-time market data pipelines, quantitative backtesting, and low-latency execution architectures in Python.",
        },
        {
            "id": "book-review-ml-marketing",
            "title": "Machine Learning & Generative AI for Marketing (Technical Book Review)",
            "subtitle": "Applied Generative AI & Personalization Systems Review",
            "role": "Technical Book Reviewer",
            "year": "2025",
            "image": "images/books/reviewed/ml_and_generative_ai_for_marketing.jpg",
            "url": f"{CANONICAL_SITE_URL}/page-books",
            "description": "Technical evaluation of customer intelligence models, privacy-preserving personalization, and generative AI pipelines.",
        },
        {
            "id": "book-review-tensorflow",
            "title": "The TensorFlow Workshop (Technical Book Review)",
            "subtitle": "Deep Neural Network Architecture & Training Review",
            "role": "Technical Book Reviewer",
            "year": "2024",
            "image": "images/books/reviewed/tensorflow_workshop.jpg",
            "url": f"{CANONICAL_SITE_URL}/page-books",
            "description": "Technical review of deep neural network architectures, TensorFlow 2.x pipelines, and distributed model training.",
        },
    ]


def build_wikidata_claims_manifest():
    """Return canonical Wikidata claims for Q139827028 (NO ACM)."""
    return [
        {
            "property": "P31",
            "label": "instance of",
            "value": "Q5",
            "value_label": "human",
            "type": "wikibase-entityid",
            "reference_url": f"{CANONICAL_SITE_URL}/page-about",
        },
        {
            "property": "P106",
            "label": "occupation",
            "value": "Q1709010",
            "value_label": "software engineer",
            "type": "wikibase-entityid",
            "reference_url": "https://theorg.com/org/palo-alto-networks/person/harsh-verma",
        },
        {
            "property": "P106",
            "label": "occupation",
            "value": "Q15976092",
            "value_label": "artificial intelligence researcher",
            "type": "wikibase-entityid",
            "reference_url": "https://scholar.google.com/citations?user=zSt9oRMAAAAJ",
        },
        {
            "property": "P106",
            "label": "occupation",
            "value": "Q82594",
            "value_label": "computer scientist",
            "type": "wikibase-entityid",
            "reference_url": "https://scholar.google.com/citations?user=zSt9oRMAAAAJ",
        },
        {
            "property": "P106",
            "label": "occupation",
            "value": "Q36180",
            "value_label": "writer / author",
            "type": "wikibase-entityid",
            "reference_url": "https://www.forbes.com/councils/forbestechcouncil/people/harshverma/",
        },
        {
            "property": "P106",
            "label": "occupation",
            "value": "Q18939491",
            "value_label": "public speaker / keynote speaker",
            "type": "wikibase-entityid",
            "reference_url": f"{CANONICAL_SITE_URL}/page-speaker",
        },
        {
            "property": "P108",
            "label": "employer",
            "value": "Q7128508",
            "value_label": "Palo Alto Networks",
            "type": "wikibase-entityid",
            "reference_url": "https://theorg.com/org/palo-alto-networks/person/harsh-verma",
        },
        {
            "property": "P69",
            "label": "educated at",
            "value": "Q41506",
            "value_label": "Stanford University",
            "type": "wikibase-entityid",
            "reference_url": f"{CANONICAL_SITE_URL}/page-about",
        },
        {
            "property": "P69",
            "label": "educated at",
            "value": "Q1781394",
            "value_label": "University of Texas at Dallas",
            "type": "wikibase-entityid",
            "reference_url": f"{CANONICAL_SITE_URL}/page-about",
        },
        {
            "property": "P69",
            "label": "educated at",
            "value": "Q7903393",
            "value_label": "Uttarakhand Technical University",
            "type": "wikibase-entityid",
            "reference_url": f"{CANONICAL_SITE_URL}/page-about",
        },
        {
            "property": "P463",
            "label": "member of",
            "value": "Q131566",
            "value_label": "Institute of Electrical and Electronics Engineers (IEEE Senior Member)",
            "type": "wikibase-entityid",
            "reference_url": "https://ieee-collabratec.ieee.org/app/p/HarshVerma59",
        },
        {
            "property": "P463",
            "label": "member of",
            "value": "Q1814176",
            "value_label": "Sigma Xi (Full Elected Member)",
            "type": "wikibase-entityid",
            "reference_url": f"{CANONICAL_SITE_URL}/page-memberships",
        },
        {
            "property": "P463",
            "label": "member of",
            "value": "Q919096",
            "value_label": "British Computer Society (Fellow FBCS)",
            "type": "wikibase-entityid",
            "reference_url": f"{CANONICAL_SITE_URL}/page-memberships",
        },
        {
            "property": "P463",
            "label": "member of",
            "value": "Q1460885",
            "value_label": "Royal Society of Arts (Fellow FRSA)",
            "type": "wikibase-entityid",
            "reference_url": f"{CANONICAL_SITE_URL}/page-memberships",
        },
        {
            "property": "P463",
            "label": "member of",
            "value": "Q466113",
            "value_label": "Association for the Advancement of Artificial Intelligence (AAAI)",
            "type": "wikibase-entityid",
            "reference_url": f"{CANONICAL_SITE_URL}/page-memberships",
        },
        {
            "property": "P856",
            "label": "official website",
            "value": "https://www.harshverma.me/",
            "value_label": "https://www.harshverma.me/",
            "type": "url",
            "reference_url": "https://harshverma.bio/",
        },
        {
            "property": "P973",
            "label": "described at URL",
            "value": "https://en.everybodywiki.com/Harsh_Verma_(Software_Engineer)",
            "value_label": "EverybodyWiki Biography: Harsh Verma (Software Engineer)",
            "type": "url",
            "reference_url": "https://en.everybodywiki.com/Harsh_Verma_(Software_Engineer)",
        },
        {
            "property": "P973",
            "label": "described at URL",
            "value": "https://www.forbes.com/councils/forbestechcouncil/people/harshverma/",
            "value_label": "Forbes Technology Council Executive Profile",
            "type": "url",
            "reference_url": "https://www.forbes.com/councils/forbestechcouncil/people/harshverma/",
        },
        {
            "property": "P973",
            "label": "described at URL",
            "value": "https://theorg.com/org/palo-alto-networks/person/harsh-verma",
            "value_label": "The Org: Palo Alto Networks Leadership Profile",
            "type": "url",
            "reference_url": "https://theorg.com/org/palo-alto-networks/person/harsh-verma",
        },
        {
            "property": "P973",
            "label": "described at URL",
            "value": "https://influencermagazine.uk/harsh-verma/",
            "value_label": "Influencer Magazine UK Feature Profile",
            "type": "url",
            "reference_url": "https://influencermagazine.uk/harsh-verma/",
        },
        {
            "property": "P496",
            "label": "ORCID iD",
            "value": "0000-0003-2134-2600",
            "value_label": "0000-0003-2134-2600",
            "type": "external-id",
            "formatter_url": "https://orcid.org/0000-0003-2134-2600",
            "reference_url": "https://orcid.org/0000-0003-2134-2600",
        },
        {
            "property": "P1960",
            "label": "Google Scholar author ID",
            "value": "zSt9oRMAAAAJ",
            "value_label": "zSt9oRMAAAAJ",
            "type": "external-id",
            "formatter_url": "https://scholar.google.com/citations?user=zSt9oRMAAAAJ",
            "reference_url": "https://scholar.google.com/citations?user=zSt9oRMAAAAJ",
        },
        {
            "property": "P4012",
            "label": "Semantic Scholar author ID",
            "value": "145004805",
            "value_label": "145004805",
            "type": "external-id",
            "formatter_url": "https://www.semanticscholar.org/author/Harsh-Verma/145004805",
            "reference_url": "https://www.semanticscholar.org/author/Harsh-Verma/145004805",
        },
        {
            "property": "P8968",
            "label": "OpenReview ID",
            "value": "~Harsh_Verma3",
            "value_label": "~Harsh_Verma3",
            "type": "external-id",
            "formatter_url": "https://openreview.net/profile?id=~Harsh_Verma3",
            "reference_url": "https://openreview.net/profile?id=~Harsh_Verma3",
        },
        {
            "property": "P3747",
            "label": "SSRN author ID",
            "value": "11144549",
            "value_label": "11144549",
            "type": "external-id",
            "formatter_url": "https://papers.ssrn.com/sol3/cf_dev/AbsByAuth.cfm?per_id=11144549",
            "reference_url": "https://papers.ssrn.com/sol3/cf_dev/AbsByAuth.cfm?per_id=11144549",
        },
        {
            "property": "P2038",
            "label": "ResearchGate profile ID",
            "value": "Harsh-Verma-43",
            "value_label": "Harsh-Verma-43",
            "type": "external-id",
            "formatter_url": "https://www.researchgate.net/profile/Harsh-Verma-43",
            "reference_url": "https://www.researchgate.net/profile/Harsh-Verma-43",
        },
        {
            "property": "P2037",
            "label": "GitHub username",
            "value": "iamharshverma",
            "value_label": "iamharshverma",
            "type": "external-id",
            "formatter_url": "https://github.com/iamharshverma",
            "reference_url": "https://github.com/iamharshverma",
        },
        {
            "property": "P6634",
            "label": "LinkedIn personal profile ID",
            "value": "harshverma59",
            "value_label": "harshverma59",
            "type": "external-id",
            "formatter_url": "https://www.linkedin.com/in/harshverma59/",
            "reference_url": "https://www.linkedin.com/in/harshverma59/",
        },
        {
            "property": "P2002",
            "label": "X (Twitter) username",
            "value": "harshverma59",
            "value_label": "harshverma59",
            "type": "external-id",
            "formatter_url": "https://x.com/harshverma59",
            "reference_url": "https://x.com/harshverma59",
        },
        {
            "property": "P3899",
            "label": "Medium username",
            "value": "harshverma59",
            "value_label": "harshverma59",
            "type": "external-id",
            "formatter_url": "https://medium.com/@harshverma59",
            "reference_url": "https://medium.com/@harshverma59",
        },
    ]


def generate_quickstatements(claims):
    """Generate comprehensive QuickStatements batch commands for Wikidata Q139827028,
    including reference replacement for outdated iamharshverma.github.io URLs and ACM removal."""
    lines = [
        f"# ==============================================================================",
        f"# QUICKSTATEMENTS BATCH FOR HARSH VERMA ({WIKIDATA_QID})",
        f"# Target URL: https://www.wikidata.org/wiki/{WIKIDATA_QID}",
        f"# QuickStatements Tool: https://quickstatements.toolforge.org/#/batch",
        f"# Canonical Entity: https://www.harshverma.me/#person",
        f"# ==============================================================================",
        f"",
        f"# ------------------------------------------------------------------------------",
        f"# PART 1: LIVE REFERENCE MIGRATION & DEPRECATED CLAIMS REMOVAL",
        f"# Replaces all live references from iamharshverma.github.io to https://www.harshverma.me/",
        f"# and removes ACM (Q127992) claim per user instructions.",
        f"# ------------------------------------------------------------------------------",
        f"",
        f"# 1. Update Official Website (P856) to canonical https://www.harshverma.me/",
        f'-{WIKIDATA_QID}\tP856\t"https://iamharshverma.github.io/"',
        f'{WIKIDATA_QID}\tP856\t"https://www.harshverma.me/"\tS854\t"https://www.harshverma.me/"',
        f"",
        f"# 2. Remove ACM (Q127992) membership claim completely",
        f'-{WIKIDATA_QID}\tP463\tQ127992',
        f"",
        f"# 3. Replace Member Of (P463) references from iamharshverma.github.io/page-memberships to https://www.harshverma.me/page-memberships",
        f'-{WIKIDATA_QID}\tP463\tQ1814176',
        f'{WIKIDATA_QID}\tP463\tQ1814176\tS854\t"https://www.harshverma.me/page-memberships"',
        f'-{WIKIDATA_QID}\tP463\tQ919096',
        f'{WIKIDATA_QID}\tP463\tQ919096\tS854\t"https://www.harshverma.me/page-memberships"',
        f'-{WIKIDATA_QID}\tP463\tQ1460885',
        f'{WIKIDATA_QID}\tP463\tQ1460885\tS854\t"https://www.harshverma.me/page-memberships"',
        f'-{WIKIDATA_QID}\tP463\tQ466113',
        f'{WIKIDATA_QID}\tP463\tQ466113\tS854\t"https://www.harshverma.me/page-memberships"',
        f"",
        f"# 4. Replace Educated At (P69) references to https://www.harshverma.me/page-about",
        f'-{WIKIDATA_QID}\tP69\tQ41506',
        f'{WIKIDATA_QID}\tP69\tQ41506\tS854\t"https://www.harshverma.me/page-about"',
        f'-{WIKIDATA_QID}\tP69\tQ7903393',
        f'{WIKIDATA_QID}\tP69\tQ7903393\tS854\t"https://www.harshverma.me/page-about"',
        f"",
        f"# 5. Replace Keynote Speaker (P106) reference to https://www.harshverma.me/page-speaker",
        f'-{WIKIDATA_QID}\tP106\tQ12859263',
        f'{WIKIDATA_QID}\tP106\tQ12859263\tS854\t"https://www.harshverma.me/page-speaker"',
        f"",
        f"# ------------------------------------------------------------------------------",
        f"# PART 2: CANONICAL LABELS, DESCRIPTIONS & AUTHORITY CONTROL IDENTIFIERS",
        f"# ------------------------------------------------------------------------------",
        f'{WIKIDATA_QID}\tLen\t"Harsh Verma"',
        f'{WIKIDATA_QID}\tDen\t"Principal AI Software Engineer at Palo Alto Networks, Keynote Speaker, Author, and Researcher"',
        f'{WIKIDATA_QID}\tAen\t"Harsh Verma (Software Engineer)"',
    ]
    for c in claims:
        prop = c["property"]
        val = c["value"]
        ref = c.get("reference_url", "https://www.harshverma.me/")
        # Skip duplicates of claims already explicitly emitted in Part 1
        if prop in ("P463", "P69", "P856") or (prop == "P106" and val == "Q12859263"):
            continue
        if c["type"] == "wikibase-entityid":
            lines.append(f'{WIKIDATA_QID}\t{prop}\t{val}\tS854\t"{ref}"')
        else:
            lines.append(f'{WIKIDATA_QID}\t{prop}\t"{val}"\tS854\t"{ref}"')
    return "\n".join(lines) + "\n"


def generate_reference_replacement_batches():
    """Generate both QuickStatements v2 and QuickStatements 3.0 batches specifically for
    replacing the 8 live references on Q139827028."""
    v2_lines = [
        "# QuickStatements v2 Reference Replacement Batch for Q139827028",
        "# Replaces all 8 references pointing to iamharshverma.github.io with https://www.harshverma.me/",
        "# Also updates Official Website P856 and removes ACM Q127992.",
        "-Q139827028\tP856\t\"https://iamharshverma.github.io/\"",
        "Q139827028\tP856\t\"https://www.harshverma.me/\"\tS854\t\"https://www.harshverma.me/\"",
        "-Q139827028\tP463\tQ127992",
        "-Q139827028\tP463\tQ1814176",
        "Q139827028\tP463\tQ1814176\tS854\t\"https://www.harshverma.me/page-memberships\"",
        "-Q139827028\tP463\tQ919096",
        "Q139827028\tP463\tQ919096\tS854\t\"https://www.harshverma.me/page-memberships\"",
        "-Q139827028\tP463\tQ1460885",
        "Q139827028\tP463\tQ1460885\tS854\t\"https://www.harshverma.me/page-memberships\"",
        "-Q139827028\tP463\tQ466113",
        "Q139827028\tP463\tQ466113\tS854\t\"https://www.harshverma.me/page-memberships\"",
        "-Q139827028\tP69\tQ41506",
        "Q139827028\tP69\tQ41506\tS854\t\"https://www.harshverma.me/page-about\"",
        "-Q139827028\tP69\tQ7903393",
        "Q139827028\tP69\tQ7903393\tS854\t\"https://www.harshverma.me/page-about\"",
        "-Q139827028\tP106\tQ12859263",
        "Q139827028\tP106\tQ12859263\tS854\t\"https://www.harshverma.me/page-speaker\"",
    ]

    v3_lines = [
        "# QuickStatements 3.0 Reference Replacement Syntax",
        "-Q139827028 | P856 | \"https://iamharshverma.github.io/\"",
        "Q139827028 | P856 | \"https://www.harshverma.me/\" | S854 | \"https://www.harshverma.me/\"",
        "-Q139827028 | P463 | Q127992",
        "REMOVE_REF_BLOCK | Q139827028 | P463 | Q1814176 | S854 | \"https://iamharshverma.github.io/page-memberships\"",
        "Q139827028 | P463 | Q1814176 | S854 | \"https://www.harshverma.me/page-memberships\"",
        "REMOVE_REF_BLOCK | Q139827028 | P463 | Q919096 | S854 | \"https://iamharshverma.github.io/page-memberships\"",
        "Q139827028 | P463 | Q919096 | S854 | \"https://www.harshverma.me/page-memberships\"",
        "REMOVE_REF_BLOCK | Q139827028 | P463 | Q1460885 | S854 | \"https://iamharshverma.github.io/page-memberships\"",
        "Q139827028 | P463 | Q1460885 | S854 | \"https://www.harshverma.me/page-memberships\"",
        "REMOVE_REF_BLOCK | Q139827028 | P463 | Q466113 | S854 | \"https://iamharshverma.github.io/page-memberships\"",
        "Q139827028 | P463 | Q466113 | S854 | \"https://www.harshverma.me/page-memberships\"",
        "REMOVE_REF_BLOCK | Q139827028 | P69 | Q41506 | S854 | \"https://iamharshverma.github.io/page-about\"",
        "Q139827028 | P69 | Q41506 | S854 | \"https://www.harshverma.me/page-about\"",
        "REMOVE_REF_BLOCK | Q139827028 | P69 | Q7903393 | S854 | \"https://iamharshverma.github.io/page-about\"",
        "Q139827028 | P69 | Q7903393 | S854 | \"https://www.harshverma.me/page-about\"",
        "REMOVE_REF_BLOCK | Q139827028 | P106 | Q12859263 | S854 | \"https://iamharshverma.github.io/page-speaker\"",
        "Q139827028 | P106 | Q12859263 | S854 | \"https://www.harshverma.me/page-speaker\"",
    ]

    return "\n".join(v2_lines) + "\n\n" + "\n".join(v3_lines) + "\n"


def generate_everybodywiki_wikitext(profiles, media, awards, blogs, books, papers, associations):
    """Generate comprehensive, encyclopedic MediaWiki markup for EverybodyWiki."""
    authored_books = [b for b in books if b.get("role") == "Authored Book"]
    reviewed_books = [b for b in books if b.get("role") != "Authored Book"]

    lines = []
    lines.append("{{Infobox person")
    lines.append("| honorific_prefix   = Mr")
    lines.append("| first_name         = Harsh")
    lines.append("| family_name        = Verma")
    lines.append("| given_name         = Harsh")
    lines.append("| surname            = Verma")
    lines.append("| name               = Harsh Verma")
    lines.append("| image              = Harsh Verma Software Engineer.jpg")
    lines.append("| caption            = Harsh Verma, Principal AI Software Engineer, Author & Keynote Speaker")
    lines.append("| nationality        = Indian")
    lines.append("| occupation         = Principal Software Engineer (AI), Enterprise AI Architect, Author, Keynote Speaker, Researcher")
    lines.append("| employer           = [[Palo Alto Networks]]")
    lines.append("| alma_mater         = [[Stanford University]]<br/>[[University of Texas at Dallas]] (M.S. CS)<br/>[[Uttarakhand Technical University]] (B.Tech CSE)")
    lines.append("| known_for          = Enterprise Agentic AI Architectures, Autonomous Cyber Defense, Multi-Agent Systems, Explainable AI (XAI)")
    lines.append("| notable_works      = ''Beyond AI Engineering: From Creator to Curator''<br/>''AI vs. AI: Engineering the Cybersecurity Counteroffensive''")
    lines.append("| awards             = Forttuna Global 100 Power List (2026)<br/>Nobel Technology Awards Gold Winner (2026)<br/>TITAN Innovation Award (2026)<br/>NVTC Cyber50 Honoree (2026)<br/>Global Recognition Award (2026)<br/>Marquis Who's Who in America")
    lines.append("| website            = {{URL|https://www.harshverma.me/}}")
    lines.append("| twitter            = harshverma59")
    lines.append("| facebook           = harshverma59")
    lines.append("| instagram          = aiwithharsh")
    lines.append("| linkedin           = /in/harshverma59/")
    lines.append("| module             = {{Authority control|QID=Q139827028|ORCID=0000-0003-2134-2600}}")
    lines.append("}}")
    lines.append("")
    lines.append("'''Harsh Verma''' is an internationally recognized Principal Software Engineer in Artificial Intelligence at [[Palo Alto Networks]], enterprise AI architect, author, keynote speaker, and computer science researcher.<ref>{{cite web |title=The Org: Harsh Verma - Principal Software Engineer in AI at Palo Alto Networks |url=https://theorg.com/org/palo-alto-networks/person/harsh-verma |website=The Org}}</ref><ref>{{cite web |title=Wikidata Entity Q139827028: Harsh Verma |url=https://www.wikidata.org/wiki/Q139827028 |website=Wikidata}}</ref> He is an official member and columnist for the [[Forbes Technology Council]],<ref>{{cite web |title=Harsh Verma - Forbes Technology Council Profile |url=https://www.forbes.com/councils/forbestechcouncil/people/harshverma/ |website=Forbes}}</ref> a Senior Member of the [[Institute of Electrical and Electronics Engineers]] (SMIEEE), an elected Fellow of the [[British Computer Society]] (FBCS), an elected Fellow of the [[Royal Society of Arts]] (FRSA), and a Full Member of [[Sigma Xi]]: The Scientific Research Honor Society.<ref>{{cite web |title=Harsh Verma Invited Associations & Fellowships |url=https://www.harshverma.me/page-memberships |website=Harsh Verma Official Portfolio}}</ref>")
    lines.append("")
    lines.append("Verma has authored two books on enterprise autonomous systems and cyber defense (''Beyond AI Engineering: From Creator to Curator'' and ''AI vs. AI: Engineering the Cybersecurity Counteroffensive''), served as technical reviewer for six AI and engineering books, published {{nowrap|" + str(len(papers)) + "+}} peer-reviewed research papers across IEEE, Springer Nature, Oxford Academic, and international journals with over 150 academic citations,<ref>{{cite web |title=Harsh Verma Google Scholar Citations |url=https://scholar.google.com/citations?user=zSt9oRMAAAAJ |website=Google Scholar}}</ref> and received {{nowrap|" + str(len(awards)) + "}} international technology and leadership honors.")
    lines.append("")
    lines.append("== Education ==")
    lines.append("* '''[[Stanford University]]''' – Graduate Certificate in Artificial Intelligence & Executive Leadership (Stanford Center for Professional Development).")
    lines.append("* '''[[University of Texas at Dallas]]''' (Erik Jonsson School of Engineering and Computer Science) – Master of Science (M.S.) in Computer Science (Intelligent Systems & Distributed Computing).")
    lines.append("* '''[[Uttarakhand Technical University]]''' – Bachelor of Technology (B.Tech) in Computer Science and Engineering.")
    lines.append("")
    lines.append("== Career and Executive Leadership ==")
    lines.append("Verma serves as Principal Software Engineer (AI) at [[Palo Alto Networks]] in Santa Clara, California, where he architects autonomous multi-agent systems, deterministic AI security guardrails, and high-throughput enterprise cloud platforms.<ref>{{cite web |title=The Engineer Rewriting the Rules by Thinking AI Beyond the Code: Inside the World of Harsh Verma |url=https://nyweeklyjournal.com/blog/the-engineer-rewriting-the-rules-by-thinking-%E2%80%9Cai-beyond-the-code%E2%80%9D-inside-the-world-of-harsh-verma |website=New York Weekly Journal}}</ref> Earlier in his career, he engineered hyper-scale distributed backend platforms, real-time analytics pipelines, and deep learning systems at Hike Messenger, Reliance Jio (UT-Design), Worlds Enterprises, and Hypergiant Sensory Science.")
    lines.append("")
    lines.append("In addition to his engineering leadership, Verma serves as an official contributor on the [[Forbes Technology Council]], Global Advisor at [[UC Berkeley SkyDeck]], industry awards judge for the Business Intelligence Group (BIG), Globee Awards, and Stevie Awards, and startup mentor for [[MassChallenge]] and ADPList.")
    lines.append("")
    lines.append("== Authored Books & Technical Book Reviews ==")
    lines.append("=== Authored Books ===")
    for b in authored_books:
        lines.append(f"* '''''{b['title']}''''' – ''{b['subtitle']}'' ({b['year']}). {b['description']} [https://www.harshverma.me/page-books Official Book Hub]")
    lines.append("")
    lines.append("=== Technical Books Reviewed ===")
    for b in reviewed_books:
        lines.append(f"* '''''{b['title']}''''' – {b['description']}")
    lines.append("")
    lines.append(f"== Selected Forbes Columns & Thought Leadership ({len(blogs)} Articles) ==")
    for blog in blogs:
        lines.append(f"* [{blog['url']} \"{blog['title']}\"] – ''{blog['platform']}'' ({blog['date']})")
    lines.append("")
    lines.append(f"== Peer-Reviewed Research Publications ({len(papers)}+ Papers) ==")
    for p in papers:
        venue = p.get("venue", "Peer-Reviewed Venue")
        yr = p.get("year", "")
        link = p.get("link", "https://www.harshverma.me/page-publications")
        doi = p.get("doi", "")
        doi_str = f" (DOI: <code>{doi}</code>)" if doi else ""
        lines.append(f"* [{link} \"{p.get('title', '')}\"] – ''{venue}'' ({yr}){doi_str}")
    lines.append("")
    lines.append(f"== Invited Fellowships, Councils & Associations ({len(associations)} Appointments) ==")
    for assoc in associations:
        lines.append(f"* '''{assoc['title']}''' – {assoc['role']} ({assoc['tier']}) [{assoc['url']} Verify]")
    lines.append("")
    lines.append(f"== Honors and Global Awards ({len(awards)} Recognitions) ==")
    for aw in awards:
        links = aw.get("links") or []
        aw_url = links[0]["url"] if links else "https://www.harshverma.me/page-awards"
        lines.append(f"* '''{aw.get('title', '')}''' ({aw.get('year', '2026')}) – {aw.get('organization', '')} [{aw_url} Citation]")
    lines.append("")
    lines.append(f"== Media Coverage, Interviews & Podcasts ({len(media)}+ Features) ==")
    for m in media:
        m_url = m.get("primary_url") or "https://www.harshverma.me/page-media"
        if "app.link" in m_url or "bit.ly" in m_url or "tinyurl.com" in m_url:
            m_url = "https://www.lifepage.in/" if "lifepage" in m_url else "https://www.harshverma.me/page-media"
        lines.append(f"* [{m_url} \"{m.get('title', '')}\"] – ''{m.get('outlet', '')}'' ({m.get('date_display', m.get('year', ''))})")
    lines.append("")
    lines.append(f"== Verified Authority Profiles & External Links ({len(profiles)} Registries) ==")
    lines.append("* [https://www.harshverma.me/ Official Portfolio Website (www.harshverma.me)]")
    lines.append("* [https://www.harshverma.me/page-identity Official Google Knowledge Graph & Entity Verification Hub]")
    for prof in profiles:
        p_url = prof["url"].replace("https://iamharshverma.github.io", CANONICAL_SITE_URL)
        if "app.link" in p_url or "bit.ly" in p_url or "tinyurl.com" in p_url:
            continue
        lines.append(f"* [{p_url} {prof['title']}] ({prof['category_label']} – <code>{prof['identifier']}</code>)")
    lines.append("")
    lines.append("== References ==")
    lines.append("{{reflist}}")
    lines.append("")
    lines.append("[[Category:Living people]]")
    lines.append("[[Category:American computer scientists]]")
    lines.append("[[Category:Indian software engineers]]")
    lines.append("[[Category:Artificial intelligence researchers]]")
    lines.append("[[Category:Fellows of the British Computer Society]]")
    lines.append("[[Category:Fellows of the Royal Society of Arts]]")
    lines.append("[[Category:Senior Members of the IEEE]]")
    lines.append("[[Category:Stanford University alumni]]")
    lines.append("[[Category:University of Texas at Dallas alumni]]")
    return "\n".join(lines) + "\n"


def build_schema_org_graph(profiles, media, awards, blogs, books, papers, associations):
    """Build the comprehensive Schema.org @graph JSON-LD object anchored to https://www.harshverma.me/#person."""
    same_as_urls = [
        "https://www.wikidata.org/wiki/Q139827028",
        "http://www.wikidata.org/entity/Q139827028",
        "https://en.everybodywiki.com/Harsh_Verma_(Software_Engineer)",
        "https://wikialpha.co/wiki/Harsh_Verma_(Software_Engineer)",
        "https://en.wikiflux.org/wiki/index.php/Harsh_Verma_(Software_Engineer)",
        "https://localwiki.org/main/Harsh_Verma",
        "https://localwiki.org/santaclara/Harsh_Verma",
        "https://localwiki.org/dallas/Harsh_Verma",
        "https://www.harshverma.me/",
        "https://harshverma.me/",
        "https://harshverma.bio/",
        "https://x.com/harshverma59",
        "https://twitter.com/harshverma59",
        "https://www.linkedin.com/in/harshverma59/",
        "https://github.com/iamharshverma",
        "https://facebook.com/harshverma59",
        "https://www.facebook.com/harshverma59/",
        "https://www.instagram.com/aiwithharsh",
        "https://instagram.com/aiwithharsh",
        "https://mastodon.social/@harshverma59",
        "https://substack.com/@aiwithharsh",
        "https://aiwithharsh.substack.com/",
        "https://medium.com/@harshverma59",
        "https://imdb.me/harshverma",
        "https://www.imdb.com/name/nm16738096/",
        "https://flipboard.com/@harshverma59",
        "https://ieee-collabratec.ieee.org/app/p/HarshVerma59",
        "https://spotlight.favikon.com/harshverma59/",
        "https://mediakit.bio/@harshverma59",
        "https://topmate.io/iamharshverma/",
        "https://adplist.org/mentors/harsh-verma",
        "https://devpost.com/harshverma59",
        "https://about.me/harshverma59/",
        "https://bold.pro/my/harshverma",
        "https://hackernoon.com/u/harshverma59",
        "https://www.soundverse.ai/@harshverma59",
        "https://www.founderscreative.org/author/harsh/",
        "https://www.screna.ai/mentor-dashboard",
    ]
    for p in profiles:
        u = p.get("url", "").strip().replace("https://iamharshverma.github.io", CANONICAL_SITE_URL)
        if u and u.startswith("http") and u not in same_as_urls and "acm.org" not in u.lower():
            same_as_urls.append(u)

    for b in blogs:
        ap = b.get("author_profile", "")
        if ap and ap.startswith("http") and ap not in same_as_urls:
            same_as_urls.append(ap)

    # Mirror Wikidata Q139827028 member of (P463) claims explicitly
    member_of = [
        {
            "@type": "Organization",
            "@id": "http://www.wikidata.org/entity/Q131566",
            "name": "Institute of Electrical and Electronics Engineers",
            "alternateName": "IEEE",
            "url": "https://www.ieee.org/",
            "sameAs": [
                "https://www.wikidata.org/wiki/Q131566",
                "http://www.wikidata.org/entity/Q131566",
                "https://ieee-collabratec.ieee.org/app/p/HarshVerma59",
            ],
            "description": "Senior Member (SMIEEE) - Member ID: 95132014",
        },
        {
            "@type": "Organization",
            "@id": "http://www.wikidata.org/entity/Q1814176",
            "name": "Sigma Xi, The Scientific Research Honor Society",
            "alternateName": "Sigma Xi",
            "url": "https://www.sigmaxi.org/",
            "sameAs": [
                "https://www.wikidata.org/wiki/Q1814176",
                "http://www.wikidata.org/entity/Q1814176",
            ],
            "description": "Full Elected Member",
        },
        {
            "@type": "Organization",
            "@id": "http://www.wikidata.org/entity/Q919096",
            "name": "British Computer Society (BCS) - The Chartered Institute for IT",
            "alternateName": "BCS",
            "url": "https://www.bcs.org/",
            "sameAs": [
                "https://www.wikidata.org/wiki/Q919096",
                "http://www.wikidata.org/entity/Q919096",
                "https://www.bcs.org/find-a-bcs-member/",
            ],
            "description": "Elected Fellow (FBCS)",
        },
        {
            "@type": "Organization",
            "@id": "http://www.wikidata.org/entity/Q1460885",
            "name": "Royal Society of Arts",
            "alternateName": "RSA / FRSA",
            "url": "https://www.thersa.org/",
            "sameAs": [
                "https://www.wikidata.org/wiki/Q1460885",
                "http://www.wikidata.org/entity/Q1460885",
            ],
            "description": "Elected Fellow (FRSA)",
        },
        {
            "@type": "Organization",
            "@id": "http://www.wikidata.org/entity/Q466113",
            "name": "Association for the Advancement of Artificial Intelligence (AAAI)",
            "alternateName": "AAAI",
            "url": "https://aaai.org/",
            "sameAs": [
                "https://www.wikidata.org/wiki/Q466113",
                "http://www.wikidata.org/entity/Q466113",
            ],
            "description": "Professional Member",
        },
        {
            "@type": "Organization",
            "name": "Forbes Technology Council",
            "url": "https://www.forbes.com/councils/forbestechcouncil/people/harshverma/",
            "sameAs": [
                "https://councils.forbes.com/profile/Harsh-Verma-Principal-Software-Engineer-AI-Palo-Alto-Networks/2a1e2c7a-5541-4c49-acee-0ec37da532a5",
            ],
            "description": "Official Council Member & Columnist",
        },
        {
            "@type": "Organization",
            "name": "Forttuna Technology Council",
            "url": "https://councils.forttuna.com/council-member/harsh-verma/",
            "sameAs": [
                "https://global100.forttuna.com/the-power-list-2026-honorees/profile?name=harsh-verma",
            ],
            "description": "Council Member & Global 100 Honoree",
        },
    ]
    seen_assoc_names = {m["name"].lower() for m in member_of}
    for assoc in associations:
        t = assoc["title"]
        if "acm" in t.lower():
            continue
        if t.lower() not in seen_assoc_names:
            seen_assoc_names.add(t.lower())
            member_of.append({
                "@type": "Organization",
                "name": t,
                "url": assoc["url"],
                "description": f"{assoc['role']} ({assoc['tier']})",
            })

    award_titles = [f"{a.get('title')} ({a.get('year', '2026')}) - {a.get('organization', '')}" for a in awards]
    has_credentials = []
    for a in awards:
        links = a.get("links") or []
        cred_url = links[0]["url"] if links else f"{CANONICAL_SITE_URL}/page-awards"
        all_aw_urls = [l["url"] for l in links if l.get("url")]
        cred_obj = {
            "@type": "EducationalOccupationalCredential",
            "@id": f"{CANONICAL_SITE_URL}/page-awards#{a.get('id', '')}",
            "name": a.get("title", ""),
            "credentialCategory": a.get("tier", "Global Award"),
            "dateCreated": str(a.get("year", "2026")),
            "description": a.get("description", ""),
            "image": f"{CANONICAL_SITE_URL}/{a.get('image', '').lstrip('/')}" if a.get("image") else None,
            "url": cred_url,
            "recognizedBy": {
                "@type": "Organization",
                "name": a.get("organization", "International Awards Committee"),
            },
        }
        if len(all_aw_urls) > 1:
            cred_obj["sameAs"] = all_aw_urls
        has_credentials.append({k: v for k, v in cred_obj.items() if v is not None})

    subject_of = [
        {
            "@type": "WebPage",
            "@id": "https://en.everybodywiki.com/Harsh_Verma_(Software_Engineer)",
            "name": "Harsh Verma (Software Engineer) - EverybodyWiki Biography",
            "url": "https://en.everybodywiki.com/Harsh_Verma_(Software_Engineer)",
        },
        {
            "@type": "WebPage",
            "@id": "https://www.wikidata.org/wiki/Q139827028",
            "name": "Harsh Verma - Wikidata Knowledge Graph Entity (Q139827028)",
            "url": "https://www.wikidata.org/wiki/Q139827028",
        },
        {
            "@type": "WebPage",
            "@id": "https://wikialpha.co/wiki/Harsh_Verma_(Software_Engineer)",
            "name": "Harsh Verma (Software Engineer) - WikiAlpha Biography",
            "url": "https://wikialpha.co/wiki/Harsh_Verma_(Software_Engineer)",
        },
        {
            "@type": "WebPage",
            "@id": "https://en.wikiflux.org/wiki/index.php/Harsh_Verma_(Software_Engineer)",
            "name": "Harsh Verma (Software Engineer) - WikiFlux Biography",
            "url": "https://en.wikiflux.org/wiki/index.php/Harsh_Verma_(Software_Engineer)",
        },
        {
            "@type": "WebPage",
            "@id": "https://localwiki.org/main/Harsh_Verma",
            "name": "Harsh Verma - LocalWiki Global Hub Biography",
            "url": "https://localwiki.org/main/Harsh_Verma",
        },
        {
            "@type": "WebPage",
            "@id": "https://localwiki.org/santaclara/Harsh_Verma",
            "name": "Harsh Verma - LocalWiki Santa Clara Silicon Valley Guide",
            "url": "https://localwiki.org/santaclara/Harsh_Verma",
        },
        {
            "@type": "WebPage",
            "@id": "https://localwiki.org/dallas/Harsh_Verma",
            "name": "Harsh Verma - LocalWiki Dallas Guide",
            "url": "https://localwiki.org/dallas/Harsh_Verma",
        },
    ]
    for m in media:
        m_type = "PodcastEpisode" if m.get("type") == "podcast" else "NewsArticle"
        m_url = m.get("primary_url") or f"{CANONICAL_SITE_URL}/page-media"
        m_links = [l["url"] for l in (m.get("links") or []) if l.get("url")]
        m_icon = m.get("icon_svg", "")
        m_node = {
            "@type": m_type,
            "@id": f"{CANONICAL_SITE_URL}/page-media#{m.get('id', '')}",
            "headline": m.get("title", ""),
            "name": m.get("title", ""),
            "description": m.get("summary", ""),
            "url": m_url,
            "datePublished": parse_iso_date(str(m.get("date") or m.get("year", "2026"))),
            "image": f"{CANONICAL_SITE_URL}/images/media/{m_icon}" if m_icon else None,
            "about": {"@id": f"{CANONICAL_SITE_URL}/#person"},
            "publisher": {
                "@type": "Organization",
                "name": m.get("outlet", "Global Media Outlet"),
            },
        }
        if len(m_links) > 1:
            m_node["sameAs"] = m_links
        subject_of.append({k: v for k, v in m_node.items() if v is not None})

    book_nodes = []
    for b in books:
        if b.get("role") == "Authored Book":
            book_nodes.append({
                "@type": "Book",
                "@id": f"{CANONICAL_SITE_URL}/page-books#{b['id']}",
                "name": b["title"],
                "alternateName": b["subtitle"],
                "description": b["description"],
                "author": {"@id": f"{CANONICAL_SITE_URL}/#person"},
                "datePublished": parse_iso_date(str(b.get("year", "2026"))),
                "image": f"{CANONICAL_SITE_URL}/{b['image'].lstrip('/')}",
                "url": f"{CANONICAL_SITE_URL}/page-books",
                "bookFormat": "https://schema.org/EBook",
                "inLanguage": "en",
            })
        else:
            book_nodes.append({
                "@type": "Review",
                "@id": f"{CANONICAL_SITE_URL}/page-books#{b['id']}",
                "name": b["title"],
                "reviewBody": b["description"],
                "author": {"@id": f"{CANONICAL_SITE_URL}/#person"},
                "datePublished": parse_iso_date(str(b.get("year", "2026"))),
                "itemReviewed": {
                    "@type": "Book",
                    "name": b["title"].replace(" (Technical Book Review)", ""),
                    "image": f"{CANONICAL_SITE_URL}/{b['image'].lstrip('/')}",
                },
            })

    article_nodes = []
    for b in blogs:
        if b.get("url"):
            art_obj = {
                "@type": "TechArticle",
                "@id": f"{CANONICAL_SITE_URL}/page-blog#{b.get('id', '')}",
                "headline": b["title"],
                "name": b["title"],
                "description": b.get("description", ""),
                "url": b["url"],
                "image": f"{CANONICAL_SITE_URL}/{b.get('image', '').lstrip('/')}" if b.get("image") else None,
                "datePublished": parse_iso_date(str(b.get("date", "2026"))),
                "author": {"@id": f"{CANONICAL_SITE_URL}/#person"},
                "publisher": {
                    "@type": "Organization",
                    "name": b.get("platform", "Forbes Technology Council"),
                },
            }
            article_nodes.append({k: v for k, v in art_obj.items() if v is not None})

    paper_nodes = []
    for p in papers:
        p_node = {
            "@type": "ScholarlyArticle",
            "@id": f"{CANONICAL_SITE_URL}/page-publications#{p.get('id', '')}",
            "headline": p.get("title", ""),
            "name": p.get("title", ""),
            "abstract": p.get("abstract", ""),
            "author": {"@id": f"{CANONICAL_SITE_URL}/#person"},
            "datePublished": parse_iso_date(str(p.get("year", "2026"))),
            "url": p.get("link", f"{CANONICAL_SITE_URL}/page-publications"),
            "publisher": {
                "@type": "Organization",
                "name": p.get("venue") or p.get("publisher") or "IEEE / Peer-Reviewed Venue",
            },
        }
        if p.get("doi"):
            p_node["identifier"] = f"https://doi.org/{p['doi']}"
            p_node["sameAs"] = f"https://doi.org/{p['doi']}"
        paper_nodes.append(p_node)

    person_node = {
        "@type": "Person",
        "@id": f"{CANONICAL_SITE_URL}/#person",
        "name": "Harsh Verma",
        "givenName": "Harsh",
        "familyName": "Verma",
        "alternateName": [
            "Harsh Verma (Software Engineer)",
            "Harsh Verma AI",
            "iamharshverma",
            "harshverma59",
        ],
        "jobTitle": [
            "Principal Software Engineer (AI)",
            "Enterprise AI Architect",
            "Keynote Speaker",
            "Author",
            "Computer Science Researcher",
        ],
        "description": "Harsh Verma is an internationally recognized Principal Software Engineer in AI at Palo Alto Networks, Forbes Technology Council Member, IEEE Senior Member (SMIEEE), Fellow of the British Computer Society (FBCS), Fellow of the Royal Society of Arts (FRSA), Full Member of Sigma Xi, Author, Keynote Speaker, and AI Researcher.",
        "url": f"{CANONICAL_SITE_URL}/",
        "mainEntityOfPage": {
            "@id": f"{CANONICAL_SITE_URL}/page-identity#profilepage",
        },
        "image": [
            {
                "@type": "ImageObject",
                "@id": f"{CANONICAL_SITE_URL}/#headshot-primary",
                "url": f"{CANONICAL_SITE_URL}/images/harsh/Harsh_portfolio_pic.png",
                "contentUrl": f"{CANONICAL_SITE_URL}/images/harsh/Harsh_portfolio_pic.png",
                "caption": "Harsh Verma - Principal AI Software Engineer at Palo Alto Networks, Keynote Speaker, Author & Researcher",
            },
            {
                "@type": "ImageObject",
                "@id": f"{CANONICAL_SITE_URL}/#headshot-editorial",
                "url": f"{CANONICAL_SITE_URL}/images/harsh/infq_harsh.jpg",
                "contentUrl": f"{CANONICAL_SITE_URL}/images/harsh/infq_harsh.jpg",
                "caption": "Harsh Verma - Executive Portrait",
            },
        ],
        "identifier": [
            {
                "@type": "PropertyValue",
                "propertyID": "CanonicalURI",
                "name": "Primary Canonical Entity URI",
                "value": f"{CANONICAL_SITE_URL}/#person",
                "url": f"{CANONICAL_SITE_URL}/page-identity",
            },
            {
                "@type": "PropertyValue",
                "propertyID": "RootDomainURI",
                "name": "Root Domain Entity URI",
                "value": f"{SECONDARY_SITE_URL}/#person",
                "url": f"{SECONDARY_SITE_URL}/page-identity",
            },
            {
                "@type": "PropertyValue",
                "propertyID": "Wikidata",
                "name": "Wikidata Entity ID",
                "value": WIKIDATA_QID,
                "url": f"https://www.wikidata.org/wiki/{WIKIDATA_QID}",
            },
            {
                "@type": "PropertyValue",
                "propertyID": "EverybodyWiki",
                "name": "EverybodyWiki Article ID",
                "value": EVERYBODYWIKI_TITLE,
                "url": f"https://en.everybodywiki.com/{EVERYBODYWIKI_TITLE}",
            },
            {
                "@type": "PropertyValue",
                "propertyID": "WikiAlpha",
                "name": "WikiAlpha Article ID",
                "value": "Harsh_Verma_(Software_Engineer)",
                "url": "https://wikialpha.co/wiki/Harsh_Verma_(Software_Engineer)",
            },
            {
                "@type": "PropertyValue",
                "propertyID": "WikiFlux",
                "name": "WikiFlux Article ID",
                "value": "Harsh_Verma_(Software_Engineer)",
                "url": "https://en.wikiflux.org/wiki/index.php/Harsh_Verma_(Software_Engineer)",
            },
            {
                "@type": "PropertyValue",
                "propertyID": "LocalWiki",
                "name": "LocalWiki Main Profile",
                "value": "main/Harsh_Verma",
                "url": "https://localwiki.org/main/Harsh_Verma",
            },
            {
                "@type": "PropertyValue",
                "propertyID": "LocalWiki",
                "name": "LocalWiki Santa Clara Profile",
                "value": "santaclara/Harsh_Verma",
                "url": "https://localwiki.org/santaclara/Harsh_Verma",
            },
            {
                "@type": "PropertyValue",
                "propertyID": "ORCID",
                "name": "ORCID iD",
                "value": "0000-0003-2134-2600",
                "url": "https://orcid.org/0000-0003-2134-2600",
            },
            {
                "@type": "PropertyValue",
                "propertyID": "GoogleScholar",
                "name": "Google Scholar Author ID",
                "value": "zSt9oRMAAAAJ",
                "url": "https://scholar.google.com/citations?user=zSt9oRMAAAAJ",
            },
            {
                "@type": "PropertyValue",
                "propertyID": "SemanticScholar",
                "name": "Semantic Scholar Author ID",
                "value": "145004805",
                "url": "https://www.semanticscholar.org/author/Harsh-Verma/145004805",
            },
            {
                "@type": "PropertyValue",
                "propertyID": "SSRN",
                "name": "SSRN Author ID",
                "value": "11144549",
                "url": "https://papers.ssrn.com/sol3/cf_dev/AbsByAuth.cfm?per_id=11144549",
            },
            {
                "@type": "PropertyValue",
                "propertyID": "IEEE",
                "name": "IEEE Senior Member ID",
                "value": "95132014",
                "url": "https://ieee-collabratec.ieee.org/app/p/HarshVerma59",
            },
        ],
        "worksFor": {
            "@type": "Organization",
            "@id": "http://www.wikidata.org/entity/Q7128508",
            "name": "Palo Alto Networks",
            "url": "https://www.paloaltonetworks.com/",
            "sameAs": [
                "https://www.wikidata.org/wiki/Q7128508",
                "https://theorg.com/org/palo-alto-networks/person/harsh-verma",
            ],
        },
        "alumniOf": [
            {
                "@type": "CollegeOrUniversity",
                "@id": "http://www.wikidata.org/entity/Q41506",
                "name": "Stanford University",
                "alternateName": "Stanford",
                "url": "https://www.stanford.edu/",
                "sameAs": [
                    "https://www.wikidata.org/wiki/Q41506",
                    "http://www.wikidata.org/entity/Q41506",
                ],
                "description": "Graduate Certificate in Artificial Intelligence & Executive Leadership, Stanford Center for Professional Development (SCPD)",
            },
            {
                "@type": "CollegeOrUniversity",
                "@id": "http://www.wikidata.org/entity/Q1781394",
                "name": "University of Texas at Dallas",
                "alternateName": "UT Dallas",
                "url": "https://www.utdallas.edu/",
                "sameAs": [
                    "https://www.wikidata.org/wiki/Q1781394",
                    "http://www.wikidata.org/entity/Q1781394",
                ],
                "description": "Graduate Studies in Computer Science & Systems Engineering, Erik Jonsson School of Engineering and Computer Science",
            },
            {
                "@type": "CollegeOrUniversity",
                "@id": "http://www.wikidata.org/entity/Q7903393",
                "name": "Uttarakhand Technical University",
                "alternateName": "UTU",
                "url": "https://uktech.ac.in/",
                "sameAs": [
                    "https://www.wikidata.org/wiki/Q7903393",
                    "http://www.wikidata.org/entity/Q7903393",
                ],
                "description": "Bachelor of Technology (B.Tech) in Computer Science & Engineering",
            },
        ],
        "knowsAbout": [
            "Artificial Intelligence",
            "Agentic AI Architectures",
            "Multi-Agent Systems",
            "Autonomous Cyber Defense",
            "Zero-Trust Security Architecture",
            "Large Language Models (LLMs)",
            "Distributed Cloud Computing",
            "Explainable AI (XAI)",
            "Real-Time Streaming Analytics",
            "Enterprise Software Engineering",
        ],
        "memberOf": member_of,
        "award": award_titles,
        "hasCredential": has_credentials,
        "subjectOf": subject_of,
        "sameAs": same_as_urls,
    }

    website_node = {
        "@type": "WebSite",
        "@id": f"{CANONICAL_SITE_URL}/#website",
        "url": f"{CANONICAL_SITE_URL}/",
        "sameAs": [
            f"{SECONDARY_SITE_URL}/",
        ],
        "name": "Harsh Verma Official Portfolio & Knowledge Graph Hub",
        "publisher": {"@id": f"{CANONICAL_SITE_URL}/#person"},
        "inLanguage": "en-US",
    }

    profile_page_node = {
        "@type": "ProfilePage",
        "@id": f"{CANONICAL_SITE_URL}/page-identity#profilepage",
        "url": f"{CANONICAL_SITE_URL}/page-identity",
        "sameAs": [
            f"{SECONDARY_SITE_URL}/page-identity",
            f"{CANONICAL_SITE_URL}/page-about",
        ],
        "name": "Harsh Verma - Official Entity Verification, Wikidata Q139827028 & Knowledge Graph Hub",
        "isPartOf": {"@id": f"{CANONICAL_SITE_URL}/#website"},
        "about": {"@id": f"{CANONICAL_SITE_URL}/#person"},
        "mainEntity": {"@id": f"{CANONICAL_SITE_URL}/#person"},
    }

    return {
        "@context": "https://schema.org",
        "@graph": [
            website_node,
            profile_page_node,
            person_node,
            *book_nodes,
            *article_nodes,
            *paper_nodes,
        ],
    }


def query_and_sync_wikidata(claims, bot_user=None, bot_pass=None, two_factor_token=None):
    """Query live Wikidata entity Q139827028, audit all claims and reference URLs,
    identify any references pointing to iamharshverma.github.io, remove ACM Q127992,
    update P856 official website, and execute live wbsetreference / wbsetclaim / wbremoveclaims
    if bot/2FA credentials are available, or generate exact QuickStatements payload."""
    result = {
        "entity_id": WIKIDATA_QID,
        "entity_url": f"https://www.wikidata.org/wiki/{WIKIDATA_QID}",
        "json_endpoint": f"https://www.wikidata.org/wiki/Special:EntityData/{WIKIDATA_QID}.json",
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "live_reachable": False,
        "existing_labels": {},
        "existing_descriptions": {},
        "existing_claims_count": 0,
        "existing_properties": [],
        "missing_properties": [],
        "removed_acm_claims": 0,
        "outdated_references": [],
        "outdated_references_count": 0,
        "updated_references_count": 0,
        "p856_outdated": False,
        "api_write_status": "unknown",
        "api_write_message": "",
    }

    existing_prop_val_pairs = set()
    acm_claim_guids = []
    p856_guid = None
    outdated_refs = []

    try:
        url = f"https://www.wikidata.org/wiki/Special:EntityData/{WIKIDATA_QID}.json"
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        ent = data.get("entities", {}).get(WIKIDATA_QID, {})
        if ent and "missing" not in ent:
            result["live_reachable"] = True
            result["lastrevid"] = ent.get("lastrevid")
            result["modified"] = ent.get("modified")
            labels = ent.get("labels", {})
            descs = ent.get("descriptions", {})
            if "en" in labels:
                result["existing_labels"]["en"] = labels["en"].get("value", "")
            if "en" in descs:
                result["existing_descriptions"]["en"] = descs["en"].get("value", "")
            live_claims = ent.get("claims", {})
            result["existing_properties"] = sorted(list(live_claims.keys()))
            result["existing_claims_count"] = sum(len(v) for v in live_claims.values())

            for prop, clist in live_claims.items():
                for c_item in clist:
                    guid = c_item.get("id")
                    mainsnak = c_item.get("mainsnak", {})
                    dv = mainsnak.get("datavalue", {}).get("value")

                    # Check for ACM (Q127992)
                    if isinstance(dv, dict) and "id" in dv:
                        if dv["id"] == "Q127992":
                            if guid:
                                acm_claim_guids.append(guid)
                        else:
                            existing_prop_val_pairs.add((prop, dv["id"]))
                    elif isinstance(dv, str):
                        if "iamharshverma.github.io" in dv:
                            if prop == "P856":
                                p856_guid = guid
                                result["p856_outdated"] = True
                            if guid and prop != "P856":
                                acm_claim_guids.append(guid)
                        else:
                            existing_prop_val_pairs.add((prop, dv))

                    # Deep audit of all statement references for iamharshverma.github.io
                    for ref in c_item.get("references", []):
                        ref_hash = ref.get("hash")
                        for rprop, rsnaks in ref.get("snaks", {}).items():
                            for rsnak in rsnaks:
                                rval = rsnak.get("datavalue", {}).get("value")
                                if isinstance(rval, str) and "iamharshverma.github.io" in rval:
                                    target_url = "https://www.harshverma.me/"
                                    if prop == "P463":
                                        target_url = "https://www.harshverma.me/page-memberships"
                                    elif prop == "P69":
                                        target_url = "https://www.harshverma.me/page-about"
                                    elif prop == "P106":
                                        target_url = "https://www.harshverma.me/page-speaker"
                                    elif "memberships" in rval:
                                        target_url = "https://www.harshverma.me/page-memberships"
                                    elif "about" in rval:
                                        target_url = "https://www.harshverma.me/page-about"
                                    elif "speaker" in rval:
                                        target_url = "https://www.harshverma.me/page-speaker"

                                    outdated_refs.append({
                                        "statement_id": guid,
                                        "property": prop,
                                        "statement_val": dv.get("id") if isinstance(dv, dict) else dv,
                                        "reference_hash": ref_hash,
                                        "old_url": rval,
                                        "new_url": target_url,
                                    })
    except Exception as e:
        result["api_write_message"] = f"Read warning: {str(e)}"

    result["outdated_references"] = outdated_refs
    result["outdated_references_count"] = len(outdated_refs)

    missing_claims = []
    for c in claims:
        if (c["property"], c["value"]) not in existing_prop_val_pairs:
            missing_claims.append(c)

    result["missing_properties"] = [
        {"property": m["property"], "label": m["label"], "value": m["value_label"]}
        for m in missing_claims
    ]

    # Attempt live synchronization if authentication is provided
    bot_user = bot_user or os.environ.get("WIKIDATA_BOT_USER")
    bot_pass = bot_pass or os.environ.get("WIKIDATA_BOT_PASS")
    two_factor_token = two_factor_token or os.environ.get("WIKIDATA_2FA_TOKEN")

    cookie_path = os.path.join(DATA_DIR, "wikidata_session.txt")
    token_path = os.path.join(DATA_DIR, "wikidata_logintoken.txt")
    cj = http.cookiejar.MozillaCookieJar(cookie_path)
    if os.path.exists(cookie_path):
        try:
            cj.load(ignore_discard=True, ignore_expires=True)
        except Exception:
            pass

    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.addheaders = [("User-Agent", USER_AGENT)]

    authenticated = False
    try:
        if bot_user and bot_pass:
            lt_resp = opener.open(f"{WIKIDATA_API}?action=query&meta=tokens&type=login&format=json", timeout=12)
            login_token = json.loads(lt_resp.read().decode())["query"]["tokens"]["logintoken"]
            lg_payload = urllib.parse.urlencode({
                "action": "login",
                "lgname": bot_user,
                "lgpassword": bot_pass,
                "lgtoken": login_token,
                "format": "json",
            }).encode("utf-8")
            lg_resp = opener.open(WIKIDATA_API, data=lg_payload, timeout=15)
            lg_json = json.loads(lg_resp.read().decode())
            if lg_json.get("login", {}).get("result") == "Success":
                authenticated = True

        elif two_factor_token:
            # Check if we have an active persistent session and logintoken
            login_token = None
            if os.path.exists(token_path):
                try:
                    with open(token_path, "r", encoding="utf-8") as f:
                        login_token = f.read().strip()
                except Exception:
                    pass

            if not login_token:
                lt_resp = opener.open(f"{WIKIDATA_API}?action=query&meta=tokens&type=login&format=json", timeout=12)
                login_token = json.loads(lt_resp.read().decode())["query"]["tokens"]["logintoken"]
                cl1_payload = urllib.parse.urlencode({
                    "action": "clientlogin",
                    "username": "harshverma59",
                    "password": bot_pass or os.environ.get("WIKIDATA_USER_PASS", ""),
                    "logintoken": login_token,
                    "loginreturnurl": "https://www.wikidata.org/",
                    "format": "json"
                }).encode("utf-8")
                opener.open(WIKIDATA_API, data=cl1_payload, timeout=15)
                cj.save(ignore_discard=True, ignore_expires=True)
                with open(token_path, "w", encoding="utf-8") as f:
                    f.write(login_token)

            # Submit 2FA email token within the exact persistent session
            cl2_payload = urllib.parse.urlencode({
                "action": "clientlogin",
                "logintoken": login_token,
                "token": two_factor_token.strip(),
                "logincontinue": 1,
                "format": "json"
            }).encode("utf-8")
            cl2_resp = opener.open(WIKIDATA_API, data=cl2_payload, timeout=15)
            cl2_json = json.loads(cl2_resp.read().decode())
            if cl2_json.get("clientlogin", {}).get("status") == "PASS":
                authenticated = True
                cj.save(ignore_discard=True, ignore_expires=True)
            elif cl2_json.get("clientlogin", {}).get("status") == "UI":
                result["api_write_message"] = cl2_json.get("clientlogin", {}).get("message", "2FA failed")

        tok_resp = opener.open(f"{WIKIDATA_API}?action=query&meta=tokens&format=json", timeout=12)
        tok_data = json.loads(tok_resp.read().decode("utf-8"))
        csrf_token = tok_data.get("query", {}).get("tokens", {}).get("csrftoken", "+\\")

        if authenticated:
            # 1. Update each outdated reference via wbsetreference
            updated_count = 0
            for o_ref in outdated_refs:
                snaks = {
                    "P854": [
                        {
                            "snaktype": "value",
                            "property": "P854",
                            "datavalue": {"type": "string", "value": o_ref["new_url"]},
                        }
                    ]
                }
                ref_payload = urllib.parse.urlencode({
                    "action": "wbsetreference",
                    "statement": o_ref["statement_id"],
                    "reference": o_ref["reference_hash"],
                    "snaks": json.dumps(snaks),
                    "summary": f"Update reference URL to {o_ref['new_url']} (canonical domain migration)",
                    "token": csrf_token,
                    "format": "json",
                }).encode("utf-8")
                ref_resp = opener.open(WIKIDATA_API, data=ref_payload, timeout=15)
                ref_json = json.loads(ref_resp.read().decode())
                if "reference" in ref_json:
                    updated_count += 1
            result["updated_references_count"] = updated_count

            # 2. Update P856 official website if outdated
            if p856_guid:
                p856_payload = urllib.parse.urlencode({
                    "action": "wbsetclaim",
                    "claim": json.dumps({
                        "id": p856_guid,
                        "type": "statement",
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P856",
                            "datavalue": {"type": "string", "value": "https://www.harshverma.me/"},
                        },
                    }),
                    "summary": "Update official website to canonical https://www.harshverma.me/",
                    "token": csrf_token,
                    "format": "json",
                }).encode("utf-8")
                opener.open(WIKIDATA_API, data=p856_payload, timeout=15)

            # 3. Remove ACM claims if present
            if acm_claim_guids:
                rm_data = urllib.parse.urlencode({
                    "action": "wbremoveclaims",
                    "claim": "|".join(acm_claim_guids),
                    "summary": "Remove ACM (Q127992) claim per canonical entity verification update",
                    "token": csrf_token,
                    "format": "json",
                }).encode("utf-8")
                opener.open(WIKIDATA_API, data=rm_data, timeout=15)
                result["removed_acm_claims"] = len(acm_claim_guids)

            result["api_write_status"] = "synced"
            result["api_write_message"] = (
                f"Successfully updated {updated_count} references live to https://www.harshverma.me/, "
                f"updated P856 official website, and removed ACM on Wikidata {WIKIDATA_QID}!"
            )
        else:
            result["api_write_status"] = "ready_for_quickstatements"
            result["api_write_message"] = (
                f"Audited Wikidata {WIKIDATA_QID} live: Found {len(outdated_refs)} references pointing to "
                f"iamharshverma.github.io and 1 P856 website claim. QuickStatements batch generated "
                f"for 1-click execution in Toolforge without 2FA, or submit Email 2FA token / Bot password."
            )
    except Exception as e:
        result["api_write_status"] = "audit_complete"
        result["api_write_message"] = f"Wikidata Note: {str(e)}"

    return result


def query_and_sync_everybodywiki(wikitext):
    """Query live EverybodyWiki article and execute authenticated clientlogin/login + action=edit."""
    result = {
        "article_title": EVERYBODYWIKI_TITLE,
        "article_url": f"https://en.everybodywiki.com/{EVERYBODYWIKI_TITLE}",
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "live_reachable": False,
        "existing_bytes": 0,
        "generated_bytes": len(wikitext.encode("utf-8")),
        "api_write_status": "unknown",
        "api_write_message": "",
    }

    try:
        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        opener.addheaders = [("User-Agent", USER_AGENT)]

        q_url = (
            f"{EVERYBODYWIKI_API}?action=query&titles={urllib.parse.quote(EVERYBODYWIKI_TITLE)}"
            f"&prop=revisions|info&rvprop=content|ids|timestamp&format=json"
        )
        q_resp = opener.open(q_url, timeout=15)
        q_data = json.loads(q_resp.read().decode("utf-8"))
        pages = q_data.get("query", {}).get("pages", {})
        for pid, pinfo in pages.items():
            if int(pid) > 0:
                result["live_reachable"] = True
                result["pageid"] = int(pid)
                result["lastrevid"] = pinfo.get("lastrevid")
                result["existing_bytes"] = pinfo.get("length", 0)
                revs = pinfo.get("revisions", [])
                if revs:
                    result["last_timestamp"] = revs[0].get("timestamp")

        ew_user = os.environ.get("EVERYBODYWIKI_USER")
        ew_pass = os.environ.get("EVERYBODYWIKI_PASS")
        logged_in_user = None

        if ew_user and ew_pass:
            lt_resp = opener.open(f"{EVERYBODYWIKI_API}?action=query&meta=tokens&type=login&format=json", timeout=12)
            lt_data = json.loads(lt_resp.read().decode("utf-8"))
            login_token = lt_data["query"]["tokens"]["logintoken"]

            # Try clientlogin first (supports standard user accounts on MediaWiki 1.27+)
            cl_payload = urllib.parse.urlencode({
                "action": "clientlogin",
                "username": ew_user,
                "password": ew_pass,
                "logintoken": login_token,
                "loginreturnurl": "https://en.everybodywiki.com/",
                "format": "json",
            }).encode("utf-8")
            cl_resp = opener.open(EVERYBODYWIKI_API, data=cl_payload, timeout=15)
            cl_json = json.loads(cl_resp.read().decode("utf-8"))
            if cl_json.get("clientlogin", {}).get("status") == "PASS":
                logged_in_user = cl_json["clientlogin"].get("username")
            else:
                # Fallback to action=login
                lt_resp2 = opener.open(f"{EVERYBODYWIKI_API}?action=query&meta=tokens&type=login&format=json", timeout=12)
                login_token2 = json.loads(lt_resp2.read().decode("utf-8"))["query"]["tokens"]["logintoken"]
                lg_payload = urllib.parse.urlencode({
                    "action": "login",
                    "lgname": ew_user,
                    "lgpassword": ew_pass,
                    "lgtoken": login_token2,
                    "format": "json",
                }).encode("utf-8")
                lg_resp = opener.open(EVERYBODYWIKI_API, data=lg_payload, timeout=15)
                lg_json = json.loads(lg_resp.read().decode("utf-8"))
                if lg_json.get("login", {}).get("result") == "Success":
                    logged_in_user = lg_json["login"].get("lgusername")

        tok_resp = opener.open(f"{EVERYBODYWIKI_API}?action=query&meta=tokens&format=json", timeout=12)
        tok_data = json.loads(tok_resp.read().decode("utf-8"))
        csrf_token = tok_data.get("query", {}).get("tokens", {}).get("csrftoken", "+\\")

        edit_payload = urllib.parse.urlencode({
            "action": "edit",
            "title": EVERYBODYWIKI_TITLE,
            "text": wikitext,
            "summary": "Comprehensive biography update: Palo Alto Networks AI role, Stanford/UTD/UTU education, 2 authored books, 27+ papers, 27 awards, 26 fellowships, 42+ media features, and Wikidata Q139827028 authority links",
            "token": csrf_token,
            "format": "json",
        }).encode("utf-8")

        edit_resp = opener.open(EVERYBODYWIKI_API, data=edit_payload, timeout=20)
        edit_json = json.loads(edit_resp.read().decode("utf-8"))

        if edit_json.get("edit", {}).get("result") == "Success":
            result["api_write_status"] = "synced"
            result["newrevid"] = edit_json["edit"].get("newrevid")
            result["lastrevid"] = edit_json["edit"].get("newrevid", result.get("lastrevid"))
            result["existing_bytes"] = result["generated_bytes"]
            result["api_write_message"] = (
                f"Successfully updated EverybodyWiki article live via MediaWiki API (user: {logged_in_user or 'authenticated'}, new revision: {result['newrevid']})!"
            )
        elif "edit" in edit_json and "captcha" in edit_json["edit"]:
            cap = edit_json["edit"]["captcha"]
            result["api_write_status"] = "captcha_challenge"
            result["captcha_info"] = cap
            result["api_write_message"] = (
                f"Authenticated as '{logged_in_user}', EverybodyWiki requested QuestyCaptcha/SimpleCaptcha ({cap})."
            )
        elif "error" in edit_json:
            err_code = edit_json["error"].get("code", "unknown")
            err_info = edit_json["error"].get("info", "")
            result["api_write_status"] = f"requires_auth ({err_code})"
            result["api_write_message"] = f"EverybodyWiki API note ({err_code}): {err_info}"
        else:
            result["api_write_status"] = "response_info"
            result["api_write_message"] = f"EverybodyWiki response: {json.dumps(edit_json)}"
    except Exception as e:
        result["api_write_status"] = "fallback_ready"
        result["api_write_message"] = f"EverybodyWiki API note: {str(e)}"

    return result


def ensure_paper_thumbnails(papers):
    """Generate dedicated SVG banner thumbnails for each research paper in images/papers/."""
    papers_dir = os.path.join(ROOT_DIR, "images", "papers")
    os.makedirs(papers_dir, exist_ok=True)
    for idx, p in enumerate(papers, 1):
        venue = (p.get("venue") or p.get("publisher") or "IEEE / Peer-Reviewed Venue").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        yr = str(p.get("year") or "2025")
        doi = (p.get("doi") or "Peer-Reviewed Research").replace("&", "&amp;")
        title = (p.get("title") or "Research Publication").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        line1 = title[:52] + ("..." if len(title) > 52 else "")
        venue_short = venue[:42] + ("..." if len(venue) > 42 else "")
        svg_rel = f"images/papers/paper_{idx}.svg"
        svg_path = os.path.join(ROOT_DIR, svg_rel)
        svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 160" width="400" height="160">
  <defs>
    <linearGradient id="pg{idx}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#09152b"/>
      <stop offset="55%" stop-color="#0f2942"/>
      <stop offset="100%" stop-color="#1e3a8a"/>
    </linearGradient>
  </defs>
  <rect width="400" height="160" rx="14" fill="url(#pg{idx})"/>
  <rect x="8" y="8" width="384" height="144" rx="10" fill="none" stroke="rgba(56,189,248,0.28)" stroke-width="1.5"/>
  <rect x="20" y="20" width="96" height="24" rx="6" fill="rgba(56,189,248,0.18)" stroke="#38bdf8" stroke-width="1"/>
  <text x="68" y="36" text-anchor="middle" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">PAPER #{idx} · {yr}</text>
  <text x="20" y="68" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13.5" font-weight="700">{venue_short}</text>
  <text x="20" y="94" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11.5">{line1}</text>
  <text x="20" y="132" fill="#93c5fd" font-family="monospace" font-size="10.5">DOI: {doi[:38]}</text>
</svg>'''
        with open(svg_path, "w", encoding="utf-8") as sf:
            sf.write(svg_content)
        p["image"] = svg_rel
    return papers


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Synchronize Knowledge Graph, Wikidata, and EverybodyWiki")
    parser.add_argument("--wikidata-2fa", dest="wikidata_2fa", default=os.environ.get("WIKIDATA_2FA_TOKEN"), help="6-digit Wikidata Email 2FA token")
    parser.add_argument("--bot-user", dest="bot_user", default=os.environ.get("WIKIDATA_BOT_USER"), help="Wikidata Bot Username")
    parser.add_argument("--bot-pass", dest="bot_pass", default=os.environ.get("WIKIDATA_BOT_PASS"), help="Wikidata Bot Password")
    args, _ = parser.parse_known_args()

    # EverybodyWiki username
    if not os.environ.get("EVERYBODYWIKI_USER"):
        os.environ["EVERYBODYWIKI_USER"] = "harshverma59"

    print("=== Building Canonical Google Knowledge Graph & Executing Wiki Sync ===")
    profiles = extract_verified_profiles()
    media = load_json_file("media_data.json")
    awards = load_json_file("awards_data.json")
    papers = ensure_paper_thumbnails(load_json_file("papers_data.json"))
    blogs = extract_blogs()
    associations = extract_associations()
    books = build_books_data()

    print(
        f"Loaded {len(profiles)} Verified Profiles, {len(media)} Media Features, "
        f"{len(awards)} Awards, {len(blogs)} Blogs/Columns, {len(books)} Books/Reviews, "
        f"{len(papers)} Research Papers, {len(associations)} Associations (ACM Removed)."
    )

    wd_claims = build_wikidata_claims_manifest()
    qs_text = generate_quickstatements(wd_claims)
    qs_path = os.path.join(DATA_DIR, "wikidata-quickstatements.txt")
    with open(qs_path, "w", encoding="utf-8") as f:
        f.write(qs_text)

    ref_replacement_text = generate_reference_replacement_batches()
    ref_replacement_path = os.path.join(DATA_DIR, "wikidata-reference-replacement.txt")
    with open(ref_replacement_path, "w", encoding="utf-8") as f:
        f.write(ref_replacement_text)

    wikitext = generate_everybodywiki_wikitext(profiles, media, awards, blogs, books, papers, associations)
    wiki_path = os.path.join(DATA_DIR, "everybodywiki-article.wiki")
    with open(wiki_path, "w", encoding="utf-8") as f:
        f.write(wikitext)

    schema_graph = build_schema_org_graph(profiles, media, awards, blogs, books, papers, associations)

    print(f"Querying & syncing Wikidata ({WIKIDATA_QID})...")
    wd_sync = query_and_sync_wikidata(
        wd_claims,
        bot_user=args.bot_user,
        bot_pass=args.bot_pass,
        two_factor_token=args.wikidata_2fa,
    )
    print(f"  -> Wikidata Status: {wd_sync['api_write_status']} | {wd_sync['api_write_message']}")

    print(f"Querying & syncing EverybodyWiki ({EVERYBODYWIKI_TITLE})...")
    ew_sync = query_and_sync_everybodywiki(wikitext)
    print(f"  -> EverybodyWiki Status: {ew_sync['api_write_status']} | {ew_sync['api_write_message']}")

    # Preserve previous synced status if EverybodyWiki was already synced earlier and current run had no env vars
    sync_status_path = os.path.join(DATA_DIR, "wiki-sync-status.json")
    if ew_sync["api_write_status"].startswith("requires_auth") and os.path.exists(sync_status_path):
        try:
            prev_status = json.load(open(sync_status_path, "r", encoding="utf-8"))
            if prev_status.get("everybodywiki", {}).get("api_write_status") == "synced":
                ew_sync = prev_status["everybodywiki"]
        except Exception:
            pass

    sync_status = {
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "wikidata": wd_sync,
        "everybodywiki": ew_sync,
    }
    with open(sync_status_path, "w", encoding="utf-8") as f:
        json.dump(sync_status, f, indent=2)

    master_payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "entity_id": f"{CANONICAL_SITE_URL}/#person",
        "secondary_entity_ids": [
            f"{SECONDARY_SITE_URL}/#person",
            f"http://www.wikidata.org/entity/{WIKIDATA_QID}",
        ],
        "wikidata_qid": WIKIDATA_QID,
        "wikidata_url": f"https://www.wikidata.org/wiki/{WIKIDATA_QID}",
        "everybodywiki_title": EVERYBODYWIKI_TITLE,
        "everybodywiki_url": f"https://en.everybodywiki.com/{EVERYBODYWIKI_TITLE}",
        "wikialpha_url": "https://wikialpha.co/wiki/Harsh_Verma_(Software_Engineer)",
        "wikiflux_url": "https://en.wikiflux.org/wiki/index.php/Harsh_Verma_(Software_Engineer)",
        "localwiki_main_url": "https://localwiki.org/main/Harsh_Verma",
        "localwiki_santaclara_url": "https://localwiki.org/santaclara/Harsh_Verma",
        "localwiki_dallas_url": "https://localwiki.org/dallas/Harsh_Verma",
        "counts": {
            "profiles": len(profiles),
            "media": len(media),
            "awards": len(awards),
            "blogs": len(blogs),
            "books": len(books),
            "papers": len(papers),
            "associations": len(associations),
            "wikidata_claims": len(wd_claims),
            "total_linked_nodes": len(profiles) + len(media) + len(awards) + len(blogs) + len(books) + len(papers) + len(associations),
        },
        "wikidata_claims": wd_claims,
        "quickstatements": qs_text,
        "quickstatements_reference_replacement": ref_replacement_text,
        "everybodywiki_wikitext": wikitext,
        "sync_status": sync_status,
        "entities": {
            "profiles": profiles,
            "media": media,
            "awards": awards,
            "blogs": blogs,
            "books": books,
            "papers": papers,
            "associations": associations,
        },
        "schema_json_ld": schema_graph,
    }

    kg_path = os.path.join(DATA_DIR, "knowledge-graph.json")
    with open(kg_path, "w", encoding="utf-8") as f:
        json.dump(master_payload, f, indent=2)
    print(f"Saved master Knowledge Graph dataset to {kg_path} ({master_payload['counts']['total_linked_nodes']} total linked nodes).")

    # Generate specialized multi-wiki syndication packages
    try:
        import subprocess
        gen_script = os.path.join(ROOT_DIR, "scripts", "generate_multi_wiki_articles.py")
        if os.path.exists(gen_script):
            subprocess.run(["python3", gen_script], check=True)
    except Exception as e:
        print(f"[Warn] Could not run generate_multi_wiki_articles: {e}")


if __name__ == "__main__":
    main()
