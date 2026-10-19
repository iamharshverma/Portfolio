/**
 * hv-advisory.js
 * Client-side interactivity for Board & Strategic Advisory Hub
 * Manages counter animations, mandate inquiry modal, bio modal, and interactive infographics
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
                    var duration = 1500;
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

    // 2. Interactive Strategic Flywheel Quadrant Selector
    window.selectFlywheelQuadrant = function (qNum) {
        var quadrants = document.querySelectorAll('.flywheel-quadrant');
        quadrants.forEach(function (q) {
            if (parseInt(q.getAttribute('data-quadrant'), 10) === qNum) {
                q.classList.add('active');
            } else {
                q.classList.remove('active');
            }
        });

        var details = {
            1: {
                title: "Frontier Technical Moat Architecture",
                deliverables: "Proprietary streaming data pipelines, custom regression eval datasets, vendor lock-in mitigation, and non-wrapper software defensibility.",
                boardFocus: "Strategic Technology Planning & IP Protection"
            },
            2: {
                title: "Zero-Trust Autonomous Security",
                deliverables: "Ephemeral agent execution sandboxes, continuous behavioral authorization, prompt injection defense, and MCP tool isolation.",
                boardFocus: "Cybersecurity & Enterprise Risk Oversight"
            },
            3: {
                title: "Institutional AI Governance & Safety",
                deliverables: "Automated red-teaming harnesses, algorithmic drift telemetry, EU AI Act compliance, and NIST AI RMF certification audits.",
                boardFocus: "Corporate Governance, Ethics & Audit Committees"
            },
            4: {
                title: "Capital Efficiency & Scaling Velocity",
                deliverables: "Multi-cloud model routing, token cost optimization (40%+ reduction), engineering talent acquisition, and syndicate investor readiness.",
                boardFocus: "Compensation, Growth & Capital Allocation"
            }
        };

        var detailBox = document.getElementById('flywheelDetailBox');
        if (detailBox && details[qNum]) {
            detailBox.innerHTML = '<div class="d-flex align-items-center justify-content-between mb-1">' +
                '<strong class="text-warning small text-uppercase" style="letter-spacing:0.8px;">' + details[qNum].boardFocus + '</strong>' +
                '<span class="badge badge-pill badge-primary px-2" style="font-size:10px;">Quadrant ' + qNum + '</span>' +
                '</div>' +
                '<h5 class="text-white font-weight-bold mb-2">' + details[qNum].title + '</h5>' +
                '<p class="text-light small mb-0" style="opacity:0.9;">' + details[qNum].deliverables + '</p>';
        }
    };

    // 3. Open Advisory Modal with pre-selected mandate
    window.openAdvisoryModal = function (mandateName) {
        var modalEl = document.getElementById('advisoryInquiryModal');
        if (!modalEl) return;

        if (mandateName) {
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

    // 4. Form Submission Handling
    window.handleAdvisorySubmit = function (event) {
        event.preventDefault();
        var nameInput = document.getElementById('advName');
        var orgInput = document.getElementById('advOrg');
        var emailInput = document.getElementById('advEmail');

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
            var form = document.getElementById('advisoryInquiryForm');
            if (form) form.style.display = 'none';
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
            if (form) form.reset();
        }, 600);

        return false;
    };

    // 5. Board Biography Modal / Download Handling
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
