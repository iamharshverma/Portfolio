/**
 * Harsh Verma Portfolio - Global Impact & Media Reach Dashboard
 * Visualizes 3.75B+ audience impressions, Times Square billboard broadcast,
 * patent milestones, and global keynote footprint.
 */

(function () {
  'use strict';

  function initGlobalImpact() {
    var root = document.getElementById('hvGlobalImpactRoot');
    if (!root) return;

    var html =
      '<div class="hv-impact-dashboard-box">' +
        '<div class="d-flex flex-wrap justify-content-between align-items-center mb-4">' +
          '<div>' +
            '<span class="badge badge-pill text-white px-3 py-1 font-weight-bold" style="background: linear-gradient(135deg, #2563eb 0%, #06b6d4 100%); letter-spacing: 0.5px; font-size: 11px;">' +
              '<i class="mdi mdi-earth mr-1"></i> Global Influence & Reach' +
            '</span>' +
            '<h3 class="font-weight-bold text-dark mb-1 mt-2" style="font-size: 1.6rem; letter-spacing: -0.3px;">' +
              'Executive Impact & Media Reach Dashboard' +
            '</h3>' +
            '<p class="text-muted mb-0 small" style="max-width: 780px;">' +
              'Measuring enterprise footprint, academic citations, intellectual property, and global public discourse.' +
            '</p>' +
          '</div>' +
          '<div class="mt-2 mt-md-0">' +
            '<a href="page-media" class="btn btn-outline-primary btn-sm font-weight-bold rounded">' +
              '<i class="mdi mdi-newspaper mr-1"></i> View All 44 Media Features' +
            '</a>' +
          '</div>' +
        '</div>' +

        '<!-- 4 Key Stat Metrics Cards -->' +
        '<div class="row">' +
          '<div class="col-lg-3 col-sm-6 mb-3">' +
            '<div class="hv-impact-stat-card">' +
              '<div>' +
                '<div class="hv-impact-stat-num">3.75B+</div>' +
                '<div class="hv-impact-stat-label">Verified Media Reach</div>' +
                '<p class="hv-impact-stat-desc mb-0">Broadcast impressions across Times Square, Business Insider, AP News & international syndication.</p>' +
              '</div>' +
            '</div>' +
          '</div>' +
          '<div class="col-lg-3 col-sm-6 mb-3">' +
            '<div class="hv-impact-stat-card">' +
              '<div>' +
                '<div class="hv-impact-stat-num">27 + 6</div>' +
                '<div class="hv-impact-stat-label">Publications & Patents</div>' +
                '<p class="hv-impact-stat-desc mb-0">27 Peer-reviewed scientific papers across IEEE & Springer, plus 6 patents (2 granted, 4 in-process).</p>' +
              '</div>' +
            '</div>' +
          '</div>' +
          '<div class="col-lg-3 col-sm-6 mb-3">' +
            '<div class="hv-impact-stat-card">' +
              '<div>' +
                '<div class="hv-impact-stat-num">27</div>' +
                '<div class="hv-impact-stat-label">Global Tech Honors</div>' +
                '<p class="hv-impact-stat-desc mb-0">Global Recognition Award 2026 AI Innovator of the Year, NVTC Cyber50, Forttuna Global Leader.</p>' +
              '</div>' +
            '</div>' +
          '</div>' +
          '<div class="col-lg-3 col-sm-6 mb-3">' +
            '<div class="hv-impact-stat-card">' +
              '<div>' +
                '<div class="hv-impact-stat-num">26</div>' +
                '<div class="hv-impact-stat-label">Fellowships & Councils</div>' +
                '<p class="hv-impact-stat-desc mb-0">Fellow of British Computer Society (FBCS), Senior Member IEEE (SMIEEE), Forbes Tech Council.</p>' +
              '</div>' +
            '</div>' +
          '</div>' +
        '</div>' +

        '<!-- Times Square & Enterprise Security Highlight -->' +
        '<div class="hv-impact-highlight-box">' +
          '<div class="row align-items-center">' +
            '<div class="col-md-8">' +
              '<div class="d-flex align-items-center mb-1">' +
                '<span class="badge badge-warning text-dark font-weight-bold px-2.5 py-0.5 mr-2" style="font-size: 11px;">' +
                  '<i class="mdi mdi-billboard mr-1"></i> Times Square Broadcast' +
                '</span>' +
                '<span class="text-muted small font-weight-bold">Nasdaq Tower • New York City</span>' +
              '</div>' +
              '<h5 class="font-weight-bold text-dark mb-1" style="font-size: 1.15rem;">' +
                'Spotlighted on the Nasdaq Billboard in Times Square, New York' +
              '</h5>' +
              '<p class="text-muted mb-0 small" style="line-height: 1.55;">' +
                'Honoring sustained technological leadership in autonomous multi-agent defense architectures, patent-worthy innovation, and executive mentorship across the global deep-tech ecosystem.' +
              '</p>' +
            '</div>' +
            '<div class="col-md-4 text-md-right mt-3 mt-md-0">' +
              '<a href="page-media-distribution-analytics" class="btn btn-primary btn-sm font-weight-bold rounded px-3 py-2">' +
                '<i class="mdi mdi-chart-bell-curve mr-1"></i> View Distribution Analytics' +
              '</a>' +
            '</div>' +
          '</div>' +
        '</div>' +
      '</div>';

    root.innerHTML = html;
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initGlobalImpact);
  } else {
    initGlobalImpact();
  }

  window.hvInitGlobalImpact = initGlobalImpact;

})();
