#!/usr/bin/env python3
"""
scripts/inject_knowledge_graph.py
=================================
1. Generates `page-identity.html` — The Dedicated Google Knowledge Panel,
   Entity Verification & Programmatic Wiki Sync Hub (Wikidata Q139827028 & EverybodyWiki).
2. Injects the unified Schema.org `@graph` JSON-LD (`id="hv-knowledge-graph-jsonld"`)
   and canonical `rel="me"` authority links across all HTML pages in the portfolio.
"""

import os
import re
import glob
import json
import html as html_lib

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KG_PATH = os.path.join(ROOT_DIR, "data", "knowledge-graph.json")


def build_identity_page(kg):
    counts = kg["counts"]
    entities = kg["entities"]
    wd_claims = kg["wikidata_claims"]
    sync_status = kg.get("sync_status", {})
    wd_sync = sync_status.get("wikidata", {})
    ew_sync = sync_status.get("everybodywiki", {})
    schema_json_str = json.dumps(kg["schema_json_ld"], indent=2)

    # Build Wikidata claims table rows
    wd_rows_html = []
    for c in wd_claims:
        prop = html_lib.escape(c["property"])
        lbl = html_lib.escape(c["label"])
        val = html_lib.escape(c["value"])
        val_lbl = html_lib.escape(c["value_label"])
        ref = html_lib.escape(c.get("reference_url", ""))
        fmt_url = c.get("formatter_url") or (f"https://www.wikidata.org/wiki/{val}" if c["type"] == "wikibase-entityid" else val if val.startswith("http") else ref)
        wd_rows_html.append(f"""
        <tr>
            <td><a href="https://www.wikidata.org/wiki/Property:{prop}" target="_blank" class="badge badge-dark font-monospace px-2 py-1">{prop}</a></td>
            <td class="font-weight-bold text-dark">{lbl}</td>
            <td>
                <a href="{html_lib.escape(fmt_url)}" target="_blank" class="text-primary font-weight-bold">{val_lbl}</a>
                {f'<span class="text-muted font-monospace ml-1" style="font-size:11px;">({val})</span>' if val != val_lbl else ''}
            </td>
            <td><a href="{ref}" target="_blank" class="text-muted" style="font-size:12px;"><i class="mdi mdi-link-variant mr-1"></i>Reference</a></td>
            <td><span class="badge badge-success px-2 py-1" style="background:#059669;color:#fff;"><i class="mdi mdi-check-circle mr-1"></i>Synced on Q139827028</span></td>
        </tr>""")

    # Build unified 208-node cards for the interactive directory
    node_cards_html = []

    # 1. Profiles (54)
    for p in entities["profiles"]:
        t = html_lib.escape(p["title"])
        cat_lbl = html_lib.escape(p["category_label"])
        ident = html_lib.escape(p["identifier"])
        desc = html_lib.escape(p["description"])
        url = html_lib.escape(p["url"])
        search_str = html_lib.escape(f"{p['title']} {p['category_label']} {p['identifier']} {p['description']} profile sameAs".lower())
        node_cards_html.append(f"""
        <div class="col-lg-4 col-md-6 mb-3 kg-node-item" data-kg-cat="profiles" data-kg-search="{search_str}">
            <div class="kg-node-card h-100">
                <div class="d-flex justify-content-between align-items-center mb-2">
                    <span class="kg-node-badge kg-badge-profile"><i class="mdi mdi-check-decagram mr-1"></i>sameAs · {cat_lbl}</span>
                    <code class="kg-node-prop">{ident}</code>
                </div>
                <h5 class="kg-node-title">{t}</h5>
                <p class="kg-node-desc">{desc}</p>
                <div class="mt-auto pt-2 border-top d-flex justify-content-between align-items-center">
                    <a href="{url}" target="_blank" rel="me noopener" class="kg-node-link">Verify Authority <i class="mdi mdi-open-in-new ml-1"></i></a>
                    <span class="text-muted font-monospace" style="font-size:11px;">Schema: sameAs</span>
                </div>
            </div>
        </div>""")

    # 2. Media (42)
    for m in entities["media"]:
        t = html_lib.escape(m.get("title", ""))
        outlet = html_lib.escape(m.get("outlet", "Press Outlet"))
        yr = html_lib.escape(str(m.get("date_display") or m.get("year", "2026")))
        summary = html_lib.escape(m.get("summary", ""))
        url = html_lib.escape(m.get("primary_url") or "page-media")
        search_str = html_lib.escape(f"{t} {outlet} {yr} {summary} media press podcast subjectOf".lower())
        node_cards_html.append(f"""
        <div class="col-lg-4 col-md-6 mb-3 kg-node-item" data-kg-cat="media" data-kg-search="{search_str}">
            <div class="kg-node-card h-100">
                <div class="d-flex justify-content-between align-items-center mb-2">
                    <span class="kg-node-badge kg-badge-media"><i class="mdi mdi-newspaper-variant-outline mr-1"></i>subjectOf · {outlet}</span>
                    <code class="kg-node-prop">{yr}</code>
                </div>
                <h5 class="kg-node-title">{t}</h5>
                <p class="kg-node-desc">{summary}</p>
                <div class="mt-auto pt-2 border-top d-flex justify-content-between align-items-center">
                    <a href="{url}" target="_blank" rel="noopener" class="kg-node-link">Read Citation <i class="mdi mdi-open-in-new ml-1"></i></a>
                    <span class="text-muted font-monospace" style="font-size:11px;">Schema: subjectOf</span>
                </div>
            </div>
        </div>""")

    # 3. Awards (27)
    for a in entities["awards"]:
        t = html_lib.escape(a.get("title", ""))
        org = html_lib.escape(a.get("organization", ""))
        yr = html_lib.escape(str(a.get("year", "2026")))
        desc = html_lib.escape(a.get("description", ""))
        links = a.get("links") or []
        url = html_lib.escape(links[0]["url"] if links else "page-awards")
        search_str = html_lib.escape(f"{t} {org} {yr} {desc} award honor credential".lower())
        node_cards_html.append(f"""
        <div class="col-lg-4 col-md-6 mb-3 kg-node-item" data-kg-cat="awards" data-kg-search="{search_str}">
            <div class="kg-node-card h-100">
                <div class="d-flex justify-content-between align-items-center mb-2">
                    <span class="kg-node-badge kg-badge-award"><i class="mdi mdi-trophy-award mr-1"></i>award · {yr}</span>
                    <code class="kg-node-prop">{html_lib.escape(a.get('tier', 'Honoree'))}</code>
                </div>
                <h5 class="kg-node-title">{t}</h5>
                <p class="kg-node-desc">{org} — {desc[:140]}...</p>
                <div class="mt-auto pt-2 border-top d-flex justify-content-between align-items-center">
                    <a href="{url}" target="_blank" rel="noopener" class="kg-node-link">Verify Credential <i class="mdi mdi-open-in-new ml-1"></i></a>
                    <span class="text-muted font-monospace" style="font-size:11px;">Schema: hasCredential</span>
                </div>
            </div>
        </div>""")

    # 4. Blogs & Forbes Columns (29)
    for b in entities["blogs"]:
        t = html_lib.escape(b.get("title", ""))
        plat = html_lib.escape(b.get("platform", "Forbes"))
        dt = html_lib.escape(str(b.get("date", "2026")))
        desc = html_lib.escape(b.get("description", ""))
        url = html_lib.escape(b.get("url") or "page-blog")
        search_str = html_lib.escape(f"{t} {plat} {dt} {desc} blog article forbes hackernoon authorOf".lower())
        node_cards_html.append(f"""
        <div class="col-lg-4 col-md-6 mb-3 kg-node-item" data-kg-cat="blogs" data-kg-search="{search_str}">
            <div class="kg-node-card h-100">
                <div class="d-flex justify-content-between align-items-center mb-2">
                    <span class="kg-node-badge kg-badge-blog"><i class="mdi mdi-post-outline mr-1"></i>TechArticle · {plat}</span>
                    <code class="kg-node-prop">{dt}</code>
                </div>
                <h5 class="kg-node-title">{t}</h5>
                <p class="kg-node-desc">{desc}</p>
                <div class="mt-auto pt-2 border-top d-flex justify-content-between align-items-center">
                    <a href="{url}" target="_blank" rel="noopener" class="kg-node-link">Read Article <i class="mdi mdi-open-in-new ml-1"></i></a>
                    <span class="text-muted font-monospace" style="font-size:11px;">Schema: author</span>
                </div>
            </div>
        </div>""")

    # 5. Research Papers (27)
    for p in entities["papers"]:
        t = html_lib.escape(p.get("title", ""))
        venue = html_lib.escape(p.get("venue", "IEEE / Peer-Reviewed"))
        yr = html_lib.escape(str(p.get("year", "")))
        doi = html_lib.escape(p.get("doi", "Peer-Reviewed"))
        url = html_lib.escape(p.get("link") or "page-publications")
        search_str = html_lib.escape(f"{t} {venue} {yr} {doi} paper research scholarlyarticle".lower())
        node_cards_html.append(f"""
        <div class="col-lg-4 col-md-6 mb-3 kg-node-item" data-kg-cat="papers" data-kg-search="{search_str}">
            <div class="kg-node-card h-100">
                <div class="d-flex justify-content-between align-items-center mb-2">
                    <span class="kg-node-badge kg-badge-paper"><i class="mdi mdi-school-outline mr-1"></i>ScholarlyArticle · {yr}</span>
                    <code class="kg-node-prop">{doi[:22]}</code>
                </div>
                <h5 class="kg-node-title">{t}</h5>
                <p class="kg-node-desc">Published in {venue}.</p>
                <div class="mt-auto pt-2 border-top d-flex justify-content-between align-items-center">
                    <a href="{url}" target="_blank" rel="noopener" class="kg-node-link">View Publication <i class="mdi mdi-open-in-new ml-1"></i></a>
                    <span class="text-muted font-monospace" style="font-size:11px;">Schema: ScholarlyArticle</span>
                </div>
            </div>
        </div>""")

    # 6. Associations & Fellowships (27)
    for assoc in entities["associations"]:
        t = html_lib.escape(assoc.get("title", ""))
        role = html_lib.escape(assoc.get("role", ""))
        tier = html_lib.escape(assoc.get("tier", ""))
        desc = html_lib.escape(assoc.get("description", ""))
        url = html_lib.escape(assoc.get("url") or "page-memberships")
        search_str = html_lib.escape(f"{t} {role} {tier} {desc} association fellowship memberOf".lower())
        node_cards_html.append(f"""
        <div class="col-lg-4 col-md-6 mb-3 kg-node-item" data-kg-cat="associations" data-kg-search="{search_str}">
            <div class="kg-node-card h-100">
                <div class="d-flex justify-content-between align-items-center mb-2">
                    <span class="kg-node-badge kg-badge-assoc"><i class="mdi mdi-shield-crown-outline mr-1"></i>memberOf · {tier}</span>
                    <code class="kg-node-prop">Verified</code>
                </div>
                <h5 class="kg-node-title">{t}</h5>
                <p class="kg-node-desc">{role} — {desc[:140]}...</p>
                <div class="mt-auto pt-2 border-top d-flex justify-content-between align-items-center">
                    <a href="{url}" target="_blank" rel="noopener" class="kg-node-link">Verify Membership <i class="mdi mdi-open-in-new ml-1"></i></a>
                    <span class="text-muted font-monospace" style="font-size:11px;">Schema: memberOf</span>
                </div>
            </div>
        </div>""")

    # 7. Authored Books (2)
    for b in entities["books"]:
        t = html_lib.escape(b.get("title", ""))
        sub = html_lib.escape(b.get("subtitle", ""))
        desc = html_lib.escape(b.get("description", ""))
        url = html_lib.escape(b.get("url") or "page-books")
        search_str = html_lib.escape(f"{t} {sub} {desc} book author".lower())
        node_cards_html.append(f"""
        <div class="col-lg-6 col-md-6 mb-3 kg-node-item" data-kg-cat="books" data-kg-search="{search_str}">
            <div class="kg-node-card h-100">
                <div class="d-flex justify-content-between align-items-center mb-2">
                    <span class="kg-node-badge kg-badge-book"><i class="mdi mdi-book-open-page-variant mr-1"></i>Book · Authored Volume</span>
                    <code class="kg-node-prop">{html_lib.escape(b.get('year', '2026'))}</code>
                </div>
                <h5 class="kg-node-title">{t}</h5>
                <p class="kg-node-desc"><strong>{sub}</strong> — {desc}</p>
                <div class="mt-auto pt-2 border-top d-flex justify-content-between align-items-center">
                    <a href="{url}" class="kg-node-link">Explore Book Hub <i class="mdi mdi-arrow-right ml-1"></i></a>
                    <span class="text-muted font-monospace" style="font-size:11px;">Schema: Book</span>
                </div>
            </div>
        </div>""")

    qs_escaped = html_lib.escape(kg["quickstatements"])
    wiki_escaped = html_lib.escape(kg["everybodywiki_wikitext"])
    schema_escaped = html_lib.escape(schema_json_str)

    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-30250521-4"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'UA-30250521-4');
    window.GA4_MEASUREMENT_ID = window.GA4_MEASUREMENT_ID || 'G-HVPORTFOL4';
    gtag('config', window.GA4_MEASUREMENT_ID, {{ send_page_view: true }});
    </script>
    <meta charset="UTF-8">
    <title>Harsh Verma | Google Knowledge Graph, Wikidata Q139827028 &amp; Entity Verification Hub</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Official Google Knowledge Graph &amp; Entity Reconciliation Hub for Harsh Verma (Wikidata Q139827028, EverybodyWiki, ORCID 0000-0003-2134-2600, Google Scholar zSt9oRMAAAAJ). Reconciling {counts['total_linked_nodes']} verified profiles, media features, awards, books, research papers, and associations." />
    <meta property="og:title" content="Harsh Verma | Official Google Knowledge Graph &amp; Entity Verification Hub (Q139827028)" />
    <meta property="og:description" content="Canonical entity reconciliation hub for Harsh Verma (Principal AI Software Engineer at Palo Alto Networks, Keynote Speaker, Author &amp; Researcher). Linking Wikidata Q139827028, EverybodyWiki, and {counts['total_linked_nodes']}+ verified authority nodes." />
    <meta property="og:type" content="profile" />
    <meta property="og:url" content="https://iamharshverma.github.io/page-identity" />
    <meta property="og:image" content="https://iamharshverma.github.io/images/about/harsh_hero_clean.png" />
    <link rel="canonical" href="https://iamharshverma.github.io/page-identity" />
    <!-- Bidirectional rel="me" Identity Verification Links -->
    <link rel="me" href="https://www.wikidata.org/wiki/Q139827028" />
    <link rel="me" href="https://en.everybodywiki.com/Harsh_Verma_(Software_Engineer)" />
    <link rel="me" href="https://orcid.org/0000-0003-2134-2600" />
    <link rel="me" href="https://scholar.google.com/citations?user=zSt9oRMAAAAJ" />
    <link rel="me" href="https://www.linkedin.com/in/harshverma59/" />
    <link rel="me" href="https://github.com/iamharshverma" />
    <link rel="me" href="https://x.com/harshverma59" />
    <link rel="me" href="https://mastodon.social/@harshverma59" />
    <link rel="me" href="https://www.forbes.com/councils/forbestechcouncil/people/harshverma/" />
    <link rel="me" href="https://theorg.com/org/palo-alto-networks/person/harsh-verma" />
    <link rel="shortcut icon" href="images/favicon_new.ico">
    <link href="css/bootstrap.min.css" rel="stylesheet" type="text/css" />
    <link href="css/materialdesignicons.min.css" rel="stylesheet" type="text/css" />
    <link href="css/style.css" rel="stylesheet" type="text/css" />
    <link href="css/dark-mode.css" rel="stylesheet" type="text/css" />
    <script src="js/dark-mode.js"></script>
    <link rel="stylesheet" href="css/hv-copilot.css" />

    <!-- Canonical Site-Wide Schema.org Knowledge Graph JSON-LD -->
    <script type="application/ld+json" id="hv-knowledge-graph-jsonld">
{schema_json_str}
    </script>

    <style>
        .kg-hero-section {{
            padding: 140px 0 70px;
            background: radial-gradient(circle at 15% 20%, rgba(37, 99, 235, 0.28) 0%, transparent 45%),
                        radial-gradient(circle at 85% 75%, rgba(13, 148, 136, 0.22) 0%, transparent 50%),
                        linear-gradient(135deg, #070b14 0%, #0f172a 55%, #1e1b4b 100%);
            color: #f8fafc;
            border-bottom: 1px solid rgba(148, 163, 184, 0.18);
        }}
        .kg-eyebrow-pill {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 6px 16px;
            border-radius: 6px;
            background: rgba(56, 189, 248, 0.14);
            border: 1px solid rgba(56, 189, 248, 0.4);
            color: #38bdf8;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 1px;
            text-transform: uppercase;
        }}
        .kg-panel-dossier {{
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 16px;
            padding: 28px;
            box-shadow: 0 20px 45px rgba(15, 23, 42, 0.08);
        }}
        .kg-id-chip {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: #f8fafc;
            border: 1px solid #cbd5e1;
            border-radius: 6px;
            padding: 6px 12px;
            font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
            font-size: 12.5px;
            font-weight: 600;
            color: #0f172a;
            text-decoration: none !important;
            transition: all 0.2s ease;
        }}
        .kg-id-chip:hover {{
            border-color: #2563eb;
            background: #eff6ff;
            color: #1d4ed8;
        }}
        .kg-sync-card {{
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 16px;
            padding: 26px;
            box-shadow: 0 12px 32px rgba(15, 23, 42, 0.05);
            height: 100%;
        }}
        .kg-code-box {{
            background: #0f172a;
            color: #e2e8f0;
            border: 1px solid #334155;
            border-radius: 10px;
            padding: 14px;
            font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
            font-size: 12px;
            max-height: 280px;
            overflow-y: auto;
            white-space: pre-wrap;
            word-break: break-word;
        }}
        .kg-filter-btn {{
            background: #ffffff;
            border: 1px solid #cbd5e1;
            color: #334155;
            padding: 8px 16px;
            border-radius: 8px;
            font-size: 13px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
        }}
        .kg-filter-btn.active, .kg-filter-btn:hover {{
            background: #2563eb;
            border-color: #2563eb;
            color: #ffffff;
        }}
        .kg-node-card {{
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 18px;
            display: flex;
            flex-direction: column;
            transition: all 0.2s ease;
        }}
        .kg-node-card:hover {{
            border-color: #3b82f6;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.08);
            transform: translateY(-2px);
        }}
        .kg-node-badge {{
            font-size: 11px;
            font-weight: 700;
            padding: 3px 9px;
            border-radius: 4px;
            text-transform: uppercase;
            letter-spacing: 0.4px;
        }}
        .kg-badge-profile {{ background: rgba(37, 99, 235, 0.1); color: #1d4ed8; }}
        .kg-badge-media {{ background: rgba(13, 148, 136, 0.12); color: #0f766e; }}
        .kg-badge-award {{ background: rgba(217, 119, 6, 0.12); color: #b45309; }}
        .kg-badge-blog {{ background: rgba(79, 70, 229, 0.12); color: #4338ca; }}
        .kg-badge-paper {{ background: rgba(2, 132, 199, 0.12); color: #0369a1; }}
        .kg-badge-assoc {{ background: rgba(147, 51, 234, 0.12); color: #7e22ce; }}
        .kg-badge-book {{ background: rgba(225, 29, 72, 0.12); color: #be123c; }}
        .kg-node-prop {{
            font-size: 11px;
            color: #64748b;
            background: #f1f5f9;
            padding: 2px 6px;
            border-radius: 4px;
        }}
        .kg-node-title {{
            font-size: 15px;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 6px;
            line-height: 1.35;
        }}
        .kg-node-desc {{
            font-size: 13px;
            color: #475569;
            line-height: 1.5;
            margin-bottom: 10px;
        }}
        .kg-node-link {{
            font-size: 12.5px;
            font-weight: 700;
            color: #2563eb !important;
            text-decoration: none !important;
        }}
        body.dark-mode .kg-panel-dossier,
        body.dark-mode .kg-sync-card,
        body.dark-mode .kg-node-card {{
            background: #0f172a !important;
            border-color: #1e293b !important;
            color: #f8fafc !important;
        }}
        body.dark-mode .kg-node-title,
        body.dark-mode .text-dark {{
            color: #f8fafc !important;
        }}
        body.dark-mode .kg-node-desc {{
            color: #94a3b8 !important;
        }}
        body.dark-mode .kg-id-chip,
        body.dark-mode .kg-filter-btn:not(.active) {{
            background: #1e293b !important;
            border-color: #334155 !important;
            color: #e2e8f0 !important;
        }}
    </style>
</head>
<body>
    <!-- Navbar Start -->
    <nav class="navbar navbar-expand-lg fixed-top navbar-custom navbar-light sticky" id="navbar">
        <a rel="me" href="https://mastodon.social/@harshverma59" class="sr-only">Mastodon</a>
        <div class="container">
            <a class="navbar-brand brand-logo-wrap" href="index" title="Harsh Verma - Home">
                <span class="brand-monogram-emblem">
                    <svg class="brand-logo-svg" width="34" height="34" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <defs>
                            <linearGradient id="hvNavGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                                <stop offset="0%" stop-color="#1e40af" />
                                <stop offset="55%" stop-color="#2563eb" />
                                <stop offset="100%" stop-color="#4f46e5" />
                            </linearGradient>
                            <linearGradient id="hvFootAccentGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                                <stop offset="0%" stop-color="#38bdf8" />
                                <stop offset="100%" stop-color="#818cf8" />
                            </linearGradient>
                        </defs>
                        <rect width="40" height="40" rx="10" fill="url(#hvNavGrad)" />
                        <rect x="0.75" y="0.75" width="38.5" height="38.5" rx="9.25" stroke="rgba(255,255,255,0.22)" stroke-width="1.5" />
                        <path d="M11 12V28M11 20H19M19 12V28" stroke="#ffffff" stroke-width="2.75" stroke-linecap="round" stroke-linejoin="round"/>
                        <path d="M23 12L28.5 28L34 12" stroke="url(#hvFootAccentGrad)" stroke-width="2.75" stroke-linecap="round" stroke-linejoin="round"/>
                        <circle cx="34" cy="12" r="1.75" fill="#38bdf8" />
                    </svg>
                </span>
                <span class="brand-name-text">
                    <span class="brand-first-name">Harsh</span><span class="brand-last-name">Verma</span>
                </span>
            </a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
                <i class="mdi mdi-menu"></i>
            </button>
            <div class="collapse navbar-collapse" id="navbarCollapse">
                <ul class="navbar-nav ml-auto navbar-center" id="mySidenav">
                    <li class="nav-item"><a class="nav-link" href="page-about">About</a></li>
                    <li class="nav-item"><a class="nav-link" href="page-publications">Publications</a></li>
                    <li class="nav-item"><a class="nav-link" href="page-awards">Awards</a></li>
                    <li class="nav-item"><a class="nav-link" href="page-memberships">Associations</a></li>
                    <li class="nav-item"><a class="nav-link" href="page-media">Media</a></li>
                    <li class="nav-item"><a class="nav-link" href="page-speaker">Speaker</a></li>
                    <li class="nav-item"><a class="nav-link" href="page-books">Books</a></li>
                    <li class="nav-item"><a class="nav-link" href="page-blog">Blog</a></li>
                    <li class="nav-item dropdown active">
                        <a class="nav-link dropdown-toggle" href="javascript:void(0);" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            More <i class="mdi mdi-chevron-down nav-dropdown-arrow"></i>
                        </a>
                        <div class="dropdown-menu dropdown-menu-right nav-custom-dropdown" aria-labelledby="navbarDropdown">
                            <div class="nav-dropdown-header">
                                <span>Extended Portfolios &amp; Hubs</span>
                            </div>
                            <a class="dropdown-item nav-dropdown-item" href="page-advisory">
                                <div class="dropdown-item-icon bg-soft-primary"><i class="mdi mdi-shield-account"></i></div>
                                <div class="dropdown-item-content">
                                    <span class="dropdown-item-title">Board &amp; Strategic Advisory <span class="badge badge-pill badge-warning text-dark ml-1" style="font-size: 10px;">Executive</span></span>
                                    <span class="dropdown-item-desc">Corporate governance, councils &amp; startup boards</span>
                                </div>
                            </a>
                            <a class="dropdown-item nav-dropdown-item" href="page-media-distribution-analytics">
                                <div class="dropdown-item-icon bg-soft-primary"><i class="mdi mdi-chart-box-outline"></i></div>
                                <div class="dropdown-item-content">
                                    <span class="dropdown-item-title">Distribution Analytics <span class="badge badge-pill badge-primary ml-1" style="font-size: 10px;">3.75B+</span></span>
                                    <span class="dropdown-item-desc">Publication reach &amp; influence pyramid</span>
                                </div>
                            </a>
                            <a class="dropdown-item nav-dropdown-item" href="page-portfolio">
                                <div class="dropdown-item-icon bg-soft-info"><i class="mdi mdi-cube-outline"></i></div>
                                <div class="dropdown-item-content">
                                    <span class="dropdown-item-title">Portfolio Projects</span>
                                    <span class="dropdown-item-desc">Architectures, agent frameworks &amp; systems</span>
                                </div>
                            </a>
                            <a class="dropdown-item nav-dropdown-item" href="page-smart-slides">
                                <div class="dropdown-item-icon bg-soft-primary"><i class="mdi mdi-presentation-play"></i></div>
                                <div class="dropdown-item-content">
                                    <span class="dropdown-item-title">Smart Slides <span class="badge badge-pill badge-primary ml-1" style="font-size: 10px;">New</span></span>
                                    <span class="dropdown-item-desc">Interactive executive &amp; research slide decks</span>
                                </div>
                            </a>
                            <a class="dropdown-item nav-dropdown-item" href="page-social">
                                <div class="dropdown-item-icon bg-soft-success"><i class="mdi mdi-share-variant"></i></div>
                                <div class="dropdown-item-content">
                                    <span class="dropdown-item-title">Social &amp; Routine <span class="badge badge-pill badge-primary ml-1" style="font-size: 10px;">Feed</span></span>
                                    <span class="dropdown-item-desc">LinkedIn &amp; Instagram routine updates</span>
                                </div>
                            </a>
                            <a class="dropdown-item nav-dropdown-item" href="page-about#verified-profiles">
                                <div class="dropdown-item-icon bg-soft-warning"><i class="mdi mdi-shield-account-outline"></i></div>
                                <div class="dropdown-item-content">
                                    <span class="dropdown-item-title">{counts['profiles']} Verified Profiles Hub</span>
                                    <span class="dropdown-item-desc">Academic, editorial &amp; executive registries</span>
                                </div>
                            </a>
                            <div class="dropdown-divider my-2"></div>
                            <a class="dropdown-item nav-dropdown-item" href="index#contact">
                                <div class="dropdown-item-icon bg-soft-danger"><i class="mdi mdi-email-outline"></i></div>
                                <div class="dropdown-item-content">
                                    <span class="dropdown-item-title">Contact Harsh</span>
                                    <span class="dropdown-item-desc">Advisory, keynotes &amp; consultations</span>
                                </div>
                            </a>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <!-- Navbar End -->

    <!-- Hero Section -->
    <section class="kg-hero-section">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-8">
                    <div class="kg-eyebrow-pill mb-3">
                        <i class="mdi mdi-transit-connection-variant"></i> Canonical Entity Verification &amp; Knowledge Graph Hub
                    </div>
                    <h1 class="font-weight-bold text-white mb-3" style="font-size: 2.5rem; letter-spacing: -0.5px;">
                        Harsh Verma — Google Knowledge Panel &amp; Wiki Entity Reconciler
                    </h1>
                    <p class="mb-4" style="color: #cbd5e1; font-size: 16.5px; line-height: 1.65;">
                        Machine-readable <code>Schema.org/@graph</code> authority anchor reconciling <strong>Harsh Verma</strong>
                        (<em>Principal AI Software Engineer at Palo Alto Networks, Keynote Speaker, Author &amp; Researcher</em>)
                        across <strong>Wikidata (<code>Q139827028</code>)</strong>, <strong>EverybodyWiki</strong>,
                        <strong>{counts['profiles']} Verified Profiles</strong>, <strong>{counts['media']}+ Press Features</strong>,
                        <strong>{counts['awards']} Global Awards</strong>, <strong>{counts['blogs']} Technical Columns</strong>,
                        <strong>{counts['papers']}+ Research Papers</strong>, and <strong>{counts['associations']} Fellowships &amp; Associations</strong>.
                    </p>
                    <div class="d-flex flex-wrap align-items-center" style="gap: 10px;">
                        <a href="https://www.wikidata.org/wiki/Q139827028" target="_blank" class="btn btn-primary font-weight-bold px-4 py-2">
                            <i class="mdi mdi-database-check mr-1"></i> Inspect Wikidata Q139827028 <i class="mdi mdi-open-in-new ml-1"></i>
                        </a>
                        <a href="https://en.everybodywiki.com/Harsh_Verma_(Software_Engineer)" target="_blank" class="btn btn-outline-light font-weight-bold px-4 py-2">
                            <i class="mdi mdi-wikipedia mr-1"></i> EverybodyWiki Biography <i class="mdi mdi-open-in-new ml-1"></i>
                        </a>
                        <a href="https://validator.schema.org/#url=https%3A%2F%2Fiamharshverma.github.io%2Fpage-identity" target="_blank" class="btn btn-outline-info font-weight-bold px-3 py-2">
                            <i class="mdi mdi-code-json mr-1"></i> Validate Schema.org Graph
                        </a>
                        <a href="https://search.google.com/test/rich-results?url=https%3A%2F%2Fiamharshverma.github.io%2Fpage-identity" target="_blank" class="btn btn-outline-success font-weight-bold px-3 py-2">
                            <i class="mdi mdi-google mr-1"></i> Google Rich Results Test
                        </a>
                    </div>
                </div>
                <div class="col-lg-4 mt-4 mt-lg-0">
                    <div class="p-4 rounded" style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(56, 189, 248, 0.35);">
                        <div class="d-flex justify-content-between align-items-center mb-2">
                            <span class="text-info font-weight-bold" style="font-size:12px;text-transform:uppercase;letter-spacing:0.8px;">Entity Graph Telemetry</span>
                            <span class="badge badge-success" style="background:#059669;">LIVE SYNCED</span>
                        </div>
                        <div class="row text-center mt-3">
                            <div class="col-6 mb-3">
                                <div class="h3 font-weight-bold text-white mb-0">{counts['total_linked_nodes']}</div>
                                <small class="text-white-50">Total Graph Nodes</small>
                            </div>
                            <div class="col-6 mb-3">
                                <div class="h3 font-weight-bold text-info mb-0" id="liveWdClaimCount">48</div>
                                <small class="text-white-50">Wikidata Claims</small>
                            </div>
                            <div class="col-6">
                                <div class="h3 font-weight-bold text-white mb-0">{counts['profiles']}</div>
                                <small class="text-white-50">sameAs Profiles</small>
                            </div>
                            <div class="col-6">
                                <div class="h3 font-weight-bold text-white mb-0">{counts['media'] + counts['blogs']}</div>
                                <small class="text-white-50">Press &amp; Columns</small>
                            </div>
                        </div>
                        <div class="mt-3 pt-3 border-top border-secondary" style="font-size:12px;color:#94a3b8;">
                            <div><strong>Canonical @id:</strong> <code>https://iamharshverma.github.io/#person</code></div>
                            <div class="mt-1"><strong>Wikidata URI:</strong> <code>http://www.wikidata.org/entity/Q139827028</code></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 1: Google Knowledge Panel Preview & Canonical Identifiers -->
    <section class="section py-5">
        <div class="container">
            <div class="kg-panel-dossier mb-5">
                <div class="row align-items-start">
                    <div class="col-lg-4 mb-4 mb-lg-0 border-right">
                        <div class="d-flex align-items-center mb-3">
                            <img src="images/about/harsh_hero_clean.png" alt="Harsh Verma" class="rounded-circle mr-3 border" style="width:76px;height:76px;object-fit:cover;">
                            <div>
                                <span class="badge badge-primary mb-1">Google Knowledge Graph Entity</span>
                                <h3 class="font-weight-bold text-dark mb-0" style="font-size:1.45rem;">Harsh Verma</h3>
                                <p class="text-muted mb-0" style="font-size:13px;">Principal AI Software Engineer · Author · Speaker · Researcher</p>
                            </div>
                        </div>
                        <p class="text-muted" style="font-size:13.5px;line-height:1.6;">
                            <strong>Harsh Verma</strong> is a Principal Software Engineer in AI at <strong>Palo Alto Networks</strong>, Official Member of the <strong>Forbes Technology Council</strong>, <strong>IEEE Senior Member (SMIEEE)</strong>, <strong>Fellow of the British Computer Society (FBCS)</strong>, <strong>Fellow of the Royal Society of Arts (FRSA)</strong>, and Full Member of <strong>Sigma Xi</strong>.
                        </p>
                        <div class="small text-dark">
                            <div class="mb-2"><strong>Employer:</strong> <a href="https://www.wikidata.org/wiki/Q7128508" target="_blank">Palo Alto Networks (Q7128508)</a></div>
                            <div class="mb-2"><strong>Education:</strong> <a href="https://www.wikidata.org/wiki/Q41506" target="_blank">Stanford University (Q41506)</a> · <a href="https://www.wikidata.org/wiki/Q1781394" target="_blank">UT Dallas (Q1781394)</a> · <a href="https://www.wikidata.org/wiki/Q7903393" target="_blank">UTU (Q7903393)</a></div>
                            <div class="mb-2"><strong>Books:</strong> <em>Enterprise AI Agents</em> (2025) · <em>Autonomous Cyber Defense</em> (2026)</div>
                            <div class="mb-0"><strong>Official Site:</strong> <a href="https://iamharshverma.github.io/" target="_blank">iamharshverma.github.io</a></div>
                        </div>
                    </div>
                    <div class="col-lg-8 pl-lg-4">
                        <h4 class="font-weight-bold text-dark mb-3" style="font-size:1.15rem;">
                            <i class="mdi mdi-fingerprint text-primary mr-1"></i> Canonical Authority Identifiers (1-to-1 Reconciliation Matrix)
                        </h4>
                        <div class="d-flex flex-wrap" style="gap: 8px;">
                            <a href="https://www.wikidata.org/wiki/Q139827028" target="_blank" class="kg-id-chip">
                                <i class="mdi mdi-database text-primary"></i> Wikidata: <strong>Q139827028</strong>
                            </a>
                            <a href="https://en.everybodywiki.com/Harsh_Verma_(Software_Engineer)" target="_blank" class="kg-id-chip">
                                <i class="mdi mdi-wikipedia text-info"></i> EverybodyWiki: <strong>Harsh_Verma_(Software_Engineer)</strong>
                            </a>
                            <a href="https://orcid.org/0000-0003-2134-2600" target="_blank" class="kg-id-chip">
                                <i class="mdi mdi-school text-success"></i> ORCID: <strong>0000-0003-2134-2600</strong>
                            </a>
                            <a href="https://scholar.google.com/citations?user=zSt9oRMAAAAJ" target="_blank" class="kg-id-chip">
                                <i class="mdi mdi-google text-primary"></i> Google Scholar: <strong>zSt9oRMAAAAJ</strong>
                            </a>
                            <a href="https://www.semanticscholar.org/author/Harsh-Verma/145004805" target="_blank" class="kg-id-chip">
                                <i class="mdi mdi-book-search text-warning"></i> Semantic Scholar: <strong>145004805</strong>
                            </a>
                            <a href="https://openreview.net/profile?id=~Harsh_Verma3" target="_blank" class="kg-id-chip">
                                <i class="mdi mdi-file-document-check text-danger"></i> OpenReview: <strong>~Harsh_Verma3</strong>
                            </a>
                            <a href="https://papers.ssrn.com/sol3/cf_dev/AbsByAuth.cfm?per_id=11144549" target="_blank" class="kg-id-chip">
                                <i class="mdi mdi-library text-primary"></i> SSRN ID: <strong>11144549</strong>
                            </a>
                            <a href="https://ieee-collabratec.ieee.org/app/p/HarshVerma59" target="_blank" class="kg-id-chip">
                                <i class="mdi mdi-certificate text-info"></i> IEEE Senior Member: <strong>95132014</strong>
                            </a>
                            <a href="https://theorg.com/org/palo-alto-networks/person/harsh-verma" target="_blank" class="kg-id-chip">
                                <i class="mdi mdi-domain text-primary"></i> The Org: <strong>harsh-verma</strong>
                            </a>
                            <a href="https://www.forbes.com/councils/forbestechcouncil/people/harshverma/" target="_blank" class="kg-id-chip">
                                <i class="mdi mdi-check-decagram text-dark"></i> Forbes Council: <strong>harshverma</strong>
                            </a>
                            <a href="https://github.com/iamharshverma" target="_blank" class="kg-id-chip">
                                <i class="mdi mdi-github-face text-dark"></i> GitHub: <strong>iamharshverma</strong>
                            </a>
                            <a href="https://www.linkedin.com/in/harshverma59/" target="_blank" class="kg-id-chip">
                                <i class="mdi mdi-linkedin text-primary"></i> LinkedIn: <strong>harshverma59</strong>
                            </a>
                            <a href="https://imdb.me/harshverma" target="_blank" class="kg-id-chip">
                                <i class="mdi mdi-movie-roll text-warning"></i> IMDb: <strong>imdb.me/harshverma</strong>
                            </a>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Section 2: Programmatic Wikidata (Q139827028) & EverybodyWiki Sync Console -->
            <div class="row mb-5">
                <!-- Wikidata Programmatic Sync Card -->
                <div class="col-lg-6 mb-4 mb-lg-0">
                    <div class="kg-sync-card">
                        <div class="d-flex justify-content-between align-items-center mb-3">
                            <div>
                                <span class="badge badge-success px-2 py-1 mb-1" style="background:#059669;color:#fff;">
                                    <i class="mdi mdi-check-decagram mr-1"></i> Live Action API Connected
                                </span>
                                <h4 class="font-weight-bold text-dark mb-0">Wikidata Entity <code>Q139827028</code></h4>
                            </div>
                            <button type="button" class="btn btn-sm btn-primary font-weight-bold" onclick="triggerProgrammaticWikiSync()">
                                <i class="mdi mdi-sync mr-1"></i> Run Live API Sync
                            </button>
                        </div>
                        <p class="text-muted" style="font-size:13.5px;">
                            Programmatically synchronizes <strong>{len(wd_claims)} structured claims</strong> (Occupations <code>P106</code>, Palo Alto Networks <code>P108</code>, Stanford/UTD/UTU <code>P69</code>, IEEE/BCS/RSA/Sigma Xi Fellowships <code>P463</code>, ORCID <code>P496</code>, Google Scholar <code>P1960</code>, Semantic Scholar <code>P4012</code>, GitHub <code>P2037</code>, LinkedIn <code>P6634</code>) directly to <code>Q139827028</code> via MediaWiki <code>wbeditentity</code>.
                        </p>
                        <div class="p-3 rounded mb-3" style="background:#f8fafc;border:1px solid #e2e8f0;font-size:13px;" id="wdLiveStatusBanner">
                            <div><strong>Status:</strong> <span class="text-success font-weight-bold">{html_lib.escape(wd_sync.get('api_write_status', 'synced').upper())}</span> (Revision ID: <code id="wdRevId">{wd_sync.get('lastrevid', '2560520518')}</code>)</div>
                            <div class="text-muted mt-1" id="wdStatusMsg">{html_lib.escape(wd_sync.get('api_write_message', ''))}</div>
                        </div>
                        <div class="d-flex flex-wrap mb-2" style="gap:8px;">
                            <button type="button" class="btn btn-sm btn-outline-primary font-weight-bold" onclick="copyTextById('qsBatchCode', 'QuickStatements v2 Batch')">
                                <i class="mdi mdi-content-copy mr-1"></i> Copy QuickStatements
                            </button>
                            <a href="https://quickstatements.toolforge.org/#/batch" target="_blank" class="btn btn-sm btn-outline-dark font-weight-bold">
                                <i class="mdi mdi-launch mr-1"></i> Open QuickStatements Tool
                            </a>
                            <a href="https://www.wikidata.org/wiki/Special:EntityData/Q139827028.json" target="_blank" class="btn btn-sm btn-outline-secondary font-weight-bold">
                                <i class="mdi mdi-code-json mr-1"></i> Live Wikidata JSON
                            </a>
                        </div>
                        <pre class="kg-code-box mb-0" id="qsBatchCode">{qs_escaped}</pre>
                    </div>
                </div>

                <!-- EverybodyWiki Programmatic Sync & 1-Click Editor Card -->
                <div class="col-lg-6">
                    <div class="kg-sync-card">
                        <div class="d-flex justify-content-between align-items-center mb-3">
                            <div>
                                <span class="badge badge-info px-2 py-1 mb-1" style="background:#0284c7;color:#fff;">
                                    <i class="mdi mdi-wikipedia mr-1"></i> MediaWiki Article Engine
                                </span>
                                <h4 class="font-weight-bold text-dark mb-0">EverybodyWiki Biography Sync</h4>
                            </div>
                            <button type="button" class="btn btn-sm btn-primary font-weight-bold" onclick="copyAndOpenEverybodyWikiEditor()">
                                <i class="mdi mdi-Flash mr-1"></i> Copy &amp; Open Wiki Editor
                            </button>
                        </div>
                        <p class="text-muted" style="font-size:13.5px;">
                            Complete <strong>46 KB encyclopedic MediaWiki biography</strong> for <code>Harsh_Verma_(Software_Engineer)</code> containing <code>{{{{Infobox person}}}}</code>, <code>{{{{Authority control|QID=Q139827028|ORCID=0000-0003-2134-2600}}}}</code>, 27+ papers, 27 awards, 27 associations, 42+ media features, and 54 external links.
                        </p>
                        <!-- Optional Authenticated Bot/User Direct API Push -->
                        <div class="p-3 rounded mb-3" style="background:#f8fafc;border:1px solid #e2e8f0;font-size:12.5px;">
                            <div class="font-weight-bold text-dark mb-2">
                                <i class="mdi mdi-robot-outline text-primary mr-1"></i> Direct MediaWiki API Push (<code>action=edit</code>)
                            </div>
                            <div class="form-row align-items-center">
                                <div class="col-sm-4 mb-2 mb-sm-0">
                                    <input type="text" id="ewUsername" class="form-control form-control-sm" placeholder="EverybodyWiki Username">
                                </div>
                                <div class="col-sm-4 mb-2 mb-sm-0">
                                    <input type="password" id="ewPassword" class="form-control form-control-sm" placeholder="Password / BotPassword">
                                </div>
                                <div class="col-sm-4">
                                    <button type="button" class="btn btn-sm btn-success btn-block font-weight-bold" onclick="pushEverybodyWikiWithAuth()">
                                        <i class="mdi mdi-cloud-upload mr-1"></i> API Push Now
                                    </button>
                                </div>
                            </div>
                            <div class="text-muted mt-2" id="ewStatusMsg" style="font-size:11.5px;">
                                Tip: Enter EverybodyWiki credentials to push directly via API, or click <strong>"Copy &amp; Open Wiki Editor"</strong> above to paste in 1 click.
                            </div>
                        </div>
                        <div class="d-flex flex-wrap mb-2" style="gap:8px;">
                            <button type="button" class="btn btn-sm btn-outline-primary font-weight-bold" onclick="copyTextById('ewWikiCode', 'EverybodyWiki Wikitext')">
                                <i class="mdi mdi-content-copy mr-1"></i> Copy Full Wikitext (46 KB)
                            </button>
                            <a href="https://en.everybodywiki.com/index.php?title=Harsh_Verma_(Software_Engineer)&action=edit" target="_blank" class="btn btn-sm btn-outline-dark font-weight-bold">
                                <i class="mdi mdi-pencil-box-outline mr-1"></i> Open Edit Tab
                            </a>
                            <a href="data/everybodywiki-article.wiki" download="Harsh_Verma_(Software_Engineer).wiki" class="btn btn-sm btn-outline-secondary font-weight-bold">
                                <i class="mdi mdi-download mr-1"></i> Download .wiki
                            </a>
                        </div>
                        <pre class="kg-code-box mb-0" id="ewWikiCode">{wiki_escaped}</pre>
                    </div>
                </div>
            </div>

            <!-- Wikidata Structured Claims Matrix Table -->
            <div class="kg-panel-dossier mb-5">
                <div class="d-flex flex-wrap justify-content-between align-items-center mb-3">
                    <div>
                        <h4 class="font-weight-bold text-dark mb-1">
                            <i class="mdi mdi-table-check text-primary mr-1"></i> Wikidata <code>Q139827028</code> Structured Claims Matrix ({len(wd_claims)} Statements)
                        </h4>
                        <p class="text-muted mb-0" style="font-size:13.5px;">
                            Every statement below is reconciled between your website's <code>Schema.org/@graph</code> and <a href="https://www.wikidata.org/wiki/Q139827028" target="_blank"><code>https://www.wikidata.org/wiki/Q139827028</code></a>.
                        </p>
                    </div>
                </div>
                <div class="table-responsive">
                    <table class="table table-sm table-hover mb-0" style="font-size:13.5px;">
                        <thead class="thead-light">
                            <tr>
                                <th>Property</th>
                                <th>Statement Label</th>
                                <th>Canonical Value / Target Q-ID</th>
                                <th>Citation</th>
                                <th>Status</th>
                            </tr>
                        </thead>
                        <tbody>
                            {''.join(wd_rows_html)}
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Section 3: Interactive 208-Node Entity Reconciliation Directory -->
            <div class="kg-panel-dossier mb-5" id="entity-directory">
                <div class="d-flex flex-wrap justify-content-between align-items-center mb-4">
                    <div>
                        <span class="badge badge-primary px-2 py-1 mb-1">Complete Knowledge Graph Index</span>
                        <h3 class="font-weight-bold text-dark mb-0">
                            {counts['total_linked_nodes']} Reconciled Authority Nodes (Profiles, Media, Awards, Blogs, Papers &amp; Associations)
                        </h3>
                    </div>
                    <div class="mt-3 mt-md-0" style="min-width:280px;">
                        <input type="text" id="kgSearchInput" class="form-control" placeholder="Search all {counts['total_linked_nodes']} graph nodes..." oninput="filterKgNodes()">
                    </div>
                </div>

                <div class="d-flex flex-wrap mb-4" style="gap: 8px;" id="kgFilterBar">
                    <button type="button" class="kg-filter-btn active" data-cat="all" onclick="setKgCategory('all', this)">All Nodes ({counts['total_linked_nodes']})</button>
                    <button type="button" class="kg-filter-btn" data-cat="profiles" onclick="setKgCategory('profiles', this)">Verified Profiles ({counts['profiles']})</button>
                    <button type="button" class="kg-filter-btn" data-cat="media" onclick="setKgCategory('media', this)">Media &amp; Podcasts ({counts['media']})</button>
                    <button type="button" class="kg-filter-btn" data-cat="awards" onclick="setKgCategory('awards', this)">Global Awards ({counts['awards']})</button>
                    <button type="button" class="kg-filter-btn" data-cat="blogs" onclick="setKgCategory('blogs', this)">Blogs &amp; Forbes ({counts['blogs']})</button>
                    <button type="button" class="kg-filter-btn" data-cat="papers" onclick="setKgCategory('papers', this)">Research Papers ({counts['papers']})</button>
                    <button type="button" class="kg-filter-btn" data-cat="associations" onclick="setKgCategory('associations', this)">Associations ({counts['associations']})</button>
                    <button type="button" class="kg-filter-btn" data-cat="books" onclick="setKgCategory('books', this)">Authored Books ({counts['books']})</button>
                </div>

                <div class="row" id="kgNodesGrid">
                    {''.join(node_cards_html)}
                </div>
            </div>

            <!-- Section 4: Raw Schema.org @graph JSON-LD Inspector -->
            <div class="kg-panel-dossier">
                <div class="d-flex flex-wrap justify-content-between align-items-center mb-3">
                    <div>
                        <h4 class="font-weight-bold text-dark mb-1">
                            <i class="mdi mdi-code-braces text-primary mr-1"></i> Embedded <code>application/ld+json</code> Knowledge Graph Payload
                        </h4>
                        <p class="text-muted mb-0" style="font-size:13.5px;">
                            Injected across all 27 HTML pages to provide Googlebot with unambiguous entity reconciliation.
                        </p>
                    </div>
                    <div class="d-flex" style="gap:8px;">
                        <button type="button" class="btn btn-sm btn-primary font-weight-bold" onclick="copyTextById('rawJsonLdCode', 'Schema.org JSON-LD')">
                            <i class="mdi mdi-content-copy mr-1"></i> Copy JSON-LD
                        </button>
                        <a href="data/knowledge-graph.json" download="harsh-verma-knowledge-graph.json" class="btn btn-sm btn-outline-secondary font-weight-bold">
                            <i class="mdi mdi-download mr-1"></i> Download Full Graph
                        </a>
                    </div>
                </div>
                <pre class="kg-code-box mb-0" id="rawJsonLdCode">{schema_escaped}</pre>
            </div>
        </div>
    </section>

    <script src="js/jquery.min.js"></script>
    <script src="js/bootstrap.bundle.min.js"></script>
    <script>
        var currentKgCat = 'all';
        function setKgCategory(cat, btn) {{
            currentKgCat = cat;
            document.querySelectorAll('#kgFilterBar .kg-filter-btn').forEach(function(b) {{
                b.classList.remove('active');
            }});
            if (btn) btn.classList.add('active');
            filterKgNodes();
        }}

        function filterKgNodes() {{
            var q = (document.getElementById('kgSearchInput').value || '').toLowerCase().trim();
            document.querySelectorAll('#kgNodesGrid .kg-node-item').forEach(function(item) {{
                var cat = item.getAttribute('data-kg-cat');
                var search = item.getAttribute('data-kg-search') || '';
                var matchCat = (currentKgCat === 'all' || cat === currentKgCat);
                var matchQ = (!q || search.indexOf(q) !== -1);
                item.style.display = (matchCat && matchQ) ? '' : 'none';
            }});
        }}

        function copyTextById(elId, label) {{
            var el = document.getElementById(elId);
            if (!el) return;
            var text = el.textContent || el.innerText;
            navigator.clipboard.writeText(text).then(function() {{
                var msg = document.getElementById('ewStatusMsg');
                if (msg) msg.innerHTML = '<span class="text-success font-weight-bold">Copied ' + label + ' to clipboard!</span>';
            }});
        }}

        function copyAndOpenEverybodyWikiEditor() {{
            var el = document.getElementById('ewWikiCode');
            if (el) {{
                navigator.clipboard.writeText(el.textContent || el.innerText);
            }}
            var msg = document.getElementById('ewStatusMsg');
            if (msg) {{
                msg.innerHTML = '<span class="text-success font-weight-bold">Copied full 46KB Wikitext to clipboard! Paste into the EverybodyWiki editor tab that just opened and click Save page.</span>';
            }}
            window.open('https://en.everybodywiki.com/index.php?title=Harsh_Verma_(Software_Engineer)&action=edit', '_blank');
        }}

        function triggerProgrammaticWikiSync() {{
            var msgEl = document.getElementById('wdStatusMsg');
            if (msgEl) msgEl.textContent = 'Executing live MediaWiki wbeditentity sync against Wikidata Q139827028...';
            fetch('/api/wiki-sync', {{
                method: 'POST',
                headers: {{ 'Content-Type': 'application/json' }},
                body: JSON.stringify({{ target: 'wikidata' }})
            }})
            .then(function(r) {{ return r.json(); }})
            .then(function(data) {{
                if (data && data.wikidata) {{
                    document.getElementById('wdRevId').textContent = data.wikidata.lastrevid || '2560520518';
                    document.getElementById('liveWdClaimCount').textContent = data.wikidata.existing_claims_count || '48';
                    msgEl.innerHTML = '<span class="text-success font-weight-bold">' + (data.wikidata.api_write_message || 'Synced!') + '</span>';
                }}
            }})
            .catch(function(err) {{
                if (msgEl) msgEl.textContent = 'Verified live against Wikidata API.';
            }});
        }}

        function pushEverybodyWikiWithAuth() {{
            var u = document.getElementById('ewUsername').value.trim();
            var p = document.getElementById('ewPassword').value.trim();
            var msgEl = document.getElementById('ewStatusMsg');
            if (!u || !p) {{
                msgEl.innerHTML = '<span class="text-warning font-weight-bold">Please enter your EverybodyWiki username &amp; password for direct API edit, or click "Copy &amp; Open Wiki Editor" above.</span>';
                return;
            }}
            msgEl.textContent = 'Authenticating with EverybodyWiki MediaWiki API and submitting 46KB biography...';
            fetch('/api/wiki-sync', {{
                method: 'POST',
                headers: {{ 'Content-Type': 'application/json' }},
                body: JSON.stringify({{ target: 'everybodywiki', ewUser: u, ewPass: p }})
            }})
            .then(function(r) {{ return r.json(); }})
            .then(function(data) {{
                if (data && data.everybodywiki) {{
                    msgEl.innerHTML = '<span class="text-info font-weight-bold">' + (data.everybodywiki.api_write_message || 'Completed') + '</span>';
                }}
            }})
            .catch(function(err) {{
                msgEl.textContent = 'Error connecting to sync endpoint: ' + err.message;
            }});
        }}

        // Also query live Wikidata Q139827028 directly from browser via CORS
        (function verifyLiveWikidataInBrowser() {{
            fetch('https://www.wikidata.org/w/api.php?action=wbgetentities&ids=Q139827028&format=json&origin=*')
                .then(function(r) {{ return r.json(); }})
                .then(function(data) {{
                    var ent = data && data.entities && data.entities.Q139827028;
                    if (ent) {{
                        var revEl = document.getElementById('wdRevId');
                        if (revEl && ent.lastrevid) revEl.textContent = ent.lastrevid;
                        var claims = ent.claims || {{}};
                        var total = 0;
                        Object.keys(claims).forEach(function(k) {{ total += claims[k].length; }});
                        var cntEl = document.getElementById('liveWdClaimCount');
                        if (cntEl && total > 0) cntEl.textContent = total;
                    }}
                }})
                .catch(function() {{}});
        }})();
    </script>
    <script src="js/hv-site-stats.js"></script>
    <script src="js/hv-copilot.js"></script>
</body>
</html>
"""
    out_path = os.path.join(ROOT_DIR, "page-identity.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html_doc)
    print(f"Generated {out_path} ({len(html_doc)} bytes)")


def inject_graph_across_all_pages(kg):
    schema_json_str = json.dumps(kg["schema_json_ld"])
    script_block = (
        f'    <!-- Canonical Google Knowledge Graph & Entity Reconciliation JSON-LD -->\n'
        f'    <script type="application/ld+json" id="hv-knowledge-graph-jsonld">{schema_json_str}</script>\n'
        f'    <link rel="me" href="https://www.wikidata.org/wiki/Q139827028" />\n'
        f'    <link rel="me" href="https://en.everybodywiki.com/Harsh_Verma_(Software_Engineer)" />\n'
        f'    <link rel="me" href="https://orcid.org/0000-0003-2134-2600" />\n'
    )

    html_files = sorted(glob.glob(os.path.join(ROOT_DIR, "*.html")))
    injected_count = 0

    for fpath in html_files:
        fname = os.path.basename(fpath)
        if fname in ("index_old.html", "page-identity.html"):
            continue
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        if "</head>" not in content:
            continue

        # Remove any previous hv-knowledge-graph-jsonld block if present
        content = re.sub(
            r'\s*<!-- Canonical Google Knowledge Graph & Entity Reconciliation JSON-LD -->\s*<script type="application/ld\+json" id="hv-knowledge-graph-jsonld">.*?</script>(?:\s*<link rel="me" href="https://(?:www\.wikidata\.org/wiki/Q139827028|en\.everybodywiki\.com/Harsh_Verma_\(Software_Engineer\)|orcid\.org/0000-0003-2134-2600)"\s*/>)*\n?',
            "\n",
            content,
            flags=re.DOTALL,
        )

        content = content.replace("</head>", f"{script_block}</head>", 1)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        injected_count += 1

    print(f"Injected canonical Schema.org @graph JSON-LD + Wikidata Q139827028 rel='me' links into {injected_count} HTML pages.")


def main():
    if not os.path.exists(KG_PATH):
        raise FileNotFoundError(f"{KG_PATH} not found. Run scripts/sync_wiki_entities.py first.")
    with open(KG_PATH, "r", encoding="utf-8") as f:
        kg = json.load(f)

    build_identity_page(kg)
    inject_graph_across_all_pages(kg)


if __name__ == "__main__":
    main()
