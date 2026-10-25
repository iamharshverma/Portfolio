#!/usr/bin/env python3
"""
scripts/sync_wiki_entities.py
=============================
Builds the unified Google Knowledge Graph dataset (`data/knowledge-graph.json`),
generates programmatic Wikidata (`Q139827028`) QuickStatements (`data/wikidata-quickstatements.txt`),
generates the complete EverybodyWiki biography Wikitext (`data/everybodywiki-article.wiki`),
and executes live MediaWiki Action API synchronization against:
  1. Wikidata: https://www.wikidata.org/wiki/Q139827028
  2. EverybodyWiki: https://en.everybodywiki.com/Harsh_Verma_(Software_Engineer)
"""

import os
import re
import json
import time
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
CANONICAL_SITE_URL = "https://iamharshverma.github.io"
USER_AGENT = "HarshVermaKnowledgeGraphBot/2.1 (https://iamharshverma.github.io/; mailto:harshverma59@gmail.com)"


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


def extract_verified_profiles():
    """Extract all 54 verified profile cards from page-about.html."""
    about_path = os.path.join(ROOT_DIR, "page-about.html")
    profiles = []
    seen_Keys = set()

    if os.path.exists(about_path):
        with open(about_path, "r", encoding="utf-8") as f:
            html = f.read()

        # Split by profile-card-item marker
        chunks = re.split(r'<div class="col-lg-4 col-md-6 mb-4 profile-card-item"', html)[1:]
        for chunk in chunks:
            # Cut chunk before next major section if last item
            chunk = chunk.split("<!-- End Verified Profiles")[0]
            cat_code_m = re.search(r'data-category="([^"]+)"', chunk)
            category_code = cat_code_m.group(1).strip() if cat_code_m else "direct"

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
            if url and key not in seen_Keys:
                seen_Keys.add(key)
                profiles.append({
                    "title": title,
                    "category": category_code,
                    "category_label": category_label,
                    "identifier": identifier,
                    "description": desc,
                    "url": url,
                })

    return profiles


def extract_blogs():
    """Extract all blog and Forbes articles from generate_blog_page.py."""
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
                            "category": item.get("category", "Enterprise AI"),
                            "date": item.get("date", "2026"),
                            "url": item.get("url", ""),
                            "author_profile": item.get("author_profile", ""),
                            "description": item.get("description", ""),
                        })
                except Exception as e:
                    print(f"[Warn] Could not exec articles_data: {e}")
    return blogs


def extract_associations():
    """Extract all 27+ invited memberships, fellowships, and associations from page-memberships.html."""
    mem_path = os.path.join(ROOT_DIR, "page-memberships.html")
    associations = []
    if os.path.exists(mem_path):
        with open(mem_path, "r", encoding="utf-8") as f:
            html = f.read()

        chunks = re.split(r'<div class="col-lg-4 col-md-6 mb-4 membership-item"', html)[1:]
        for chunk in chunks:
            cat_m = re.search(r'data-category="([^"]+)"', chunk)
            cat = cat_m.group(1).strip() if cat_m else "fellowship"
            tier_m = re.search(r'<span class="membership-tier-pill[^"]*">(.*?)</span>', chunk, re.DOTALL)
            title_m = re.search(r'<h3 class="membership-title[^"]*">(.*?)</h3>', chunk, re.DOTALL)
            org_m = re.search(r'<div class="membership-org[^"]*">(.*?)</div>', chunk, re.DOTALL)
            cred_m = re.search(r'<div class="membership-credential-id[^"]*">(.*?)</div>', chunk, re.DOTALL)
            desc_m = re.search(r'<p class="membership-desc[^"]*">(.*?)</p>', chunk, re.DOTALL)
            url_m = re.search(r'<a href="([^"]+)"[^>]*class="btn-verify[^"]*"', chunk)

            title = clean_html(title_m.group(1)) if title_m else ""
            if title:
                url = url_m.group(1).strip() if url_m else f"{CANONICAL_SITE_URL}/page-memberships"
                if url and not url.startswith("http"):
                    url = f"{CANONICAL_SITE_URL}/{url.lstrip('/')}"
                associations.append({
                    "title": title,
                    "role": clean_html(org_m.group(1)) if org_m else "Member",
                    "tier": clean_html(tier_m.group(1)) if tier_m else "Fellow / Member",
                    "credential_id": clean_html(cred_m.group(1)) if cred_m else "",
                    "category": cat,
                    "description": clean_html(desc_m.group(1)) if desc_m else "",
                    "url": url,
                })
    return associations


def load_json_file(filename):
    p = os.path.join(ROOT_DIR, filename)
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def build_wikidata_claims_manifest():
    """Return canonical Wikidata claims for Q139827028 using verified Wikidata QIDs."""
    return [
        {
            "property": "P31",
            "label": "instance of",
            "value": "Q5",
            "value_label": "human",
            "type": "wikibase-entityid",
            "reference_url": "https://iamharshverma.github.io/page-about",
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
            "reference_url": "https://iamharshverma.github.io/page-speaker",
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
            "reference_url": "https://iamharshverma.github.io/page-about",
        },
        {
            "property": "P69",
            "label": "educated at",
            "value": "Q1781394",
            "value_label": "University of Texas at Dallas",
            "type": "wikibase-entityid",
            "reference_url": "https://iamharshverma.github.io/page-about",
        },
        {
            "property": "P69",
            "label": "educated at",
            "value": "Q7903393",
            "value_label": "Uttarakhand Technical University",
            "type": "wikibase-entityid",
            "reference_url": "https://iamharshverma.github.io/page-about",
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
            "reference_url": "https://iamharshverma.github.io/page-memberships",
        },
        {
            "property": "P463",
            "label": "member of",
            "value": "Q919096",
            "value_label": "British Computer Society (Fellow FBCS)",
            "type": "wikibase-entityid",
            "reference_url": "https://iamharshverma.github.io/page-memberships",
        },
        {
            "property": "P463",
            "label": "member of",
            "value": "Q1460885",
            "value_label": "Royal Society of Arts (Fellow FRSA)",
            "type": "wikibase-entityid",
            "reference_url": "https://iamharshverma.github.io/page-memberships",
        },
        {
            "property": "P463",
            "label": "member of",
            "value": "Q127992",
            "value_label": "Association for Computing Machinery (ACM)",
            "type": "wikibase-entityid",
            "reference_url": "https://iamharshverma.github.io/page-memberships",
        },
        {
            "property": "P463",
            "label": "member of",
            "value": "Q466113",
            "value_label": "Association for the Advancement of Artificial Intelligence (AAAI)",
            "type": "wikibase-entityid",
            "reference_url": "https://iamharshverma.github.io/page-memberships",
        },
        {
            "property": "P856",
            "label": "official website",
            "value": "https://iamharshverma.github.io/",
            "value_label": "https://iamharshverma.github.io/",
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
            "value": "Harsh-Verma-36",
            "value_label": "Harsh-Verma-36",
            "type": "external-id",
            "formatter_url": "https://www.researchgate.net/profile/Harsh-Verma-36",
            "reference_url": "https://www.researchgate.net/profile/Harsh-Verma-36",
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
    """Generate QuickStatements v1/v2 batch commands for Wikidata Q139827028."""
    lines = [
        f"# QuickStatements Batch for Harsh Verma ({WIKIDATA_QID})",
        f"# Target URL: https://www.wikidata.org/wiki/{WIKIDATA_QID}",
        f"# QuickStatements Tool: https://quickstatements.toolforge.org/#/batch",
        f'{WIKIDATA_QID}\tLen\t"Harsh Verma"',
        f'{WIKIDATA_QID}\tDen\t"Principal AI Software Engineer at Palo Alto Networks, Keynote Speaker, Author, and Researcher"',
        f'{WIKIDATA_QID}\tAen\t"Harsh Verma (Software Engineer)"',
    ]
    for c in claims:
        prop = c["property"]
        val = c["value"]
        ref = c.get("reference_url", "https://iamharshverma.github.io/")
        if c["type"] == "wikibase-entityid":
            lines.append(f'{WIKIDATA_QID}\t{prop}\t{val}\tS854\t"{ref}"')
        else:
            lines.append(f'{WIKIDATA_QID}\t{prop}\t"{val}"\tS854\t"{ref}"')
    return "\n".join(lines) + "\n"


def generate_everybodywiki_wikitext(profiles, media, awards, blogs, books, papers, associations):
    """Generate comprehensive, encyclopedic MediaWiki markup for EverybodyWiki."""
    lines = []
    lines.append("{{Infobox person")
    lines.append("| name               = Harsh Verma")
    lines.append("| image              = ")
    lines.append("| caption            = Harsh Verma, Principal AI Software Engineer, Author & Keynote Speaker")
    lines.append("| occupation         = Principal Software Engineer (AI), Enterprise AI Architect, Author, Keynote Speaker, Researcher")
    lines.append("| employer           = [[Palo Alto Networks]]")
    lines.append("| alma_mater         = [[Stanford University]]<br/>[[University of Texas at Dallas]] (M.S. CS)<br/>[[Uttarakhand Technical University]] (B.Tech CSE)")
    lines.append("| known_for          = Enterprise Agentic AI Architectures, Autonomous Cyber Defense, Multi-Agent Systems, Explainable AI (XAI)")
    lines.append("| notable_works      = ''Enterprise AI Agents: Build Your Authority and Lead the AI Agent Revolution''<br/>''Autonomous Cyber Defense: Adversarial Intelligence and Battleground Systems''")
    lines.append("| awards             = Forttuna Global 100 Power List (2026)<br/>Nobel Technology Awards Gold Winner (2026)<br/>TITAN Innovation Award (2026)<br/>NVTC Cyber50 Honoree (2026)<br/>Global Recognition Award (2026)<br/>Marquis Who's Who in America")
    lines.append("| website            = {{URL|https://iamharshverma.github.io/}}")
    lines.append("| module             = {{Authority control|QID=Q139827028|ORCID=0000-0003-2134-2600}}")
    lines.append("}}")
    lines.append("")
    lines.append("'''Harsh Verma''' is an internationally recognized Principal Software Engineer in Artificial Intelligence at [[Palo Alto Networks]], enterprise AI architect, author, keynote speaker, and computer science researcher.<ref>{{cite web |title=The Org: Harsh Verma - Principal Software Engineer in AI at Palo Alto Networks |url=https://theorg.com/org/palo-alto-networks/person/harsh-verma |website=The Org}}</ref><ref>{{cite web |title=Wikidata Entity Q139827028: Harsh Verma |url=https://www.wikidata.org/wiki/Q139827028 |website=Wikidata}}</ref> He is an official member and columnist for the [[Forbes Technology Council]],<ref>{{cite web |title=Harsh Verma - Forbes Technology Council Profile |url=https://www.forbes.com/councils/forbestechcouncil/people/harshverma/ |website=Forbes}}</ref> a Senior Member of the [[Institute of Electrical and Electronics Engineers]] (SMIEEE), an elected Fellow of the [[British Computer Society]] (FBCS), an elected Fellow of the [[Royal Society of Arts]] (FRSA), and a Full Member of [[Sigma Xi]]: The Scientific Research Honor Society.<ref>{{cite web |title=Harsh Verma Invited Associations & Fellowships |url=https://iamharshverma.github.io/page-memberships |website=Harsh Verma Portfolio}}</ref>")
    lines.append("")
    lines.append("Verma has authored two books on enterprise autonomous systems and cyber defense, published {{nowrap|" + str(len(papers)) + "+}} peer-reviewed research papers across IEEE, Springer Nature, Oxford Academic, and international journals with over 150 academic citations,<ref>{{cite web |title=Harsh Verma Google Scholar Citations |url=https://scholar.google.com/citations?user=zSt9oRMAAAAJ |website=Google Scholar}}</ref> and received {{nowrap|" + str(len(awards)) + "}} international technology and leadership honors.")
    lines.append("")
    lines.append("== Education ==")
    lines.append("* '''[[Stanford University]]''' – Graduate Certificate in Artificial Intelligence & Executive Leadership (Stanford Center for Professional Development).")
    lines.append("* '''[[University of Texas at Dallas]]''' (Erik Jonsson School of Engineering and Computer Science) – Master of Science (M.S.) in Computer Science (Intelligent Systems & Distributed Computing).")
    lines.append("* '''[[Uttarakhand Technical University]]''' – Bachelor of Technology (B.Tech) in Computer Science and Engineering.")
    lines.append("")
    lines.append("== Career and Executive Leadership ==")
    lines.append("Verma serves as Principal Software Engineer (AI) at [[Palo Alto Networks]], where he architects autonomous multi-agent systems, deterministic AI security guardrails, and high-throughput enterprise cloud platforms.<ref>{{cite web |title=The Engineer Rewriting the Rules by Thinking AI Beyond the Code: Inside the World of Harsh Verma |url=https://nyweeklyjournal.com/blog/the-engineer-rewriting-the-rules-by-thinking-%E2%80%9Cai-beyond-the-code%E2%80%9D-inside-the-world-of-harsh-verma |website=New York Weekly Journal}}</ref> Earlier in his career, he engineered large-scale distributed systems, real-time analytics pipelines, and cloud security infrastructure across enterprise technology organizations.")
    lines.append("")
    lines.append("In addition to his engineering leadership, Verma serves as an official contributor on the [[Forbes Technology Council]], an industry awards judge for the Business Intelligence Group (BIG), Globee Awards, and Stevie Awards, and a startup mentor for [[MassChallenge]] and ADPList.")
    lines.append("")
    lines.append("== Authored Books ==")
    for b in books:
        lines.append(f"* '''''{b['title']}''''' – ''{b['subtitle']}'' ({b['description']}) [https://iamharshverma.github.io/page-books Official Book Hub]")
    lines.append("")
    lines.append(f"== Selected Forbes Columns & Thought Leadership ({len(blogs)} Articles) ==")
    for blog in blogs:
        lines.append(f"* [{blog['url']} \"{blog['title']}\"] – ''{blog['platform']}'' ({blog['date']})")
    lines.append("")
    lines.append(f"== Peer-Reviewed Research Publications ({len(papers)}+ Papers) ==")
    for p in papers:
        venue = p.get("venue", "Peer-Reviewed Venue")
        yr = p.get("year", "")
        link = p.get("link", "https://iamharshverma.github.io/page-publications")
        doi = p.get("doi", "")
        doi_str = f" (DOI: <code>{doi}</code>)" if doi else ""
        lines.append(f"* [{link} \"{p.get('title', '')}\"] – ''{venue}'' ({yr}){doi_str}")
    lines.append("")
    lines.append(f"== Invited Fellowships, Councils & Associations ({len(associations)}+ Appointments) ==")
    for assoc in associations:
        lines.append(f"* '''{assoc['title']}''' – {assoc['role']} ({assoc['tier']}) [{assoc['url']} Verify]")
    lines.append("")
    lines.append(f"== Honors and Global Awards ({len(awards)} Recognitions) ==")
    for aw in awards:
        links = aw.get("links") or []
        aw_url = links[0]["url"] if links else "https://iamharshverma.github.io/page-awards"
        lines.append(f"* '''{aw.get('title', '')}''' ({aw.get('year', '2026')}) – {aw.get('organization', '')} [{aw_url} Citation]")
    lines.append("")
    lines.append(f"== Media Coverage, Interviews & Podcasts ({len(media)}+ Features) ==")
    for m in media:
        m_url = m.get("primary_url") or "https://iamharshverma.github.io/page-media"
        lines.append(f"* [{m_url} \"{m.get('title', '')}\"] – ''{m.get('outlet', '')}'' ({m.get('date_display', m.get('year', ''))})")
    lines.append("")
    lines.append(f"== Verified Authority Profiles & External Links ({len(profiles)} Registries) ==")
    lines.append("* [https://iamharshverma.github.io/ Official Portfolio Website]")
    lines.append("* [https://iamharshverma.github.io/page-identity Official Google Knowledge Graph & Entity Verification Hub]")
    for prof in profiles:
        lines.append(f"* [{prof['url']} {prof['title']}] ({prof['category_label']} – <code>{prof['identifier']}</code>)")
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
    """Build the comprehensive Schema.org @graph JSON-LD object."""
    same_as_urls = [
        "https://www.wikidata.org/wiki/Q139827028",
        "http://www.wikidata.org/entity/Q139827028",
        "https://en.everybodywiki.com/Harsh_Verma_(Software_Engineer)",
        "https://iamharshverma.github.io/",
        "https://harshverma.bio/",
        "https://www.harshverma.me/",
    ]
    for p in profiles:
        u = p.get("url", "").strip()
        if u and u.startswith("http") and u not in same_as_urls:
            same_as_urls.append(u)

    for b in blogs:
        ap = b.get("author_profile", "")
        if ap and ap.startswith("http") and ap not in same_as_urls:
            same_as_urls.append(ap)

    member_of = [
        {
            "@type": "Organization",
            "@id": "http://www.wikidata.org/entity/Q131566",
            "name": "Institute of Electrical and Electronics Engineers (IEEE)",
            "url": "https://ieee-collabratec.ieee.org/app/p/HarshVerma59",
            "description": "Senior Member (SMIEEE) - Member ID: 95132014",
        },
        {
            "@type": "Organization",
            "name": "Forbes Technology Council",
            "url": "https://www.forbes.com/councils/forbestechcouncil/people/harshverma/",
            "description": "Official Council Member & Columnist",
        },
        {
            "@type": "Organization",
            "@id": "http://www.wikidata.org/entity/Q1814176",
            "name": "Sigma Xi, The Scientific Research Honor Society",
            "url": "https://www.sigmaxi.org/",
            "description": "Full Elected Member",
        },
        {
            "@type": "Organization",
            "@id": "http://www.wikidata.org/entity/Q919096",
            "name": "British Computer Society (BCS) - The Chartered Institute for IT",
            "url": "https://www.bcs.org/",
            "description": "Elected Fellow (FBCS)",
        },
        {
            "@type": "Organization",
            "@id": "http://www.wikidata.org/entity/Q1460885",
            "name": "Royal Society of Arts (RSA)",
            "url": "https://www.thersa.org/",
            "description": "Elected Fellow (FRSA)",
        },
    ]
    seen_assoc_names = {m["name"].lower() for m in member_of}
    for assoc in associations:
        t = assoc["title"]
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
        has_credentials.append({
            "@type": "EducationalOccupationalCredential",
            "name": a.get("title", ""),
            "credentialCategory": a.get("tier", "Global Award"),
            "dateCreated": str(a.get("year", "2026")),
            "url": cred_url,
            "recognizedBy": {
                "@type": "Organization",
                "name": a.get("organization", "International Awards Committee"),
            },
        })

    subject_of = [
        {
            "@type": "WebPage",
            "@id": "https://en.everybodywiki.com/Harsh_Verma_(Software_Engineer)",
            "name": "Harsh Verma (Software Engineer) - EverybodyWiki Biography",
            "url": "https://en.everybodywiki.com/Harsh_Verma_(Software_Engineer)",
        },
        {
            "@type": "Dataset",
            "@id": "https://www.wikidata.org/wiki/Q139827028",
            "name": "Harsh Verma - Wikidata Knowledge Graph Entity (Q139827028)",
            "url": "https://www.wikidata.org/wiki/Q139827028",
        },
    ]
    for m in media:
        m_type = "PodcastEpisode" if m.get("type") == "podcast" else "NewsArticle"
        m_url = m.get("primary_url") or f"{CANONICAL_SITE_URL}/page-media"
        subject_of.append({
            "@type": m_type,
            "headline": m.get("title", ""),
            "name": m.get("title", ""),
            "url": m_url,
            "datePublished": str(m.get("year", "2026")),
            "publisher": {
                "@type": "Organization",
                "name": m.get("outlet", "Global Media Outlet"),
            },
        })

    book_nodes = [
        {
            "@type": "Book",
            "@id": f"{CANONICAL_SITE_URL}/page-books#enterprise-ai-agents",
            "name": "Enterprise AI Agents: Build Your Authority and Lead the AI Agent Revolution",
            "alternateName": "Architectures, Production Protocols, and Operational Multi-Agent Systems",
            "author": {"@id": f"{CANONICAL_SITE_URL}/#person"},
            "url": f"{CANONICAL_SITE_URL}/page-books",
            "bookFormat": "https://schema.org/EBook",
            "inLanguage": "en",
            "genre": "Artificial Intelligence & Enterprise Architecture",
        },
        {
            "@type": "Book",
            "@id": f"{CANONICAL_SITE_URL}/page-books#autonomous-cyber-defense",
            "name": "Autonomous Cyber Defense: Adversarial Intelligence and Battleground Systems",
            "alternateName": "Zero-Trust Architecture, Threat Vector Modeling, and Autonomous Response",
            "author": {"@id": f"{CANONICAL_SITE_URL}/#person"},
            "url": f"{CANONICAL_SITE_URL}/page-books",
            "bookFormat": "https://schema.org/EBook",
            "inLanguage": "en",
            "genre": "Cybersecurity & Autonomous Defense",
        },
    ]

    article_nodes = []
    for b in blogs:
        if b.get("url"):
            article_nodes.append({
                "@type": "TechArticle",
                "headline": b["title"],
                "name": b["title"],
                "url": b["url"],
                "datePublished": b.get("date", "2026"),
                "author": {"@id": f"{CANONICAL_SITE_URL}/#person"},
                "publisher": {
                    "@type": "Organization",
                    "name": b.get("platform", "Forbes Technology Council"),
                },
            })

    paper_nodes = []
    for p in papers:
        p_node = {
            "@type": "ScholarlyArticle",
            "headline": p.get("title", ""),
            "name": p.get("title", ""),
            "author": {"@id": f"{CANONICAL_SITE_URL}/#person"},
            "datePublished": str(p.get("year", "")),
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
        "description": "Harsh Verma is an internationally recognized Principal Software Engineer in AI at Palo Alto Networks, Forbes Technology Council Member, IEEE Senior Member (SMIEEE), Fellow of the British Computer Society (FBCS), Fellow of the Royal Society of Arts (FRSA), Author, Keynote Speaker, and AI Researcher.",
        "url": f"{CANONICAL_SITE_URL}/",
        "mainEntityOfPage": {
            "@id": f"{CANONICAL_SITE_URL}/page-identity#profilepage",
        },
        "image": {
            "@type": "ImageObject",
            "@id": f"{CANONICAL_SITE_URL}/#headshot",
            "url": f"{CANONICAL_SITE_URL}/images/about/harsh_hero_clean.png",
            "caption": "Harsh Verma - Principal AI Software Engineer, Keynote Speaker, Author & Researcher",
        },
        "identifier": [
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
                "url": "https://www.stanford.edu/",
                "sameAs": "https://www.wikidata.org/wiki/Q41506",
            },
            {
                "@type": "CollegeOrUniversity",
                "@id": "http://www.wikidata.org/entity/Q1781394",
                "name": "University of Texas at Dallas",
                "url": "https://www.utdallas.edu/",
                "sameAs": "https://www.wikidata.org/wiki/Q1781394",
            },
            {
                "@type": "CollegeOrUniversity",
                "@id": "http://www.wikidata.org/entity/Q7903393",
                "name": "Uttarakhand Technical University",
                "url": "https://uktech.ac.in/",
                "sameAs": "https://www.wikidata.org/wiki/Q7903393",
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
        "name": "Harsh Verma Official Portfolio & Knowledge Graph Hub",
        "publisher": {"@id": f"{CANONICAL_SITE_URL}/#person"},
        "inLanguage": "en-US",
    }

    profile_page_node = {
        "@type": "ProfilePage",
        "@id": f"{CANONICAL_SITE_URL}/page-identity#profilepage",
        "url": f"{CANONICAL_SITE_URL}/page-identity",
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


def query_and_sync_wikidata(claims):
    """Query live Wikidata entity Q139827028 and attempt programmatic claim sync."""
    result = {
        "entity_id": WIKIDATA_QID,
        "entity_url": f"https://www.wikidata.org/wiki/{WIKIDATA_QID}",
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "live_reachable": False,
        "existing_labels": {},
        "existing_descriptions": {},
        "existing_claims_count": 0,
        "existing_properties": [],
        "missing_properties": [],
        "api_write_status": "unknown",
        "api_write_message": "",
    }

    existing_prop_val_pairs = set()
    try:
        url = f"{WIKIDATA_API}?action=wbgetentities&ids={WIKIDATA_QID}&format=json"
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
                    dv = c_item.get("mainsnak", {}).get("datavalue", {}).get("value")
                    if isinstance(dv, dict) and "id" in dv:
                        existing_prop_val_pairs.add((prop, dv["id"]))
                    elif isinstance(dv, str):
                        existing_prop_val_pairs.add((prop, dv))
    except Exception as e:
        result["api_write_message"] = f"Read warning: {str(e)}"

    # Determine missing claims
    missing_claims = []
    for c in claims:
        if (c["property"], c["value"]) not in existing_prop_val_pairs:
            missing_claims.append(c)

    result["missing_properties"] = [
        {"property": m["property"], "label": m["label"], "value": m["value_label"]}
        for m in missing_claims
    ]

    if not missing_claims and result["live_reachable"]:
        result["api_write_status"] = "synced"
        result["api_write_message"] = f"All {len(claims)} canonical claims are live on Wikidata {WIKIDATA_QID}!"
        return result

    # Attempt programmatic edit via MediaWiki API (CSRF token + wbeditentity for missing claims)
    try:
        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        opener.addheaders = [("User-Agent", USER_AGENT)]

        wd_user = os.environ.get("WIKIDATA_USER") or os.environ.get("WIKIDATA_BOT_USER")
        wd_pass = os.environ.get("WIKIDATA_PASS") or os.environ.get("WIKIDATA_BOT_PASS")

        if wd_user and wd_pass:
            lt_resp = opener.open(f"{WIKIDATA_API}?action=query&meta=tokens&type=login&format=json", timeout=12)
            lt_data = json.loads(lt_resp.read().decode("utf-8"))
            login_token = lt_data["query"]["tokens"]["logintoken"]

            login_payload = urllib.parse.urlencode({
                "action": "login",
                "lgname": wd_user,
                "lgpassword": wd_pass,
                "lgtoken": login_token,
                "format": "json",
            }).encode("utf-8")
            opener.open(WIKIDATA_API, data=login_payload, timeout=12)

        tok_resp = opener.open(f"{WIKIDATA_API}?action=query&meta=tokens&format=json", timeout=12)
        tok_data = json.loads(tok_resp.read().decode("utf-8"))
        csrf_token = tok_data.get("query", {}).get("tokens", {}).get("csrftoken", "+\\")

        claim_objs = []
        for c in missing_claims:
            prop = c["property"]
            val = c["value"]
            if c["type"] == "wikibase-entityid":
                num_id = int(val.lstrip("Q"))
                datavalue = {
                    "value": {"entity-type": "item", "numeric-id": num_id, "id": val},
                    "type": "wikibase-entityid",
                }
            else:
                datavalue = {"value": val, "type": "string"}

            claim_obj = {
                "mainsnak": {
                    "snaktype": "value",
                    "property": prop,
                    "datavalue": datavalue,
                },
                "type": "statement",
                "rank": "normal",
            }
            if c.get("reference_url"):
                claim_obj["references"] = [
                    {
                        "snaks": {
                            "P854": [
                                {
                                    "snaktype": "value",
                                    "property": "P854",
                                    "datavalue": {"value": c["reference_url"], "type": "string"},
                                }
                            ]
                        }
                    }
                ]
            claim_objs.append(claim_obj)

        entity_payload = {
            "descriptions": {
                "en": {
                    "language": "en",
                    "value": "Principal AI Software Engineer at Palo Alto Networks, Keynote Speaker, Author, and Researcher",
                }
            },
            "aliases": {
                "en": [
                    {"language": "en", "value": "Harsh Verma (Software Engineer)"},
                    {"language": "en", "value": "iamharshverma"},
                ]
            },
            "claims": claim_objs,
        }

        post_data = urllib.parse.urlencode({
            "action": "wbeditentity",
            "id": WIKIDATA_QID,
            "data": json.dumps(entity_payload),
            "summary": "Synchronize canonical authority identifiers (ORCID, Google Scholar, Stanford/UTD/UTU, IEEE/BCS/RSA/Sigma Xi Fellowships) from official Knowledge Graph Hub",
            "token": csrf_token,
            "format": "json",
        }).encode("utf-8")

        edit_resp = opener.open(WIKIDATA_API, data=post_data, timeout=15)
        edit_json = json.loads(edit_resp.read().decode("utf-8"))

        if "success" in edit_json:
            result["api_write_status"] = "synced"
            new_ent = edit_json.get("entity", {})
            result["lastrevid"] = new_ent.get("lastrevid", result.get("lastrevid"))
            new_claims = new_ent.get("claims", {})
            if new_claims:
                result["existing_properties"] = sorted(list(new_claims.keys()))
                result["existing_claims_count"] = sum(len(v) for v in new_claims.values())
            result["missing_properties"] = []
            result["api_write_message"] = (
                f"Successfully updated Wikidata {WIKIDATA_QID} live via Action API (revision {result['lastrevid']}, {result['existing_claims_count']} total claims)!"
            )
        elif "error" in edit_json:
            err_code = edit_json["error"].get("code", "unknown")
            err_info = edit_json["error"].get("info", "")
            result["api_write_status"] = f"requires_auth ({err_code})"
            result["api_write_message"] = (
                f"Wikidata API returned '{err_code}': {err_info}. "
                f"Generated QuickStatements v2 batch (data/wikidata-quickstatements.txt) for 1-click browser execution or WIKIDATA_USER/WIKIDATA_PASS bot sync."
            )
    except Exception as e:
        result["api_write_status"] = "fallback_ready"
        result["api_write_message"] = f"API write note: {str(e)}. QuickStatements batch ready."

    return result


def query_and_sync_everybodywiki(wikitext):
    """Query live EverybodyWiki article and attempt programmatic edit."""
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
        if ew_user and ew_pass:
            lt_resp = opener.open(f"{EVERYBODYWIKI_API}?action=query&meta=tokens&type=login&format=json", timeout=12)
            lt_data = json.loads(lt_resp.read().decode("utf-8"))
            login_token = lt_data["query"]["tokens"]["logintoken"]
            login_payload = urllib.parse.urlencode({
                "action": "login",
                "lgname": ew_user,
                "lgpassword": ew_pass,
                "lgtoken": login_token,
                "format": "json",
            }).encode("utf-8")
            opener.open(EVERYBODYWIKI_API, data=login_payload, timeout=12)

        tok_resp = opener.open(f"{EVERYBODYWIKI_API}?action=query&meta=tokens&format=json", timeout=12)
        tok_data = json.loads(tok_resp.read().decode("utf-8"))
        csrf_token = tok_data.get("query", {}).get("tokens", {}).get("csrftoken", "+\\")

        edit_payload = urllib.parse.urlencode({
            "action": "edit",
            "title": EVERYBODYWIKI_TITLE,
            "text": wikitext,
            "summary": "Update biography with verified 2026 awards, 27+ peer-reviewed publications, Palo Alto Networks role, and Wikidata Q139827028 authority links",
            "token": csrf_token,
            "format": "json",
        }).encode("utf-8")

        edit_resp = opener.open(EVERYBODYWIKI_API, data=edit_payload, timeout=15)
        edit_json = json.loads(edit_resp.read().decode("utf-8"))

        if edit_json.get("edit", {}).get("result") == "Success":
            result["api_write_status"] = "synced"
            result["newrevid"] = edit_json["edit"].get("newrevid")
            result["api_write_message"] = f"Successfully updated EverybodyWiki article (newrevid: {result['newrevid']})."
        elif "error" in edit_json:
            err_code = edit_json["error"].get("code", "unknown")
            err_info = edit_json["error"].get("info", "")
            result["api_write_status"] = f"requires_auth ({err_code})"
            result["api_write_message"] = (
                f"EverybodyWiki API requires authenticated session ({err_code}). "
                f"Full 36KB MediaWiki biography generated in data/everybodywiki-article.wiki with 1-Click Pre-filled Editor launcher in page-identity."
            )
        else:
            result["api_write_status"] = "captcha_or_login_required"
            result["api_write_message"] = (
                f"EverybodyWiki requires authenticated session or anti-bot verification. "
                f"Full Wikitext ready in data/everybodywiki-article.wiki."
            )
    except Exception as e:
        result["api_write_status"] = "fallback_ready"
        result["api_write_message"] = f"EverybodyWiki API note: {str(e)}. Wikitext payload ready."

    return result


def main():
    print("=== Building Canonical Google Knowledge Graph & Executing Wiki Sync ===")
    profiles = extract_verified_profiles()
    media = load_json_file("media_data.json")
    awards = load_json_file("awards_data.json")
    papers = load_json_file("papers_data.json")
    blogs = extract_blogs()
    associations = extract_associations()
    books = [
        {
            "id": "book-enterprise-ai-agents",
            "title": "Enterprise AI Agents: Build Your Authority and Lead the AI Agent Revolution",
            "subtitle": "Architectures, Production Protocols, and Operational Multi-Agent Systems",
            "year": "2025",
            "url": f"{CANONICAL_SITE_URL}/page-books",
            "description": "Definitive guide to designing, architecting, and deploying resilient autonomous AI agents, deterministic guardrails, and memory graphs at enterprise scale.",
        },
        {
            "id": "book-autonomous-cyber-defense",
            "title": "Autonomous Cyber Defense: Adversarial Intelligence and Battleground Systems",
            "subtitle": "Zero-Trust Architecture, Threat Vector Modeling, and Autonomous Response",
            "year": "2026",
            "url": f"{CANONICAL_SITE_URL}/page-books",
            "description": "Examines modern threat landscapes and how autonomous machine intelligence dynamically detects, isolates, and neutralizes cyber threats in high-throughput networks.",
        },
    ]

    print(
        f"Loaded {len(profiles)} Verified Profiles, {len(media)} Media Features, "
        f"{len(awards)} Awards, {len(blogs)} Blogs/Columns, {len(books)} Books, "
        f"{len(papers)} Research Papers, {len(associations)} Associations."
    )

    wd_claims = build_wikidata_claims_manifest()
    qs_text = generate_quickstatements(wd_claims)
    qs_path = os.path.join(DATA_DIR, "wikidata-quickstatements.txt")
    with open(qs_path, "w", encoding="utf-8") as f:
        f.write(qs_text)
    print(f"Wrote QuickStatements v2 batch ({len(wd_claims)} claims) to {qs_path}")

    wikitext = generate_everybodywiki_wikitext(profiles, media, awards, blogs, books, papers, associations)
    wiki_path = os.path.join(DATA_DIR, "everybodywiki-article.wiki")
    with open(wiki_path, "w", encoding="utf-8") as f:
        f.write(wikitext)
    print(f"Wrote EverybodyWiki MediaWiki markup ({len(wikitext)} chars) to {wiki_path}")

    schema_graph = build_schema_org_graph(profiles, media, awards, blogs, books, papers, associations)

    print(f"Querying & syncing Wikidata ({WIKIDATA_QID})...")
    wd_sync = query_and_sync_wikidata(wd_claims)
    print(f"  -> Wikidata Status: {wd_sync['api_write_status']} | {wd_sync['api_write_message']}")

    print(f"Querying & syncing EverybodyWiki ({EVERYBODYWIKI_TITLE})...")
    ew_sync = query_and_sync_everybodywiki(wikitext)
    print(f"  -> EverybodyWiki Status: {ew_sync['api_write_status']} | {ew_sync['api_write_message']}")

    sync_status = {
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "wikidata": wd_sync,
        "everybodywiki": ew_sync,
    }
    sync_status_path = os.path.join(DATA_DIR, "wiki-sync-status.json")
    with open(sync_status_path, "w", encoding="utf-8") as f:
        json.dump(sync_status, f, indent=2)

    master_payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "entity_id": f"{CANONICAL_SITE_URL}/#person",
        "wikidata_qid": WIKIDATA_QID,
        "wikidata_url": f"https://www.wikidata.org/wiki/{WIKIDATA_QID}",
        "everybodywiki_title": EVERYBODYWIKI_TITLE,
        "everybodywiki_url": f"https://en.everybodywiki.com/{EVERYBODYWIKI_TITLE}",
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


if __name__ == "__main__":
    main()
