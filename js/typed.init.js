
// Typed Text
(function($) {
    "use strict";
    if (typeof $.fn.typed !== 'undefined') {
        $(".element").each(function(){
            var $this = $(this);
            var dataElems = $this.attr('data-elements');
            if (dataElems) {
                $this.typed({
                    strings: dataElems.split(','),
                    typeSpeed: 100, // typing speed
                    backDelay: 3000 // pause before backspacing
                });
            }
        });
    }
})(jQuery);