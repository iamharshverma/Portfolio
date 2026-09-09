/**
 * Harsh Verma Portfolio - Fullscreen Lightbox Modal System
 * High-performance fullscreen viewer for technical architecture diagrams & project screenshots
 * Featuring: Fullscreen API, Pan & Zoom (1x - 4x), Keyboard shortcuts, Touch swipes,
 * Technical architecture metadata, Repository deep-links, and Thumbnail navigation.
 */

(function(window, document, $) {
    "use strict";

    // Global state
    var activeGallery = [];
    var currentIndex = 0;
    var isOpen = false;

    // Zoom and pan state
    var currentScale = 1.0;
    var minScale = 1.0;
    var maxScale = 4.0;
    var translateX = 0;
    var translateY = 0;
    var isDragging = false;
    var startDragX = 0;
    var startDragY = 0;
    var initialTranslateX = 0;
    var initialTranslateY = 0;

    // Touch swipe state
    var touchStartX = 0;
    var touchStartY = 0;
    var touchStartTime = 0;

    // Elements cache
    var $modal = null;
    var $image = null;
    var $imageWrap = null;
    var $loader = null;
    var $counter = null;
    var $title = null;
    var $badge = null;
    var $captionTitle = null;
    var $captionDesc = null;
    var $captionTags = null;
    var $repoLink = null;
    var $downloadBtn = null;
    var $newTabBtn = null;
    var $zoomLevel = null;
    var $prevBtn = null;
    var $nextBtn = null;
    var $fullscreenBtn = null;
    var $thumbsStrip = null;
    var $thumbsWrap = null;

    /**
     * Build and inject Modal DOM structure
     */
    function initDOM() {
        if ($('#hv-lightbox-modal').length) {
            $modal = $('#hv-lightbox-modal');
        } else {
            var html = [
                '<div id="hv-lightbox-modal" class="hv-lightbox" role="dialog" aria-modal="true" aria-label="Technical Diagram Fullscreen Viewer">',
                '  <!-- Header Bar -->',
                '  <div class="hv-lb-header">',
                '    <div class="hv-lb-meta">',
                '      <span class="hv-lb-badge" id="hvLbBadge"><i class="mdi mdi-sitemap"></i> ARCHITECTURE</span>',
                '      <span class="hv-lb-counter" id="hvLbCounter">1 / 1</span>',
                '      <h4 class="hv-lb-title" id="hvLbTitle">Diagram Preview</h4>',
                '    </div>',
                '    <div class="hv-lb-toolbar">',
                '      <button type="button" class="hv-lb-btn icon-only" id="hvLbZoomOut" title="Zoom Out ( - )" aria-label="Zoom Out">',
                '        <i class="mdi mdi-magnify-minus-outline font-18"></i>',
                '      </button>',
                '      <button type="button" class="hv-lb-btn" id="hvLbZoomReset" title="Reset Zoom ( 0 )" aria-label="Reset Zoom">',
                '        <span class="hv-lb-zoom-level" id="hvLbZoomLevel">100%</span>',
                '      </button>',
                '      <button type="button" class="hv-lb-btn icon-only" id="hvLbZoomIn" title="Zoom In ( + )" aria-label="Zoom In">',
                '        <i class="mdi mdi-magnify-plus-outline font-18"></i>',
                '      </button>',
                '      <button type="button" class="hv-lb-btn hide-mobile" id="hvLbFullscreen" title="Toggle Fullscreen ( F )" aria-label="Toggle Fullscreen">',
                '        <i class="mdi mdi-fullscreen font-18" id="hvLbFsIcon"></i> <span id="hvLbFsText">Fullscreen</span>',
                '      </button>',
                '      <a href="#" target="_blank" class="hv-lb-btn hv-lb-btn-repo hide-mobile" id="hvLbRepoLink" title="View Source Code Repository">',
                '        <i class="mdi mdi-github-face font-16"></i> <span>GitHub Repo</span>',
                '      </a>',
                '      <button type="button" class="hv-lb-btn hv-lb-btn-close icon-only" id="hvLbClose" title="Close ( Esc )" aria-label="Close">',
                '        <i class="mdi mdi-close font-20"></i>',
                '      </button>',
                '    </div>',
                '  </div>',
                '',
                '  <!-- Stage Viewport -->',
                '  <div class="hv-lb-stage" id="hvLbStage">',
                '    <button type="button" class="hv-lb-nav-btn hv-lb-prev" id="hvLbPrev" title="Previous Diagram (Left Arrow)" aria-label="Previous">',
                '      <i class="mdi mdi-chevron-left"></i>',
                '    </button>',
                '    <div class="hv-lb-image-wrap" id="hvLbImageWrap">',
                '      <img src="" alt="Technical Architecture Diagram" class="hv-lb-image" id="hvLbImage" />',
                '    </div>',
                '    <div class="hv-lb-loader" id="hvLbLoader"></div>',
                '    <button type="button" class="hv-lb-nav-btn hv-lb-next" id="hvLbNext" title="Next Diagram (Right Arrow)" aria-label="Next">',
                '      <i class="mdi mdi-chevron-right"></i>',
                '    </button>',
                '  </div>',
                '',
                '  <!-- Caption & Controls Footer -->',
                '  <div class="hv-lb-footer" id="hvLbFooter">',
                '    <div class="hv-lb-caption-content">',
                '      <div class="hv-lb-caption-tags" id="hvLbTags"></div>',
                '      <h3 class="hv-lb-caption-title" id="hvLbCaptionTitle">Architecture Overview</h3>',
                '      <p class="hv-lb-caption-desc" id="hvLbCaptionDesc">Diagram description details...</p>',
                '      <div class="hv-lb-footer-actions">',
                '        <a href="#" target="_blank" class="hv-lb-btn" id="hvLbNewTab" title="Open High-Resolution in New Tab">',
                '          <i class="mdi mdi-open-in-new font-16"></i> <span>Open Full Resolution</span>',
                '        </a>',
                '        <a href="#" download class="hv-lb-btn" id="hvLbDownload" title="Download Technical Diagram">',
                '          <i class="mdi mdi-download font-16"></i> <span>Download Diagram</span>',
                '        </a>',
                '      </div>',
                '    </div>',
                '    <div class="hv-lb-thumbs-wrap" id="hvLbThumbsWrap">',
                '      <div class="hv-lb-thumbs-strip" id="hvLbThumbsStrip"></div>',
                '    </div>',
                '  </div>',
                '</div>'
            ].join('\n');

            $('body').append(html);
            $modal = $('#hv-lightbox-modal');
        }

        // Cache elements
        $image = $('#hvLbImage');
        $imageWrap = $('#hvLbImageWrap');
        $loader = $('#hvLbLoader');
        $counter = $('#hvLbCounter');
        $title = $('#hvLbTitle');
        $badge = $('#hvLbBadge');
        $captionTitle = $('#hvLbCaptionTitle');
        $captionDesc = $('#hvLbCaptionDesc');
        $captionTags = $('#hvLbTags');
        $repoLink = $('#hvLbRepoLink');
        $downloadBtn = $('#hvLbDownload');
        $newTabBtn = $('#hvLbNewTab');
        $zoomLevel = $('#hvLbZoomLevel');
        $prevBtn = $('#hvLbPrev');
        $nextBtn = $('#hvLbNext');
        $fullscreenBtn = $('#hvLbFullscreen');
        $thumbsStrip = $('#hvLbThumbsStrip');
        $thumbsWrap = $('#hvLbThumbsWrap');

        bindEvents();
    }

    /**
     * Apply transform to image container
     */
    function updateTransform(animate) {
        if (!$imageWrap) return;

        if (animate) {
            $imageWrap.css('transition', 'transform 0.18s ease-out');
        } else {
            $imageWrap.css('transition', 'none');
        }

        var transformStr = 'translate3d(' + translateX + 'px, ' + translateY + 'px, 0px) scale(' + currentScale + ')';
        $imageWrap.css('transform', transformStr);

        if ($zoomLevel) {
            $zoomLevel.text(Math.round(currentScale * 100) + '%');
        }

        if (currentScale > 1.0) {
            $imageWrap.addClass('can-drag');
        } else {
            $imageWrap.removeClass('can-drag');
            translateX = 0;
            translateY = 0;
        }
    }

    /**
     * Reset Zoom & Pan
     */
    function resetZoom(animate) {
        currentScale = 1.0;
        translateX = 0;
        translateY = 0;
        updateTransform(animate !== false);
    }

    /**
     * Zoom In / Out
     */
    function setZoom(newScale, animate) {
        currentScale = Math.min(maxScale, Math.max(minScale, newScale));
        if (currentScale <= 1.0) {
            translateX = 0;
            translateY = 0;
        }
        updateTransform(animate !== false);
    }

    function zoomIn() {
        setZoom(currentScale + 0.5, true);
    }

    function zoomOut() {
        setZoom(currentScale - 0.5, true);
    }

    /**
     * Toggle HTML5 Fullscreen
     */
    function toggleFullscreen() {
        var elem = $modal[0];
        var isFs = document.fullscreenElement || document.webkitFullscreenElement || document.mozFullScreenElement || document.msFullscreenElement;

        if (!isFs) {
            if (elem.requestFullscreen) {
                elem.requestFullscreen().catch(function() {});
            } else if (elem.webkitRequestFullscreen) {
                elem.webkitRequestFullscreen();
            } else if (elem.mozRequestFullScreen) {
                elem.mozRequestFullScreen();
            } else if (elem.msRequestFullscreen) {
                elem.msRequestFullscreen();
            }
        } else {
            if (document.exitFullscreen) {
                document.exitFullscreen().catch(function() {});
            } else if (document.webkitExitFullscreen) {
                document.webkitExitFullscreen();
            } else if (document.mozCancelFullScreen) {
                document.mozCancelFullScreen();
            } else if (document.msExitFullscreen) {
                document.msExitFullscreen();
            }
        }
    }

    function updateFullscreenUI() {
        var isFs = !!(document.fullscreenElement || document.webkitFullscreenElement || document.mozFullScreenElement || document.msFullscreenElement);
        if (isFs) {
            $('#hvLbFsIcon').removeClass('mdi-fullscreen').addClass('mdi-fullscreen-exit');
            $('#hvLbFsText').text('Exit Fullscreen');
        } else {
            $('#hvLbFsIcon').removeClass('mdi-fullscreen-exit').addClass('mdi-fullscreen');
            $('#hvLbFsText').text('Fullscreen');
        }
    }

    /**
     * Load slide item by index
     */
    function loadSlide(index) {
        if (!activeGallery.length) return;

        if (index < 0) index = activeGallery.length - 1;
        if (index >= activeGallery.length) index = 0;

        currentIndex = index;
        var item = activeGallery[currentIndex];

        // Reset zoom for new slide
        resetZoom(false);

        // Update counter & titles
        $counter.text((currentIndex + 1) + ' / ' + activeGallery.length);
        $title.text(item.title || 'Technical Diagram');
        $captionTitle.text(item.title || 'Technical Diagram');
        $captionDesc.text(item.description || 'Detailed technical diagram and system architecture workflow.');

        // Badge
        var domain = (item.category || item.tag || 'SYSTEM ARCHITECTURE').toUpperCase();
        $badge.html('<i class="mdi mdi-sitemap"></i> ' + domain);

        // Tags
        $captionTags.empty();
        if (item.tags && item.tags.length) {
            item.tags.forEach(function(t) {
                $captionTags.append('<span class="hv-lb-tag">' + t + '</span>');
            });
        } else if (item.category) {
            $captionTags.append('<span class="hv-lb-tag">' + item.category + '</span>');
        }

        // Repository link
        if (item.repo) {
            $repoLink.attr('href', item.repo).css('display', 'inline-flex');
        } else {
            $repoLink.css('display', 'none');
        }

        // New tab & download
        $newTabBtn.attr('href', item.src);
        $downloadBtn.attr('href', item.src);
        if (item.src) {
            var filename = item.src.split('/').pop();
            $downloadBtn.attr('download', filename || 'architecture_diagram.svg');
        }

        // Loading state
        $image.addClass('loading');
        $loader.addClass('active');

        // Preload image
        var tempImg = new Image();
        tempImg.onload = function() {
            $image.attr('src', item.src);
            $image.removeClass('loading');
            $loader.removeClass('active');
        };
        tempImg.onerror = function() {
            $image.attr('src', item.src);
            $image.removeClass('loading');
            $loader.removeClass('active');
        };
        tempImg.src = item.src;

        // Navigation button states
        if (activeGallery.length <= 1) {
            $prevBtn.hide();
            $nextBtn.hide();
            $thumbsWrap.hide();
        } else {
            $prevBtn.show();
            $nextBtn.show();
            $thumbsWrap.show();
        }

        // Highlight thumbnail
        $thumbsStrip.find('.hv-lb-thumb-item').removeClass('active');
        var $activeThumb = $thumbsStrip.find('[data-thumb-idx="' + currentIndex + '"]');
        if ($activeThumb.length) {
            $activeThumb.addClass('active');
            // Center thumbnail in strip
            var strip = $thumbsStrip[0];
            var thumb = $activeThumb[0];
            if (strip && thumb) {
                var scrollLeft = thumb.offsetLeft - (strip.clientWidth / 2) + (thumb.clientWidth / 2);
                $thumbsStrip.stop().animate({ scrollLeft: scrollLeft }, 200);
            }
        }
    }

    /**
     * Build thumbnail strip
     */
    function buildThumbnails() {
        $thumbsStrip.empty();
        if (activeGallery.length <= 1) {
            $thumbsWrap.hide();
            return;
        }

        activeGallery.forEach(function(item, idx) {
            var $t = $('<div class="hv-lb-thumb-item" data-thumb-idx="' + idx + '" title="' + (item.title || 'Diagram') + '">' +
                       '<img src="' + item.src + '" alt="thumb" loading="lazy" />' +
                       '</div>');
            $t.on('click', function(e) {
                e.stopPropagation();
                loadSlide(idx);
            });
            $thumbsStrip.append($t);
        });

        $thumbsWrap.show();
    }

    /**
     * Open Lightbox Modal
     */
    function openLightbox(gallery, startIndex) {
        initDOM();

        if (!gallery || !gallery.length) return;

        activeGallery = gallery;
        currentIndex = Math.max(0, Math.min(startIndex || 0, gallery.length - 1));

        buildThumbnails();
        loadSlide(currentIndex);

        $modal.addClass('active');
        $('body').addClass('hv-lightbox-open');
        isOpen = true;
    }

    /**
     * Close Lightbox Modal
     */
    function closeLightbox() {
        if (!isOpen) return;

        // Exit fullscreen if in fs mode
        if (document.fullscreenElement || document.webkitFullscreenElement || document.mozFullScreenElement || document.msFullscreenElement) {
            if (document.exitFullscreen) {
                document.exitFullscreen().catch(function() {});
            }
        }

        $modal.removeClass('active');
        $('body').removeClass('hv-lightbox-open');
        isOpen = false;
        resetZoom(false);
    }

    /**
     * Bind all interactive events
     */
    function bindEvents() {
        // Close buttons
        $('#hvLbClose').on('click', function(e) {
            e.preventDefault();
            closeLightbox();
        });

        // Click on stage background to close (unless clicking on image or controls)
        $('#hvLbStage').on('click', function(e) {
            if (e.target.id === 'hvLbStage' && currentScale === 1.0) {
                closeLightbox();
            }
        });

        // Prev & Next
        $prevBtn.on('click', function(e) {
            e.stopPropagation();
            loadSlide(currentIndex - 1);
        });

        $nextBtn.on('click', function(e) {
            e.stopPropagation();
            loadSlide(currentIndex + 1);
        });

        // Zoom controls
        $('#hvLbZoomIn').on('click', function(e) {
            e.stopPropagation();
            zoomIn();
        });

        $('#hvLbZoomOut').on('click', function(e) {
            e.stopPropagation();
            zoomOut();
        });

        $('#hvLbZoomReset').on('click', function(e) {
            e.stopPropagation();
            resetZoom(true);
        });

        // Fullscreen toggle
        $fullscreenBtn.on('click', function(e) {
            e.stopPropagation();
            toggleFullscreen();
        });

        $(document).on('fullscreenchange webkitfullscreenchange mozfullscreenchange MSFullscreenChange', function() {
            updateFullscreenUI();
        });

        // Double click to zoom toggle
        $imageWrap.on('dblclick', function(e) {
            e.stopPropagation();
            if (currentScale > 1.0) {
                resetZoom(true);
            } else {
                setZoom(2.25, true);
            }
        });

        // Mousewheel Zoom on Stage
        $('#hvLbStage').on('wheel', function(e) {
            e.preventDefault();
            var delta = e.originalEvent.deltaY;
            if (delta < 0) {
                // Zoom in
                setZoom(currentScale + 0.25, false);
            } else {
                // Zoom out
                setZoom(currentScale - 0.25, false);
            }
        });

        // Mouse Drag to Pan when zoomed in
        $imageWrap.on('mousedown', function(e) {
            if (currentScale <= 1.0) return;
            e.preventDefault();
            isDragging = true;
            startDragX = e.clientX;
            startDragY = e.clientY;
            initialTranslateX = translateX;
            initialTranslateY = translateY;
            $imageWrap.addClass('is-dragging');
        });

        $(window).on('mousemove', function(e) {
            if (!isDragging || currentScale <= 1.0) return;
            var dx = e.clientX - startDragX;
            var dy = e.clientY - startDragY;

            // Constrain translation to bounds
            var boundX = (window.innerWidth * (currentScale - 1)) / 2 + 100;
            var boundY = (window.innerHeight * (currentScale - 1)) / 2 + 100;

            translateX = Math.max(-boundX, Math.min(boundX, initialTranslateX + dx));
            translateY = Math.max(-boundY, Math.min(boundY, initialTranslateY + dy));
            updateTransform(false);
        });

        $(window).on('mouseup', function() {
            if (isDragging) {
                isDragging = false;
                $imageWrap.removeClass('is-dragging');
            }
        });

        // Touch handling (Swipe left/right or Drag when zoomed)
        var touchStartX = 0;
        var touchStartY = 0;
        var touchCurrentX = 0;
        var touchCurrentY = 0;

        $('#hvLbStage').on('touchstart', function(e) {
            if (!isOpen) return;
            var touch = e.originalEvent.touches[0];
            touchStartX = touch.clientX;
            touchStartY = touch.clientY;
            touchStartTime = Date.now();

            if (currentScale > 1.0) {
                isDragging = true;
                startDragX = touch.clientX;
                startDragY = touch.clientY;
                initialTranslateX = translateX;
                initialTranslateY = translateY;
            }
        });

        $('#hvLbStage').on('touchmove', function(e) {
            if (!isOpen) return;
            var touch = e.originalEvent.touches[0];
            touchCurrentX = touch.clientX;
            touchCurrentY = touch.clientY;

            if (currentScale > 1.0 && isDragging) {
                var dx = touchCurrentX - startDragX;
                var dy = touchCurrentY - startDragY;
                translateX = initialTranslateX + dx;
                translateY = initialTranslateY + dy;
                updateTransform(false);
            }
        });

        $('#hvLbStage').on('touchend', function() {
            if (!isOpen) return;
            if (isDragging) {
                isDragging = false;
            } else if (currentScale <= 1.0) {
                var diffX = touchCurrentX - touchStartX;
                var diffY = touchCurrentY - touchStartY;
                var timeDiff = Date.now() - touchStartTime;

                // Horizontal swipe detection
                if (Math.abs(diffX) > 45 && Math.abs(diffY) < 70 && timeDiff < 350) {
                    if (diffX < 0) {
                        loadSlide(currentIndex + 1); // Swipe left -> next
                    } else {
                        loadSlide(currentIndex - 1); // Swipe right -> prev
                    }
                }
            }
        });

        // Keyboard Shortcuts
        $(document).on('keydown', function(e) {
            if (!isOpen) return;

            switch (e.key) {
                case 'Escape':
                    e.preventDefault();
                    closeLightbox();
                    break;
                case 'ArrowLeft':
                    e.preventDefault();
                    loadSlide(currentIndex - 1);
                    break;
                case 'ArrowRight':
                    e.preventDefault();
                    loadSlide(currentIndex + 1);
                    break;
                case '+':
                case '=':
                    e.preventDefault();
                    zoomIn();
                    break;
                case '-':
                case '_':
                    e.preventDefault();
                    zoomOut();
                    break;
                case '0':
                    e.preventDefault();
                    resetZoom(true);
                    break;
                case 'f':
                case 'F':
                    e.preventDefault();
                    toggleFullscreen();
                    break;
                case 't':
                case 'T':
                    e.preventDefault();
                    $thumbsWrap.slideToggle(180);
                    break;
            }
        });
    }

    /**
     * Collect gallery items from DOM elements
     */
    function parseGalleryFromDOM($triggers) {
        var items = [];
        $triggers.each(function(idx) {
            var $el = $(this);
            var src = $el.attr('data-src') || $el.attr('href') || $el.find('img').attr('src') || '';
            if (!src || src === '#' || src.startsWith('javascript:')) return;

            var title = $el.attr('data-title') || $el.attr('title') || $el.find('.title').text() || $el.find('img').attr('alt') || 'Technical Diagram';
            var category = $el.attr('data-category') || $el.attr('data-tag') || $el.find('.tag').text() || '';
            var description = $el.attr('data-description') || $el.attr('data-desc') || $el.find('p').text() || '';
            var repo = $el.attr('data-repo') || $el.attr('data-github') || '';
            var tagsAttr = $el.attr('data-tags');
            var tags = tagsAttr ? tagsAttr.split(',').map(function(s) { return s.trim(); }) : [];

            items.push({
                src: src,
                title: $.trim(title),
                category: $.trim(category),
                description: $.trim(description),
                repo: $.trim(repo),
                tags: tags
            });

            // Set index reference
            $el.attr('data-hv-idx', idx);
        });
        return items;
    }

    /**
     * Auto-bind lightbox triggers on document ready
     */
    function autoBindTriggers() {
        initDOM();

        // 1. Bind portfolio projects gallery
        var $portfolioCards = $('.projects-wrapper .work-container, .projects-wrapper .card, [data-gallery="portfolio"]');
        if ($portfolioCards.length) {
            var portfolioItems = [];
            $portfolioCards.each(function(idx) {
                var $card = $(this);
                var $img = $card.find('img');
                var $mfp = $card.find('.mfp-image, .work-icon');
                var src = $mfp.attr('href') || $img.attr('src') || '';
                var title = $card.find('.title').text() || $img.attr('alt') || 'Architecture Diagram';
                var category = $card.find('.tag').text() || 'System Architecture';
                var repo = $card.find('.title a').attr('href') || $card.find('a[href*="github.com"]').attr('href') || '';
                var desc = $card.attr('data-description') || 'High-resolution technical architecture diagram and engineering pipeline specification.';

                portfolioItems.push({
                    src: src,
                    title: $.trim(title),
                    category: $.trim(category),
                    description: $.trim(desc),
                    repo: $.trim(repo),
                    tags: [$.trim(category), 'Distributed Architecture']
                });

                // Add interactive diagram expand badge if not present
                if (!$card.find('.hv-diagram-expand-badge').length) {
                    var $badgeBtn = $('<a href="' + src + '" class="hv-diagram-expand-badge hv-lightbox-trigger" title="Inspect Fullscreen Architecture Diagram" data-gallery="portfolio" data-idx="' + idx + '">' +
                                      '<i class="mdi mdi-fullscreen"></i> <span>Fullscreen Diagram</span>' +
                                      '</a>');
                    $card.find('.card-body, .work-container').first().append($badgeBtn);
                }

                // Click handler on card image & icons
                $card.find('img, .work-icon, .hv-diagram-expand-badge, .overlay-work').on('click', function(e) {
                    // If target is direct github link, let it open
                    if ($(e.target).closest('a[href*="github.com"]').length) return;

                    e.preventDefault();
                    e.stopPropagation();
                    e.stopImmediatePropagation();
                    openLightbox(portfolioItems, idx);
                    return false;
                });
            });
        }

        // 2. Bind home projects grid (#homeProjectsGrid)
        var $homeCards = $('#homeProjectsGrid .home-proj-card');
        if ($homeCards.length) {
            var homeItems = [];
            $homeCards.each(function(idx) {
                var $c = $(this);
                var $img = $c.find('.proj-thumb-img');
                var src = $img.attr('src') || '';
                var title = $c.find('.proj-title-link').text() || $img.attr('alt') || 'Project Diagram';
                var category = $c.find('.badge').first().text() || 'Architecture';
                var desc = $c.find('p').first().text() || '';
                var repo = $c.find('a[href*="github.com"]').first().attr('href') || '';
                var tags = [];
                $c.find('.badge-light').each(function() {
                    tags.push($(this).text().trim());
                });

                homeItems.push({
                    src: src,
                    title: $.trim(title),
                    category: $.trim(category),
                    description: $.trim(desc),
                    repo: $.trim(repo),
                    tags: tags
                });

                // Add expand badge to thumbnail wrapper if missing
                var $thumbWrap = $c.find('.proj-thumb-wrapper');
                if ($thumbWrap.length && !$thumbWrap.find('.hv-diagram-expand-badge').length) {
                    var $badgeBtn = $('<div class="hv-diagram-expand-badge" title="Inspect Fullscreen Architecture Diagram">' +
                                      '<i class="mdi mdi-fullscreen"></i> <span>Fullscreen Diagram</span>' +
                                      '</div>');
                    $thumbWrap.append($badgeBtn);
                }

                // Make thumbnail wrapper and expand badge trigger the lightbox
                $thumbWrap.addClass('hv-lightbox-clickable').on('click', function(e) {
                    // If user specifically clicked GitHub or details button inside overlay
                    if ($(e.target).closest('a.btn').length) return;

                    e.preventDefault();
                    e.stopPropagation();
                    openLightbox(homeItems, idx);
                });
            });
        }

        // 3. Bind certification cards gallery (#certifications)
        var $certItems = $('.cert-grid-item');
        if ($certItems.length) {
            var certGallery = [];
            $certItems.each(function(idx) {
                var $ci = $(this);
                var src = $ci.find('.cert-zoom-btn').attr('href') || $ci.find('.cert-card-img').attr('src') || '';
                var title = $ci.find('.cert-card-title').text() || $ci.find('.cert-card-img').attr('alt') || 'Certification';
                var org = $ci.find('.cert-issuer-name').text() || 'Credential Issuer';
                var desc = $ci.find('.cert-card-desc').text() || 'Verified professional credential and advanced specialization accomplishment.';
                var certLink = $ci.find('.cert-verify-link').attr('href') || '';

                certGallery.push({
                    src: src,
                    title: $.trim(title),
                    category: 'VERIFIED CREDENTIAL • ' + $.trim(org).toUpperCase(),
                    description: $.trim(desc),
                    repo: certLink,
                    tags: [$.trim(org), 'Credential', 'Specialization']
                });

                // Intercept cert inspect / zoom buttons
                $ci.find('.cert-zoom-btn, .cert-overlay-preview-link, .btn-inspect-cert, .cert-card-img-wrap').on('click', function(e) {
                    e.preventDefault();
                    e.stopPropagation();
                    e.stopImmediatePropagation();
                    openLightbox(certGallery, idx);
                    return false;
                });
            });
        }

        // 4. Intercept all remaining .mfp-image links across the entire site
        // This ensures ANY legacy or dynamic .mfp-image link seamlessly opens the fullscreen modal
        $(document).on('click', '.mfp-image', function(e) {
            var $this = $(this);
            // If already handled by card handler, ignore
            if ($this.closest('.cert-grid-item, .projects-wrapper, #homeProjectsGrid').length) {
                return;
            }

            e.preventDefault();
            e.stopPropagation();
            e.stopImmediatePropagation();

            var src = $this.attr('href') || $this.attr('data-src');
            var title = $this.attr('title') || $this.attr('data-title') || 'Diagram Preview';

            // Find siblings to form a gallery if part of a group
            var $group = $this.closest('.row, .port-images, .gallery, section').find('.mfp-image');
            if ($group.length > 1) {
                var groupItems = [];
                var startIndex = 0;
                $group.each(function(i) {
                    var $g = $(this);
                    var gSrc = $g.attr('href') || $g.attr('data-src');
                    if (gSrc === src) startIndex = i;
                    groupItems.push({
                        src: gSrc,
                        title: $g.attr('title') || 'Technical Screenshot ' + (i + 1),
                        category: 'TECHNICAL ARTIFACT',
                        description: 'System architectural diagram and high-resolution engineering screenshot.',
                        repo: '',
                        tags: ['Engineering Artifact', 'Architecture']
                    });
                });
                openLightbox(groupItems, startIndex);
            } else {
                openLightbox([{
                    src: src,
                    title: title,
                    category: 'TECHNICAL ARTIFACT',
                    description: 'System architectural diagram and high-resolution engineering screenshot.',
                    repo: '',
                    tags: ['Architecture']
                }], 0);
            }

            return false;
        });
    }

    // Expose Global API
    window.HVLightbox = {
        open: openLightbox,
        close: closeLightbox,
        next: function() { loadSlide(currentIndex + 1); },
        prev: function() { loadSlide(currentIndex - 1); },
        zoomIn: zoomIn,
        zoomOut: zoomOut,
        resetZoom: resetZoom,
        toggleFullscreen: toggleFullscreen,
        refresh: autoBindTriggers
    };

    // Auto initialize on DOM ready
    $(document).ready(function() {
        autoBindTriggers();
    });

})(window, document, window.jQuery || window.$);
