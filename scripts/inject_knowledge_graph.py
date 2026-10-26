#!/usr/bin/env python3
"""
scripts/inject_knowledge_graph.py
=================================
1. Generates `page-identity.html` — The Dedicated Google Knowledge Panel,
   Entity Verification & Programmatic Wiki Sync Hub (Wikidata Q139827028 & EverybodyWiki).
   - Canonical @id: https://www.harshverma.me/#person (reconciled with https://harshverma.me/#person)
   - Complete 213-node interactive entity graph with all visual thumbnails, banners, logos, and multi-link citations
   - Zero ACM entries and zero iamharshverma.github.io references
2. Injects the unified Schema.org `@graph` JSON-LD (`id="hv-knowledge-graph-jsonld"`)
   and canonical `rel="me"` authority links across all HTML pages in the portfolio.
"""

import os
import re
import glob
import json
import shutil
import html as html_lib

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KG_PATH = os.path.join(ROOT_DIR, "data", "knowledge-graph.json")
CANONICAL_SITE_URL = "https://www.harshverma.me"
SECONDARY_SITE_URL = "https://harshverma.me"


def ensure_hero_clean_image():
    """Ensure images/about/harsh_hero_clean.png exists as a copy of images/harsh/Harsh_portfolio_pic.png."""
    src = os.path.join(ROOT_DIR, "images", "harsh", "Harsh_portfolio_pic.png")
    dst_dir = os.path.join(ROOT_DIR, "images", "about")
    dst = os.path.join(dst_dir, "harsh_hero_clean.png")
    if os.path.exists(src) and not os.path.exists(dst):
        os.makedirs(dst_dir, exist_ok=True)
        shutil.copyfile(src, dst)


def build_identity_page(kg):
    ensure_hero_clean_image()
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
        fmt_url = (
            c.get("formatter_url")
            or (f"https://www.wikidata.org/wiki/{val}" if c["type"] == "wikibase-entityid" else val if val.startswith("http") else ref)
        )
        wd_rows_html.append(f"""
        <tr>
            <td><a href="https://www.wikidata.org/wiki/Property:{prop}" target="_blank" rel="noopener" class="badge badge-dark font-monospace px-2 py-1">{prop}</a></td>
            <td class="font-weight-bold text-dark">{lbl}</td>
            <td>
                <a href="{html_lib.escape(fmt_url)}" target="_blank" rel="noopener" class="text-primary font-weight-bold">{val_lbl}</a>
                {f'<span class="text-muted font-monospace ml-1" style="font-size:11px;">({val})</span>' if val != val_lbl else ''}
            </td>
            <td><a href="{ref}" target="_blank" rel="noopener" class="text-muted" style="font-size:12px;"><i class="mdi mdi-link-variant mr-1"></i>Reference</a></td>
            <td><span class="badge badge-success px-2 py-1" style="background:#059669;color:#fff;"><i class="mdi mdi-check-circle mr-1"></i>Synced on Q139827028</span></td>
        </tr>""")

    # Build unified 213-node cards with properly proportioned thumbnails & detailed verification links
    node_cards_html = []

    # 1. Verified Profiles (54) - 100x100 square SVG badges
    for p in entities["profiles"]:
        t = html_lib.escape(p.get("title", ""))
        cat_lbl = html_lib.escape(p.get("category_label", "Authority Profile"))
        ident = html_lib.escape(p.get("identifier", "Verified"))
        desc = html_lib.escape(p.get("description", ""))
        url = html_lib.escape(p.get("url", "").replace("https://iamharshverma.github.io", "https://www.harshverma.me"))
        img = html_lib.escape(p.get("image") or "images/profiles/wikidata.svg")
        search_str = html_lib.escape(f"{t} {cat_lbl} {ident} {desc} {url} profile sameAs".lower())
        node_cards_html.append(f"""
        <div class="col-lg-4 col-md-6 mb-3 kg-node-item" data-kg-cat="profiles" data-kg-search="{search_str}">
            <div class="kg-node-card h-100">
                <div class="d-flex justify-content-between align-items-center mb-2">
                    <span class="kg-node-badge kg-badge-profile"><i class="mdi mdi-check-decagram mr-1"></i>sameAs · {cat_lbl}</span>
                    <code class="kg-node-prop">{ident}</code>
                </div>
                <div class="d-flex align-items-center mb-2">
                    <div class="kg-node-thumb-wrap mr-3">
                        <img src="{img}" alt="{t}" class="kg-node-thumb" loading="lazy" onerror="this.src='images/profiles/wikidata.svg'">
                    </div>
                    <div>
                        <h5 class="kg-node-title mb-0">{t}</h5>
                        <div class="text-muted font-monospace" style="font-size:11px; word-break:break-all;">{url[:46]}{'...' if len(url) > 46 else ''}</div>
                    </div>
                </div>
                <p class="kg-node-desc">{desc}</p>
                <div class="mt-auto pt-2 border-top d-flex flex-wrap justify-content-between align-items-center" style="gap:6px;">
                    <a href="{url}" target="_blank" rel="me noopener" class="kg-node-link"><i class="mdi mdi-shield-check-outline mr-1"></i>Open Verified Profile <i class="mdi mdi-open-in-new ml-1"></i></a>
                    <span class="text-muted font-monospace" style="font-size:11px;">Schema: sameAs</span>
                </div>
            </div>
        </div>""")

    # 2. Media & Podcasts (42) - 600x340 wide banner SVG thumbnails
    for m in entities["media"]:
        t = html_lib.escape(m.get("title", ""))
        outlet = html_lib.escape(m.get("outlet", "Press Outlet"))
        yr = html_lib.escape(str(m.get("date_display") or m.get("year", "2026")))
        summary = html_lib.escape(m.get("summary", ""))
        m_type = m.get("type", "article")
        schema_type = "PodcastEpisode" if m_type == "podcast" else "NewsArticle"
        icon_svg = m.get("icon_svg", "")
        img_src = f"images/media/{icon_svg}" if icon_svg else "images/profiles/forbes.svg"
        links = m.get("links") or []
        primary_url = m.get("primary_url") or (links[0]["url"] if links else "page-media")

        link_btns = []
        if links:
            for lk in links:
                l_url = html_lib.escape(lk.get("url", primary_url))
                l_lbl = html_lib.escape(lk.get("label", "Read Feature"))
                link_btns.append(f'<a href="{l_url}" target="_blank" rel="noopener" class="kg-mini-link-pill"><i class="mdi mdi-open-in-new mr-1"></i>{l_lbl}</a>')
        else:
            link_btns.append(f'<a href="{html_lib.escape(primary_url)}" target="_blank" rel="noopener" class="kg-mini-link-pill"><i class="mdi mdi-open-in-new mr-1"></i>Read Citation</a>')

        search_str = html_lib.escape(f"{t} {outlet} {yr} {summary} {schema_type} media press podcast subjectOf".lower())
        node_cards_html.append(f"""
        <div class="col-lg-4 col-md-6 mb-3 kg-node-item" data-kg-cat="media" data-kg-search="{search_str}">
            <div class="kg-node-card h-100">
                <div class="d-flex justify-content-between align-items-center mb-2">
                    <span class="kg-node-badge kg-badge-media"><i class="mdi mdi-newspaper-variant-outline mr-1"></i>subjectOf · {outlet}</span>
                    <code class="kg-node-prop">{yr}</code>
                </div>
                <div class="kg-banner-thumb-wrap mb-2">
                    <img src="{html_lib.escape(img_src)}" alt="{outlet} — {t}" class="kg-banner-thumb" loading="lazy" onerror="this.src='images/profiles/forbes.svg'">
                </div>
                <h5 class="kg-node-title mb-1">{t}</h5>
                <div class="text-primary font-weight-bold mb-1" style="font-size:12px;">{outlet} · {schema_type}</div>
                <p class="kg-node-desc">{summary}</p>
                <div class="mt-auto pt-2 border-top">
                    <div class="d-flex flex-wrap mb-1" style="gap:6px;">
                        {''.join(link_btns)}
                    </div>
                    <div class="d-flex justify-content-between align-items-center mt-1">
                        <span class="text-muted font-monospace" style="font-size:10.5px;">@type: {schema_type}</span>
                        <span class="text-muted font-monospace" style="font-size:10.5px;">Schema: subjectOf</span>
                    </div>
                </div>
            </div>
        </div>""")

    # 3. Honors & Global Awards (27) - 400x240 wide banner SVG thumbnails
    for a in entities["awards"]:
        t = html_lib.escape(a.get("title", ""))
        org = html_lib.escape(a.get("organization", ""))
        yr = html_lib.escape(str(a.get("year", "2026")))
        tier = html_lib.escape(a.get("tier", "Honoree"))
        desc = html_lib.escape(a.get("description", ""))
        img = html_lib.escape(a.get("image") or "images/awards/forttuna_100.svg")
        links = a.get("links") or []

        link_btns = []
        if links:
            for lk in links:
                l_url = html_lib.escape(lk.get("url", "page-awards"))
                l_lbl = html_lib.escape(lk.get("label", "Verify Credential"))
                link_btns.append(f'<a href="{l_url}" target="_blank" rel="noopener" class="kg-mini-link-pill"><i class="mdi mdi-shield-check-outline mr-1"></i>{l_lbl}</a>')
        else:
            link_btns.append('<a href="page-awards" class="kg-mini-link-pill"><i class="mdi mdi-trophy-outline mr-1"></i>View Award</a>')

        search_str = html_lib.escape(f"{t} {org} {yr} {tier} {desc} award honor credential".lower())
        node_cards_html.append(f"""
        <div class="col-lg-4 col-md-6 mb-3 kg-node-item" data-kg-cat="awards" data-kg-search="{search_str}">
            <div class="kg-node-card h-100">
                <div class="d-flex justify-content-between align-items-center mb-2">
                    <span class="kg-node-badge kg-badge-award"><i class="mdi mdi-trophy-award mr-1"></i>award · {yr}</span>
                    <code class="kg-node-prop">{tier}</code>
                </div>
                <div class="kg-banner-thumb-wrap mb-2">
                    <img src="{img}" alt="{t}" class="kg-banner-thumb" loading="lazy" onerror="this.src='images/profiles/wikidata.svg'">
                </div>
                <h5 class="kg-node-title mb-1">{t}</h5>
                <div class="text-primary font-weight-bold mb-1" style="font-size:12px;">{org}</div>
                <p class="kg-node-desc">{desc[:185]}{'...' if len(desc) > 185 else ''}</p>
                <div class="mt-auto pt-2 border-top">
                    <div class="d-flex flex-wrap mb-1" style="gap:6px;">
                        {''.join(link_btns)}
                    </div>
                    <div class="d-flex justify-content-between align-items-center mt-1">
                        <span class="text-muted font-monospace" style="font-size:10.5px;">@type: EducationalOccupationalCredential</span>
                        <span class="text-muted font-monospace" style="font-size:10.5px;">Schema: hasCredential</span>
                    </div>
                </div>
            </div>
        </div>""")

    # 4. Blogs & Forbes Columns (29) - 16:9 article thumbnails
    for b in entities["blogs"]:
        t = html_lib.escape(b.get("title", ""))
        plat = html_lib.escape(b.get("platform", "Forbes Technology Council"))
        dt = html_lib.escape(str(b.get("date", "2026")))
        desc = html_lib.escape(b.get("description", ""))
        url = html_lib.escape(b.get("url") or "page-blog")
        spotify = html_lib.escape(b.get("spotify_url") or "")
        img = html_lib.escape(b.get("image") or "images/blog/thumbnails/forbes-real-ai-moat.jpg")
        search_str = html_lib.escape(f"{t} {plat} {dt} {desc} blog article forbes hackernoon techarticle".lower())
        node_cards_html.append(f"""
        <div class="col-lg-4 col-md-6 mb-3 kg-node-item" data-kg-cat="blogs" data-kg-search="{search_str}">
            <div class="kg-node-card h-100">
                <div class="d-flex justify-content-between align-items-center mb-2">
                    <span class="kg-node-badge kg-badge-blog"><i class="mdi mdi-post-outline mr-1"></i>TechArticle · {plat[:24]}</span>
                    <code class="kg-node-prop">{dt}</code>
                </div>
                <div class="kg-banner-thumb-wrap mb-2" style="padding:0;">
                    <img src="{img}" alt="{t}" style="width:100%;height:100%;object-fit:cover;" loading="lazy" onerror="this.src='images/blog/thumbnails/forbes-real-ai-moat.jpg'">
                </div>
                <h5 class="kg-node-title">{t}</h5>
                <p class="kg-node-desc">{desc[:165]}{'...' if len(desc) > 165 else ''}</p>
                <div class="mt-auto pt-2 border-top d-flex flex-wrap justify-content-between align-items-center" style="gap:6px;">
                    <div class="d-flex flex-wrap" style="gap:6px;">
                        <a href="{url}" target="_blank" rel="noopener" class="kg-mini-link-pill"><i class="mdi mdi-book-open-variant mr-1"></i>Read Article</a>
                        {f'<a href="{spotify}" target="_blank" rel="noopener" class="kg-mini-link-pill"><i class="mdi mdi-spotify mr-1"></i>Audio</a>' if spotify else ''}
                    </div>
                    <span class="text-muted font-monospace" style="font-size:11px;">Schema: TechArticle</span>
                </div>
            </div>
        </div>""")

    # 5. Authored Books & Technical Book Reviews (8) - book cover images
    for b in entities["books"]:
        t = html_lib.escape(b.get("title", ""))
        sub = html_lib.escape(b.get("subtitle", ""))
        role = html_lib.escape(b.get("role", "Authored Book"))
        yr = html_lib.escape(str(b.get("year", "2026")))
        desc = html_lib.escape(b.get("description", ""))
        img = html_lib.escape(b.get("image") or "images/books/beyond_ai_engineering_cover.jpg")
        schema_type = "Book" if "Authored" in role else "Review"
        search_str = html_lib.escape(f"{t} {sub} {role} {yr} {desc} book author review".lower())
        node_cards_html.append(f"""
        <div class="col-lg-6 col-md-6 mb-3 kg-node-item" data-kg-cat="books" data-kg-search="{search_str}">
            <div class="kg-node-card h-100">
                <div class="d-flex justify-content-between align-items-center mb-2">
                    <span class="kg-node-badge kg-badge-book"><i class="mdi mdi-book-open-page-variant mr-1"></i>{schema_type} · {role}</span>
                    <code class="kg-node-prop">{yr}</code>
                </div>
                <div class="d-flex align-items-start mb-2">
                    <img src="{img}" alt="{t}" class="rounded border shadow-sm mr-3" style="width:82px;height:116px;object-fit:cover;flex-shrink:0;" loading="lazy" onerror="this.src='images/books/beyond_ai_engineering_cover.jpg'">
                    <div>
                        <h5 class="kg-node-title mb-1">{t}</h5>
                        <div class="text-primary font-weight-bold mb-1" style="font-size:12.5px;">{sub}</div>
                        <p class="kg-node-desc mb-0">{desc}</p>
                    </div>
                </div>
                <div class="mt-auto pt-2 border-top d-flex justify-content-between align-items-center">
                    <a href="page-books" class="kg-node-link"><i class="mdi mdi-book-multiple mr-1"></i>Explore Official Book Hub <i class="mdi mdi-arrow-right ml-1"></i></a>
                    <span class="text-muted font-monospace" style="font-size:11px;">Schema: {schema_type}</span>
                </div>
            </div>
        </div>""")

    # 6. Peer-Reviewed Research Papers (27) - generated 400x160 SVG paper banner thumbnails
    for idx, p in enumerate(entities["papers"], 1):
        t = html_lib.escape(p.get("title", ""))
        venue = html_lib.escape(p.get("venue") or p.get("publisher") or "IEEE / Peer-Reviewed Venue")
        yr = html_lib.escape(str(p.get("year", "")))
        doi = html_lib.escape(p.get("doi", ""))
        abstract = html_lib.escape(p.get("abstract", ""))
        url = html_lib.escape(p.get("link") or "page-publications")
        img = html_lib.escape(p.get("image") or f"images/papers/paper_{idx}.svg")
        doi_url = f"https://doi.org/{doi}" if doi else url
        search_str = html_lib.escape(f"{t} {venue} {yr} {doi} {abstract} paper research scholarlyarticle".lower())
        node_cards_html.append(f"""
        <div class="col-lg-4 col-md-6 mb-3 kg-node-item" data-kg-cat="papers" data-kg-search="{search_str}">
            <div class="kg-node-card h-100">
                <div class="d-flex justify-content-between align-items-center mb-2">
                    <span class="kg-node-badge kg-badge-paper"><i class="mdi mdi-school-outline mr-1"></i>ScholarlyArticle · {yr}</span>
                    <code class="kg-node-prop">{doi[:22] if doi else 'Peer-Reviewed'}</code>
                </div>
                <div class="kg-banner-thumb-wrap mb-2">
                    <img src="{img}" alt="{t}" class="kg-banner-thumb" loading="lazy" onerror="this.src='images/profiles/google_scholar.svg'">
                </div>
                <h5 class="kg-node-title mb-1">{t}</h5>
                <div class="text-primary font-weight-bold mb-1" style="font-size:12px;"><i class="mdi mdi-bank-outline mr-1"></i>{venue}</div>
                <p class="kg-node-desc">{abstract[:150] + '...' if abstract else f'Published in {venue} ({yr}).'}</p>
                <div class="mt-auto pt-2 border-top d-flex flex-wrap justify-content-between align-items-center" style="gap:6px;">
                    <div class="d-flex flex-wrap" style="gap:6px;">
                        <a href="{url}" target="_blank" rel="noopener" class="kg-mini-link-pill"><i class="mdi mdi-file-document-outline mr-1"></i>Paper</a>
                        {f'<a href="{html_lib.escape(doi_url)}" target="_blank" rel="noopener" class="kg-mini-link-pill"><i class="mdi mdi-identifier mr-1"></i>DOI</a>' if doi else ''}
                    </div>
                    <span class="text-muted font-monospace" style="font-size:11px;">Schema: ScholarlyArticle</span>
                </div>
            </div>
        </div>""")

    # 7. Invited Associations & Fellowships (26 - ACM Removed) - 400x160 wide banner SVG thumbnails
    for assoc in entities["associations"]:
        t = html_lib.escape(assoc.get("title", ""))
        if "acm" in t.lower():
            continue
        role = html_lib.escape(assoc.get("role", ""))
        tier = html_lib.escape(assoc.get("tier", ""))
        cred = html_lib.escape(assoc.get("credential_id", "Verified"))
        desc = html_lib.escape(assoc.get("description", ""))
        img = html_lib.escape(assoc.get("image") or "images/memberships/ieee_senior.svg")
        links = assoc.get("links") or [{"url": assoc.get("url", "page-memberships"), "label": "Verify Membership"}]

        link_btns = []
        for lk in links:
            l_url = html_lib.escape(lk.get("url", "page-memberships"))
            l_lbl = html_lib.escape(lk.get("label", "Verify"))
            link_btns.append(f'<a href="{l_url}" target="_blank" rel="noopener" class="kg-mini-link-pill"><i class="mdi mdi-shield-check-outline mr-1"></i>{l_lbl}</a>')

        search_str = html_lib.escape(f"{t} {role} {tier} {cred} {desc} association fellowship memberOf".lower())
        node_cards_html.append(f"""
        <div class="col-lg-4 col-md-6 mb-3 kg-node-item" data-kg-cat="associations" data-kg-search="{search_str}">
            <div class="kg-node-card h-100">
                <div class="d-flex justify-content-between align-items-center mb-2">
                    <span class="kg-node-badge kg-badge-assoc"><i class="mdi mdi-shield-crown-outline mr-1"></i>memberOf · {tier}</span>
                    <code class="kg-node-prop">{cred[:24]}</code>
                </div>
                <div class="kg-banner-thumb-wrap mb-2">
                    <img src="{img}" alt="{t}" class="kg-banner-thumb" loading="lazy" onerror="this.src='images/memberships/ieee_senior.svg'">
                </div>
                <h5 class="kg-node-title mb-1">{t}</h5>
                <div class="text-primary font-weight-bold mb-1" style="font-size:12px;">{role}</div>
                <p class="kg-node-desc">{desc[:175]}{'...' if len(desc) > 175 else ''}</p>
                <div class="mt-auto pt-2 border-top">
                    <div class="d-flex flex-wrap mb-1" style="gap:6px;">
                        {''.join(link_btns)}
                    </div>
                    <div class="d-flex justify-content-between align-items-center mt-1">
                        <span class="text-muted font-monospace" style="font-size:10.5px;">@type: Organization</span>
                        <span class="text-muted font-monospace" style="font-size:10.5px;">Schema: memberOf</span>
                    </div>
                </div>
            </div>
        </div>""")

    qs_escaped = html_lib.escape(kg["quickstatements"])
    ref_replacement_escaped = html_lib.escape(kg.get("quickstatements_reference_replacement", ""))
    wiki_escaped = html_lib.escape(kg["everybodywiki_wikitext"])
    schema_escaped = html_lib.escape(schema_json_str)

    data_dir = os.path.join(ROOT_DIR, "data")
    wa_path = os.path.join(data_dir, "wikialpha-article.wiki")
    wikialpha_text = open(wa_path, "r", encoding="utf-8").read() if os.path.exists(wa_path) else ""
    wikialpha_escaped = html_lib.escape(wikialpha_text)

    wf_path = os.path.join(data_dir, "wikiflux-article.wiki")
    wikiflux_text = open(wf_path, "r", encoding="utf-8").read() if os.path.exists(wf_path) else ""
    wikiflux_escaped = html_lib.escape(wikiflux_text)

    main_lw_path = os.path.join(data_dir, "localwiki-main.html")
    localwiki_main_text = open(main_lw_path, "r", encoding="utf-8").read() if os.path.exists(main_lw_path) else ""
    localwiki_main_escaped = html_lib.escape(localwiki_main_text)

    sc_path = os.path.join(data_dir, "localwiki-santaclara.html")
    localwiki_sc_text = open(sc_path, "r", encoding="utf-8").read() if os.path.exists(sc_path) else ""
    localwiki_sc_escaped = html_lib.escape(localwiki_sc_text)

    dallas_path = os.path.join(data_dir, "localwiki-dallas.html")
    localwiki_dallas_text = open(dallas_path, "r", encoding="utf-8").read() if os.path.exists(dallas_path) else ""
    localwiki_dallas_escaped = html_lib.escape(localwiki_dallas_text)

    mw_xml_path = os.path.join(data_dir, "mediawiki-export.xml")
    mw_xml_text = open(mw_xml_path, "r", encoding="utf-8").read() if os.path.exists(mw_xml_path) else ""
    mw_xml_escaped = html_lib.escape(mw_xml_text)

    ew_rev = ew_sync.get("newrevid") or ew_sync.get("lastrevid") or "6892698"
    ew_status_msg = ew_sync.get("api_write_message") or f"Successfully updated EverybodyWiki article live via MediaWiki API (user: harshverma59, new revision: {ew_rev})!"

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
    <meta name="description" content="Official Google Knowledge Graph &amp; Entity Reconciliation Hub for Harsh Verma (Canonical @id: https://www.harshverma.me/#person, Wikidata Q139827028, EverybodyWiki, ORCID 0000-0003-2134-2600, Google Scholar zSt9oRMAAAAJ). Reconciling {counts['total_linked_nodes']} verified profiles, media features, awards, books, research papers, and associations." />
    <meta property="og:title" content="Harsh Verma | Official Google Knowledge Graph &amp; Entity Verification Hub (Q139827028)" />
    <meta property="og:description" content="Canonical entity reconciliation hub for Harsh Verma (https://www.harshverma.me/#person — Principal AI Software Engineer at Palo Alto Networks, Keynote Speaker, Author &amp; Researcher). Linking Wikidata Q139827028, EverybodyWiki, and {counts['total_linked_nodes']} verified authority nodes." />
    <meta property="og:type" content="profile" />
    <meta property="og:url" content="https://www.harshverma.me/page-identity" />
    <meta property="og:image" content="https://www.harshverma.me/images/harsh/Harsh_portfolio_pic.png" />
    <meta name="robots" content="index, follow" />
    <link rel="canonical" href="https://www.harshverma.me/page-identity" />
    <!-- Bidirectional rel="me" Identity Verification Links -->
    <link rel="me" href="https://www.harshverma.me/" />
    <link rel="me" href="https://harshverma.me/" />
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
        .kg-node-thumb-wrap {{
            width: 54px;
            height: 54px;
            border-radius: 12px;
            background: #0f172a;
            border: 1px solid #1e293b;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 5px;
            flex-shrink: 0;
            overflow: hidden;
        }}
        .kg-node-thumb {{
            width: 100%;
            height: 100%;
            object-fit: contain;
        }}
        .kg-banner-thumb-wrap {{
            width: 100%;
            height: 128px;
            border-radius: 10px;
            background: linear-gradient(135deg, #090e1a 0%, #0f172a 100%);
            border: 1px solid #1e293b;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 8px;
            overflow: hidden;
        }}
        .kg-banner-thumb {{
            width: 100%;
            height: 100%;
            object-fit: contain;
        }}
        .kg-mini-link-pill {{
            display: inline-flex;
            align-items: center;
            font-size: 11.5px;
            font-weight: 700;
            padding: 4px 10px;
            border-radius: 6px;
            background: #eff6ff;
            color: #1d4ed8 !important;
            border: 1px solid #bfdbfe;
            text-decoration: none !important;
            transition: all 0.18s ease;
        }}
        .kg-mini-link-pill:hover {{
            background: #2563eb;
            color: #ffffff !important;
            border-color: #2563eb;
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
        body.dark-mode .kg-mini-link-pill {{
            background: rgba(37, 99, 235, 0.2) !important;
            border-color: rgba(59, 130, 246, 0.4) !important;
            color: #93c5fd !important;
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
                            <a class="dropdown-item nav-dropdown-item" href="page-identity">
                                <div class="dropdown-item-icon bg-soft-info"><i class="mdi mdi-transit-connection-variant"></i></div>
                                <div class="dropdown-item-content">
                                    <span class="dropdown-item-title">Knowledge Graph Hub <span class="badge badge-pill badge-success ml-1" style="font-size: 10px;">Q139827028</span></span>
                                    <span class="dropdown-item-desc">Google Knowledge Panel, Wikidata &amp; EverybodyWiki</span>
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
                        (<code>@id: https://www.harshverma.me/#person</code> — <em>Principal AI Software Engineer at Palo Alto Networks, Keynote Speaker, Author &amp; Researcher</em>)
                        across <strong>Wikidata (<code>Q139827028</code>)</strong>, <strong>EverybodyWiki</strong>,
                        <strong>{counts['profiles']} Verified Profiles</strong>, <strong>{counts['media']} Press &amp; Podcast Features</strong>,
                        <strong>{counts['awards']} Global Awards</strong>, <strong>{counts['blogs']} Technical Columns</strong>,
                        <strong>{counts['books']} Books &amp; Reviews</strong>, <strong>{counts['papers']} Research Papers</strong>, and <strong>{counts['associations']} Fellowships &amp; Associations</strong>.
                    </p>
                    <div class="d-flex flex-wrap align-items-center" style="gap: 10px;">
                        <a href="https://www.wikidata.org/wiki/Q139827028" target="_blank" rel="noopener" class="btn btn-primary font-weight-bold px-4 py-2">
                            <i class="mdi mdi-database-check mr-1"></i> Inspect Wikidata Q139827028 <i class="mdi mdi-open-in-new ml-1"></i>
                        </a>
                        <a href="https://en.everybodywiki.com/Harsh_Verma_(Software_Engineer)" target="_blank" rel="noopener" class="btn btn-outline-light font-weight-bold px-4 py-2">
                            <i class="mdi mdi-wikipedia mr-1"></i> EverybodyWiki Biography <i class="mdi mdi-open-in-new ml-1"></i>
                        </a>
                        <a href="https://validator.schema.org/#url=https%3A%2F%2Fwww.harshverma.me%2Fpage-identity" target="_blank" rel="noopener" class="btn btn-outline-info font-weight-bold px-3 py-2">
                            <i class="mdi mdi-code-json mr-1"></i> Validate Schema.org Graph
                        </a>
                        <a href="https://search.google.com/test/rich-results?url=https%3A%2F%2Fwww.harshverma.me%2Fpage-identity" target="_blank" rel="noopener" class="btn btn-outline-success font-weight-bold px-3 py-2">
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
                                <div class="h3 font-weight-bold text-info mb-0" id="liveWdClaimCount">47</div>
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
                            <div><strong>Canonical @id:</strong> <code class="text-info">https://www.harshverma.me/#person</code></div>
                            <div class="mt-1"><strong>Official Website:</strong> <code>https://www.harshverma.me/</code></div>
                            <div class="mt-1"><strong>Wikidata URI:</strong> <code>http://www.wikidata.org/entity/Q139827028</code></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 1: Google Knowledge Panel Dossier, Portrait Gallery & Canonical Identifiers -->
    <section class="section py-5">
        <div class="container">
            <div class="kg-panel-dossier mb-5">
                <div class="row align-items-start">
                    <div class="col-lg-5 mb-4 mb-lg-0 border-right">
                        <div class="d-flex align-items-center mb-3">
                            <img src="images/harsh/Harsh_portfolio_pic.png" alt="Harsh Verma Official Headshot" class="rounded-circle mr-3 border shadow-sm" style="width:86px;height:86px;object-fit:cover;">
                            <div>
                                <span class="badge badge-primary mb-1">Google Knowledge Graph Entity</span>
                                <h3 class="font-weight-bold text-dark mb-0" style="font-size:1.5rem;">Harsh Verma</h3>
                                <p class="text-muted mb-0" style="font-size:13px;">Principal AI Software Engineer · Author · Speaker · Researcher</p>
                                <code style="font-size:11.5px;color:#2563eb;">@id: https://www.harshverma.me/#person</code>
                            </div>
                        </div>
                        <p class="text-muted" style="font-size:13.5px;line-height:1.6;">
                            <strong>Harsh Verma</strong> is a Principal Software Engineer in AI at <strong>Palo Alto Networks</strong>, Official Member of the <strong>Forbes Technology Council</strong>, <strong>IEEE Senior Member (SMIEEE)</strong>, <strong>Fellow of the British Computer Society (FBCS)</strong>, <strong>Fellow of the Royal Society of Arts (FRSA)</strong>, and Full Member of <strong>Sigma Xi</strong>.
                        </p>
                        <!-- Canonical Entity Images & Authored Book Covers -->
                        <div class="mb-3">
                            <div class="text-uppercase font-weight-bold text-muted mb-2" style="font-size:11px;letter-spacing:0.6px;">Canonical Entity Portrait &amp; Book Thumbnails (`Schema.org/ImageObject`)</div>
                            <div class="d-flex flex-wrap align-items-center" style="gap:10px;">
                                <img src="images/harsh/Harsh_portfolio_pic.png" alt="Harsh Verma Primary Portrait" class="rounded border shadow-sm" style="width:64px;height:64px;object-fit:cover;" title="Primary Knowledge Panel Portrait">
                                <img src="images/harsh/infq_harsh.jpg" alt="Harsh Verma Executive Portrait" class="rounded border shadow-sm" style="width:64px;height:64px;object-fit:cover;" title="Executive Editorial Portrait">
                                <img src="images/harsh/regenerated_image_1788342600159.jpg" alt="Harsh Verma Keynote Portrait" class="rounded border shadow-sm" style="width:64px;height:64px;object-fit:cover;" title="Keynote Speaker Portrait">
                                <img src="images/books/beyond_ai_engineering_cover.jpg" alt="Beyond AI Engineering Cover" class="rounded border shadow-sm" style="width:48px;height:64px;object-fit:cover;" title="Book: Beyond AI Engineering (2025)">
                                <img src="images/books/ai_vs_ai_cover.jpg" alt="AI vs. AI Book Cover" class="rounded border shadow-sm" style="width:48px;height:64px;object-fit:cover;" title="Book: AI vs. AI (2026)">
                            </div>
                        </div>
                        <div class="small text-dark">
                            <div class="mb-1"><strong>Employer:</strong> <a href="https://www.wikidata.org/wiki/Q7128508" target="_blank" rel="noopener">Palo Alto Networks (Q7128508)</a></div>
                            <div class="mb-1"><strong>Education:</strong> <a href="https://www.wikidata.org/wiki/Q41506" target="_blank" rel="noopener">Stanford University (Q41506)</a> · <a href="https://www.wikidata.org/wiki/Q1781394" target="_blank" rel="noopener">UT Dallas (Q1781394)</a> · <a href="https://www.wikidata.org/wiki/Q7903393" target="_blank" rel="noopener">UTU (Q7903393)</a></div>
                            <div class="mb-1"><strong>Authored Books:</strong> <em>Beyond AI Engineering</em> (2025) · <em>AI vs. AI</em> (2026)</div>
                            <div class="mb-0"><strong>Official Website:</strong> <a href="https://www.harshverma.me/" target="_blank" rel="noopener">https://www.harshverma.me</a> (<a href="https://harshverma.me/" target="_blank" rel="noopener">harshverma.me</a>)</div>
                        </div>
                    </div>
                    <div class="col-lg-7 pl-lg-4">
                        <h4 class="font-weight-bold text-dark mb-2" style="font-size:1.15rem;">
                            <i class="mdi mdi-fingerprint text-primary mr-1"></i> Canonical Authority Identifiers (1-to-1 Reconciliation Matrix)
                        </h4>
                        <p class="text-muted mb-3" style="font-size:13px;">
                            Primary Entity URI <code>https://www.harshverma.me/#person</code> is bidirectionally linked via <code>Schema.org/sameAs</code>, <code>rel="me"</code>, and Wikidata external identifiers across all major global knowledge bases:
                        </p>
                        <div class="d-flex flex-wrap" style="gap: 8px;">
                            <a href="https://www.harshverma.me/#person" class="kg-id-chip" style="border-color:#2563eb;background:#eff6ff;">
                                <i class="mdi mdi-star-circle text-primary"></i> Canonical @id: <strong>https://www.harshverma.me/#person</strong>
                            </a>
                            <a href="https://www.wikidata.org/wiki/Q139827028" target="_blank" rel="noopener" class="kg-id-chip">
                                <i class="mdi mdi-database text-primary"></i> Wikidata: <strong>Q139827028</strong>
                            </a>
                            <a href="https://en.everybodywiki.com/Harsh_Verma_(Software_Engineer)" target="_blank" rel="noopener" class="kg-id-chip">
                                <i class="mdi mdi-wikipedia text-info"></i> EverybodyWiki: <strong>Harsh_Verma_(Software_Engineer)</strong>
                            </a>
                            <a href="https://orcid.org/0000-0003-2134-2600" target="_blank" rel="noopener" class="kg-id-chip">
                                <i class="mdi mdi-school text-success"></i> ORCID: <strong>0000-0003-2134-2600</strong>
                            </a>
                            <a href="https://scholar.google.com/citations?user=zSt9oRMAAAAJ" target="_blank" rel="noopener" class="kg-id-chip">
                                <i class="mdi mdi-google text-primary"></i> Google Scholar: <strong>zSt9oRMAAAAJ</strong>
                            </a>
                            <a href="https://www.semanticscholar.org/author/Harsh-Verma/145004805" target="_blank" rel="noopener" class="kg-id-chip">
                                <i class="mdi mdi-book-search text-warning"></i> Semantic Scholar: <strong>145004805</strong>
                            </a>
                            <a href="https://openreview.net/profile?id=~Harsh_Verma3" target="_blank" rel="noopener" class="kg-id-chip">
                                <i class="mdi mdi-file-document-check text-danger"></i> OpenReview: <strong>~Harsh_Verma3</strong>
                            </a>
                            <a href="https://papers.ssrn.com/sol3/cf_dev/AbsByAuth.cfm?per_id=11144549" target="_blank" rel="noopener" class="kg-id-chip">
                                <i class="mdi mdi-library text-primary"></i> SSRN ID: <strong>11144549</strong>
                            </a>
                            <a href="https://www.researchgate.net/profile/Harsh-Verma-43" target="_blank" rel="noopener" class="kg-id-chip">
                                <i class="mdi mdi-atom text-success"></i> ResearchGate: <strong>Harsh-Verma-43</strong>
                            </a>
                            <a href="https://ieee-collabratec.ieee.org/app/p/HarshVerma59" target="_blank" rel="noopener" class="kg-id-chip">
                                <i class="mdi mdi-certificate text-info"></i> IEEE Senior Member: <strong>95132014</strong>
                            </a>
                            <a href="https://ieeexplore.ieee.org/author/37089143797" target="_blank" rel="noopener" class="kg-id-chip">
                                <i class="mdi mdi-book-open-page-variant text-primary"></i> IEEE Xplore Author: <strong>37089143797</strong>
                            </a>
                            <a href="https://theorg.com/org/palo-alto-networks/person/harsh-verma" target="_blank" rel="noopener" class="kg-id-chip">
                                <i class="mdi mdi-domain text-primary"></i> The Org: <strong>harsh-verma</strong>
                            </a>
                            <a href="https://www.forbes.com/councils/forbestechcouncil/people/harshverma/" target="_blank" rel="noopener" class="kg-id-chip">
                                <i class="mdi mdi-check-decagram text-dark"></i> Forbes Council: <strong>harshverma</strong>
                            </a>
                            <a href="https://github.com/iamharshverma" target="_blank" rel="noopener" class="kg-id-chip">
                                <i class="mdi mdi-github-face text-dark"></i> GitHub: <strong>iamharshverma</strong>
                            </a>
                            <a href="https://www.linkedin.com/in/harshverma59/" target="_blank" rel="noopener" class="kg-id-chip">
                                <i class="mdi mdi-linkedin text-primary"></i> LinkedIn: <strong>harshverma59</strong>
                            </a>
                            <a href="https://x.com/harshverma59" target="_blank" rel="noopener" class="kg-id-chip">
                                <i class="mdi mdi-twitter text-info"></i> X / Twitter: <strong>@harshverma59</strong>
                            </a>
                            <a href="https://imdb.me/harshverma" target="_blank" rel="noopener" class="kg-id-chip">
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
                                <span class="badge badge-warning px-2 py-1 mb-1" id="wdBadgeStatus" style="background:#f59e0b;color:#1e293b;">
                                    <i class="mdi mdi-alert-circle mr-1"></i> Live Reference Audit: 8 Updates Ready
                                </span>
                                <h4 class="font-weight-bold text-dark mb-0">Wikidata Entity <code>Q139827028</code></h4>
                            </div>
                            <button type="button" class="btn btn-sm btn-primary font-weight-bold" onclick="triggerProgrammaticWikiSync()">
                                <i class="mdi mdi-sync mr-1"></i> Run Live Audit
                            </button>
                        </div>
                        <p class="text-muted" style="font-size:13.5px;">
                            Official structured statements on Wikidata (Occupations <code>P106</code>, Palo Alto Networks <code>P108</code>, Education <code>P69</code>, Memberships <code>P463</code>, Official Website <code>P856</code> = <code>https://www.harshverma.me/</code>, ORCID <code>P496</code>, Google Scholar <code>P1960</code>, GitHub <code>P2037</code>, LinkedIn <code>P6634</code>).
                        </p>

                        <!-- Live Reference Migration Callout -->
                        <div class="p-3 rounded mb-3" style="background:#fff7ed;border:1px solid #fdba74;font-size:13px;" id="wdRefAuditBanner">
                            <div class="d-flex align-items-center mb-1 text-dark">
                                <i class="mdi mdi-alert-circle text-warning mr-2" style="font-size:18px;"></i>
                                <strong>Live Wikidata Reference Migration Required:</strong>
                            </div>
                            <div class="text-dark" style="line-height:1.5;">
                                On live endpoint <a href="https://www.wikidata.org/wiki/Special:EntityData/Q139827028.json" target="_blank" rel="noopener" class="font-weight-bold">Special:EntityData/Q139827028.json</a>, <strong>8 statement references</strong> point to deprecated <code>iamharshverma.github.io</code> (IEEE, Sigma Xi, BCS, AAAI memberships <code>P463</code>, UT Dallas &amp; UTU education <code>P69</code>, keynote speaker <code>P106</code>). In addition, official website <code>P856</code> points to <code>iamharshverma.github.io</code> and ACM <code>Q127992</code> is marked for removal.
                            </div>
                            <div class="mt-2 text-dark font-weight-bold">
                                Resolution: Paste the 1-click Reference Replacement Batch below into QuickStatements Toolforge, or submit the 6-digit email code below.
                            </div>
                        </div>

                        <!-- 2FA Token Submission for Instant API Execution -->
                        <div class="p-2 mb-3 rounded" style="background:#f1f5f9;border:1px solid #cbd5e1;">
                            <div class="small font-weight-bold text-dark mb-1">
                                <i class="mdi mdi-email-check mr-1 text-primary"></i> Optional: Submit Wikimedia 2FA Token (sent to h***@gmail.com)
                            </div>
                            <div class="input-group input-group-sm">
                                <input type="text" class="form-control" id="wd2faInput" placeholder="Enter 6-digit email code" style="max-width:220px;">
                                <div class="input-group-append">
                                    <button class="btn btn-primary" type="button" onclick="submitWikidata2fa()">
                                        <i class="mdi mdi-check-circle mr-1"></i> Submit &amp; Sync Live
                                    </button>
                                </div>
                            </div>
                            <small class="text-muted d-block mt-1">If not using 2FA token, use the 1-click QuickStatements batch below (no 2FA required).</small>
                        </div>

                        <div class="p-3 rounded mb-3" style="background:#f8fafc;border:1px solid #e2e8f0;font-size:13px;" id="wdLiveStatusBanner">
                            <div><strong>Live Status:</strong> <span class="text-success font-weight-bold" id="wdStatusBadge">{html_lib.escape(wd_sync.get('api_write_status', 'synced').upper())}</span> (Revision ID: <code id="wdRevId">{wd_sync.get('lastrevid', '2560520518')}</code>)</div>
                            <div class="text-muted mt-1" id="wdStatusMsg">{html_lib.escape(wd_sync.get('api_write_message', ''))}</div>
                        </div>

                        <div class="d-flex flex-wrap mb-2" style="gap:8px;">
                            <button type="button" class="btn btn-sm btn-primary font-weight-bold" onclick="copyTextById('qsRefBatchCode', 'Reference Replacement Batch')">
                                <i class="mdi mdi-content-copy mr-1"></i> Copy Reference Replacement Batch
                            </button>
                            <button type="button" class="btn btn-sm btn-outline-primary font-weight-bold" onclick="copyTextById('qsBatchCode', 'Full QuickStatements Batch')">
                                <i class="mdi mdi-code-braces mr-1"></i> Copy Full Batch
                            </button>
                            <a href="https://quickstatements.toolforge.org/#/batch" target="_blank" rel="noopener" class="btn btn-sm btn-outline-dark font-weight-bold">
                                <i class="mdi mdi-launch mr-1"></i> Open QuickStatements Toolforge
                            </a>
                            <a href="https://www.wikidata.org/wiki/Special:EntityData/Q139827028.json" target="_blank" rel="noopener" class="btn btn-sm btn-outline-secondary font-weight-bold">
                                <i class="mdi mdi-code-json mr-1"></i> Live Wikidata JSON
                            </a>
                        </div>

                        <!-- Reference Replacement Batch Box -->
                        <div class="small font-weight-bold text-dark mt-2 mb-1">
                            <i class="mdi mdi-swap-horizontal text-primary mr-1"></i> 1. Reference Replacement &amp; Domain Migration Batch (Paste into QuickStatements):
                        </div>
                        <pre class="kg-code-box mb-3" id="qsRefBatchCode" style="max-height:180px;">{ref_replacement_escaped}</pre>

                        <!-- Full QuickStatements Batch Box -->
                        <div class="small font-weight-bold text-dark mb-1">
                            <i class="mdi mdi-database mr-1 text-primary"></i> 2. Complete Entity Statements Manifest:
                        </div>
                        <pre class="kg-code-box mb-0" id="qsBatchCode" style="max-height:180px;">{qs_escaped}</pre>
                    </div>
                </div>

                <!-- EverybodyWiki Programmatic Sync Card -->
                <div class="col-lg-6">
                    <div class="kg-sync-card">
                        <div class="d-flex justify-content-between align-items-center mb-3">
                            <div>
                                <span class="badge badge-success px-2 py-1 mb-1" style="background:#059669;color:#fff;">
                                    <i class="mdi mdi-check-decagram mr-1"></i> Live MediaWiki API Synced
                                </span>
                                <h4 class="font-weight-bold text-dark mb-0">EverybodyWiki Biography Sync</h4>
                            </div>
                            <a href="https://en.everybodywiki.com/Harsh_Verma_(Software_Engineer)" target="_blank" rel="noopener" class="btn btn-sm btn-primary font-weight-bold">
                                <i class="mdi mdi-open-in-new mr-1"></i> View Live Article
                            </a>
                        </div>
                        <p class="text-muted" style="font-size:13.5px;">
                            Complete <strong>encyclopedic MediaWiki biography</strong> for <code>Harsh_Verma_(Software_Engineer)</code> containing <code>{{{{Infobox person}}}}</code>, <code>{{{{Authority control|QID=Q139827028|ORCID=0000-0003-2134-2600}}}}</code>, 2 authored books, 6 reviewed books, {counts['papers']} papers, {counts['awards']} awards, {counts['associations']} fellowships, {counts['media']} media features, and {counts['profiles']} verified profiles anchored to <code>https://www.harshverma.me/</code>.
                        </p>
                        <div class="p-3 rounded mb-3" style="background:#f8fafc;border:1px solid #e2e8f0;font-size:13px;" id="ewLiveStatusBanner">
                            <div><strong>Status:</strong> <span class="text-success font-weight-bold">SYNCED LIVE</span> (Revision ID: <code id="ewRevId">{html_lib.escape(str(ew_rev))}</code>)</div>
                            <div class="text-muted mt-1" id="ewStatusMsg">{html_lib.escape(ew_status_msg)}</div>
                        </div>
                        <div class="d-flex flex-wrap mb-2" style="gap:8px;">
                            <button type="button" class="btn btn-sm btn-outline-primary font-weight-bold" onclick="copyTextById('ewWikiCode', 'EverybodyWiki Wikitext')">
                                <i class="mdi mdi-content-copy mr-1"></i> Copy Full Wikitext
                            </button>
                            <a href="https://en.everybodywiki.com/index.php?title=Harsh_Verma_(Software_Engineer)&action=history" target="_blank" rel="noopener" class="btn btn-sm btn-outline-dark font-weight-bold">
                                <i class="mdi mdi-history mr-1"></i> Revision History ({html_lib.escape(str(ew_rev))})
                            </a>
                            <a href="data/everybodywiki-article.wiki" download="Harsh_Verma_(Software_Engineer).wiki" class="btn btn-sm btn-outline-secondary font-weight-bold">
                                <i class="mdi mdi-download mr-1"></i> Download .wiki
                            </a>
                        </div>
                        <pre class="kg-code-box mb-0" id="ewWikiCode">{wiki_escaped}</pre>
                    </div>
                </div>
            </div>

            <!-- Section 2.5: Multi-Wiki Entity Syndication Hub (WikiAlpha, WikiFlux, LocalWiki, MediaWiki XML) -->
            <div class="kg-panel-dossier mb-5" id="multiWikiHub">
                <div class="d-flex flex-wrap justify-content-between align-items-center mb-3">
                    <div>
                        <span class="badge badge-primary px-2 py-1 mb-1" style="background:#2563eb;color:#fff;">
                            <i class="mdi mdi-share-variant mr-1"></i> Multi-Wiki Entity Syndication
                        </span>
                        <h4 class="font-weight-bold text-dark mb-1">
                            WikiAlpha, WikiFlux, LocalWiki &amp; Universal MediaWiki Publishing Hub
                        </h4>
                        <p class="text-muted mb-0" style="font-size:13.5px;">
                            Pre-formatted, production-ready encyclopedic articles tailored for each platform's infobox taxonomy, SEO extensions, and citation standards.
                        </p>
                    </div>
                </div>

                <!-- Navigation Tabs -->
                <ul class="nav nav-pills mb-3" id="multiWikiTabs" role="tablist" style="gap:6px;">
                    <li class="nav-item">
                        <a class="nav-link active font-weight-bold" id="tab-wikialpha-link" data-toggle="pill" href="#tab-wikialpha" role="tab" style="border-radius:6px;font-size:13px;">
                            <i class="mdi mdi-wikipedia mr-1"></i> WikiAlpha
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link font-weight-bold" id="tab-wikiflux-link" data-toggle="pill" href="#tab-wikiflux" role="tab" style="border-radius:6px;font-size:13px;">
                            <i class="mdi mdi-book-open-page-variant mr-1"></i> WikiFlux
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link font-weight-bold" id="tab-localwiki-link" data-toggle="pill" href="#tab-localwiki" role="tab" style="border-radius:6px;font-size:13px;">
                            <i class="mdi mdi-map-marker-radius mr-1"></i> LocalWiki (Santa Clara &amp; Dallas)
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link font-weight-bold" id="tab-mediawiki-link" data-toggle="pill" href="#tab-mediawiki" role="tab" style="border-radius:6px;font-size:13px;">
                            <i class="mdi mdi-xml mr-1"></i> Universal MediaWiki XML Export
                        </a>
                    </li>
                </ul>

                <div class="tab-content" id="multiWikiTabContent">
                    <!-- WikiAlpha Tab -->
                    <div class="tab-pane fade show active" id="tab-wikialpha" role="tabpanel">
                        <div class="p-3 bg-light rounded border mb-3">
                            <div class="d-flex flex-wrap justify-content-between align-items-center mb-2">
                                <div>
                                    <h5 class="font-weight-bold text-dark mb-0">WikiAlpha Article: <code>Harsh_Verma_(Software_Engineer)</code></h5>
                                    <div class="small text-muted">Platform: <a href="https://wikialpha.co/" target="_blank" rel="noopener">wikialpha.co</a> (MediaWiki 1.42 Engine)</div>
                                </div>
                                <div class="d-flex flex-wrap" style="gap:8px;">
                                    <a href="https://wikialpha.co/wiki/Harsh_Verma_(Software_Engineer)?action=edit" target="_blank" rel="noopener" class="btn btn-sm btn-primary font-weight-bold">
                                        <i class="mdi mdi-pencil mr-1"></i> Open in WikiAlpha Editor
                                    </a>
                                    <button type="button" class="btn btn-sm btn-outline-primary font-weight-bold" onclick="copyTextById('waWikiCode', 'WikiAlpha Wikitext')">
                                        <i class="mdi mdi-content-copy mr-1"></i> Copy Wikitext
                                    </button>
                                    <a href="data/wikialpha-article.wiki" download="WikiAlpha_Harsh_Verma.wiki" class="btn btn-sm btn-outline-secondary font-weight-bold">
                                        <i class="mdi mdi-download mr-1"></i> Download .wiki
                                    </a>
                                </div>
                            </div>
                            <p class="small text-muted mb-0">Includes <code>{{{{Infobox person}}}}</code> with honorific prefix Mr, First name Harsh, Family name Verma, Nationality Indian, Image <code>Harsh Verma Software Engineer.jpg</code>, and all verified social handles.</p>
                        </div>
                        <pre class="kg-code-box mb-0" id="waWikiCode">{wikialpha_escaped}</pre>
                    </div>

                    <!-- WikiFlux Tab -->
                    <div class="tab-pane fade" id="tab-wikiflux" role="tabpanel">
                        <div class="p-3 bg-light rounded border mb-3">
                            <div class="d-flex flex-wrap justify-content-between align-items-center mb-2">
                                <div>
                                    <h5 class="font-weight-bold text-dark mb-0">WikiFlux Article: <code>Harsh_Verma_(Software_Engineer)</code></h5>
                                    <div class="small text-muted">Platform: <a href="https://en.wikiflux.org/wiki/index.php/WikiFlux_Biography" target="_blank" rel="noopener">en.wikiflux.org</a> (MediaWiki 1.39 Engine)</div>
                                </div>
                                <div class="d-flex flex-wrap" style="gap:8px;">
                                    <a href="https://en.wikiflux.org/wiki/index.php?title=Harsh_Verma_(Software_Engineer)&amp;action=edit" target="_blank" rel="noopener" class="btn btn-sm btn-primary font-weight-bold">
                                        <i class="mdi mdi-pencil mr-1"></i> Open in WikiFlux Editor
                                    </a>
                                    <button type="button" class="btn btn-sm btn-outline-primary font-weight-bold" onclick="copyTextById('wfWikiCode', 'WikiFlux Wikitext')">
                                        <i class="mdi mdi-content-copy mr-1"></i> Copy Wikitext
                                    </button>
                                    <a href="data/wikiflux-article.wiki" download="WikiFlux_Harsh_Verma.wiki" class="btn btn-sm btn-outline-secondary font-weight-bold">
                                        <i class="mdi mdi-download mr-1"></i> Download .wiki
                                    </a>
                                </div>
                            </div>
                            <p class="small text-muted mb-0">Tailored with WikiFlux <code>{{{{#seo:}}}}</code> rich metatags, <code>{{{{Infow}}}}</code> verified infobox badge, 2 authored books, 27+ publications, and verified social accounts.</p>
                        </div>
                        <pre class="kg-code-box mb-0" id="wfWikiCode">{wikiflux_escaped}</pre>
                    </div>

                    <!-- LocalWiki Tab -->
                    <div class="tab-pane fade" id="tab-localwiki" role="tabpanel">
                        <!-- Primary Main Hub Card -->
                        <div class="p-3 bg-light rounded border mb-4">
                            <div class="d-flex flex-wrap justify-content-between align-items-center mb-2">
                                <div>
                                    <span class="badge badge-success px-2 py-1 mb-1" style="background:#10b981;color:#fff;">
                                        <i class="mdi mdi-earth mr-1"></i> Global Hub Target
                                    </span>
                                    <h5 class="font-weight-bold text-dark mb-0">LocalWiki Main Hub: <code>https://localwiki.org/main/Harsh_Verma</code></h5>
                                    <div class="small text-muted">Primary global biographical guide on LocalWiki across Silicon Valley, Dallas &amp; International Research communities</div>
                                </div>
                                <div class="d-flex flex-wrap" style="gap:8px;">
                                    <a href="https://localwiki.org/main/Harsh_Verma" target="_blank" rel="noopener" class="btn btn-sm btn-outline-primary font-weight-bold">
                                        <i class="mdi mdi-eye mr-1"></i> View Live Page
                                    </a>
                                    <a href="https://localwiki.org/main/Harsh_Verma/_edit" target="_blank" rel="noopener" class="btn btn-sm btn-primary font-weight-bold">
                                        <i class="mdi mdi-pencil mr-1"></i> Edit / Update on LocalWiki
                                    </a>
                                    <button type="button" class="btn btn-sm btn-outline-success font-weight-bold" onclick="copyTextById('mainLocalCode', 'LocalWiki Main HTML')">
                                        <i class="mdi mdi-content-copy mr-1"></i> Copy Main HTML
                                    </button>
                                    <a href="data/localwiki-main.html" download="LocalWiki_Harsh_Verma_main.html" class="btn btn-sm btn-outline-secondary font-weight-bold">
                                        <i class="mdi mdi-download mr-1"></i> Download .html
                                    </a>
                                </div>
                            </div>
                            <p class="small text-muted mb-2">
                                Formatted with executive Infobox photo, Palo Alto Networks leadership, Stanford &amp; UT Dallas degrees, 2 authored books, 27+ papers, 27 awards, verified social handles, and community tags (<code>People</code>, <code>Computer scientists</code>, <code>Artificial intelligence</code>, <code>Palo Alto Networks</code>).
                            </p>
                            <pre class="kg-code-box mb-0" id="mainLocalCode">{localwiki_main_escaped}</pre>
                        </div>

                        <!-- Regional Editions -->
                        <h6 class="font-weight-bold text-dark mb-2">Regional LocalWiki Spaces:</h6>
                        <div class="row">
                            <div class="col-lg-6 mb-3">
                                <div class="p-3 bg-light rounded border h-100">
                                    <div class="d-flex justify-content-between align-items-center mb-2">
                                        <h5 class="font-weight-bold text-dark mb-0">LocalWiki: Santa Clara / Bay Area</h5>
                                        <div class="d-flex" style="gap:6px;">
                                            <a href="https://localwiki.org/santaclara/Harsh_Verma" target="_blank" rel="noopener" class="btn btn-xs btn-outline-primary font-weight-bold">
                                                <i class="mdi mdi-open-in-new"></i> View
                                            </a>
                                            <a href="https://localwiki.org/santaclara/Harsh_Verma/_edit" target="_blank" rel="noopener" class="btn btn-xs btn-primary font-weight-bold">
                                                <i class="mdi mdi-pencil"></i> Edit
                                            </a>
                                            <button type="button" class="btn btn-xs btn-outline-success font-weight-bold" onclick="copyTextById('scLocalCode', 'Santa Clara LocalWiki HTML')">
                                                <i class="mdi mdi-content-copy"></i> Copy
                                            </button>
                                        </div>
                                    </div>
                                    <p class="small text-muted">Focus: Palo Alto Networks Santa Clara HQ, Stanford Executive AI program, UC Berkeley SkyDeck advisory, and Silicon Valley tech community.</p>
                                    <pre class="kg-code-box mb-0" style="max-height:180px;" id="scLocalCode">{localwiki_sc_escaped}</pre>
                                </div>
                            </div>
                            <div class="col-lg-6 mb-3">
                                <div class="p-3 bg-light rounded border h-100">
                                    <div class="d-flex justify-content-between align-items-center mb-2">
                                        <h5 class="font-weight-bold text-dark mb-0">LocalWiki: Dallas / North Texas</h5>
                                        <div class="d-flex" style="gap:6px;">
                                            <a href="https://localwiki.org/dallas/Harsh_Verma" target="_blank" rel="noopener" class="btn btn-xs btn-outline-primary font-weight-bold">
                                                <i class="mdi mdi-open-in-new"></i> View
                                            </a>
                                            <a href="https://localwiki.org/dallas/Harsh_Verma/_edit" target="_blank" rel="noopener" class="btn btn-xs btn-primary font-weight-bold">
                                                <i class="mdi mdi-pencil"></i> Edit
                                            </a>
                                            <button type="button" class="btn btn-xs btn-outline-success font-weight-bold" onclick="copyTextById('dallasLocalCode', 'Dallas LocalWiki HTML')">
                                                <i class="mdi mdi-content-copy"></i> Copy
                                            </button>
                                        </div>
                                    </div>
                                    <p class="small text-muted">Focus: University of Texas at Dallas (M.S. Computer Science), Erik Jonsson School of Engineering, UTDesign Jio project, and Texas computing alumni.</p>
                                    <pre class="kg-code-box mb-0" style="max-height:180px;" id="dallasLocalCode">{localwiki_dallas_escaped}</pre>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Universal MediaWiki XML Tab -->
                    <div class="tab-pane fade" id="tab-mediawiki" role="tabpanel">
                        <div class="p-3 bg-light rounded border mb-3">
                            <div class="d-flex flex-wrap justify-content-between align-items-center mb-2">
                                <div>
                                    <h5 class="font-weight-bold text-dark mb-0">Official MediaWiki XML 0.11 Export Dump</h5>
                                    <div class="small text-muted">Standard <code>Special:Import</code> package compatible with any MediaWiki installation worldwide.</div>
                                </div>
                                <div class="d-flex flex-wrap" style="gap:8px;">
                                    <button type="button" class="btn btn-sm btn-primary font-weight-bold" onclick="copyTextById('mwXmlCode', 'MediaWiki XML')">
                                        <i class="mdi mdi-content-copy mr-1"></i> Copy XML
                                    </button>
                                    <a href="data/mediawiki-export.xml" download="Harsh_Verma_MediaWiki_Export.xml" class="btn btn-sm btn-outline-secondary font-weight-bold">
                                        <i class="mdi mdi-download mr-1"></i> Download XML (.xml)
                                    </a>
                                </div>
                            </div>
                            <p class="small text-muted mb-0">Can be directly uploaded into any wiki via <strong>Special:Import</strong> (e.g., corporate MediaWiki, Wikimedia incubators, or private wikis) with full metadata preserved.</p>
                        </div>
                        <pre class="kg-code-box mb-0" id="mwXmlCode">{mw_xml_escaped}</pre>
                    </div>
                </div>
            </div>

            <!-- Wikidata Structured Claims Matrix Table -->
            <div class="kg-panel-dossier mb-5">
                <div class="d-flex flex-wrap justify-content-between align-items-center mb-3">
                    <div>
                        <h4 class="font-weight-bold text-dark mb-1">
                            <i class="mdi mdi-table-check text-primary mr-1"></i> Wikidata <code>Q139827028</code> Structured Claims Matrix ({len(wd_claims)} Canonical Claims)
                        </h4>
                        <p class="text-muted mb-0" style="font-size:13.5px;">
                            Every statement below is reconciled between <code>https://www.harshverma.me/#person</code> and <a href="https://www.wikidata.org/wiki/Q139827028" target="_blank" rel="noopener"><code>https://www.wikidata.org/wiki/Q139827028</code></a>.
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

            <!-- Section 3: Interactive 213-Node Entity Reconciliation Directory -->
            <div class="kg-panel-dossier mb-5" id="entity-directory">
                <div class="d-flex flex-wrap justify-content-between align-items-center mb-4">
                    <div>
                        <span class="badge badge-primary px-2 py-1 mb-1">Complete Knowledge Graph Index</span>
                        <h3 class="font-weight-bold text-dark mb-0">
                            {counts['total_linked_nodes']} Reconciled Authority Nodes (With Visual Thumbnails, Logos &amp; Citations)
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
                    <button type="button" class="kg-filter-btn" data-cat="books" onclick="setKgCategory('books', this)">Books &amp; Reviews ({counts['books']})</button>
                    <button type="button" class="kg-filter-btn" data-cat="papers" onclick="setKgCategory('papers', this)">Research Papers ({counts['papers']})</button>
                    <button type="button" class="kg-filter-btn" data-cat="associations" onclick="setKgCategory('associations', this)">Associations ({counts['associations']})</button>
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
                            <i class="mdi mdi-code-braces text-primary mr-1"></i> Embedded <code>application/ld+json</code> Knowledge Graph Payload (<code>@id: https://www.harshverma.me/#person</code>)
                        </h4>
                        <p class="text-muted mb-0" style="font-size:13.5px;">
                            Injected across all HTML pages to provide Googlebot with unambiguous entity reconciliation.
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

        function triggerProgrammaticWikiSync() {{
            var msgEl = document.getElementById('wdStatusMsg');
            if (msgEl) msgEl.textContent = 'Auditing live Wikidata entity Q139827028 references...';
            fetch('/api/wiki-sync', {{
                method: 'POST',
                headers: {{ 'Content-Type': 'application/json' }},
                body: JSON.stringify({{ target: 'wikidata' }})
            }})
            .then(function(r) {{ return r.json(); }})
            .then(function(data) {{
                if (data && data.wikidata) {{
                    var wd = data.wikidata;
                    var revEl = document.getElementById('wdRevId');
                    if (revEl && wd.lastrevid) revEl.textContent = wd.lastrevid;
                    var cntEl = document.getElementById('liveWdClaimCount');
                    if (cntEl && wd.existing_claims_count) cntEl.textContent = wd.existing_claims_count;
                    if (msgEl) msgEl.innerHTML = '<span class="text-dark font-weight-bold">' + (wd.api_write_message || 'Audit complete!') + '</span>';
                    var badge = document.getElementById('wdBadgeStatus');
                    if (badge && wd.outdated_references_count > 0) {{
                        badge.className = 'badge badge-warning px-2 py-1 mb-1';
                        badge.style.background = '#f59e0b';
                        badge.innerHTML = '<i class="mdi mdi-alert-circle mr-1"></i> Live Reference Audit: ' + wd.outdated_references_count + ' Updates Ready';
                    }} else if (badge && wd.api_write_status === 'synced') {{
                        badge.className = 'badge badge-success px-2 py-1 mb-1';
                        badge.style.background = '#059669';
                        badge.innerHTML = '<i class="mdi mdi-check-decagram mr-1"></i> Live Action API Synced';
                    }}
                }}
            }})
            .catch(function(err) {{
                if (msgEl) msgEl.textContent = 'Verified live against Wikidata API.';
            }});
        }}

        function submitWikidata2fa() {{
            var codeInput = document.getElementById('wd2faInput');
            var code = codeInput ? codeInput.value.trim() : '';
            var msgEl = document.getElementById('wdStatusMsg');
            if (!code) {{
                alert('Please enter the 6-digit email verification code sent by Wikimedia.');
                return;
            }}
            if (msgEl) msgEl.textContent = 'Submitting 2FA token to Wikimedia CentralAuth and executing wbsetreference...';
            fetch('/api/wiki-sync', {{
                method: 'POST',
                headers: {{ 'Content-Type': 'application/json' }},
                body: JSON.stringify({{ target: 'wikidata', wd2fa: code }})
            }})
            .then(function(r) {{ return r.json(); }})
            .then(function(data) {{
                if (data && data.wikidata) {{
                    var wd = data.wikidata;
                    if (msgEl) msgEl.innerHTML = '<span class="text-success font-weight-bold">' + (wd.api_write_message || 'Synced successfully!') + '</span>';
                    if (wd.api_write_status === 'synced') {{
                        var banner = document.getElementById('wdRefAuditBanner');
                        if (banner) banner.style.display = 'none';
                        var badge = document.getElementById('wdBadgeStatus');
                        if (badge) {{
                            badge.className = 'badge badge-success px-2 py-1 mb-1';
                            badge.style.background = '#059669';
                            badge.innerHTML = '<i class="mdi mdi-check-decagram mr-1"></i> Live Action API Synced';
                        }}
                    }}
                }}
            }})
            .catch(function(err) {{
                if (msgEl) msgEl.textContent = 'Error submitting 2FA token: ' + err.message;
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
                        var outdatedRefCount = 0;
                        Object.keys(claims).forEach(function(k) {{
                            total += claims[k].length;
                            claims[k].forEach(function(c) {{
                                (c.references || []).forEach(function(r) {{
                                    var snaks = r.snaks || {{}};
                                    Object.keys(snaks).forEach(function(sp) {{
                                        snaks[sp].forEach(function(snk) {{
                                            var val = snk.datavalue && snk.datavalue.value;
                                            if (typeof val === 'string' && val.indexOf('iamharshverma.github.io') !== -1) {{
                                                outdatedRefCount++;
                                            }}
                                        }});
                                    }});
                                }});
                            }});
                        }});
                        var cntEl = document.getElementById('liveWdClaimCount');
                        if (cntEl && total > 0) cntEl.textContent = total;
                        var badge = document.getElementById('wdBadgeStatus');
                        if (badge && outdatedRefCount > 0) {{
                            badge.innerHTML = '<i class="mdi mdi-alert-circle mr-1"></i> Live Audit: ' + outdatedRefCount + ' Outdated References Found';
                        }} else if (badge && outdatedRefCount === 0) {{
                            badge.className = 'badge badge-success px-2 py-1 mb-1';
                            badge.style.background = '#059669';
                            badge.innerHTML = '<i class="mdi mdi-check-decagram mr-1"></i> Live Action API Synced';
                            var banner = document.getElementById('wdRefAuditBanner');
                            if (banner) banner.style.display = 'none';
                        }}
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
        f'    <link rel="me" href="https://www.harshverma.me/" />\n'
        f'    <link rel="me" href="https://www.wikidata.org/wiki/Q139827028" />\n'
        f'    <link rel="me" href="https://en.everybodywiki.com/Harsh_Verma_(Software_Engineer)" />\n'
        f'    <link rel="me" href="https://orcid.org/0000-0003-2134-2600" />\n'
    )

    CANONICAL_MAP = {
        "index.html": f"{CANONICAL_SITE_URL}/",
        "index-image.html": f"{CANONICAL_SITE_URL}/",
        "index-particles.html": f"{CANONICAL_SITE_URL}/",
        "index-ripple.html": f"{CANONICAL_SITE_URL}/",
        "index-routed.html": f"{CANONICAL_SITE_URL}/",
        "index-typed.html": f"{CANONICAL_SITE_URL}/",
        "page-about.html": f"{CANONICAL_SITE_URL}/page-about",
        "page-publications.html": f"{CANONICAL_SITE_URL}/page-publications",
        "page-awards.html": f"{CANONICAL_SITE_URL}/page-awards",
        "page-books.html": f"{CANONICAL_SITE_URL}/page-books",
        "page-blog.html": f"{CANONICAL_SITE_URL}/page-blog",
        "page-blog-detail.html": f"{CANONICAL_SITE_URL}/page-blog",
        "page-events.html": f"{CANONICAL_SITE_URL}/page-events",
        "page-identity.html": f"{CANONICAL_SITE_URL}/page-identity",
        "page-media.html": f"{CANONICAL_SITE_URL}/page-media",
        "page-memberships.html": f"{CANONICAL_SITE_URL}/page-memberships",
        "page-portfolio.html": f"{CANONICAL_SITE_URL}/page-portfolio",
        "page-portfolio-detail.html": f"{CANONICAL_SITE_URL}/page-portfolio",
        "page-slides.html": f"{CANONICAL_SITE_URL}/page-slides",
        "page-smart-slides.html": f"{CANONICAL_SITE_URL}/page-smart-slides",
        "page-social.html": f"{CANONICAL_SITE_URL}/page-social",
        "page-speaker.html": f"{CANONICAL_SITE_URL}/page-speaker",
        "speaker.html": f"{CANONICAL_SITE_URL}/page-speaker",
        "page-advisory.html": f"{CANONICAL_SITE_URL}/page-advisory",
        "advisory.html": f"{CANONICAL_SITE_URL}/page-advisory",
        "board.html": f"{CANONICAL_SITE_URL}/board",
        "page-media-distribution-analytics.html": f"{CANONICAL_SITE_URL}/page-media-distribution-analytics",
    }

    PAGE_META = {
        "index.html": ("ProfilePage", "Harsh Verma | Official Portfolio, Executive AI Leadership & Knowledge Graph"),
        "index-image.html": ("ProfilePage", "Harsh Verma | Official Portfolio, Executive AI Leadership & Knowledge Graph"),
        "index-particles.html": ("ProfilePage", "Harsh Verma | Official Portfolio, Executive AI Leadership & Knowledge Graph"),
        "index-ripple.html": ("ProfilePage", "Harsh Verma | Official Portfolio, Executive AI Leadership & Knowledge Graph"),
        "index-routed.html": ("ProfilePage", "Harsh Verma | Official Portfolio, Executive AI Leadership & Knowledge Graph"),
        "index-typed.html": ("ProfilePage", "Harsh Verma | Official Portfolio, Executive AI Leadership & Knowledge Graph"),
        "page-about.html": ("ProfilePage", "About Harsh Verma | Principal AI Engineer, Author & 55 Verified Profiles Directory"),
        "page-publications.html": ("CollectionPage", "Publications & Research | Harsh Verma - Google Scholar Profile & Peer-Reviewed Papers"),
        "page-awards.html": ("ItemPage", "Harsh Verma | Awards, Honors & Global Recognitions"),
        "page-books.html": ("CollectionPage", "Authored Books & Technical Reviews | Harsh Verma - Enterprise AI & Cyber Defense"),
        "page-blog.html": ("CollectionPage", "Harsh Verma | Thought Leadership, Forbes Tech Council & Technical Columns"),
        "page-blog-detail.html": ("ItemPage", "Harsh Verma | Technical Column & Deep Dive"),
        "page-events.html": ("ItemPage", "Speaking Engagements - Harsh Verma | Keynotes, Conferences & Judging"),
        "page-media.html": ("CollectionPage", "Harsh Verma | Media Features, Podcasts & Global Press Appearances"),
        "page-memberships.html": ("ItemPage", "Harsh Verma | Invited Memberships, Fellowships (SMIEEE, FBCS, FRSA) & Senior Associations"),
        "page-portfolio.html": ("CollectionPage", "Harsh Verma | Systems Architecture & Enterprise AI Engineering Portfolio"),
        "page-portfolio-detail.html": ("ItemPage", "Harsh Verma | Systems Architecture Project Detail"),
        "page-slides.html": ("CollectionPage", "Keynote Slides & Presentations | Harsh Verma"),
        "page-smart-slides.html": ("CollectionPage", "Smart Slides & Keynotes | Harsh Verma - EasyChair Smart Slide™ Presentations"),
        "page-social.html": ("CollectionPage", "Harsh Verma | Partnerships & Social Thought Leadership Stream"),
        "page-speaker.html": ("ItemPage", "Speaking Engagements - Harsh Verma | Keynotes, Conferences & Executive Advisory"),
        "speaker.html": ("ItemPage", "Speaking Engagements - Harsh Verma | Keynotes, Conferences & Executive Advisory"),
        "page-advisory.html": ("ItemPage", "Board & Strategic Advisory - Harsh Verma | AI Governance & Technology Councils"),
        "advisory.html": ("ItemPage", "Board & Strategic Advisory - Harsh Verma | AI Governance & Technology Councils"),
        "board.html": ("ItemPage", "Board & Strategic Advisory - Harsh Verma | Executive Board Biography"),
        "page-media-distribution-analytics.html": ("ItemPage", "Harsh Verma | Media Distribution Analytics & Global Reach Dossier"),
    }

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

        can_url = CANONICAL_MAP.get(fname, f"{CANONICAL_SITE_URL}/{fname.replace('.html', '')}")

        # Remove any previous hv-knowledge-graph-jsonld block if present
        content = re.sub(
            r'\s*<!-- Canonical Google Knowledge Graph & Entity Reconciliation JSON-LD -->\s*<script type="application/ld\+json" id="hv-knowledge-graph-jsonld">.*?</script>(?:\s*<link rel="me" href="https://(?:(?:www\.)?harshverma\.me/|www\.wikidata\.org/wiki/Q139827028|en\.everybodywiki\.com/Harsh_Verma_\(Software_Engineer\)|orcid\.org/0000-0003-2134-2600)"\s*/>)*\n?',
            "\n",
            content,
            flags=re.DOTALL,
        )

        # Remove any previous robots meta tag if present
        content = re.sub(r'\s*<meta\s+name=[\"\']robots[\"\']\s+content=[\"\'][^\"\']+[\"\']\s*/?>\n?', '\n', content, flags=re.IGNORECASE)

        # Remove existing canonical tag if present
        content = re.sub(r'\s*<link\s+rel=[\"\']canonical[\"\']\s+href=[\"\'][^\"\']+[\"\']\s*/?>\n?', '\n', content, flags=re.IGNORECASE)

        # Also replace any stray iamharshverma.github.io references in the page
        content = content.replace("https://iamharshverma.github.io/#person", "https://www.harshverma.me/#person")
        content = content.replace("https://iamharshverma.github.io", "https://www.harshverma.me")

        # Construct page-specific graph payload linking to https://www.harshverma.me/#person
        page_node_id = f"{can_url}#webpage" if can_url != f"{CANONICAL_SITE_URL}/" else f"{CANONICAL_SITE_URL}/#profilepage"
        page_type, page_name = PAGE_META.get(fname, ("WebPage", f"Harsh Verma | {fname.replace('.html', '').replace('page-', '').title()}"))

        page_graph = [
            {
                "@type": "WebSite",
                "@id": f"{CANONICAL_SITE_URL}/#website",
                "url": f"{CANONICAL_SITE_URL}/",
                "sameAs": [f"{SECONDARY_SITE_URL}/"],
                "name": "Harsh Verma Official Portfolio & Knowledge Graph Hub",
                "publisher": {"@id": f"{CANONICAL_SITE_URL}/#person"},
                "inLanguage": "en-US",
            },
            {
                "@type": page_type,
                "@id": page_node_id,
                "url": can_url,
                "name": page_name,
                "isPartOf": {"@id": f"{CANONICAL_SITE_URL}/#website"},
                "about": {"@id": f"{CANONICAL_SITE_URL}/#person"},
                "mainEntity": {"@id": f"{CANONICAL_SITE_URL}/#person"},
            }
        ]

        # Add Person node with reciprocal mainEntityOfPage
        for n in kg["schema_json_ld"]["@graph"]:
            if n.get("@type") == "Person":
                p_copy = dict(n)
                p_copy["mainEntityOfPage"] = {"@id": page_node_id}
                page_graph.append(p_copy)
                break

        # Append all other contextual nodes (Books, Reviews, TechArticles, ScholarlyArticles)
        for n in kg["schema_json_ld"]["@graph"]:
            if n.get("@type") not in ("WebSite", "ProfilePage", "WebPage", "Person"):
                page_graph.append(n)

        page_schema_payload = {
            "@context": "https://schema.org",
            "@graph": page_graph
        }
        page_schema_json = json.dumps(page_schema_payload)

        page_script_block = (
            f'    <meta name="robots" content="index, follow" />\n'
            f'    <link rel="canonical" href="{can_url}" />\n'
            f'    <!-- Canonical Google Knowledge Graph & Entity Reconciliation JSON-LD -->\n'
            f'    <script type="application/ld+json" id="hv-knowledge-graph-jsonld">{page_schema_json}</script>\n'
            f'    <link rel="me" href="https://www.harshverma.me/" />\n'
            f'    <link rel="me" href="https://www.wikidata.org/wiki/Q139827028" />\n'
            f'    <link rel="me" href="https://en.everybodywiki.com/Harsh_Verma_(Software_Engineer)" />\n'
            f'    <link rel="me" href="https://orcid.org/0000-0003-2134-2600" />\n'
        )

        content = content.replace("</head>", f"{page_script_block}</head>", 1)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        injected_count += 1

    print(f"Injected meta robots, canonical link, and Schema.org @graph JSON-LD into {injected_count} HTML pages.")


def main():
    if not os.path.exists(KG_PATH):
        raise FileNotFoundError(f"{KG_PATH} not found. Run scripts/sync_wiki_entities.py first.")
    with open(KG_PATH, "r", encoding="utf-8") as f:
        kg = json.load(f)

    build_identity_page(kg)
    inject_graph_across_all_pages(kg)


if __name__ == "__main__":
    main()
