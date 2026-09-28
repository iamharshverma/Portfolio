/**
 * Dark Mode Manager for Harsh Verma Portfolio
 * Handles theme toggling, persistence, and accessibility.
 * Default theme is Light Mode.
 */

(function () {
  'use strict';

  var THEME_KEY = 'portfolio_theme';

  // Get current stored theme - explicitly defaults to light mode
  function getPreferredTheme() {
    var storedTheme = localStorage.getItem(THEME_KEY);
    if (storedTheme === 'dark') {
      return 'dark';
    }
    // Default mode is light mode
    return 'light';
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

  // Initial application immediately (defaults to light mode)
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
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initThemeToggle);
  } else {
    initThemeToggle();
  }

  // Expose toggle globally if needed
  window.toggleTheme = toggleTheme;
})();
