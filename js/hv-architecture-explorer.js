/**
 * Harsh Verma Portfolio - Interactive Research & Architecture Explorer
 * Visual relationship matrix connecting 5 core research pillars directly
 * to patents, published papers, and authored books.
 */

(function () {
  'use strict';

  var explorerData = [
    {
      id: 'pillar-agentic-systems',
      title: 'Autonomous Multi-Agent Systems & Agentic Workflows',
      icon: 'mdi-robot',
      badge: '6 Papers • 4 Patents • 1 Book',
      tagline: 'Deterministic execution, self-healing state machines, and dynamic consensus topologies.',
      description: 'Establishes theoretical and architectural foundations for autonomous multi-agent orchestration in enterprise environments, eliminating LLM nondeterminism through closed-loop validation.',
      items: [
        {
          type: 'PATENT SUITE (PENDING)',
          badgeClass: 'badge-primary',
          title: 'Agentic AI, Enterprise Copilot Systems & Copilot Navigation Architectures',
          desc: 'Suite of 4 in-process patent applications developing foundational intellectual property in autonomous copilot reasoning and contextual security operations at Palo Alto Networks.',
          url: 'https://www.paloaltonetworks.com/',
          actionText: 'Review Patent Suite'
        },
        {
          type: 'AUTHORED BOOK (2026)',
          badgeClass: 'badge-danger',
          title: 'Beyond AI Engineering: From Creator to Curator',
          desc: 'Palo Alto Technical Press monograph detailing the paradigm shift from generative prompts to deterministic multi-agent curation, self-healing loops, and zero-trust verification.',
          url: 'page-books#beyond-ai-engineering',
          actionText: 'Explore Book'
        },
        {
          type: 'RESEARCH PAPER (2026)',
          badgeClass: 'badge-info',
          title: 'Designing Self-Healing AI Agentic Systems: A Framework for Autonomous Detection and Response',
          desc: 'IJSRM 2026 paper formulating closed-loop state machines allowing autonomous agent networks to detect and patch runtime errors without human escalation.',
          url: 'https://doi.org/10.18535/ijsrm/v14i02.cs01',
          actionText: 'Read Paper (DOI)'
        },
        {
          type: 'RESEARCH PAPER (2024)',
          badgeClass: 'badge-info',
          title: 'Autonomous Multi-Agent Systems for Enterprise Decision-Making',
          desc: 'IJEETR 2024 paper introducing hierarchical agent coordination topologies with dynamic consensus protocols for enterprise operational planning.',
          url: 'https://doi.org/10.5281/zenodo.14013444',
          actionText: 'Read Paper (DOI)'
        }
      ]
    },
    {
      id: 'pillar-cyber-defense',
      title: 'Enterprise AI Cyber Defense & Machine-Speed Counteroffensives',
      icon: 'mdi-shield-lock-outline',
      badge: '8 Papers • 1 Book',
      tagline: 'Formalizing Clean Attacks, Intent-Based Trust, and Trust Graphs.',
      description: 'Pioneers defensive paradigms for autonomous agents, neutralizing automated machine-speed cyber attacks and replacing broken identity tokens with mathematical intent models.',
      items: [
        {
          type: 'AUTHORED BOOK (2026)',
          badgeClass: 'badge-danger',
          title: 'AI vs. AI: Engineering the Cybersecurity Counteroffensive',
          desc: 'Cyber Defense Press blueprint for architecting machine-speed defensive agent counteroffensives capable of neutralizing intelligent adversarial agents in milliseconds.',
          url: 'page-books#ai-vs-ai',
          actionText: 'Explore Book'
        },
        {
          type: 'LANDMARK PAPER (2025)',
          badgeClass: 'badge-warning',
          title: 'Clean Attacks: Formalizing Semantically Valid Adversarial Behavior in Autonomous AI Agents',
          desc: 'Seminal paper formalizing attacks that satisfy all schema and syntax boundaries while coercing agents into executing malicious sub-tasks.',
          url: 'https://doi.org/10.18535/ijsrm/v13i12.cs01',
          actionText: 'Read Paper (DOI)'
        },
        {
          type: 'RESEARCH PAPER (2026)',
          badgeClass: 'badge-info',
          title: 'Intent-Based Security: Replacing Identity-Centric Trust in Autonomous AI Agentic Systems',
          desc: 'Mathematical model verifying agent execution intent prior to tool invocation, proving why traditional RBAC tokens fail in dynamic agent topologies.',
          url: 'https://doi.org/10.18535/ijsrm/v14i02.cs02',
          actionText: 'Read Paper (DOI)'
        },
        {
          type: 'RESEARCH PAPER (2026)',
          badgeClass: 'badge-info',
          title: 'Security in Multi-Agent AI Systems: Modeling Emergent Vulnerabilities via Trust Graphs',
          desc: 'Graph-theoretic approach to detect cascading privilege escalations and emergent trust vulnerabilities across multi-agent networks.',
          url: 'https://doi.org/10.18535/ijsrm/v14i01.cs01',
          actionText: 'Read Paper (DOI)'
        }
      ]
    },
    {
      id: 'pillar-distributed-streaming',
      title: 'Distributed Cloud Streaming & Real-Time Load Simulation',
      icon: 'mdi-server-network',
      badge: '5 Papers • 1 Granted Patent',
      tagline: 'Petabyte-scale telemetry ingestion, Kafka/Spark pipelines, and Granted Patent 555747.',
      description: 'Engineers high-throughput streaming fabrics capable of ingesting millions of telemetry events per second with zero data loss and automated stress benchmarking.',
      items: [
        {
          type: 'GRANTED PATENT (2024)',
          badgeClass: 'badge-success',
          title: 'Patent No: 555747 — Systems & Methods for Performing Load Testing of a Social Networking Application',
          desc: 'Indian Patent Office issued patent for distributed peer-coordinated load generator agents dynamic stress benchmarking at 100M+ user scale.',
          url: 'https://iprsearch.ipindia.gov.in/PublicSearch/PublicationSearch/',
          actionText: 'Official Patent Portal'
        },
        {
          type: 'RESEARCH PAPER (2019)',
          badgeClass: 'badge-info',
          title: 'Secure Real Time Heterogeneous Data Management Tool (IEEE CogML)',
          desc: 'Presented at IEEE CogML; details unified real-time secure ingestion across heterogeneous relational, NoSQL, and cloud object datastores.',
          url: 'https://doi.org/10.1109/CogML.2019.00010',
          actionText: 'IEEE Xplore (DOI)'
        },
        {
          type: 'RESEARCH PAPER (2017)',
          badgeClass: 'badge-info',
          title: 'Real Time Analytics Performance Load Simulation and Scaling (IJCA)',
          desc: 'Theoretical and architectural basis for distributed load testing that culminated in Granted Patent 555747.',
          url: 'https://doi.org/10.5120/ijca2017915502',
          actionText: 'Read Paper (DOI)'
        },
        {
          type: 'RESEARCH PAPER (2020)',
          badgeClass: 'badge-info',
          title: 'Scalable Real-Time Data Pipelines for AI and Machine Learning–Driven Enterprise Systems',
          desc: 'EJCSIT architectural blueprint for real-time feature transformation across distributed Apache Kafka and Spark pipelines.',
          url: 'https://doi.org/10.37745/ejcsit.2013/vol8no2pp115',
          actionText: 'Read Paper (DOI)'
        }
      ]
    },
    {
      id: 'pillar-optimization-wsn',
      title: 'Differential Evolution & Delay-Tolerant Sensor Networks',
      icon: 'mdi-chart-timeline-variant',
      badge: '3 Papers • 1 Granted Patent',
      tagline: 'MA-DEBTP trajectory planning, DEICA-ML clustering, and Granted Patent 606481.',
      description: 'Formulates mathematical optimization algorithms for mobile data collectors and energy-efficient clustering across sparse, partitioned wireless sensor networks.',
      items: [
        {
          type: 'GRANTED PATENT',
          badgeClass: 'badge-success',
          title: 'Patent No: 606481 — COVID Preventive Automated Entry Point (COPAEP)',
          desc: 'Integrated automated cyber-physical checkpoint coordinating multi-tier edge sensors for non-contact thermal scanning, sanitization misting, and access control verification.',
          url: 'https://iprsearch.ipindia.gov.in/PublicSearch/PublicationSearch/',
          actionText: 'Official Patent Portal'
        },
        {
          type: 'RESEARCH PAPER (2026)',
          badgeClass: 'badge-info',
          title: 'Multi-Agent Differential Evolution-Based Trajectory Planning (MA-DEBTP)',
          desc: 'ICACCM 2026 paper introducing MA-DEBTP, optimizing autonomous mobile data collectors in delay-tolerant wireless sensor networks with high delivery ratios.',
          url: 'https://doi.org/10.5281/zenodo.icaccm2026.madebtp',
          actionText: 'Read Paper (DOI)'
        },
        {
          type: 'RESEARCH PAPER (2026)',
          badgeClass: 'badge-info',
          title: 'DEICA-ML: Multi-Layer Differential Evolution Clustering for IoT Networks',
          desc: 'IEEE Access paper formulating multi-layer cluster head election protocols extending heterogeneous IoT sensor network lifespan by 38%.',
          url: 'https://doi.org/10.1109/ACCESS.2026.52653',
          actionText: 'IEEE Access (DOI)'
        }
      ]
    },
    {
      id: 'pillar-xai-ethics',
      title: 'Explainable AI (XAI), Ethics & Enterprise Governance',
      icon: 'mdi-scale-balance',
      badge: '5 Papers • 6 Packt Reviews',
      tagline: 'Algorithmic transparency, bias mitigation, and executive AI adoption strategy.',
      description: 'Develops formal frameworks for explainability and fairness auditing in enterprise machine learning systems, ensuring regulatory compliance and board-level oversight.',
      items: [
        {
          type: 'TECHNICAL BOOK REVIEWS',
          badgeClass: 'badge-danger',
          title: 'Official Technical Peer Reviewer for Packt Publishing (6 Volumes)',
          desc: 'Technical evaluation of AI Ethics in Action, Hands-On AI Dev with Python, Leadership at the Helm of AI, Python for Algorithmic Trading, and The TensorFlow Workshop.',
          url: 'page-books',
          actionText: 'View Reviewed Books'
        },
        {
          type: 'RESEARCH PAPER (2024)',
          badgeClass: 'badge-info',
          title: 'Explainable AI (XAI) for Software Engineering Decision-Making',
          desc: 'IJIRCCE 2024 paper designing transparent attribution frameworks enabling software leaders to audit automated code generation and architectural recommendations.',
          url: 'https://doi.org/10.15680/IJIRCCE.2024.1205012',
          actionText: 'Read Paper (DOI)'
        },
        {
          type: 'RESEARCH PAPER (2025)',
          badgeClass: 'badge-info',
          title: 'Ethical Challenges and Bias Mitigation in Artificial Intelligence Systems',
          desc: 'WJARR 2025 paper detailing mathematical auditing techniques for detecting and mitigating latent demographic bias in enterprise training datasets.',
          url: 'https://doi.org/10.30574/wjarr.2025.25.1.0182',
          actionText: 'Read Paper (DOI)'
        }
      ]
    }
  ];

  var activeIndex = 0;

  function initArchitectureExplorer() {
    var root = document.getElementById('hvArchitectureExplorerRoot');
    if (!root) return;

    renderExplorer(root);
  }

  function renderExplorer(root) {
    var current = explorerData[activeIndex];

    var html =
      '<div class="hv-arch-explorer-card">' +
        '<div class="d-flex flex-wrap justify-content-between align-items-center mb-2">' +
          '<div>' +
            '<span class="badge badge-pill text-white px-3 py-1 font-weight-bold" style="background: linear-gradient(135deg, #1e3a8a 0%, #0284c7 100%); letter-spacing: 0.5px; font-size: 11px;">' +
              '<i class="mdi mdi-graphql mr-1"></i> Interactive Architecture Matrix' +
            '</span>' +
            '<h3 class="font-weight-bold text-dark mb-1 mt-2" style="font-size: 1.55rem; letter-spacing: -0.3px;">' +
              'Research Pillars to Enterprise Systems' +
            '</h3>' +
            '<p class="text-muted mb-0 small" style="max-width: 780px;">' +
              'Select any strategic research domain below to explore how theoretical breakthroughs directly translate into granted patents, enterprise books, and peer-reviewed software systems.' +
            '</p>' +
          '</div>' +
          '<div class="mt-2 mt-md-0">' +
            '<a href="page-publications" class="btn btn-outline-primary btn-sm font-weight-bold rounded">' +
              '<i class="mdi mdi-book-open-page-variant mr-1"></i> All 27 Publications & 6 Patents' +
            '</a>' +
          '</div>' +
        '</div>' +

        '<div class="hv-arch-pillar-grid">';

    explorerData.forEach(function (pillar, idx) {
      var isActive = idx === activeIndex;
      html +=
        '<button type="button" class="hv-arch-pillar-btn' + (isActive ? ' active' : '') + '" data-index="' + idx + '">' +
          '<div>' +
            '<div class="hv-arch-pillar-icon"><i class="mdi ' + pillar.icon + '"></i></div>' +
            '<div class="hv-arch-pillar-title">' + pillar.title + '</div>' +
          '</div>' +
          '<div class="hv-arch-pillar-count">' +
            '<i class="mdi mdi-checkbox-marked-circle-outline text-primary"></i> ' + pillar.badge +
          '</div>' +
        '</button>';
    });

    html +=
        '</div>' +

        '<!-- Active Pillar Detail Drawer -->' +
        '<div class="hv-arch-detail-drawer">' +
          '<div class="hv-arch-detail-header">' +
            '<div>' +
              '<div class="d-flex align-items-center">' +
                '<span class="badge badge-pill badge-primary mr-2 font-weight-bold px-2.5 py-1" style="font-size: 11px;">Selected Research Domain</span>' +
                '<h4 class="font-weight-bold text-dark mb-0" style="font-size: 1.18rem;">' + current.title + '</h4>' +
              '</div>' +
              '<p class="text-muted mb-0 mt-1 small" style="line-height: 1.5;">' + current.description + '</p>' +
            '</div>' +
            '<div class="text-muted small font-weight-bold text-uppercase" style="letter-spacing: 0.5px;">' +
              current.badge +
            '</div>' +
          '</div>' +

          '<div class="hv-arch-item-list">';

    current.items.forEach(function (it) {
      html +=
        '<div class="hv-arch-item-card">' +
          '<div>' +
            '<div class="hv-arch-item-top">' +
              '<span class="badge ' + it.badgeClass + ' font-weight-bold px-2 py-0.5" style="font-size: 10.5px;">' + it.type + '</span>' +
            '</div>' +
            '<h5 class="hv-arch-item-title">' + it.title + '</h5>' +
            '<p class="hv-arch-item-desc">' + it.desc + '</p>' +
          '</div>' +
          '<a href="' + it.url + '" target="' + (it.url.indexOf('http') === 0 ? '_blank' : '_self') + '" class="hv-arch-item-btn">' +
            it.actionText + ' <i class="mdi mdi-arrow-right ml-1"></i>' +
          '</a>' +
        '</div>';
    });

    html +=
          '</div>' +
        '</div>' +
      '</div>';

    root.innerHTML = html;

    // Attach click listeners to pillar buttons
    root.querySelectorAll('.hv-arch-pillar-btn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        activeIndex = parseInt(btn.getAttribute('data-index'), 10);
        renderExplorer(root);
      });
    });
  }

  // Self-initialize on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initArchitectureExplorer);
  } else {
    initArchitectureExplorer();
  }

  window.hvInitArchitectureExplorer = initArchitectureExplorer;

})();
