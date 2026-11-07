#!/usr/bin/env python3
"""
scripts/build_command_palette_js.py
Compiles 200+ verified records across Harsh Verma's portfolio and generates
the high-performance, zero-dependency client-side Command Palette script: js/hv-command-palette.js
"""

import os
import sys
import re
import json

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

DATA_DIR = os.path.join(ROOT_DIR, "data")
JS_DIR = os.path.join(ROOT_DIR, "js")
os.makedirs(JS_DIR, exist_ok=True)

from scripts.export_all_sections_json import parse_event_cards

def compile_index():
    index_items = []

    # 1. Publications & Patents (27 records)
    with open(os.path.join(DATA_DIR, "research_publications.json"), "r", encoding="utf-8") as f:
        pubs = json.load(f)
    for p in pubs:
        title = p.get("title", "")
        is_patent = "patent" in title.lower() or "patent" in p.get("venue", "").lower()
        url = p.get("primary_url") or p.get("doi") or p.get("pdf_url") or "page-publications"
        if url.startswith("10."):
            url = f"https://doi.org/{url}"
        
        patent_id = ""
        if "555747" in title or "555747" in p.get("abstract", ""):
            patent_id = "Patent No: 555747"
        elif "606481" in title or "606481" in p.get("abstract", ""):
            patent_id = "Patent No: 606481"

        index_items.append({
            "id": f"pub-{p.get('id', len(index_items))}",
            "title": title,
            "subtitle": p.get("venue", "Peer-Reviewed Scholarly Venue"),
            "category": "pubs",
            "categoryLabel": "Publications & Patents",
            "icon": "mdi-certificate" if is_patent else "mdi-file-document-outline",
            "date": str(p.get("year", "2026")),
            "url": url,
            "identifier": patent_id or p.get("doi", ""),
            "desc": p.get("abstract", "")[:180] + ("..." if len(p.get("abstract", "")) > 180 else ""),
            "search_text": f"{title} {p.get('venue', '')} {patent_id} {p.get('doi', '')} {p.get('abstract', '')} {p.get('year', '')} patent publication research ieee springer".lower()
        })

    # Also explicitly ensure Granted Patent 555747 and 606481 and In-Process Suite are indexable
    patent_entries = [
        {
            "id": "patent-555747",
            "title": "SYSTEMS AND METHODS FOR PERFORMING LOAD TESTING OF A SOCIAL NETWORKING APPLICATION",
            "subtitle": "Granted Patent · Patent No: 555747 · App No: 201711003607",
            "category": "pubs",
            "categoryLabel": "Publications & Patents",
            "icon": "mdi-certificate",
            "date": "Dec 3, 2024",
            "url": "https://iprsearch.ipindia.gov.in/PublicSearch/PublicationSearch/",
            "identifier": "Patent No: 555747",
            "desc": "Granted Patent for automated high-throughput load simulation, performance stress benchmarking, and real-time telemetry testing across distributed service topologies.",
            "search_text": "patent 555747 201711003607 load testing performance simulation hike social networking distributed systems granted".lower()
        },
        {
            "id": "patent-606481",
            "title": "COVID PREVENTIVE AUTOMATED ENTRY POINT (COPAEP)",
            "subtitle": "Granted Patent · Patent No: 606481 · App No: 202011024968",
            "category": "pubs",
            "categoryLabel": "Publications & Patents",
            "icon": "mdi-certificate",
            "date": "Granted",
            "url": "https://iprsearch.ipindia.gov.in/PublicSearch/PublicationSearch/",
            "identifier": "Patent No: 606481",
            "desc": "Granted Patent for integrated automated screening checkpoint system incorporating multi-tier sensor subsystems for non-contact thermal scanning.",
            "search_text": "patent 606481 202011024968 copaep thermal sensor screening checkpoint cyber-physical granted".lower()
        },
        {
            "id": "patent-panw-suite",
            "title": "AGENTIC AI, ENTERPRISE COPILOT SYSTEMS & COPILOT NAVIGATION ARCHITECTURES",
            "subtitle": "Palo Alto Networks · Suite of 4 Patent Applications (In-Process)",
            "category": "pubs",
            "categoryLabel": "Publications & Patents",
            "icon": "mdi-shield-lock-outline",
            "date": "In Process",
            "url": "https://www.paloaltonetworks.com/",
            "identifier": "4 Patents In Process · Palo Alto Networks",
            "desc": "Proprietary suite of four in-process patent applications developing foundational intellectual property in autonomous Agentic AI orchestration and Copilot Navigation.",
            "search_text": "palo alto networks patent agentic ai copilot navigation enterprise copilot autonomous reasoning".lower()
        }
    ]
    for pe in patent_entries:
        if not any(it.get("identifier") == pe["identifier"] for it in index_items):
            index_items.append(pe)

    # 2. Tier-1 Media Features (44 records)
    with open(os.path.join(DATA_DIR, "media_features.json"), "r", encoding="utf-8") as f:
        media = json.load(f)
    for m in media:
        outlet = m.get("outlet", "")
        title = m.get("headline", "") or m.get("title", "")
        url = m.get("link", "") or m.get("url", "")
        index_items.append({
            "id": f"media-{m.get('id', len(index_items))}",
            "title": title,
            "subtitle": f"{outlet} · Tier-1 Press Coverage",
            "category": "media",
            "categoryLabel": "Media Features",
            "icon": "mdi-newspaper-variant-outline",
            "date": m.get("date", "2026"),
            "url": url,
            "identifier": outlet,
            "desc": m.get("excerpt", "") or m.get("description", "") or f"Featured in {outlet}",
            "search_text": f"{title} {outlet} {m.get('date', '')} {m.get('excerpt', '')} business insider ap news yahoo finance times square techtimes press media".lower()
        })

    # 3. Speaking, Keynotes & Judging (33 records)
    event_cards = parse_event_cards()
    for ev in event_cards:
        category = ev.get("category", "")
        role = ev.get("role", "")
        url = ev.get("primary_url", "page-events")
        is_keynote = "keynote" in ev.get("title", "").lower() or "speaker" in role.lower()
        index_items.append({
            "id": f"event-{ev.get('id', len(index_items))}",
            "title": ev.get("title", ""),
            "subtitle": f"{ev.get('organizer', '')} · {role}",
            "category": "keynotes",
            "categoryLabel": "Speaking & Keynotes",
            "icon": "mdi-microphone" if is_keynote else "mdi-gavel",
            "date": ev.get("date", "2026"),
            "url": url,
            "identifier": ev.get("badge", role),
            "desc": ev.get("description", "")[:180] + ("..." if len(ev.get("description", "")) > 180 else ""),
            "search_text": f"{ev.get('title', '')} {ev.get('organizer', '')} {role} {ev.get('date', '')} {ev.get('location', '')} {ev.get('description', '')} {' '.join(ev.get('tags', []))} keynote speaking judging panel hackathon".lower()
        })

    # 4. Awards & Honors (27 records)
    with open(os.path.join(DATA_DIR, "awards_and_honors.json"), "r", encoding="utf-8") as f:
        awards = json.load(f)
    for a in awards:
        title = a.get("title", "")
        org = a.get("issuer", "") or a.get("organization", "") or a.get("presenter", "")
        url = a.get("url", "") or a.get("link", "") or "page-awards"
        index_items.append({
            "id": f"award-{a.get('id', len(index_items))}",
            "title": title,
            "subtitle": f"{org} · {a.get('category', 'Global Technology Honor')}",
            "category": "awards",
            "categoryLabel": "Awards & Honors",
            "icon": "mdi-trophy-variant-outline",
            "date": str(a.get("year", "2026")),
            "url": url,
            "identifier": a.get("badge", "Honoree"),
            "desc": a.get("description", "")[:180] + ("..." if len(a.get("description", "")) > 180 else ""),
            "search_text": f"{title} {org} {a.get('year', '')} {a.get('category', '')} {a.get('description', '')} award honor nvtc cyber50 innovator of the year forttuna".lower()
        })

    # 5. Verified Directory Profiles (57 records)
    with open(os.path.join(DATA_DIR, "verified_profiles.json"), "r", encoding="utf-8") as f:
        profiles = json.load(f)
    for pr in profiles:
        title = pr.get("name", "")
        url = pr.get("url", "")
        index_items.append({
            "id": f"profile-{pr.get('id', len(index_items))}",
            "title": title,
            "subtitle": f"{pr.get('category_label', pr.get('category', 'Directory'))} · {pr.get('identifier', 'Verified Profile')}",
            "category": "profiles",
            "categoryLabel": "Verified Profiles",
            "icon": "mdi-account-check-outline",
            "date": "Verified",
            "url": url,
            "identifier": pr.get("identifier", "Verified"),
            "desc": pr.get("description", "")[:180] + ("..." if len(pr.get("description", "")) > 180 else ""),
            "search_text": f"{title} {pr.get('category_label', '')} {pr.get('identifier', '')} {pr.get('description', '')} {pr.get('search_keywords', '')} verified profile directory".lower()
        })

    # 6. Memberships & Fellowships (26 records)
    with open(os.path.join(DATA_DIR, "memberships.json"), "r", encoding="utf-8") as f:
        memberships = json.load(f)
    for m in memberships:
        title = m.get("organization_name", m.get("title", ""))
        role = m.get("membership_role", m.get("role", ""))
        mem_id = m.get("membership_id", m.get("credential_id", ""))
        url = m.get("link", m.get("url", ""))
        index_items.append({
            "id": f"mem-{m.get('id', len(index_items))}",
            "title": title,
            "subtitle": f"{role} · {mem_id or 'Elected Fellow/Member'}",
            "category": "memberships",
            "categoryLabel": "Memberships & Fellowships",
            "icon": "mdi-shield-star-outline",
            "date": str(m.get("date_joined", "2026")),
            "url": url,
            "identifier": mem_id,
            "desc": m.get("description", "")[:180] + ("..." if len(m.get("description", "")) > 180 else ""),
            "search_text": f"{title} {role} {mem_id} {m.get('description', '')} bcs fellow fbcs ieee senior member smieee forbes council frsa sigmaxi membership fellowship".lower()
        })

    # 7. Books & Volumes (8 records)
    with open(os.path.join(DATA_DIR, "books_and_volumes.json"), "r", encoding="utf-8") as f:
        books = json.load(f)
    for b in books:
        title = b.get("title", "")
        role = b.get("role", "")
        url = b.get("catalog_url", "page-books")
        index_items.append({
            "id": f"book-{b.get('id', len(index_items))}",
            "title": title,
            "subtitle": f"{role} · {b.get('publisher', '')}",
            "category": "books",
            "categoryLabel": "Books & Volumes",
            "icon": "mdi-book-open-page-variant-outline",
            "date": str(b.get("publication_date", "2026")),
            "url": url,
            "identifier": b.get("publication_status", role),
            "desc": b.get("synopsis", "")[:180] + ("..." if len(b.get("synopsis", "")) > 180 else ""),
            "search_text": f"{title} {b.get('subtitle', '')} {role} {b.get('publisher', '')} {b.get('synopsis', '')} {' '.join(b.get('key_themes', []))} beyond ai engineering ai vs ai packt author book".lower()
        })

    print(f"Total compiled index items: {len(index_items)}")
    return index_items

def generate_js_file():
    items = compile_index()
    raw_json = json.dumps(items, ensure_ascii=False)

    js_content = f"""/**
 * js/hv-command-palette.js
 * ========================
 * Executive Command Palette (Cmd+K Global Omnisearch)
 * Indexes 200+ verified records across Publications & Patents, Media Features,
 * Speaking & Keynotes, Awards & Honors, Verified Profiles, Memberships, and Books.
 * 
 * Features:
 * - Universal keyboard access: Cmd+K (macOS), Ctrl+K (Windows/Linux), Escape to close
 * - Top-center Global Search pill integration
 * - Real-time fuzzy filtering with keyword highlights
 * - Category filter pills (All, Publications & Patents, Media, Keynotes, Awards, Profiles, Memberships, Books)
 * - Arrow-key navigation (Up/Down) & Enter to open verified URL
 */

(function() {{
  'use strict';

  var recordsIndex = {raw_json};
  var activeCategory = 'all';
  var activeIndex = 0;
  var filteredResults = [];
  var isPaletteOpen = false;

  var categoryPillDefinitions = [
    {{ id: 'all', label: 'All', count: recordsIndex.length }},
    {{ id: 'pubs', label: 'Publications & Patents', count: recordsIndex.filter(function(r) {{ return r.category === 'pubs'; }}).length }},
    {{ id: 'media', label: 'Media', count: recordsIndex.filter(function(r) {{ return r.category === 'media'; }}).length }},
    {{ id: 'keynotes', label: 'Keynotes & Speaking', count: recordsIndex.filter(function(r) {{ return r.category === 'keynotes'; }}).length }},
    {{ id: 'awards', label: 'Awards', count: recordsIndex.filter(function(r) {{ return r.category === 'awards'; }}).length }},
    {{ id: 'profiles', label: 'Profiles', count: recordsIndex.filter(function(r) {{ return r.category === 'profiles'; }}).length }},
    {{ id: 'memberships', label: 'Memberships', count: recordsIndex.filter(function(r) {{ return r.category === 'memberships'; }}).length }},
    {{ id: 'books', label: 'Books', count: recordsIndex.filter(function(r) {{ return r.category === 'books'; }}).length }}
  ];

  function createModalHtml() {{
    if (document.getElementById('hvCommandPaletteBackdrop')) return;

    var filterPillsHtml = categoryPillDefinitions.map(function(def) {{
      var isActive = def.id === 'all' ? 'active' : '';
      return '<button type="button" class="hv-filter-pill ' + isActive + '" data-cat="' + def.id + '">' +
             def.label + ' <span style="opacity: 0.75; font-size: 10.5px;">(' + def.count + ')</span></button>';
    }}).join('');

    var modalHtml = 
      '<div class="hv-palette-backdrop" id="hvCommandPaletteBackdrop" role="dialog" aria-modal="true" aria-label="Executive Omnisearch">' +
      '  <div class="hv-palette-dialog" id="hvPaletteDialog">' +
      '    <div class="hv-palette-header">' +
      '      <i class="mdi mdi-magnify hv-palette-icon-search"></i>' +
      '      <input type="text" class="hv-palette-input" id="hvPaletteInput" placeholder="Search 200+ publications, patents, keynotes, media, awards..." autocomplete="off" spellcheck="false">' +
      '      <button type="button" class="hv-palette-close-btn" id="hvPaletteCloseBtn" title="Close (ESC)">ESC</button>' +
      '    </div>' +
      '    <div class="hv-palette-filters" id="hvPaletteFilters">' +
             filterPillsHtml +
      '    </div>' +
      '    <div class="hv-palette-results" id="hvPaletteResults">' +
      '    </div>' +
      '    <div class="hv-palette-footer">' +
      '      <div class="hv-palette-hints">' +
      '        <span class="hv-hint-item"><kbd>↑</kbd> <kbd>↓</kbd> navigate</span>' +
      '        <span class="hv-hint-item"><kbd>↵</kbd> select</span>' +
      '        <span class="hv-hint-item"><kbd>ESC</kbd> close</span>' +
      '      </div>' +
      '      <div class="hv-palette-total-badge">' +
      '        <span style="font-weight: 700; color: #2563eb;">' + recordsIndex.length + ' Verified Records</span>' +
      '      </div>' +
      '    </div>' +
      '  </div>' +
      '</div>';

    var container = document.createElement('div');
    container.innerHTML = modalHtml;
    document.body.appendChild(container.firstElementChild);

    bindModalEvents();
  }}

  function highlightMatches(text, query) {{
    if (!query || !text) return text;
    var safeQuery = query.trim().replace(/[.*+?^${{}}()|[\\]\\\\]/g, '\\\\$&');
    var tokens = safeQuery.split(/\\s+/).filter(Boolean);
    if (!tokens.length) return text;
    var pattern = new RegExp('(' + tokens.join('|') + ')', 'gi');
    return text.replace(pattern, '<mark class="hv-item-highlight">$1</mark>');
  }}

  function filterRecords(query) {{
    var cleanQuery = (query || '').trim().toLowerCase();
    var tokens = cleanQuery.split(/\\s+/).filter(Boolean);

    filteredResults = recordsIndex.filter(function(item) {{
      if (activeCategory !== 'all' && item.category !== activeCategory) {{
        return false;
      }}
      if (!tokens.length) return true;
      var target = item.search_text;
      return tokens.every(function(tok) {{
        return target.indexOf(tok) !== -1;
      }});
    }});

    activeIndex = 0;
    renderResults(cleanQuery);
  }}

  function renderResults(query) {{
    var resultsContainer = document.getElementById('hvPaletteResults');
    if (!resultsContainer) return;

    if (!filteredResults.length) {{
      resultsContainer.innerHTML = 
        '<div class="hv-palette-empty">' +
        '  <div class="hv-palette-empty-icon"><i class="mdi mdi-text-search"></i></div>' +
        '  <h6 style="font-weight: 700; margin-bottom: 4px;">No matching records found</h6>' +
        '  <p style="font-size: 13px; margin-bottom: 0;">Try searching for \"Patent 555747\", \"Forbes\", \"Clean Attacks\", \"Keynote\", or \"BCS\".</p>' +
        '</div>';
      return;
    }}

    var html = filteredResults.map(function(item, idx) {{
      var isActive = idx === activeIndex ? 'active-palette-item' : '';
      var iconClass = item.icon || 'mdi-file-document-outline';
      var highlightedTitle = highlightMatches(item.title, query);
      var highlightedSub = highlightMatches(item.subtitle, query);
      var highlightedDesc = highlightMatches(item.desc, query);

      return (
        '<a href=\"' + item.url + '\" target=\"_blank\" rel=\"noopener noreferrer\" class=\"hv-palette-item ' + isActive + '\" data-index=\"' + idx + '\">' +
        '  <div class=\"hv-item-icon-box cat-' + item.category + '\">' +
        '    <i class=\"mdi ' + iconClass + '\"></i>' +
        '  </div>' +
        '  <div class=\"hv-item-content\">' +
        '    <div class=\"hv-item-topline\">' +
        '      <span class=\"hv-item-cat-badge\">' + item.categoryLabel + '</span>' +
        (item.date ? '      <span class=\"hv-item-date\">' + item.date + '</span>' : '') +
        (item.identifier ? '      <span class=\"hv-item-date font-weight-bold\" style=\"color: #2563eb;\">' + item.identifier + '</span>' : '') +
        '    </div>' +
        '    <div class=\"hv-item-title\">' + highlightedTitle + '</div>' +
        (item.subtitle ? '    <div style=\"font-size: 12px; color: #64748b; margin-bottom: 2px;\">' + highlightedSub + '</div>' : '') +
        (item.desc ? '    <div class=\"hv-item-desc\">' + highlightedDesc + '</div>' : '') +
        '  </div>' +
        '  <div class=\"hv-item-action-icon\"><i class=\"mdi mdi-arrow-top-right\"></i></div>' +
        '</a>'
      );
    }}).join('');

    resultsContainer.innerHTML = html;

    var activeEl = resultsContainer.querySelector('.active-palette-item');
    if (activeEl) {{
      activeEl.scrollIntoView({{ block: 'nearest' }});
    }}
  }}

  function openPalette(initialCategory) {{
    createModalHtml();
    var backdrop = document.getElementById('hvCommandPaletteBackdrop');
    var input = document.getElementById('hvPaletteInput');
    if (!backdrop || !input) return;

    if (initialCategory) {{
      activeCategory = initialCategory;
      var pills = document.querySelectorAll('.hv-filter-pill');
      pills.forEach(function(p) {{
        if (p.getAttribute('data-cat') === initialCategory) {{
          p.classList.add('active');
        }} else {{
          p.classList.remove('active');
        }}
      }});
    }}

    backdrop.classList.add('hv-open');
    isPaletteOpen = true;
    document.body.style.overflow = 'hidden';

    input.value = '';
    filterRecords('');
    setTimeout(function() {{
      input.focus();
    }}, 50);
  }}

  function closePalette() {{
    var backdrop = document.getElementById('hvCommandPaletteBackdrop');
    if (!backdrop) return;
    backdrop.classList.remove('hv-open');
    isPaletteOpen = false;
    document.body.style.overflow = '';
  }}

  function bindModalEvents() {{
    var backdrop = document.getElementById('hvCommandPaletteBackdrop');
    var dialog = document.getElementById('hvPaletteDialog');
    var input = document.getElementById('hvPaletteInput');
    var closeBtn = document.getElementById('hvPaletteCloseBtn');
    var filters = document.getElementById('hvPaletteFilters');
    var results = document.getElementById('hvPaletteResults');

    if (closeBtn) {{
      closeBtn.addEventListener('click', closePalette);
    }}

    if (backdrop) {{
      backdrop.addEventListener('click', function(e) {{
        if (e.target === backdrop) {{
          closePalette();
        }}
      }});
    }}

    if (filters) {{
      filters.addEventListener('click', function(e) {{
        var btn = e.target.closest('.hv-filter-pill');
        if (!btn) return;
        var cat = btn.getAttribute('data-cat');
        activeCategory = cat;
        document.querySelectorAll('.hv-filter-pill').forEach(function(b) {{
          b.classList.remove('active');
        }});
        btn.classList.add('active');
        filterRecords(input.value);
        input.focus();
      }});
    }}

    if (input) {{
      input.addEventListener('input', function() {{
        filterRecords(input.value);
      }});
    }}

    if (results) {{
      results.addEventListener('mousemove', function(e) {{
        var item = e.target.closest('.hv-palette-item');
        if (!item) return;
        var idx = parseInt(item.getAttribute('data-index'), 10);
        if (!isNaN(idx) && idx !== activeIndex) {{
          activeIndex = idx;
          results.querySelectorAll('.hv-palette-item').forEach(function(el, i) {{
            if (i === idx) el.classList.add('active-palette-item');
            else el.classList.remove('active-palette-item');
          }});
        }}
      }});
    }}
  }}

  // Global Keyboard shortcuts: Cmd+K / Ctrl+K / ESC / Arrow navigation
  window.addEventListener('keydown', function(e) {{
    var isCmdK = (e.metaKey || e.ctrlKey) && (e.key === 'k' || e.key === 'K');
    
    if (isCmdK) {{
      e.preventDefault();
      if (isPaletteOpen) {{
        closePalette();
      }} else {{
        openPalette();
      }}
      return;
    }}

    if (!isPaletteOpen) return;

    if (e.key === 'Escape') {{
      e.preventDefault();
      closePalette();
      return;
    }}

    if (e.key === 'ArrowDown') {{
      e.preventDefault();
      if (filteredResults.length > 0) {{
        activeIndex = (activeIndex + 1) % filteredResults.length;
        renderResults(document.getElementById('hvPaletteInput').value);
      }}
      return;
    }}

    if (e.key === 'ArrowUp') {{
      e.preventDefault();
      if (filteredResults.length > 0) {{
        activeIndex = (activeIndex - 1 + filteredResults.length) % filteredResults.length;
        renderResults(document.getElementById('hvPaletteInput').value);
      }}
      return;
    }}

    if (e.key === 'Enter') {{
      if (filteredResults.length > 0 && filteredResults[activeIndex]) {{
        e.preventDefault();
        var targetUrl = filteredResults[activeIndex].url;
        closePalette();
        if (targetUrl) {{
          window.open(targetUrl, '_blank', 'noopener,noreferrer');
        }}
      }}
      return;
    }}
  }});

  // Public API
  window.hvCommandPalette = {{
    open: openPalette,
    close: closePalette,
    getRecordsCount: function() {{ return recordsIndex.length; }},
    getIndex: function() {{ return recordsIndex; }}
  }};

  // Delegate click for any .btn-global-search-trigger on the page
  document.addEventListener('click', function(e) {{
    var trigger = e.target.closest('.btn-global-search-trigger, .nav-search-btn');
    if (trigger) {{
      e.preventDefault();
      openPalette();
    }}
  }});

  // Auto-init modal on DOM load
  if (document.readyState === 'loading') {{
    document.addEventListener('DOMContentLoaded', createModalHtml);
  }} else {{
    createModalHtml();
  }}

}})();
"""

    output_path = os.path.join(JS_DIR, "hv-command-palette.js")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"Generated {output_path} with {len(items)} indexed records.")

if __name__ == "__main__":
    generate_js_file()
