#!/usr/bin/env python3
"""
scripts/build_omnisearch_index.py
Builds the unified 200+ (222 records) Executive Omnisearch Index from:
- research_publications.json (27)
- media_features.json (44)
- speaking_engagements.json (12) + judging_engagements.json (21) = 33 speaking & keynote records
- awards_and_honors.json (27)
- verified_profiles.json (57)
- memberships.json (26)
- books_and_volumes.json (8)
Total = 222 records.
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
        title = p.get("title", "")
        venue = p.get("venue", "")
        year = str(p.get("year", ""))
        doi = p.get("doi", "")
        patent_no = p.get("patent_number", "")
        is_patent = "patent" in title.lower() or "patent" in venue.lower() or "patent_number" in p or "555747" in title or "606481" in title

        keywords = f"{title} {venue} {year} {doi} {patent_no} {p.get('abstract', '')}"
        badge = "Granted Patent" if "Granted" in str(p.get("status", "")) or "555747" in title or "606481" in title else (f"IEEE / {year}" if "IEEE" in venue else f"Peer-Reviewed · {year}")
        badge_class = "badge-success" if "Patent" in badge else "badge-primary"
        icon = "mdi-certificate" if is_patent else "mdi-file-document-outline"

        # URL destination
        url = p.get("primary_url") or p.get("url") or (f"https://doi.org/{doi}" if doi and not doi.startswith("http") else doi) or "page-publications"

        index.append({
            "id": p.get("id", f"pub-{len(index)}"),
            "category": "Publications & Patents",
            "category_pill": "publications",
            "title": title,
            "subtitle": f"{venue} · {year}",
            "badge": badge,
            "badge_class": badge_class,
            "icon": icon,
            "keywords": keywords,
            "url": url,
            "external": url.startswith("http"),
            "description": p.get("abstract", "")[:180] + ("..." if len(p.get("abstract", "")) > 180 else "")
        })

    # 2. Tier-1 Media Features (44 records)
    with open(os.path.join(DATA_DIR, "media_features.json"), "r", encoding="utf-8") as f:
        media = json.load(f)
    for m in media:
        headline = m.get("headline", "")
        outlet = m.get("outlet", "")
        date = m.get("date", "")
        reach = m.get("reach", "")
        tier = m.get("tier", "Tier-1")
        url = m.get("link") or m.get("url") or "page-media"

        keywords = f"{headline} {outlet} {date} {reach} {m.get('topic', '')} {m.get('summary', '')}"

        index.append({
            "id": m.get("id", f"media-{len(index)}"),
            "category": "Tier-1 Media Features",
            "category_pill": "media",
            "title": headline,
            "subtitle": f"{outlet} · {date} · Reach: {reach}",
            "badge": f"{outlet} ({tier})",
            "badge_class": "badge-info",
            "icon": "mdi-newspaper-variant-outline",
            "keywords": keywords,
            "url": url,
            "external": url.startswith("http"),
            "description": m.get("summary", "")[:180] + ("..." if len(m.get("summary", "")) > 180 else "")
        })

    # 3. Speaking & Keynotes (33 records: 12 speaking + 21 judging)
    with open(os.path.join(DATA_DIR, "speaking_engagements.json"), "r", encoding="utf-8") as f:
        speaking = json.load(f)
    for s in speaking:
        title = s.get("title", "")
        event = s.get("event", "")
        year = str(s.get("year", ""))
        format_type = s.get("format", "Keynote")
        url = s.get("video_url") or s.get("url") or s.get("link") or "page-speaker"

        keywords = f"{title} {event} {year} {format_type} {s.get('location', '')} {s.get('description', '')}"

        index.append({
            "id": s.get("id", f"speaking-{len(index)}"),
            "category": "Speaking & Keynotes",
            "category_pill": "keynotes",
            "title": title,
            "subtitle": f"{event} · {year} · {s.get('location', '')}",
            "badge": format_type,
            "badge_class": "badge-warning text-dark",
            "icon": "mdi-microphone-variant",
            "keywords": keywords,
            "url": url,
            "external": url.startswith("http"),
            "description": s.get("description", "")[:180] + ("..." if len(s.get("description", "")) > 180 else "")
        })

    with open(os.path.join(DATA_DIR, "judging_engagements.json"), "r", encoding="utf-8") as f:
        judging = json.load(f)
    for j in judging:
        title = j.get("event", "") or j.get("title", "")
        role = j.get("role", "Grand Jury Judge")
        org = j.get("organization", "")
        date = j.get("date", "")
        url = j.get("link") or j.get("url") or "page-speaker"

        keywords = f"{title} {role} {org} {date} {j.get('scope', '')} {j.get('description', '')}"

        index.append({
            "id": j.get("id", f"judging-{len(index)}"),
            "category": "Speaking & Keynotes",
            "category_pill": "keynotes",
            "title": title,
            "subtitle": f"{role} · {org} ({date})",
            "badge": "Jury & Judging",
            "badge_class": "badge-secondary",
            "icon": "mdi-gavel",
            "keywords": keywords,
            "url": url,
            "external": url.startswith("http"),
            "description": j.get("description", "")[:180] + ("..." if len(j.get("description", "")) > 180 else "")
        })

    # 4. Awards & Honors (27 records)
    with open(os.path.join(DATA_DIR, "awards_and_honors.json"), "r", encoding="utf-8") as f:
        awards = json.load(f)
    for a in awards:
        title = a.get("title", "")
        body = a.get("awarding_body", "") or a.get("organization", "")
        year = str(a.get("year", ""))
        category = a.get("category", "")
        url = a.get("link") or a.get("url") or "page-awards"

        keywords = f"{title} {body} {year} {category} {a.get('description', '')}"

        index.append({
            "id": a.get("id", f"award-{len(index)}"),
            "category": "Awards & Honors",
            "category_pill": "awards",
            "title": title,
            "subtitle": f"{body} · {year}",
            "badge": f"{year} Honor",
            "badge_class": "badge-primary",
            "icon": "mdi-trophy-variant",
            "keywords": keywords,
            "url": url,
            "external": url.startswith("http"),
            "description": a.get("description", "")[:180] + ("..." if len(a.get("description", "")) > 180 else "")
        })

    # 5. Verified Directory Profiles (57 records)
    with open(os.path.join(DATA_DIR, "verified_profiles.json"), "r", encoding="utf-8") as f:
        profiles = json.load(f)
    for pr in profiles:
        name = pr.get("name", "")
        cat = pr.get("category", "")
        handle = pr.get("handle_or_id", "")
        url = pr.get("url", "")

        keywords = f"{name} {cat} {handle} {pr.get('description', '')} {pr.get('verification_method', '')}"

        index.append({
            "id": pr.get("id", f"profile-{len(index)}"),
            "category": "Verified Profiles",
            "category_pill": "profiles",
            "title": name,
            "subtitle": f"{cat} · {handle}",
            "badge": "Verified Registry",
            "badge_class": "badge-success",
            "icon": "mdi-check-decagram",
            "keywords": keywords,
            "url": url,
            "external": url.startswith("http"),
            "description": pr.get("description", "")[:180] + ("..." if len(pr.get("description", "")) > 180 else "")
        })

    # 6. Memberships & Fellowships (26 records)
    with open(os.path.join(DATA_DIR, "memberships.json"), "r", encoding="utf-8") as f:
        memberships = json.load(f)
    for m in memberships:
        org = m.get("organization_name", "") or m.get("title", "")
        role = m.get("membership_role", "") or m.get("role", "")
        mem_id = m.get("membership_id", "") or m.get("credential_id", "")
        date = m.get("date_joined", "")
        url = m.get("link") or m.get("url") or "page-memberships"

        keywords = f"{org} {role} {mem_id} {date} {m.get('description', '')}"

        index.append({
            "id": m.get("id", f"membership-{len(index)}"),
            "category": "Memberships & Fellowships",
            "category_pill": "memberships",
            "title": org,
            "subtitle": f"{role} · {mem_id}",
            "badge": role if len(role) < 22 else "Fellow / Member",
            "badge_class": "badge-primary",
            "icon": "mdi-shield-crown-outline",
            "keywords": keywords,
            "url": url,
            "external": url.startswith("http"),
            "description": m.get("description", "")[:180] + ("..." if len(m.get("description", "")) > 180 else "")
        })

    # 7. Books (8 records)
    with open(os.path.join(DATA_DIR, "books_and_volumes.json"), "r", encoding="utf-8") as f:
        books = json.load(f)
    for b in books:
        title = b.get("title", "")
        publisher = b.get("publisher", "")
        year = str(b.get("year", ""))
        role = b.get("role", "Author")
        url = b.get("link") or b.get("catalog_url") or "page-books"

        keywords = f"{title} {publisher} {year} {role} {b.get('subtitle', '')} {b.get('description', '')}"

        index.append({
            "id": b.get("id", f"book-{len(index)}"),
            "category": "Authored Books & Volumes",
            "category_pill": "books",
            "title": title,
            "subtitle": f"{publisher} · {year} ({role})",
            "badge": role,
            "badge_class": "badge-danger",
            "icon": "mdi-book-open-page-variant",
            "keywords": keywords,
            "url": url,
            "external": url.startswith("http"),
            "description": b.get("description", "")[:180] + ("..." if len(b.get("description", "")) > 180 else "")
        })

    # Save to data/omnisearch_index.json
    out_path = os.path.join(DATA_DIR, "omnisearch_index.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

    print(f"Total Omnisearch Records Indexed: {len(index)}")
    for cat in ["publications", "media", "keynotes", "awards", "profiles", "memberships", "books"]:
        count = sum(1 for item in index if item["category_pill"] == cat)
        print(f" - {cat}: {count} records")

    return index

if __name__ == "__main__":
    build_index()
