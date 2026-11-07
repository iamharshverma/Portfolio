/**
 * Harsh Verma - Executive Command Palette (Cmd+K Global Omnisearch)
 * File: js/hv-omnisearch.js
 * 
 * Features:
 * - Universal Keyboard Access: Cmd+K (macOS), Ctrl+K (Windows/Linux), or '/'
 * - 222 Verified Records across 7 Categories (Publications, Media, Keynotes, Awards, Profiles, Memberships, Books)
 * - Complete section rendering with verified MDI icons and badges
 * - Category Filter Pills with counts and MDI icons
 * - Real-Time Fuzzy Filtering and Match Highlighting
 * - Arrow-Key Navigation (↑/↓), Enter to open, Esc to close
 * - Direct 1-Click Navigation (Outbound in new tab, internal in-page)
 */

(function () {
  'use strict';

  var omnisearchRecords = [];
  var isLoaded = false;
  var currentCategory = 'all';
  var currentQuery = '';
  var selectedIndex = 0;
  var filteredRecords = [];

  var CATEGORIES = [
    { key: 'all', label: 'All', count: 222, icon: 'mdi-view-grid' },
    { key: 'publications', label: 'Publications & Patents', count: 27, icon: 'mdi-certificate' },
    { key: 'media', label: 'Media Features', count: 44, icon: 'mdi-newspaper' },
    { key: 'keynotes', label: 'Speaking & Keynotes', count: 33, icon: 'mdi-microphone' },
    { key: 'awards', label: 'Awards & Honors', count: 27, icon: 'mdi-trophy-award' },
    { key: 'profiles', label: 'Verified Profiles', count: 57, icon: 'mdi-account-check' },
    { key: 'memberships', label: 'Memberships & Fellowships', count: 26, icon: 'mdi-shield-account' },
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

  // Build Modal Markup
  function createModalDOM() {
    if (document.getElementById('hvOmnisearchModal')) return;

    var modal = document.createElement('div');
    modal.id = 'hvOmnisearchModal';
    modal.setAttribute('role', 'dialog');
    modal.setAttribute('aria-modal', 'true');
    modal.setAttribute('aria-label', 'Search Portfolio');

    var pillsHtml = CATEGORIES.map(function (c) {
      return (
        '<button type="button" class="hv-filter-pill' + (c.key === 'all' ? ' active' : '') + '" data-cat="' + c.key + '">' +
        '<i class="mdi ' + c.icon + ' mr-1"></i>' +
        c.label + ' <span class="badge badge-pill badge-light ml-1" style="font-size:10px; opacity:0.9;">' + c.count + '</span>' +
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
    if (isLoaded && omnisearchRecords.length > 0) {
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

  // Filter & Score Records
  function filterRecords() {
    var query = currentQuery.toLowerCase();
    var cat = currentCategory;

    var list = omnisearchRecords;
    if (cat !== 'all') {
      list = list.filter(function (r) {
        return r.category_pill === cat;
      });
    }

    // When query is empty, show the entire category or all records grouped by section!
    if (!query) {
      filteredRecords = list;
      return;
    }

    var tokens = query.split(/\s+/).filter(Boolean);
    var scored = [];

    for (var i = 0; i < list.length; i++) {
      var r = list[i];
      var titleLower = (r.title || '').toLowerCase();
      var kwLower = (r.keywords || '').toLowerCase();
      var subLower = (r.subtitle || '').toLowerCase();
      var descLower = (r.description || '').toLowerCase();

      var score = 0;
      var matchesAll = true;

      for (var t = 0; t < tokens.length; t++) {
        var tok = tokens[t];
        if (titleLower.indexOf(tok) !== -1) {
          score += 20;
          if (titleLower.startsWith(tok)) score += 10;
        } else if (subLower.indexOf(tok) !== -1) {
          score += 10;
        } else if (kwLower.indexOf(tok) !== -1) {
          score += 6;
        } else if (descLower.indexOf(tok) !== -1) {
          score += 3;
        } else {
          matchesAll = false;
          break;
        }
      }

      // Exact special matches: e.g. patent numbers, specific names
      if (query.indexOf('555747') !== -1 && (titleLower.indexOf('555747') !== -1 || kwLower.indexOf('555747') !== -1)) score += 60;
      if (query.indexOf('606481') !== -1 && (titleLower.indexOf('606481') !== -1 || kwLower.indexOf('606481') !== -1)) score += 60;
      if (query.indexOf('bcs') !== -1 && (titleLower.indexOf('bcs') !== -1 || kwLower.indexOf('bcs') !== -1)) score += 50;

      if (matchesAll) {
        scored.push({ record: r, score: score });
      }
    }

    scored.sort(function (a, b) {
      return b.score - a.score;
    });

    filteredRecords = scored.map(function (s) { return s.record; });
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
        return '<button type="button" class="hv-suggest-chip" data-query="' + sq + '"><i class="mdi mdi-magnify mr-1"></i> ' + sq + '</button>';
      }).join('');

      container.innerHTML =
        '<div class="hv-omnisearch-empty">' +
          '<div class="hv-empty-icon"><i class="mdi mdi-text-search"></i></div>' +
          '<div class="hv-empty-title">No matching records found for "' + escapeHtml(currentQuery) + '"</div>' +
          '<div class="hv-empty-desc">Try searching by patent number (555747, 606481), research topic (Agentic AI, Clean Attacks), book title, or fellowship (BCS Fellow).</div>' +
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
        var catCount = omnisearchRecords.filter(function (x) { return x.category === r.category; }).length;
        html += '<div class="hv-group-header">' +
                  '<span><i class="mdi ' + (r.icon || 'mdi-folder') + ' mr-1"></i> ' + r.category + '</span>' +
                  '<span class="badge badge-light border" style="font-size:10.5px;">' + catCount + ' Records</span>' +
                '</div>';
      }

      var iconClass = r.icon || 'mdi-file-document';
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
      var activeLabel = '222 Verified Records Indexed';
      if (currentCategory !== 'all') {
        var matchedCat = CATEGORIES.find(function (c) { return c.key === currentCategory; });
        activeLabel = (matchedCat ? matchedCat.label : currentCategory) + ' (' + filteredRecords.length + ' records)';
      } else if (currentQuery) {
        activeLabel = filteredRecords.length + ' matching record' + (filteredRecords.length === 1 ? '' : 's');
      }
      footerMeta.innerHTML = '<i class="mdi mdi-check-circle-outline text-success mr-1"></i> ' + activeLabel;
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
      // ignore
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
