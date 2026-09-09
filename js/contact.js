// Enhanced Modern Contact Form Handler with Client-Side Validation
$(document).ready(function() {

    // Helper: Validate email address format
    function isValidEmail(email) {
        if (!email || typeof email !== 'string') return false;
        var trimmed = email.trim();
        // RFC-compliant email regex
        var emailRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+$/;
        if (!emailRegex.test(trimmed)) return false;

        var parts = trimmed.split('@');
        if (parts.length !== 2) return false;
        var domain = parts[1];
        if (!domain.includes('.')) return false;

        var domainParts = domain.split('.');
        var tld = domainParts[domainParts.length - 1];
        // TLD should be alphabetic and at least 2 characters long
        if (!tld || tld.length < 2 || !/^[a-zA-Z]+$/.test(tld)) return false;

        return true;
    }

    // Helper: Set field error state
    function setFieldError($field, errorMessage) {
        $field.removeClass('is-valid').addClass('is-invalid');
        $field.attr('aria-invalid', 'true');

        // Locate or dynamically create feedback element
        var $feedback = $field.siblings('.invalid-feedback');
        if (!$feedback.length) {
            var fieldId = $field.attr('id') || 'field';
            $feedback = $('<div class="invalid-feedback font-weight-bold" id="' + fieldId + '-error"></div>');
            $field.after($feedback);
        }
        $feedback.html('<i class="mdi mdi-alert-circle mr-1"></i> ' + errorMessage).show();
    }

    // Helper: Clear field error state
    function clearFieldError($field, markValid) {
        $field.removeClass('is-invalid');
        $field.removeAttr('aria-invalid');
        if (markValid) {
            $field.addClass('is-valid');
        } else {
            $field.removeClass('is-valid');
        }
        var $feedback = $field.siblings('.invalid-feedback');
        if ($feedback.length) {
            $feedback.text('').hide();
        }
    }

    // Helper: Validate individual field
    function validateField(fieldId, showFeedback) {
        var $field = $('#' + fieldId);
        if (!$field.length) return { isValid: true };

        var val = ($field.val() || '').trim();
        var isValid = true;
        var errorMsg = '';

        switch (fieldId) {
            case 'name':
                if (!val) {
                    isValid = false;
                    errorMsg = 'Please enter your full name.';
                } else if (val.length < 2) {
                    isValid = false;
                    errorMsg = 'Please enter a valid full name (at least 2 characters).';
                }
                break;

            case 'email':
                if (!val) {
                    isValid = false;
                    errorMsg = 'Please enter your email address.';
                } else if (!isValidEmail(val)) {
                    isValid = false;
                    errorMsg = 'Please enter a valid email address (e.g., alex@organization.com).';
                }
                break;

            case 'subject':
                if (!val) {
                    isValid = false;
                    errorMsg = 'Please enter a subject or focus for your message.';
                }
                break;

            case 'comments':
                if (!val) {
                    isValid = false;
                    errorMsg = 'Please enter your detailed message.';
                } else if (val.length < 5) {
                    isValid = false;
                    errorMsg = 'Please enter a more detailed message (minimum 5 characters).';
                }
                break;
        }

        if (showFeedback) {
            if (!isValid) {
                setFieldError($field, errorMsg);
            } else {
                clearFieldError($field, true);
            }
        }

        return { isValid: isValid, error: errorMsg, $field: $field };
    }

    // Helper: Validate all fields in form
    function validateContactForm() {
        var fields = ['name', 'email', 'subject', 'comments'];
        var errors = [];
        var firstInvalid = null;

        fields.forEach(function(fieldId) {
            var res = validateField(fieldId, true);
            if (!res.isValid) {
                errors.push({ fieldId: fieldId, message: res.error });
                if (!firstInvalid) {
                    firstInvalid = res.$field;
                }
            }
        });

        return {
            isValid: errors.length === 0,
            errors: errors,
            firstInvalid: firstInvalid
        };
    }

    // Live validation: Clear error as user types once a field was marked invalid
    $('#contact-form').on('input keyup change', '#name, #email, #subject, #comments', function() {
        var $this = $(this);
        var fieldId = $this.attr('id');

        // If the field is currently marked invalid or has a value, re-validate it
        if ($this.hasClass('is-invalid') || $this.val().trim().length > 0) {
            var res = validateField(fieldId, false);
            if (res.isValid) {
                clearFieldError($this, true);
                // If all fields are now valid, hide the top message summary
                var checkAll = validateContactForm();
                if (checkAll.isValid) {
                    $('#message').slideUp(200);
                }
            }
        }
    });

    // Validate on blur if user entered content or skipped a required field
    $('#contact-form').on('blur', '#name, #email, #subject, #comments', function() {
        var $this = $(this);
        var fieldId = $this.attr('id');
        var val = $this.val().trim();

        // If user interacted with the field or left it empty after blur
        if (val.length > 0 || $this.hasClass('is-invalid')) {
            validateField(fieldId, true);
        }
    });

    // Topic Pills Selection Handler
    $(document).on('click', '.contact-topic-pill', function(e) {
        e.preventDefault();
        $('.contact-topic-pill').removeClass('active');
        $(this).addClass('active');
        var topic = $(this).data('topic');
        if (topic) {
            var $subject = $('#subject');
            $subject.val(topic);
            clearFieldError($subject, true);
        }
    });

    // Copy Email Helper
    window.copyHarshEmail = function(e) {
        if (e) e.preventDefault();
        var email = 'harshverma59@gmail.com';
        if (navigator.clipboard && navigator.clipboard.writeText) {
            navigator.clipboard.writeText(email).then(function() {
                showContactToast('Copied harshverma59@gmail.com to clipboard!');
            }).catch(function() {
                promptCopyEmail(email);
            });
        } else {
            promptCopyEmail(email);
        }
    };

    // Copy LinkedIn Helper
    window.copyHarshLinkedIn = function(e) {
        if (e) e.preventDefault();
        var linkedInUrl = 'https://www.linkedin.com/in/harshverma59/';
        if (navigator.clipboard && navigator.clipboard.writeText) {
            navigator.clipboard.writeText(linkedInUrl).then(function() {
                showContactToast('Copied LinkedIn profile link to clipboard!');
            }).catch(function() {
                promptCopyLinkedIn(linkedInUrl);
            });
        } else {
            promptCopyLinkedIn(linkedInUrl);
        }
    };

    function promptCopyLinkedIn(url) {
        var tempInput = document.createElement('input');
        tempInput.value = url;
        document.body.appendChild(tempInput);
        tempInput.select();
        document.execCommand('copy');
        document.body.removeChild(tempInput);
        showContactToast('Copied LinkedIn profile link to clipboard!');
    }

    function promptCopyEmail(email) {
        var tempInput = document.createElement('input');
        tempInput.value = email;
        document.body.appendChild(tempInput);
        tempInput.select();
        document.execCommand('copy');
        document.body.removeChild(tempInput);
        showContactToast('Copied harshverma59@gmail.com to clipboard!');
    }

    function showContactToast(msg) {
        var $toast = $('#contactToast');
        if (!$toast.length) {
            $('body').append(`
                <div id="contactToast" class="contact-feedback-toast" style="position: fixed; bottom: 30px; right: 30px; background: #0f172a; color: #ffffff; padding: 12px 24px; border-radius: 50px; font-size: 14px; font-weight: 600; box-shadow: 0 10px 30px rgba(0,0,0,0.25); z-index: 99999; display: none; border: 1px solid rgba(255,255,255,0.15); align-items: center;">
                    <i class="mdi mdi-check-circle text-success mr-2" style="font-size: 18px;"></i> <span id="contactToastText"></span>
                </div>
            `);
            $toast = $('#contactToast');
        }
        $('#contactToastText').text(msg);
        $toast.stop(true, true).fadeIn(300).delay(2500).fadeOut(300);
    }

    // Quick fill test message helper for instant testing
    window.fillTestContactForm = function(e) {
        if (e) e.preventDefault();
        $('#name').val('Dr. Alex Morgan');
        $('#email').val('alex.morgan@stanford.edu');
        $('#organization').val('Stanford AI Laboratory');
        $('#subject').val('AI & Agentic Systems Advisory');
        $('#comments').val('Hi Harsh, I would love to connect with you regarding your research on Agentic AI Systems and enterprise security guardrails. Looking forward to speaking!');

        // Clear errors and mark as valid
        ['name', 'email', 'subject', 'comments'].forEach(function(f) {
            clearFieldError($('#' + f), true);
        });
        $('#message').slideUp(200);

        showContactToast('Sample inquiry filled! Click "Send Message" to verify.');
    };

    // Working Contact Form Submission with Full Client-Side Validation
    $('#contact-form').on('submit', function(e) {
        e.preventDefault();
        var $form = $(this);
        var action = $form.attr('action') || '/api/contact';
        if (action.indexOf('.php') !== -1) {
            action = '/api/contact';
        }
        var $submitBtn = $('#submit');
        var $msgContainer = $("#message");

        // 1. Run Client-Side Validation
        var validation = validateContactForm();

        if (!validation.isValid) {
            // Build informative error message summary
            var errorListHtml = validation.errors.map(function(err) {
                return '<li>' + err.message + '</li>';
            }).join('');

            var summaryAlertHtml = `
                <div class="alert alert-danger shadow-sm border-0 mb-4 p-3 rounded" style="border-left: 4px solid #ef4444 !important;">
                    <div class="d-flex align-items-center mb-1">
                        <i class="mdi mdi-alert-circle mr-2 font-20 text-danger"></i>
                        <strong class="font-weight-bold" style="font-size: 15px;">Please resolve the highlighted errors:</strong>
                    </div>
                    <ul class="mb-0 pl-4 mt-2 font-weight-500" style="font-size: 13.5px; line-height: 1.6;">
                        ${errorListHtml}
                    </ul>
                </div>
            `;

            $msgContainer.html(summaryAlertHtml).slideDown(250);

            // Focus on first invalid field
            if (validation.firstInvalid && validation.firstInvalid.length) {
                validation.firstInvalid.focus();
                // Smooth scroll to element if needed
                var offset = validation.firstInvalid.offset().top - 120;
                if (window.scrollY > offset + 300 || window.scrollY < offset - 300) {
                    $('html, body').animate({ scrollTop: offset }, 300);
                }
            }

            return false;
        }

        // All fields passed client-side validation
        $msgContainer.slideUp(200);
        $submitBtn.prop('disabled', true).html('<span class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true"></span> Sending Message...');

        var formData = {
            name: ($('#name').val() || '').trim(),
            email: ($('#email').val() || '').trim(),
            subject: ($('#subject').val() || '').trim(),
            organization: ($('#organization').val() || '').trim(),
            comments: ($('#comments').val() || '').trim()
        };

        $.ajax({
            type: 'POST',
            url: action,
            data: JSON.stringify(formData),
            contentType: 'application/json',
            dataType: 'json',
            success: function(response) {
                $submitBtn.prop('disabled', false).html('<i class="mdi mdi-check mr-1"></i> Message Sent');

                var successHtml = `
                    <div id="success_page" class="alert alert-success border-0 shadow-sm p-4 rounded mb-4" style="background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%); border-left: 4px solid #10b981 !important;">
                        <div class="d-flex align-items-center justify-content-between mb-2">
                            <span class="badge badge-success px-3 py-1 font-weight-bold" style="font-size: 13px;"><i class="mdi mdi-check-circle mr-1"></i> Message Delivered</span>
                            <small class="text-muted font-weight-bold">${response.refId || 'Ref: HV-VERIFIED'}</small>
                        </div>
                        <h5 class="text-success font-weight-bold mb-2">Thank you, ${formData.name}!</h5>
                        <p class="text-dark mb-2" style="font-size: 14.5px; line-height: 1.6;">
                            Your inquiry regarding <strong>"${formData.subject || 'General Inquiry'}"</strong> has been successfully received and forwarded to <strong>harshverma59@gmail.com</strong>.
                        </p>
                        <div class="d-flex align-items-center text-muted small mt-2">
                            <span class="mr-3"><i class="mdi mdi-clock-outline mr-1 text-primary"></i> Response Time: Within 24 hours</span>
                            <span><i class="mdi mdi-shield-check mr-1 text-success"></i> Direct &amp; Confidential</span>
                        </div>
                    </div>
                `;

                $msgContainer.html(successHtml).slideDown('fast');
                $form[0].reset();

                // Clear all valid/invalid indicators
                ['name', 'email', 'subject', 'organization', 'comments'].forEach(function(f) {
                    clearFieldError($('#' + f), false);
                });
                $('.contact-topic-pill').removeClass('active');
                showContactToast('Message successfully sent to Harsh Verma!');
            },
            error: function(xhr) {
                $submitBtn.prop('disabled', false).html('<i class="mdi mdi-send mr-1"></i> Send Message');
                var errMessage = 'Failed to send message. Please try emailing directly at harshverma59@gmail.com';
                if (xhr.responseJSON && xhr.responseJSON.error) {
                    errMessage = xhr.responseJSON.error;
                } else if (xhr.responseText) {
                    errMessage = xhr.responseText;
                }
                $msgContainer.html('<div class="alert alert-danger font-weight-bold mb-4 shadow-sm border-0"><i class="mdi mdi-alert-circle mr-1"></i> ' + errMessage + '</div>').slideDown('fast');
            }
        });

        return false;
    });
});
