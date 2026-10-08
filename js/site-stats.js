/**
 * Site Stats Uniform Synchronization Module
 * Author: Harsh Verma Portfolio Systems
 * 
 * Ensures all research paper counters, publication counts, and Google Scholar badges
 * are dynamically and uniformly synchronized across all pages from papers_data.json.
 */
(function(window, document) {
  'use strict';

  var DEFAULT_PAPER_COUNT = 25;
  var cachedPaperCount = DEFAULT_PAPER_COUNT;

  function updateDOMCounters(count) {
    if (!count || typeof count !== 'number' || count <= 0) {
      count = DEFAULT_PAPER_COUNT;
    }
    cachedPaperCount = count;
    var countPlus = count + '+';
    var countRaw = count.toString();

    // 1. Elements with explicit data-stat="papers-count"
    var statElements = document.querySelectorAll('[data-stat="papers-count"]');
    for (var i = 0; i < statElements.length; i++) {
      var el = statElements[i];
      var format = el.getAttribute('data-stat-format');
      el.textContent = (format === 'raw') ? countRaw : countPlus;
    }

    // 2. Elements with data-stat="papers-link"
    var linkElements = document.querySelectorAll('[data-stat="papers-link"]');
    for (var j = 0; j < linkElements.length; j++) {
      var link = linkElements[j];
      var countSpan = link.querySelector('[data-stat="papers-count"]');
      if (countSpan) {
        countSpan.textContent = countPlus;
      } else {
        // If no inner span, safely update link text while keeping icon
        link.innerHTML = '<i class="mdi mdi-school mr-1"></i> View ' + countPlus + ' Published Papers &rarr;';
      }
    }

    // 3. Books hero card specific paper count
    var booksHeroCount = document.getElementById('books-hero-paper-count');
    if (booksHeroCount) {
      booksHeroCount.textContent = countPlus;
    }

    // 4. Any author stat card displaying Research Papers
    var statCards = document.querySelectorAll('.author-stat-card');
    for (var k = 0; k < statCards.length; k++) {
      var card = statCards[k];
      var lbl = card.querySelector('.stat-lbl');
      var val = card.querySelector('.stat-val');
      if (lbl && val && /research\s+papers/i.test(lbl.textContent.trim())) {
        val.textContent = countPlus;
      }
    }

    // 5. Publications page stat box (#scholar-stat-papers)
    var scholarStatBox = document.getElementById('scholar-stat-papers');
    if (scholarStatBox) {
      var numEl = scholarStatBox.querySelector('.scholar-stat-number');
      if (numEl) {
        numEl.textContent = countRaw;
      }
    }

    // 6. Navigation bar Google Scholar links
    var scholarNavLinks = document.querySelectorAll('a.nav-social-btn[href*="scholar.google.com"], a[title*="Google Scholar"]');
    for (var s = 0; s < scholarNavLinks.length; s++) {
      scholarNavLinks[s].setAttribute('title', 'Google Scholar (' + countPlus + ' Papers)');
      scholarNavLinks[s].setAttribute('aria-label', 'Google Scholar (' + countPlus + ' Papers)');
    }

    // 7. Generic paper counters with [data-paper-counter] or .research-papers-counter
    var genericCounters = document.querySelectorAll('[data-paper-counter], .research-papers-counter');
    for (var g = 0; g < genericCounters.length; g++) {
      genericCounters[g].textContent = countPlus;
    }

    // Dispatch custom event for copilot or other reactive components
    try {
      window.dispatchEvent(new CustomEvent('site:papers-count-updated', {
        detail: { count: count, formatted: countPlus }
      }));
    } catch (e) {}
  }

  function fetchAndSyncPapers() {
    // If window.PAPERS_DATA is already injected or available
    if (window.PAPERS_DATA && Array.isArray(window.PAPERS_DATA) && window.PAPERS_DATA.length > 0) {
      updateDOMCounters(window.PAPERS_DATA.length);
      return;
    }

    // Fetch papers_data.json
    fetch('papers_data.json')
      .then(function(res) {
        if (!res.ok) throw new Error('Status ' + res.status);
        return res.json();
      })
      .then(function(data) {
        var count = Array.isArray(data) ? data.length : (data && Array.isArray(data.papers) ? data.papers.length : DEFAULT_PAPER_COUNT);
        updateDOMCounters(count);
      })
      .catch(function() {
        // Fallback to latest known constant
        updateDOMCounters(DEFAULT_PAPER_COUNT);
      });
  }

  // Public API
  window.SiteStats = {
    getPaperCount: function() {
      return cachedPaperCount;
    },
    setPaperCount: function(newCount) {
      var parsed = parseInt(newCount, 10);
      if (!isNaN(parsed) && parsed > 0) {
        updateDOMCounters(parsed);
      }
    },
    sync: fetchAndSyncPapers
  };

  // Run automatically
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', fetchAndSyncPapers);
  } else {
    fetchAndSyncPapers();
  }

  // Allow trigger via event
  window.addEventListener('site:sync-papers', function(e) {
    if (e && e.detail && typeof e.detail.count === 'number') {
      updateDOMCounters(e.detail.count);
    } else {
      fetchAndSyncPapers();
    }
  });

})(typeof window !== 'undefined' ? window : this, typeof document !== 'undefined' ? document : {});
