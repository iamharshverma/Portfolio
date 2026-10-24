/**
 * Harsh Verma Portfolio - Executive Smooth Scroll-Spy Engine
 * Provides ultra-smooth, responsive section navigation, active highlight tracking,
 * and mobile menu orchestration for the single-page layout.
 */
(function () {
  'use strict';

  function initScrollSpy() {
    var navbar = document.getElementById('navbar') || document.querySelector('.navbar-custom');
    var navCollapse = document.getElementById('navbarCollapse');
    var navLinks = document.querySelectorAll('#mySidenav .nav-link:not(.dropdown-toggle), .navbar-nav .nav-link[href^="#"]');

    if (!navbar || navLinks.length === 0) return;

    var navHeight = 72;
    var isScrollingFromClick = false;
    var scrollTimeout = null;

    // Collect all valid in-page target sections
    var sectionMap = [];
    navLinks.forEach(function (link) {
      var href = link.getAttribute('href');
      if (href && href.startsWith('#') && href.length > 1) {
        try {
          var targetElem = document.querySelector(href);
          if (targetElem) {
            sectionMap.push({
              id: href,
              link: link,
              item: link.closest('.nav-item') || link.parentElement,
              element: targetElem
            });
          }
        } catch (e) {
          // Ignore invalid selector
        }
      }
    });

    if (sectionMap.length === 0) return;

    // Helper: update active state
    function setActiveSection(activeId) {
      sectionMap.forEach(function (sec) {
        if (sec.id === activeId) {
          if (sec.item) sec.item.classList.add('active');
          sec.link.classList.add('active');
          sec.link.setAttribute('aria-current', 'page');
        } else {
          if (sec.item) sec.item.classList.remove('active');
          sec.link.classList.remove('active');
          sec.link.removeAttribute('aria-current');
        }
      });
    }

    // Scroll listener with RAF throttling
    var ticking = false;

    function onScroll() {
      if (isScrollingFromClick) return;

      if (!ticking) {
        window.requestAnimationFrame(function () {
          updateScrollSpy();
          ticking = false;
        });
        ticking = true;
      }
    }

    function updateScrollSpy() {
      var scrollPos = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;
      var windowHeight = window.innerHeight || document.documentElement.clientHeight;
      var docHeight = Math.max(
        document.body.scrollHeight,
        document.documentElement.scrollHeight,
        document.body.offsetHeight,
        document.documentElement.offsetHeight
      );

      // 1. Near the top of the page -> First section (#home)
      if (scrollPos < 100) {
        setActiveSection(sectionMap[0].id);
        return;
      }

      // 2. Near bottom of page -> Last section
      if (scrollPos + windowHeight >= docHeight - 60) {
        setActiveSection(sectionMap[sectionMap.length - 1].id);
        return;
      }

      // 3. Find section currently occupying focal reading viewport
      var currentActiveId = null;
      var focalPoint = scrollPos + navHeight + 80;

      for (var i = 0; i < sectionMap.length; i++) {
        var sec = sectionMap[i];
        var top = sec.element.offsetTop;
        var bottom = top + sec.element.offsetHeight;

        if (focalPoint >= top && focalPoint < bottom) {
          currentActiveId = sec.id;
          break;
        }
      }

      // Fallback: Find closest preceding section
      if (!currentActiveId) {
        for (var j = sectionMap.length - 1; j >= 0; j--) {
          var s = sectionMap[j];
          if (scrollPos + navHeight + 10 >= s.element.offsetTop) {
            currentActiveId = s.id;
            break;
          }
        }
      }

      if (currentActiveId) {
        setActiveSection(currentActiveId);
      }
    }

    // Smooth scroll on click
    navLinks.forEach(function (link) {
      link.addEventListener('click', function (e) {
        var href = this.getAttribute('href');
        if (!href || !href.startsWith('#') || href.length < 2) return;

        var target = document.querySelector(href);
        if (!target) return;

        e.preventDefault();

        // Immediate visual feedback
        setActiveSection(href);
        isScrollingFromClick = true;

        var targetY = target.getBoundingClientRect().top + window.pageYOffset - (navHeight - 8);

        // Smooth scroll
        window.scrollTo({
          top: Math.max(0, targetY),
          behavior: 'smooth'
        });

        // Update URL hash cleanly without jumping
        if (history.pushState) {
          history.pushState(null, null, href);
        } else {
          window.location.hash = href;
        }

        // Close mobile dropdown if open
        if (navCollapse && navCollapse.classList.contains('show')) {
          if (window.jQuery && typeof window.jQuery(navCollapse).collapse === 'function') {
            window.jQuery(navCollapse).collapse('hide');
          } else {
            navCollapse.classList.remove('show');
          }
        }

        // Release scroll lock after scroll finishes
        clearTimeout(scrollTimeout);
        scrollTimeout = setTimeout(function () {
          isScrollingFromClick = false;
          updateScrollSpy();
        }, 850);
      });
    });

    // Listen to scroll events passively
    window.addEventListener('scroll', onScroll, { passive: true });

    // Initial check on load
    updateScrollSpy();

    // Check if initial URL has hash, scroll smoothly to it
    if (window.location.hash) {
      setTimeout(function () {
        var initialTarget = document.querySelector(window.location.hash);
        if (initialTarget) {
          var initY = initialTarget.getBoundingClientRect().top + window.pageYOffset - (navHeight - 8);
          window.scrollTo({
            top: Math.max(0, initY),
            behavior: 'smooth'
          });
          setActiveSection(window.location.hash);
        }
      }, 150);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initScrollSpy);
  } else {
    initScrollSpy();
  }
})();
