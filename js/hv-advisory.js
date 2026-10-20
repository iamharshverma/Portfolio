/**
 * hv-advisory.js
 * Client-side interactivity for Board & Strategic Advisory Hub
 * Manages counter animations, mandate inquiry modal, bio modal, interactive flywheel, and roadmap timeline
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
                '<h5 class="text-dark font-weight-bold mb-1">' + details[qNum].title + '</h5>' +
                '<p class="text-muted small mb-0">' + details[qNum].deliverables + '</p>';
        }
    };

    // 3. Interactive Roadmap Cadence Switcher with Stepper Synchronization
    var currentCadencePhase = 1;

    window.switchCadencePhase = function (phaseNum) {
        currentCadencePhase = phaseNum;

        // Update Step Boxes
        var stepBoxes = document.querySelectorAll('.cadence-step-box');
        stepBoxes.forEach(function (box) {
            if (parseInt(box.getAttribute('data-step'), 10) === phaseNum) {
                box.classList.add('active');
            } else {
                box.classList.remove('active');
            }
        });

        // Update Stepper Nodes and Progress Line
        var nodes = document.querySelectorAll('.roadmap-step-node');
        nodes.forEach(function (node) {
            var nVal = parseInt(node.getAttribute('data-node'), 10);
            if (nVal === phaseNum) {
                node.classList.add('active');
                node.classList.remove('completed');
            } else if (nVal < phaseNum) {
                node.classList.remove('active');
                node.classList.add('completed');
            } else {
                node.classList.remove('active', 'completed');
            }
        });

        var progressLine = document.getElementById('roadmapProgressLine');
        if (progressLine) {
            var pct = ((phaseNum - 1) / 3) * 100;
            progressLine.style.width = pct + '%';
        }

        var phaseData = {
            1: {
                phase: "Days 1–30: Diagnostic & Moat Evaluation",
                badgeClass: "badge-days-30",
                daysTag: "Days 1–30",
                title: "Deep-Dive Architecture & Moat Diagnostic",
                format: "2x 90-min technical architecture sessions + comprehensive codebase review",
                focus: "Rapid triage of technical debt, foundation model wrapper vulnerabilities, and data moat defensibility to calibrate executive priorities.",
                deliverables: [
                    "Technical debt & scalability bottleneck audit",
                    "Data moat defensibility & proprietary IP evaluation",
                    "Third-party API vulnerability & vendor lock-in mitigation plan",
                    "Immediate 90-day technical priority roadmap"
                ],
                stakeholders: "Founders, CTO, VP Engineering, Lead Architect",
                mandateType: "Startup Advisory Board"
            },
            2: {
                phase: "Days 31–60: Governance Baseline & Guardrails",
                badgeClass: "badge-days-60",
                daysTag: "Days 31–60",
                title: "Governance Baseline & Safety Guardrails",
                format: "Bi-weekly executive syncs + CISO/CTO architectural review",
                focus: "Institutionalizing automated evaluation harnesses and security guardrails to protect capital and regulatory posture.",
                deliverables: [
                    "Automated regression evaluation harness deployment",
                    "Zero-Trust agent behavioral authorization controls",
                    "EU AI Act & NIST AI RMF preliminary gap analysis",
                    "Executive risk telemetry dashboard for board visibility"
                ],
                stakeholders: "CEO, CISO, Head of AI, Risk Committee",
                mandateType: "AI Governance Committee"
            },
            3: {
                phase: "Days 61–90: High-Conviction Board Cadence",
                badgeClass: "badge-days-90",
                daysTag: "Days 61–90",
                title: "Active Quarterly Board Service & Strategic Sounding Board",
                format: "Quarterly formal board meetings + monthly architecture sprint syncs + on-demand executive hotline",
                focus: "High-level strategic steering, key engineering executive vetting, investor syndicate diligence, and crisis triage.",
                deliverables: [
                    "Formal boardroom technology & AI governance section",
                    "Technical vetting of C-suite & Staff+ engineering candidates",
                    "Inference compute unit economics optimization (30–50% cost drop)",
                    "Strategic partnership & cloud provider term negotiations"
                ],
                stakeholders: "Board of Directors, Executive Committee, Lead Investors",
                mandateType: "Technology Advisory Council"
            },
            4: {
                phase: "Day 90+: Fiduciary Scale & Sovereign Assets",
                badgeClass: "badge-days-beyond",
                daysTag: "Day 90+ & Ongoing",
                title: "Comprehensive Fiduciary & Scale Audit",
                format: "Annual risk committee review + investor syndicate briefings",
                focus: "Auditing multi-year technological defensibility, sovereign IP assets, and institutional audit compliance.",
                deliverables: [
                    "Full SOC2 Type II & EU AI Act compliance validation audit",
                    "Institutional venture syndicate diligence readiness dossier",
                    "Autonomous agent fleet penetration testing review",
                    "Multi-year sovereign technology roadmap for next growth phase"
                ],
                stakeholders: "Full Board of Directors, Audit Committee, Major Shareholders",
                mandateType: "Independent Director"
            }
        };

        var detailEl = document.getElementById('roadmapDetailBox');
        if (detailEl && phaseData[phaseNum]) {
            var data = phaseData[phaseNum];
            var deliverablesList = data.deliverables.map(function(d) {
                return '<li class="mb-1"><i class="mdi mdi-check-circle text-primary mr-1"></i> ' + d + '</li>';
            }).join('');

            detailEl.innerHTML = 
                '<div class="d-flex align-items-center justify-content-between mb-2 flex-wrap">' +
                    '<div>' +
                        '<span class="roadmap-days-badge ' + data.badgeClass + ' mr-2 font-weight-bold">' + data.daysTag + '</span>' +
                        '<span class="badge badge-pill badge-primary px-3 py-1 mr-2 font-weight-bold" style="font-size:11px;">' + data.phase + '</span>' +
                    '</div>' +
                    '<span class="text-muted small"><i class="mdi mdi-account-group text-primary mr-1"></i><strong>Stakeholders:</strong> ' + data.stakeholders + '</span>' +
                '</div>' +
                '<h4 class="text-dark font-weight-bold mb-2" style="font-size:18px;">' + data.title + '</h4>' +
                '<p class="text-muted small mb-2" style="line-height:1.6;">' + data.focus + '</p>' +
                '<div class="row align-items-center mt-2">' +
                    '<div class="col-lg-8 mb-2 mb-lg-0">' +
                        '<strong class="text-dark small d-block mb-1"><i class="mdi mdi-format-list-checks text-success mr-1"></i> Key Phase Deliverables:</strong>' +
                        '<ul class="small text-muted pl-0 mb-0" style="list-style:none;">' + deliverablesList + '</ul>' +
                    '</div>' +
                    '<div class="col-lg-4 text-center text-lg-right">' +
                        '<div class="p-2 rounded bg-light border mb-2 text-left small">' +
                            '<strong>Format:</strong> <span class="text-muted">' + data.format + '</span>' +
                        '</div>' +
                        '<button type="button" class="btn btn-sm btn-primary font-weight-bold px-3 py-2 w-100" style="border-radius:20px;" onclick="openAdvisoryModal(\'' + data.mandateType + '\')">' +
                            '<i class="mdi mdi-calendar-check mr-1"></i> Inquire for ' + data.daysTag + ' Mandate' +
                        '</button>' +
                    '</div>' +
                '</div>';
        }
    };

    // Roadmap Prev/Next Navigation
    window.navigateRoadmap = function (delta) {
        var next = currentCadencePhase + delta;
        if (next < 1) next = 4;
        if (next > 4) next = 1;
        window.switchCadencePhase(next);
    };

    // 4. Interactive Mandates Filter Tabs
    window.filterMandates = function (category, btn) {
        var buttons = document.querySelectorAll('.mandates-filter-btn');
        buttons.forEach(function (b) { b.classList.remove('active'); });
        if (btn) btn.classList.add('active');

        var items = document.querySelectorAll('.mandate-card-item');
        items.forEach(function (item) {
            var cat = item.getAttribute('data-category');
            if (category === 'all' || cat.indexOf(category) !== -1) {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });
    };

    // 4b. Interactive Venture Advisory Ecosystem Filter
    window.filterEcosystem = function (category, btn) {
        var buttons = document.querySelectorAll('.ecosystem-filter-btn');
        buttons.forEach(function (b) { b.classList.remove('active'); });
        if (btn) btn.classList.add('active');

        var cols = document.querySelectorAll('.ecosystem-card-col');
        cols.forEach(function (col) {
            var cat = col.getAttribute('data-category');
            if (category === 'all' || cat.indexOf(category) !== -1) {
                col.classList.remove('dimmed');
                col.classList.add('highlighted');
            } else {
                col.classList.add('dimmed');
                col.classList.remove('highlighted');
            }
        });
    };

    // 5. Open Advisory Modal with pre-selected mandate
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
                if (pill.getAttribute('data-mandate').toLowerCase().indexOf(mandateName.toLowerCase()) !== -1 ||
                    mandateName.toLowerCase().indexOf(pill.getAttribute('data-mandate').toLowerCase()) !== -1) {
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

    // 6. Form Submission Handling
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

    // 7. Board Biography Modal Handling
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
