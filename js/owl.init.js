//Owl Carousel
(function($) {
  "use strict";
  if (typeof $.fn.owlCarousel !== 'undefined') {
    if ($('#customer-testi').length) {
      $('#customer-testi').owlCarousel({
        loop:true,
        nav: false,
        dots: true,
        autoplay:true,
        autoplayTimeout:3000,
        autoplayHoverPause:true,
        responsive:{
          0:{ items:1 },
          600:{ items:2 },
          1000:{ items:3 }
        }
      });
    }

    if ($('#client-four').length) {
      $('#client-four').owlCarousel({
        loop:true,
        nav: false,
        dots: true,
        autoplay:true,
        autoplayTimeout:3000,
        autoplayHoverPause:true,
        responsive:{
          0:{ items:1 },
          600:{ items:2 },
          1000:{ items:4 }
        }
      });
    }

    if ($('#owl-fade').length) {
      $('#owl-fade').owlCarousel({
        loop:true,
        nav: false,
        dots: true,
        autoplay:true,
        autoplayTimeout:3000,
        autoplayHoverPause:true,
        animateOut: 'fadeOut',
        items: 1
      });
    }

    if ($('#single-owl').length) {
      $('#single-owl').owlCarousel({
        loop:true,
        nav: false,
        dots: true,
        autoplay:true,
        autoplayTimeout:5000,
        autoplayHoverPause:true,
        items: 1
      });
    }
  }
})(jQuery);