#!/usr/bin/env python3
"""
scripts/generate_omnisearch_js.py
Generates js/hv-omnisearch.js:
Production-grade Executive Command Palette (Cmd+K Global Omnisearch)
"""

import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JS_DIR = os.path.join(ROOT_DIR, "js")
os.makedirs(JS_DIR, exist_ok=True)

OMNI_JS = r"""/**
 * Harsh Verma - Executive Command Palette (Cmd+K Global Omnisearch)
 * File: js/hv-omnisearch.js
 * 
 * Features:
 * - Universal Keyboard Access: Cmd+K (macOS), Ctrl+K (Windows/Linux), or '/'
 * - 200+ Verified Records Indexed (222 records across 7 categories)
 * - Category Filter Pills: All (222), Publications & Patents (27), Media (44),
 *   Keynotes (33), Awards (27), Profiles (57), Memberships (26), Books (8)
 * - Real-Time Fuzzy Filtering, Token Scoring, and Match Highlighting
 * - Arrow-Key Navigation (↑/↓), Enter to open, Esc to close
 * - Direct 1-Click Navigation (Outbound in new tab, internal in-page)
 * - Search Analytics Telemetry and High-Intent Suggested Queries
 */

(function () {
  'use strict';

  var omnisearchRecords = [];
  var isLoaded = false;
  var currentCategory = 'all';
  var currentQuery = '';
  var selectedIndex = 0;
  var filteredRecords = [];
  var searchCache = {};

  var CATEGORIES = [
    { key: 'all', label: 'All', count: 222, icon: 'mdi-view-grid' },
    { key: 'publications', label: 'Publications & Patents', count: 27, icon: 'mdi-certificate' },
    { key: 'media', label: 'Media Features', count: 44, icon: 'mdi-newspaper-variant-outline' },
    { key: 'keynotes', label: 'Speaking & Keynotes', count: 33, icon: 'mdi-microphone-variant' },
    { key: 'awards', label: 'Awards & Honors', count: 27, icon: 'mdi-trophy-variant' },
    { key: 'profiles', label: 'Verified Profiles', count: 57, icon: 'mdi-check-decagram' },
    { key: 'memberships', label: 'Memberships & Fellowships', count: 26, icon: 'mdi-shield-crown-outline' },
    { key: 'books', label: 'Books & Volumes', count: 8, icon: 'mdi-book-open-page-variant' }
  ];

  var SUGGESTED_QUERIES = [
    'Agentic AI',
    'Patent 555747',
    'BCS Fellow',
    'Clean Attacks',
    'Beyond AI Engineering',
    'AI vs AI',
    'IEEE Senior Member',
    'Forbes Tech Council',
    'UC Berkeley SkyDeck',
    'TrueML Keynote',
    '606481'
  ];

  // Helper: detect macOS for shortcut labeling
  var isMac = typeof navigator !== 'undefined' && /Mac|iPod|iPhone|iPad/.test(navigator.platform);
  var shortcutLabel = isMac ? '⌘K' : 'Ctrl K';

  // Build Modal Markup
  function createModalDOM() {
    if (document.getElementById('hvOmnisearchModal')) return;

    var modal = document.createElement('div');
    modal.id = 'hvOmnisearchModal';
    modal.setAttribute('role', 'dialog');
    modal.setAttribute('aria-modal', 'true');
    modal.setAttribute('aria-label', 'Executive Command Palette');

    var pillsHtml = CATEGORIES.map(function (c) {
      return (
        '<button type="button" class="hv-filter-pill' + (c.key === 'all' ? ' active' : '') + '" data-cat="' + c.key + '">' +
        c.label + ' <span class="badge badge-pill badge-light ml-1" style="font-size:10px; opacity:0.85;">' + c.count + '</span>' +
        '</button>'
      );
    }).join('');

    modal.innerHTML =
      '<div class="hv-omnisearch-backdrop" id="hvOmnisearchBackdrop"></div>' +
      '<div class="hv-omnisearch-dialog">' +
        '<div class="hv-omnisearch-header">' +
          '<div class="hv-omnisearch-icon"><i class="mdi mdi-magnify"></i></div>' +
          '<input type="text" id="hvOmnisearchInput" class="hv-omnisearch-input" ' +
            'placeholder="Search 222+ publications, patents (555747), keynotes, media, awards, profiles..." ' +
            'autocomplete="off" spellcheck="false" aria-label="Search portfolio">' +
          '<button type="button" class="hv-omnisearch-close-btn" id="hvOmnisearchCloseBtn" aria-label="Close search">' +
            '<i class="mdi mdi-close"></i>' +
          '</button>' +
        '</div>' +
        '<div class="hv-omnisearch-pills" id="hvOmnisearchPills">' + pillsHtml + '</div>' +
        '<div class="hv-omnisearch-results" id="hvOmnisearchResults" role="listbox"></div>' +
        '<div class="hv-omnisearch-footer">' +
          '<div class="hv-footer-hints">' +
            '<span class="hv-hint-item"><kbd>↑</kbd><kbd>↓</kbd> navigate</span>' +
            '<span class="hv-hint-item"><kbd>↵</kbd> select</span>' +
            '<span class="hv-hint-item"><kbd>esc</kbd> close</span>' +
          '</div>' +
          '<div class="hv-footer-meta" id="hvFooterMeta">' +
            '<i class="mdi mdi-shield-check text-primary mr-1"></i> 222 Verified Records Indexed' +
          '</div>' +
        '</div>' +
      '</div>';

    document.body.appendChild(modal);

    // Bind inner events
    document.getElementById('hvOmnisearchBackdrop').addEventListener('click', closeOmnisearch);
    document.getElementById('hvOmnisearchCloseBtn').addEventListener('click', closeOmnisearch);

    var input = document.getElementById('hvOmnisearchInput');
    input.addEventListener('input', function (e) {
      currentQuery = e.target.value.trim();
      selectedIndex = 0;
      renderResults();
    });

    input.addEventListener('keydown', handleKeyNavigation);

    // Pill click events
    var pillBtns = modal.querySelectorAll('.hv-filter-pill');
    pillBtns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        pillBtns.forEach(function (b) { b.classList.remove('active'); });
        btn.classList.add('active');
        currentCategory = btn.getAttribute('data-cat');
        selectedIndex = 0;
        renderResults();
      });
    });
  }

  // Fetch Index Data
  function loadIndex(callback) {
    if (isLoaded) {
      if (callback) callback();
      return;
    }

    var urls = ['data/omnisearch_index.json', '/data/omnisearch_index.json'];
    function tryFetch(i) {
      if (i >= urls.length) {
        console.warn('[Omnisearch] Could not load omnisearch_index.json');
        return;
      }
      fetch(urls[i])
        .then(function (res) {
          if (!res.ok) throw new Error('HTTP ' + res.status);
          return res.json();
        })
        .then(function (data) {
          omnisearchRecords = data;
          isLoaded = true;
          if (callback) callback();
        })
        .catch(function () {
          tryFetch(i + 1);
        });
    }
    tryFetch(0);
  }

  // Open / Close Omnisearch
  function openOmnisearch(initialQuery) {
    createModalDOM();
    loadIndex(function () {
      renderResults();
    });

    var modal = document.getElementById('hvOmnisearchModal');
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';

    var input = document.getElementById('hvOmnisearchInput');
    if (typeof initialQuery === 'string') {
      input.value = initialQuery;
      currentQuery = initialQuery;
    }
    setTimeout(function () {
      input.focus();
      input.select();
    }, 50);

    renderResults();
  }

  function closeOmnisearch() {
    var modal = document.getElementById('hvOmnisearchModal');
    if (!modal) return;
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }

  function toggleOmnisearch() {
    var modal = document.getElementById('hvOmnisearchModal');
    if (modal && modal.classList.contains('active')) {
      closeOmnisearch();
    } else {
      openOmnisearch();
    }
  }

  // Escape HTML helper
  function escapeHtml(str) {
    if (!str) return '';
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  // Substring Match Highlighter
  function highlightMatches(text, query) {
    if (!query || !text) return escapeHtml(text);
    var escaped = escapeHtml(text);
    var tokens = query.split(/\s+/).filter(function (t) { return t.length > 0; });
    if (!tokens.length) return escaped;

    tokens.forEach(function (token) {
      var regex = new RegExp('(' + token.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi');
      escaped = escaped.replace(regex, '<mark class="hv-highlight-match">$1</mark>');
    });
    return escaped;
  }

  // Fuzzy Token Scoring Filter
  function filterRecords() {
    var query = currentQuery.toLowerCase();
    var cat = currentCategory;

    var list = omnisearchRecords;
    if (cat !== 'all') {
      list = list.filter(function (r) {
        return r.category_pill === cat;
      });
    }

    if (!query) {
      filteredRecords = list.slice(0, 40);
      return;
    }

    var tokens = query.split(/\s+/).filter(Boolean);

    var scored = [];
    for (var i = 0; i < list.length; i++) {
      var r = list[i];
      var titleLower = (r.title || '').toLowerCase();
      var kwLower = (r.keywords || '').toLowerCase();
      var subLower = (r.subtitle || '').toLowerCase();

      var score = 0;
      var matchesAll = true;

      for (var t = 0; t < tokens.length; t++) {
        var tok = tokens[t];
        if (titleLower.indexOf(tok) !== -1) {
          score += 15;
          if (titleLower.startsWith(tok)) score += 10;
        } else if (subLower.indexOf(tok) !== -1) {
          score += 8;
        } else if (kwLower.indexOf(tok) !== -1) {
          score += 4;
        } else {
          matchesAll = false;
          break;
        }
      }

      // Exact special matches: e.g. patent 555747
      if (query.indexOf('555747') !== -1 && titleLower.indexOf('555747') !== -1) score += 50;
      if (query.indexOf('606481') !== -1 && titleLower.indexOf('606481') !== -1) score += 50;
      if (query.indexOf('bcs') !== -1 && titleLower.indexOf('bcs') !== -1) score += 40;

      if (matchesAll) {
        scored.push({ record: r, score: score });
      }
    }

    scored.sort(function (a, b) {
      return b.score - a.score;
    });

    filteredRecords = scored.map(function (s) { return s.record; }).slice(0, 60);
  }

  // Render Result DOM
  function renderResults() {
    var container = document.getElementById('hvOmnisearchResults');
    var footerMeta = document.getElementById('hvFooterMeta');
    if (!container) return;

    filterRecords();

    if (selectedIndex >= filteredRecords.length) {
      selectedIndex = Math.max(0, filteredRecords.length - 1);
    }

    // Empty state
    if (filteredRecords.length === 0) {
      var suggestionsHtml = SUGGESTED_QUERIES.map(function (sq) {
        return '<button type="button" class="hv-suggest-chip" data-query="' + sq + '"><i class="mdi mdi-magnify"></i> ' + sq + '</button>';
      }).join('');

      container.innerHTML =
        '<div class="hv-omnisearch-empty">' +
          '<div class="hv-empty-icon"><i class="mdi mdi-text-search"></i></div>' +
          '<div class="hv-empty-title">No matching records found for "' + escapeHtml(currentQuery) + '"</div>' +
          '<div class="hv-empty-desc">Try searching by patent number (555747), research topic (Agentic AI), book title, or fellowship (BCS Fellow).</div>' +
          '<div class="hv-suggestions-container">' + suggestionsHtml + '</div>' +
        '</div>';

      if (footerMeta) {
        footerMeta.innerHTML = '<span class="text-muted">0 matches found</span>';
      }

      // Bind suggestion chips
      container.querySelectorAll('.hv-suggest-chip').forEach(function (chip) {
        chip.addEventListener('click', function () {
          var q = chip.getAttribute('data-query');
          var input = document.getElementById('hvOmnisearchInput');
          input.value = q;
          currentQuery = q;
          renderResults();
          input.focus();
        });
      });
      return;
    }

    var html = '';
    var lastCategory = null;

    for (var i = 0; i < filteredRecords.length; i++) {
      var r = filteredRecords[i];
      var isSelected = (i === selectedIndex);

      // Section group header when viewing 'all'
      if (currentCategory === 'all' && r.category !== lastCategory) {
        lastCategory = r.category;
        html += '<div class="hv-group-header">' +
                  '<span>' + r.category + '</span>' +
                  '<span class="badge badge-light border" style="font-size:10px;">' + r.category_pill + '</span>' +
                '</div>';
      }

      var iconClass = r.icon || 'mdi-file-document-outline';
      var badgeClass = r.badge_class || 'badge-primary';
      var titleHighlighted = highlightMatches(r.title, currentQuery);
      var subHighlighted = highlightMatches(r.subtitle, currentQuery);

      html +=
        '<a href="' + escapeHtml(r.url) + '" ' + (r.external ? 'target="_blank" rel="noopener noreferrer"' : '') +
        ' class="hv-search-item' + (isSelected ? ' selected' : '') + '" data-index="' + i + '" role="option" aria-selected="' + isSelected + '">' +
          '<div class="hv-item-icon-box">' +
            '<i class="mdi ' + iconClass + '"></i>' +
          '</div>' +
          '<div class="hv-item-body">' +
            '<div class="hv-item-top">' +
              '<h4 class="hv-item-title">' + titleHighlighted + '</h4>' +
              '<span class="badge badge-pill ' + badgeClass + ' hv-item-badge">' + escapeHtml(r.badge) + '</span>' +
            '</div>' +
            '<div class="hv-item-subtitle">' + subHighlighted + '</div>' +
            (r.description ? '<div class="hv-item-desc">' + escapeHtml(r.description) + '</div>' : '') +
          '</div>' +
          '<div class="hv-item-arrow"><i class="mdi ' + (r.external ? 'mdi-open-in-new' : 'mdi-arrow-right') + '"></i></div>' +
        '</a>';
    }

    container.innerHTML = html;

    if (footerMeta) {
      footerMeta.innerHTML =
        '<i class="mdi mdi-check-circle-outline text-success mr-1"></i> ' +
        filteredRecords.length + ' match' + (filteredRecords.length === 1 ? '' : 'es') +
        (currentCategory !== 'all' ? ' in ' + currentCategory : ' across 222 indexed records');
    }

    // Scroll active item into view
    var activeEl = container.querySelector('.hv-search-item.selected');
    if (activeEl) {
      activeEl.scrollIntoView({ block: 'nearest' });
    }

    // Click & hover events on search items
    var itemEls = container.querySelectorAll('.hv-search-item');
    itemEls.forEach(function (el) {
      el.addEventListener('mouseenter', function () {
        itemEls.forEach(function (e) { e.classList.remove('selected'); });
        el.classList.add('selected');
        selectedIndex = parseInt(el.getAttribute('data-index'), 10);
      });
      el.addEventListener('click', function () {
        logSearchSelection(currentQuery, filteredRecords[selectedIndex]);
        closeOmnisearch();
      });
    });
  }

  // Keyboard navigation handler
  function handleKeyNavigation(e) {
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      if (filteredRecords.length > 0) {
        selectedIndex = (selectedIndex + 1) % filteredRecords.length;
        renderResults();
      }
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      if (filteredRecords.length > 0) {
        selectedIndex = (selectedIndex - 1 + filteredRecords.length) % filteredRecords.length;
        renderResults();
      }
    } else if (e.key === 'Enter') {
      e.preventDefault();
      if (filteredRecords.length > 0 && filteredRecords[selectedIndex]) {
        var item = filteredRecords[selectedIndex];
        logSearchSelection(currentQuery, item);
        closeOmnisearch();
        if (item.url) {
          if (item.external) {
            window.open(item.url, '_blank', 'noopener,noreferrer');
          } else {
            window.location.href = item.url;
          }
        }
      }
    } else if (e.key === 'Escape') {
      e.preventDefault();
      closeOmnisearch();
    }
  }

  // Telemetry logger
  function logSearchSelection(query, item) {
    try {
      var telemetry = JSON.parse(localStorage.getItem('hv_omnisearch_telemetry') || '[]');
      telemetry.unshift({
        query: query,
        selected_id: item.id,
        category: item.category,
        timestamp: new Date().toISOString()
      });
      if (telemetry.length > 50) telemetry = telemetry.slice(0, 50);
      localStorage.setItem('hv_omnisearch_telemetry', JSON.stringify(telemetry));
    } catch (err) {
      // ignore localStorage quota errors
    }
  }

  // Check if focus is in an input or editable element
  function isInputFocused() {
    var tag = document.activeElement ? document.activeElement.tagName.toLowerCase() : '';
    return tag === 'input' || tag === 'textarea' || (document.activeElement && document.activeElement.isContentEditable);
  }

  // Global Keyboard Listener
  window.addEventListener('keydown', function (e) {
    // Cmd+K or Ctrl+K
    if ((e.metaKey || e.ctrlKey) && (e.key === 'k' || e.key === 'K')) {
      e.preventDefault();
      toggleOmnisearch();
      return;
    }

    // '/' key when not focused in input
    if (e.key === '/' && !isInputFocused()) {
      var modal = document.getElementById('hvOmnisearchModal');
      if (!modal || !modal.classList.contains('active')) {
        e.preventDefault();
        openOmnisearch();
      }
    }
  });

  // Attach search triggers across the page
  function attachTriggers() {
    document.querySelectorAll('[data-action="open-omnisearch"], #navGlobalSearchBtn, .open-omnisearch-trigger').forEach(function (btn) {
      if (!btn.hasAttribute('data-omnisearch-bound')) {
        btn.setAttribute('data-omnisearch-bound', 'true');
        btn.addEventListener('click', function (e) {
          e.preventDefault();
          openOmnisearch();
        });
      }
    });

    // Update shortcut badge text according to OS
    document.querySelectorAll('.nav-kbd, .search-kbd-shortcut kbd').forEach(function (kbd) {
      kbd.textContent = shortcutLabel;
    });
  }

  // Auto-init on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      loadIndex();
      attachTriggers();
    });
  } else {
    loadIndex();
    attachTriggers();
  }

  // Expose API on window
  window.HVOmnisearch = {
    open: openOmnisearch,
    close: closeOmnisearch,
    toggle: toggleOmnisearch,
    loadIndex: loadIndex
  };

})();
"""

with open(os.path.join(JS_DIR, "hv-omnisearch.js"), "w", encoding="utf-8") as f:
    f.write(OMNI_JS)

print("Generated js/hv-omnisearch.js successfully!")
