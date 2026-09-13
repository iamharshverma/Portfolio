/**
 * Google Analytics 4 (GA4) Event Tracking Service
 * Harsh Verma Portfolio
 * 
 * Provides a clean, modular, and fault-tolerant service to monitor:
 * 1. Project filter button interactions (home page & portfolio page)
 * 2. Contact form interactions & lifecycle (attempts, validation errors, success/leads, errors)
 */

(function(window, document) {
    'use strict';

    // Default or configured GA4 Measurement ID
    var GA4_ID = window.GA4_MEASUREMENT_ID || 'G-HVPORTFOL4';

    // Ensure dataLayer exists
    window.dataLayer = window.dataLayer || [];

    // Ensure gtag function exists
    if (typeof window.gtag !== 'function') {
        window.gtag = function() {
            window.dataLayer.push(arguments);
        };
    }

    // Initialize GA4 property config if not already configured
    var isGA4Configured = false;
    function ensureGA4Config() {
        if (!isGA4Configured && GA4_ID) {
            window.gtag('js', new Date());
            window.gtag('config', GA4_ID, {
                send_page_view: true,
                cookie_flags: 'SameSite=None;Secure'
            });
            isGA4Configured = true;
        }
    }

    ensureGA4Config();

    var AnalyticsService = {
        measurementId: GA4_ID,
        debug: true,

        /**
         * Core method to send events to GA4
         * @param {string} eventName - GA4 event name (e.g., 'select_content', 'generate_lead')
         * @param {Object} eventParams - Additional key-value parameters
         */
        trackEvent: function(eventName, eventParams) {
            try {
                eventParams = eventParams || {};
                
                // Add standard contextual metadata
                if (!eventParams.page_location) {
                    eventParams.page_location = window.location.href;
                }
                if (!eventParams.page_title) {
                    eventParams.page_title = document.title;
                }
                if (!eventParams.timestamp) {
                    eventParams.timestamp = new Date().toISOString();
                }

                // Invoke GA4 gtag
                if (typeof window.gtag === 'function') {
                    window.gtag('event', eventName, eventParams);
                }

                // Debug logging for verification
                if (this.debug && window.console && console.log) {
                    console.log('%c[GA4 Event]%c ' + eventName, 'color: #2563eb; font-weight: bold;', 'color: #0f172a;', eventParams);
                }

                // Dispatch Custom DOM Event for custom telemetry or UI listeners
                if (typeof window.CustomEvent === 'function') {
                    var customEvt = new CustomEvent('ga4:event', {
                        detail: {
                            eventName: eventName,
                            eventParams: eventParams
                        }
                    });
                    window.dispatchEvent(customEvt);
                }
            } catch (err) {
                if (window.console && console.warn) {
                    console.warn('[AnalyticsService] Error dispatching event:', err);
                }
            }
        },

        /**
         * Track project filter interactions
         * @param {string} category - Selected category ('all', 'bigdata', 'nlp', 'security', 'vision', etc.)
         * @param {Object} [options] - Additional details like filter label, page source, element id
         */
        trackProjectFilter: function(category, options) {
            options = options || {};
            var cleanCategory = (category || 'all').replace(/^\./, '').trim();
            var filterLabel = options.label || cleanCategory;
            var pageSource = options.page || (window.location.pathname.indexOf('page-portfolio') !== -1 ? 'portfolio_page' : 'home_page');

            // 1. Standard GA4 content selection event
            this.trackEvent('select_content', {
                content_type: 'project_filter',
                item_id: cleanCategory,
                item_name: filterLabel,
                item_category: cleanCategory,
                source_page: pageSource
            });

            // 2. Custom high-granularity event
            this.trackEvent('project_filter_click', {
                filter_category: cleanCategory,
                filter_label: filterLabel,
                source_page: pageSource,
                active_filter_selector: category
            });
        },

        /**
         * Track contact form lifecycle interactions
         * @param {string} status - 'attempt', 'validation_error', 'success', 'error'
         * @param {Object} details - Metadata related to the event
         */
        trackContactSubmission: function(status, details) {
            details = details || {};
            var formId = details.formId || 'contact-form';

            switch (status) {
                case 'attempt':
                    this.trackEvent('contact_form_attempt', {
                        form_id: formId,
                        form_subject: details.subject || 'General Inquiry',
                        has_organization: Boolean(details.organization)
                    });
                    break;

                case 'validation_error':
                    this.trackEvent('contact_form_validation_failed', {
                        form_id: formId,
                        error_count: details.errorCount || (details.errors ? details.errors.length : 0),
                        invalid_fields: details.invalidFields ? details.invalidFields.join(', ') : 'unknown'
                    });
                    break;

                case 'success':
                    // GA4 standard recommended conversion event for contact forms
                    this.trackEvent('generate_lead', {
                        lead_type: 'portfolio_contact',
                        value: 1,
                        currency: 'USD',
                        contact_subject: details.subject || 'General Inquiry',
                        reference_id: details.refId || 'HV-VERIFIED'
                    });

                    // Custom descriptive event
                    this.trackEvent('contact_form_success', {
                        form_id: formId,
                        subject: details.subject || 'General Inquiry',
                        organization: details.organization || 'Individual',
                        ref_id: details.refId || 'HV-VERIFIED'
                    });
                    break;

                case 'error':
                    this.trackEvent('contact_form_error', {
                        form_id: formId,
                        error_message: details.errorMessage || 'Network or server error'
                    });
                    break;

                default:
                    this.trackEvent('contact_form_interaction', details);
            }
        },

        /**
         * Track topic pill selection
         * @param {string} topic - Selected topic
         */
        trackTopicSelect: function(topic) {
            this.trackEvent('contact_topic_select', {
                topic_name: topic
            });
        },

        /**
         * Auto-attach click listeners to existing filter buttons in the DOM
         */
        autoAttachListeners: function() {
            var self = this;

            function bind() {
                // 1. Home page project filter buttons: .home-proj-filter-btn
                document.querySelectorAll('.home-proj-filter-btn').forEach(function(btn) {
                    if (!btn.getAttribute('data-ga4-bound')) {
                        btn.setAttribute('data-ga4-bound', 'true');
                        btn.addEventListener('click', function() {
                            var text = (btn.innerText || '').trim();
                            var onclickAttr = btn.getAttribute('onclick') || '';
                            var match = onclickAttr.match(/filterHomeProjects\(['"]([^'"]+)['"]/);
                            var cat = match ? match[1] : text.toLowerCase();
                            self.trackProjectFilter(cat, {
                                label: text,
                                page: 'home_page'
                            });
                        });
                    }
                });

                // 2. Portfolio page isotope filter buttons: #filter a or .categories-filter a
                var filterUl = document.getElementById('filter');
                if (filterUl) {
                    filterUl.querySelectorAll('a').forEach(function(link) {
                        if (!link.getAttribute('data-ga4-bound')) {
                            link.setAttribute('data-ga4-bound', 'true');
                            link.addEventListener('click', function() {
                                var catSelector = link.getAttribute('data-filter') || '*';
                                var label = (link.innerText || '').trim();
                                self.trackProjectFilter(catSelector, {
                                    label: label,
                                    page: 'portfolio_page'
                                });
                            });
                        }
                    });
                }

                // 3. Contact topic pills
                document.querySelectorAll('.contact-topic-pill').forEach(function(pill) {
                    if (!pill.getAttribute('data-ga4-bound')) {
                        pill.setAttribute('data-ga4-bound', 'true');
                        pill.addEventListener('click', function() {
                            var topic = pill.getAttribute('data-topic') || (pill.innerText || '').trim();
                            self.trackTopicSelect(topic);
                        });
                    }
                });
            }

            if (document.readyState === 'loading') {
                document.addEventListener('DOMContentLoaded', bind);
            } else {
                bind();
            }
        }
    };

    // Initialize auto-listeners
    AnalyticsService.autoAttachListeners();

    // Export globally
    window.AnalyticsService = AnalyticsService;
    window.GA4Tracker = AnalyticsService;

})(window, document);
