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
                <span>Grounded in 24 Awards, Books &amp; Research</span>
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
            <i class="mdi mdi-school mr-1"></i> 22+ Papers
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
              placeholder="Ask about Harsh's AI books, 24 awards, papers, or speaking..."
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
I am your intelligent liaison grounded in Harsh Verma's **24 Global Awards**, **22+ Research Publications**, **Authored Books on AI Agents**, and executive advisory background.

How can I assist you today? You can ask about:
- **Executive Biography & Technical Focus**
- **24 Prestigious Recognitions & Fellowships**
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

      const data = await response.json();
      removeTypingIndicator();

      if (data && data.reply) {
        messageHistory.push({ role: 'assistant', content: data.reply });
        appendMessageToDOM('assistant', data.reply);
        saveHistory();
      } else {
        const errorMsg = "I'm sorry, I encountered an unexpected error while preparing the answer. Please feel free to try again or reach out directly to harshverma59@gmail.com.";
        appendMessageToDOM('assistant', errorMsg);
      }
    } catch (err) {
      removeTypingIndicator();
      console.error('Copilot request error:', err);
      const networkErrorMsg = "Unable to reach the AI server right now. Please explore the portfolio navigation directly or email **[harshverma59@gmail.com](mailto:harshverma59@gmail.com)**.";
      appendMessageToDOM('assistant', networkErrorMsg);
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

  async function fetchSuggestions() {
    try {
      const res = await fetch('/api/copilot/suggestions');
      const data = await res.json();
      if (data && data.suggestions && data.suggestions.length > 0) {
        const bar = document.getElementById('hvSuggestionsBar');
        if (bar) {
          bar.innerHTML = data.suggestions
            .map(
              (s) => `
            <button class="hv-chip-btn" data-query="${escapeHtml(s.text)}">
              <i class="mdi mdi-lightning-bolt mr-1"></i> ${escapeHtml(s.category || s.text.slice(0, 24))}
            </button>
          `
            )
            .join('');
        }
      }
    } catch (e) {
      // Fallback chips already in DOM
    }
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
