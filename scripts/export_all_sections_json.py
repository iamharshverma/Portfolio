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


def parse_event_cards():
    """Parse all 33 event cards from page-events.html / page-speaker.html."""
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
            url = l_match.group(1).strip()
            label = clean_text(l_match.group(2))
            if url and label:
                links.append({"label": label, "url": url})

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
        keynotes_list.append({
            "id": f"keynote-{v.get('id', '')}",
            "keynote_title": v.get("title", ""),
            "event_name": v.get("outlet", ""),
            "organizer": v.get("outlet", "").split("(")[0].strip(),
            "date": v.get("date", ""),
            "duration": v.get("duration", ""),
            "format": "Keynote Cinema & Recorded Address",
            "youtube_id": v.get("id", ""),
            "recording_url": v.get("recording_url", ""),
            "slides_url": v.get("slides_url", ""),
            "thumbnail_url": v.get("thumb", ""),
            "synopsis": v.get("desc", ""),
            "key_takeaways": v.get("tags", []),
            "primary_url": v.get("recording_url") or v.get("slides_url", ""),
        })

    # Also include the conference keynotes from event cards
    all_events = parse_event_cards()
    for ev in all_events:
        if "keynote" in ev["title"].lower() and not any(k["keynote_title"] == ev["title"] for k in keynotes_list):
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
                "slides_url": "",
                "thumbnail_url": "",
                "synopsis": ev["description"],
                "key_takeaways": ev["tags"],
                "primary_url": ev["primary_url"],
            })

    output_path = os.path.join(DATA_DIR, "keynote_engagements.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(keynotes_list, f, indent=2, ensure_ascii=False)
    print(f"Exported {len(keynotes_list)} headline keynotes to {output_path}")
    return keynotes_list


def export_media():
    """4. Export 44 media features and press features."""
    media_path = os.path.join(ROOT_DIR, "media_data.json")
    with open(media_path, "r", encoding="utf-8") as f:
        media = json.load(f)

    output_path = os.path.join(DATA_DIR, "media_features.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(media, f, indent=2, ensure_ascii=False)
    print(f"Exported {len(media)} media features to {output_path}")
    return media


def export_awards():
    """5. Export 27 prestigious awards and global technology honors."""
    awards_path = os.path.join(ROOT_DIR, "awards_data.json")
    with open(awards_path, "r", encoding="utf-8") as f:
        awards = json.load(f)

    output_path = os.path.join(DATA_DIR, "awards_and_honors.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(awards, f, indent=2, ensure_ascii=False)
    print(f"Exported {len(awards)} awards & honors to {output_path}")
    return awards


def export_publications():
    """6. Export 27 peer-reviewed publications and patents."""
    papers_path = os.path.join(ROOT_DIR, "papers_data.json")
    with open(papers_path, "r", encoding="utf-8") as f:
        papers = json.load(f)

    output_path = os.path.join(DATA_DIR, "research_publications.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(papers, f, indent=2, ensure_ascii=False)
    print(f"Exported {len(papers)} research publications & patents to {output_path}")
    return papers


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
            "catalog_url": "https://www.harshverma.me/page-books#beyond-ai-engineering",
            "cover_image": "images/books/book_creator_to_curator.png"
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
            "catalog_url": "https://www.harshverma.me/page-books#ai-vs-ai",
            "cover_image": "images/books/book_cybersecurity_counteroffensive.png"
        },
        {
            "id": "book-review-ai-ethics-in-action",
            "title": "AI Ethics in Action",
            "subtitle": "Critical Perspectives on Enterprise AI Transparency and Alignment",
            "role": "Technical Book Reviewer",
            "publication_status": "Technical Peer Review",
            "publication_date": "2025",
            "publisher": "Packt Publishing",
            "synopsis": "Official peer-reviewed technical evaluation of operational AI ethics frameworks, examining fairness metrics, algorithmic auditing, explainability in production deployments, and human-in-the-loop oversight.",
            "key_themes": ["AI Ethics", "Algorithmic Transparency", "Explainable AI (XAI)", "Responsible AI"],
            "catalog_url": "https://www.packtpub.com/",
            "cover_image": "images/books/review_ai_ethics.png"
        },
        {
            "id": "book-review-hands-on-ai-dev",
            "title": "Hands-On AI Dev with Python",
            "subtitle": "Engineering Scalable Machine Learning Pipelines in Production",
            "role": "Technical Book Reviewer",
            "publication_status": "Technical Peer Review",
            "publication_date": "2025",
            "publisher": "Packt Publishing",
            "synopsis": "Rigorous technical review of end-to-end Python machine learning architectures, microservice model serving, distributed caching, and performance benchmarking for high-scale enterprise systems.",
            "key_themes": ["Python ML", "High-Throughput Pipelines", "Production AI", "Distributed Systems"],
            "catalog_url": "https://www.packtpub.com/",
            "cover_image": "images/books/review_hands_on_ai.png"
        },
        {
            "id": "book-review-leadership-ai",
            "title": "Leadership at the Helm of AI",
            "subtitle": "Executive Playbook for Navigating Disruptive AI Transformation",
            "role": "Technical Book Reviewer",
            "publication_status": "Technical Peer Review",
            "publication_date": "2025",
            "publisher": "Packt Publishing",
            "synopsis": "Technical evaluation of executive strategies for organizational AI adoption, balancing ROI velocity against architectural resilience, technical debt, and enterprise workforce upskilling.",
            "key_themes": ["AI Leadership", "Enterprise Strategy", "Organizational Transformation", "AI ROI"],
            "catalog_url": "https://www.packtpub.com/",
            "cover_image": "images/books/review_leadership_ai.png"
        },
        {
            "id": "book-review-python-algo-trading",
            "title": "Python for Algorithmic Trading Cookbook",
            "subtitle": "Recipes for Designing and Testing Real-Time Quantitative Trading Strategies",
            "role": "Technical Book Reviewer",
            "publication_status": "Technical Peer Review",
            "publication_date": "2024",
            "publisher": "Packt Publishing",
            "synopsis": "Comprehensive technical review of low-latency algorithmic trading backends, real-time market data streaming with Kafka and NumPy, and quantitative risk management architectures.",
            "key_themes": ["Algorithmic Trading", "Quantitative Systems", "Real-Time Streaming", "Python FinTech"],
            "catalog_url": "https://www.packtpub.com/",
            "cover_image": "images/books/review_python_trading.png"
        },
        {
            "id": "book-review-ml-genai-marketing",
            "title": "Machine Learning & Generative AI for Marketing",
            "subtitle": "Practical Techniques for Personalization, Content Generation, and Customer Intelligence",
            "role": "Technical Book Reviewer",
            "publication_status": "Technical Peer Review",
            "publication_date": "2024",
            "publisher": "Packt Publishing",
            "synopsis": "Expert peer review of generative AI workflows for personalized customer experiences, predictive churn analytics, and multi-modal campaign orchestration at scale.",
            "key_themes": ["Generative AI", "Customer Intelligence", "Multi-Modal AI", "Predictive Analytics"],
            "catalog_url": "https://www.packtpub.com/",
            "cover_image": "images/books/review_genai_marketing.png"
        },
        {
            "id": "book-review-tensorflow-workshop",
            "title": "The TensorFlow Workshop",
            "subtitle": "A New, Interactive Approach to Learning Deep Neural Networks",
            "role": "Technical Book Reviewer",
            "publication_status": "Technical Peer Review",
            "publication_date": "2023",
            "publisher": "Packt Publishing",
            "synopsis": "Thorough technical review covering deep neural network fundamentals, convolutional and recurrent layers, distributed training on GPUs/TPUs, and TensorFlow Lite edge deployments.",
            "key_themes": ["TensorFlow", "Deep Learning", "Edge AI", "Distributed Training"],
            "catalog_url": "https://www.packtpub.com/",
            "cover_image": "images/books/review_tensorflow.png"
        }
    ]

    output_path = os.path.join(DATA_DIR, "books_and_volumes.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(books_detailed, f, indent=2, ensure_ascii=False)
    print(f"Exported {len(books_detailed)} books & reviewed volumes to {output_path}")
    return books_detailed


def export_blogs():
    """8. Export 31 articles and executive thought leadership essays."""
    kg_path = os.path.join(ROOT_DIR, "data", "knowledge-graph.json")
    with open(kg_path, "r", encoding="utf-8") as f:
        kg = json.load(f)

    blogs = kg.get("entities", {}).get("blogs", [])
    blogs_list = list(blogs)

    existing_urls = {b.get("url") for b in blogs_list}

    # Add the latest Forbes pieces and Substack articles if missing
    additional_blogs = [
        {
            "id": "forbes-physical-ai-coming",
            "title": "Physical AI Is Coming: When AI Stops Generating Content And Starts Acting On The World",
            "platform": "Forbes Technology Council",
            "platform_short": "Forbes",
            "category": "Physical AI & Robotics",
            "date": "October 27, 2026",
            "read_time": "7 min read",
            "url": "https://www.forbes.com/councils/forbestechcouncil/2026/10/27/physical-ai-is-coming-when-ai-stops-generating-content-and-starts-acting-on-the-world/",
            "spotify_url": "",
            "author_profile": "https://www.forbes.com/councils/forbestechcouncil/people/harshverma/",
            "image": "images/blog/thumbnails/forbes-physical-ai.jpg",
            "description": "Explores the frontier transition from digital chat models to embodied, actuator-driven physical AI systems. Analyzes irreversible physical consequences, real-time cyber-physical security, sensor provenance, and latency requirements in robotic enterprise workflows.",
            "tags": ["Forbes Tech Council", "Physical AI", "Robotics", "Embodied AI", "Cyber-Physical Safety"]
        },
        {
            "id": "founders-creative-corporate-startup-co-innovation",
            "title": "Unlocking Corporate-Startup Co-Innovation: Tactical Playbook for Enterprise Growth",
            "platform": "Founders' Creative Substack",
            "platform_short": "Substack",
            "category": "Venture & Innovation Strategy",
            "date": "September 15, 2026",
            "read_time": "5 min read",
            "url": "https://founderscreative.substack.com/p/unlocking-corporatestartup-co-innovation",
            "spotify_url": "",
            "author_profile": "https://founderscreative.substack.com/",
            "image": "images/blog/thumbnails/founders-creative-innovation.jpg",
            "description": "Strategic blueprint on aligning enterprise risk tolerances with early-stage founder agility. Formulates joint proof-of-concept roadmaps, sandboxed AI evaluation environments, and scalable IP co-ownership models.",
            "tags": ["Founders Creative", "Co-Innovation", "Venture Strategy", "Enterprise AI Adoption"]
        }
    ]

    for ab in additional_blogs:
        if ab["url"] not in existing_urls:
            blogs_list.append(ab)

    output_path = os.path.join(DATA_DIR, "blog_articles.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(blogs_list, f, indent=2, ensure_ascii=False)
    print(f"Exported {len(blogs_list)} blog articles to {output_path}")
    return blogs_list


def export_verified_profiles():
    """9. Export all 57 verified directory profiles."""
    about_path = os.path.join(ROOT_DIR, "page-about.html")
    with open(about_path, "r", encoding="utf-8") as f:
        html = f.read()

    card_matches = re.finditer(
        r'<div class="col-lg-4 col-md-6 mb-4 profile-card-item"[^>]*data-category="([^"]+)"[^>]*data-search="([^"]*)"[^>]*>([\s\S]*?)(?=(?:<div class="col-lg-4 col-md-6 mb-4 profile-card-item"|<div id="noProfilesFound"|<!-- Empty State|\Z))',
        html,
    )

    profiles = []
    seen_urls = set()

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

        url_match = re.search(r'<a\s+[^>]*href="([^"]+)"[^>]*class="btn-hub-action', chunk)
        url = url_match.group(1).strip() if url_match else ""

        if not url:
            generic_url = re.search(r'href="([^"]+)"', chunk)
            url = generic_url.group(1).strip() if generic_url else ""

        if url and url not in seen_urls:
            seen_urls.add(url)
            profiles.append({
                "id": "profile-" + re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-"),
                "name": title,
                "category": category,
                "category_label": category_label,
                "identifier": identifier,
                "description": description,
                "url": url,
                "icon_svg": thumb,
                "search_keywords": search_kw,
            })

    output_path = os.path.join(DATA_DIR, "verified_profiles.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(profiles, f, indent=2, ensure_ascii=False)
    print(f"Exported {len(profiles)} verified profiles to {output_path}")
    return profiles


def export_memberships_and_associations():
    """10. Export all 26 verified associations, fellowships & memberships."""
    kg_path = os.path.join(ROOT_DIR, "data", "knowledge-graph.json")
    with open(kg_path, "r", encoding="utf-8") as f:
        kg = json.load(f)

    assocs = kg.get("entities", {}).get("associations", [])

    output_path = os.path.join(DATA_DIR, "memberships_and_associations.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(assocs, f, indent=2, ensure_ascii=False)
    
    # Also write alias filenames for developer convenience
    for alias_name in ("associations.json", "memberships.json"):
        alias_path = os.path.join(DATA_DIR, alias_name)
        with open(alias_path, "w", encoding="utf-8") as f:
            json.dump(assocs, f, indent=2, ensure_ascii=False)

    print(f"Exported {len(assocs)} memberships & associations to {output_path} (and aliases)")
    return assocs


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

    print("\nSummary of Exported Files:")
    print(f"1.  data/judging_engagements.json:           {len(j)} records")
    print(f"2.  data/speaking_engagements.json:          {len(s)} records")
    print(f"3.  data/keynote_engagements.json:           {len(k)} records")
    print(f"4.  data/media_features.json:                {len(m)} records")
    print(f"5.  data/awards_and_honors.json:             {len(a)} records")
    print(f"6.  data/research_publications.json:         {len(p)} records")
    print(f"7.  data/books_and_volumes.json:             {len(b)} records")
    print(f"8.  data/blog_articles.json:                 {len(bl)} records")
    print(f"9.  data/verified_profiles.json:             {len(vp)} records")
    print(f"10. data/memberships_and_associations.json:  {len(ma)} records (also as associations.json & memberships.json)")
    print("================================================================================")


if __name__ == "__main__":
    main()
