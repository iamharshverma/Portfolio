#!/usr/bin/env python3
"""
scripts/export_all_sections_json.py
===================================
Exports full, comprehensive, and detailed JSON data files for each major section
across Harsh Verma's portfolio website:
1. data/judging_engagements.json
2. data/speaking_engagements.json
3. data/keynote_engagements.json
4. data/media_features.json
5. data/awards_and_honors.json
6. data/research_publications.json
7. data/books_and_volumes.json
8. data/blog_articles.json
9. data/verified_profiles.json
10. data/memberships_and_associations.json
11. data/about.json
12. data/professional_work.json
13. data/slides.json
14. data/projects_certification.json
15. data/social_posts.json
16. data/advisory_and_board.json
17. data/patents.json
18. data/media_distribution_analytics.json
19. data/social_partnerships.json
20. data/speaker_profile.json

Every entry is structured as a direct key-value object containing verified links,
dates, engagement types, detailed descriptions, organizers, and all related details.
"""

import os
import re
import json

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)


def clean_text(html_str):
    if not html_str:
        return ""
    text = re.sub(r"<[^>]+>", " ", html_str)
    text = (
        text.replace("&amp;", "&")
        .replace("&bull;", "•")
        .replace("&quot;", '"')
        .replace("&#39;", "'")
        .replace("&lt;", "<")
        .replace("&gt;", ">")
    )
    return re.sub(r"\s+", " ", text).strip()


CANONICAL_BASE = "https://www.harshverma.me"


def to_canonical_url(url):
    if not url:
        return ""
    u = url.strip()
    if not u or u.startswith("javascript:") or u.startswith("mailto:"):
        return ""
    if u.startswith("http://") or u.startswith("https://"):
        return u
    if u.startswith("#"):
        return f"{CANONICAL_BASE}/{u}"
    return f"{CANONICAL_BASE}/{u.lstrip('/')}"


def dedup_links(raw_links):
    seen = set()
    out = []
    for item in raw_links:
        if not isinstance(item, dict):
            continue
        url = (item.get("url") or "").strip()
        if not url:
            continue
        norm_key = url.rstrip("/")
        if norm_key in seen:
            continue
        seen.add(norm_key)
        entry = {"label": (item.get("label") or "Open Link").strip(), "url": url}
        if item.get("icon"):
            entry["icon"] = item["icon"]
        out.append(entry)
    return out


def parse_event_cards():
    """Parse all event cards from page-events.html / page-speaker.html."""
    events_path = os.path.join(ROOT_DIR, "page-events.html")
    with open(events_path, "r", encoding="utf-8") as f:
        html = f.read()

    card_matches = re.finditer(
        r'<div class="col-lg-6 col-md-12 mb-4 event-card-item"[^>]*data-category="([^"]+)"([\s\S]*?)(?=(?:<div class="col-lg-6 col-md-12 mb-4 event-card-item"|<div id="noEventsNotice"|<!-- End Event Cards|<section|\Z))',
        html,
    )

    parsed_events = []
    for match in card_matches:
        category = match.group(1).strip()
        chunk = match.group(2)

        # ID from copyEventInfo button
        id_match = re.search(r"copyEventInfo\('([^']+)'", chunk)
        item_id = id_match.group(1).strip() if id_match else ""

        # Title
        title_match = re.search(r'<h4 class="event-card-title[^"]*">\s*([\s\S]*?)\s*</h4>', chunk)
        title = clean_text(title_match.group(1)) if title_match else ""

        # Org & Role
        org_match = re.search(r'<div class="event-card-org[^"]*">\s*([\s\S]*?)\s*</div>', chunk)
        org_raw = org_match.group(1) if org_match else ""
        org_parts = org_raw.split("&bull;")
        organizer = clean_text(org_parts[0]) if len(org_parts) > 0 else ""
        role = clean_text(org_parts[1]) if len(org_parts) > 1 else ""

        # Location & Date
        loc_date_match = re.search(r'<div class="event-org-name[^"]*">\s*([\s\S]*?)\s*</div>', chunk)
        loc_date_raw = loc_date_match.group(1) if loc_date_match else ""
        loc_parts = loc_date_raw.split("&bull;")
        location = clean_text(loc_parts[0]) if len(loc_parts) > 0 else ""
        date_str = clean_text(loc_parts[1]) if len(loc_parts) > 1 else ""

        # Badge Label
        badge_match = re.search(r'<span class="badge[^"]*"[^>]*>\s*([\s\S]*?)\s*</span>', chunk)
        badge_label = clean_text(badge_match.group(1)) if badge_match else ""

        # Description
        desc_match = re.search(r'<p class="event-card-desc[^"]*">\s*([\s\S]*?)\s*</p>', chunk)
        description = clean_text(desc_match.group(1)) if desc_match else ""

        # Tags
        tags = [clean_text(t) for t in re.findall(r'<span class="event-tag-pill[^"]*">\s*([\s\S]*?)\s*</span>', chunk)]

        # Links
        links = []
        for l_match in re.finditer(r'<a\s+[^>]*href="([^"]+)"[^>]*>([\s\S]*?)</a>', chunk):
            url = to_canonical_url(l_match.group(1).strip())
            label = clean_text(l_match.group(2)) or "View Details"
            if url:
                links.append({"label": label, "url": url})
        links = dedup_links(links)

        primary_url = links[0]["url"] if links else "https://www.harshverma.me/page-events"

        if not item_id:
            item_id = "event-" + re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")

        parsed_events.append({
            "id": item_id,
            "category": category,
            "title": title,
            "role": role or badge_label,
            "organizer": organizer,
            "date": date_str,
            "location": location,
            "badge": badge_label,
            "description": description,
            "tags": tags,
            "primary_url": primary_url,
            "links": links,
        })

    return parsed_events


def parse_keynote_cinema_videos():
    """Parse the 10 headline keynote videos from page-events.html / page-speaker.html."""
    events_path = os.path.join(ROOT_DIR, "page-events.html")
    with open(events_path, "r", encoding="utf-8") as f:
        html = f.read()

    match = re.search(r"var keynoteVideosList\s*=\s*(\[[\s\S]*?\]);", html)
    if not match:
        return []

    raw_json = match.group(1)
    try:
        videos = json.loads(raw_json)
        return videos
    except Exception as e:
        print("Error parsing keynoteVideosList json:", e)
        return []


def export_judging():
    """1. Export judging & jury appointments."""
    all_events = parse_event_cards()
    judging_list = []

    for ev in all_events:
        if ev["category"] == "judging" or "judge" in ev["role"].lower() or "committee" in ev["role"].lower() or "mentor" in ev["role"].lower():
            judging_list.append({
                "id": ev["id"],
                "event_title": ev["title"],
                "role": ev["role"] or "Judge & Selection Committee",
                "organizer": ev["organizer"],
                "date": ev["date"],
                "location": ev["location"],
                "engagement_type": "Hackathon & Pitch Competition Judging / Startup Evaluation",
                "badge": ev["badge"],
                "description": ev["description"],
                "evaluation_focus": ev["tags"],
                "primary_url": ev["primary_url"],
                "links": ev["links"],
            })

    output_path = os.path.join(DATA_DIR, "judging_engagements.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(judging_list, f, indent=2, ensure_ascii=False)
    print(f"Exported {len(judging_list)} judging engagements to {output_path}")
    return judging_list


def export_speaking():
    """2. Export conference speaking, session chairs, and panel discussions."""
    all_events = parse_event_cards()
    speaking_list = []

    for ev in all_events:
        if ev["category"] in ("conferences", "panels") or "keynote" in ev["title"].lower() or "panel" in ev["title"].lower() or "chair" in ev["role"].lower():
            speaking_list.append({
                "id": ev["id"],
                "session_title": ev["title"],
                "event_name": ev["organizer"] or ev["title"],
                "engagement_type": "Panel Discussion" if ev["category"] == "panels" else "Conference Session / Keynote Chair",
                "role": ev["role"] or "Speaker & Subject Matter Expert",
                "date": ev["date"],
                "location_or_platform": ev["location"],
                "description": ev["description"],
                "key_topics": ev["tags"],
                "primary_url": ev["primary_url"],
                "links": ev["links"],
            })

    output_path = os.path.join(DATA_DIR, "speaking_engagements.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(speaking_list, f, indent=2, ensure_ascii=False)
    print(f"Exported {len(speaking_list)} speaking engagements to {output_path}")
    return speaking_list


def export_keynotes():
    """3. Export major headline keynote addresses with recordings and slide decks."""
    videos = parse_keynote_cinema_videos()
    keynotes_list = []

    for v in videos:
        rec_url = to_canonical_url(v.get("recording_url", ""))
        slides_url = to_canonical_url(v.get("slides_url", ""))
        links = dedup_links([
            {"label": "Watch Recording", "url": rec_url},
            {"label": "Interactive Slides", "url": slides_url},
        ])
        keynotes_list.append({
            "id": f"keynote-{v.get('id', '')}",
            "keynote_title": v.get("title", ""),
            "event_name": v.get("outlet", ""),
            "organizer": v.get("outlet", "").split("(")[0].strip(),
            "date": v.get("date", ""),
            "duration": v.get("duration", ""),
            "format": "Keynote Cinema & Recorded Address",
            "youtube_id": v.get("id", ""),
            "recording_url": rec_url,
            "slides_url": slides_url,
            "thumbnail_url": v.get("thumb", ""),
            "synopsis": v.get("desc", ""),
            "key_takeaways": v.get("tags", []),
            "primary_url": rec_url or slides_url,
            "links": links,
        })

    # Also include the conference keynotes from event cards
    all_events = parse_event_cards()
    for ev in all_events:
        if "keynote" in ev["title"].lower() and not any(k["keynote_title"] == ev["title"] for k in keynotes_list):
            ev_links = dedup_links(ev.get("links", []) + ([{"label": "Session Link", "url": ev["primary_url"]}] if ev.get("primary_url") else []))
            inferred_slides = next((l["url"] for l in ev_links if "smart-slides" in l["url"]), "")
            keynotes_list.append({
                "id": ev["id"],
                "keynote_title": ev["title"],
                "event_name": ev["organizer"],
                "organizer": ev["organizer"],
                "date": ev["date"],
                "duration": "Keynote Address",
                "format": "In-Person / Virtual Conference Keynote",
                "youtube_id": "",
                "recording_url": "",
                "slides_url": inferred_slides,
                "thumbnail_url": "",
                "synopsis": ev["description"],
                "key_takeaways": ev["tags"],
                "primary_url": ev["primary_url"],
                "links": ev_links,
            })

    output_path = os.path.join(DATA_DIR, "keynote_engagements.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(keynotes_list, f, indent=2, ensure_ascii=False)
    print(f"Exported {len(keynotes_list)} headline keynotes to {output_path}")
    return keynotes_list


def export_media():
    """4. Export 45 media features and press features with normalized canonical links."""
    media_path = os.path.join(ROOT_DIR, "media_data.json")
    with open(media_path, "r", encoding="utf-8") as f:
        media = json.load(f)

    enriched_media = []
    for item in media:
        entry = dict(item)
        purl = to_canonical_url(entry.get("primary_url", ""))
        if purl:
            entry["primary_url"] = purl
        if entry.get("distribution_report_url"):
            entry["distribution_report_url"] = to_canonical_url(entry["distribution_report_url"])

        raw_links = []
        if purl:
            raw_links.append({"label": f"Read on {entry.get('outlet', 'Source')}", "url": purl})
        for lk in entry.get("links", []):
            lk_copy = dict(lk)
            lk_copy["url"] = to_canonical_url(lk_copy.get("url", ""))
            raw_links.append(lk_copy)
        if entry.get("distribution_report_url"):
            raw_links.append({
                "label": "Distribution Report (PDF)",
                "url": entry["distribution_report_url"],
                "icon": "mdi-file-pdf-box",
            })
        # Preserve original order of item['links'] first, then ensure primary & distribution report included
        ordered_links = []
        for lk in entry.get("links", []):
            lk_copy = dict(lk)
            lk_copy["url"] = to_canonical_url(lk_copy.get("url", ""))
            ordered_links.append(lk_copy)
        ordered_links.extend(raw_links)
        entry["links"] = dedup_links(ordered_links)
        enriched_media.append(entry)

    output_path = os.path.join(DATA_DIR, "media_features.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(enriched_media, f, indent=2, ensure_ascii=False)
    print(f"Exported {len(enriched_media)} media features to {output_path}")
    return enriched_media


def export_awards():
    """5. Export 27 prestigious awards and global technology honors with primary_url & complete links."""
    awards_path = os.path.join(ROOT_DIR, "awards_data.json")
    with open(awards_path, "r", encoding="utf-8") as f:
        awards = json.load(f)

    enriched_awards = []
    for a in awards:
        entry = dict(a)
        norm_links = []
        for lk in entry.get("links", []):
            lk_copy = dict(lk)
            lk_copy["url"] = to_canonical_url(lk_copy.get("url", ""))
            norm_links.append(lk_copy)
        norm_links = dedup_links(norm_links)
        purl = to_canonical_url(entry.get("primary_url") or "") or (norm_links[0]["url"] if norm_links else f"{CANONICAL_BASE}/page-awards")
        entry["primary_url"] = purl
        entry["url"] = purl
        entry["links"] = norm_links
        enriched_awards.append(entry)

    output_path = os.path.join(DATA_DIR, "awards_and_honors.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(enriched_awards, f, indent=2, ensure_ascii=False)
    print(f"Exported {len(enriched_awards)} awards & honors to {output_path}")
    return enriched_awards


def export_publications():
    """6. Export 27 peer-reviewed publications and patents with full DOI, venue, PDF & ResearchGate links."""
    papers_path = os.path.join(ROOT_DIR, "papers_data.json")
    with open(papers_path, "r", encoding="utf-8") as f:
        papers = json.load(f)

    enriched_papers = []
    for p in papers:
        entry = dict(p)
        primary_link = to_canonical_url(entry.get("link", ""))
        doi = (entry.get("doi") or "").strip()
        doi_url = f"https://doi.org/{doi}" if (doi and not doi.startswith("http")) else to_canonical_url(doi)
        alt_link = to_canonical_url(entry.get("alt_link", ""))
        alt_label = (entry.get("alt_label") or "Alternate Link").strip()

        links = dedup_links([
            {"label": "Read Paper", "url": primary_link},
            {"label": "DOI", "url": doi_url},
            {"label": alt_label, "url": alt_link},
            {"label": "Google Scholar Profile", "url": "https://scholar.google.com/citations?hl=en&user=zSt9oRMAAAAJ"},
            {"label": "ORCID Record", "url": "https://orcid.org/0000-0003-2134-2600"},
        ])
        entry["primary_url"] = primary_link or doi_url or alt_link
        if doi_url:
            entry["doi_url"] = doi_url
        entry["author_profiles"] = [
            {"label": "Google Scholar", "url": "https://scholar.google.com/citations?hl=en&user=zSt9oRMAAAAJ"},
            {"label": "ORCID", "url": "https://orcid.org/0000-0003-2134-2600"},
            {"label": "Academia.edu", "url": "https://mygsb.academia.edu/harshverma"},
            {"label": "ResearchGate", "url": "https://www.researchgate.net/profile/Harsh-Verma-43"},
            {"label": "IEEE Xplore Author", "url": "https://ieeexplore.ieee.org/author/37089143797"},
        ]
        entry["links"] = links
        enriched_papers.append(entry)

    output_path = os.path.join(DATA_DIR, "research_publications.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(enriched_papers, f, indent=2, ensure_ascii=False)
    print(f"Exported {len(enriched_papers)} research publications & patents to {output_path}")
    return enriched_papers


def export_books():
    """7. Export authored books and editorial monograph reviews."""
    kg_path = os.path.join(ROOT_DIR, "data", "knowledge-graph.json")
    with open(kg_path, "r", encoding="utf-8") as f:
        kg = json.load(f)

    books_raw = kg.get("entities", {}).get("books", [])

    books_detailed = [
        {
            "id": "book-enterprise-ai-agents",
            "title": "Beyond AI Engineering: From Creator to Curator",
            "subtitle": "Mastering the Human and Strategic Dimensions of Curating AI Systems",
            "role": "Authored Book (Lead Author)",
            "publication_status": "Published / Enterprise Edition",
            "publication_date": "2026",
            "publisher": "Palo Alto Technical Press & Enterprise AI Publishing",
            "synopsis": "Comprehensive treatise on the architectural transition from generative prompt wrappers to autonomous agentic architectures. Details multi-agent topologies, tool execution protocols, deterministic self-healing loops, zero-trust verification harnesses, and strategic enterprise AI curation.",
            "key_themes": [
                "Agentic Topologies",
                "Deterministic Validation",
                "Autonomous Threat Modeling",
                "Self-Healing Agent Workflows",
                "Enterprise AI Governance"
            ],
            "catalog_url": "https://www.beyondaiengineering.com/",
            "website_url": "https://www.beyondaiengineering.com/",
            "url": "https://www.beyondaiengineering.com/",
            "page_url": "https://www.harshverma.me/page-books#book1",
            "partner_url": "https://profilegenius.careeraccelerator.net/",
            "cover_image": "images/books/book_creator_to_curator.png",
            "links": [
                {"label": "Official Book Website", "url": "https://www.beyondaiengineering.com/"},
                {"label": "ProfileGenius by Career Accelerator (Featured Platform)", "url": "https://profilegenius.careeraccelerator.net/"},
                {"label": "Portfolio Books Hub", "url": "https://www.harshverma.me/page-books#book1"}
            ]
        },
        {
            "id": "book-autonomous-cyber-defense",
            "title": "AI vs. AI: Engineering the Cybersecurity Counteroffensive",
            "subtitle": "Architecting Autonomous AI Defenses Against Intelligent Adversaries",
            "role": "Authored Book (Lead Author)",
            "publication_status": "Published / Cyber Defense Edition",
            "publication_date": "2026",
            "publisher": "Cyber Defense Press",
            "synopsis": "Blueprint for designing autonomous machine-speed cyber defense fabrics capable of neutralizing automated adversarial agents. Formulates proactive prompt provenance, multi-agent behavioral containment, decentralized threat sharing, and automated runtime mitigation.",
            "key_themes": [
                "Autonomous Cyber Defense",
                "Adversarial AI Mitigation",
                "Machine-Speed Incident Response",
                "Zero-Trust Agent Governance",
                "Enterprise Security Architecture"
            ],
            "catalog_url": "https://www.beyondaivsai.com/",
            "website_url": "https://www.beyondaivsai.com/",
            "url": "https://www.beyondaivsai.com/",
            "page_url": "https://www.harshverma.me/page-books#book2",
            "cover_image": "images/books/book_cybersecurity_counteroffensive.png",
            "links": [
                {"label": "Official Book Website", "url": "https://www.beyondaivsai.com/"},
                {"label": "Portfolio Books Hub", "url": "https://www.harshverma.me/page-books#book2"}
            ]
        },
        {
            "id": "book-review-ai-ethics-in-action",
            "title": "AI Ethics in Action",
            "subtitle": "Critical Perspectives on Enterprise AI Transparency and Alignment",
            "role": "Technical Book Reviewer",
            "publication_status": "Reviewed (Technical Peer Review Completed)",
            "review_status": "Reviewed",
            "publication_date": "2025",
            "publisher": "Packt Publishing",
            "synopsis": "Official peer-reviewed technical evaluation of operational AI ethics frameworks, examining fairness metrics, algorithmic auditing, explainability in production deployments, and human-in-the-loop oversight.",
            "key_themes": ["AI Ethics", "Algorithmic Transparency", "Explainable AI (XAI)", "Responsible AI"],
            "catalog_url": "https://packt.link/MuEPg",
            "url": "https://packt.link/MuEPg",
            "page_url": "https://www.harshverma.me/page-books#reviewed-books",
            "cover_image": "images/books/review_ai_ethics.png",
            "links": [
                {"label": "View Book (Packt)", "url": "https://packt.link/MuEPg"},
                {"label": "Portfolio Reviewed Volumes", "url": "https://www.harshverma.me/page-books#reviewed-books"}
            ]
        },
        {
            "id": "book-review-hands-on-ai-dev",
            "title": "Hands-On AI Dev with Python",
            "subtitle": "Engineering Scalable Machine Learning Pipelines in Production",
            "role": "Technical Book Reviewer",
            "publication_status": "Reviewed (Technical Peer Review Completed)",
            "review_status": "Reviewed",
            "publication_date": "2025",
            "publisher": "Packt Publishing",
            "synopsis": "Rigorous technical review of end-to-end Python machine learning architectures, microservice model serving, distributed caching, and performance benchmarking for high-scale enterprise systems.",
            "key_themes": ["Python ML", "High-Throughput Pipelines", "Production AI", "Distributed Systems"],
            "catalog_url": "https://packt.link/pZ2C5",
            "url": "https://packt.link/pZ2C5",
            "page_url": "https://www.harshverma.me/page-books#reviewed-books",
            "cover_image": "images/books/review_hands_on_ai.png",
            "links": [
                {"label": "View Book (Packt)", "url": "https://packt.link/pZ2C5"},
                {"label": "Portfolio Reviewed Volumes", "url": "https://www.harshverma.me/page-books#reviewed-books"}
            ]
        },
        {
            "id": "book-review-leadership-ai",
            "title": "Leadership at the Helm of AI",
            "subtitle": "Executive Playbook for Navigating Disruptive AI Transformation",
            "role": "Technical Book Reviewer",
            "publication_status": "Reviewed (Technical Peer Review Completed)",
            "review_status": "Reviewed",
            "publication_date": "2025",
            "publisher": "Packt Publishing",
            "synopsis": "Technical evaluation of executive strategies for organizational AI adoption, balancing ROI velocity against architectural resilience, technical debt, and enterprise workforce upskilling.",
            "key_themes": ["AI Leadership", "Enterprise Strategy", "Organizational Transformation", "AI ROI"],
            "catalog_url": "https://www.packtpub.com/",
            "url": "https://www.packtpub.com/",
            "page_url": "https://www.harshverma.me/page-books#reviewed-books",
            "cover_image": "images/books/review_leadership_ai.png",
            "links": [
                {"label": "Packt Publishing Catalog", "url": "https://www.packtpub.com/"},
                {"label": "Portfolio Reviewed Volumes", "url": "https://www.harshverma.me/page-books#reviewed-books"}
            ]
        },
        {
            "id": "book-review-python-algo-trading",
            "title": "Python for Algorithmic Trading Cookbook",
            "subtitle": "Recipes for Designing and Testing Real-Time Quantitative Trading Strategies",
            "role": "Technical Book Reviewer",
            "publication_status": "Reviewed (Technical Peer Review Completed)",
            "review_status": "Reviewed",
            "publication_date": "2024",
            "publisher": "Packt Publishing",
            "synopsis": "Comprehensive technical review of low-latency algorithmic trading backends, real-time market data streaming with Kafka and NumPy, and quantitative risk management architectures.",
            "key_themes": ["Algorithmic Trading", "Quantitative Systems", "Real-Time Streaming", "Python FinTech"],
            "catalog_url": "https://packt.link/8jmuy",
            "url": "https://packt.link/8jmuy",
            "page_url": "https://www.harshverma.me/page-books#reviewed-books",
            "cover_image": "images/books/review_python_trading.png",
            "links": [
                {"label": "View Book (Packt)", "url": "https://packt.link/8jmuy"},
                {"label": "Portfolio Reviewed Volumes", "url": "https://www.harshverma.me/page-books#reviewed-books"}
            ]
        },
        {
            "id": "book-review-ml-genai-marketing",
            "title": "Machine Learning & Generative AI for Marketing",
            "subtitle": "Practical Techniques for Personalization, Content Generation, and Customer Intelligence",
            "role": "Technical Book Reviewer",
            "publication_status": "Reviewed (Technical Peer Review Completed)",
            "review_status": "Reviewed",
            "publication_date": "2024",
            "publisher": "Packt Publishing",
            "synopsis": "Expert peer review of generative AI workflows for personalized customer experiences, predictive churn analytics, and multi-modal campaign orchestration at scale.",
            "key_themes": ["Generative AI", "Customer Intelligence", "Multi-Modal AI", "Predictive Analytics"],
            "catalog_url": "https://www.packtpub.com/",
            "url": "https://www.packtpub.com/",
            "page_url": "https://www.harshverma.me/page-books#reviewed-books",
            "cover_image": "images/books/review_genai_marketing.png",
            "links": [
                {"label": "Packt Publishing Catalog", "url": "https://www.packtpub.com/"},
                {"label": "Portfolio Reviewed Volumes", "url": "https://www.harshverma.me/page-books#reviewed-books"}
            ]
        },
        {
            "id": "book-review-tensorflow-workshop",
            "title": "The TensorFlow Workshop",
            "subtitle": "A New, Interactive Approach to Learning Deep Neural Networks",
            "role": "Technical Book Reviewer",
            "publication_status": "Reviewed (Technical Peer Review Completed)",
            "review_status": "Reviewed",
            "publication_date": "2023",
            "publisher": "Packt Publishing",
            "synopsis": "Thorough technical review covering deep neural network fundamentals, convolutional and recurrent layers, distributed training on GPUs/TPUs, and TensorFlow Lite edge deployments.",
            "key_themes": ["TensorFlow", "Deep Learning", "Edge AI", "Distributed Training"],
            "catalog_url": "https://www.packtpub.com/",
            "url": "https://www.packtpub.com/",
            "page_url": "https://www.harshverma.me/page-books#reviewed-books",
            "cover_image": "images/books/review_tensorflow.png",
            "links": [
                {"label": "Packt Publishing Catalog", "url": "https://www.packtpub.com/"},
                {"label": "Portfolio Reviewed Volumes", "url": "https://www.harshverma.me/page-books#reviewed-books"}
            ]
        }
    ]

    author_profile_links = [
        {"label": "Author LinkedIn", "url": "https://www.linkedin.com/in/harshverma59/"},
        {"label": "Author Google Scholar", "url": "https://scholar.google.com/citations?hl=en&user=zSt9oRMAAAAJ"},
        {"label": "Author Portfolio Books Hub", "url": "https://www.harshverma.me/page-books"},
    ]
    for b in books_detailed:
        b["primary_url"] = b.get("url") or b.get("catalog_url") or b.get("page_url", "")
        b["author_links"] = author_profile_links
        if "Authored Book" in b.get("role", ""):
            b["links"] = dedup_links(b.get("links", []) + author_profile_links)

    output_path = os.path.join(DATA_DIR, "books_and_volumes.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(books_detailed, f, indent=2, ensure_ascii=False)
    print(f"Exported {len(books_detailed)} books & reviewed volumes to {output_path}")
    return books_detailed


def export_blogs():
    """8. Export all 31 articles and executive thought leadership essays with complete card, Spotify, Substack, and slide links."""
    kg_path = os.path.join(ROOT_DIR, "data", "knowledge-graph.json")
    with open(kg_path, "r", encoding="utf-8") as f:
        kg = json.load(f)

    # Parse actual blog cards from page-blog.html to extract any secondary links (e.g. Substack, Spotify, Author profile)
    html_card_links_by_url = {}
    blog_html_path = os.path.join(ROOT_DIR, "page-blog.html")
    if os.path.exists(blog_html_path):
        with open(blog_html_path, "r", encoding="utf-8") as bf:
            bhtml = bf.read()
        bl_cards = re.split(r'(?=<div class="col-lg-4 col-md-6 mb-4 pb-2 blog-card-item")', bhtml)
        for card in bl_cards:
            if 'blog-card-item' not in card:
                continue
            if '</section>' in card:
                card = card.split('</section>')[0]
            anchors = []
            for url, lbl in re.findall(r'<a\s+[^>]*href="([^"]+)"[^>]*>([\s\S]*?)</a>', card):
                u = to_canonical_url(url)
                if u:
                    anchors.append({"label": clean_text(lbl) or "Read Article", "url": u})
            anchors = dedup_links(anchors)
            for a in anchors:
                html_card_links_by_url[a["url"].rstrip("/")] = anchors

    # Map known RSAC/tech blog URLs to Smart Slides decks
    slides_by_blog_url = {
        "https://www.rsaconference.com/library/blog/the-clean-attack-problem": {
            "slides_url": "https://www.harshverma.me/page-smart-slides#deck=tHbS&slide=1",
            "easychair_url": "https://easychair.org/smart-slide/slide/tHbS#{sn:1}",
        },
        "https://www.rsaconference.com/Library/blog/the-death-of-authentication-why-identity-isnt-enough-for-ai-systems": {
            "slides_url": "https://www.harshverma.me/page-smart-slides#deck=xJKk&slide=1",
            "easychair_url": "https://easychair.org/smart-slide/slide/xJKk#{sn:1}",
        },
        "https://www.rsaconference.com/Library/blog/agents-dont-break-rules-they-redefine-them": {
            "slides_url": "https://www.harshverma.me/page-smart-slides#deck=X2qH&slide=1",
            "easychair_url": "https://easychair.org/smart-slide/slide/X2qH#{sn:1}",
        },
        "https://www.rsaconference.com/Library/blog/security-without-humans-designing-systems-that-defend-themselves": {
            "slides_url": "https://www.harshverma.me/page-smart-slides#deck=NZ5R&slide=1",
            "easychair_url": "https://easychair.org/smart-slide/slide/NZ5R#{sn:1}",
        },
    }

    blogs = kg.get("entities", {}).get("blogs", [])
    blogs_list = []
    seen_urls = set()

    for b in blogs:
        entry = dict(b)
        url = to_canonical_url(entry.get("url", ""))
        if not url or url.rstrip("/") in seen_urls:
            continue
        seen_urls.add(url.rstrip("/"))
        entry["url"] = url

        card_links = html_card_links_by_url.get(url.rstrip("/"), [])
        # Extract Substack URL if present on HTML card
        substack_url = entry.get("substack_url", "")
        for cl in card_links:
            if "substack.com" in cl["url"]:
                substack_url = cl["url"]
                break
        if substack_url:
            entry["substack_url"] = substack_url

        slide_ref = slides_by_blog_url.get(url)
        if slide_ref:
            entry["slides_url"] = slide_ref["slides_url"]
            entry["easychair_url"] = slide_ref["easychair_url"]

        combined_links = [
            {"label": "Read Article", "url": url},
            {"label": "Read on Substack", "url": substack_url},
            {"label": "Spotify Podcast", "url": to_canonical_url(entry.get("spotify_url", ""))},
            {"label": f"{entry.get('platform_short') or entry.get('platform', 'Platform')} Author Profile", "url": to_canonical_url(entry.get("author_profile", ""))},
        ]
        if slide_ref:
            combined_links.append({"label": "Interactive Smart Slides", "url": slide_ref["slides_url"]})
            combined_links.append({"label": "EasyChair Smart Slide", "url": slide_ref["easychair_url"]})
        combined_links.extend(card_links)

        entry["primary_url"] = url
        entry["links"] = dedup_links(combined_links)
        blogs_list.append(entry)

    output_path = os.path.join(DATA_DIR, "blog_articles.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(blogs_list, f, indent=2, ensure_ascii=False)
    print(f"Exported {len(blogs_list)} blog articles to {output_path}")
    return blogs_list


def export_verified_profiles():
    """9. Export all 59 verified directory profiles including all secondary links on multi-link cards."""
    about_path = os.path.join(ROOT_DIR, "page-about.html")
    with open(about_path, "r", encoding="utf-8") as f:
        html = f.read()

    card_matches = re.finditer(
        r'<div class="col-lg-4 col-md-6 mb-4 profile-card-item"[^>]*data-category="([^"]+)"[^>]*data-search="([^"]*)"[^>]*>([\s\S]*?)(?=(?:<div class="col-lg-4 col-md-6 mb-4 profile-card-item"|<div id="noProfilesFound"|<!-- Empty State|\Z))',
        html,
    )

    profiles = []
    seen_ids = set()

    for match in card_matches:
        category = match.group(1).strip()
        search_kw = match.group(2).strip()
        chunk = match.group(3)

        title_match = re.search(r'<h5 class="profile-card-title[^"]*">\s*([\s\S]*?)\s*</h5>', chunk)
        title = clean_text(title_match.group(1)) if title_match else ""

        cat_pill_match = re.search(r'<span class="profile-category-pill[^"]*">\s*([\s\S]*?)\s*</span>', chunk)
        category_label = clean_text(cat_pill_match.group(1)) if cat_pill_match else ""

        id_match = re.search(r'<div class="profile-card-identifier[^"]*">([\s\S]*?)</div>', chunk)
        identifier = clean_text(id_match.group(1)) if id_match else ""

        desc_match = re.search(r'<p class="profile-card-desc[^"]*">\s*([\s\S]*?)\s*</p>', chunk)
        description = clean_text(desc_match.group(1)) if desc_match else ""

        thumb_match = re.search(r'<img[^>]*src="([^"]+)"', chunk)
        thumb = thumb_match.group(1).strip() if thumb_match else ""

        # Collect ALL links on the profile card
        raw_card_links = []
        primary_action = re.search(r'<a\s+[^>]*href="([^"]+)"[^>]*class="btn-hub-action[^"]*"[^>]*>([\s\S]*?)</a>', chunk)
        if primary_action:
            raw_card_links.append({
                "label": clean_text(primary_action.group(2)) or f"Open {title}",
                "url": to_canonical_url(primary_action.group(1)),
            })
        for am in re.finditer(r'<a\s+[^>]*href="([^"]+)"[^>]*>([\s\S]*?)</a>', chunk):
            u = to_canonical_url(am.group(1))
            if u:
                raw_card_links.append({
                    "label": clean_text(am.group(2)) or f"Open {title}",
                    "url": u,
                })

        card_links = dedup_links(raw_card_links)
        url = card_links[0]["url"] if card_links else ""
        pid = "profile-" + re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")

        if url and pid not in seen_ids:
            seen_ids.add(pid)
            profiles.append({
                "id": pid,
                "name": title,
                "category": category,
                "category_label": category_label,
                "identifier": identifier,
                "description": description,
                "url": url,
                "primary_url": url,
                "links": card_links,
                "icon_svg": thumb,
                "search_keywords": search_kw,
            })

    output_path = os.path.join(DATA_DIR, "verified_profiles.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(profiles, f, indent=2, ensure_ascii=False)
    print(f"Exported {len(profiles)} verified profiles to {output_path}")
    return profiles


def export_memberships_and_associations():
    """10. Export all verified associations, fellowships & memberships with enriched schema."""
    kg_path = os.path.join(ROOT_DIR, "data", "knowledge-graph.json")
    with open(kg_path, "r", encoding="utf-8") as f:
        kg = json.load(f)

    assocs = kg.get("entities", {}).get("associations", [])

    meta_map = {
        "Forbes Technology Council": {
            "organization_name": "Forbes Technology Council",
            "membership_role": "Official Council Member & Columnist",
            "membership_id": "Forbes Executive Profile Verified",
            "date_joined": "2024",
            "link": "https://www.forbes.com/councils/forbestechcouncil/people/harshverma/"
        },
        "IEEE & IEEE Computer Society": {
            "organization_name": "IEEE & IEEE Computer Society",
            "membership_role": "Senior Member (SMIEEE)",
            "membership_id": "95132014",
            "date_joined": "2023",
            "link": "https://ieee-collabratec.ieee.org/app/p/HarshVerma59"
        },
        "British Computer Society (BCS)": {
            "organization_name": "British Computer Society (BCS)",
            "membership_role": "Fellow (FBCS)",
            "membership_id": "FBCS",
            "date_joined": "2026",
            "link": "https://www.bcs.org/membership-and-registrations/our-members/harsh-verma-fbcs"
        },
        "IEEE Technical Societies": {
            "organization_name": "IEEE Computational Intelligence Society & Young Professionals",
            "membership_role": "Society Member (CIS, YP & IEEE500)",
            "membership_id": "IEEE500, YP060, CIS011",
            "date_joined": "2023",
            "link": "https://cis.ieee.org/"
        },
        "IEEE Xplore Verified Author": {
            "organization_name": "IEEE Xplore Digital Library & Author Center",
            "membership_role": "Verified Author & Researcher",
            "membership_id": "37089143797",
            "date_joined": "2019",
            "link": "https://ieeexplore.ieee.org/author/37089143797"
        },
        "Interacting with Computers": {
            "organization_name": "Interacting with Computers (Oxford University Press & BCS)",
            "membership_role": "Peer Reviewer & Contributing Scholar",
            "membership_id": "mc.manuscriptcentral.com/iwc",
            "date_joined": "2025",
            "link": "https://mc.manuscriptcentral.com/iwc"
        },
        "Raptors.Dev Fellowship": {
            "organization_name": "Raptors.Dev Elite Engineering Fellowship",
            "membership_role": "Fellow Member",
            "membership_id": "Elite Engineering Fellowship",
            "date_joined": "2026",
            "link": "https://www.raptors.dev/fellow-membership"
        },
        "UC Berkeley SkyDeck": {
            "organization_name": "UC Berkeley SkyDeck",
            "membership_role": "Global Advisor & Startup Mentor",
            "membership_id": "Berkeley SkyDeck Global Advisor",
            "date_joined": "2024",
            "link": "https://skydeck.berkeley.edu/advisors/"
        },
        "ISACA": {
            "organization_name": "Information Systems Audit and Control Association (ISACA)",
            "membership_role": "Member, Verified Expert & Volunteer",
            "membership_id": "2394223",
            "date_joined": "2024",
            "link": "https://engage.isaca.org/expert/harshverma"
        },
        "Sigma Xi (The Scientific Research Honor Society)": {
            "organization_name": "Sigma Xi (The Scientific Research Honor Society)",
            "membership_role": "Full Elected Member",
            "membership_id": "Elected Member",
            "date_joined": "2024",
            "link": "https://www.sigmaxi.org/"
        },
        "Royal Society of Arts (RSA)": {
            "organization_name": "Royal Society of Arts (RSA)",
            "membership_role": "Fellow of the Royal Society of Arts (FRSA)",
            "membership_id": "Distinction: FRSA",
            "date_joined": "2025",
            "link": "https://www.thersa.org/"
        },
        "IOASD (Scientific & Academic Development)": {
            "organization_name": "International Organization for Academic and Scientific Development (IOASD)",
            "membership_role": "Royal Fellow (FRIOASD)",
            "membership_id": "FRIOASD-1066-2026",
            "date_joined": "2026",
            "link": "https://ioasd.org/royal-fellows/membership-id-frioasd-1066-2026/"
        },
        "Science Tech Xplore": {
            "organization_name": "Science Tech Xplore",
            "membership_role": "Fellow Member",
            "membership_id": "Official Registry: Harsh Verma",
            "date_joined": "2026",
            "link": "https://sciencetechxplore.org/fellow-members1.php"
        },
        "Forttuna Technical Council": {
            "organization_name": "Forttuna Global Technical Council",
            "membership_role": "Council Member",
            "membership_id": "Official Council Appointment",
            "date_joined": "2025",
            "link": "https://councils.forttuna.com/council-member/harsh-verma/"
        },
        "AAAI (Advancement of Artificial Intelligence)": {
            "organization_name": "Association for the Advancement of Artificial Intelligence (AAAI)",
            "membership_role": "Active Member",
            "membership_id": "656475",
            "date_joined": "2024",
            "link": "https://aaai.org/"
        },
        "AAAS (Advancement of Science)": {
            "organization_name": "American Association for the Advancement of Science (AAAS)",
            "membership_role": "Supporting Member",
            "membership_id": "Scientific Society Member",
            "date_joined": "2024",
            "link": "https://www.aaas.org/"
        },
        "Python Software Foundation (PSF)": {
            "organization_name": "Python Software Foundation (PSF)",
            "membership_role": "Contributing Member",
            "membership_id": "harshverma59",
            "date_joined": "2022",
            "link": "https://www.python.org/users/harshverma59/"
        },
        "OWASP Foundation": {
            "organization_name": "Open Web Application Security Project (OWASP Foundation)",
            "membership_role": "Global Member",
            "membership_id": "3981139",
            "date_joined": "2024",
            "link": "https://owasp.glueup.com/my/memberships/3981139"
        },
        "IFGICT (Global Green ICT)": {
            "organization_name": "International Federation of Global Green ICT (IFGICT)",
            "membership_role": "Fellow",
            "membership_id": "06042Z26HV",
            "date_joined": "2026",
            "link": "https://timebusinessnews.com/harsh-verma-ifgict/"
        },
        "Google Developer Expert": {
            "organization_name": "Google Developer Groups & Experts",
            "membership_role": "Google Developer Expert (AI & Cloud)",
            "membership_id": "Google Recognized Leader",
            "date_joined": "2024",
            "link": "https://me.developers.google.com/communities/experts?q=harsh%20verma"
        },
        "RSA Conference (RSAC)": {
            "organization_name": "RSA Conference (RSAC)",
            "membership_role": "Invite-Only Expert Member & Contributor",
            "membership_id": "RSAC Expert Contributor",
            "date_joined": "2024",
            "link": "https://portal.onersac.com/library/discover"
        },
        "ADPList Mentorship Community": {
            "organization_name": "ADPList Global Mentorship Network",
            "membership_role": "Top Mentor (AI & Tech Leadership)",
            "membership_id": "Verified Global Mentor",
            "date_joined": "2023",
            "link": "https://adplist.org/mentors/harsh-verma"
        },
        "Dent Capital Expert List": {
            "organization_name": "Dent Capital & Venture Network",
            "membership_role": "Mentor & Technical Advisor",
            "membership_id": "Venture & Tech Network Advisor",
            "date_joined": "2024",
            "link": "https://councils.forttuna.com/council-member/harsh-verma/"
        },
        "HackUTD & Hackmakers": {
            "organization_name": "HackUTD (University of Texas at Dallas) & Hackmakers Global",
            "membership_role": "AI Challenge Judge & Technical Mentor",
            "membership_id": "Jury & Mentor Panel",
            "date_joined": "2023",
            "link": "https://hackutd.co/"
        },
        "ODSC & SIIM Communities": {
            "organization_name": "Open Data Science Conference (ODSC) & SIIM",
            "membership_role": "Speaker, Author & Member",
            "membership_id": "Community Member",
            "date_joined": "2023",
            "link": "https://odsc.com/"
        },
        "Screna.ai": {
            "organization_name": "Screna.ai",
            "membership_role": "Technical Mentor & AI Advisor",
            "membership_id": "Technical Mentor & Evaluation Board",
            "date_joined": "2025",
            "link": "https://www.screna.ai/mentor-dashboard"
        },
        "American Institute for Information Technology & Engineering (AIITE)": {
            "organization_name": "American Institute for Information Technology & Engineering (AIITE)",
            "membership_role": "Reviewer and Ambassador",
            "membership_id": "Member ID: AIITE-A-000ABC",
            "date_joined": "2026",
            "link": "https://theaiite.org"
        },
        "Business Intelligence Group": {
            "organization_name": "Business Intelligence Group",
            "membership_role": "2026 BIG Awards for Business Judge",
            "membership_id": "Executive Awards Jury",
            "date_joined": "2026",
            "link": "https://judges.bintelligence.com/harsh-verma"
        }
    }

    enriched = []
    for a in assocs:
        title = a.get("title", "")
        m = meta_map.get(title, {})
        primary_link = to_canonical_url(m.get("link", a.get("url", "")))
        org_name = m.get("organization_name", title)
        raw_links = [{"url": primary_link, "label": f"View {org_name} Profile"}]
        for lk in (a.get("links") or []):
            u = to_canonical_url(lk.get("url", ""))
            if u:
                raw_links.append({"url": u, "label": (lk.get("label") or f"View {org_name}").strip()})
        item = {
            "organization_name": org_name,
            "membership_role": m.get("membership_role", a.get("role", "")),
            "membership_id": m.get("membership_id", a.get("credential_id", "")),
            "date_joined": m.get("date_joined", "2024"),
            "link": primary_link,
            "primary_url": primary_link,
            "title": title,
            "role": a.get("role", ""),
            "tier": a.get("tier", ""),
            "credential_id": a.get("credential_id", ""),
            "category": a.get("category", ""),
            "image": a.get("image", ""),
            "description": a.get("description", ""),
            "url": primary_link,
            "links": dedup_links(raw_links),
        }
        enriched.append(item)

    output_path = os.path.join(DATA_DIR, "memberships_and_associations.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(enriched, f, indent=2, ensure_ascii=False)

    print(f"Exported {len(enriched)} memberships & associations to {output_path}")
    return enriched


def export_about():
    """11. Export comprehensive about page dossier data."""
    about_path = os.path.join(ROOT_DIR, "scripts", "generate_about_and_work.py")
    if os.path.exists(about_path):
        import importlib.util
        spec = importlib.util.spec_from_file_location("generate_about_and_work", about_path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod.generate_about_json()
    return {}


def export_professional_work():
    """12. Export authoritative professional work and impact dossier."""
    work_path = os.path.join(ROOT_DIR, "scripts", "generate_professional_work_json.py")
    if os.path.exists(work_path):
        import importlib.util
        spec = importlib.util.spec_from_file_location("generate_professional_work_json", work_path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod.generate_professional_work()
    return {}


def export_slides():
    """13. Export unified Smart Slides catalog and per-slide details to data/slides.json."""
    deck_definitions = [
        {
            "deck_number": 1,
            "id": "ntzm5",
            "slug": "agentic-security-governance",
            "folder": "agentic-security-governance",
            "data_file": "data/agentic-security-governance.json",
            "title": "The Era of Agentic Security: Governance in the Age of Autonomy",
            "shortTitle": "The Era of Agentic Security",
            "subtitle": "Architecting Autonomous Security Operations & Verifiable AI Guardrails",
            "description": "Architecting autonomous security operations (SecOps), managing non-deterministic workflows, verifiable AI guardrails, and the Hierarchy of Needs for AI agents.",
            "badge": "Verified Academic Ref",
            "author": "Harsh Verma",
            "year": "2026",
            "easyChairUrl": "https://easychair.org/smart-slide/slide/ntzm5#{sn:1}",
            "portfolioUrl": "https://www.harshverma.me/page-smart-slides#deck=ntzm5&slide=1",
            "blogUrl": None,
            "blogTitle": None,
            "bibtex": "@misc{verma2026agenticsecurity,\n  author = {Verma, Harsh},\n  title = {The Era of Agentic Security: Governance in the Age of Autonomy},\n  howpublished = {EasyChair Smart Slide Series, Ref. ntzm5},\n  year = {2026},\n  url = {https://easychair.org/smart-slide/slide/ntzm5}\n}",
        },
        {
            "deck_number": 2,
            "id": "T45r",
            "slug": "powering-cybersecurity-genai",
            "folder": "powering-cybersecurity-genai",
            "data_file": "data/powering-cybersecurity-genai.json",
            "title": "Powering Cybersecurity with Gen-AI and Intelligent Agents",
            "shortTitle": "Powering Cybersecurity with Gen-AI",
            "subtitle": "Autonomous Self-Healing Defense, Threat Summarizers & Rakshak-AI",
            "description": "Addressing attack velocity (every 39 seconds) and $4.35M breach costs with autonomous self-healing agentic defense, threat summarizers, and Rakshak-AI.",
            "badge": "Case Study Included",
            "author": "Harsh Verma",
            "year": "2026",
            "easyChairUrl": "https://easychair.org/smart-slide/slide/T45r#{sn:1}",
            "portfolioUrl": "https://www.harshverma.me/page-smart-slides#deck=T45r&slide=1",
            "blogUrl": None,
            "blogTitle": None,
            "bibtex": "@misc{verma2026cybersecuritygenai,\n  author = {Verma, Harsh},\n  title = {Powering Cybersecurity with Gen-AI and Intelligent Agents},\n  howpublished = {EasyChair Smart Slide Series, Ref. T45r},\n  year = {2026},\n  url = {https://easychair.org/smart-slide/slide/T45r}\n}",
        },
        {
            "deck_number": 3,
            "id": "r92g",
            "slug": "enterprises-multi-agent-systems",
            "folder": "enterprises-multi-agent-systems",
            "data_file": "data/enterprises-multi-agent-systems.json",
            "title": "When Enterprises Become Multi-Agent Systems",
            "shortTitle": "Enterprises as Multi-Agent Systems",
            "subtitle": "Rethinking Security, Trust, and Control in the Agentic Era",
            "description": "Rethinking security, trust boundaries, multi-agent orchestration, deterministic vs non-deterministic workflows, and enterprise governance in autonomous ecosystems.",
            "badge": "Multi-Agent Architecture",
            "author": "Harsh Verma",
            "year": "2026",
            "easyChairUrl": "https://easychair.org/smart-slide/slide/r92g#{sn:1}",
            "portfolioUrl": "https://www.harshverma.me/page-smart-slides#deck=r92g&slide=1",
            "blogUrl": None,
            "blogTitle": None,
            "bibtex": "@misc{verma2026enterprisemultiagent,\n  author = {Verma, Harsh},\n  title = {When Enterprises Become Multi-Agent Systems},\n  howpublished = {EasyChair Smart Slide Series, Ref. r92g},\n  year = {2026},\n  url = {https://easychair.org/smart-slide/slide/r92g}\n}",
        },
        {
            "deck_number": 4,
            "id": "GxwP",
            "slug": "agentic-security-defender-threat",
            "folder": "agentic-security-defender-threat",
            "data_file": "data/agentic-security-defender-threat.json",
            "title": "Agentic Security: When AI Becomes Both Defender and Threat",
            "shortTitle": "Agentic Security: Defender and Threat",
            "subtitle": "Cybersecurity Paradigms for Autonomous Systems",
            "description": "Exploring the cybersecurity battlefield, the new agentic attack surface, prompt injection defenses, multi-agent risk multiplication, and runtime intent enforcement.",
            "badge": "Threat & Defense Playbook",
            "author": "Harsh Verma",
            "year": "2026",
            "easyChairUrl": "https://easychair.org/smart-slide/slide/GxwP#{sn:1}",
            "portfolioUrl": "https://www.harshverma.me/page-smart-slides#deck=GxwP&slide=1",
            "blogUrl": None,
            "blogTitle": None,
            "bibtex": "@misc{verma2026agenticthreatdefender,\n  author = {Verma, Harsh},\n  title = {Agentic Security: When AI Becomes Both Defender and Threat},\n  howpublished = {EasyChair Smart Slide Series, Ref. GxwP},\n  year = {2026},\n  url = {https://easychair.org/smart-slide/slide/GxwP}\n}",
        },
        {
            "deck_number": 5,
            "id": "8WpM",
            "slug": "hikerunner-loadtest-framework",
            "folder": "hikerunner-loadtest-framework",
            "data_file": "data/hikerunner-loadtest-framework.json",
            "title": "HikeRunner: LoadTestFramework",
            "shortTitle": "HikeRunner: LoadTestFramework",
            "subtitle": "High-Throughput Distributed Performance Testing Architecture",
            "description": "In-house distributed load testing framework to simulate real-world messaging user journeys, vertically & horizontally stressing backend DBs, caches, queues, and CI/CD pipelines.",
            "badge": "Performance Engineering",
            "author": "Harsh Verma",
            "year": "2026",
            "easyChairUrl": "https://easychair.org/smart-slide/slide/8WpM#{sn:1}",
            "portfolioUrl": "https://www.harshverma.me/page-smart-slides#deck=8WpM&slide=1",
            "blogUrl": None,
            "blogTitle": None,
            "bibtex": "@misc{verma2026hikerunner,\n  author = {Verma, Harsh},\n  title = {HikeRunner: LoadTestFramework},\n  howpublished = {EasyChair Smart Slide Series, Ref. 8WpM},\n  year = {2026},\n  url = {https://easychair.org/smart-slide/slide/8WpM}\n}",
        },
        {
            "deck_number": 6,
            "id": "tHbS",
            "slug": "cybersecurity-evolution-clean-attack",
            "folder": "cybersecurity-evolution-clean-attack",
            "data_file": "data/cybersecurity-evolution-clean-attack.json",
            "title": "The Evolution of Cybersecurity: From Anomaly Detection to Intent-Based Security. The Clean Attack Problem: When Nothing Looks Wrong but Everything Is Compromised",
            "shortTitle": "The Evolution of Cybersecurity: Clean Attack Problem",
            "subtitle": "From Anomaly Detection to Intent Reasoning & Behavioral Sequencing",
            "description": "The Clean Attack Problem: When nothing looks wrong but everything is compromised. Shifting from anomaly detection to intent reasoning, behavioral sequencing, and runtime decision analysis.",
            "badge": "Intent-Based Security",
            "author": "Harsh Verma",
            "year": "2026",
            "easyChairUrl": "https://easychair.org/smart-slide/slide/tHbS#{sn:1}",
            "portfolioUrl": "https://www.harshverma.me/page-smart-slides#deck=tHbS&slide=1",
            "blogUrl": "https://www.rsaconference.com/library/blog/the-clean-attack-problem",
            "blogTitle": "RSA Conference: The Clean Attack Problem",
            "bibtex": "@misc{verma2026cybersecuritycleanattack,\n  author = {Verma, Harsh},\n  title = {The Evolution of Cybersecurity: From Anomaly Detection to Intent-Based Security. The Clean Attack Problem: When Nothing Looks Wrong but Everything Is Compromised},\n  howpublished = {EasyChair Smart Slide Series, Ref. tHbS},\n  year = {2026},\n  url = {https://easychair.org/smart-slide/slide/tHbS}\n}",
        },
        {
            "deck_number": 7,
            "id": "xJKk",
            "slug": "death-of-authentication-ai-systems",
            "folder": "death-of-authentication-ai-systems",
            "data_file": "data/death-of-authentication-ai-systems.json",
            "title": "The Death of Authentication: Why Identity Isn'T Enough for AI Systems",
            "shortTitle": "The Death of Authentication: Identity Isn't Enough",
            "subtitle": "Post-Authentication Risk, Behavioral Monitoring & Runtime Intent Analysis",
            "description": "Addressing post-authentication risk and trusted-agent misuse. Why Zero Trust must evolve beyond static identity verification toward continuous behavioral monitoring and runtime intent analysis.",
            "badge": "Zero Trust Evolution",
            "author": "Harsh Verma",
            "year": "2026",
            "easyChairUrl": "https://easychair.org/smart-slide/slide/xJKk#{sn:1}",
            "portfolioUrl": "https://www.harshverma.me/page-smart-slides#deck=xJKk&slide=1",
            "blogUrl": "https://www.rsaconference.com/Library/blog/the-death-of-authentication-why-identity-isnt-enough-for-ai-systems",
            "blogTitle": "RSA Conference: The Death of Authentication",
            "bibtex": "@misc{verma2026deathofauthentication,\n  author = {Verma, Harsh},\n  title = {The Death of Authentication: Why Identity Isn'T Enough for AI Systems},\n  howpublished = {EasyChair Smart Slide Series, Ref. xJKk},\n  year = {2026},\n  url = {https://easychair.org/smart-slide/slide/xJKk}\n}",
        },
        {
            "deck_number": 8,
            "id": "X2qH",
            "slug": "agents-dont-break-rules-they-redefine-them",
            "folder": "agents-dont-break-rules-they-redefine-them",
            "data_file": "data/agents-dont-break-rules-they-redefine-them.json",
            "title": "Agents Don't Break Rules, They Redefine Them: Cybersecurity in the Age of Autonomous AI",
            "shortTitle": "Agents Don't Break Rules: Redefining Intent",
            "subtitle": "Continuous Runtime Governance & Behavioral Invariants for Autonomous AI",
            "description": "Cybersecurity in the age of autonomous AI. Why autonomous agents don't fail by violating rules—they follow instructions literally while circumventing intent through policy drift and specification gaming.",
            "badge": "Continuous Governance",
            "author": "Harsh Verma",
            "year": "2026",
            "easyChairUrl": "https://easychair.org/smart-slide/slide/X2qH#{sn:1}",
            "portfolioUrl": "https://www.harshverma.me/page-smart-slides#deck=X2qH&slide=1",
            "blogUrl": "https://www.rsaconference.com/Library/blog/agents-dont-break-rules-they-redefine-them",
            "blogTitle": "RSA Conference: Agents Don't Break Rules",
            "bibtex": "@misc{verma2026agentsdontbreakrules,\n  author = {Verma, Harsh},\n  title = {Agents Don't Break Rules, They Redefine Them: Cybersecurity in the Age of Autonomous AI},\n  howpublished = {EasyChair Smart Slide Series, Ref. X2qH},\n  year = {2026},\n  url = {https://easychair.org/smart-slide/slide/X2qH}\n}",
        },
        {
            "deck_number": 9,
            "id": "JSZf",
            "slug": "why-multi-agent-systems-cybersecurity-nightmare",
            "folder": "why-multi-agent-systems-cybersecurity-nightmare",
            "data_file": "data/why-multi-agent-systems-cybersecurity-nightmare.json",
            "title": "Why Multi-Agent Systems Are a Cybersecurity Nightmare: Deep-Dive into Inter-Agent Trust Chains, Cascade Injections & Agentic IAM",
            "shortTitle": "Why Multi-Agent Systems Are a Cybersecurity Nightmare",
            "subtitle": "Inter-Agent Trust Chains, Cascade Injections & Machine-to-Machine IAM",
            "description": "Deep-dive into inter-agent trust chains, cascade prompt injections, memory and vector store poisoning, and machine-to-machine agentic IAM architecture.",
            "badge": "Multi-Agent Defense",
            "author": "Harsh Verma",
            "year": "2026",
            "easyChairUrl": "https://easychair.org/smart-slide/slide/JSZf#{sn:1}",
            "portfolioUrl": "https://www.harshverma.me/page-smart-slides#deck=JSZf&slide=1",
            "blogUrl": "https://www.rsaconference.com/Library/blog/why-multi-agent-systems-are-a-cybersecurity-nightmare",
            "blogTitle": "RSA Conference: Why Multi-Agent Systems Are a Cybersecurity Nightmare",
            "bibtex": "@misc{verma2026whymultiagentsystemscybersecuritynightmare,\n  author = {Verma, Harsh},\n  title = {Why Multi-Agent Systems Are a Cybersecurity Nightmare},\n  howpublished = {EasyChair Smart Slide Series, Ref. JSZf},\n  year = {2026},\n  url = {https://easychair.org/smart-slide/slide/JSZf}\n}",
        },
        {
            "deck_number": 10,
            "id": "NZ5R",
            "slug": "security-without-humans-defend-themselves",
            "folder": "security-without-humans-defend-themselves",
            "data_file": "data/security-without-humans-defend-themselves.json",
            "title": "Security Without Humans: Designing Systems That Defend Themselves",
            "shortTitle": "Security Without Humans: Self-Defending Systems",
            "subtitle": "Closed-Loop Containment, L0-L3 Risk Envelope & 90-Day Autonomous Defense Roadmap",
            "description": "Shifting from alert-centric visibility to autonomous resilience across Intent, Time, and Interaction—featuring closed-loop containment, the L0–L3 risk envelope, and a 90-day enterprise roadmap.",
            "badge": "Autonomous Defense",
            "author": "Harsh Verma",
            "year": "2026",
            "easyChairUrl": "https://easychair.org/smart-slide/slide/NZ5R#{sn:1}",
            "portfolioUrl": "https://www.harshverma.me/page-smart-slides#deck=NZ5R&slide=1",
            "blogUrl": "https://www.rsaconference.com/Library/blog/security-without-humans-designing-systems-that-defend-themselves",
            "blogTitle": "RSA Conference: Security Without Humans: Designing Systems that Defend Themselves",
            "bibtex": "@misc{verma2026securitywithouthumans,\n  author = {Verma, Harsh},\n  title = {Security Without Humans: Designing Systems That Defend Themselves},\n  howpublished = {EasyChair Smart Slide Series, Ref. NZ5R},\n  year = {2026},\n  url = {https://easychair.org/smart-slide/slide/NZ5R}\n}",
        },
    ]

    decks_out = []
    total_slides = 0
    for meta in deck_definitions:
        deck_file = os.path.join(ROOT_DIR, meta["data_file"])
        raw_slides = []
        if os.path.exists(deck_file):
            with open(deck_file, "r", encoding="utf-8") as f:
                raw_slides = json.load(f)

        folder = meta["folder"]
        enriched_slides = []
        categories = []
        all_tags = []
        for s in raw_slides:
            sn = s.get("slide")
            cat = s.get("category", "")
            tags = s.get("tags", [])
            if cat and cat not in categories:
                categories.append(cat)
            for t in tags:
                if t and t not in all_tags:
                    all_tags.append(t)
            enriched_slides.append({
                "slide": sn,
                "title": s.get("title", ""),
                "takeaways": s.get("takeaways", []),
                "category": cat,
                "tags": tags,
                "image": f"images/smart-slides/{folder}/slide-{sn}.jpg",
                "thumbnail": f"images/smart-slides/{folder}/thumb-{sn}.jpg",
            })

        total_slides += len(enriched_slides)
        deck_entry = dict(meta)
        deck_entry["count"] = len(enriched_slides)
        deck_entry["cover_image"] = f"images/smart-slides/{folder}/slide-1.jpg"
        deck_entry["thumbnail_image"] = f"images/smart-slides/{folder}/thumb-1.jpg"
        deck_entry["categories"] = categories
        deck_entry["tags"] = all_tags
        deck_entry["primary_url"] = meta["easyChairUrl"]
        deck_entry["links"] = dedup_links([
            {"label": "EasyChair Smart Slide", "url": meta["easyChairUrl"]},
            {"label": "Portfolio Interactive Viewer", "url": meta["portfolioUrl"]},
            {"label": meta.get("blogTitle") or "Associated Article", "url": meta.get("blogUrl") or ""},
        ])
        deck_entry["slides"] = enriched_slides
        decks_out.append(deck_entry)

    payload = {
        "section": "Smart Slides & Keynote Hub",
        "author": "Harsh Verma",
        "easychair_author_url": "https://easychair.org/smart-slide/author/v5zJ",
        "page_url": "https://www.harshverma.me/page-smart-slides",
        "total_decks": len(decks_out),
        "total_slides": total_slides,
        "decks": decks_out,
    }

    output_path = os.path.join(DATA_DIR, "slides.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    print(f"Exported {len(decks_out)} smart slide decks ({total_slides} slides) to {output_path}")
    return payload


def export_projects_certification():
    """14. Export all featured projects, widgets, and verified certifications to data/projects_certification.json."""
    portfolio_path = os.path.join(ROOT_DIR, "page-portfolio.html")
    with open(portfolio_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Isolate Projects wrapper
    proj_sec_match = re.search(
        r'<div class="row projects-wrapper">([\s\S]*?)<!-- All Repositories Centered Action Row -->',
        html,
    )
    proj_html = proj_sec_match.group(1) if proj_sec_match else ""

    # Split project columns cleanly
    proj_chunks = re.split(r'(?=<div class="col-lg-4 col-md-6 col-12 mt-4 pt-2 )', proj_html)
    projects = []
    widgets = []

    domain_label_map = {
        "ai": "AI & ML",
        "software": "Software & Systems",
        "bigdata": "Big Data",
        "nlp": "NLP & Speech",
        "vision": "Computer Vision",
    }

    for chunk in proj_chunks:
        chunk = chunk.strip()
        if not chunk.startswith('<div class="col-lg-4 col-md-6 col-12 mt-4 pt-2 '):
            continue

        open_tag_match = re.match(r'<div ([^>]+)>', chunk)
        if not open_tag_match:
            continue
        attrs = open_tag_match.group(1)

        cls_match = re.search(r'class="([^"]+)"', attrs)
        classes = cls_match.group(1).split() if cls_match else []
        is_widget = "project-grid-filler-widget" in classes

        id_match = re.search(r'id="([^"]+)"', attrs)
        widget_type_match = re.search(r'data-widget="([^"]+)"', attrs)
        desc_attr_match = re.search(r'data-description="([^"]*)"', attrs)
        tags_attr_match = re.search(r'data-tags="([^"]*)"', attrs)

        categories = [c for c in classes if c in domain_label_map]
        category_labels = [domain_label_map[c] for c in categories]

        status_match = re.search(r'<span class="proj-status-badge ([^"]+)"[^>]*>([\s\S]*?)</span>', chunk)
        status_class = status_match.group(1).strip() if status_match else ""
        status_label = clean_text(status_match.group(2)) if status_match else ""

        thumb_match = re.search(r'<img[^>]*class="portfolio-thumb-img"[^>]*src="([^"]+)"', chunk)
        if not thumb_match:
            thumb_match = re.search(r'<img[^>]*src="([^"]+)"[^>]*class="portfolio-thumb-img"', chunk)
        image = thumb_match.group(1).strip() if thumb_match else ""

        domain_match = re.search(r'<span class="proj-domain-badge"[^>]*>([\s\S]*?)</span>', chunk)
        domain = clean_text(domain_match.group(1)) if domain_match else ""

        metric_match = re.search(r'<span class="proj-metric-badge"[^>]*>([\s\S]*?)</span>', chunk)
        metric = clean_text(metric_match.group(1)) if metric_match else ""

        title_match = re.search(
            r'<h5 class="proj-card-title"[^>]*>\s*<a\s+[^>]*href="([^"]+)"[^>]*>([\s\S]*?)</a>\s*</h5>',
            chunk,
        )
        primary_url = clean_text(title_match.group(1)) if title_match else ""
        title = clean_text(title_match.group(2)) if title_match else ""

        desc_match = re.search(r'<p class="proj-card-desc[^"]*">([\s\S]*?)</p>', chunk)
        description = clean_text(desc_match.group(1)) if desc_match else (clean_text(desc_attr_match.group(1)) if desc_attr_match else "")

        tags = [clean_text(t) for t in re.findall(r'<span class="proj-tag-pill">([\s\S]*?)</span>', chunk)]
        if not tags and tags_attr_match:
            tags = [t.strip() for t in tags_attr_match.group(1).split(",") if t.strip()]

        repo_name = ""
        if "github.com/iamharshverma/" in primary_url:
            repo_name = primary_url.rstrip("/").split("/")[-1]

        actions = []
        actions_match = re.search(r'<div class="proj-card-actions">([\s\S]*?)</div>', chunk)
        if actions_match:
            for am in re.finditer(r'<a\s+[^>]*href="([^"]+)"[^>]*>([\s\S]*?)</a>', actions_match.group(1)):
                actions.append({
                    "label": clean_text(am.group(2)),
                    "url": clean_text(am.group(1)),
                })

        slug_id = (
            id_match.group(1)
            if id_match
            else "proj-" + re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
        )

        widget_or_proj_anchor = f"https://www.harshverma.me/page-portfolio#{slug_id}" if id_match else "https://www.harshverma.me/page-portfolio#projects-section"
        resolved_primary_url = to_canonical_url(primary_url) or widget_or_proj_anchor

        raw_proj_links = [{"label": "Primary URL", "url": resolved_primary_url}]
        if primary_url.startswith("mailto:"):
            raw_proj_links.append({"label": "Inquire via Email", "url": primary_url})
        for a in actions:
            u = a["url"]
            if u.startswith("mailto:"):
                raw_proj_links.append({"label": a["label"], "url": u})
            else:
                cu = to_canonical_url(u)
                if cu:
                    raw_proj_links.append({"label": a["label"], "url": cu})
        norm_links = dedup_links(raw_proj_links)

        entry = {
            "id": slug_id,
            "title": title,
            "domain": domain,
            "status": status_label,
            "status_type": status_class.replace("status-", ""),
            "metric": metric,
            "categories": categories,
            "category_labels": category_labels,
            "description": description,
            "tags": tags,
            "url": primary_url,
            "primary_url": resolved_primary_url,
            "github_url": primary_url if "github.com" in primary_url else None,
            "repository_name": repo_name or None,
            "preview_image": image,
            "actions": actions,
            "links": norm_links,
            "page_url": "https://www.harshverma.me/page-portfolio#projects-section",
        }

        if is_widget:
            entry["widget_type"] = widget_type_match.group(1) if widget_type_match else "hub-widget"
            widgets.append(entry)
        else:
            entry["project_number"] = len(projects) + 1
            projects.append(entry)

    # Isolate Certifications grid
    cert_sec_match = re.search(
        r'<div class="row" id="certGridContainer">([\s\S]*?)<!-- Complete Certifications Repository Callout Banner -->',
        html,
    )
    cert_html = cert_sec_match.group(1) if cert_sec_match else ""
    cert_chunks = re.split(r'(?=<div class="col-lg-4 col-md-6 col-12 mb-4 cert-grid-item")', cert_html)

    cert_cat_label_map = {
        "gcp": "Google Cloud & GCP",
        "ai": "AI & Deep Learning",
        "bigdata": "Data Science & Big Data",
        "software": "Software & DevOps",
    }

    certifications = []
    for chunk in cert_chunks:
        chunk = chunk.strip()
        if not chunk.startswith('<div class="col-lg-4 col-md-6 col-12 mb-4 cert-grid-item"'):
            continue

        open_tag_match = re.match(r'<div ([^>]+)>', chunk)
        if not open_tag_match:
            continue
        attrs = open_tag_match.group(1)

        cat_match = re.search(r'data-category="([^"]*)"', attrs)
        category = cat_match.group(1).strip() if cat_match else ""
        search_match = re.search(r'data-search="([^"]*)"', attrs)
        search_keywords = clean_text(search_match.group(1)) if search_match else ""

        img_match = re.search(r'<img[^>]*class="cert-card-img"[^>]*src="([^"]+)"', chunk)
        if not img_match:
            img_match = re.search(r'<img[^>]*src="([^"]+)"[^>]*class="cert-card-img"', chunk)
        image = img_match.group(1).strip() if img_match else ""

        issuer_badge_match = re.search(r'<span class="cert-issuer-badge"[^>]*>([\s\S]*?)</span>', chunk)
        issuer_badge = clean_text(issuer_badge_match.group(1)) if issuer_badge_match else ""

        topic_badge_match = re.search(r'<span class="cert-topic-badge[^"]*"[^>]*>([\s\S]*?)</span>', chunk)
        topic_badge = clean_text(topic_badge_match.group(1)) if topic_badge_match else ""

        title_match = re.search(r'<h5 class="cert-title"(?:\s+title="([^"]*)")?[^>]*>([\s\S]*?)</h5>', chunk)
        full_title = clean_text(title_match.group(1)) if (title_match and title_match.group(1)) else ""
        title = clean_text(title_match.group(2)) if title_match else ""
        if not full_title:
            full_title = title

        issuer_line_match = re.search(r'<div class="cert-issuer-line">([\s\S]*?)</div>', chunk)
        issuer_line = clean_text(issuer_line_match.group(1)) if issuer_line_match else ""

        issuer_parts = [p.strip() for p in issuer_line.split("•") if p.strip()]
        issuer = issuer_parts[0] if issuer_parts else issuer_badge
        platform = issuer_parts[1] if len(issuer_parts) > 1 else ("Coursera" if "coursera" in issuer_line.lower() else issuer_badge)

        tags = [clean_text(t) for t in re.findall(r'<span class="cert-tag">([\s\S]*?)</span>', chunk)]

        status_match = re.search(r'<span class="cert-status-badge">([\s\S]*?)</span>', chunk)
        status_label = clean_text(status_match.group(1)) if status_match else "Verified Credential"

        cert_slug = "cert-" + re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
        preview_url = f"https://www.harshverma.me/{image}" if image else ""
        archive_repo = "https://github.com/iamharshverma/CertificatesAccomplishment"
        cert_page_url = "https://www.harshverma.me/page-portfolio#certifications"

        certifications.append({
            "id": cert_slug,
            "certificate_number": len(certifications) + 1,
            "title": title,
            "full_title": full_title,
            "category": category,
            "category_label": cert_cat_label_map.get(category, category.title()),
            "topic_badge": topic_badge,
            "issuer": issuer,
            "issuer_badge": issuer_badge,
            "platform": platform,
            "issuer_line": issuer_line,
            "status": status_label,
            "tags": tags,
            "search_keywords": search_keywords,
            "image": image,
            "preview_url": preview_url,
            "archive_repo_url": archive_repo,
            "page_url": cert_page_url,
            "primary_url": preview_url or archive_repo,
            "links": dedup_links([
                {"label": "Certificate Image", "url": preview_url},
                {"label": "All Certificates Repository (GitHub)", "url": archive_repo},
                {"label": "Portfolio Certifications Section", "url": cert_page_url},
            ]),
        })

    # Compute structured summary breakdowns
    domain_counts = {}
    for c_key, c_label in domain_label_map.items():
        domain_counts[c_key] = {
            "label": c_label,
            "count": sum(1 for p in projects if c_key in p["categories"]),
        }

    status_counts = {}
    for p in projects:
        st = p["status"] or "Other"
        status_counts[st] = status_counts.get(st, 0) + 1

    cert_track_counts = {}
    for c_key, c_label in cert_cat_label_map.items():
        cert_track_counts[c_key] = {
            "label": c_label,
            "count": sum(1 for c in certifications if c["category"] == c_key),
        }

    payload = {
        "section": "Portfolio Projects & Verified Certifications",
        "author": "Harsh Verma",
        "page_url": "https://www.harshverma.me/page-portfolio",
        "github_profile": "https://github.com/iamharshverma",
        "certificates_archive_repo": "https://github.com/iamharshverma/CertificatesAccomplishment",
        "summary_stats": {
            "total_projects": len(projects),
            "total_hub_widgets": len(widgets),
            "total_certifications": len(certifications),
            "completed_specializations_total": "30+",
            "github_repositories_total": "60+",
            "open_source_verified_pct": "100%",
            "project_domains": domain_counts,
            "project_status_breakdown": status_counts,
            "certification_tracks": cert_track_counts,
        },
        "projects": projects,
        "hub_widgets": widgets,
        "certifications": certifications,
    }

    output_path = os.path.join(DATA_DIR, "projects_certification.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    print(
        f"Exported {len(projects)} projects, {len(widgets)} hub widgets, and {len(certifications)} certifications to {output_path}"
    )
    return payload


def export_advisory_and_board():
    """16. Export complete Board & Strategic Advisory data, models, roadmap, case studies, ecosystem, and links to data/advisory_and_board.json."""
    adv_path = os.path.join(ROOT_DIR, "page-advisory.html")
    html = open(adv_path, "r", encoding="utf-8").read() if os.path.exists(adv_path) else ""

    # 1. Governance Flywheel 4 Pillars
    flywheel_pillars = []
    for blk in html.split('class="flywheel-quadrant')[1:]:
        blk = blk.split("<!-- Quadrant")[0].split("</section>")[0]
        t_m = re.search(r'<h4[^>]*>([\s\S]*?)</h4>', blk)
        bullets = [clean_text(li) for li in re.findall(r'<li[^>]*>([\s\S]*?)</li>', blk) if clean_text(li)]
        if t_m:
            flywheel_pillars.append({
                "title": clean_text(t_m.group(1)),
                "highlights": bullets,
            })

    # 2. Core Advisory Expertise Pillars
    expertise_pillars = []
    for cm in re.finditer(r'<h3 class="advisory-card-title"[^>]*>([\s\S]*?)</h3>\s*<div class="advisory-card-tagline"[^>]*>([\s\S]*?)</div>\s*<p class="advisory-card-desc"[^>]*>([\s\S]*?)</p>([\s\S]{0,1200}?)(?=<div class="advisory-card-footer"|</section>)', html):
        bullets = [clean_text(li) for li in re.findall(r'<li[^>]*>([\s\S]*?)</li>', cm.group(4)) if clean_text(li)]
        expertise_pillars.append({
            "title": clean_text(cm.group(1)),
            "tagline": clean_text(cm.group(2)),
            "summary": clean_text(cm.group(3)),
            "highlights": bullets,
        })

    # 3. Three Advisory Engagement Models
    engagement_models = []
    for blk in html.split('id="advisoryFormatCard-')[1:]:
        blk = blk.split("<!-- Format ")[0].split("<!-- 30")[0].split("</section>")[0][:2500]
        title_m = re.search(r'<h4 class="advisory-format-card-title"[^>]*>([\s\S]*?)</h4>', blk)
        tag_m = re.search(r'<div class="advisory-format-tagline"[^>]*>([\s\S]*?)</div>', blk)
        desc_m = re.search(r'<p class="advisory-format-card-desc"[^>]*>([\s\S]*?)</p>', blk)
        details = []
        for dm in re.finditer(r'<span class="advisory-detail-label"[^>]*>([\s\S]*?)</span>\s*<span class="advisory-detail-val"[^>]*>([\s\S]*?)</span>', blk):
            details.append({"label": clean_text(dm.group(1)).rstrip(":"), "value": clean_text(dm.group(2))})
        if title_m:
            engagement_models.append({
                "model": clean_text(title_m.group(1)),
                "tagline": clean_text(tag_m.group(1)) if tag_m else "",
                "summary": clean_text(desc_m.group(1)) if desc_m else "",
                "specifications": details,
            })

    # 4. 30-60-90 Day Board Integration Roadmap
    roadmap_phases = []
    for blk in html.split('class="cadence-step-box')[1:]:
        blk = blk[:900]
        days_m = re.search(r'<span class="roadmap-days-badge[^"]*"[^>]*>([\s\S]*?)</span>', blk)
        title_m = re.search(r'<h5 class="step-phase-title"[^>]*>([\s\S]*?)</h5>', blk)
        desc_m = re.search(r'<p class="step-phase-desc"[^>]*>([\s\S]*?)</p>', blk)
        if title_m:
            roadmap_phases.append({
                "phase": clean_text(days_m.group(1)) if days_m else "",
                "title": clean_text(title_m.group(1)),
                "description": clean_text(desc_m.group(1)) if desc_m else "",
            })

    # 5. Executive Case Studies
    case_studies = []
    for cs_title in ("Escaping the LLM Wrapper Trap", "Securing Autonomous Agent Actions", "Inference Unit Economics"):
        cm = re.search(rf'(<h3[^>]*>\s*{re.escape(cs_title)}\s*</h3>[\s\S]{{0,2500}}?)(?=<div class="col-lg-4|</section>|<section|<!-- )', html)
        if cm:
            blk = cm.group(1)
            paras = [clean_text(p) for p in re.findall(r'<p[^>]*>([\s\S]*?)</p>', blk) if clean_text(p)]
            metrics = [clean_text(s) for s in re.findall(r'<span class="badge[^"]*"[^>]*>([\s\S]*?)</span>', blk) if clean_text(s)]
            case_studies.append({
                "title": cs_title,
                "challenge": paras[0] if len(paras) > 0 else "",
                "advisory_contribution": paras[1] if len(paras) > 1 else "",
                "strategic_outcome": paras[2] if len(paras) > 2 else "",
                "summary": " ".join(paras),
                "badges": metrics,
            })

    # 6. Ecosystem Accelerator & Governance Anchor Cards
    ecosystem_cards = []
    eco_idx = html.find("ecosystem-card-col")
    if eco_idx != -1:
        eco_blk = html[eco_idx:eco_idx + 18000]
        for ec in re.split(r'(?=<div class="col-lg-4 col-md-6 mb-4 d-flex ecosystem-card-col")', eco_blk):
            if "ecosystem-card-col" not in ec:
                continue
            ec = ec.split("</section>")[0]
            cat_m = re.search(r'data-category="([^"]+)"', ec)
            t_m = re.search(r'<h3[^>]*>([\s\S]*?)</h3>', ec)
            sub_m = re.search(r'<div class="eco-subtitle[^"]*"[^>]*>([\s\S]*?)</div>', ec)
            p_m = re.search(r'<p[^>]*>([\s\S]*?)</p>', ec)
            if t_m:
                ecosystem_cards.append({
                    "organization": clean_text(t_m.group(1)),
                    "category": cat_m.group(1).strip() if cat_m else "ecosystem",
                    "role": clean_text(sub_m.group(1)) if sub_m else "",
                    "description": clean_text(p_m.group(1)) if p_m else "",
                })

    # 7. Board Mandate Opportunities
    board_mandates = []
    bm_idx = html.find("Startup Advisory Boards")
    if bm_idx != -1:
        bm_blk = html[max(0, bm_idx - 500):bm_idx + 12000]
        for bm in re.finditer(r'<h3[^>]*>([\s\S]*?)</h3>[\s\S]{0,600}?<p[^>]*>([\s\S]*?)</p>', bm_blk):
            bt = clean_text(bm.group(1))
            bd = clean_text(bm.group(2))
            if any(k in bt for k in ("Advisory", "Board", "Committee", "Due Diligence", "Director")):
                board_mandates.append({"title": bt, "description": bd})

    all_event_cards = parse_event_cards()
    judging_only = sum(1 for e in all_event_cards if e.get("category") == "judging")
    speaking_only = sum(1 for e in all_event_cards if e.get("category") in ("conferences", "panels"))
    videos_only = len(parse_keynote_cinema_videos())
    events_total_display = f"{judging_only + speaking_only + videos_only}+"

    links = dedup_links([
        {"label": "Board & Strategic Advisory Hub", "url": f"{CANONICAL_BASE}/page-advisory"},
        {"label": "Board Executive Biography View", "url": f"{CANONICAL_BASE}/board"},
        {"label": "Executive Board Biography (PDF)", "url": f"{CANONICAL_BASE}/files/Harsh_Verma_Board_Biography.pdf"},
        {"label": "UC Berkeley SkyDeck Advisors", "url": "https://skydeck.berkeley.edu/advisors/"},
        {"label": "LinkedIn", "url": "https://www.linkedin.com/in/harshverma59/"},
        {"label": "Wikidata Q139827028", "url": "https://www.wikidata.org/wiki/Q139827028"},
        {"label": "Google Knowledge Graph", "url": "https://www.google.com/search?kgmid=/g/11njtn74r4"},
        {"label": "EverybodyWiki Biography", "url": "https://en.everybodywiki.com/Harsh_Verma_(Software_Engineer)"},
        {"label": "ORCID", "url": "https://orcid.org/0000-0003-2134-2600"},
        {"label": "Google Scholar", "url": "https://scholar.google.com/citations?hl=en&user=zSt9oRMAAAAJ"},
        {"label": "GitHub", "url": "https://github.com/iamharshverma"},
        {"label": "Medium", "url": "https://medium.com/@harshverma59"},
        {"label": "Twitter / X", "url": "https://twitter.com/harshverma59"},
        {"label": "Mastodon", "url": "https://mastodon.social/@harshverma59"},
        {"label": "Instagram", "url": "https://www.instagram.com/aiwithharsh/"},
    ])

    payload = {
        "section": "Board & Strategic Advisory",
        "author": "Harsh Verma, FBCS, SMIEEE, FRSA",
        "page_url": f"{CANONICAL_BASE}/page-advisory",
        "alternate_urls": [f"{CANONICAL_BASE}/advisory", f"{CANONICAL_BASE}/board"],
        "board_biography_pdf": "files/Harsh_Verma_Board_Biography.pdf",
        "board_biography_pdf_url": f"{CANONICAL_BASE}/files/Harsh_Verma_Board_Biography.pdf",
        "ecosystem_stats": {
            "startups_and_ventures_evaluated": "120+",
            "accelerators_and_judging_panels": f"{judging_only}+",
            "total_keynotes_panels_and_judging": events_total_display,
            "enterprise_ai_capital_impacted": "$50M+",
            "technical_fellowship_tier": "Top 8%",
            "peer_reviewed_papers": 27,
            "patents": 7,
            "media_features": "45+",
            "global_awards": 27,
        },
        "governance_flywheel_pillars": flywheel_pillars,
        "core_expertise_pillars": expertise_pillars,
        "advisory_engagement_models": engagement_models,
        "onboarding_roadmap_30_60_90": roadmap_phases,
        "case_studies": case_studies,
        "ecosystem_organizations": ecosystem_cards,
        "board_mandates": board_mandates,
        "primary_url": f"{CANONICAL_BASE}/page-advisory",
        "links": links,
    }

    output_path = os.path.join(DATA_DIR, "advisory_and_board.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    print(f"Exported Board & Strategic Advisory data to {output_path}")
    return payload


def export_patents():
    """17. Export full 7-patent intellectual property portfolio (2 Granted + 5 Palo Alto Networks Filed-Pending) to data/patents.json."""
    patents_list = [
        {
            "id": "patent-555747",
            "patent_number": "555747",
            "application_number": "201711003607",
            "title": "SYSTEMS AND METHODS FOR PERFORMING LOAD TESTING OF A SOCIAL NETWORKING APPLICATION",
            "status": "Granted Patent",
            "issued_date": "Dec 3, 2024",
            "authority": "Indian Patent Office",
            "organization": "Hike Messenger",
            "description": "Novel architecture and methodology for orchestrating automated, high-throughput load simulation, performance stress benchmarking, and real-time telemetry testing across social networking applications and distributed service topologies.",
            "primary_url": "https://iprsearch.ipindia.gov.in/PublicSearch/PublicationSearch/",
            "links": [
                {"label": "Official Patent Search (555747)", "url": "https://iprsearch.ipindia.gov.in/PublicSearch/PublicationSearch/"},
                {"label": "Portfolio Patents Section", "url": f"{CANONICAL_BASE}/page-publications"},
            ],
        },
        {
            "id": "patent-606481",
            "patent_number": "606481",
            "application_number": "202011024968",
            "title": "COVID PREVENTIVE AUTOMATED ENTRY POINT (COPAEP)",
            "status": "Granted Patent",
            "issued_date": "Granted",
            "authority": "Indian Patent Office",
            "organization": "Independent / Research Invention",
            "description": "An integrated automated screening checkpoint system incorporating multi-tier hardware and sensor subsystems for automated non-contact thermal scanning and public health facility entry control.",
            "primary_url": "https://iprsearch.ipindia.gov.in/PublicSearch/PublicationSearch/",
            "links": [
                {"label": "Official Patent Search (606481)", "url": "https://iprsearch.ipindia.gov.in/PublicSearch/PublicationSearch/"},
                {"label": "Portfolio Patents Section", "url": f"{CANONICAL_BASE}/page-publications"},
            ],
        },
        {
            "id": "patent-panw-1",
            "patent_number": "Filed-Pending (PANW-1 of 5)",
            "application_number": "Undisclosed (Enterprise Review)",
            "title": "Autonomous Agentic AI Security & Orchestration Architecture",
            "status": "Filed-Pending",
            "issued_date": "Filed-Pending",
            "authority": "USPTO / Enterprise Patent Filings",
            "organization": "Palo Alto Networks",
            "description": "Proprietary enterprise intellectual property in autonomous agentic AI reasoning guardrails and multi-agent cybersecurity workflows at Palo Alto Networks.",
            "primary_url": "https://www.paloaltonetworks.com/",
            "links": [
                {"label": "Palo Alto Networks", "url": "https://www.paloaltonetworks.com/"},
                {"label": "Portfolio Patents Overview", "url": f"{CANONICAL_BASE}/page-publications"},
            ],
        },
        {
            "id": "patent-panw-2",
            "patent_number": "Filed-Pending (PANW-2 of 5)",
            "application_number": "Undisclosed (Enterprise Review)",
            "title": "Enterprise Copilot Navigation & Guided Workflow Engine",
            "status": "Filed-Pending",
            "issued_date": "Filed-Pending",
            "authority": "USPTO / Enterprise Patent Filings",
            "organization": "Palo Alto Networks",
            "description": "Proprietary copilot navigation and contextual UI/API orchestration mechanisms engineered for mission-critical enterprise security consoles.",
            "primary_url": "https://www.paloaltonetworks.com/",
            "links": [
                {"label": "Palo Alto Networks", "url": "https://www.paloaltonetworks.com/"},
                {"label": "Portfolio Patents Overview", "url": f"{CANONICAL_BASE}/page-publications"},
            ],
        },
        {
            "id": "patent-panw-3",
            "patent_number": "Filed-Pending (PANW-3 of 5)",
            "application_number": "Undisclosed (Enterprise Review)",
            "title": "Intent-Based Agent Telemetry & Runtime Threat Containment",
            "status": "Filed-Pending",
            "issued_date": "Filed-Pending",
            "authority": "USPTO / Enterprise Patent Filings",
            "organization": "Palo Alto Networks",
            "description": "Behavioral intent verification and real-time runtime anomaly containment for autonomous multi-agent enterprise AI deployments.",
            "primary_url": "https://www.paloaltonetworks.com/",
            "links": [
                {"label": "Palo Alto Networks", "url": "https://www.paloaltonetworks.com/"},
                {"label": "Portfolio Patents Overview", "url": f"{CANONICAL_BASE}/page-publications"},
            ],
        },
        {
            "id": "patent-panw-4",
            "patent_number": "Filed-Pending (PANW-4 of 5)",
            "application_number": "Undisclosed (Enterprise Review)",
            "title": "Distributed Real-Time Copilot State Synchronization & Guardrail Enforcement",
            "status": "Filed-Pending",
            "issued_date": "Filed-Pending",
            "authority": "USPTO / Enterprise Patent Filings",
            "organization": "Palo Alto Networks",
            "description": "Low-latency distributed policy enforcement and verifiable audit pipelines for enterprise AI copilot platforms.",
            "primary_url": "https://www.paloaltonetworks.com/",
            "links": [
                {"label": "Palo Alto Networks", "url": "https://www.paloaltonetworks.com/"},
                {"label": "Portfolio Patents Overview", "url": f"{CANONICAL_BASE}/page-publications"},
            ],
        },
        {
            "id": "patent-panw-5",
            "patent_number": "Filed-Pending (PANW-5 of 5)",
            "application_number": "Undisclosed (Enterprise Review)",
            "title": "Zero-Trust Multi-Agent Execution Verification & Contextual Policy Synthesis",
            "status": "Filed-Pending",
            "issued_date": "Filed-Pending",
            "authority": "USPTO / Enterprise Patent Filings",
            "organization": "Palo Alto Networks",
            "description": "Deterministic zero-trust verification and adaptive contextual policy synthesis for enterprise multi-agent security operations at Palo Alto Networks.",
            "primary_url": "https://www.paloaltonetworks.com/",
            "links": [
                {"label": "Palo Alto Networks", "url": "https://www.paloaltonetworks.com/"},
                {"label": "Portfolio Patents Overview", "url": f"{CANONICAL_BASE}/page-publications"},
            ],
        },
    ]

    payload = {
        "section": "Patents & Intellectual Property",
        "inventor": "Harsh Verma",
        "page_url": f"{CANONICAL_BASE}/page-publications",
        "summary_stats": {
            "total_patents": 7,
            "granted_patents": 2,
            "in_process_patents": 5,
            "filed_pending_patents": 5,
            "granted_patent_numbers": ["555747", "606481"],
            "in_process_assignee": "Palo Alto Networks",
        },
        "academic_and_registry_links": [
            {"label": "Indian Patent Office Public Search", "url": "https://iprsearch.ipindia.gov.in/PublicSearch/PublicationSearch/"},
            {"label": "Google Scholar", "url": "https://scholar.google.com/citations?hl=en&user=zSt9oRMAAAAJ"},
            {"label": "ORCID", "url": "https://orcid.org/0000-0003-2134-2600"},
            {"label": "Academia.edu", "url": "https://mygsb.academia.edu/harshverma"},
            {"label": "ResearchGate", "url": "https://www.researchgate.net/profile/Harsh-Verma-43"},
            {"label": "Palo Alto Networks", "url": "https://www.paloaltonetworks.com/"},
        ],
        "patents": patents_list,
    }

    output_path = os.path.join(DATA_DIR, "patents.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    print(f"Exported {len(patents_list)} patents to {output_path}")
    return payload


def export_media_distribution_analytics():
    """18. Export Media Distribution Analytics & Career Trajectory Dossier to data/media_distribution_analytics.json."""
    mda_path = os.path.join(ROOT_DIR, "page-media-distribution-analytics.html")
    html = open(mda_path, "r", encoding="utf-8").read() if os.path.exists(mda_path) else ""

    # Career trajectory milestones (2013 - 2026)
    career_milestones = []
    for blk in html.split('class="timeline-phase-card')[1:]:
        blk = blk.split("<!-- Phase ")[0][:3000]
        yr_m = re.search(r'<span class="timeline-phase-year"[^>]*>([\s\S]*?)</span>', blk)
        t_m = re.search(r'<h5 class="timeline-phase-title"[^>]*>([\s\S]*?)</h5>', blk)
        sub_m = re.search(r'<div class="timeline-phase-subtitle"[^>]*>([\s\S]*?)</div>', blk)
        p_m = re.search(r'<p class="timeline-phase-desc"[^>]*>([\s\S]*?)</p>', blk)
        bullets = [clean_text(li) for li in re.findall(r'<li[^>]*>([\s\S]*?)</li>', blk) if clean_text(li)]
        if t_m:
            career_milestones.append({
                "period_label": clean_text(yr_m.group(1)) if yr_m else "",
                "phase": clean_text(t_m.group(1)),
                "subtitle": clean_text(sub_m.group(1)) if sub_m else "",
                "description": clean_text(p_m.group(1)) if p_m else "",
                "highlights": bullets,
            })

    # Audience cohorts
    cohorts = []
    for cohort_name in ("Engineers", "Founders", "Investors", "General Consumers"):
        cm = re.search(rf'<h3 class="audience-title"[^>]*>\s*{cohort_name}\s*</h3>([\s\S]{{0,1200}}?)(?=<h3 class="audience-title"|<section|<!-- )', html)
        if cm:
            blk = cm.group(1)
            prof_m = re.search(r'<div class="audience-profile"[^>]*>([\s\S]*?)</div>', blk)
            pct_m = re.search(r'width:\s*(\d+%)', blk)
            desc_m = re.search(r'<p class="audience-desc"[^>]*>([\s\S]*?)</p>', blk)
            cohorts.append({
                "cohort": cohort_name,
                "profile": clean_text(prof_m.group(1)) if prof_m else "",
                "share_estimate": pct_m.group(1) if pct_m else "",
                "summary": clean_text(desc_m.group(1)) if desc_m else "",
            })

    media_count = len(json.load(open(os.path.join(ROOT_DIR, "media_data.json"), "r", encoding="utf-8"))) if os.path.exists(os.path.join(ROOT_DIR, "media_data.json")) else 45

    links = dedup_links([
        {"label": "Media Distribution Analytics Dossier", "url": f"{CANONICAL_BASE}/page-media-distribution-analytics"},
        {"label": "Full Media Hub", "url": f"{CANONICAL_BASE}/page-media"},
        {"label": "LinkedIn", "url": "https://www.linkedin.com/in/harshverma59/"},
        {"label": "Instagram (@aiwithharsh)", "url": "https://www.instagram.com/aiwithharsh/"},
        {"label": "Instagram (@iamharshverma)", "url": "https://www.instagram.com/iamharshverma/"},
        {"label": "Twitter / X", "url": "https://twitter.com/harshverma59"},
        {"label": "Medium", "url": "https://medium.com/@harshverma59"},
        {"label": "Mastodon", "url": "https://mastodon.social/@harshverma59"},
        {"label": "GitHub", "url": "https://github.com/iamharshverma"},
        {"label": "ORCID", "url": "https://orcid.org/0000-0003-2134-2600"},
        {"label": "Google Scholar", "url": "https://scholar.google.com/citations?hl=en&user=zSt9oRMAAAAJ"},
        {"label": "Wikidata Q139827028", "url": "https://www.wikidata.org/wiki/Q139827028"},
        {"label": "EverybodyWiki", "url": "https://en.everybodywiki.com/Harsh_Verma_(Software_Engineer)"},
        {"label": "Google Knowledge Graph", "url": "https://www.google.com/search?kgmid=/g/11njtn74r4"},
    ])

    payload = {
        "section": "Media Distribution Analytics & Career Trajectory",
        "author": "Harsh Verma",
        "page_url": f"{CANONICAL_BASE}/page-media-distribution-analytics",
        "headline_metrics": {
            "total_media_features": media_count,
            "total_media_features_display": f"{media_count}+",
            "cumulative_potential_views": "3.75B+",
            "estimated_monthly_reach": "100M+",
            "premier_platforms_count": "7+",
            "syndicated_outlets_sampled": "100+",
            "linkedin_followers": 16816,
            "instagram_engagement_posts": 170,
            "interaction_rate": "7.3%",
            "career_span": "2013 - 2026",
        },
        "tier1_platform_anchors": [
            "Forbes Technology Council",
            "Bloomberg Markets & Tech",
            "AP News Wire",
            "Business Insider",
            "Yahoo Finance",
            "VentureBeat AI",
            "HackerNoon Tech",
            "TechCrunch / Disrupt Coverage",
            "Reuters Technology Wire",
            "Nasdaq Times Square Billboard",
        ],
        "career_journey_timeline": career_milestones,
        "audience_cohorts": cohorts,
        "flywheel_stages": [
            "1. Build Systems",
            "2. Publish Research",
            "3. Media Syndication",
            "4. Keynote Stage",
            "5. Venture & Board Advisory",
            "6. Global Compounding Influence",
        ],
        "primary_url": f"{CANONICAL_BASE}/page-media-distribution-analytics",
        "links": links,
    }

    output_path = os.path.join(DATA_DIR, "media_distribution_analytics.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    print(f"Exported Media Distribution Analytics dossier to {output_path}")
    return payload


def export_social_partnerships():
    """19. Export Partnerships, Creator Authority & Social Hub metadata to data/social_partnerships.json."""
    social_path = os.path.join(ROOT_DIR, "page-social.html")
    html = open(social_path, "r", encoding="utf-8").read() if os.path.exists(social_path) else ""

    partnership_models = []
    for blk in html.split('class="collab-package-card')[1:]:
        blk = blk.split("<!-- Collaboration Card")[0].split("</section>")[0]
        cat_m = re.search(r'<span class="collab-category-badge[^"]*"[^>]*>([\s\S]*?)</span>', blk)
        t_m = re.search(r'<h4 class="collab-card-title"[^>]*>([\s\S]*?)</h4>', blk)
        p_m = re.search(r'<p class="collab-card-desc"[^>]*>([\s\S]*?)</p>', blk)
        bullets = [clean_text(li) for li in re.findall(r'<li[^>]*>([\s\S]*?)</li>', blk) if clean_text(li)]
        if t_m:
            partnership_models.append({
                "title": clean_text(t_m.group(1)),
                "category": clean_text(cat_m.group(1)) if cat_m else "",
                "description": clean_text(p_m.group(1)) if p_m else "",
                "deliverables": bullets,
            })

    links = dedup_links([
        {"label": "Partnerships & Social Hub", "url": f"{CANONICAL_BASE}/page-social"},
        {"label": "ADPList Mentor Profile (Top 1% AI/ML)", "url": "https://adplist.org/mentors/harsh-verma"},
        {"label": "ADPList Community Swag Recognition", "url": "https://adplist-users-production.s3.us-east-1.amazonaws.com/bf7f5f217d25ad3c2eb26b16a6b42201/swags/d9276a51-144d-5fb0-b046-9e03f78fcc1f.webp"},
        {"label": "Favikon Creator Spotlight", "url": "https://spotlight.favikon.com/harshverma59/"},
        {"label": "LinkedIn (@harshverma59)", "url": "https://www.linkedin.com/in/harshverma59/"},
        {"label": "Instagram (@aiwithharsh)", "url": "https://www.instagram.com/aiwithharsh/"},
        {"label": "Instagram (@iamharshverma)", "url": "https://www.instagram.com/iamharshverma/"},
        {"label": "Twitter / X (@harshverma59)", "url": "https://twitter.com/harshverma59"},
        {"label": "Medium (@harshverma59)", "url": "https://medium.com/@harshverma59"},
        {"label": "Mastodon (@harshverma59)", "url": "https://mastodon.social/@harshverma59"},
        {"label": "GitHub (iamharshverma)", "url": "https://github.com/iamharshverma"},
        {"label": "ORCID", "url": "https://orcid.org/0000-0003-2134-2600"},
        {"label": "Google Scholar", "url": "https://scholar.google.com/citations?hl=en&user=zSt9oRMAAAAJ"},
        {"label": "Wikidata Q139827028", "url": "https://www.wikidata.org/wiki/Q139827028"},
        {"label": "EverybodyWiki", "url": "https://en.everybodywiki.com/Harsh_Verma_(Software_Engineer)"},
        {"label": "Google Knowledge Graph", "url": "https://www.google.com/search?kgmid=/g/11njtn74r4"},
    ])

    sp_path = os.path.join(DATA_DIR, "social_posts.json")
    posts_count = len(json.load(open(sp_path, "r", encoding="utf-8"))) if os.path.exists(sp_path) else 12

    payload = {
        "section": "Brand Partnerships, Creator Authority & Social Hub",
        "author": "Harsh Verma",
        "page_url": f"{CANONICAL_BASE}/page-social",
        "creator_metrics": {
            "total_social_posts_indexed": posts_count,
            "linkedin_followers": "16,800+",
            "favikon_authority_score": "79/100",
            "adplist_percentile": "Top 1% AI & ML Engineering Mentor",
            "audience_demographics": {
                "enterprise_tech_leadership_and_vps": "42%",
                "ai_architects_and_engineers": "36%",
                "founders_vcs_and_investors": "22%",
            },
        },
        "partnership_models": partnership_models,
        "primary_url": f"{CANONICAL_BASE}/page-social",
        "links": links,
    }

    output_path = os.path.join(DATA_DIR, "social_partnerships.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    print(f"Exported Social & Partnerships data to {output_path}")
    return payload


def export_speaker_profile():
    """20. Export Speaker Kit stats, speaking formats, audience segments, and streaming links to data/speaker_profile.json."""
    events = parse_event_cards()
    videos = parse_keynote_cinema_videos()
    judging_cnt = sum(1 for e in events if e.get("category") == "judging")
    conferences_cnt = sum(1 for e in events if e.get("category") == "conferences")
    panels_cnt = sum(1 for e in events if e.get("category") == "panels")
    videos_cnt = len(videos)
    total_engagements = judging_cnt + conferences_cnt + panels_cnt + videos_cnt

    links = dedup_links([
        {"label": "Speaker Dossier Hub", "url": f"{CANONICAL_BASE}/page-speaker"},
        {"label": "Events & Keynotes Calendar", "url": f"{CANONICAL_BASE}/page-events"},
        {"label": "Interactive Smart Slides Hub", "url": f"{CANONICAL_BASE}/page-smart-slides"},
        {"label": "Board & Speaker Biography PDF", "url": f"{CANONICAL_BASE}/files/Harsh_Verma_Board_Biography.pdf"},
        {"label": "Champions Speakers Verified Profile", "url": "https://champions-speakers.co.uk/speaker-agent/harsh-verma"},
        {"label": "All American Speakers Verified Profile (#470303)", "url": "https://www.allamericanspeakers.com/speakers/470303/Harsh-Verma"},
        {"label": "Upcoming: Health Tech Week 2027 Speaker Profile (Jan 2027)", "url": "https://healthtechweek.org/speakers/harsh-verma"},
        {"label": "Upcoming: Health Tech Week Portal", "url": "https://healthtechweek.org/"},
        {"label": "Upcoming: HealthTech Summit 2027 Luma Event (#HTSummit27)", "url": "https://luma.com/HTSummit27"},
        {"label": "Upcoming: HealthTech Summit 2027 LinkedIn Feature", "url": "https://lnkd.in/p/gZdmbTmf"},
        {"label": "Xraised: Beyond the Code Video Stream", "url": "https://xraised.com/videos/ai-engineering-beyond-code/stream"},
        {"label": "EasyChair Smart Slides Author Profile", "url": "https://easychair.org/smart-slide/author/v5zJ"},
    ])

    payload = {
        "section": "Executive Speaking Dossier, Keynote Formats & Audience Reach",
        "speaker": "Harsh Verma, FBCS, SMIEEE, FRSA",
        "page_url": f"{CANONICAL_BASE}/page-speaker",
        "events_url": f"{CANONICAL_BASE}/page-events",
        "stats": {
            "judging_and_committees": judging_cnt,
            "conference_keynotes": conferences_cnt,
            "industry_panels_and_salons": panels_cnt,
            "featured_keynote_videos": videos_cnt,
            "total_engagements": total_engagements,
            "total_engagements_display": f"{total_engagements}+",
            "leaders_and_engineers_reached": "5,000+",
            "senior_csuite_founders_pct": "85%+",
            "organizer_recommendation_rate": "98%",
        },
        "verified_speaker_profiles": [
            {
                "bureau": "Champions Speakers",
                "region": "UK & International",
                "url": "https://champions-speakers.co.uk/speaker-agent/harsh-verma",
                "logo": f"{CANONICAL_BASE}/images/events/champions_speakers.svg",
                "image": f"{CANONICAL_BASE}/images/harsh/Harsh_portfolio_pic.png",
            },
            {
                "bureau": "All American Speakers",
                "region": "North America",
                "speaker_id": "470303",
                "url": "https://www.allamericanspeakers.com/speakers/470303/Harsh-Verma",
                "logo": f"{CANONICAL_BASE}/images/events/all_american_speakers.svg",
                "image": f"{CANONICAL_BASE}/images/harsh/harsh_kg_primary.jpg",
            },
        ],
        "upcoming_events": [
            {
                "title": "Health Tech Week 2027 — HealthTech Summit (#HTSummit27)",
                "date": "January 2027",
                "location": "San Francisco, CA",
                "role": "Featured Speaker",
                "speaker_profile_url": "https://healthtechweek.org/speakers/harsh-verma",
                "event_portal_url": "https://healthtechweek.org/",
                "luma_url": "https://luma.com/HTSummit27",
                "linkedin_feature_url": "https://lnkd.in/p/gZdmbTmf",
            }
        ],
        "audience_segments": [
            {"segment": "CEOs & Board Directors", "share": "35%", "focus": "AI governance, unit economics, enterprise transformation"},
            {"segment": "CISOs & Security Architects", "share": "32%", "focus": "Autonomous cyber defense, agentic security, zero-trust"},
            {"segment": "Founders & Venture Investors", "share": "23%", "focus": "Technical moats, GTM scaling, agentic architectures"},
            {"segment": "Scholars & Principal Engineers", "share": "10%", "focus": "Multi-agent systems, research translation, distributed AI"},
        ],
        "speaking_formats": [
            "Flagship Conference Keynotes (30-60 min)",
            "Executive Fireside Chats & Panels",
            "Corporate AI & Security Masterclasses (Half/Full-Day)",
            "Boardroom Briefings & C-Suite Roundtables",
            "Global Hackathon & Startup Pitch Judging",
        ],
        "subject_matter_expertise": [
            "Autonomous Agentic AI Architectures",
            "AI vs. AI Cybersecurity Counteroffensives",
            "Clean Attacks & Intent-Based Security",
            "Distributed Cloud & Real-Time Telemetry Pipelines",
            "From Creator to Curator: Future of Software Engineering",
        ],
        "primary_url": f"{CANONICAL_BASE}/page-speaker",
        "links": links,
    }

    output_path = os.path.join(DATA_DIR, "speaker_profile.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    print(f"Exported Speaker Profile dossier ({total_engagements} total engagements) to {output_path}")
    return payload


def enrich_social_posts():
    """15. Ensure every entry in data/social_posts.json has canonical primary_url and links[]."""
    sp_path = os.path.join(DATA_DIR, "social_posts.json")
    if not os.path.exists(sp_path):
        return []
    with open(sp_path, "r", encoding="utf-8") as f:
        posts = json.load(f)

    updated = []
    for post in posts:
        entry = dict(post)
        post_url = to_canonical_url(entry.get("postUrl", ""))
        platform_label = "LinkedIn Post" if entry.get("platform") == "linkedin" else "Instagram Post"
        raw_links = [{"label": platform_label, "url": post_url}] if post_url else []
        for u in re.findall(r'https?://[^\s"\'<>]+', entry.get("content", "")):
            u_clean = u.rstrip(".,);")
            raw_links.append({"label": "Featured Article / Video", "url": u_clean})
        if entry.get("mediaUrl"):
            raw_links.append({"label": "Post Media Asset", "url": to_canonical_url(entry["mediaUrl"])})
        entry["primary_url"] = post_url
        entry["links"] = dedup_links(raw_links)
        updated.append(entry)

    with open(sp_path, "w", encoding="utf-8") as f:
        json.dump(updated, f, indent=2, ensure_ascii=False)
    print(f"Enriched {len(updated)} social posts with complete links in {sp_path}")
    return updated


def main():
    print("=== Exporting All Portfolio Sections to Individual Comprehensive JSON Files ===")
    j = export_judging()
    s = export_speaking()
    k = export_keynotes()
    m = export_media()
    a = export_awards()
    p = export_publications()
    b = export_books()
    bl = export_blogs()
    vp = export_verified_profiles()
    ma = export_memberships_and_associations()
    ab = export_about()
    pw = export_professional_work()
    sl = export_slides()
    pc = export_projects_certification()
    sp = enrich_social_posts()
    adv = export_advisory_and_board()
    pat = export_patents()
    mda = export_media_distribution_analytics()
    sop = export_social_partnerships()
    spk = export_speaker_profile()

    print("\nSummary of Exported Files:")
    print(f"1.  data/judging_engagements.json:            {len(j)} records")
    print(f"2.  data/speaking_engagements.json:           {len(s)} records")
    print(f"3.  data/keynote_engagements.json:            {len(k)} records")
    print(f"4.  data/media_features.json:                 {len(m)} records")
    print(f"5.  data/awards_and_honors.json:              {len(a)} records")
    print(f"6.  data/research_publications.json:          {len(p)} records")
    print(f"7.  data/books_and_volumes.json:              {len(b)} records")
    print(f"8.  data/blog_articles.json:                  {len(bl)} records")
    print(f"9.  data/verified_profiles.json:              {len(vp)} records")
    print(f"10. data/memberships_and_associations.json:   {len(ma)} records")
    print(f"11. data/about.json:                          {len(ab)} root sections")
    print(f"12. data/professional_work.json:              {len(pw)} root sections")
    print(f"13. data/slides.json:                         {sl['total_decks']} decks ({sl['total_slides']} slides)")
    print(f"14. data/projects_certification.json:         {pc['summary_stats']['total_projects']} projects, {pc['summary_stats']['total_hub_widgets']} widgets, {pc['summary_stats']['total_certifications']} certifications")
    print(f"15. data/social_posts.json:                   {len(sp)} records")
    print(f"16. data/advisory_and_board.json:             {len(adv['ecosystem_organizations'])} ecosystem orgs, {len(adv['board_mandates'])} mandates")
    print(f"17. data/patents.json:                        {pat['summary_stats']['total_patents']} patents ({pat['summary_stats']['granted_patents']} granted, {pat['summary_stats']['in_process_patents']} pending)")
    print(f"18. data/media_distribution_analytics.json:   {mda['headline_metrics']['total_media_features_display']} media features ({mda['headline_metrics']['cumulative_potential_views']} views)")
    print(f"19. data/social_partnerships.json:            {len(sop['partnership_models'])} partnership models")
    print(f"20. data/speaker_profile.json:                {spk['stats']['total_engagements_display']} total engagements")
    print("================================================================================")


if __name__ == "__main__":
    main()
