/**
 * hv-advisory.js
 * Client-side interactivity for Board & Strategic Advisory Hub
 * Manages counter animations, mandate inquiry modal, and bio modal interactions
 */

(function () {
    'use strict';

    // 1. Animated Metric Counters
    function initAdvisoryCounters() {
        var counters = document.querySelectorAll('.advisory-metric-num[data-target]');
        if (!counters.length) return;

        var observer = new IntersectionObserver(function (entries, obs) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    var el = entry.target;
                    var target = parseInt(el.getAttribute('data-target'), 10) || 0;
                    var suffix = el.getAttribute('data-suffix') || '+';
                    var duration = 1600;
                    var start = 0;
                    var startTime = null;

                    function step(timestamp) {
                        if (!startTime) startTime = timestamp;
                        var progress = Math.min((timestamp - startTime) / duration, 1);
                        var current = Math.floor(progress * target);
                        el.innerHTML = current + '<span class="plus-accent">' + suffix + '</span>';
                        if (progress < 1) {
                            window.requestAnimationFrame(step);
                        } else {
                            el.innerHTML = target + '<span class="plus-accent">' + suffix + '</span>';
                        }
                    }

                    window.requestAnimationFrame(step);
                    obs.unobserve(el);
                }
            });
        }, { threshold: 0.3 });

        counters.forEach(function (c) {
            observer.observe(c);
        });
    }

    // 2. Open Advisory Modal with pre-selected mandate
    window.openAdvisoryModal = function (mandateName) {
        var modalEl = document.getElementById('advisoryInquiryModal');
        if (!modalEl) return;

        if (mandateName) {
            // Update select or active pill
            var selectEl = document.getElementById('advisoryMandateSelect');
            if (selectEl) {
                for (var i = 0; i < selectEl.options.length; i++) {
                    if (selectEl.options[i].text.toLowerCase().indexOf(mandateName.toLowerCase()) !== -1 ||
                        selectEl.options[i].value.toLowerCase().indexOf(mandateName.toLowerCase()) !== -1) {
                        selectEl.selectedIndex = i;
                        break;
                    }
                }
            }

            var pills = document.querySelectorAll('.mandate-pill-opt');
            pills.forEach(function (pill) {
                if (pill.getAttribute('data-mandate') === mandateName) {
                    pill.classList.add('active');
                } else {
                    pill.classList.remove('active');
                }
            });
        }

        // Reset any prior submission message
        var form = document.getElementById('advisoryInquiryForm');
        var successBox = document.getElementById('advisorySuccessBox');
        if (form) form.style.display = 'block';
        if (successBox) successBox.style.display = 'none';

        if (window.$ && typeof $(modalEl).modal === 'function') {
            $(modalEl).modal('show');
        } else {
            modalEl.classList.add('show');
            modalEl.style.display = 'block';
            document.body.classList.add('modal-open');
        }
    };

    window.closeAdvisoryModal = function () {
        var modalEl = document.getElementById('advisoryInquiryModal');
        if (!modalEl) return;
        if (window.$ && typeof $(modalEl).modal === 'function') {
            $(modalEl).modal('hide');
        } else {
            modalEl.classList.remove('show');
            modalEl.style.display = 'none';
            document.body.classList.remove('modal-open');
        }
    };

    window.selectMandatePill = function (btn, mandateValue) {
        var pills = document.querySelectorAll('.mandate-pill-opt');
        pills.forEach(function (p) { p.classList.remove('active'); });
        btn.classList.add('active');

        var selectEl = document.getElementById('advisoryMandateSelect');
        if (selectEl) {
            selectEl.value = mandateValue;
        }
    };

    // 3. Form Submission Handling
    window.handleAdvisorySubmit = function (event) {
        event.preventDefault();
        var form = event.target;
        var nameInput = document.getElementById('advName');
        var orgInput = document.getElementById('advOrg');
        var emailInput = document.getElementById('advEmail');
        var mandateInput = document.getElementById('advisoryMandateSelect');
        var notesInput = document.getElementById('advNotes');

        if (!nameInput.value.trim() || !emailInput.value.trim() || !orgInput.value.trim()) {
            alert('Please provide your name, organization, and business email.');
            return false;
        }

        var submitBtn = document.getElementById('advisorySubmitBtn');
        if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<i class="mdi mdi-loading mdi-spin mr-1"></i> Transmitting Inquiry...';
        }

        setTimeout(function () {
            form.style.display = 'none';
            var successBox = document.getElementById('advisorySuccessBox');
            if (successBox) {
                successBox.style.display = 'block';
                var refCode = 'ADV-' + Math.floor(100000 + Math.random() * 900000);
                var refCodeEl = document.getElementById('advRefCode');
                if (refCodeEl) refCodeEl.textContent = refCode;
            }
            if (submitBtn) {
                submitBtn.disabled = false;
                submitBtn.innerHTML = 'Submit Advisory Mandate Inquiry';
            }
            form.reset();
        }, 800);

        return false;
    };

    // 4. Board Biography Modal / Download Handling
    window.openBoardBioModal = function () {
        var modalEl = document.getElementById('boardBioModal');
        if (!modalEl) return;
        if (window.$ && typeof $(modalEl).modal === 'function') {
            $(modalEl).modal('show');
        } else {
            modalEl.classList.add('show');
            modalEl.style.display = 'block';
            document.body.classList.add('modal-open');
        }
    };

    window.closeBoardBioModal = function () {
        var modalEl = document.getElementById('boardBioModal');
        if (!modalEl) return;
        if (window.$ && typeof $(modalEl).modal === 'function') {
            $(modalEl).modal('hide');
        } else {
            modalEl.classList.remove('show');
            modalEl.style.display = 'none';
            document.body.classList.remove('modal-open');
        }
    };

    // Initialize on DOMContentLoaded
    document.addEventListener('DOMContentLoaded', function () {
        initAdvisoryCounters();
    });

})();
