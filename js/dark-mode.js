/**
 * Dark Mode Manager for Harsh Verma Portfolio
 * Handles theme toggling, persistence, and accessibility.
 */

(function () {
  'use strict';

  var THEME_KEY = 'portfolio_theme';

  // Get current stored theme or system preference
  function getPreferredTheme() {
    var storedTheme = localStorage.getItem(THEME_KEY);
    if (storedTheme) {
      return storedTheme;
    }
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches
      ? 'dark'
      : 'light';
  }

  // Apply theme to document (both html and body for full CSS selector compatibility)
  function applyTheme(theme) {
    var isDark = theme === 'dark';
    if (isDark) {
      document.documentElement.classList.add('dark-mode');
      if (document.body) {
        document.body.classList.add('dark-mode');
      }
    } else {
      document.documentElement.classList.remove('dark-mode');
      if (document.body) {
        document.body.classList.remove('dark-mode');
      }
    }

    // Update all theme toggle buttons on the page
    var toggleButtons = document.querySelectorAll('.theme-toggle-btn');
    toggleButtons.forEach(function (btn) {
      btn.setAttribute('aria-label', isDark ? 'Switch to light mode' : 'Switch to dark mode');
      btn.setAttribute('title', isDark ? 'Switch to light mode' : 'Switch to dark mode');
      btn.setAttribute('aria-pressed', isDark ? 'true' : 'false');
    });

    // Dispatch global events so components, canvas, and charts can react
    try {
      var event = new CustomEvent('themeChanged', { detail: { theme: theme, isDark: isDark } });
      window.dispatchEvent(event);
      document.dispatchEvent(event);
    } catch (e) {}
  }

  // Toggle theme handler
  function toggleTheme() {
    var currentIsDark = document.documentElement.classList.contains('dark-mode');
    var newTheme = currentIsDark ? 'light' : 'dark';
    localStorage.setItem(THEME_KEY, newTheme);
    applyTheme(newTheme);
  }

  // Initial application immediately (can also run before DOM is fully parsed)
  var initialTheme = getPreferredTheme();
  applyTheme(initialTheme);

  // Setup event listeners once DOM is ready
  function initThemeToggle() {
    applyTheme(getPreferredTheme());

    document.addEventListener('click', function (event) {
      var target = event.target;
      var toggleBtn = target.closest('.theme-toggle-btn');
      if (toggleBtn) {
        event.preventDefault();
        toggleTheme();
      }
    });

    // Listen to system preference changes if user hasn't chosen manually
    if (window.matchMedia) {
      window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function (e) {
        if (!localStorage.getItem(THEME_KEY)) {
          applyTheme(e.matches ? 'dark' : 'light');
        }
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initThemeToggle);
  } else {
    initThemeToggle();
  }

  // Expose toggle globally if needed
  window.toggleTheme = toggleTheme;
})();
