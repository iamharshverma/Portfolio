#!/usr/bin/env python3
"""
scripts/build_omnisearch_index.py
Builds the unified Executive Omnisearch Index across all portfolio sections:
- research_publications.json (27) + patents.json (7 patents)
- media_features.json (45)
- speaking_engagements.json (12) + judging_engagements.json (25)
- awards_and_honors.json (27)
- verified_profiles.json (57)
- memberships_and_associations.json (28)
- books_and_volumes.json (8)
- blog_articles.json (31)
- projects_certification.json (13 projects + 24 certifications)
- slides.json (10 interactive Smart Slide decks)
"""

import os
import json

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, "data")

def build_index():
    index = []

    # 1. Publications & Patents (27 records)
    with open(os.path.join(DATA_DIR, "research_publications.json"), "r", encoding="utf-8") as f:
        pubs = json.load(f)
    for p in pubs:
        title = p.get("title", "").strip()
        venue = p.get("venue", "").strip()
        year = str(p.get("year", "")).strip()
        doi = p.get("doi", "").strip()
        patent_no = p.get("patent_number", "").strip()
        is_patent = "patent" in title.lower() or "patent" in venue.lower() or patent_no != "" or "555747" in title or "606481" in title

        keywords = f"{title} {venue} {year} {doi} {patent_no} {p.get('abstract', '')}"
        badge = "Granted Patent" if "Granted" in str(p.get("status", "")) or "555747" in title or "606481" in title else (f"IEEE · {year}" if "IEEE" in venue else f"Peer-Reviewed · {year}")
        badge_class = "badge-success" if "Patent" in badge else "badge-primary"
        icon = "mdi-certificate" if is_patent else "mdi-file-document"

        url = p.get("primary_url") or p.get("link") or (f"https://doi.org/{doi}" if doi and not doi.startswith("http") else doi) or "page-publications"

        index.append({
            "id": p.get("id", f"pub-{len(index)+1}"),
            "category": "Publications & Patents",
            "category_pill": "publications",
            "title": title,
            "subtitle": f"{venue} · {year}" if year else venue,
            "badge": badge,
            "badge_class": badge_class,
            "icon": icon,
            "keywords": keywords,
            "url": url,
            "external": url.startswith("http"),
            "description": p.get("abstract", "").strip()[:180] + ("..." if len(p.get("abstract", "").strip()) > 180 else "")
        })

    # 1b. Patents (7 records from data/patents.json)
    patents_path = os.path.join(DATA_DIR, "patents.json")
    if os.path.exists(patents_path):
        with open(patents_path, "r", encoding="utf-8") as f:
            pat_data = json.load(f)
        for pat in pat_data.get("patents", []):
            title = pat.get("title", "").strip()
            pat_no = pat.get("patent_number", "").strip()
            app_no = pat.get("application_number", "").strip()
            org = pat.get("organization", "").strip()
            status = pat.get("status", "Patent").strip()
            issued = pat.get("issued_date", "").strip()
            url = pat.get("primary_url", "").strip() or "page-publications"
            desc = pat.get("description", "").strip()
            subtitle_parts = [part for part in [status, f"Patent No: {pat_no}" if pat_no else "", f"App: {app_no}" if app_no else "", org] if part]
            badge = "Granted Patent" if "granted" in status.lower() else "Filed-Pending Patent"
            badge_class = "badge-success" if "granted" in status.lower() else "badge-warning text-dark"
            index.append({
                "id": pat.get("id", f"patent-{len(index)+1}"),
                "category": "Publications & Patents",
                "category_pill": "publications",
                "title": title,
                "subtitle": " · ".join(subtitle_parts),
                "badge": badge,
                "badge_class": badge_class,
                "icon": "mdi-certificate",
                "keywords": f"{title} {pat_no} {app_no} {org} {status} {issued} {desc} patent intellectual property",
                "url": url,
                "external": url.startswith("http"),
                "description": desc[:180] + ("..." if len(desc) > 180 else "")
            })

    # 2. Tier-1 Media Features (45 records)
    with open(os.path.join(DATA_DIR, "media_features.json"), "r", encoding="utf-8") as f:
        media = json.load(f)
    for m in media:
        title = m.get("title", "").strip() or m.get("headline", "").strip()
        outlet = m.get("outlet", "").strip()
        date_str = m.get("date_display", "").strip() or str(m.get("year", "")).strip()
        type_lbl = m.get("type_label", "Media Coverage").strip()
        url = m.get("primary_url", "").strip() or m.get("link", "").strip() or "page-media"
        summary = m.get("summary", "").strip() or m.get("highlight", "").strip()

        keywords = f"{title} {outlet} {date_str} {type_lbl} {summary}"

        index.append({
            "id": m.get("id", f"media-{len(index)+1}"),
            "category": "Tier-1 Media Features",
            "category_pill": "media",
            "title": title,
            "subtitle": f"{outlet} · {date_str}" if date_str else outlet,
            "badge": f"{outlet} ({type_lbl})",
            "badge_class": "badge-info",
            "icon": "mdi-newspaper",
            "keywords": keywords,
            "url": url,
            "external": url.startswith("http"),
            "description": summary[:180] + ("..." if len(summary) > 180 else "")
        })

    # 3. Speaking & Keynotes (12 speaking + 25 judging = 37 records)
    with open(os.path.join(DATA_DIR, "speaking_engagements.json"), "r", encoding="utf-8") as f:
        speaking = json.load(f)
    for s in speaking:
        title = s.get("session_title", "").strip() or s.get("event_name", "").strip() or s.get("title", "").strip()
        event = s.get("event_name", "").strip()
        role = s.get("role", "Keynote Speaker").strip()
        date_str = s.get("date", "").strip()
        url = s.get("primary_url", "").strip() or s.get("video_url", "").strip() or s.get("link", "").strip() or "page-speaker"
        desc = s.get("description", "").strip()

        keywords = f"{title} {event} {role} {date_str} {desc}"

        index.append({
            "id": s.get("id", f"speaking-{len(index)+1}"),
            "category": "Speaking & Keynotes",
            "category_pill": "keynotes",
            "title": title,
            "subtitle": f"{role} · {event}" if event else role,
            "badge": "Keynote Speaker",
            "badge_class": "badge-warning text-dark",
            "icon": "mdi-microphone",
            "keywords": keywords,
            "url": url,
            "external": url.startswith("http"),
            "description": desc[:180] + ("..." if len(desc) > 180 else "")
        })

    with open(os.path.join(DATA_DIR, "judging_engagements.json"), "r", encoding="utf-8") as f:
        judging = json.load(f)
    for j in judging:
        title = j.get("event_title", "").strip() or j.get("title", "").strip() or j.get("role", "Grand Jury Judge").strip()
        role = j.get("role", "Grand Jury Judge").strip()
        org = j.get("organizer", "").strip() or j.get("organization", "").strip()
        date_str = j.get("date", "").strip()
        url = j.get("primary_url", "").strip() or j.get("link", "").strip() or "page-speaker"
        desc = j.get("description", "").strip()

        keywords = f"{title} {role} {org} {date_str} {desc}"

        index.append({
            "id": j.get("id", f"judging-{len(index)+1}"),
            "category": "Speaking & Keynotes",
            "category_pill": "keynotes",
            "title": title,
            "subtitle": f"{role}" + (f" · {org}" if org else ""),
            "badge": "Jury & Judging",
            "badge_class": "badge-secondary",
            "icon": "mdi-gavel",
            "keywords": keywords,
            "url": url,
            "external": url.startswith("http"),
            "description": desc[:180] + ("..." if len(desc) > 180 else "")
        })

    # 4. Awards & Honors (27 records)
    with open(os.path.join(DATA_DIR, "awards_and_honors.json"), "r", encoding="utf-8") as f:
        awards = json.load(f)
    for a in awards:
        title = a.get("title", "").strip()
        org = a.get("organization", "").strip() or a.get("awarding_body", "").strip()
        year = str(a.get("year", "")).strip()
        tier = a.get("tier", "International Honoree").strip()
        desc = a.get("description", "").strip()
        links = a.get("links", [])
        first_link = links[0].get("url") if links and isinstance(links, list) and isinstance(links[0], dict) else ""
        url = (a.get("primary_url") or first_link or "page-awards").strip()

        keywords = f"{title} {org} {year} {tier} {desc}"

        index.append({
            "id": a.get("id", f"award-{len(index)+1}"),
            "category": "Awards & Honors",
            "category_pill": "awards",
            "title": title,
            "subtitle": f"{org} · {year}" if year else org,
            "badge": f"{year} Honor" if year else tier,
            "badge_class": "badge-primary",
            "icon": "mdi-trophy-award",
            "keywords": keywords,
            "url": url,
            "external": url.startswith("http"),
            "description": desc[:180] + ("..." if len(desc) > 180 else "")
        })

    # 5. Verified Directory Profiles (57 records)
    with open(os.path.join(DATA_DIR, "verified_profiles.json"), "r", encoding="utf-8") as f:
        profiles = json.load(f)
    for pr in profiles:
        name = pr.get("name", "").strip()
        cat_lbl = pr.get("category_label", "").strip() or pr.get("category", "Directory").strip()
        identifier = pr.get("identifier", "").strip() or pr.get("handle_or_id", "").strip()
        url = pr.get("url", "").strip() or "page-about#verified-profiles"
        desc = pr.get("description", "").strip()

        keywords = f"{name} {cat_lbl} {identifier} {desc} {pr.get('search_keywords', '')}"

        index.append({
            "id": pr.get("id", f"profile-{len(index)+1}"),
            "category": "Verified Profiles",
            "category_pill": "profiles",
            "title": name,
            "subtitle": f"{cat_lbl} · {identifier}" if identifier else cat_lbl,
            "badge": "Verified Registry",
            "badge_class": "badge-success",
            "icon": "mdi-account-check",
            "keywords": keywords,
            "url": url,
            "external": url.startswith("http"),
            "description": desc[:180] + ("..." if len(desc) > 180 else "")
        })

    # 6. Memberships & Fellowships
    with open(os.path.join(DATA_DIR, "memberships_and_associations.json"), "r", encoding="utf-8") as f:
        memberships = json.load(f)
    for m in memberships:
        org = m.get("organization_name", "").strip() or m.get("title", "").strip()
        role = m.get("membership_role", "").strip() or m.get("role", "Member").strip()
        mem_id = m.get("membership_id", "").strip() or m.get("credential_id", "").strip()
        date_str = str(m.get("date_joined", "")).strip()
        url = m.get("link", "").strip() or m.get("url", "").strip() or "page-memberships"
        desc = m.get("description", "").strip()

        keywords = f"{org} {role} {mem_id} {date_str} {desc}"

        badge_text = role if len(role) <= 22 else "Fellow / Member"

        index.append({
            "id": m.get("id", f"membership-{len(index)+1}"),
            "category": "Memberships & Fellowships",
            "category_pill": "memberships",
            "title": org,
            "subtitle": f"{role}" + (f" · ID: {mem_id}" if mem_id else ""),
            "badge": badge_text,
            "badge_class": "badge-primary",
            "icon": "mdi-shield-account",
            "keywords": keywords,
            "url": url,
            "external": url.startswith("http"),
            "description": desc[:180] + ("..." if len(desc) > 180 else "")
        })

    # 7. Books (8 records)
    with open(os.path.join(DATA_DIR, "books_and_volumes.json"), "r", encoding="utf-8") as f:
        books = json.load(f)
    for b in books:
        title = b.get("title", "").strip()
        sub = b.get("subtitle", "").strip()
        publisher = b.get("publisher", "").strip()
        pub_date = str(b.get("publication_date", "")).strip() or str(b.get("year", "")).strip()
        role = b.get("role", "Author").strip()
        url = b.get("catalog_url", "").strip() or b.get("link", "").strip() or "page-books"
        synopsis = b.get("synopsis", "").strip() or b.get("description", "").strip()

        keywords = f"{title} {sub} {publisher} {pub_date} {role} {synopsis}"

        index.append({
            "id": b.get("id", f"book-{len(index)+1}"),
            "category": "Authored Books & Volumes",
            "category_pill": "books",
            "title": title,
            "subtitle": f"{publisher} · {pub_date} ({role})" if pub_date else f"{publisher} ({role})",
            "badge": "Lead Author" if "Lead" in role else "Peer Reviewer",
            "badge_class": "badge-danger",
            "icon": "mdi-book-open-page-variant",
            "keywords": keywords,
            "url": url,
            "external": url.startswith("http"),
            "description": synopsis[:180] + ("..." if len(synopsis) > 180 else "")
        })

    # 8. Blog Articles & Columns (31 records)
    blogs_path = os.path.join(DATA_DIR, "blog_articles.json")
    if os.path.exists(blogs_path):
        with open(blogs_path, "r", encoding="utf-8") as f:
            blogs = json.load(f)
        for bl in blogs:
            title = bl.get("title", "").strip()
            pub = bl.get("publication", "Technical Blog").strip()
            date_str = str(bl.get("date", "")).strip()
            url = (bl.get("primary_url") or bl.get("url") or "page-blog").strip()
            desc = (bl.get("summary") or bl.get("description") or "").strip()
            tags_str = " ".join(bl.get("tags", [])) if isinstance(bl.get("tags"), list) else str(bl.get("tags", ""))
            index.append({
                "id": bl.get("id", f"blog-{len(index)+1}"),
                "category": "Blog & Articles",
                "category_pill": "blogs",
                "title": title,
                "subtitle": f"{pub} · {date_str}" if date_str else pub,
                "badge": pub,
                "badge_class": "badge-info",
                "icon": "mdi-post-outline",
                "keywords": f"{title} {pub} {date_str} {tags_str} {desc} blog article column",
                "url": url,
                "external": url.startswith("http"),
                "description": desc[:180] + ("..." if len(desc) > 180 else "")
            })

    # 9. Projects & Certifications (13 projects + 24 certifications)
    pc_path = os.path.join(DATA_DIR, "projects_certification.json")
    if os.path.exists(pc_path):
        with open(pc_path, "r", encoding="utf-8") as f:
            pc_data = json.load(f)
        for pr in pc_data.get("projects", []):
            title = pr.get("title", "").strip()
            role = pr.get("role", "Enterprise Project").strip()
            status = pr.get("status", "Project").strip()
            tags = " ".join(pr.get("tags", [])) if isinstance(pr.get("tags"), list) else ""
            url = (pr.get("primary_url") or "page-portfolio").strip()
            desc = (pr.get("description") or "").strip()
            index.append({
                "id": pr.get("id", f"proj-{len(index)+1}"),
                "category": "Projects & Certifications",
                "category_pill": "portfolio",
                "title": title,
                "subtitle": f"{role} · {status}",
                "badge": "Featured Project",
                "badge_class": "badge-primary",
                "icon": "mdi-cube-outline",
                "keywords": f"{title} {role} {status} {tags} {desc} project portfolio architecture",
                "url": url,
                "external": url.startswith("http"),
                "description": desc[:180] + ("..." if len(desc) > 180 else "")
            })
        for cert in pc_data.get("certifications", []):
            title = cert.get("title", "").strip()
            issuer = cert.get("issuer", "Verified Credential").strip()
            date_str = str(cert.get("issued", "") or cert.get("date", "")).strip()
            cred_id = cert.get("credential_id", "").strip()
            url = (cert.get("primary_url") or cert.get("verify_url") or "page-portfolio#certifications").strip()
            desc = (cert.get("description") or f"Verified certification issued by {issuer}.").strip()
            index.append({
                "id": cert.get("id", f"cert-{len(index)+1}"),
                "category": "Projects & Certifications",
                "category_pill": "portfolio",
                "title": title,
                "subtitle": f"{issuer}" + (f" · {date_str}" if date_str else ""),
                "badge": "Verified Certification",
                "badge_class": "badge-success",
                "icon": "mdi-certificate-outline",
                "keywords": f"{title} {issuer} {date_str} {cred_id} {desc} certification credential",
                "url": url,
                "external": url.startswith("http"),
                "description": desc[:180] + ("..." if len(desc) > 180 else "")
            })

    # 10. Smart Slides & Decks (10 interactive decks)
    slides_path = os.path.join(DATA_DIR, "slides.json")
    if os.path.exists(slides_path):
        with open(slides_path, "r", encoding="utf-8") as f:
            slides_data = json.load(f)
        for deck in slides_data.get("decks", []):
            title = deck.get("title", "").strip()
            deck_id = deck.get("id", "").strip()
            count = deck.get("count", 0)
            url = (deck.get("portfolioUrl") or deck.get("primary_url") or "page-smart-slides").strip()
            desc = (deck.get("description") or deck.get("subtitle") or "").strip()
            index.append({
                "id": f"slide-{deck_id or len(index)+1}",
                "category": "Smart Slides & Decks",
                "category_pill": "slides",
                "title": title,
                "subtitle": f"EasyChair Smart Slide Ref. {deck_id} · {count} Slides",
                "badge": f"{count} Slides",
                "badge_class": "badge-warning text-dark",
                "icon": "mdi-presentation-play",
                "keywords": f"{title} {deck.get('subtitle', '')} {deck_id} {' '.join(deck.get('tags', []))} {desc} smart slides deck presentation",
                "url": url,
                "external": url.startswith("http"),
                "description": desc[:180] + ("..." if len(desc) > 180 else "")
            })

    # Verify no empty titles or fields
    missing_titles = [r for r in index if not r.get("title")]
    if missing_titles:
        raise ValueError(f"Found {len(missing_titles)} records with missing titles: {missing_titles}")

    # Save to data/omnisearch_index.json
    out_path = os.path.join(DATA_DIR, "omnisearch_index.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

    print(f"Total Omnisearch Records Indexed: {len(index)}")
    for cat in ["publications", "media", "keynotes", "awards", "profiles", "memberships", "books", "blogs", "portfolio", "slides"]:
        count = sum(1 for item in index if item["category_pill"] == cat)
        print(f" - {cat}: {count} records")

    return index

if __name__ == "__main__":
    build_index()
