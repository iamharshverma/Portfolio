/**
 * HV AI Copilot — Client-side Assistant Engine
 * Grounded in Harsh Verma's Portfolio Knowledge Base
 */

(function () {
  'use strict';

  // State
  let isChatOpen = false;
  let isFullscreen = false;
  let messageHistory = [];
  let isGenerating = false;
  let dockSide = 'right'; // 'left' | 'right'
  let topPercent = null; // null for bottom default, or percentage (10 - 90)
  let isDismissed = false;

  // Initialize once DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initHVCopilot);
  } else {
    initHVCopilot();
  }

  function initHVCopilot() {
    // Avoid multiple instances
    if (document.getElementById('hv-copilot-root')) return;

    // Load saved preferences
    try {
      const savedHist = sessionStorage.getItem('hv_copilot_history');
      if (savedHist) messageHistory = JSON.parse(savedHist);

      const savedSide = localStorage.getItem('hv_copilot_dock_side');
      if (savedSide === 'left' || savedSide === 'right') dockSide = savedSide;

      const savedTop = localStorage.getItem('hv_copilot_top_pct');
      if (savedTop !== null) {
        const parsedTop = parseFloat(savedTop);
        if (!isNaN(parsedTop) && parsedTop >= 5 && parsedTop <= 95) {
          topPercent = parsedTop;
        }
      }

      isDismissed = localStorage.getItem('hv_copilot_dismissed') === 'true';
    } catch (e) {
      // ignore storage errors
    }

    createCopilotDOM();
    applyPositionStyles();
    bindEvents();
    renderInitialMessages();
    fetchSuggestions();

    if (isDismissed) {
      applyDismissedState(true);
    }
  }

  function getSideSwitchSvg(side) {
    if (side === 'left') {
      // Docked on left, clicking will dock to right -> arrow points right
      return `<svg class="hv-side-switch-svg" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="3"/><path d="M15 3v18"/><path d="M7 12h5"/><path d="M9 9l3 3-3 3"/></svg>`;
    }
    // Docked on right, clicking will dock to left -> arrow points left
    return `<svg class="hv-side-switch-svg" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="3"/><path d="M9 3v18"/><path d="M17 12h-5"/><path d="M15 9l-3 3 3 3"/></svg>`;
  }

  function createCopilotDOM() {
    if (document.getElementById('hv-copilot-root')) {
      return;
    }
    const root = document.createElement('div');
    root.id = 'hv-copilot-root';

    root.innerHTML = `
      <!-- Launcher Trigger (Draggable, Dockable, Dismissible) -->
      <div class="hv-copilot-launcher ${dockSide === 'left' ? 'dock-left' : 'dock-right'}" id="hvCopilotLauncher" aria-label="Open Harsh Verma AI Copilot" title="Ask Harsh Verma's AI Copilot (Drag to move, click to open)">
        <div class="hv-launcher-grip" title="Drag anywhere to move launcher">
          <i class="mdi mdi-drag-vertical"></i>
        </div>
        
        <div class="hv-launcher-content" id="hvLauncherMainTrigger">
          <div class="hv-launcher-avatar">
            <img src="images/harsh/Harsh_portfolio_pic.png" alt="Harsh Verma" class="hv-launcher-img" />
            <span class="hv-launcher-pulse"></span>
          </div>
          <div class="hv-launcher-text">
            <span class="hv-launcher-title">Harsh AI Copilot</span>
            <span class="hv-launcher-subtitle">Ask anything about my work</span>
          </div>
        </div>

        <div class="hv-launcher-controls">
          <button class="hv-launcher-btn hv-launcher-side-btn" id="hvLauncherSideBtn" title="Move to ${dockSide === 'left' ? 'Right' : 'Left'} side" aria-label="Move to other side">
            ${getSideSwitchSvg(dockSide)}
          </button>
          <button class="hv-launcher-btn hv-launcher-dismiss-btn" id="hvLauncherDismissBtn" title="Hide Copilot from screen" aria-label="Hide Copilot">
            <i class="mdi mdi-close"></i>
          </button>
        </div>
      </div>

      <!-- Minimal Edge Restore Tab (Visible when launcher is hidden/closed, Draggable & Dockable) -->
      <div class="hv-copilot-restore-tab ${dockSide === 'left' ? 'dock-left' : 'dock-right'}" id="hvCopilotRestoreTab" title="Open Harsh Verma AI Copilot (Drag to move anywhere)">
        <div class="hv-restore-tab-grip" id="hvRestoreTabGrip" title="Drag vertically or across sides to move">
          <i class="mdi mdi-drag-vertical"></i>
        </div>
        <div class="hv-restore-tab-main" id="hvRestoreTabMain" style="display:flex;align-items:center;gap:6px;">
          <img src="images/harsh/Harsh_portfolio_pic.png" class="hv-restore-tab-avatar" alt="Harsh Verma" />
          <span>AI Copilot</span>
        </div>
        <div class="hv-restore-tab-controls">
          <button class="hv-restore-btn" id="hvRestoreSideBtn" title="Move to ${dockSide === 'left' ? 'Right' : 'Left'} side" aria-label="Move to other side">
            ${getSideSwitchSvg(dockSide)}
          </button>
        </div>
      </div>

      <!-- Chat Container -->
      <div class="hv-copilot-container ${dockSide === 'left' ? 'dock-left' : 'dock-right'}" id="hvCopilotContainer" role="dialog" aria-modal="true" aria-label="Harsh Verma AI Copilot">
        <!-- Header -->
        <div class="hv-copilot-header">
          <div class="hv-header-info">
            <div class="hv-header-avatar-wrap">
              <img src="images/harsh/Harsh_portfolio_pic.png" alt="Harsh Verma" class="hv-header-avatar-img" />
              <span class="hv-header-online-dot"></span>
            </div>
            <div class="hv-header-titles">
              <div class="hv-header-name">
                Harsh Verma Copilot
                <span class="hv-header-badge">AI Assistant</span>
              </div>
              <div class="hv-header-status">
                <span class="hv-status-dot"></span>
                <span>Grounded in 25 Awards, Books &amp; Research</span>
              </div>
            </div>
          </div>
          <div class="hv-header-actions">
            <button class="hv-action-btn" id="hvHeaderSideBtn" title="Move window to ${dockSide === 'left' ? 'Right' : 'Left'} side" aria-label="Switch side">
              ${getSideSwitchSvg(dockSide)}
            </button>
            <button class="hv-action-btn" id="hvClearChatBtn" title="Clear conversation" aria-label="Clear chat">
              <i class="mdi mdi-refresh"></i>
            </button>
            <button class="hv-action-btn" id="hvExpandChatBtn" title="Toggle full size" aria-label="Toggle full size">
              <i class="mdi mdi-arrow-expand-all" id="hvExpandIcon"></i>
            </button>
            <button class="hv-action-btn" id="hvCloseChatBtn" title="Minimize Copilot" aria-label="Close chat">
              <i class="mdi mdi-close"></i>
            </button>
          </div>
        </div>

        <!-- Quick Starter Chips -->
        <div class="hv-suggestions-bar" id="hvSuggestionsBar">
          <button class="hv-chip-btn" data-query="Give me an executive summary of Harsh's career & expertise">
            <i class="mdi mdi-account-tie mr-1"></i> Executive Bio
          </button>
          <button class="hv-chip-btn" data-query="What are Harsh's top awards and global recognitions?">
            <i class="mdi mdi-trophy-award mr-1"></i> 24 Awards
          </button>
          <button class="hv-chip-btn" data-query="Summarize his authored books on AI Agents & Cyber Defense">
            <i class="mdi mdi-book-open-variant mr-1"></i> Authored Books
          </button>
          <button class="hv-chip-btn" data-query="What are his key research publications & academic citations?">
            <i class="mdi mdi-school mr-1"></i> 26+ Papers
          </button>
          <button class="hv-chip-btn" data-query="How can I invite Harsh for a keynote, panel, or advisory role?">
            <i class="mdi mdi-microphone mr-1"></i> Keynotes &amp; Advisory
          </button>
        </div>

        <!-- Message Thread -->
        <div class="hv-chat-messages" id="hvChatMessages">
          <!-- Dynamic message bubbles rendered here -->
        </div>

        <!-- Input Area -->
        <div class="hv-copilot-input-area">
          <form class="hv-input-form" id="hvInputForm">
            <textarea
              class="hv-input-textarea"
              id="hvInputTextarea"
              rows="1"
              placeholder="Ask about Harsh's AI books, 25 awards, papers, or speaking..."
              aria-label="Message to HV Copilot"
            ></textarea>
            <button type="submit" class="hv-send-btn" id="hvSendBtn" aria-label="Send message">
              <i class="mdi mdi-send"></i>
            </button>
          </form>
          <div class="hv-input-disclaimer">
            Grounded in Harsh Verma's verified academic, book, and industry achievements.
          </div>
        </div>
      </div>
    `;

    document.body.appendChild(root);
  }

  function applyPositionStyles() {
    const launcher = document.getElementById('hvCopilotLauncher');
    const container = document.getElementById('hvCopilotContainer');
    const restoreTab = document.getElementById('hvCopilotRestoreTab');

    [launcher, container, restoreTab].forEach(el => {
      if (!el) return;
      el.classList.remove('dock-left', 'dock-right');
      el.classList.add(dockSide === 'left' ? 'dock-left' : 'dock-right');
    });

    if (topPercent !== null) {
      const topCss = `${topPercent}vh`;
      if (launcher) {
        launcher.style.top = topCss;
        launcher.style.bottom = 'auto';
      }
      if (restoreTab) {
        restoreTab.style.top = topCss;
        restoreTab.style.bottom = 'auto';
      }
      if (container) {
        // Position container aligned vertically within viewport
        const clampedContainerTop = Math.max(10, Math.min(topPercent - 40, 45));
        container.style.top = `${clampedContainerTop}vh`;
        container.style.bottom = 'auto';
      }
    } else {
      if (launcher) {
        launcher.style.top = '';
        launcher.style.bottom = '26px';
      }
      if (restoreTab) {
        restoreTab.style.top = '';
        restoreTab.style.bottom = '26px';
      }
      if (container) {
        container.style.top = '';
        container.style.bottom = '26px';
      }
    }

    // Update icons using SVGs
    const svgContent = getSideSwitchSvg(dockSide);
    const oppositeSide = dockSide === 'left' ? 'Right' : 'Left';

    const launcherSideBtn = document.getElementById('hvLauncherSideBtn');
    if (launcherSideBtn) {
      launcherSideBtn.innerHTML = svgContent;
      launcherSideBtn.title = `Move to ${oppositeSide} side`;
    }

    const headerSideBtn = document.getElementById('hvHeaderSideBtn');
    if (headerSideBtn) {
      headerSideBtn.innerHTML = svgContent;
      headerSideBtn.title = `Move window to ${oppositeSide} side`;
    }

    const restoreSideBtn = document.getElementById('hvRestoreSideBtn');
    if (restoreSideBtn) {
      restoreSideBtn.innerHTML = svgContent;
      restoreSideBtn.title = `Move to ${oppositeSide} side`;
    }
  }

  function applyDismissedState(dismissed) {
    isDismissed = dismissed;
    const launcher = document.getElementById('hvCopilotLauncher');
    const restoreTab = document.getElementById('hvCopilotRestoreTab');

    try {
      if (dismissed) {
        localStorage.setItem('hv_copilot_dismissed', 'true');
      } else {
        localStorage.removeItem('hv_copilot_dismissed');
      }
    } catch (e) {}

    if (launcher) {
      launcher.classList.toggle('is-hidden', dismissed);
    }
    if (restoreTab) {
      restoreTab.classList.toggle('active', dismissed && !isChatOpen);
    }
  }

  function switchDockSide() {
    dockSide = dockSide === 'left' ? 'right' : 'left';
    try {
      localStorage.setItem('hv_copilot_dock_side', dockSide);
    } catch (e) {}
    applyPositionStyles();
  }

  function bindEvents() {
    const launcher = document.getElementById('hvCopilotLauncher');
    const launcherMainTrigger = document.getElementById('hvLauncherMainTrigger');
    const container = document.getElementById('hvCopilotContainer');
    const closeBtn = document.getElementById('hvCloseChatBtn');
    const expandBtn = document.getElementById('hvExpandChatBtn');
    const clearBtn = document.getElementById('hvClearChatBtn');
    const form = document.getElementById('hvInputForm');
    const textarea = document.getElementById('hvInputTextarea');
    const suggestionsBar = document.getElementById('hvSuggestionsBar');
    const launcherSideBtn = document.getElementById('hvLauncherSideBtn');
    const launcherDismissBtn = document.getElementById('hvLauncherDismissBtn');
    const headerSideBtn = document.getElementById('hvHeaderSideBtn');
    const restoreTab = document.getElementById('hvCopilotRestoreTab');

    // Drag-and-Drop / Move functionality for Launcher & Restore Tab
    initDraggableLauncher(launcher);
    initDraggableRestoreTab(restoreTab);

    // Click on main launcher content opens chat
    if (launcherMainTrigger) {
      launcherMainTrigger.addEventListener('click', () => {
        if (!launcher.dataset.wasDragged) {
          toggleChat(true);
        }
      });
    }

    // Side switcher buttons
    if (launcherSideBtn) {
      launcherSideBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        switchDockSide();
      });
    }

    if (headerSideBtn) {
      headerSideBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        switchDockSide();
      });
    }

    const restoreSideBtn = document.getElementById('hvRestoreSideBtn');
    if (restoreSideBtn) {
      restoreSideBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        switchDockSide();
      });
    }

    // Dismiss button on launcher
    if (launcherDismissBtn) {
      launcherDismissBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        applyDismissedState(true);
      });
    }

    // Restore tab click
    const restoreTabMain = document.getElementById('hvRestoreTabMain');
    if (restoreTabMain) {
      restoreTabMain.addEventListener('click', () => {
        if (!restoreTab || !restoreTab.dataset.wasDragged) {
          applyDismissedState(false);
          toggleChat(true);
        }
      });
    } else if (restoreTab) {
      restoreTab.addEventListener('click', (e) => {
        if (e.target.closest('#hvRestoreSideBtn')) return;
        if (!restoreTab.dataset.wasDragged) {
          applyDismissedState(false);
          toggleChat(true);
        }
      });
    }

    // Close chat button in header
    if (closeBtn) {
      closeBtn.addEventListener('click', () => {
        toggleChat(false);
      });
    }

    // Expand / collapse
    if (expandBtn) {
      expandBtn.addEventListener('click', () => {
        isFullscreen = !isFullscreen;
        container.classList.toggle('fullscreen', isFullscreen);
        const icon = document.getElementById('hvExpandIcon');
        if (icon) {
          icon.className = isFullscreen ? 'mdi mdi-arrow-collapse-all' : 'mdi mdi-arrow-expand-all';
        }
      });
    }

    // Clear chat
    if (clearBtn) {
      clearBtn.addEventListener('click', () => {
        messageHistory = [];
        sessionStorage.removeItem('hv_copilot_history');
        renderInitialMessages();
      });
    }

    // Suggestion chips
    if (suggestionsBar) {
      suggestionsBar.addEventListener('click', (e) => {
        const chip = e.target.closest('.hv-chip-btn');
        if (chip && chip.dataset.query) {
          sendMessage(chip.dataset.query);
        }
      });
    }

    // Auto-resize textarea
    if (textarea) {
      textarea.addEventListener('input', () => {
        textarea.style.height = 'auto';
        textarea.style.height = Math.min(textarea.scrollHeight, 100) + 'px';
      });

      // Keyboard submit (Enter sends, Shift+Enter new line)
      textarea.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
          e.preventDefault();
          form.dispatchEvent(new Event('submit'));
        }
        if (e.key === 'Escape' && isChatOpen) {
          toggleChat(false);
        }
      });
    }

    // Form submit
    if (form) {
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        const text = textarea.value.trim();
        if (!text || isGenerating) return;

        textarea.value = '';
        textarea.style.height = 'auto';
        sendMessage(text);
      });
    }
  }

  function initDraggableLauncher(launcher) {
    if (!launcher) return;

    let isDragging = false;
    let startX = 0;
    let startY = 0;
    let initialLeft = 0;
    let initialTop = 0;
    let hasMoved = false;

    function onPointerDown(e) {
      // Don't drag if clicking buttons directly
      if (e.target.closest('.hv-launcher-btn')) return;

      isDragging = true;
      hasMoved = false;
      launcher.dataset.wasDragged = '';

      const rect = launcher && typeof launcher.getBoundingClientRect === 'function' ? launcher.getBoundingClientRect() : { left: 0, top: 0, width: 0, height: 0 };
      startX = e.clientX || (e.touches && e.touches[0].clientX) || 0;
      startY = e.clientY || (e.touches && e.touches[0].clientY) || 0;
      initialLeft = (rect && typeof rect.left === 'number') ? rect.left : 0;
      initialTop = (rect && typeof rect.top === 'number') ? rect.top : 0;

      window.addEventListener('pointermove', onPointerMove);
      window.addEventListener('pointerup', onPointerUp);
      window.addEventListener('touchmove', onPointerMove, { passive: false });
      window.addEventListener('touchend', onPointerUp);
    }

    function onPointerMove(e) {
      if (!isDragging) return;

      const clientX = e.clientX || (e.touches && e.touches[0].clientX) || 0;
      const clientY = e.clientY || (e.touches && e.touches[0].clientY) || 0;
      const deltaX = clientX - startX;
      const deltaY = clientY - startY;

      if (Math.abs(deltaX) > 4 || Math.abs(deltaY) > 4) {
        hasMoved = true;
        launcher.classList.add('is-dragging');
        if (e.cancelable) e.preventDefault();

        // Calculate free movement during active drag
        const newLeft = Math.max(10, Math.min(window.innerWidth - launcher.offsetWidth - 10, initialLeft + deltaX));
        const newTop = Math.max(10, Math.min(window.innerHeight - launcher.offsetHeight - 10, initialTop + deltaY));

        launcher.style.left = `${newLeft}px`;
        launcher.style.top = `${newTop}px`;
        launcher.style.right = 'auto';
        launcher.style.bottom = 'auto';
      }
    }

    function onPointerUp(e) {
      if (!isDragging) return;
      isDragging = false;

      window.removeEventListener('pointermove', onPointerMove);
      window.removeEventListener('pointerup', onPointerUp);
      window.removeEventListener('touchmove', onPointerMove);
      window.removeEventListener('touchend', onPointerUp);

      launcher.classList.remove('is-dragging');

      if (hasMoved) {
        launcher.dataset.wasDragged = 'true';
        setTimeout(() => {
          launcher.dataset.wasDragged = '';
        }, 150);

        // Snap to nearest side (Left or Right)
        const rect = launcher && typeof launcher.getBoundingClientRect === 'function' ? launcher.getBoundingClientRect() : null;
        if (rect) {
          const centerX = (rect.left || 0) + (rect.width || 0) / 2;
          dockSide = centerX < window.innerWidth / 2 ? 'left' : 'right';

          // Calculate and clamp vertical top percentage
          const clampedY = Math.max(20, Math.min(window.innerHeight - (rect.height || 0) - 20, rect.top || 0));
          topPercent = Math.round((clampedY / window.innerHeight) * 100);

          try {
            localStorage.setItem('hv_copilot_dock_side', dockSide);
            localStorage.setItem('hv_copilot_top_pct', topPercent.toString());
          } catch (err) {}

          applyPositionStyles();
        }
      }
    }

    launcher.addEventListener('pointerdown', onPointerDown);
  }

  function initDraggableRestoreTab(restoreTab) {
    if (!restoreTab) return;

    let isDragging = false;
    let startX = 0;
    let startY = 0;
    let initialLeft = 0;
    let initialTop = 0;
    let hasMoved = false;

    function onPointerDown(e) {
      // Don't drag if clicking buttons directly
      if (e.target.closest('#hvRestoreSideBtn')) return;

      isDragging = true;
      hasMoved = false;
      restoreTab.dataset.wasDragged = '';

      const rect = restoreTab && typeof restoreTab.getBoundingClientRect === 'function' ? restoreTab.getBoundingClientRect() : { left: 0, top: 0, width: 0, height: 0 };
      startX = e.clientX || (e.touches && e.touches[0].clientX) || 0;
      startY = e.clientY || (e.touches && e.touches[0].clientY) || 0;
      initialLeft = (rect && typeof rect.left === 'number') ? rect.left : 0;
      initialTop = (rect && typeof rect.top === 'number') ? rect.top : 0;

      window.addEventListener('pointermove', onPointerMove);
      window.addEventListener('pointerup', onPointerUp);
      window.addEventListener('touchmove', onPointerMove, { passive: false });
      window.addEventListener('touchend', onPointerUp);
    }

    function onPointerMove(e) {
      if (!isDragging) return;

      const clientX = e.clientX || (e.touches && e.touches[0].clientX) || 0;
      const clientY = e.clientY || (e.touches && e.touches[0].clientY) || 0;
      const deltaX = clientX - startX;
      const deltaY = clientY - startY;

      if (Math.abs(deltaX) > 4 || Math.abs(deltaY) > 4) {
        hasMoved = true;
        restoreTab.classList.add('is-dragging');
        if (e.cancelable) e.preventDefault();

        // Calculate free movement during active drag across entire viewport
        const newLeft = Math.max(0, Math.min(window.innerWidth - restoreTab.offsetWidth, initialLeft + deltaX));
        const newTop = Math.max(10, Math.min(window.innerHeight - restoreTab.offsetHeight - 10, initialTop + deltaY));

        restoreTab.style.left = `${newLeft}px`;
        restoreTab.style.top = `${newTop}px`;
        restoreTab.style.right = 'auto';
        restoreTab.style.bottom = 'auto';
      }
    }

    function onPointerUp(e) {
      if (!isDragging) return;
      isDragging = false;

      window.removeEventListener('pointermove', onPointerMove);
      window.removeEventListener('pointerup', onPointerUp);
      window.removeEventListener('touchmove', onPointerMove);
      window.removeEventListener('touchend', onPointerUp);

      restoreTab.classList.remove('is-dragging');

      if (hasMoved) {
        restoreTab.dataset.wasDragged = 'true';
        setTimeout(() => {
          restoreTab.dataset.wasDragged = '';
        }, 150);

        // Snap to nearest side (Left or Right)
        const rect = restoreTab && typeof restoreTab.getBoundingClientRect === 'function' ? restoreTab.getBoundingClientRect() : null;
        if (rect) {
          const centerX = (rect.left || 0) + (rect.width || 0) / 2;
          dockSide = centerX < window.innerWidth / 2 ? 'left' : 'right';

          // Calculate and clamp vertical top percentage
          const clampedY = Math.max(10, Math.min(window.innerHeight - (rect.height || 0) - 10, rect.top || 0));
          topPercent = Math.round((clampedY / window.innerHeight) * 100);

          try {
            localStorage.setItem('hv_copilot_dock_side', dockSide);
            localStorage.setItem('hv_copilot_top_pct', topPercent.toString());
          } catch (err) {}

          applyPositionStyles();
        }
      }
    }

    restoreTab.addEventListener('pointerdown', onPointerDown);
  }

  function toggleChat(open) {
    isChatOpen = open;
    const container = document.getElementById('hvCopilotContainer');
    const launcher = document.getElementById('hvCopilotLauncher');
    const restoreTab = document.getElementById('hvCopilotRestoreTab');
    const textarea = document.getElementById('hvInputTextarea');

    if (container) {
      container.classList.toggle('active', open);
    }
    if (launcher) {
      if (open) {
        launcher.style.display = 'none';
      } else {
        launcher.style.display = isDismissed ? 'none' : 'flex';
      }
    }
    if (restoreTab) {
      restoreTab.classList.toggle('active', isDismissed && !open);
    }

    if (open && textarea) {
      setTimeout(() => textarea.focus(), 250);
      scrollToBottom();
    }
  }

  function renderInitialMessages() {
    const messagesEl = document.getElementById('hvChatMessages');
    if (!messagesEl) return;

    messagesEl.innerHTML = '';

    if (messageHistory.length === 0) {
      // Welcome message
      const welcomeContent = `### 👋 Welcome to Harsh Verma's AI Copilot!
I am your intelligent liaison grounded in Harsh Verma's **25 Global Awards**, **25+ Research Publications**, **Authored Books on AI Agents**, and executive advisory background.

How can I assist you today? You can ask about:
- **Executive Biography & Technical Focus**
- **25 Prestigious Recognitions & Fellowships**
- **Authored AI Agent & Cyber Defense Books**
- **Speaking Engagements & Keynote Bookings**`;

      appendMessageToDOM('assistant', welcomeContent, false);
    } else {
      messageHistory.forEach((msg) => {
        appendMessageToDOM(msg.role, msg.content, false);
      });
    }

    scrollToBottom();
  }

  function appendMessageToDOM(role, content, shouldScroll = true) {
    const messagesEl = document.getElementById('hvChatMessages');
    if (!messagesEl) return;

    const msgDiv = document.createElement('div');
    msgDiv.className = `hv-msg hv-msg-${role === 'user' ? 'user' : 'bot'}`;

    const avatarHtml =
      role === 'user'
        ? `<div class="hv-msg-avatar hv-msg-avatar-user"><i class="mdi mdi-account"></i></div>`
        : `<div class="hv-msg-avatar hv-msg-avatar-harsh"><img src="images/harsh/Harsh_portfolio_pic.png" alt="Harsh Verma" class="hv-msg-avatar-img" /></div>`;

    const parsedHtml = parseMarkdown(content);

    let actionsHtml = '';
    if (role === 'assistant') {
      actionsHtml = `
        <div class="hv-msg-actions">
          <button class="hv-msg-btn hv-copy-btn" title="Copy response to clipboard">
            <i class="mdi mdi-content-copy"></i> Copy
          </button>
          <button class="hv-msg-btn hv-speak-btn" title="Listen to response">
            <i class="mdi mdi-volume-high"></i> Listen
          </button>
        </div>
      `;
    }

    msgDiv.innerHTML = `
      ${avatarHtml}
      <div class="hv-msg-content">
        ${parsedHtml}
        ${actionsHtml}
      </div>
    `;

    // Attach copy & listen events
    if (role === 'assistant') {
      const copyBtn = msgDiv.querySelector('.hv-copy-btn');
      if (copyBtn) {
        copyBtn.addEventListener('click', () => {
          const rawText = content.replace(/[#*`_\[\]()]/g, '');
          navigator.clipboard.writeText(rawText).then(() => {
            copyBtn.innerHTML = '<i class="mdi mdi-check"></i> Copied!';
            setTimeout(() => {
              copyBtn.innerHTML = '<i class="mdi mdi-content-copy"></i> Copy';
            }, 2000);
          });
        });
      }

      const speakBtn = msgDiv.querySelector('.hv-speak-btn');
      if (speakBtn && 'speechSynthesis' in window) {
        speakBtn.addEventListener('click', () => {
          if (window.speechSynthesis.speaking) {
            window.speechSynthesis.cancel();
            speakBtn.innerHTML = '<i class="mdi mdi-volume-high"></i> Listen';
            return;
          }
          const cleanText = content.replace(/\[([^\]]+)\]\([^)]+\)/g, '$1').replace(/[#*`_]/g, '');
          const utterance = new SpeechSynthesisUtterance(cleanText);
          utterance.rate = 1.05;
          utterance.onend = () => {
            speakBtn.innerHTML = '<i class="mdi mdi-volume-high"></i> Listen';
          };
          window.speechSynthesis.speak(utterance);
          speakBtn.innerHTML = '<i class="mdi mdi-pause"></i> Stop';
        });
      }
    }

    messagesEl.appendChild(msgDiv);
    if (shouldScroll) scrollToBottom();
  }

  function showTypingIndicator() {
    const messagesEl = document.getElementById('hvChatMessages');
    if (!messagesEl) return null;

    const typingDiv = document.createElement('div');
    typingDiv.className = 'hv-msg hv-msg-bot';
    typingDiv.id = 'hvTypingIndicator';
    typingDiv.innerHTML = `
      <div class="hv-msg-avatar hv-msg-avatar-harsh">
        <img src="images/harsh/Harsh_portfolio_pic.png" alt="Harsh Verma" class="hv-msg-avatar-img" />
      </div>
      <div class="hv-msg-content">
        <div class="hv-typing">
          <div class="hv-typing-dot"></div>
          <div class="hv-typing-dot"></div>
          <div class="hv-typing-dot"></div>
        </div>
      </div>
    `;
    messagesEl.appendChild(typingDiv);
    scrollToBottom();
    return typingDiv;
  }

  function removeTypingIndicator() {
    const indicator = document.getElementById('hvTypingIndicator');
    if (indicator) indicator.remove();
  }

  async function sendMessage(userText) {
    if (!userText.trim() || isGenerating) return;

    // Append user message
    messageHistory.push({ role: 'user', content: userText });
    appendMessageToDOM('user', userText);
    saveHistory();

    isGenerating = true;
    const sendBtn = document.getElementById('hvSendBtn');
    if (sendBtn) sendBtn.disabled = true;

    showTypingIndicator();

    try {
      const response = await fetch('/api/copilot', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          message: userText,
          history: messageHistory.slice(-8)
        })
      });

      if (!response.ok) {
        throw new Error(`Server returned HTTP ${response.status}`);
      }

      const data = await response.json();
      removeTypingIndicator();

      if (data && data.reply) {
        messageHistory.push({ role: 'assistant', content: data.reply });
        appendMessageToDOM('assistant', data.reply);
        saveHistory();
      } else {
        // Fallback to embedded client-side knowledge engine
        const fallbackReply = resolveClientKnowledge(userText);
        messageHistory.push({ role: 'assistant', content: fallbackReply });
        appendMessageToDOM('assistant', fallbackReply);
        saveHistory();
      }
    } catch (err) {
      removeTypingIndicator();
      console.warn('Backend /api/copilot is unavailable (e.g. static hosting or network offline). Activating embedded client knowledge engine:', err.message);
      // Autonomous seamless fallback grounded in Harsh Verma's portfolio
      const fallbackReply = resolveClientKnowledge(userText);
      messageHistory.push({ role: 'assistant', content: fallbackReply });
      appendMessageToDOM('assistant', fallbackReply);
      saveHistory();
    } finally {
      isGenerating = false;
      if (sendBtn) sendBtn.disabled = false;
      scrollToBottom();
    }
  }

  function saveHistory() {
    try {
      sessionStorage.setItem('hv_copilot_history', JSON.stringify(messageHistory.slice(-20)));
    } catch (e) {
      // Storage limit handling
    }
  }

  function scrollToBottom() {
    const messagesEl = document.getElementById('hvChatMessages');
    if (messagesEl) {
      messagesEl.scrollTop = messagesEl.scrollHeight;
    }
  }

  const DEFAULT_SUGGESTIONS = [
    { text: "Give me an executive summary of Harsh's career & expertise", category: "Bio & Overview" },
    { text: "What are Harsh's top awards and global recognitions?", category: "Honors & Awards" },
    { text: "Summarize his authored books on AI Agents & Cyber Defense", category: "Authored Books" },
    { text: "What are his key research publications & academic citations?", category: "Research & Papers" },
    { text: "Tell me about his interactive EasyChair Smart Slides keynotes", category: "Smart Slides" },
    { text: "How can I invite Harsh for a keynote, panel, or advisory role?", category: "Speaking & Contact" }
  ];

  async function fetchSuggestions() {
    const bar = document.getElementById('hvSuggestionsBar');
    if (!bar) return;

    try {
      const res = await fetch('/api/copilot/suggestions');
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      if (data && data.suggestions && data.suggestions.length > 0) {
        renderSuggestionChips(data.suggestions);
        return;
      }
    } catch (e) {
      // Static hosting fallback
    }

    // Default suggestions when running statically
    renderSuggestionChips(DEFAULT_SUGGESTIONS);
  }

  function renderSuggestionChips(suggestions) {
    const bar = document.getElementById('hvSuggestionsBar');
    if (!bar || !suggestions) return;
    bar.innerHTML = suggestions
      .map(
        (s) => `
      <button class="hv-chip-btn" data-query="${escapeHtml(s.text)}">
        <i class="mdi mdi-lightning-bolt mr-1"></i> ${escapeHtml(s.category || s.text.slice(0, 24))}
      </button>
    `
      )
      .join('');
  }

  // Autonomous embedded client-side knowledge engine
  function resolveClientKnowledge(query) {
    const q = (query || '').toLowerCase().trim();

    // 1. Awards & Recognitions
    if (
      q.includes('award') ||
      q.includes('recognition') ||
      q.includes('honor') ||
      q.includes('globee') ||
      q.includes('stevie') ||
      q.includes('nobel') ||
      q.includes('forttuna') ||
      q.includes('titans') ||
      q.includes('brandon') ||
      q.includes('achievement') ||
      q.includes('winner')
    ) {
      return `### 🏆 Harsh Verma — 25 Prestigious Global Awards & Honors

Harsh Verma has received **25 international awards and recognitions** celebrating breakthrough innovations in Enterprise AI, Autonomous Multi-Agent Architectures, and Cyber Defense:

- **Forttuna Global 100 Power List (2026)**: Honored among the world's top 100 technology luminaries shaping the future of autonomous intelligence.
- **Nobel Technology Awards (2026)**: Gold Winner (#145) for pioneering scalable multi-agent systems and real-time enterprise platforms.
- **Global Recognition Award (2026)**: AI Innovator of the Year honoring sustained technical leadership and patent-worthy architectures.
- **Globee & Stevie International Business Awards**: Multiple Gold & Silver honors for Enterprise Technology and AI Breakthroughs.
- **Brandon Hall Group & Tech Titans Honors**: Excellence in High-Impact Engineering Leadership.

👉 Explore the full dossier of honors with official verification credentials: **[View All 25 Awards](page-awards)**`;
    }

    // 2. Books & Authorship
    if (
      q.includes('book') ||
      q.includes('author') ||
      q.includes('agent revolution') ||
      q.includes('published book') ||
      q.includes('writing') ||
      q.includes('cyber defense') ||
      q.includes('enterprise ai agent')
    ) {
      return `### 📚 Authored Books by Harsh Verma

Harsh Verma is the author of two definitive technical volumes bridging academic rigor and mission-critical enterprise engineering:

1. **Enterprise AI Agents: Build Your Authority and Lead the AI Agent Revolution**
   - *Focus*: Architectural patterns, production protocols, deterministic guardrails, and memory graphs for enterprise multi-agent systems.
   - *Target Readers*: AI architects, engineering leaders, and enterprise strategists.

2. **Autonomous Cyber Defense: Adversarial Intelligence and Battleground Systems**
   - *Focus*: Zero-Trust architectures, threat vector modeling, and autonomous threat mitigation in high-throughput distributed networks.

👉 Read chapter outlines and access reading previews: **[Explore Authored Books](page-books)**`;
    }

    // 3. Publications & Academic Citations
    if (
      q.includes('paper') ||
      q.includes('publication') ||
      q.includes('research') ||
      q.includes('scholar') ||
      q.includes('citation') ||
      q.includes('ieee') ||
      q.includes('springer') ||
      q.includes('icaccm') ||
      q.includes('ejcsit') ||
      q.includes('hikerunner') ||
      q.includes('article') ||
      q.includes('journal')
    ) {
      return `### 🔬 25+ Peer-Reviewed Research Publications & Academic Citations

Harsh Verma has published **25+ peer-reviewed and conference papers** across leading IEEE conferences, ICACCM, Springer Nature, and international computer science journals with over **150+ academic citations**:

- **Data Quality, Feature Engineering, and Model Reliability in Large-Scale AI Multi-Agentic Systems** (EJCSIT, May 30, 2021).
- **Scalable Real-Time Data Pipelines for AI and Machine Learning–Driven Enterprise Systems** (EJCSIT, December 30, 2020).
- **Multi-Agent Systems & Trajectory Planning** for Delay-Tolerant Wireless Sensor Networks (ICACCM 2026).
- **Explainable AI (XAI)** for Software Engineering Decision-Making & Risk Reduction.
- **Secure Real-Time Heterogeneous Data Management** in Distributed Cloud Systems.
- **Real-Time Analytics Performance Load Simulation & Scaling** for High-Frequency FinTech.
- **Autonomous Zero-Trust Defense Protocols** for Cloud Microservice Ecosystems.

👉 Access full abstracts, DOIs, and citation downloads: **[Explore 25+ Research Publications](page-publications)** or review the **[Google Scholar Profile](https://scholar.google.com/citations?hl=en&user=zSt9oRMAAAAJ)**.`;
    }

    // 4. Articles & Thought Leadership
    if (
      q.includes('blog') ||
      q.includes('article') ||
      q.includes('moat') ||
      q.includes('orchestration') ||
      (q.includes('forbes') && (q.includes('post') || q.includes('article') || q.includes('read') || q.includes('write')))
    ) {
      return `### ✍️ Articles & Thought Leadership (30 Publications)

Harsh Verma actively authors high-impact technical articles across major global publications including **Forbes Technology Council**, **HackerNoon**, **The AI Journal**, and **RSA Conference**:

- **Latest Forbes Council Article (Oct 2, 2026)**: **[The Real AI Moat: Why Models Are Cheap But Data Orchestration Is Priceless](https://www.forbes.com/councils/forbestechcouncil/2026/10/02/the-real-ai-moat-why-models-are-cheap-but-data-orchestration-is-priceless/)**
- **Engineering The Predictable**: Why Pure Determinism Is Becoming The New Premium In AI Architecture (*Forbes*)
- **The Intelligence Per Dollar Metric**: How Influential Leaders Measure AI Success (*Forbes*)
- **Your First AI Agent Is An Experiment, Not A Product** (*Forbes*)
- **Beyond The Code**: The Evolution Of The Next-Generation Engineer (*Forbes*)

👉 Explore all 30 articles and syndicated feeds: **[Visit Blog & Articles Hub](page-blog)**`;
    }

    // 5. Fellowships & Professional Memberships
    if (
      q.includes('member') ||
      q.includes('fellow') ||
      q.includes('harvard') ||
      q.includes('ieee') ||
      q.includes('bcs') ||
      q.includes('forbes') ||
      q.includes('sigma xi') ||
      q.includes('owasp') ||
      q.includes('acm') ||
      q.includes('association') ||
      q.includes('credential') ||
      q.includes('certification') ||
      q.includes('society')
    ) {
      return `### 🎖️ Invited Fellowships & Professional Memberships

Harsh Verma holds prestigious fellowships and elected senior memberships across elite international scientific, computing, and executive institutions:

- **Harvard Square Leaders Excellence Fellow** (Cambridge, MA)
- **Senior Member of IEEE (SMIEEE 95132014)** (Institute of Electrical and Electronics Engineers)
- **Fellow of The British Computer Society (FBCS, Chartered IT Professional)**
- **Official Member, Forbes Technology Council** (Published Thought Leader)
- **Fellow of The Royal Society of Arts (FRSA)**
- **Full Elected Member of Sigma Xi** (The Scientific Research Honor Society)
- **OWASP Global Member & Cloud Security Alliance (CSA) Member**

👉 Deep dive into all citations, certifications, and appointments on the **[Invited Memberships Page](page-memberships)** and **[47 Verified Academic &amp; Industry Hubs](page-about#verified-profiles)**.`;
    }

    // 5. Professional Career & Experience
    if (
      q.includes('experience') ||
      q.includes('career') ||
      q.includes('role') ||
      q.includes('job') ||
      q.includes('work') ||
      q.includes('history') ||
      q.includes('background') ||
      q.includes('palo alto') ||
      q.includes('company') ||
      q.includes('resume') ||
      q.includes('cv') ||
      q.includes('who is') ||
      q.includes('profile')
    ) {
      return `### 💼 Harsh Verma — Professional Career & Experience

Harsh Verma brings over **12+ years of proven technical leadership** across enterprise engineering, cloud distributed systems, and AI innovation:

- **Principal AI/ML Engineer & Enterprise Architect**: Spearheading autonomous agent intelligence, AI security guardrails, and mission-critical cloud pipelines at **Palo Alto Networks**.
- **Enterprise Engineering Leadership**: Architecting mission-critical platforms, streaming data backbones, and Zero-Trust frameworks.
- **R&D and Open Source Roots**: Former R&D Engineer Intern at **ISRO** (Spatial Computing & GIS) and **Mozilla Firefox Ambassador**.
- **10 Structured Roles**: Covering enterprise engineering, tech leadership, research, and high-impact innovation.

👉 Explore the interactive experience timeline and tech stacks: **[Experience Section](index#experience)** or read the full biography on **[About Harsh](page-about)**.`;
    }

    // 6. Smart Slides & Keynote Decks
    if (
      q.includes('slide') ||
      q.includes('presentation') ||
      q.includes('deck') ||
      q.includes('easychair') ||
      q.includes('powerpoint')
    ) {
      return `### 📊 EasyChair Smart Slides & Keynote Decks

Harsh's verified keynote slide decks are available via an interactive slide player with slide-by-slide citations and downloads:

- **Agentic Security Governance**: Production protocols and deterministic safety boundaries for enterprise multi-agent networks.
- **GenAI Cybersecurity & Cyber Defense**: Zero-Trust battleground systems against adversarial AI threats.
- **HikeRunner: LoadTestFramework**: Distributed performance benchmarking for microservices and real-time streams.

👉 Launch the interactive slide viewer: **[Open Smart Slides Hub](page-smart-slides)**`;
    }

    // 7. Keynotes & Speaking Engagements
    if (
      q.includes('speak') ||
      q.includes('event') ||
      q.includes('keynote') ||
      q.includes('conference') ||
      q.includes('panel') ||
      q.includes('talk') ||
      q.includes('booking') ||
      q.includes('agenda') ||
      q.includes('retreat') ||
      q.includes('ata') ||
      q.includes('gtr') ||
      q.includes('sf tech week') ||
      q.includes('dim sum') ||
      q.includes('dent')
    ) {
      return `### 🎙️ Keynotes, Panels & Speaking Engagements

Harsh Verma is an international keynote speaker, panelist, and startup judge:
- **Demos & Dim Sum — #SFTechWeek (Oct 7, 2026)**: Serving on the official Dent Expert Network judging panel (*Dent Capital, The MBA Fund, Deel & Manatt*).
- **AI × Security during SF Tech Week (Oct 6, 2026)**: Securing the AI Supply Chain & Autonomous Agent Ecosystem (*Hosted by AI Insiders with Pebblebed*).
- **Enterprise AI Agent Orchestration**: Scaling autonomous agents with deterministic controls.
- **Autonomous Cyber Defense**: Battleground machine learning against zero-day threats.
- **High-Throughput Cloud Distributed Architectures**: Lessons from enterprise-scale data platforms.
- **Featured Appearances**: Keynote speaker at @#ATAGTR2017 (Global Testing Retreat), IEEE Symposia, and global engineering conferences.

👉 Review 35+ appearances across keynotes, panels & hackathon judging: **[Speaking Engagements](page-events)** or book an executive hold: **[Contact & Booking Form](index#contact)**.`;
    }

    // 8. Media Coverage & Distribution Analytics
    if (
      q.includes('media') ||
      q.includes('press') ||
      q.includes('news') ||
      q.includes('interview') ||
      q.includes('views') ||
      q.includes('reach') ||
      q.includes('distribution') ||
      q.includes('yahoo') ||
      q.includes('business insider') ||
      q.includes('usa today') ||
      q.includes('ap news')
    ) {
      return `### 📰 Media Coverage & Global Distribution Reach

Harsh Verma's technical thought leadership has reached an aggregate global audience of over **3.75+ Billion potential views** across **40+ media features**:

- **Major Syndication Platforms**: Featured on **Yahoo Finance, Business Insider, USA TODAY, AP News, NewsBreak, Barchart, and StreetInsider**.
- **Geographic Reach**: 48% US, 18% UK, 14% India, 12% Canada, 8% Asia & Middle East.
- **Audience Demographics**: Engineers & Systems Architects (32%), Founders & CTOs (26%), Investors & VCs (24%).

👉 Deep dive into the reach metrics: **[Media Distribution Analytics](page-media-distribution-analytics)** or browse full articles on **[Media Coverage](page-media)**.`;
    }

    // 9. Everyday Routine & Social Feeds
    if (
      q.includes('routine') ||
      q.includes('social') ||
      q.includes('post') ||
      q.includes('feed') ||
      q.includes('instagram') ||
      q.includes('linkedin') ||
      q.includes('daily') ||
      q.includes('fitness') ||
      q.includes('wellness')
    ) {
      return `### ⚡ Everyday Routine & Social Feed

Harsh shares active insights on engineering leadership, daily discipline, and enterprise architectures:

- **LinkedIn (@harshverma59)**: Deep dives into AI Agent systems, Forbes Tech Council articles, and enterprise architecture.
- **Instagram (@aiwithharsh)**: Visual reels on AI engineering beyond code, daily routine, and wellness.

👉 Check out the interactive feed: **[Everyday Routine & Social Hub](index#routine)**`;
    }

    // 10. Newsletter & Dispatch
    if (
      q.includes('newsletter') ||
      q.includes('dispatch') ||
      q.includes('subscribe') ||
      q.includes('monthly')
    ) {
      return `### 📬 The Agentic Systems & AI Dispatch

A monthly curated executive newsletter by Harsh Verma covering deep dives on Agentic AI & Autonomous Copilots, Zero-Trust Cyber Defense, and Enterprise High-Scale Systems Architecture.

- Read by over **3,240+ engineers, researchers, and technology executives**.
- Published monthly with actionable architectural breakdowns.

👉 Read recent articles and subscribe for free: **[Explore Blog & Dispatch](page-blog)**`;
    }

    // 11. Contact & Collaboration
    if (
      q.includes('contact') ||
      q.includes('email') ||
      q.includes('collaborate') ||
      q.includes('hire') ||
      q.includes('advisory') ||
      q.includes('consult') ||
      q.includes('reach') ||
      q.includes('message') ||
      q.includes('touch') ||
      q.includes('inquiry')
    ) {
      return `### ✉️ Get in Touch with Harsh Verma

Harsh Verma is available for executive advisory, enterprise AI architecture consulting, keynote engagements, and research collaborations:

- **Direct Email**: [harshverma59@gmail.com](mailto:harshverma59@gmail.com)
- **LinkedIn**: [linkedin.com/in/harshverma59/](https://www.linkedin.com/in/harshverma59/)
- **GitHub**: [github.com/iamharshverma](https://github.com/iamharshverma)
- **Direct Portfolio Contact Form**: **[Send a Message to Harsh](index#contact)**

All verified inquiries submitted through this portfolio are delivered directly with a guaranteed 24-hour response window.`;
    }

    // Default executive bio
    return `### 🌟 Harsh Verma — Executive Overview

**Harsh Verma** is an internationally recognized **Enterprise AI Architect, Principal Technologist, and Author** based in the San Francisco Bay Area with over 12+ years of pioneering achievements:

- **Specializations**: Enterprise Generative AI, Autonomous Multi-Agent Architectures, Zero-Trust Cyber Resilience, and Cloud Distributed Systems.
- **Recognitions**: **25 Global Awards** (Forttuna Global 100, Nobel Technology Awards Gold Winner, AI Innovator of the Year, Globee & Stevie Awards).
- **Academic Impact**: **25+ Peer-Reviewed Publications** on IEEE/Google Scholar, **2 Published Books**, and **47 Verified Academic/Professional Registries**.
- **Fellowships**: Harvard Square Leaders Excellence Fellow, IEEE Senior Member, and Forbes Technology Council Member.

**Explore further:**
- 🏆 **[25 Prestigious Awards](page-awards)**
- 🔬 **[25+ Research Publications](page-publications)**
- 💼 **[Professional Experience & Roles](index#experience)**
- 📚 **[Authored Books](page-books)**
- 👥 **[Invited Memberships](page-memberships)**
- ✉️ **[Get in Touch / Book a Keynote](index#contact)**`;
  }

  // Lightweight robust Markdown parser
  function parseMarkdown(md) {
    if (!md) return '';
    let html = md;

    // Escape basic HTML except intentional
    html = html
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');

    // Headings
    html = html.replace(/^### (.*$)/gim, '<h4>$1</h4>');
    html = html.replace(/^## (.*$)/gim, '<h3>$1</h3>');

    // Bold & Italic
    html = html.replace(/\*\*(.*?)\*\*/gim, '<strong>$1</strong>');
    html = html.replace(/\*(.*?)\*/gim, '<em>$1</em>');

    // Links [Text](url)
    html = html.replace(
      /\[([^\]]+)\]\(([^)]+)\)/gim,
      '<a href="$2" target="_self" class="hv-link">$1 <i class="mdi mdi-arrow-top-right small"></i></a>'
    );

    // Unordered Lists
    html = html.replace(/^\s*-\s+(.*$)/gim, '<li>$1</li>');
    html = html.replace(/(<li>.*<\/li>)/gims, '<ul>$1</ul>');
    html = html.replace(/<\/ul>\s*<ul>/gim, '');

    // Paragraphs / Linebreaks
    html = html.replace(/\n\n+/g, '</p><p>');
    html = html.replace(/\n/g, '<br/>');

    return `<p>${html}</p>`
      .replace(/<p><\/p>/g, '')
      .replace(/<p>(<h4>.*?<\/h4>)<\/p>/g, '$1')
      .replace(/<p>(<h3>.*?<\/h3>)<\/p>/g, '$1')
      .replace(/<p>(<ul>.*?<\/ul>)<\/p>/g, '$1');
  }

  function escapeHtml(text) {
    return (text || '')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');
  }
})();
