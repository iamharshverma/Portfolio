#!/usr/bin/env python3
"""
scripts/generate_extra_json.py
Generates:
1. data/memberships.json (harmonized with organization_name, membership_role, membership_id, date_joined, link)
2. data/about.json (complete details from page-about.html, bio, pillars, career milestones, stats, authority identifiers)
3. data/professional_work.json (executive, authoritative review of work, background, publications, books, patents, and critical impact)
"""

import os
import json

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

def generate_memberships():
    kg_path = os.path.join(DATA_DIR, "knowledge-graph.json")
    with open(kg_path, "r", encoding="utf-8") as f:
        kg = json.load(f)

    assocs = kg.get("entities", {}).get("associations", [])

    # Metadata map to harmonize requested keys
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
        }
    }

    enriched = []
    for a in assocs:
        title = a.get("title", "")
        m = meta_map.get(title, {})
        item = {
            "organization_name": m.get("organization_name", title),
            "membership_role": m.get("membership_role", a.get("role", "")),
            "membership_id": m.get("membership_id", a.get("credential_id", "")),
            "date_joined": m.get("date_joined", "2024"),
            "link": m.get("link", a.get("url", "")),
            "title": title,
            "role": a.get("role", ""),
            "tier": a.get("tier", ""),
            "credential_id": a.get("credential_id", ""),
            "category": a.get("category", ""),
            "image": a.get("image", ""),
            "description": a.get("description", ""),
            "url": m.get("link", a.get("url", "")),
            "links": [
                {
                    "url": m.get("link", a.get("url", "")),
                    "label": f"View {m.get('organization_name', title)} Profile"
                }
            ]
        }
        enriched.append(item)

    output_path = os.path.join(DATA_DIR, "memberships.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(enriched, f, indent=2, ensure_ascii=False)

    # Also update memberships_and_associations.json and associations.json
    for alias in ("memberships_and_associations.json", "associations.json"):
        with open(os.path.join(DATA_DIR, alias), "w", encoding="utf-8") as f:
            json.dump(enriched, f, indent=2, ensure_ascii=False)

    print(f"Exported {len(enriched)} enriched memberships to {output_path} and aliases")
    return enriched

if __name__ == "__main__":
    generate_memberships()
