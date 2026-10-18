//Cta Video
if (typeof window.$ !== 'undefined' && window.$.fn && typeof window.$.fn.magnificPopup !== 'undefined') {
    window.$('.map-popup-view').magnificPopup({
        disableOn: 375,
        type: 'iframe',
        mainClass: 'mfp-fade',
        removalDelay: 160,
        preloader: false,
        fixedContentPos: false,
    });
}