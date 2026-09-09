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
    
}(jQuery)