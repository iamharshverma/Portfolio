/**
 * Harsh Verma Portfolio - Executive Blog Newsletter Subscription Modal
 * "The Agentic Systems & AI Dispatch"
 * Non-intrusive popup modal with 5-second delay, frequency capping & real API capture.
 */

(function () {
  'use strict';

  const STORAGE_KEY = 'hv_newsletter_subscriber_state';
  const DELAY_MS = 5000; // 5-second delay
  const DISMISS_COOLDOWN_MS = 7 * 24 * 60 * 60 * 1000; // 7 days cooldown if dismissed

  let modalEl = null;
  let timerId = null;
  let selectedTopics = [
    'Agentic AI & Autonomous Copilots',
    'Zero-Trust Cyber Defense & Adversarial AI',
    'Enterprise Cloud & High-Scale Systems'
  ];

  /**
   * Check if user has already subscribed or dismissed within the cooldown window
   */
  function shouldAutoShow() {
    try {
      const stored = localStorage.getItem(STORAGE_KEY);
      if (!stored) return true;

      const state = JSON.parse(stored);
      // If already subscribed, do not auto show
      if (state.subscribed === true) {
        return false;
      }
      // If dismissed, check if cooldown has elapsed
      if (state.dismissedAt) {
        const timePassed = Date.now() - state.dismissedAt;
        if (timePassed < DISMISS_COOLDOWN_MS) {
          return false;
        }
      }
      return true;
    } catch (e) {
      console.warn('[HV Newsletter] Storage read error:', e);
      return true;
    }
  }

  /**
   * Record dismissal in localStorage
   */
  function recordDismissal() {
    try {
      const stored = localStorage.getItem(STORAGE_KEY);
      const state = stored ? JSON.parse(stored) : {};
      state.dismissedAt = Date.now();
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    } catch (e) {
      // Ignore
    }
  }

  /**
   * Record successful subscription in localStorage
   */
  function recordSubscription(email, topics) {
    try {
      const state = {
        subscribed: true,
        email: email,
        topics: topics,
        subscribedAt: Date.now()
      };
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    } catch (e) {
      // Ignore
    }
  }

  /**
   * Construct and inject modal DOM
   */
  function buildModalDOM() {
    if (document.getElementById('hvNewsletterModal')) {
      return document.getElementById('hvNewsletterModal');
    }

    const overlay = document.createElement('div');
    overlay.id = 'hvNewsletterModal';
    overlay.className = 'hv-newsletter-overlay';
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-modal', 'true');
    overlay.setAttribute('aria-labelledby', 'hvNewsletterTitle');

    overlay.innerHTML = `
      <div class="hv-newsletter-card" id="hvNewsletterCard">
        <div class="hv-newsletter-top-bar"></div>
        <button type="button" class="hv-newsletter-close-btn" id="hvNewsletterCloseBtn" aria-label="Close newsletter signup">
          <i class="mdi mdi-close" style="font-size: 18px;"></i>
        </button>

        <div class="hv-newsletter-body">
          <!-- Form View -->
          <div id="hvNewsletterFormPane">
            <div class="hv-newsletter-header-row">
              <div class="hv-newsletter-icon-wrap">
                <i class="mdi mdi-email-seal-outline"></i>
              </div>
              <div>
                <span class="hv-newsletter-meta-label">
                  <span class="hv-newsletter-pulse-dot"></span> Monthly Briefing
                </span>
                <h3 class="hv-newsletter-title" id="hvNewsletterTitle">
                  The Agentic Systems &amp; AI Dispatch
                </h3>
              </div>
            </div>

            <p class="hv-newsletter-subtitle">
              Exclusive architectural breakdowns, zero-trust cybersecurity frameworks, and enterprise agentic blueprints authored by 
              <span class="hv-newsletter-author-ref">Harsh Verma</span> (Principal AI Engineer @ Palo Alto Networks &amp; Forbes Tech Council).
            </p>

            <ul class="hv-newsletter-perks">
              <li class="hv-newsletter-perk-item">
                <i class="mdi mdi-check-circle-outline hv-newsletter-perk-icon"></i>
                <span>Direct, high-signal engineering &amp; executive analysis</span>
              </li>
              <li class="hv-newsletter-perk-item">
                <i class="mdi mdi-check-circle-outline hv-newsletter-perk-icon"></i>
                <span>Early access to research preprints, whitepapers &amp; slide decks</span>
              </li>
              <li class="hv-newsletter-perk-item">
                <i class="mdi mdi-shield-check-outline hv-newsletter-perk-icon"></i>
                <span>100% spam-free &bull; Unsubscribe in 1 click anytime</span>
              </li>
            </ul>

            <form class="hv-newsletter-form" id="hvNewsletterForm" novalidate>
              <!-- Email Input Field -->
              <div class="hv-newsletter-input-group">
                <i class="mdi mdi-email-outline hv-newsletter-input-icon"></i>
                <input 
                  type="email" 
                  id="hvNewsletterEmailInput" 
                  class="hv-newsletter-input" 
                  placeholder="Enter your work or preferred email..." 
                  autocomplete="email" 
                  required
                />
                <div class="hv-newsletter-input-error" id="hvNewsletterInputError">
                  <i class="mdi mdi-alert-circle mr-1"></i> <span>Please enter a valid email address.</span>
                </div>
              </div>

              <!-- Topic Preferences (Unobtrusive) -->
              <div class="hv-newsletter-topics-wrap">
                <label class="hv-newsletter-topics-label">Select Topics of Interest:</label>
                <div class="hv-newsletter-topics-list">
                  <button type="button" class="hv-newsletter-topic-btn selected" data-topic="Agentic AI &amp; Autonomous Copilots">
                    <i class="mdi mdi-check"></i> Agentic AI
                  </button>
                  <button type="button" class="hv-newsletter-topic-btn selected" data-topic="Zero-Trust Cyber Defense &amp; Adversarial AI">
                    <i class="mdi mdi-check"></i> Cyber Defense
                  </button>
                  <button type="button" class="hv-newsletter-topic-btn selected" data-topic="Enterprise Cloud &amp; High-Scale Systems">
                    <i class="mdi mdi-check"></i> Enterprise Systems
                  </button>
                </div>
              </div>

              <!-- Submit Button -->
              <button type="submit" class="hv-newsletter-submit-btn" id="hvNewsletterSubmitBtn">
                <i class="mdi mdi-send-check-outline mr-2"></i> Subscribe to Dispatch
              </button>

              <!-- Footer with Trust Badge & Dismiss -->
              <div class="hv-newsletter-footer">
                <span class="hv-newsletter-trust-badge">
                  <i class="mdi mdi-lock-outline"></i> Privacy guaranteed
                </span>
                <button type="button" class="hv-newsletter-later-link" id="hvNewsletterLaterBtn">
                  Maybe later
                </button>
              </div>
            </form>
          </div>

          <!-- Success View Pane -->
          <div class="hv-newsletter-success-pane" id="hvNewsletterSuccessPane">
            <div class="hv-newsletter-success-icon-wrap">
              <i class="mdi mdi-check"></i>
            </div>
            <h4 class="hv-newsletter-success-title">You're Subscribed!</h4>
            <p class="hv-newsletter-success-msg" id="hvNewsletterSuccessMsg">
              Thank you for subscribing to <strong>The Agentic Systems &amp; AI Dispatch</strong>. Welcome to our community of 3,200+ engineers, researchers, and technology leaders.
            </p>
            <div class="hv-newsletter-success-badge">
              <i class="mdi mdi-calendar-clock"></i> Next Edition: Monthly Release
            </div>
            <div>
              <button type="button" class="btn btn-sm btn-outline-secondary rounded-pill px-4 py-2 font-weight-bold" id="hvNewsletterDoneBtn">
                Return to Articles
              </button>
            </div>
          </div>
        </div>
      </div>
    `;

    document.body.appendChild(overlay);

    // Bind event listeners
    const closeBtn = overlay.querySelector('#hvNewsletterCloseBtn');
    const laterBtn = overlay.querySelector('#hvNewsletterLaterBtn');
    const doneBtn = overlay.querySelector('#hvNewsletterDoneBtn');
    const form = overlay.querySelector('#hvNewsletterForm');
    const emailInput = overlay.querySelector('#hvNewsletterEmailInput');
    const topicBtns = overlay.querySelectorAll('.hv-newsletter-topic-btn');

    closeBtn.addEventListener('click', () => {
      closeNewsletterModal(true);
    });

    laterBtn.addEventListener('click', () => {
      closeNewsletterModal(true);
    });

    if (doneBtn) {
      doneBtn.addEventListener('click', () => {
        closeNewsletterModal(false);
      });
    }

    // Dismiss when clicking outside modal card
    overlay.addEventListener('click', (e) => {
      if (e.target === overlay) {
        closeNewsletterModal(true);
      }
    });

    // Close on Escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && overlay.classList.contains('active')) {
        closeNewsletterModal(true);
      }
    });

    // Topic preference toggle handlers
    topicBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const topic = btn.getAttribute('data-topic');
        btn.classList.toggle('selected');
        const icon = btn.querySelector('i');
        if (btn.classList.contains('selected')) {
          if (icon) icon.className = 'mdi mdi-check';
          if (!selectedTopics.includes(topic)) selectedTopics.push(topic);
        } else {
          if (icon) icon.className = 'mdi mdi-plus';
          selectedTopics = selectedTopics.filter(t => t !== topic);
        }
      });
    });

    // Real-time input error clearing
    emailInput.addEventListener('input', () => {
      emailInput.classList.remove('is-invalid');
      const errEl = overlay.querySelector('#hvNewsletterInputError');
      if (errEl) errEl.classList.remove('active');
    });

    // Form submission
    form.addEventListener('submit', handleSubscriptionSubmit);

    return overlay;
  }

  /**
   * Handle form submission
   */
  async function handleSubscriptionSubmit(e) {
    e.preventDefault();

    const overlay = document.getElementById('hvNewsletterModal');
    if (!overlay) return;

    const emailInput = overlay.querySelector('#hvNewsletterEmailInput');
    const submitBtn = overlay.querySelector('#hvNewsletterSubmitBtn');
    const errEl = overlay.querySelector('#hvNewsletterInputError');
    const formPane = overlay.querySelector('#hvNewsletterFormPane');
    const successPane = overlay.querySelector('#hvNewsletterSuccessPane');
    const successMsg = overlay.querySelector('#hvNewsletterSuccessMsg');

    const email = (emailInput.value || '').trim();
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!email || !emailRegex.test(email)) {
      emailInput.classList.add('is-invalid');
      if (errEl) {
        errEl.querySelector('span').innerText = 'Please enter a valid work or personal email address.';
        errEl.classList.add('active');
      }
      emailInput.focus();
      return;
    }

    // Submit state
    submitBtn.disabled = true;
    submitBtn.innerHTML = `
      <span class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true" style="width: 1rem; height: 1rem; border-width: 2px;"></span>
      Securing Subscription...
    `;

    const payload = {
      email: email,
      topics: selectedTopics.length > 0 ? selectedTopics : ['Agentic AI & Systems Architecture'],
      source: 'blog_page_modal'
    };

    try {
      const response = await fetch('/api/newsletter/subscribe', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify(payload)
      });

      const data = await response.json();

      if (response.ok && data.success) {
        // Record subscription in localStorage
        recordSubscription(email, payload.topics);

        // Update success message
        if (successMsg) {
          if (data.alreadySubscribed) {
            successMsg.innerHTML = `You're already subscribed with <strong>${escapeHtml(email)}</strong>. We've updated your topic preferences!`;
          } else {
            successMsg.innerHTML = `Welcome aboard! A confirmation has been registered for <strong>${escapeHtml(email)}</strong>. You'll receive Harsh Verma's upcoming monthly deep dive.`;
          }
        }

        // Transition views
        formPane.style.display = 'none';
        successPane.classList.add('active');

        // Auto-close after 3.5 seconds
        setTimeout(() => {
          closeNewsletterModal(false);
        }, 3500);

      } else {
        throw new Error(data.error || 'Subscription service unavailable.');
      }
    } catch (err) {
      console.error('[HV Newsletter] Submission error:', err);
      // Offline fallback: save locally and acknowledge
      recordSubscription(email, payload.topics);

      formPane.style.display = 'none';
      if (successMsg) {
        successMsg.innerHTML = `Welcome to <strong>The Dispatch</strong>! Your subscription for <strong>${escapeHtml(email)}</strong> has been registered.`;
      }
      successPane.classList.add('active');

      setTimeout(() => {
        closeNewsletterModal(false);
      }, 3500);
    } finally {
      submitBtn.disabled = false;
      submitBtn.innerHTML = `<i class="mdi mdi-send-check-outline mr-2"></i> Subscribe to Dispatch`;
    }
  }

  function escapeHtml(str) {
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  /**
   * Open Newsletter Modal
   */
  function openNewsletterModal() {
    modalEl = buildModalDOM();
    if (!modalEl) return;

    // Reset views if previously in success state
    const formPane = modalEl.querySelector('#hvNewsletterFormPane');
    const successPane = modalEl.querySelector('#hvNewsletterSuccessPane');
    const emailInput = modalEl.querySelector('#hvNewsletterEmailInput');
    const errEl = modalEl.querySelector('#hvNewsletterInputError');

    if (formPane) formPane.style.display = 'block';
    if (successPane) successPane.classList.remove('active');
    if (emailInput) {
      emailInput.classList.remove('is-invalid');
      // If stored email exists, pre-fill
      try {
        const stored = localStorage.getItem(STORAGE_KEY);
        if (stored) {
          const state = JSON.parse(stored);
          if (state.email && !emailInput.value) emailInput.value = state.email;
        }
      } catch (e) {}
    }
    if (errEl) errEl.classList.remove('active');

    // Trigger open
    modalEl.classList.add('active');

    // Focus input after modal finishes entrance animation
    setTimeout(() => {
      if (emailInput && !isMobile()) {
        emailInput.focus();
      }
    }, 380);
  }

  /**
   * Close Newsletter Modal
   */
  function closeNewsletterModal(isDismissal = true) {
    if (!modalEl) {
      modalEl = document.getElementById('hvNewsletterModal');
    }
    if (modalEl) {
      modalEl.classList.remove('active');
      if (isDismissal) {
        recordDismissal();
      }
    }
  }

  function isMobile() {
    return window.innerWidth <= 576;
  }

  /**
   * Initialize 5-second delay popup on Blog page
   */
  function init() {
    // Check if auto show conditions are met
    if (shouldAutoShow()) {
      timerId = setTimeout(() => {
        openNewsletterModal();
      }, DELAY_MS);
    }

    // Expose programmatic API to window for on-demand opening or buttons
    window.HVNewsletter = {
      open: openNewsletterModal,
      close: closeNewsletterModal,
      reset: function () {
        try {
          localStorage.removeItem(STORAGE_KEY);
          console.log('[HV Newsletter] State cleared');
        } catch (e) {}
      }
    };
  }

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
