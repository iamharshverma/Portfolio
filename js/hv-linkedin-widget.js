/**
 * Harsh Verma - LinkedIn Professional Activity Feed Widget Engine
 * Non-Intrusive Layout, Live API Synchronization, Dynamic Topic Filtering & Reactions
 */

(function (window, document) {
  'use strict';

  var STORAGE_LIKES_KEY = 'hv_linkedin_likes_v1';
  var STORAGE_VIEW_KEY = 'hv_linkedin_view_mode';
  var STORAGE_COLLAPSED_KEY = 'hv_linkedin_is_collapsed';

  function getStoredLikes() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_LIKES_KEY) || '{}');
    } catch (e) {
      return {};
    }
  }

  function saveStoredLikes(likes) {
    try {
      localStorage.setItem(STORAGE_LIKES_KEY, JSON.stringify(likes));
    } catch (e) {
      // storage unavailable
    }
  }

  function formatRelativeTime(isoString) {
    if (!isoString) return 'Recently';
    var d = new Date(isoString);
    if (isNaN(d.getTime())) return 'Recently';

    var now = new Date();
    var diffMs = now - d;
    var diffSec = Math.floor(diffMs / 1000);
    var diffMin = Math.floor(diffSec / 60);
    var diffHrs = Math.floor(diffMin / 60);
    var diffDays = Math.floor(diffHrs / 24);

    if (diffSec < 60) return 'Just now';
    if (diffMin < 60) return diffMin + 'm ago';
    if (diffHrs < 24) return diffHrs + 'h ago';
    if (diffDays === 1) return 'Yesterday';
    if (diffDays < 7) return diffDays + 'd ago';
    if (diffDays < 30) return Math.floor(diffDays / 7) + 'w ago';
    return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
  }

  function escapeHtml(str) {
    if (!str) return '';
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  function formatHashtags(text) {
    if (!text) return '';
    return text.replace(/(#[a-zA-Z0-9_]+)/g, '<span class="hv-li-tag">$1</span>');
  }

  // Toast feedback helper
  function notify(msg, isSuccess) {
    // If global page toast exists
    if (window.jQuery && window.jQuery('#socialToast').length) {
      var $t = window.jQuery('#socialToast');
      var $icon = window.jQuery('#toastIcon');
      window.jQuery('#toastTitle').text('LinkedIn Feed');
      window.jQuery('#toastMessage').text(msg);
      $t.css('border-left-color', isSuccess ? '#0a66c2' : '#ef4444');
      $icon.attr('class', isSuccess ? 'mdi mdi-linkedin text-primary' : 'mdi mdi-alert-circle text-danger');
      $t.stop(true, true).fadeIn(200);
      setTimeout(function () {
        $t.fadeOut(300);
      }, 3500);
      return;
    }

    // Fallback mini notification
    var banner = document.getElementById('hv-li-mini-notify');
    if (!banner) {
      banner = document.createElement('div');
      banner.id = 'hv-li-mini-notify';
      banner.style.cssText = 'position:fixed;bottom:24px;right:24px;z-index:99999;background:#0a66c2;color:#fff;padding:10px 18px;border-radius:30px;font-size:13px;font-weight:600;box-shadow:0 8px 24px rgba(0,0,0,0.2);display:flex;align-items:center;gap:8px;transition:all 0.3s ease;transform:translateY(80px);opacity:0;';
      document.body.appendChild(banner);
    }
    banner.innerHTML = '<i class="mdi mdi-linkedin"></i> <span>' + escapeHtml(msg) + '</span>';
    banner.style.transform = 'translateY(0)';
    banner.style.opacity = '1';
    clearTimeout(banner._timer);
    banner._timer = setTimeout(function () {
      banner.style.transform = 'translateY(80px)';
      banner.style.opacity = '0';
    }, 3500);
  }

  function LinkedInWidget(containerEl, options) {
    this.container = typeof containerEl === 'string' ? document.querySelector(containerEl) : containerEl;
    if (!this.container) return;

    var attrCompact = this.container.getAttribute('data-compact');
    var attrCollapsed = this.container.getAttribute('data-collapsed');
    var initialCompact = attrCompact !== null ? (attrCompact === 'true') : (localStorage.getItem(STORAGE_VIEW_KEY) === 'compact');
    var initialCollapsed = attrCollapsed !== null ? (attrCollapsed === 'true') : (localStorage.getItem(STORAGE_COLLAPSED_KEY) === 'true');

    this.options = Object.assign({
      endpoint: '/api/social/linkedin-feed',
      compactMode: initialCompact,
      isCollapsed: initialCollapsed,
      maxInitialDisplay: 8,
      defaultCategory: 'all'
    }, options);

    this.activities = [];
    this.profile = null;
    this.activeCategory = this.options.defaultCategory;
    this.isSyncing = false;
    this.likedMap = getStoredLikes();

    this.init();
  }

  LinkedInWidget.prototype.init = function () {
    this.renderSkeleton();
    this.fetchData();
  };

  LinkedInWidget.prototype.fetchData = function (isRefresh) {
    var self = this;
    self.isSyncing = true;
    self.updateSyncButtonState();

    var url = self.options.endpoint + (isRefresh ? '?refresh=1' : '');

    fetch(url)
      .then(function (res) {
        if (!res.ok) throw new Error('Network error ' + res.status);
        return res.json();
      })
      .then(function (data) {
        self.isSyncing = false;
        self.updateSyncButtonState();

        if (data && data.success) {
          self.activities = data.activities || [];
          self.profile = data.profile || {
            name: 'Harsh Verma',
            headline: 'Principal AI Architect @ Palo Alto Networks | Forbes Technology Council',
            followersDisplay: '16.6K+',
            profileUrl: 'https://www.linkedin.com/in/harshverma59/'
          };
          self.render();
          if (isRefresh) {
            notify('Successfully pulled latest LinkedIn professional activity!', true);
          }
        } else {
          throw new Error((data && data.error) || 'Failed to parse activity data');
        }
      })
      .catch(function (err) {
        console.warn('[LinkedIn Widget] API fetch notice:', err.message);
        self.isSyncing = false;
        self.updateSyncButtonState();
        self.renderFallback();
      });
  };

  LinkedInWidget.prototype.updateSyncButtonState = function () {
    var syncBtn = this.container.querySelector('.hv-li-btn-sync');
    if (!syncBtn) return;
    if (this.isSyncing) {
      syncBtn.classList.add('is-syncing');
      syncBtn.setAttribute('disabled', 'disabled');
      syncBtn.innerHTML = '<i class="mdi mdi-refresh"></i> <span>Syncing...</span>';
    } else {
      syncBtn.classList.remove('is-syncing');
      syncBtn.removeAttribute('disabled');
      syncBtn.innerHTML = '<i class="mdi mdi-refresh"></i> <span>Pull Latest</span>';
    }
  };

  LinkedInWidget.prototype.renderSkeleton = function () {
    this.container.innerHTML = `
      <div class="hv-linkedin-widget">
        <div class="hv-li-accent-stripe"></div>
        <div class="hv-li-header">
          <div class="hv-li-brand-wrap">
            <div class="hv-li-logo-icon">
              <i class="mdi mdi-linkedin"></i>
              <span class="hv-li-live-pulse" title="Live LinkedIn Activity Stream"></span>
            </div>
            <div class="hv-li-title-box">
              <div class="hv-li-main-title">
                <span>LinkedIn Professional Activity</span>
                <i class="mdi mdi-check-decagram hv-li-verified-badge" title="Verified Creator"></i>
              </div>
              <p class="hv-li-sub-title">Connecting to live feed...</p>
            </div>
          </div>
        </div>
        <div class="hv-li-stream">
          <div class="hv-li-card">
            <div class="d-flex align-items-center mb-3">
              <div class="hv-li-skeleton" style="width: 40px; height: 40px; border-radius: 50%;"></div>
              <div class="ml-2 flex-grow-1">
                <div class="hv-li-skeleton" style="width: 140px; height: 14px; margin-bottom: 6px;"></div>
                <div class="hv-li-skeleton" style="width: 220px; height: 10px;"></div>
              </div>
            </div>
            <div class="hv-li-skeleton" style="width: 90%; height: 14px; margin-bottom: 8px;"></div>
            <div class="hv-li-skeleton" style="width: 75%; height: 14px; margin-bottom: 8px;"></div>
            <div class="hv-li-skeleton" style="width: 60%; height: 14px;"></div>
          </div>
        </div>
      </div>
    `;
  };

  LinkedInWidget.prototype.render = function () {
    var self = this;
    var profile = self.profile || {};
    var followers = profile.followersDisplay || '16.6K+';
    var isCompact = self.options.compactMode;
    var isCollapsed = self.options.isCollapsed;

    var filtered = self.activities.filter(function (item) {
      if (self.activeCategory === 'all') return true;
      var cat = (item.routineCategory || '').toLowerCase();
      var tags = Array.isArray(item.tags) ? item.tags.join(' ').toLowerCase() : '';
      var activeCat = self.activeCategory.toLowerCase();
      return cat.indexOf(activeCat) !== -1 || tags.indexOf(activeCat) !== -1;
    });

    var widgetHtml = `
      <div class="hv-linkedin-widget ${isCompact ? 'mode-compact' : ''}" id="hvLiWidgetCard">
        <div class="hv-li-accent-stripe"></div>
        
        <!-- Header -->
        <div class="hv-li-header">
          <div class="hv-li-brand-wrap">
            <div class="hv-li-logo-icon">
              <i class="mdi mdi-linkedin"></i>
              <span class="hv-li-live-pulse" title="Live Feed Active"></span>
            </div>
            <div class="hv-li-title-box">
              <div class="hv-li-main-title">
                <span>LinkedIn Professional Activity</span>
                <i class="mdi mdi-check-decagram hv-li-verified-badge" title="Verified Creator"></i>
              </div>
              <p class="hv-li-sub-title">
                <span>${profile.name || 'Harsh Verma'}</span>
                <span class="hv-li-stat-dot"></span>
                <span>${followers} Followers</span>
                <span class="hv-li-stat-dot"></span>
                <span class="text-success font-weight-bold">Live Synced</span>
              </p>
            </div>
          </div>
          <div class="hv-li-actions">
            <button type="button" class="hv-li-btn-sync" title="Pull latest activity from LinkedIn">
              <i class="mdi mdi-refresh"></i> <span>Pull Latest</span>
            </button>
            <button type="button" class="hv-li-btn-toggle-view" title="${isCompact ? 'Switch to Standard Cards View' : 'Switch to Compact Digest View'}">
              <i class="mdi ${isCompact ? 'mdi-view-agenda-outline' : 'mdi-format-list-bulleted'}"></i>
            </button>
            <button type="button" class="hv-li-btn-toggle-view hv-li-btn-collapse" title="${isCollapsed ? 'Expand Widget' : 'Minimize Widget'}">
              <i class="mdi ${isCollapsed ? 'mdi-chevron-down' : 'mdi-chevron-up'}"></i>
            </button>
            <a href="${profile.profileUrl || 'https://www.linkedin.com/in/harshverma59/'}" target="_blank" rel="noopener noreferrer" class="hv-li-btn-follow">
              <i class="mdi mdi-account-plus"></i> <span>Follow</span>
            </a>
          </div>
        </div>

        <!-- Collapsed Summary Ticker (shown when minimized) -->
        <div class="hv-li-collapsed-bar" style="display: ${isCollapsed ? 'flex' : 'none'};">
          <div class="hv-li-collapsed-text">
            <span class="hv-li-collapsed-badge">Latest Update</span>
            <span>${escapeHtml((self.activities[0] && self.activities[0].title) || 'Exploring Agentic AI & Autonomous Cyber Defense')}</span>
          </div>
          <span class="text-primary small font-weight-bold">Click to Expand <i class="mdi mdi-chevron-down"></i></span>
        </div>

        <!-- Category Filter Pills Bar (hidden when minimized) -->
        <div class="hv-li-body-wrapper" style="display: ${isCollapsed ? 'none' : 'block'};">
          <div class="hv-li-filter-bar">
            <div class="hv-li-filter-pill ${self.activeCategory === 'all' ? 'is-active' : ''}" data-cat="all">All Activity (${self.activities.length})</div>
            <div class="hv-li-filter-pill ${self.activeCategory === 'forbes' ? 'is-active' : ''}" data-cat="forbes">Forbes &amp; Leadership</div>
            <div class="hv-li-filter-pill ${self.activeCategory === 'ai' ? 'is-active' : ''}" data-cat="ai">Agentic AI &amp; Systems</div>
            <div class="hv-li-filter-pill ${self.activeCategory === 'cyber' ? 'is-active' : ''}" data-cat="cyber">Zero-Trust Cyber Defense</div>
            <div class="hv-li-filter-pill ${self.activeCategory === 'book' ? 'is-active' : ''}" data-cat="book">Books &amp; Keynotes</div>
          </div>

          <!-- Activity Cards Stream -->
          <div class="hv-li-stream">
            ${filtered.length === 0 ? `
              <div class="text-center py-4 text-muted">
                <i class="mdi mdi-post-outline" style="font-size: 32px;"></i>
                <p class="small mb-0 mt-2">No activity found under this category filter.</p>
              </div>
            ` : filtered.map(function (post) {
              return self.renderCardHtml(post);
            }).join('')}
          </div>

          <!-- Footer Status -->
          <div class="hv-li-footer">
            <div class="hv-li-status-line">
              <span class="hv-li-status-dot"></span>
              <span>Direct feed from Palo Alto Networks &amp; Forbes Council verified author</span>
            </div>
            <a href="https://www.linkedin.com/in/harshverma59/recent-activity/all/" target="_blank" rel="noopener noreferrer" class="hv-li-footer-link">
              View all on LinkedIn <i class="mdi mdi-open-in-new"></i>
            </a>
          </div>
        </div>
      </div>
    `;

    self.container.innerHTML = widgetHtml;
    self.attachEventListeners();
  };

  LinkedInWidget.prototype.renderCardHtml = function (post) {
    var self = this;
    var relativeTime = formatRelativeTime(post.publishedAt);
    var avatar = post.authorAvatar || 'images/harsh/Harsh_portfolio_pic.png';
    var authorTitle = post.authorTitle || 'Principal AI Architect • Forbes Technology Council • IEEE Senior Member';
    var title = post.title ? `<div class="hv-li-card-title">${escapeHtml(post.title)}</div>` : '';
    var rawContent = post.content || '';
    var isLong = rawContent.length > 210;
    var contentHtml = formatHashtags(escapeHtml(rawContent));
    var isLiked = !!self.likedMap[post.id];
    var likesCount = (post.likes || 0) + (isLiked ? 1 : 0);

    var mediaHtml = '';
    if (post.mediaUrl) {
      mediaHtml = `
        <div class="hv-li-media-preview">
          <img src="${post.mediaUrl}" alt="LinkedIn post visual" class="hv-li-media-img" loading="lazy" onerror="this.parentElement.style.display='none'" />
        </div>
      `;
    }

    var categoryBadge = post.routineCategory ? `
      <span class="hv-li-category-tag">
        <i class="mdi mdi-tag-outline mr-1"></i>${escapeHtml(post.routineCategory)}
      </span>
    ` : '';

    return `
      <article class="hv-li-card" id="li-card-${post.id}" data-id="${post.id}">
        <div class="hv-li-card-author-row">
          <div class="hv-li-author-meta">
            <img src="${avatar}" alt="${post.authorName || 'Harsh Verma'}" class="hv-li-author-avatar" />
            <div class="min-w-0">
              <div class="hv-li-author-name">
                <span>${post.authorName || 'Harsh Verma'}</span>
                <i class="mdi mdi-check-decagram hv-li-verified-badge" title="Verified Professional Profile"></i>
              </div>
              <div class="hv-li-author-subline text-truncate" style="max-width: 280px;" title="${escapeHtml(authorTitle)}">
                ${escapeHtml(authorTitle)}
              </div>
            </div>
          </div>
          <div class="d-flex align-items-center gap-2">
            ${categoryBadge}
            <span class="small text-muted" style="font-size: 11px;">${relativeTime}</span>
          </div>
        </div>

        ${title}

        <div class="hv-li-card-body is-clamped" id="li-body-${post.id}">${contentHtml}</div>
        ${isLong ? `<button type="button" class="hv-li-btn-expand-text" data-target="#li-body-${post.id}">...see more</button>` : ''}

        ${mediaHtml}

        <div class="hv-li-card-footer">
          <div class="hv-li-reactions-row">
            <button type="button" class="hv-li-reaction-btn ${isLiked ? 'has-liked' : ''}" data-action="like" data-id="${post.id}" title="Insightful / Like">
              <i class="mdi ${isLiked ? 'mdi-heart' : 'mdi-heart-outline'}"></i>
              <span class="hv-li-like-count">${likesCount}</span>
            </button>
            <span class="hv-li-reaction-btn" title="Comments">
              <i class="mdi mdi-comment-outline"></i> <span>${post.comments || 0}</span>
            </span>
            <span class="hv-li-reaction-btn" title="Reposts">
              <i class="mdi mdi-repeat"></i> <span>${post.shares || 0}</span>
            </span>
          </div>

          <div>
            <a href="${post.postUrl || 'https://www.linkedin.com/in/harshverma59/'}" target="_blank" rel="noopener noreferrer" class="hv-li-btn-view-post">
              <span>View on LinkedIn</span> <i class="mdi mdi-arrow-top-right"></i>
            </a>
          </div>
        </div>
      </article>
    `;
  };

  LinkedInWidget.prototype.attachEventListeners = function () {
    var self = this;
    var container = self.container;

    // Pull Latest / Sync button
    var syncBtn = container.querySelector('.hv-li-btn-sync');
    if (syncBtn) {
      syncBtn.addEventListener('click', function (e) {
        e.preventDefault();
        self.fetchData(true);
      });
    }

    // Toggle Compact vs Standard view
    var viewBtn = container.querySelector('.hv-li-btn-toggle-view:not(.hv-li-btn-collapse)');
    if (viewBtn) {
      viewBtn.addEventListener('click', function (e) {
        e.preventDefault();
        self.options.compactMode = !self.options.compactMode;
        localStorage.setItem(STORAGE_VIEW_KEY, self.options.compactMode ? 'compact' : 'standard');
        self.render();
      });
    }

    // Toggle Collapse / Expand
    var collapseBtn = container.querySelector('.hv-li-btn-collapse');
    var collapsedBar = container.querySelector('.hv-li-collapsed-bar');
    var toggleCollapse = function (e) {
      e.preventDefault();
      self.options.isCollapsed = !self.options.isCollapsed;
      localStorage.setItem(STORAGE_COLLAPSED_KEY, self.options.isCollapsed ? 'true' : 'false');
      self.render();
    };

    if (collapseBtn) collapseBtn.addEventListener('click', toggleCollapse);
    if (collapsedBar) collapsedBar.addEventListener('click', toggleCollapse);

    // Category pills filter
    var pills = container.querySelectorAll('.hv-li-filter-pill');
    pills.forEach(function (pill) {
      pill.addEventListener('click', function () {
        var cat = pill.getAttribute('data-cat') || 'all';
        self.activeCategory = cat;
        self.render();
      });
    });

    // Expand body text toggle
    var expandBtns = container.querySelectorAll('.hv-li-btn-expand-text');
    expandBtns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var targetSel = btn.getAttribute('data-target');
        var bodyEl = container.querySelector(targetSel);
        if (!bodyEl) return;
        var isClamped = bodyEl.classList.contains('is-clamped');
        if (isClamped) {
          bodyEl.classList.remove('is-clamped');
          btn.textContent = 'show less';
        } else {
          bodyEl.classList.add('is-clamped');
          btn.textContent = '...see more';
        }
      });
    });

    // Like button toggle
    var likeBtns = container.querySelectorAll('[data-action="like"]');
    likeBtns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var postId = btn.getAttribute('data-id');
        if (!postId) return;

        var already = !!self.likedMap[postId];
        if (already) {
          delete self.likedMap[postId];
          btn.classList.remove('has-liked');
          btn.querySelector('i').className = 'mdi mdi-heart-outline';
        } else {
          self.likedMap[postId] = true;
          btn.classList.add('has-liked');
          btn.querySelector('i').className = 'mdi mdi-heart';
        }
        saveStoredLikes(self.likedMap);

        // Update count visually
        var postObj = self.activities.find(function (p) { return p.id === postId; });
        var base = (postObj && postObj.likes) || 0;
        var countSpan = btn.querySelector('.hv-li-like-count');
        if (countSpan) {
          countSpan.textContent = base + (self.likedMap[postId] ? 1 : 0);
        }
      });
    });
  };

  LinkedInWidget.prototype.renderFallback = function () {
    var self = this;
    // Render graceful offline fallback with curated activities
    self.activities = [
      {
        id: "post-li-forbes",
        platform: "linkedin",
        authorName: "Harsh Verma",
        authorHandle: "@harshverma59",
        authorTitle: "Principal AI Architect • Forbes Technology Council • IEEE Senior Member",
        authorAvatar: "images/harsh/Harsh_portfolio_pic.png",
        postUrl: "https://www.linkedin.com/feed/update/urn:li:activity:7462604082080276482/",
        publishedAt: "2026-09-03T18:00:00Z",
        routineCategory: "Forbes & Executive Leadership",
        title: "The Intelligence Per Dollar Metric: How Leaders Measure AI Success",
        content: "As AI moves from experimentation to enterprise-scale deployment, the conversation is shifting from: “How powerful is the model?” to “How much real business intelligence are we generating per dollar spent?”. The topic I believe will define the next era of enterprise AI adoption is: “The Intelligence Per Dollar Metric: How Influential Leaders Measure AI Success.” As an Official Member of Forbes Technology Council, exploring how engineering is being redefined in the AI era.",
        tags: ["#AI", "#EngineeringLeadership", "#ForbesTechnologyCouncil", "#AgenticAI"],
        likes: 348,
        comments: 42,
        shares: 29,
        mediaType: "image",
        mediaUrl: "images/blog/01.jpg"
      },
      {
        id: "post-li-zero-trust-agents",
        platform: "linkedin",
        authorName: "Harsh Verma",
        authorHandle: "@harshverma59",
        authorTitle: "Principal AI Architect • Forbes Technology Council • IEEE Senior Member",
        authorAvatar: "images/harsh/Harsh_portfolio_pic.png",
        postUrl: "https://www.linkedin.com/in/harshverma59/",
        publishedAt: "2026-09-18T15:20:00Z",
        routineCategory: "Enterprise AI & Zero-Trust Defense",
        title: "The Death of Static Authentication: Why Identity Isn't Enough for Autonomous AI Agents",
        content: "Traditional IAM verifies 'who is acting', but in an autonomous agentic mesh, authenticated agents can still execute catastrophic unintended logic sequences. At Palo Alto Networks, we are moving beyond static token-based authentication toward Continuous Semantic Authorization and runtime action-plane telemetry.",
        tags: ["#ZeroTrust", "#AgenticAI", "#PaloAltoNetworks", "#Cybersecurity"],
        likes: 462,
        comments: 57,
        shares: 38,
        mediaType: "image",
        mediaUrl: "images/blog/01.jpg"
      }
    ];
    self.profile = {
      name: "Harsh Verma",
      headline: "Principal AI Architect @ Palo Alto Networks | Forbes Technology Council | IEEE Senior Member",
      followersDisplay: "16.6K+",
      profileUrl: "https://www.linkedin.com/in/harshverma59/"
    };
    self.render();
  };

  // Expose to window
  window.HVLinkedInWidget = {
    init: function (selector, options) {
      var elements = document.querySelectorAll(selector || '[data-linkedin-widget]');
      var instances = [];
      elements.forEach(function (el) {
        instances.push(new LinkedInWidget(el, options));
      });
      return instances;
    },
    create: function (el, options) {
      return new LinkedInWidget(el, options);
    }
  };

  // Auto initialize on DOMContentLoaded if element exists
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      window.HVLinkedInWidget.init('[data-linkedin-widget]');
    });
  } else {
    window.HVLinkedInWidget.init('[data-linkedin-widget]');
  }

})(window, document);
