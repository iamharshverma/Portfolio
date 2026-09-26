/* Template Name: Queue - Personal Portfolio Template
   Author: Zoyothemes
   E-mail: zoyothemes@gmail.com
   Created: Jun 2019
   Version: 1.0
   File Description: Main JS file of the template
*/


/*--------------------------*/
/*         INDEX            */
/*###########################
 *     01.  Loader          *
 *     02.  Menu            *
 *     03.  Sticky Menu     *
 *     03.  Back to top     *
############################*/

! function($) {
    "use strict"; 
    // Loader 
    $(window).on('load', function() {
        $('#status').fadeOut();
        $('#preloader').delay(350).fadeOut('slow');
        $('body').delay(350).css({
            'overflow': 'visible'
        });
    });

    // Navbar-toggle Menu
    $('.navbar-toggle').on('click', function (event) {
        $(this).toggleClass('open');
        $('#navbar-nav').slideToggle(400);
    });


    // Sticky Menu
    $(window).scroll(function() {
        var scroll = $(window).scrollTop();

        if (scroll >= 50) {
            $(".sticky").addClass("nav-sticky");
        } else {
            $(".sticky").removeClass("nav-sticky");
        }
    });

    // Smooth scrolling for valid in-page links
    $('.navbar-nav a, .mouse-down').on('click', function(event) {
        var href = $(this).attr('href');
        if (!href || href === '#' || href.startsWith('javascript:')) {
            return;
        }

        // Check if the link contains a hash for in-page navigation
        var hash = '';
        if (href.indexOf('#') !== -1) {
            var parts = href.split('#');
            var path = parts[0];
            hash = '#' + parts[1];

            var currentPath = window.location.pathname;
            var isCurrentPage = (path === '' || path === 'index' || path === 'index.html' || 
                                currentPath.endsWith(path) || 
                                (currentPath === '/' && (path === 'index' || path === 'index.html')));

            if (isCurrentPage && hash && hash.length > 1) {
                try {
                    var $target = $(hash);
                    if ($target && $target.length) {
                        var targetOff = $target.offset();
                        if (targetOff && typeof targetOff.top === 'number') {
                            event.preventDefault();
                            $('html, body').stop().animate({
                                scrollTop: targetOff.top - 70
                            }, 1200, 'easeInOutExpo');
                        }
                    }
                } catch (e) {
                    // Not a valid jQuery selector, ignore and let default navigation occur
                }
            }
        }
    });

    // Scrollspy
    if (typeof $.fn.scrollspy !== 'undefined') {
        $(".navbar-nav").scrollspy({ offset: 70 });
    }

    // Back to top
    $(window).scroll(function(){
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn();
        } else {
            $('.back-to-top').fadeOut();
        }
    }); 
    $('.back-to-top').click(function(){
        $("html, body").animate({ scrollTop: 0 }, 3000);
        return false;
    }); 

    // Feather icon
    if (typeof feather !== 'undefined') {
        feather.replace();
    }

    // Lightbox Modal System
    if (typeof window.HVLightbox !== 'undefined') {
        window.HVLightbox.refresh();
    } else if (typeof $.fn.magnificPopup !== 'undefined') {
        $('.mfp-image').magnificPopup({
            type: 'image',
            closeOnContentClick: true,
            mainClass: 'mfp-fade',
            gallery: {
                enabled: true,
                navigateByImgClick: true,
                preload: [0, 1]
            }
        });
    }

    // Portfolio filter
    $(window).on('load', function() {
        var $container = $('.projects-wrapper');
        var $filter = $('#filter');
        if ($container.length && typeof $.fn.isotope !== 'undefined') {
            $container.isotope({
                filter: '*',
                layoutMode: 'masonry',
                animationOptions: {
                    duration: 750,
                    easing: 'linear'
                }
            });
            $filter.find('a').click(function() {
                var selector = $(this).attr('data-filter');
                $filter.find('a').removeClass('active');
                $(this).addClass('active');

                // GA4 Event Tracking for Project Filter
                if (window.AnalyticsService) {
                    var label = $(this).text().trim();
                    window.AnalyticsService.trackProjectFilter(selector, {
                        label: label,
                        page: 'portfolio_page'
                    });
                }

                $container.isotope({
                    filter: selector,
                    animationOptions: {
                        animationDuration: 750,
                        easing: 'linear',
                        queue: false,
                    }
                });
                return false;
            });
        }
    });
    
}(jQuery);

/* ==========================================================================
   Footer Newsletter Subscription & RSS Feed Reader Modal Logic
   ========================================================================== */
window.handleFooterNewsletterSubmit = async function(e) {
    if (e && e.preventDefault) e.preventDefault();
    var input = document.getElementById('footerNewsletterEmail');
    var btn = document.getElementById('footerSubscribeBtn');
    var feedback = document.getElementById('footerNewsletterFeedback');
    
    if (!input) return false;
    var email = (input.value || '').trim();
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    
    if (!email || !emailRegex.test(email)) {
        if (feedback) {
            feedback.style.display = 'block';
            feedback.className = 'footer-newsletter-feedback mt-2 text-center small font-weight-medium text-danger';
            feedback.innerHTML = '<i class="mdi mdi-alert-circle mr-1"></i> Please enter a valid business or personal email.';
        }
        input.focus();
        return false;
    }
    
    var btnText = btn ? btn.querySelector('.btn-text') : null;
    var btnSpinner = btn ? btn.querySelector('.btn-spinner') : null;
    if (btn) btn.disabled = true;
    if (btnText) btnText.classList.add('d-none');
    if (btnSpinner) btnSpinner.classList.remove('d-none');
    if (feedback) feedback.style.display = 'none';

    try {
        var res = await fetch('/api/newsletter/subscribe', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                email: email,
                source: 'footer_newsletter_input',
                topics: ['Agentic AI & Systems Architecture', 'Technical Articles & Deep Dives']
            })
        });
        var data = await res.json();
        if (data.success) {
            input.value = '';
            if (feedback) {
                feedback.style.display = 'block';
                feedback.className = 'footer-newsletter-feedback mt-2 text-center small font-weight-medium text-success';
                feedback.innerHTML = '<i class="mdi mdi-check-circle mr-1"></i> ' + (data.message || 'Subscribed successfully! Welcome to The Dispatch.');
            }
            try {
                localStorage.setItem('hv_newsletter_subscriber_state', JSON.stringify({
                    subscribed: true,
                    email: email,
                    subscribedAt: Date.now()
                }));
            } catch (err) {}
        } else {
            if (feedback) {
                feedback.style.display = 'block';
                feedback.className = 'footer-newsletter-feedback mt-2 text-center small font-weight-medium text-danger';
                feedback.innerHTML = '<i class="mdi mdi-alert-circle mr-1"></i> ' + (data.error || 'Subscription failed. Please try again.');
            }
        }
    } catch (err) {
        if (feedback) {
            feedback.style.display = 'block';
            feedback.className = 'footer-newsletter-feedback mt-2 text-center small font-weight-medium text-danger';
            feedback.innerHTML = '<i class="mdi mdi-alert-circle mr-1"></i> Network error. Please try again.';
        }
    } finally {
        if (btn) btn.disabled = false;
        if (btnText) btnText.classList.remove('d-none');
        if (btnSpinner) btnSpinner.classList.add('d-none');
    }
    return false;
};

// Footer RSS Feed Subscription Helper
window.handleFooterRssClick = function(e) {
    // If user holding Ctrl/Cmd or middle click, allow normal open in new tab
    if (e && (e.ctrlKey || e.metaKey || e.button === 1)) {
        return;
    }
    if (e && e.preventDefault) e.preventDefault();
    openRssModal();
};

window.openRssModal = function() {
    var modal = document.getElementById('hvRssHubModal');
    var feedUrl = window.location.origin + '/rss.xml';
    
    if (!modal) {
        var modalHtml = '<div class="modal fade rss-hub-modal" id="hvRssHubModal" tabindex="-1" role="dialog" aria-labelledby="hvRssModalTitle" aria-hidden="true">' +
            '<div class="modal-dialog modal-dialog-centered" role="document">' +
              '<div class="modal-content border-0">' +
                '<div class="rss-hub-header d-flex align-items-center justify-content-between">' +
                  '<div class="d-flex align-items-center">' +
                    '<div class="rss-modal-badge mr-3" style="width: 38px; height: 38px; border-radius: 10px; background: linear-gradient(135deg, #f97316 0%, #ea580c 100%); display: flex; align-items: center; justify-content: center; color: #fff;">' +
                      '<i class="mdi mdi-rss" style="font-size: 20px;"></i>' +
                    '</div>' +
                    '<div>' +
                      '<h6 class="modal-title font-weight-bold mb-0 text-dark" id="hvRssModalTitle">Subscribe via RSS Feed</h6>' +
                      '<small class="text-muted">Follow 29+ Technical Articles in Your RSS Reader</small>' +
                    '</div>' +
                  '</div>' +
                  '<button type="button" class="close" data-dismiss="modal" aria-label="Close" style="outline: none;">' +
                    '<span aria-hidden="true">&times;</span>' +
                  '</button>' +
                '</div>' +
                '<div class="modal-body p-4">' +
                  '<p class="small text-muted mb-3">' +
                    'Add Harsh Verma\'s technical publications feed to Feedly, Inoreader, NetNewsWire, Readwise, or any standard RSS 2.0 / Atom reader.' +
                  '</p>' +
                  '<label class="font-weight-bold small text-dark mb-1">Direct RSS Feed URL:</label>' +
                  '<div class="input-group mb-3">' +
                    '<input type="text" class="form-control font-weight-medium bg-light" id="rssFeedUrlInput" value="' + feedUrl + '" readonly style="font-size: 13px; font-family: monospace;">' +
                    '<div class="input-group-append">' +
                      '<button class="btn btn-outline-secondary font-weight-semibold" type="button" id="copyRssBtn" onclick="copyRssFeedUrl()">' +
                        '<i class="mdi mdi-content-copy mr-1"></i> <span id="copyRssBtnText">Copy</span>' +
                      '</button>' +
                    '</div>' +
                  '</div>' +
                  '<label class="font-weight-bold small text-dark mb-2">One-Click Reader Subscription:</label>' +
                  '<div class="d-flex flex-wrap" style="gap: 8px;">' +
                    '<a href="https://feedly.com/i/subscription/feed/' + encodeURIComponent(feedUrl) + '" target="_blank" rel="noopener noreferrer" class="btn btn-sm btn-outline-dark rounded-pill px-3 py-1 font-weight-medium">' +
                      '<i class="mdi mdi-newspaper mr-1 text-success"></i> Add to Feedly' +
                    '</a>' +
                    '<a href="https://www.inoreader.com/feed/' + encodeURIComponent(feedUrl) + '" target="_blank" rel="noopener noreferrer" class="btn btn-sm btn-outline-dark rounded-pill px-3 py-1 font-weight-medium">' +
                      '<i class="mdi mdi-radio-tower mr-1 text-primary"></i> Add to Inoreader' +
                    '</a>' +
                    '<a href="' + feedUrl + '" target="_blank" rel="noopener noreferrer" class="btn btn-sm btn-outline-warning rounded-pill px-3 py-1 font-weight-medium text-dark">' +
                      '<i class="mdi mdi-xml mr-1 text-warning"></i> View Raw XML' +
                    '</a>' +
                  '</div>' +
                '</div>' +
                '<div class="modal-footer bg-light py-2 px-4 d-flex justify-content-between">' +
                  '<small class="text-muted"><i class="mdi mdi-check-circle-outline text-success mr-1"></i> RSS 2.0 &amp; Atom Syndication</small>' +
                  '<button type="button" class="btn btn-secondary btn-sm rounded-pill px-3" data-dismiss="modal">Close</button>' +
                '</div>' +
              '</div>' +
            '</div>' +
          '</div>';
        document.body.insertAdjacentHTML('beforeend', modalHtml);
        modal = document.getElementById('hvRssHubModal');
    } else {
        var input = document.getElementById('rssFeedUrlInput');
        if (input) input.value = feedUrl;
    }
    
    if (window.$ && typeof window.$(modal).modal === 'function') {
        window.$(modal).modal('show');
    } else {
        window.open(feedUrl, '_blank');
    }
};

window.copyRssFeedUrl = function() {
    var input = document.getElementById('rssFeedUrlInput');
    var feedUrl = input ? input.value : (window.location.origin + '/rss.xml');
    var btnText = document.getElementById('copyRssBtnText');
    
    if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(feedUrl).then(function() {
            if (btnText) btnText.innerHTML = '<i class="mdi mdi-check text-success"></i> Copied!';
            setTimeout(function() {
                if (btnText) btnText.innerText = 'Copy';
            }, 2500);
        }).catch(function() {
            fallbackCopy(input, btnText);
        });
    } else {
        fallbackCopy(input, btnText);
    }
};

function fallbackCopy(input, btnText) {
    if (input) {
        input.select();
        input.setSelectionRange(0, 99999);
        try {
            document.execCommand('copy');
            if (btnText) btnText.innerHTML = '<i class="mdi mdi-check text-success"></i> Copied!';
            setTimeout(function() {
                if (btnText) btnText.innerText = 'Copy';
            }, 2500);
        } catch (e) {}
    }
}
