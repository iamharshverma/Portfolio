/**
 * Harsh Verma Portfolio - Live Speaker One-Sheet & Media Kit Component
 * Dynamic Bio Switcher, Keynote Abstract Selector & 1-Click Asset Downloads
 */

(function () {
  'use strict';

  var bios = {
    short: {
      label: '50-Word Intro (Summit & Podcast)',
      wordCount: '~50 words',
      text: 'Harsh Verma is a Principal Software Engineer in AI at Palo Alto Networks, an elected Fellow of the British Computer Society (FBCS), Senior Member of IEEE (SMIEEE), and Forbes Technology Council member. An international keynote speaker and author, he pioneers autonomous agent systems and enterprise cyber defense architectures.'
    },
    standard: {
      label: '100-Word Bio (Conference Programs)',
      wordCount: '~100 words',
      text: 'Harsh Verma is a Principal Software Engineer in AI at Palo Alto Networks, specializing in autonomous multi-agent systems, machine-speed cybersecurity counteroffensives, and distributed cloud computing. He is an elected Fellow of the British Computer Society (FBCS), Senior Member of IEEE (SMIEEE), Fellow of the Royal Society of Arts (FRSA), and an official Forbes Technology Council member. With 27 peer-reviewed papers, 6 patents, and 2 landmark books on autonomous agents and AI security, Harsh speaks globally at premier tech summits and advises startups at UC Berkeley SkyDeck.'
    },
    executive: {
      label: '250-Word Executive Bio (Board & Dossiers)',
      wordCount: '~250 words',
      text: 'Harsh Verma is a Principal Software Engineer in AI at Palo Alto Networks, focused on advancing autonomous agent systems, multi-agent reasoning topologies, and intelligent AI defense strategies. As an elected Fellow of the British Computer Society (FBCS), Senior Member of IEEE (SMIEEE), Fellow of the Royal Society of Arts (FRSA), and official Forbes Technology Council member, he brings deep architectural rigor and strategic guidance to enterprise leaders adopting next-generation AI capabilities. Harsh leads the operationalization of responsible, deterministic AI systems across Fortune 500 environments, architecting high-scale telemetry ingestion platforms, intelligent multi-agent guardrails, and real-time copilot navigation engines (with 4 patents in-process). Over his decade-long career spanning ISRO, Hike Messenger, Reliance Jio, Worlds, and Hypergiant, he has published 27 peer-reviewed papers across IEEE, Springer, and Oxford University Press, authored 2 landmark books on autonomous agents and AI cyber defense, and developed an intellectual property portfolio of 6 patents (2 granted, 4 pending at Palo Alto Networks). Harsh holds a Master of Science in Computer Science from the University of Texas at Dallas and completed executive education in Corporate Innovation (LEAD) at the Stanford University Graduate School of Business.'
    }
  };

  var activeBioKey = 'standard';

  function initSpeakerKit() {
    var root = document.getElementById('hvSpeakerKitRoot');
    if (!root) return;

    renderSpeakerKit(root);
  }

  function renderSpeakerKit(root) {
    var currentBio = bios[activeBioKey];

    var html =
      '<div class="hv-speaker-kit-box">' +
        '<div class="d-flex flex-wrap justify-content-between align-items-center mb-3">' +
          '<div>' +
            '<span class="badge badge-pill text-white px-3 py-1 font-weight-bold" style="background: linear-gradient(135deg, #1d4ed8 0%, #2563eb 100%); letter-spacing: 0.5px; font-size: 11px;">' +
              '<i class="mdi mdi-microphone-variant mr-1"></i> Speaker & Media Kit' +
            '</span>' +
            '<h3 class="font-weight-bold text-dark mb-1 mt-2" style="font-size: 1.55rem; letter-spacing: -0.3px;">' +
              'Official Speaker Introductions & Assets' +
            '</h3>' +
            '<p class="text-muted mb-0 small">' +
              'Select preferred biography length below for event programs, moderator intros, or executive board dossiers.' +
            '</p>' +
          '</div>' +
          '<div class="mt-2 mt-md-0 d-flex gap-2">' +
            '<button type="button" class="btn btn-outline-primary btn-sm font-weight-bold rounded mr-2" onclick="window.hvOpenOneSheetModal()">' +
              '<i class="mdi mdi-file-document-outline mr-1"></i> View 1-Sheet' +
            '</button>' +
            '<a href="files/Harsh_Verma_Board_Biography.pdf" target="_blank" class="btn btn-primary btn-sm font-weight-bold rounded">' +
              '<i class="mdi mdi-download mr-1"></i> Download Board PDF' +
            '</a>' +
          '</div>' +
        '</div>' +

        '<!-- Bio Tab Switcher -->' +
        '<div class="d-flex flex-wrap align-items-center gap-2 mb-2">' +
          '<button type="button" class="hv-bio-tab-btn' + (activeBioKey === 'short' ? ' active' : '') + '" data-bio="short">50-Word Intro</button>' +
          '<button type="button" class="hv-bio-tab-btn' + (activeBioKey === 'standard' ? ' active' : '') + '" data-bio="standard">100-Word Bio</button>' +
          '<button type="button" class="hv-bio-tab-btn' + (activeBioKey === 'executive' ? ' active' : '') + '" data-bio="executive">250-Word Executive Bio</button>' +
        '</div>' +

        '<!-- Bio Display Card -->' +
        '<div class="hv-bio-content-card">' +
          '<div class="d-flex justify-content-between align-items-center mb-2">' +
            '<span class="text-muted small font-weight-bold text-uppercase">' + currentBio.label + ' (' + currentBio.wordCount + ')</span>' +
            '<button type="button" class="btn btn-sm btn-outline-secondary font-weight-bold rounded py-1 px-2.5" id="hvCopyBioBtn">' +
              '<i class="mdi mdi-content-copy mr-1"></i> Copy to Clipboard' +
            '</button>' +
          '</div>' +
          '<p class="hv-bio-text mb-0" id="hvBioTextContent">' + currentBio.text + '</p>' +
        '</div>' +

        '<!-- Press Assets Row -->' +
        '<div class="row mt-4 pt-2 border-top">' +
          '<div class="col-md-4 mb-3 mb-md-0">' +
            '<div class="d-flex align-items-center">' +
              '<img src="images/home/harsh_verma_speaker.png" alt="Harsh Verma Headshot" class="rounded mr-3 shadow-sm" style="width: 52px; height: 52px; object-fit: cover;" />' +
              '<div>' +
                '<h6 class="font-weight-bold mb-0" style="font-size: 13.5px;">Official Headshot</h6>' +
                '<a href="images/home/harsh_verma_speaker.png" download="Harsh_Verma_Official_Headshot.png" class="text-primary small font-weight-bold">' +
                  '<i class="mdi mdi-download mr-1"></i> Download High-Res' +
                '</a>' +
              '</div>' +
            '</div>' +
          '</div>' +
          '<div class="col-md-4 mb-3 mb-md-0">' +
            '<div class="d-flex align-items-center">' +
              '<img src="images/books/book_creator_to_curator.png" alt="Book Cover" class="rounded mr-3 shadow-sm" style="width: 38px; height: 52px; object-fit: cover;" />' +
              '<div>' +
                '<h6 class="font-weight-bold mb-0" style="font-size: 13.5px;">Book 1: Creator to Curator</h6>' +
                '<a href="images/books/book_creator_to_curator.png" download="Book_Beyond_AI_Engineering.png" class="text-primary small font-weight-bold">' +
                  '<i class="mdi mdi-download mr-1"></i> Cover Art (PNG)' +
                '</a>' +
              '</div>' +
            '</div>' +
          '</div>' +
          '<div class="col-md-4">' +
            '<div class="d-flex align-items-center">' +
              '<img src="images/books/book_cybersecurity_counteroffensive.png" alt="Book Cover" class="rounded mr-3 shadow-sm" style="width: 38px; height: 52px; object-fit: cover;" />' +
              '<div>' +
                '<h6 class="font-weight-bold mb-0" style="font-size: 13.5px;">Book 2: AI vs. AI</h6>' +
                '<a href="images/books/book_cybersecurity_counteroffensive.png" download="Book_AI_vs_AI.png" class="text-primary small font-weight-bold">' +
                  '<i class="mdi mdi-download mr-1"></i> Cover Art (PNG)' +
                '</a>' +
              '</div>' +
            '</div>' +
          '</div>' +
        '</div>' +
      '</div>';

    root.innerHTML = html;

    // Attach listeners
    root.querySelectorAll('.hv-bio-tab-btn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        activeBioKey = btn.getAttribute('data-bio');
        renderSpeakerKit(root);
      });
    });

    var copyBtn = document.getElementById('hvCopyBioBtn');
    if (copyBtn) {
      copyBtn.addEventListener('click', function () {
        var text = bios[activeBioKey].text;
        navigator.clipboard.writeText(text).then(function () {
          showToast('Copied ' + bios[activeBioKey].label + ' to clipboard!');
        });
      });
    }
  }

  function showToast(msg) {
    var toast = document.getElementById('hvCopyToast');
    if (!toast) {
      toast = document.createElement('div');
      toast.id = 'hvCopyToast';
      toast.className = 'hv-copy-toast';
      document.body.appendChild(toast);
    }
    toast.innerHTML = '<i class="mdi mdi-check-circle text-success"></i> ' + msg;
    toast.classList.add('show');
    setTimeout(function () {
      toast.classList.remove('show');
    }, 2800);
  }

  window.hvOpenOneSheetModal = function () {
    window.open('files/Harsh_Verma_Board_Biography.pdf', '_blank');
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSpeakerKit);
  } else {
    initSpeakerKit();
  }

  window.hvInitSpeakerKit = initSpeakerKit;

})();
