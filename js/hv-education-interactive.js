/**
 * Harsh Verma Portfolio - Interactive Education Experience Engine
 * Provides interactive hover dynamics, click-to-focus inspection,
 * and coursework micro-interactions for academic milestones.
 */
(function () {
  'use strict';

  function initEducationInteractivity() {
    var eduCards = document.querySelectorAll('.education-interactive-card');
    if (!eduCards.length) return;

    eduCards.forEach(function (card) {
      // Add accessibility attributes
      card.setAttribute('tabindex', '0');
      card.setAttribute('role', 'button');
      card.setAttribute('aria-expanded', 'false');

      // Click interaction to focus/expand
      card.addEventListener('click', function (e) {
        // Prevent default if it is an anchor
        e.preventDefault();

        var wasActive = card.classList.contains('active-degree');

        // Optional: single active mode (uncomment to collapse siblings)
        eduCards.forEach(function (c) {
          c.classList.remove('active-degree');
          c.setAttribute('aria-expanded', 'false');
        });

        if (!wasActive) {
          card.classList.add('active-degree');
          card.setAttribute('aria-expanded', 'true');
          // Visual ripple effect at click coordinates
          triggerCardRipple(card, e);
        }
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
        } else if (cardStep === 'utd') {
          var prev = document.querySelector('[data-edu-step="stanford"]');
          var next = document.querySelector('[data-edu-step="utu"]');
          if (prev) prev.classList.add('journey-chain-highlight');
          if (next) next.classList.add('journey-chain-highlight');
        } else if (cardStep === 'utu') {
          var prev = document.querySelector('[data-edu-step="utd"]');
          if (prev) prev.classList.add('journey-chain-highlight');
        }
      });

      card.addEventListener('mouseleave', function () {
        eduCards.forEach(function (c) {
          c.classList.remove('journey-chain-highlight');
        });
      });

      // Interactive Flow Connector Click Navigation
    });

    // Bi-directional hover chaining for top connectors inside cards
    var connectorUtd = document.getElementById('connector-utd');
    if (connectorUtd) {
      connectorUtd.addEventListener('mouseenter', function () {
        var stanford = document.querySelector('[data-edu-step="stanford"]');
        if (stanford) stanford.classList.add('journey-chain-highlight');
      });
      connectorUtd.addEventListener('mouseleave', function () {
        var stanford = document.querySelector('[data-edu-step="stanford"]');
        if (stanford) stanford.classList.remove('journey-chain-highlight');
      });
    }

    var connectorUtu = document.getElementById('connector-utu');
    if (connectorUtu) {
      connectorUtu.addEventListener('mouseenter', function () {
        var utd = document.querySelector('[data-edu-step="utd"]');
        if (utd) utd.classList.add('journey-chain-highlight');
      });
      connectorUtu.addEventListener('mouseleave', function () {
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
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initEducationInteractivity);
  } else {
    initEducationInteractivity();
  }
})();
