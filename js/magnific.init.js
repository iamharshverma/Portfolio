//Cta Video
if (typeof $.fn.magnificPopup !== 'undefined') {
    $('.map-popup-view').magnificPopup({
        disableOn: 375,
        type: 'iframe',
        mainClass: 'mfp-fade',
        removalDelay: 160,
        preloader: false,
        fixedContentPos: false,
    });
}