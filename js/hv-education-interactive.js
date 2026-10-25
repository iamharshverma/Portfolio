/**
 * Harsh Verma Portfolio - Interactive Education Experience Engine
 * Provides dynamic arrow calculations starting directly from departure spans,
 * interactive hover dynamics, and coursework micro-interactions for academic milestones.
 */
(function () {
  'use strict';

  function updateEducationJourneyArrows() {
    var timeline = document.querySelector('.main-timeline');
    var svg = document.getElementById('edu-journey-svg-overlay');
    if (!timeline || !svg) return;

    var spanStanford = document.querySelector('#end-stanford .edu-end-dock-pill');
    var badgeUtd = document.querySelector('#connector-utd .ext-connector-badge');
    var spanUtd = document.querySelector('#end-utd .edu-end-dock-pill');
    var badgeUtu = document.querySelector('#connector-utu .ext-connector-badge');

    if (!spanStanford || !badgeUtd || !spanUtd || !badgeUtu) return;

    var tRect = timeline.getBoundingClientRect();
    if (tRect.width === 0 || tRect.height === 0) return;

    // Helper to calculate start point from departure span
    function getSpanAnchor(spanEl) {
      var sRect = spanEl.getBoundingClientRect();
      var icon = spanEl.querySelector('i');
      var anchorX, anchorY;
      if (icon) {
        var iRect = icon.getBoundingClientRect();
        anchorX = (iRect.left + iRect.right) / 2 - tRect.left;
        anchorY = iRect.bottom - tRect.top + 2;
      } else {
        anchorX = (sRect.left + sRect.right) / 2 - tRect.left;
        anchorY = sRect.bottom - tRect.top;
      }
      return { x: anchorX, y: anchorY };
    }

    // Helper to calculate target entry point on receiving badge
    function getBadgeAnchor(badgeEl) {
      var bRect = badgeEl.getBoundingClientRect();
      var pulse = badgeEl.querySelector('.ext-badge-pulse');
      var anchorX, anchorY;
      if (pulse) {
        var pRect = pulse.getBoundingClientRect();
        anchorX = (pRect.left + pRect.right) / 2 - tRect.left;
        anchorY = bRect.top - tRect.top - 2;
      } else {
        anchorX = bRect.left + 22 - tRect.left;
        anchorY = bRect.top - tRect.top - 2;
      }
      return { x: anchorX, y: anchorY };
    }

    // --- Journey 1: Stanford Exit Span -> UT Dallas Entrance Badge ---
    var ptStart1 = getSpanAnchor(spanStanford);
    var ptEnd1 = getBadgeAnchor(badgeUtd);

    var deltaY1 = ptEnd1.y - ptStart1.y;
    var curveSpread1 = Math.max(deltaY1 * 0.5, 20);
    var cp1X1 = ptStart1.x;
    var cp1Y1 = ptStart1.y + curveSpread1;
    var cp2X1 = ptEnd1.x;
    var cp2Y1 = ptEnd1.y - curveSpread1;

    var d1 = 'M ' + ptStart1.x.toFixed(1) + ' ' + ptStart1.y.toFixed(1) +
             ' C ' + cp1X1.toFixed(1) + ' ' + cp1Y1.toFixed(1) +
             ', ' + cp2X1.toFixed(1) + ' ' + cp2Y1.toFixed(1) +
             ', ' + ptEnd1.x.toFixed(1) + ' ' + ptEnd1.y.toFixed(1);

    var pts1 = (ptEnd1.x - 3.8).toFixed(1) + ',' + (ptEnd1.y - 6).toFixed(1) + ' ' +
               ptEnd1.x.toFixed(1) + ',' + (ptEnd1.y + 0.5).toFixed(1) + ' ' +
               (ptEnd1.x + 3.8).toFixed(1) + ',' + (ptEnd1.y - 6).toFixed(1);

    var orig1 = document.getElementById('edu-path-1-origin');
    var bg1 = document.getElementById('edu-path-1-bg');
    var track1 = document.getElementById('edu-path-1-track');
    var head1 = document.getElementById('edu-path-1-head');

    if (orig1) {
      orig1.setAttribute('cx', ptStart1.x.toFixed(1));
      orig1.setAttribute('cy', ptStart1.y.toFixed(1));
    }
    if (bg1) bg1.setAttribute('d', d1);
    if (track1) track1.setAttribute('d', d1);
    if (head1) head1.setAttribute('points', pts1);

    // --- Journey 2: UT Dallas Exit Span -> UTU Entrance Badge ---
    var ptStart2 = getSpanAnchor(spanUtd);
    var ptEnd2 = getBadgeAnchor(badgeUtu);

    var deltaY2 = ptEnd2.y - ptStart2.y;
    var curveSpread2 = Math.max(deltaY2 * 0.5, 20);
    var cp1X2 = ptStart2.x;
    var cp1Y2 = ptStart2.y + curveSpread2;
    var cp2X2 = ptEnd2.x;
    var cp2Y2 = ptEnd2.y - curveSpread2;

    var d2 = 'M ' + ptStart2.x.toFixed(1) + ' ' + ptStart2.y.toFixed(1) +
             ' C ' + cp1X2.toFixed(1) + ' ' + cp1Y2.toFixed(1) +
             ', ' + cp2X2.toFixed(1) + ' ' + cp2Y2.toFixed(1) +
             ', ' + ptEnd2.x.toFixed(1) + ' ' + ptEnd2.y.toFixed(1);

    var pts2 = (ptEnd2.x - 3.8).toFixed(1) + ',' + (ptEnd2.y - 6).toFixed(1) + ' ' +
               ptEnd2.x.toFixed(1) + ',' + (ptEnd2.y + 0.5).toFixed(1) + ' ' +
               (ptEnd2.x + 3.8).toFixed(1) + ',' + (ptEnd2.y - 6).toFixed(1);

    var orig2 = document.getElementById('edu-path-2-origin');
    var bg2 = document.getElementById('edu-path-2-bg');
    var track2 = document.getElementById('edu-path-2-track');
    var head2 = document.getElementById('edu-path-2-head');

    if (orig2) {
      orig2.setAttribute('cx', ptStart2.x.toFixed(1));
      orig2.setAttribute('cy', ptStart2.y.toFixed(1));
    }
    if (bg2) bg2.setAttribute('d', d2);
    if (track2) track2.setAttribute('d', d2);
    if (head2) head2.setAttribute('points', pts2);
  }

  function initEducationInteractivity() {
    var eduCards = document.querySelectorAll('.education-interactive-card');
    if (!eduCards.length) return;

    var group1 = document.getElementById('edu-journey-group-1');
    var group2 = document.getElementById('edu-journey-group-2');

    eduCards.forEach(function (card) {
      card.setAttribute('tabindex', '0');
      card.setAttribute('role', 'button');
      card.setAttribute('aria-expanded', 'false');

      // Click interaction to focus/expand
      card.addEventListener('click', function (e) {
        e.preventDefault();
        var wasActive = card.classList.contains('active-degree');

        eduCards.forEach(function (c) {
          c.classList.remove('active-degree');
          c.setAttribute('aria-expanded', 'false');
        });

        if (!wasActive) {
          card.classList.add('active-degree');
          card.setAttribute('aria-expanded', 'true');
          triggerCardRipple(card, e);
        }

        // Recalculate arrows after card size changes
        setTimeout(updateEducationJourneyArrows, 50);
        setTimeout(updateEducationJourneyArrows, 320);
      });

      // Keyboard support (Enter or Space)
      card.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          card.click();
        }
      });

      // Connected Journey Hover Chain Dynamics
      var cardStep = card.getAttribute('data-edu-step');
      card.addEventListener('mouseenter', function () {
        if (cardStep === 'stanford') {
          var next = document.querySelector('[data-edu-step="utd"]');
          if (next) next.classList.add('journey-chain-highlight');
          if (group1) group1.classList.add('journey-active-arrow');
        } else if (cardStep === 'utd') {
          var prev = document.querySelector('[data-edu-step="stanford"]');
          var next = document.querySelector('[data-edu-step="utu"]');
          if (prev) prev.classList.add('journey-chain-highlight');
          if (next) next.classList.add('journey-chain-highlight');
          if (group1) group1.classList.add('journey-active-arrow');
          if (group2) group2.classList.add('journey-active-arrow');
        } else if (cardStep === 'utu') {
          var prev = document.querySelector('[data-edu-step="utd"]');
          if (prev) prev.classList.add('journey-chain-highlight');
          if (group2) group2.classList.add('journey-active-arrow');
        }
      });

      card.addEventListener('mouseleave', function () {
        eduCards.forEach(function (c) {
          c.classList.remove('journey-chain-highlight');
        });
        if (group1) group1.classList.remove('journey-active-arrow');
        if (group2) group2.classList.remove('journey-active-arrow');
      });
    });

    // Bi-directional hover chaining for connectors & docks
    var endStanford = document.getElementById('end-stanford');
    if (endStanford) {
      endStanford.addEventListener('mouseenter', function () {
        if (group1) group1.classList.add('journey-active-arrow');
        var utd = document.querySelector('[data-edu-step="utd"]');
        if (utd) utd.classList.add('journey-chain-highlight');
      });
      endStanford.addEventListener('mouseleave', function () {
        if (group1) group1.classList.remove('journey-active-arrow');
        var utd = document.querySelector('[data-edu-step="utd"]');
        if (utd) utd.classList.remove('journey-chain-highlight');
      });
    }

    var connectorUtd = document.getElementById('connector-utd');
    if (connectorUtd) {
      connectorUtd.addEventListener('mouseenter', function () {
        if (group1) group1.classList.add('journey-active-arrow');
        var stanford = document.querySelector('[data-edu-step="stanford"]');
        if (stanford) stanford.classList.add('journey-chain-highlight');
      });
      connectorUtd.addEventListener('mouseleave', function () {
        if (group1) group1.classList.remove('journey-active-arrow');
        var stanford = document.querySelector('[data-edu-step="stanford"]');
        if (stanford) stanford.classList.remove('journey-chain-highlight');
      });
    }

    var endUtd = document.getElementById('end-utd');
    if (endUtd) {
      endUtd.addEventListener('mouseenter', function () {
        if (group2) group2.classList.add('journey-active-arrow');
        var utu = document.querySelector('[data-edu-step="utu"]');
        if (utu) utu.classList.add('journey-chain-highlight');
      });
      endUtd.addEventListener('mouseleave', function () {
        if (group2) group2.classList.remove('journey-active-arrow');
        var utu = document.querySelector('[data-edu-step="utu"]');
        if (utu) utu.classList.remove('journey-chain-highlight');
      });
    }

    var connectorUtu = document.getElementById('connector-utu');
    if (connectorUtu) {
      connectorUtu.addEventListener('mouseenter', function () {
        if (group2) group2.classList.add('journey-active-arrow');
        var utd = document.querySelector('[data-edu-step="utd"]');
        if (utd) utd.classList.add('journey-chain-highlight');
      });
      connectorUtu.addEventListener('mouseleave', function () {
        if (group2) group2.classList.remove('journey-active-arrow');
        var utd = document.querySelector('[data-edu-step="utd"]');
        if (utd) utd.classList.remove('journey-chain-highlight');
      });
    }

    function triggerCardRipple(card, event) {
      var rect = card.getBoundingClientRect();
      var ripple = document.createElement('span');
      ripple.className = 'edu-click-ripple';
      var size = Math.max(rect.width, rect.height) * 1.5;
      ripple.style.width = size + 'px';
      ripple.style.height = size + 'px';

      var clientX = event.clientX || (rect.left + rect.width / 2);
      var clientY = event.clientY || (rect.top + rect.height / 2);
      ripple.style.left = (clientX - rect.left - size / 2) + 'px';
      ripple.style.top = (clientY - rect.top - size / 2) + 'px';

      card.appendChild(ripple);
      setTimeout(function () {
        if (ripple.parentNode) {
          ripple.parentNode.removeChild(ripple);
        }
      }, 700);
    }

    // Dynamic arrow calculations & responsive listeners
    updateEducationJourneyArrows();

    // Debounced listeners for resize and scroll
    var resizeTimer;
    window.addEventListener('resize', function () {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(updateEducationJourneyArrows, 30);
    });

    window.addEventListener('orientationchange', function () {
      setTimeout(updateEducationJourneyArrows, 100);
    });

    // Multi-phase timers for image rendering & layout settling
    [50, 150, 350, 750, 1500].forEach(function (ms) {
      setTimeout(updateEducationJourneyArrows, ms);
    });

    // ResizeObserver for automatic tracking on DOM mutations
    if (window.ResizeObserver) {
      var ro = new ResizeObserver(function () {
        updateEducationJourneyArrows();
      });
      var timelineEl = document.querySelector('.main-timeline');
      if (timelineEl) ro.observe(timelineEl);
      eduCards.forEach(function (c) { ro.observe(c); });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initEducationInteractivity);
  } else {
    initEducationInteractivity();
  }
  window.addEventListener('load', updateEducationJourneyArrows);
})();
