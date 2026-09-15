// ----- COUNTER ----- //
(function($) {
    "use strict";
    var a = 0;
    $(window).on('scroll', function() {
        var $counter = $('#counter');
        if (!$counter || !$counter.length) {
            return;
        }
        var offset = $counter.offset();
        if (!offset || typeof offset.top !== 'number') {
            return;
        }

        var oTop = offset.top - window.innerHeight;
        if (a === 0 && $(window).scrollTop() > oTop) {
            $('.counter-value').each(function() {
                var $this = $(this);
                var countTo = $this.attr('data-count');
                if (typeof countTo === 'undefined' || countTo === null) return;
                
                $({
                    countNum: $this.text()
                }).animate({
                    countNum: countTo
                }, {
                    duration: 2000,
                    easing: 'swing',
                    step: function() {
                        $this.text(Math.floor(this.countNum));
                    },
                    complete: function() {
                        $this.text(this.countNum);
                    }
                });
            });
            a = 1;
        }
    });
})(jQuery);