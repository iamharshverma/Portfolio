/**
 * Harsh Verma Portfolio - Executive Hero Parallax & Ambient Glow Engine
 * Provides subtle multi-layer 3D parallax tracking on avatar ring and typography,
 * with soft ambient sapphire luminescence on the Principal AI Engineer badge.
 */
(function () {
  'use strict';

  function initHeroParallax() {
    var heroArea = document.getElementById('home') || document.querySelector('.hero-area');
    if (!heroArea) return;

    var avatarRing = heroArea.querySelector('.hero-avatar-ring');
    var badge = heroArea.querySelector('.hero-anim-badge');
    var title = heroArea.querySelector('.hero-anim-title');
    var designation = heroArea.querySelector('.hero-anim-designation');

    if (!avatarRing && !title && !badge) return;

    // Check for reduced motion preference
    var prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // Target and interpolated values
    var targetAvatarX = 0, targetAvatarY = 0, targetAvatarRX = 0, targetAvatarRY = 0;
    var targetTitleX = 0, targetTitleY = 0;
    var targetBadgeX = 0, targetBadgeY = 0;
    var targetSubX = 0, targetSubY = 0;

    var curAvatarX = 0, curAvatarY = 0, curAvatarRX = 0, curAvatarRY = 0;
    var curTitleX = 0, curTitleY = 0;
    var curBadgeX = 0, curBadgeY = 0;
    var curSubX = 0, curSubY = 0;

    var isInteracting = false;
    var rafId = null;

    function updateParallax() {
      if (prefersReducedMotion) {
        if (rafId) {
          cancelAnimationFrame(rafId);
          rafId = null;
        }
        return;
      }

      // Smooth lerp damping factor (0.10 gives an executive, calm liquid response)
      var ease = 0.10;

      curAvatarX += (targetAvatarX - curAvatarX) * ease;
      curAvatarY += (targetAvatarY - curAvatarY) * ease;
      curAvatarRX += (targetAvatarRX - curAvatarRX) * ease;
      curAvatarRY += (targetAvatarRY - curAvatarRY) * ease;

      curTitleX += (targetTitleX - curTitleX) * ease;
      curTitleY += (targetTitleY - curTitleY) * ease;

      curBadgeX += (targetBadgeX - curBadgeX) * ease;
      curBadgeY += (targetBadgeY - curBadgeY) * ease;

      curSubX += (targetSubX - curSubX) * ease;
      curSubY += (targetSubY - curSubY) * ease;

      // Apply CSS variables on hero element
      heroArea.style.setProperty('--hero-avatar-x', curAvatarX.toFixed(2) + 'px');
      heroArea.style.setProperty('--hero-avatar-y', curAvatarY.toFixed(2) + 'px');
      heroArea.style.setProperty('--hero-avatar-rx', curAvatarRX.toFixed(2) + 'deg');
      heroArea.style.setProperty('--hero-avatar-ry', curAvatarRY.toFixed(2) + 'deg');

      heroArea.style.setProperty('--hero-title-x', curTitleX.toFixed(2) + 'px');
      heroArea.style.setProperty('--hero-title-y', curTitleY.toFixed(2) + 'px');

      heroArea.style.setProperty('--hero-badge-x', curBadgeX.toFixed(2) + 'px');
      heroArea.style.setProperty('--hero-badge-y', curBadgeY.toFixed(2) + 'px');

      heroArea.style.setProperty('--hero-subtitle-x', curSubX.toFixed(2) + 'px');
      heroArea.style.setProperty('--hero-subtitle-y', curSubY.toFixed(2) + 'px');

      // Check if motion has decayed close to zero
      var totalDelta = Math.abs(targetAvatarX - curAvatarX) +
                       Math.abs(targetAvatarY - curAvatarY) +
                       Math.abs(targetAvatarRX - curAvatarRX) +
                       Math.abs(targetAvatarRY - curAvatarRY) +
                       Math.abs(targetTitleX - curTitleX) +
                       Math.abs(targetTitleY - curTitleY) +
                       Math.abs(targetBadgeX - curBadgeX) +
                       Math.abs(targetBadgeY - curBadgeY);

      if (isInteracting || totalDelta > 0.05) {
        rafId = requestAnimationFrame(updateParallax);
      } else {
        // Snap to clean resting state
        heroArea.style.removeProperty('--hero-avatar-x');
        heroArea.style.removeProperty('--hero-avatar-y');
        heroArea.style.removeProperty('--hero-avatar-rx');
        heroArea.style.removeProperty('--hero-avatar-ry');
        heroArea.style.removeProperty('--hero-title-x');
        heroArea.style.removeProperty('--hero-title-y');
        heroArea.style.removeProperty('--hero-badge-x');
        heroArea.style.removeProperty('--hero-badge-y');
        heroArea.style.removeProperty('--hero-subtitle-x');
        heroArea.style.removeProperty('--hero-subtitle-y');
        rafId = null;
      }
    }

    function onPointerMove(e) {
      if (prefersReducedMotion) return;

      var rect = heroArea.getBoundingClientRect();
      var clientX = e.clientX;
      var clientY = e.clientY;

      if (clientX === undefined && e.touches && e.touches.length > 0) {
        clientX = e.touches[0].clientX;
        clientY = e.touches[0].clientY;
      }

      if (clientX === undefined) return;

      var relX = clientX - rect.left;
      var relY = clientY - rect.top;

      // Normalized coordinates from -1.0 to +1.0
      var normX = Math.max(-1, Math.min(1, (relX - rect.width / 2) / (rect.width / 2)));
      var normY = Math.max(-1, Math.min(1, (relY - rect.height / 2) / (rect.height / 2)));

      // Subtle executive amplitude
      targetAvatarX = normX * 13;
      targetAvatarY = normY * 10;
      targetAvatarRX = -normY * 7;
      targetAvatarRY = normX * 8.5;

      targetTitleX = normX * 7.5;
      targetTitleY = normY * 5.5;

      targetBadgeX = normX * 11;
      targetBadgeY = normY * 8.5;

      targetSubX = normX * 4.5;
      targetSubY = normY * 3.5;

      if (!isInteracting) {
        isInteracting = true;
        heroArea.classList.add('hero-interacting');
      }

      if (!rafId) {
        rafId = requestAnimationFrame(updateParallax);
      }
    }

    function onPointerLeave() {
      isInteracting = false;
      heroArea.classList.remove('hero-interacting');

      // Coast back smoothly to origin
      targetAvatarX = 0;
      targetAvatarY = 0;
      targetAvatarRX = 0;
      targetAvatarRY = 0;
      targetTitleX = 0;
      targetTitleY = 0;
      targetBadgeX = 0;
      targetBadgeY = 0;
      targetSubX = 0;
      targetSubY = 0;

      if (!rafId) {
        rafId = requestAnimationFrame(updateParallax);
      }
    }

    // Bind event listeners with passive flags
    heroArea.addEventListener('mousemove', onPointerMove, { passive: true });
    heroArea.addEventListener('mouseleave', onPointerLeave, { passive: true });

    // Optional touch support (gentle touch parallax without hijacking scroll)
    heroArea.addEventListener('touchmove', onPointerMove, { passive: true });
    heroArea.addEventListener('touchend', onPointerLeave, { passive: true });
    heroArea.addEventListener('touchcancel', onPointerLeave, { passive: true });

    // Badge specific hover enhancement
    if (badge) {
      badge.addEventListener('mouseenter', function () {
        badge.classList.add('badge-hover-active');
      });
      badge.addEventListener('mouseleave', function () {
        badge.classList.remove('badge-hover-active');
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initHeroParallax);
  } else {
    initHeroParallax();
  }
})();
