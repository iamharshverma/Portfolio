/*-----------------------------------------------------------
* Template Name    : Klee - vCard / Resume / CV Template
* Author           : beingeorge
* Version          : 1.0
* Created          : Jan 2020
* File Description : Main Js file of the template
*------------------------------------------------------------
*/

! function($) {
    "use strict";

    /* ---------------------------------------------- /*
    * Preloader
    /* ---------------------------------------------- */

    $(window).on('load', function() {
        $('#preloader').addClass("loaded");
        $('.line-drop').fadeOut('slow');
    });

    /* ---------------------------------------------- /*
    * Section Scroll - Navbar
    /* ---------------------------------------------- */
    
    $('.navbar-nav a').on('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top - 0
        }, 1500, 'easeInOutExpo');

        if($('.navbar').hasClass('active')){
            $('.navbar').removeClass('active')
            $('.ham').removeClass('active')
        }

        event.preventDefault();
    });

    $('.navbar-toggler').on('click', function(){
        $('body').toggleClass('aside-open');
        $(".ham").toggleClass('active');
    });

    /* ---------------------------------------------- /*
    * Scroll Spy - init
    /* ---------------------------------------------- */

    $("#navbarCollapse").scrollspy({
        offset:20
    });

    /* ---------------------------------------------- /*
    * Magnific Popup - Init
    /* ---------------------------------------------- */

    $('.simple-ajax-popup').magnificPopup({
        type: 'image',
        closeOnContentClick: true,
        mainClass: 'mfp-fade',
        gallery: {
            enabled: true,
            navigateByImgClick: true,
            preload: [0, 1]
        },
        zoom: {
            enabled: true,

            duration: 300,
            easing: 'ease-in-out',

            opener: function(openerElement) {
                return openerElement.is('img') ? openerElement : openerElement.find('img');
            }
        }
    });

/* ---------------------------------------------- /*
* Initialize shuffle plugin
/* ---------------------------------------------- */

var $portfolioContainer = $('.list-items-container');

$('#filter li').on('click', function (e) {
    e.preventDefault();

    $('#filter li').removeClass('active');
    $(this).addClass('active');

    var group = $(this).attr('data-group');
    var groupName = $(this).attr('data-group');

    $portfolioContainer.shuffle('shuffle', groupName );
});


// $(document).ready( function() {

//     $('.simple-ajax-popup').magnificPopup({
//         type: 'image',
//         gallery:{enabled:true}
//     });

// });

    /* ---------------------------------------------- /*
    * Swipper - Init
    /* ---------------------------------------------- */

    // Testimony init

    var swipertest = new Swiper('.swiper-testimony', {
        spaceBetween: 30,
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
    });

    // Blog Init

    var swipert = new Swiper('.swiper-blog', {
        slidesPerView: 'auto',
        spaceBetween: 30
    });

    // Home Banner Init

    var swiper = new Swiper('.swiper-home', {
        spaceBetween: 3,
        effect: 'fade',
        pagination: {
            el: '.home-pagination',
            clickable: true,
        }
    });

    /* ---------------------------------------------- /*
    * Parallax - Init
    /* ---------------------------------------------- */

    $(".js-height-full").height($(window).height());

    $(window).resize(function(){
        $(".js-height-full").height($(window).height());
    });

    if (/Android|webOS|iPhone|iPad|iPod|BlackBerry/i.test(navigator.userAgent)) {
        $('#home').css({'background-attachment': 'scroll'});
    } else {
        $('#home').parallax('50%', -0.3);
    }

    if($('.section-home').length) {
        if (/Android|webOS|iPhone|iPad|iPod|BlackBerry/i.test(navigator.userAgent)) {
            $('.swiper-slide').css({'background-attachment': 'scroll'});
        } else {
            $('.swiper-slide').parallax('50%', -0.3);
        }        
    }

    /* ---------------------------------------------- /*
    * AnimateOnScroll - Init
    /* ---------------------------------------------- */

    var wow = new WOW(
      {
        boxClass:     'wow',      // animated element css class (default is wow)
        animateClass: 'animated', // animation css class (default is animated)
        offset:       0,          // distance to the element when triggering the animation (default is 0)
        mobile:       true,       // trigger animations on mobile devices (default is true)
        live:         true,       // act on asynchronously loaded content (default is true)
        callback:     function(box) {
          // the callback is fired every time an animation is started
          // the argument that is passed in is the DOM node being animated
        },
        scrollContainer: null,    // optional scroll container selector, otherwise use window,
        resetAnimation: true,     // reset animation on end (default is true)
      }
    );
    wow.init();

    /* ---------------------------------------------- /*
    * Youtub Player
    /* ---------------------------------------------- */


    if($('.youtube-bg').length) {
        $(".youtube-bg").mb_YTPlayer();
    }

    /* ---------------------------------------------- /*
    * Color Switcher
    /* ---------------------------------------------- */


    $('.switcher a').on("click",function(e) {
        e.preventDefault();

        if($(this).attr('data-theme') == 'light' ) {
            $(this).attr('data-theme', 'dark');
            $('head').append('<link rel="stylesheet" href="assets/css/Lucy-dark.css">');
        } else {
            $(this).attr('data-theme', 'light');
            $('head').append('<link rel="stylesheet" href="assets/css/Lucy-light.css">');
        }

    });

    // about-desc-info

    $('.about-desc-info').hover(
        function(e){$(this).find('[data-toggle="tooltip"]').tooltip('show');},
        function(e){$(this).find('[data-toggle="tooltip"]').tooltip('hide');}
    );

    /* ---------------------------------------------- /*
    * Initialize shuffle plugin
    /* ---------------------------------------------- */

    var $portfolioContainer = $('.list-items-container');

    $('#filter li').on('click', function (e) {
        e.preventDefault();

        $('#filter li').removeClass('active');
        $(this).addClass('active');

        var group = $(this).attr('data-group');
        var groupName = $(this).attr('data-group');

        $portfolioContainer.shuffle('shuffle', groupName );
    });


    $(document).ready( function() {

        $('.simple-ajax-popup').magnificPopup({
            type: 'image',
            gallery:{enabled:true}
        });

    });

    /* ---------------------------------------------- /*
    *  Color Switcher
    /* ---------------------------------------------- */

    $('.toggle-theme-panel').on("click",function(e) {
        e.preventDefault();
        $('.settings_panel').toggleClass('active');
    });
    
    $('.colors-switch a').on("click",function(e) {
        $('#preloader').removeClass("loaded");
        setTimeout(function(){
            $('#preloader').addClass("loaded");    
        }, 1500)
        e.preventDefault();
        var attr = $(this).attr("title");
        console.log(attr);
        $('head').append('<link rel="stylesheet" href="assets/css/'+attr+'.css">');
    });


}(window.jQuery);

