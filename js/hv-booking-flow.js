/**
 * Harsh Verma Portfolio - Executive Keynote & Media Hub + Speaking & Advisory Booking Engine
 */

(function () {
  'use strict';

  let currentStep = 1;
  let bookingData = {
    engagementType: 'Keynote Speech',
    topic: 'The Era of Agentic Security (UC Berkeley SkyDeck Series)',
    eventFormat: 'In-Person',
    targetDate: '',
    location: '',
    audienceSize: '100 - 500 Attendees (Engineers & Executives)',
    organizerName: '',
    organization: '',
    email: '',
    phone: '',
    budget: 'Standard Enterprise / Keynote Tier',
    notes: ''
  };

  // Bios data for Press Kit
  const pressBios = {
    short: "Harsh Verma is a Principal Software Engineer in AI at Palo Alto Networks, Forbes Technology Council Member, IEEE Senior Member, and author of two books on Enterprise AI. Recognized on the Forttuna Global 100 Power List and Nobel Technology Awards Gold (#145), he architects deterministic agentic systems, zero-trust cloud perimeters, and high-throughput data platforms, keynoting across UC Berkeley SkyDeck and international AI symposiums.",
    medium: "Harsh Verma is an internationally recognized Enterprise AI Architect, Principal Software Engineer in AI at Palo Alto Networks, and Forbes Technology Council Member. With over a decade of systems leadership, Harsh has authored 2 seminal industry books on Enterprise AI Agents and Autonomous Cyber Defense, published 22+ peer-reviewed papers on IEEE and international journals with 150+ academic citations, and earned 24 global technology honors including the Forttuna Global 100 Power List, Nobel Technology Awards Gold (#145), and Global Recognition Award for AI Innovation. He serves as an elected Fellow of Harvard Square Leaders Excellence and IEEE Senior Member. Harsh is a distinguished keynote speaker—frequently headlining UC Berkeley SkyDeck, international AI summits, and venture accelerators on agentic security architectures, distributed AI infrastructure, and autonomous enterprise defense.",
    full: "Harsh Verma is a distinguished Enterprise AI Architect, Principal Software Engineer in AI at Palo Alto Networks, Forbes Technology Council Member, and prolific author. A pioneer in agentic security architectures and deterministic AI guardrails, Harsh has architected mission-critical data platforms, distributed feature pipelines, and autonomous defense perimeters protecting global enterprise networks.\n\nHe is the recipient of 24 international honors including the Forttuna Global 100 Power List (2026), Nobel Technology Awards Gold (#145), Global Recognition Award for Enterprise AI Innovation, and multiple Globee & Stevie Awards. A dedicated researcher and thought leader, Harsh has published 22+ peer-reviewed papers across IEEE and international engineering journals, accumulating over 150+ academic citations, alongside authoring two seminal books on Enterprise AI Agents and Autonomous Cyber Defense. He holds senior fellowships including Harvard Square Leaders Excellence Fellow and IEEE Senior Member.\n\nAs an invited keynote speaker and technical advisor, Harsh headlines major technology symposiums, university venture accelerators including UC Berkeley SkyDeck, and global executive forums, delivering actionable frameworks on generative AI, zero-trust cloud security, and resilient autonomous systems."
  };

  function createBookingModalDOM() {
    if (document.getElementById('hvBookingModalOverlay')) return;

    const overlay = document.createElement('div');
    overlay.id = 'hvBookingModalOverlay';
    overlay.className = 'hv-booking-modal-overlay';
    overlay.innerHTML = `
      <div class="hv-booking-modal-card">
        <div class="hv-booking-modal-header">
          <div class="d-flex align-items-center">
            <span class="mr-3 p-2 rounded" style="background: rgba(99, 102, 241, 0.25); border: 1px solid rgba(165, 180, 252, 0.4);">
              <i class="mdi mdi-calendar-star font-weight-bold" style="font-size: 22px; color: #818cf8;"></i>
            </span>
            <div>
              <h5 class="font-weight-bold text-white mb-0" style="font-size: 18px;">Executive Speaking &amp; Advisory Consultation</h5>
              <small class="text-light" style="opacity: 0.85;">Direct Consultation Request with Harsh Verma &bull; 24h Response Guarantee</small>
            </div>
          </div>
          <button type="button" class="btn btn-sm text-white" id="hvCloseBookingModalBtn" style="font-size: 22px; line-height: 1; background: transparent; border: none; opacity: 0.8;" aria-label="Close Booking Modal">
            &times;
          </button>
        </div>

        <div class="hv-booking-step-indicator">
          <div class="hv-step-dot active" id="hvStepDot1">1</div>
          <div class="hv-step-connector" id="hvStepConn1"></div>
          <div class="hv-step-dot" id="hvStepDot2">2</div>
          <div class="hv-step-connector" id="hvStepConn2"></div>
          <div class="hv-step-dot" id="hvStepDot3">3</div>
          <div class="hv-step-connector" id="hvStepConn3"></div>
          <div class="hv-step-dot" id="hvStepDot4">4</div>
        </div>

        <div class="hv-booking-modal-body">
          <form id="hvBookingForm" onsubmit="return false;">
            
            <!-- STEP 1: Engagement Type -->
            <div id="hvBookingStep1" class="hv-booking-step-content">
              <h6 class="font-weight-bold mb-1" style="font-size: 15.5px;">Step 1 of 4: Select Engagement Type</h6>
              <p class="text-muted small mb-3">Choose the format of your upcoming event or strategic consultation:</p>

              <div class="hv-type-selector-grid">
                <div class="hv-type-card-option selected" data-type="Keynote Speech">
                  <div class="hv-type-icon"><i class="mdi mdi-microphone-variant"></i></div>
                  <strong style="font-size: 14.5px;">Keynote Address</strong>
                  <small class="text-muted mt-1">Conferences, opening summits, global tech keynotes &amp; symposiums.</small>
                </div>

                <div class="hv-type-card-option" data-type="Executive AI Advisory">
                  <div class="hv-type-icon"><i class="mdi mdi-shield-account"></i></div>
                  <strong style="font-size: 14.5px;">Executive AI Advisory</strong>
                  <small class="text-muted mt-1">C-Suite &amp; board consultations on GenAI roadmaps &amp; cyber defense.</small>
                </div>

                <div class="hv-type-card-option" data-type="Corporate Workshop & Masterclass">
                  <div class="hv-type-icon"><i class="mdi mdi-school-outline"></i></div>
                  <strong style="font-size: 14.5px;">Corporate Workshop</strong>
                  <small class="text-muted mt-1">Deep architectural masterclasses on agentic AI &amp; distributed systems.</small>
                </div>

                <div class="hv-type-card-option" data-type="Panel & Fireside Chat">
                  <div class="hv-type-icon"><i class="mdi mdi-account-group-outline"></i></div>
                  <strong style="font-size: 14.5px;">Panel / Fireside Chat</strong>
                  <small class="text-muted mt-1">Industry roundtables, podcast recordings, and expert panels.</small>
                </div>

                <div class="hv-type-card-option" data-type="Hackathon / Venture Pitch Judging">
                  <div class="hv-type-icon"><i class="mdi mdi-gavel"></i></div>
                  <strong style="font-size: 14.5px;">Judging &amp; Mentorship</strong>
                  <small class="text-muted mt-1">Venture accelerators (Techstars, Berkeley SkyDeck) and AI hackathons.</small>
                </div>
              </div>

              <div class="d-flex justify-content-end mt-4">
                <button type="button" class="btn btn-primary font-weight-bold px-4 py-2" style="background: #4f46e5; border: none; border-radius: 10px;" id="hvStep1NextBtn">
                  Next: Select Topic <i class="mdi mdi-arrow-right ml-1"></i>
                </button>
              </div>
            </div>

            <!-- STEP 2: Topic Selection -->
            <div id="hvBookingStep2" class="hv-booking-step-content d-none">
              <h6 class="font-weight-bold mb-1" style="font-size: 15.5px;">Step 2 of 4: Select Keynote / Advisory Topic</h6>
              <p class="text-muted small mb-3">Select from Harsh's signature presentations or propose a customized topic:</p>

              <div class="hv-topic-select-grid">
                <div class="hv-topic-option-item selected" data-topic="The Era of Agentic Security: Autonomous Cloud Defense &amp; Self-Healing Perimeters">
                  <i class="mdi mdi-shield-check text-primary" style="font-size: 22px;"></i>
                  <div>
                    <strong style="font-size: 14px;">The Era of Agentic Security (UC Berkeley SkyDeck Series)</strong>
                    <div class="text-muted small">Autonomous agentic reasoning, zero-trust cloud perimeters, and deterministic policy enforcement.</div>
                  </div>
                </div>

                <div class="hv-topic-option-item" data-topic="Enterprise AI Agents: Orchestrating Resilient Multi-Agent Architectures">
                  <i class="mdi mdi-robot-outline text-primary" style="font-size: 22px;"></i>
                  <div>
                    <strong style="font-size: 14px;">Enterprise AI Agents: Production Multi-Agent Systems</strong>
                    <div class="text-muted small">Architecting enterprise memory, tool-calling guardrails, evaluation metrics, and mission-critical reliability.</div>
                  </div>
                </div>

                <div class="hv-topic-option-item" data-topic="Autonomous Cyber Defense: Battleground Intelligence &amp; Quantum Threat Readiness">
                  <i class="mdi mdi-lock-pattern text-primary" style="font-size: 22px;"></i>
                  <div>
                    <strong style="font-size: 14px;">Autonomous Cyber Defense &amp; Quantum Preparedness</strong>
                    <div class="text-muted small">Post-quantum cryptography, real-time adversarial threat modeling, and defensive SecOps automation.</div>
                  </div>
                </div>

                <div class="hv-topic-option-item" data-topic="High-Throughput Distributed AI Platforms: Scaling Big Data Telemetry at Enterprise Scope">
                  <i class="mdi mdi-database-sync text-primary" style="font-size: 22px;"></i>
                  <div>
                    <strong style="font-size: 14px;">High-Throughput Distributed AI &amp; Big Data Pipelines</strong>
                    <div class="text-muted small">Lessons from Palo Alto Networks &amp; tier-1 platforms: feature stores, streaming inference, and zero-downtime scaling.</div>
                  </div>
                </div>

                <div class="hv-topic-option-item" data-topic="Custom Topic / Strategic Focus">
                  <i class="mdi mdi-pencil-ruler text-primary" style="font-size: 22px;"></i>
                  <div>
                    <strong style="font-size: 14px;">Custom Strategic Focus</strong>
                    <div class="text-muted small">Tailored specifically for your enterprise executive retreat, university symposium, or keynote summit.</div>
                  </div>
                </div>
              </div>

              <div class="d-flex justify-content-between mt-4">
                <button type="button" class="btn btn-outline-secondary font-weight-bold px-3 py-2" style="border-radius: 10px;" id="hvStep2BackBtn">
                  <i class="mdi mdi-arrow-left mr-1"></i> Back
                </button>
                <button type="button" class="btn btn-primary font-weight-bold px-4 py-2" style="background: #4f46e5; border: none; border-radius: 10px;" id="hvStep2NextBtn">
                  Next: Event Logistics <i class="mdi mdi-arrow-right ml-1"></i>
                </button>
              </div>
            </div>

            <!-- STEP 3: Logistics & Format -->
            <div id="hvBookingStep3" class="hv-booking-step-content d-none">
              <h6 class="font-weight-bold mb-1" style="font-size: 15.5px;">Step 3 of 4: Event Format &amp; Timeline</h6>
              <p class="text-muted small mb-3">Provide logistical specifics to align calendar availability:</p>

              <div class="row">
                <div class="col-md-6 mb-3">
                  <label class="font-weight-bold small mb-1">Event Delivery Format *</label>
                  <select class="form-control" id="hvBookingFormat" style="border-radius: 8px;">
                    <option value="In-Person">In-Person (Onsite / Stage)</option>
                    <option value="Virtual Keynote">Virtual (Live Stream / Zoom / Broadcast)</option>
                    <option value="Hybrid">Hybrid (Onsite + Virtual Stream)</option>
                  </select>
                </div>
                <div class="col-md-6 mb-3">
                  <label class="font-weight-bold small mb-1">Target Date / Timeframe *</label>
                  <input type="date" class="form-control" id="hvBookingTargetDate" style="border-radius: 8px;" />
                </div>
                <div class="col-md-6 mb-3">
                  <label class="font-weight-bold small mb-1">Event Location / City &amp; Timezone *</label>
                  <input type="text" class="form-control" id="hvBookingLocation" placeholder="e.g. San Francisco, CA / PST (or Virtual)" style="border-radius: 8px;" />
                </div>
                <div class="col-md-6 mb-3">
                  <label class="font-weight-bold small mb-1">Estimated Audience Profile *</label>
                  <select class="form-control" id="hvBookingAudience" style="border-radius: 8px;">
                    <option value="100 - 500 Attendees (Engineers & Executives)">100 - 500 Attendees (Engineers & Executives)</option>
                    <option value="500 - 2,000+ Attendees (Major Conference / Summit)">500 - 2,000+ Attendees (Major Conference)</option>
                    <option value="20 - 50 Leaders (Executive Board / C-Suite Retreat)">20 - 50 Leaders (Executive Board / C-Suite)</option>
                    <option value="University / Academic / Researchers">University / Academic / Researchers</option>
                  </select>
                </div>
              </div>

              <div class="d-flex justify-content-between mt-4">
                <button type="button" class="btn btn-outline-secondary font-weight-bold px-3 py-2" style="border-radius: 10px;" id="hvStep3BackBtn">
                  <i class="mdi mdi-arrow-left mr-1"></i> Back
                </button>
                <button type="button" class="btn btn-primary font-weight-bold px-4 py-2" style="background: #4f46e5; border: none; border-radius: 10px;" id="hvStep3NextBtn">
                  Next: Contact Details <i class="mdi mdi-arrow-right ml-1"></i>
                </button>
              </div>
            </div>

            <!-- STEP 4: Contact & Confirmation -->
            <div id="hvBookingStep4" class="hv-booking-step-content d-none">
              <h6 class="font-weight-bold mb-1" style="font-size: 15.5px;">Step 4 of 4: Organizer &amp; Organization Details</h6>
              <p class="text-muted small mb-3">Please specify the contact details for formal coordination and executive scheduling:</p>

              <div class="row">
                <div class="col-md-6 mb-3">
                  <label class="font-weight-bold small mb-1">Coordinator / Organizer Name *</label>
                  <input type="text" class="form-control" id="hvBookingName" placeholder="e.g. Dr. Jane Smith" required style="border-radius: 8px;" />
                </div>
                <div class="col-md-6 mb-3">
                  <label class="font-weight-bold small mb-1">Company / University / Event Org *</label>
                  <input type="text" class="form-control" id="hvBookingOrg" placeholder="e.g. Stanford AI Summit / Acme Corp" required style="border-radius: 8px;" />
                </div>
                <div class="col-md-6 mb-3">
                  <label class="font-weight-bold small mb-1">Official Work Email *</label>
                  <input type="email" class="form-control" id="hvBookingEmail" placeholder="jane@stanford.edu or jane@company.com" required style="border-radius: 8px;" />
                </div>
                <div class="col-md-6 mb-3">
                  <label class="font-weight-bold small mb-1">Budget / Honorarium Tier (Optional)</label>
                  <select class="form-control" id="hvBookingBudget" style="border-radius: 8px;">
                    <option value="Enterprise Keynote Standard">Enterprise Keynote Standard</option>
                    <option value="Executive Advisory Retainer">Executive Advisory Retainer</option>
                    <option value="University / Academic / Non-Profit Keynote">University / Academic / Non-Profit</option>
                    <option value="Venture / Startup Accelerator Mentorship">Venture / Startup Accelerator Mentorship</option>
                  </select>
                </div>
                <div class="col-12 mb-3">
                  <label class="font-weight-bold small mb-1">Event Summary &amp; Specific Objectives</label>
                  <textarea class="form-control" id="hvBookingNotes" rows="2" placeholder="Describe the event themes, specific expectations, or questions..." style="border-radius: 8px;"></textarea>
                </div>
              </div>

              <div id="hvBookingErrorMsg" class="alert alert-danger d-none py-2 small font-weight-bold"></div>

              <div class="d-flex justify-content-between mt-3">
                <button type="button" class="btn btn-outline-secondary font-weight-bold px-3 py-2" style="border-radius: 10px;" id="hvStep4BackBtn">
                  <i class="mdi mdi-arrow-left mr-1"></i> Back
                </button>
                <button type="button" class="btn btn-success font-weight-bold px-4 py-2" style="background: #10b981; border: none; border-radius: 10px;" id="hvSubmitBookingBtn">
                  <i class="mdi mdi-send-check mr-1"></i> Submit Booking Consultation
                </button>
              </div>
            </div>

            <!-- SUCCESS STATE -->
            <div id="hvBookingSuccessState" class="d-none text-center py-4">
              <div class="mb-3">
                <span style="display:inline-flex; width:64px; height:64px; border-radius:50%; background:#dcfce7; color:#16a34a; align-items:center; justify-content:center; font-size:32px; box-shadow:0 8px 24px rgba(22, 163, 74, 0.2);">
                  <i class="mdi mdi-check-decagram"></i>
                </span>
              </div>
              <h4 class="font-weight-bold text-success mb-1">Booking Consultation Received!</h4>
              <p class="text-muted small mb-2" id="hvBookingRefDisplay">Reference Code: HV-BK-XXXXX</p>
              <p class="mb-4" style="font-size: 14.5px; max-width: 540px; margin: 0 auto; line-height: 1.6;" id="hvBookingSuccessMsg">
                Thank you! Your keynote request has been routed directly to Harsh Verma (<strong>harshverma59@gmail.com</strong>).
              </p>

              <div class="d-flex flex-wrap justify-content-center gap-2 mb-3">
                <a href="javascript:void(0)" id="hvDownloadIcsBtn" class="btn btn-primary font-weight-bold px-3 py-2 mr-2" style="background:#4f46e5; border:none; border-radius:10px;">
                  <i class="mdi mdi-calendar-download mr-1"></i> Download Calendar Hold (.ICS)
                </a>
                <button type="button" class="btn btn-outline-secondary font-weight-bold px-3 py-2" style="border-radius:10px;" id="hvDoneBookingBtn">
                  Close Window
                </button>
              </div>

              <div class="p-3 rounded bg-light border text-left mx-auto" style="max-width: 540px; font-size: 13px;">
                <div class="d-flex align-items-center text-muted mb-1">
                  <i class="mdi mdi-shield-check text-success mr-1"></i> <strong>Executive Response Protocol:</strong>
                </div>
                <div>All verified conference and enterprise advisory requests are reviewed within 24 business hours. If your date is time-sensitive, you may also reach out directly to <a href="mailto:harshverma59@gmail.com?subject=Urgent%20Keynote%20Inquiry" class="font-weight-bold text-primary">harshverma59@gmail.com</a>.</div>
              </div>
            </div>

          </form>
        </div>
      </div>
    `;

    document.body.appendChild(overlay);

    // Close handlers
    document.getElementById('hvCloseBookingModalBtn').addEventListener('click', closeBookingModal);
    document.getElementById('hvDoneBookingBtn').addEventListener('click', closeBookingModal);
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) closeBookingModal();
    });

    // Step 1: Type Selection Card Clicks
    const typeCards = overlay.querySelectorAll('.hv-type-card-option');
    typeCards.forEach(card => {
      card.addEventListener('click', function () {
        typeCards.forEach(c => c.classList.remove('selected'));
        this.classList.add('selected');
        bookingData.engagementType = this.getAttribute('data-type');
      });
    });

    // Step 2: Topic Selection Item Clicks
    const topicItems = overlay.querySelectorAll('.hv-topic-option-item');
    topicItems.forEach(item => {
      item.addEventListener('click', function () {
        topicItems.forEach(i => i.classList.remove('selected'));
        this.classList.add('selected');
        bookingData.topic = this.getAttribute('data-topic');
      });
    });

    // Step Navigation Handlers
    document.getElementById('hvStep1NextBtn').addEventListener('click', () => goToStep(2));
    document.getElementById('hvStep2BackBtn').addEventListener('click', () => goToStep(1));
    document.getElementById('hvStep2NextBtn').addEventListener('click', () => goToStep(3));
    document.getElementById('hvStep3BackBtn').addEventListener('click', () => goToStep(2));
    document.getElementById('hvStep3NextBtn').addEventListener('click', () => {
      const loc = document.getElementById('hvBookingLocation').value.trim();
      const date = document.getElementById('hvBookingTargetDate').value.trim();
      bookingData.eventFormat = document.getElementById('hvBookingFormat').value;
      bookingData.targetDate = date;
      bookingData.location = loc || 'Virtual / In-Person (TBD)';
      bookingData.audienceSize = document.getElementById('hvBookingAudience').value;
      goToStep(4);
    });
    document.getElementById('hvStep4BackBtn').addEventListener('click', () => goToStep(3));

    // Submit Booking
    document.getElementById('hvSubmitBookingBtn').addEventListener('click', submitBooking);
  }

  function goToStep(step) {
    currentStep = step;
    for (let i = 1; i <= 4; i++) {
      const stepEl = document.getElementById(`hvBookingStep${i}`);
      const dotEl = document.getElementById(`hvStepDot${i}`);
      const connEl = document.getElementById(`hvStepConn${i}`);

      if (stepEl) {
        if (i === step) {
          stepEl.classList.remove('d-none');
        } else {
          stepEl.classList.add('d-none');
        }
      }

      if (dotEl) {
        dotEl.classList.remove('active', 'completed');
        if (i < step) {
          dotEl.classList.add('completed');
          dotEl.innerHTML = '<i class="mdi mdi-check"></i>';
        } else if (i === step) {
          dotEl.classList.add('active');
          dotEl.innerText = i;
        } else {
          dotEl.innerText = i;
        }
      }

      if (connEl) {
        if (i < step) {
          connEl.classList.add('completed');
        } else {
          connEl.classList.remove('completed');
        }
      }
    }
  }

  function submitBooking() {
    const name = document.getElementById('hvBookingName').value.trim();
    const org = document.getElementById('hvBookingOrg').value.trim();
    const email = document.getElementById('hvBookingEmail').value.trim();
    const budget = document.getElementById('hvBookingBudget').value;
    const notes = document.getElementById('hvBookingNotes').value.trim();
    const errorEl = document.getElementById('hvBookingErrorMsg');

    if (!name) {
      errorEl.innerText = 'Please enter the organizer name.';
      errorEl.classList.remove('d-none');
      return;
    }
    if (!org) {
      errorEl.innerText = 'Please enter your organization or university.';
      errorEl.classList.remove('d-none');
      return;
    }
    if (!email || !email.includes('@') || !email.includes('.')) {
      errorEl.innerText = 'Please enter a valid work email address.';
      errorEl.classList.remove('d-none');
      return;
    }
    errorEl.classList.add('d-none');

    bookingData.organizerName = name;
    bookingData.organization = org;
    bookingData.email = email;
    bookingData.budget = budget;
    bookingData.notes = notes;

    const submitBtn = document.getElementById('hvSubmitBookingBtn');
    submitBtn.disabled = true;
    submitBtn.innerHTML = '<i class="mdi mdi-loading mdi-spin mr-1"></i> Processing Consultation Request...';

    fetch('/api/booking', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify(bookingData)
    })
      .then(res => res.json())
      .then(data => {
        submitBtn.disabled = false;
        submitBtn.innerHTML = '<i class="mdi mdi-send-check mr-1"></i> Submit Booking Consultation';

        if (data.success) {
          document.getElementById('hvBookingStep4').classList.add('d-none');
          document.querySelector('.hv-booking-step-indicator').classList.add('d-none');
          document.getElementById('hvBookingSuccessState').classList.remove('d-none');
          document.getElementById('hvBookingRefDisplay').innerText = `Reference Code: ${data.refId}`;
          document.getElementById('hvBookingSuccessMsg').innerHTML = `
            Thank you, <strong>${name}</strong>! Your consultation request for <em>"${bookingData.engagementType}"</em> on <strong>"${bookingData.topic}"</strong> has been confirmed and routed directly to <strong>harshverma59@gmail.com</strong>.
          `;

          // Configure ICS Download
          const icsBtn = document.getElementById('hvDownloadIcsBtn');
          if (data.icsData) {
            icsBtn.href = `data:text/calendar;charset=utf8;base64,${data.icsData}`;
            icsBtn.download = `${data.refId}-hold.ics`;
          } else {
            icsBtn.href = `/api/booking/download-ics?ref=${data.refId}&organizer=${encodeURIComponent(name)}&org=${encodeURIComponent(org)}&type=${encodeURIComponent(bookingData.engagementType)}&topic=${encodeURIComponent(bookingData.topic)}`;
          }
        } else {
          errorEl.innerText = data.error || 'Failed to submit booking request. Please try again.';
          errorEl.classList.remove('d-none');
        }
      })
      .catch(err => {
        submitBtn.disabled = false;
        submitBtn.innerHTML = '<i class="mdi mdi-send-check mr-1"></i> Submit Booking Consultation';
        errorEl.innerText = 'Network error. Please try again or email directly to harshverma59@gmail.com.';
        errorEl.classList.remove('d-none');
      });
  }

  function openBookingModal(preselectedTopic, preselectedType) {
    createBookingModalDOM();
    goToStep(1);

    const overlay = document.getElementById('hvBookingModalOverlay');
    const indicator = document.querySelector('.hv-booking-step-indicator');
    const successState = document.getElementById('hvBookingSuccessState');

    if (indicator) indicator.classList.remove('d-none');
    if (successState) successState.classList.add('d-none');

    if (preselectedType) {
      bookingData.engagementType = preselectedType;
      const typeCards = overlay.querySelectorAll('.hv-type-card-option');
      typeCards.forEach(c => {
        if (c.getAttribute('data-type') === preselectedType) {
          c.classList.add('selected');
        } else {
          c.classList.remove('selected');
        }
      });
    }

    if (preselectedTopic) {
      bookingData.topic = preselectedTopic;
      const topicItems = overlay.querySelectorAll('.hv-topic-option-item');
      topicItems.forEach(i => {
        if (i.getAttribute('data-topic') === preselectedTopic) {
          i.classList.add('selected');
        } else {
          i.classList.remove('selected');
        }
      });
    }

    overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeBookingModal() {
    const overlay = document.getElementById('hvBookingModalOverlay');
    if (overlay) {
      overlay.classList.remove('active');
      document.body.style.overflow = '';
    }
  }

  // Keynote Video Modal
  function createVideoModalDOM() {
    if (document.getElementById('hvVideoModalOverlay')) return;

    const modal = document.createElement('div');
    modal.id = 'hvVideoModalOverlay';
    modal.className = 'hv-video-modal-overlay';
    modal.innerHTML = `
      <div class="hv-video-modal-card">
        <div class="d-flex align-items-center justify-content-between p-3 border-bottom border-dark text-white">
          <div class="d-flex align-items-center">
            <i class="mdi mdi-play-circle-outline text-danger mr-2" style="font-size: 22px;"></i>
            <h6 class="font-weight-bold text-white mb-0" id="hvVideoModalTitle" style="font-size: 16px;">Keynote Session</h6>
          </div>
          <button type="button" class="btn btn-sm text-white" id="hvCloseVideoModalBtn" style="font-size: 24px; line-height: 1; background: transparent; border: none;" aria-label="Close Video Player">
            &times;
          </button>
        </div>
        <div class="hv-video-modal-player-wrap">
          <iframe id="hvVideoIframe" src="" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>
        <div class="p-4 text-white" style="background: #0f172a;">
          <div class="d-flex align-items-center justify-content-between mb-2">
            <span class="badge badge-pill badge-primary font-weight-bold px-3 py-1" id="hvVideoModalOutlet">Keynote Address</span>
            <button class="btn btn-sm btn-outline-light" onclick="window.openKeynoteBooking()" style="border-radius: 20px; font-size: 12.5px;">
              <i class="mdi mdi-calendar-check mr-1"></i> Book This Keynote Topic
            </button>
          </div>
          <p class="text-light mb-0" style="font-size: 14px; opacity: 0.9; line-height: 1.6;" id="hvVideoModalDesc"></p>
        </div>
      </div>
    `;

    document.body.appendChild(modal);

    document.getElementById('hvCloseVideoModalBtn').addEventListener('click', closeKeynoteVideoModal);
    modal.addEventListener('click', function (e) {
      if (e.target === modal) closeKeynoteVideoModal();
    });
  }

  function openKeynoteVideoModal(videoId, title, outlet, desc) {
    createVideoModalDOM();
    const modal = document.getElementById('hvVideoModalOverlay');
    const iframe = document.getElementById('hvVideoIframe');
    const titleEl = document.getElementById('hvVideoModalTitle');
    const outletEl = document.getElementById('hvVideoModalOutlet');
    const descEl = document.getElementById('hvVideoModalDesc');

    if (titleEl) titleEl.innerText = title || 'Keynote Presentation';
    if (outletEl) outletEl.innerText = outlet || 'Executive Keynote';
    if (descEl) descEl.innerText = desc || 'Keynote presentation by Harsh Verma.';

    if (iframe && videoId) {
      iframe.src = `https://www.youtube-nocookie.com/embed/${videoId}?autoplay=1&rel=0`;
    }

    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeKeynoteVideoModal() {
    const modal = document.getElementById('hvVideoModalOverlay');
    const iframe = document.getElementById('hvVideoIframe');
    if (iframe) iframe.src = '';
    if (modal) {
      modal.classList.remove('active');
      document.body.style.overflow = '';
    }
  }

  // Copy Bio Helper for Press Kit
  function copyPressBio(type) {
    const bioText = pressBios[type] || pressBios.medium;
    if (navigator.clipboard) {
      navigator.clipboard.writeText(bioText).then(() => {
        alert("Copied " + type.toUpperCase() + " Executive Bio to clipboard!");
      }).catch(() => {
        prompt("Copy Executive Bio:", bioText);
      });
    } else {
      prompt("Copy Executive Bio:", bioText);
    }
  }

  // Expose globally
  window.openBookingModal = openBookingModal;
  window.closeBookingModal = closeBookingModal;
  window.openKeynoteBooking = function (topic) {
    openBookingModal(topic || 'The Era of Agentic Security', 'Keynote Speech');
  };
  window.openAdvisoryBooking = function () {
    openBookingModal('Executive AI & Cybersecurity Advisory', 'Executive AI Advisory');
  };
  window.openKeynoteVideoModal = openKeynoteVideoModal;
  window.closeKeynoteVideoModal = closeKeynoteVideoModal;
  window.copyPressBio = copyPressBio;

  // Auto-bind triggers on DOM Load
  document.addEventListener('DOMContentLoaded', function () {
    // Buttons with data-booking-trigger
    document.querySelectorAll('[data-booking-trigger]').forEach(btn => {
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        const topic = this.getAttribute('data-topic') || '';
        const type = this.getAttribute('data-type') || 'Keynote Speech';
        openBookingModal(topic, type);
      });
    });

    // Buttons with data-video-id
    document.querySelectorAll('[data-keynote-video]').forEach(btn => {
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        const videoId = this.getAttribute('data-video-id');
        const title = this.getAttribute('data-title');
        const outlet = this.getAttribute('data-outlet');
        const desc = this.getAttribute('data-desc');
        openKeynoteVideoModal(videoId, title, outlet, desc);
      });
    });
  });

})();
