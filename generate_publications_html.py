import json

with open('papers_data.json', 'r') as f:
    papers = json.load(f)

html_template = """<!DOCTYPE html>
<html lang="en">

<head>
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-30250521-4"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'UA-30250521-4');
    </script>
    <meta charset="UTF-8">
    <title>Publications & Research | Harsh Verma - Google Scholar Profile</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Published research papers in IEEE, WJARR, IJSRM, IJEETR, IJRAI, and IJCA by Harsh Verma. Focus areas: AI Agentic Systems, AI Security, Autonomous Pipelines, Multi-Agent Deliberation, and Cloud Telemetry." />
    <meta name="keywords" content="Harsh Verma, Google Scholar, IEEE, WJARR, IJSRM, IJEETR, IJRAI, IJCA, Research Papers, AI Agents, Multi-Agent Systems, AI Security, Explainable AI, IoT Edge" />
    <meta content="Harsh Verma" name="author" />
    
    <!-- favicon -->
    <link rel="shortcut icon" href="images/favicon_new.ico">
    <!-- Bootstrap -->
    <link href="css/bootstrap.min.css" rel="stylesheet" type="text/css" />
    <!-- Magnific -->
    <link href="css/magnific-popup.css" rel="stylesheet" type="text/css" />
    <!-- Icons -->
    <link href="css/materialdesignicons.min.css" rel="stylesheet" type="text/css" />
    <!-- Slider -->               
    <link rel="stylesheet" href="css/owl.carousel.min.css"/> 
    <link rel="stylesheet" href="css/owl.theme.default.min.css"/>
    <!-- Flickity -->
    <link href="css/flickity.css" rel="stylesheet" type="text/css" />
    <!-- Main css File -->
    <link href="css/style.css" rel="stylesheet" type="text/css" />
    <!-- Dark Mode css File -->
    <link href="css/dark-mode.css" rel="stylesheet" type="text/css" />
    <script src="js/dark-mode.js"></script>

    <style>
        .scholar-hero-card {
            background: linear-gradient(135deg, #0a0f1d 0%, #0f172a 45%, #1e3a8a 100%);
            border-radius: 16px;
            color: #ffffff;
            padding: 32px;
            box-shadow: 0 16px 40px rgba(15, 23, 42, 0.25);
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(59, 130, 246, 0.2);
        }
        .scholar-hero-card::before {
            content: "";
            position: absolute;
            top: -40%;
            right: -20%;
            width: 400px;
            height: 400px;
            background: radial-gradient(circle, rgba(59, 130, 246, 0.3) 0%, rgba(14, 165, 233, 0.18) 45%, rgba(255, 255, 255, 0) 70%);
            border-radius: 50%;
            pointer-events: none;
        }
        .scholar-stat-box {
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 10px;
            padding: 14px 20px;
            text-align: center;
            backdrop-filter: blur(8px);
            transition: all 0.3s ease;
        }
        .scholar-stat-box:hover {
            background: rgba(255, 255, 255, 0.14);
            transform: translateY(-2px);
        }
        .scholar-stat-number {
            font-size: 26px;
            font-weight: 800;
            color: #38bdf8;
            line-height: 1.2;
        }
        .scholar-stat-label {
            font-size: 12px;
            color: #cbd5e1;
            margin-bottom: 0;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .pub-search-box {
            position: relative;
        }
        .pub-search-box input {
            padding-left: 44px;
            height: 48px;
            border-radius: 24px;
            border: 1px solid #cbd5e1;
            font-size: 15px;
            transition: all 0.3s ease;
        }
        .pub-search-box input:focus {
            border-color: #2563eb;
            box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.2);
        }
        .pub-search-box i {
            position: absolute;
            left: 18px;
            top: 14px;
            font-size: 18px;
            color: #94a3b8;
        }
        .filter-btn {
            border: 1px solid #e2e8f0;
            background: #ffffff;
            color: #475569;
            padding: 8px 18px;
            border-radius: 20px;
            font-size: 14px;
            font-weight: 600;
            margin: 4px;
            transition: all 0.25s ease;
            cursor: pointer;
            outline: none !important;
        }
        .filter-btn:hover {
            border-color: #2563eb;
            color: #2563eb;
            background: #eff6ff;
        }
        .filter-btn.active {
            background: #2563eb;
            color: #ffffff;
            border-color: #2563eb;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
        }
        .publication-card {
            background: #ffffff;
            border-radius: 12px;
            border: 1px solid rgba(226, 232, 240, 0.9);
            box-shadow: 0 4px 18px rgba(0, 0, 0, 0.03);
            padding: 26px;
            margin-bottom: 22px;
            transition: all 0.3s ease;
            position: relative;
        }
        .publication-card:hover {
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
            border-color: rgba(37, 99, 235, 0.45);
            transform: translateY(-2px);
        }
        .pub-num-badge {
            background: #eff6ff;
            color: #1e40af;
            font-weight: 700;
            font-size: 13px;
            padding: 4px 10px;
            border-radius: 6px;
            display: inline-block;
            margin-right: 8px;
        }
        .pub-type-badge {
            display: inline-block;
            font-size: 11px;
            font-weight: 700;
            padding: 4px 10px;
            border-radius: 20px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-right: 6px;
        }
        .badge-ieee {
            background-color: #e0f2fe;
            color: #0369a1;
            border: 1px solid #bae6fd;
        }
        .badge-journal {
            background-color: #e0e7ff;
            color: #3730a3;
            border: 1px solid #c7d2fe;
        }
        .badge-topic {
            background-color: #ede9fe;
            color: #6d28d9;
            border: 1px solid #ddd6fe;
        }
        .pub-title {
            font-size: 18px;
            font-weight: 700;
            line-height: 1.45;
            color: #0f172a;
            margin-top: 10px;
            margin-bottom: 8px;
        }
        .pub-title a {
            color: #0f172a;
            text-decoration: none;
            transition: color 0.2s ease;
        }
        .pub-title a:hover {
            color: #2563eb;
        }
        .pub-venue {
            font-size: 14px;
            font-weight: 600;
            color: #334155;
            margin-bottom: 6px;
        }
        .pub-authors {
            font-size: 13.5px;
            color: #64748b;
            margin-bottom: 12px;
        }
        .pub-authors strong {
            color: #2563eb;
            font-weight: 700;
        }
        .pub-abstract {
            font-size: 14px;
            color: #475569;
            line-height: 1.6;
            margin-bottom: 16px;
            background: #f8fafc;
            border-left: 3px solid #2563eb;
            padding: 10px 14px;
            border-radius: 0 6px 6px 0;
        }
        .pub-tag {
            display: inline-block;
            font-size: 12px;
            background: #f1f5f9;
            color: #475569;
            padding: 2px 10px;
            border-radius: 12px;
            margin-right: 6px;
            margin-bottom: 6px;
            font-weight: 500;
        }
        .btn-pub-action {
            font-size: 13px;
            font-weight: 600;
            padding: 6px 14px;
            border-radius: 6px;
            transition: all 0.2s ease;
            margin-right: 8px;
            margin-top: 6px;
            display: inline-flex;
            align-items: center;
            text-decoration: none !important;
        }
        .btn-pub-primary {
            background-color: #2563eb;
            color: #ffffff;
            border: 1px solid #2563eb;
        }
        .btn-pub-primary:hover {
            background-color: #1d4ed8;
            color: #ffffff;
            box-shadow: 0 3px 10px rgba(37, 99, 235, 0.35);
        }
        .btn-pub-outline {
            background-color: transparent;
            color: #475569;
            border: 1px solid #cbd5e1;
        }
        .btn-pub-outline:hover {
            background-color: #f1f5f9;
            color: #0f172a;
            border-color: #94a3b8;
        }
        .btn-pub-scholar {
            background-color: #2563eb;
            color: #ffffff;
            border: 1px solid #2563eb;
        }
        .btn-pub-scholar:hover {
            background-color: #1d4ed8;
            color: #ffffff;
        }

        /* Citation Modal */
        .bibtex-preview {
            background: #0f172a;
            color: #e2e8f0;
            padding: 16px;
            border-radius: 8px;
            font-family: 'Courier New', Courier, monospace;
            font-size: 13px;
            white-space: pre-wrap;
            word-break: break-all;
            max-height: 280px;
            overflow-y: auto;
            border: 1px solid #334155;
        }

        /* Dark mode overrides */
        body.dark-mode .scholar-hero-card {
            background: linear-gradient(135deg, #070c18 0%, #0f172a 50%, #1e293b 100%);
            border: 1px solid #334155;
        }
        body.dark-mode .publication-card {
            background: #1f2937;
            border-color: #374151;
            box-shadow: 0 4px 18px rgba(0, 0, 0, 0.25);
        }
        body.dark-mode .pub-title,
        body.dark-mode .pub-title a {
            color: #f9fafb;
        }
        body.dark-mode .pub-venue {
            color: #cbd5e1;
        }
        body.dark-mode .pub-authors {
            color: #9ca3af;
        }
        body.dark-mode .pub-abstract {
            background: #111827;
            color: #d1d5db;
            border-left-color: #3b82f6;
        }
        body.dark-mode .pub-tag {
            background: #374151;
            color: #e5e7eb;
        }
        body.dark-mode .pub-num-badge {
            background: #1e3a8a;
            color: #93c5fd;
        }
        body.dark-mode .filter-btn {
            background: #1f2937;
            color: #d1d5db;
            border-color: #374151;
        }
        body.dark-mode .filter-btn:hover {
            background: #374151;
            color: #60a5fa;
        }
        body.dark-mode .filter-btn.active {
            background: #2563eb;
            color: #ffffff;
            border-color: #2563eb;
        }
        body.dark-mode .pub-search-box input {
            background: #1f2937;
            border-color: #374151;
            color: #f9fafb;
        }
        body.dark-mode .btn-pub-outline {
            color: #cbd5e1;
            border-color: #4b5563;
        }
        body.dark-mode .btn-pub-outline:hover {
            background: #374151;
            color: #ffffff;
        }
        .patent-showcase-box {
            background: #ffffff;
            border-radius: 14px;
            border: 1px solid rgba(59, 130, 246, 0.25);
            padding: 26px;
            box-shadow: 0 4px 20px rgba(15, 23, 42, 0.04);
            margin-bottom: 30px;
        }
        .patent-card {
            background: #f8fafc;
            border-radius: 12px;
            border: 1px solid #e2e8f0;
            padding: 22px;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: all 0.25s ease;
        }
        .patent-card:hover {
            border-color: #2563eb;
            box-shadow: 0 8px 24px rgba(37, 99, 235, 0.08);
            transform: translateY(-2px);
        }
        .patent-title {
            font-size: 15.5px;
            font-weight: 700;
            line-height: 1.45;
            color: #0f172a;
            margin-top: 6px;
            margin-bottom: 8px;
        }
        .patent-meta {
            font-size: 13px;
            color: #64748b;
            margin-bottom: 10px;
        }
        .patent-number {
            color: #2563eb;
            font-weight: 700;
        }
        .patent-desc {
            font-size: 13.5px;
            color: #475569;
            line-height: 1.6;
        }
        body.dark-mode .patent-showcase-box {
            background: #111827;
            border-color: rgba(59, 130, 246, 0.3);
        }
        body.dark-mode .patent-card {
            background: #1f2937;
            border-color: #374151;
        }
        body.dark-mode .patent-card:hover {
            border-color: #3b82f6;
        }
        body.dark-mode .patent-title {
            color: #f3f4f6;
        }
        body.dark-mode .patent-desc {
            color: #cbd5e1;
        }
    </style>
</head>

<body>
    <!-- Loader -->
    <div id="preloader">
        <div id="status">
            <div class="spinner">
                <div class="double-bounce1"></div>
                <div class="double-bounce2"></div>
            </div>
        </div>
    </div>
    <!-- Loader -->

    <!-- Navbar Start -->
    <nav class="navbar navbar-expand-lg fixed-top navbar-custom navbar-light sticky" id="navbar">
        <div class="container">
            <a class="navbar-brand brand-logo-wrap" href="index" title="Harsh Verma - Home">
                <span class="brand-monogram-emblem">
                    <svg class="brand-logo-svg" width="34" height="34" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <defs>
                            <linearGradient id="hvNavGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                                <stop offset="0%" stop-color="#1e40af" />
                                <stop offset="55%" stop-color="#2563eb" />
                                <stop offset="100%" stop-color="#4f46e5" />
                            </linearGradient>
                            <linearGradient id="hvNavAccentGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                                <stop offset="0%" stop-color="#38bdf8" />
                                <stop offset="100%" stop-color="#818cf8" />
                            </linearGradient>
                        </defs>
                        <rect width="40" height="40" rx="10" fill="url(#hvNavGrad)" />
                        <rect x="0.75" y="0.75" width="38.5" height="38.5" rx="9.25" stroke="rgba(255,255,255,0.22)" stroke-width="1.5" />
                        <path d="M11 12V28M11 20H19M19 12V28" stroke="#ffffff" stroke-width="2.75" stroke-linecap="round" stroke-linejoin="round"/>
                        <path d="M23 12L28.5 28L34 12" stroke="url(#hvNavAccentGrad)" stroke-width="2.75" stroke-linecap="round" stroke-linejoin="round"/>
                        <circle cx="34" cy="12" r="1.75" fill="#38bdf8" />
                    </svg>
                </span>
                <span class="brand-name-text">
                    <span class="brand-first-name">Harsh</span><span class="brand-last-name">Verma</span>
                </span>
            </a>

            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
                <i class="mdi mdi-menu"></i>
            </button>

            <div class="collapse navbar-collapse" id="navbarCollapse">
                <ul class="navbar-nav ml-auto navbar-center" id="mySidenav">
                    <li class="nav-item">
                        <a class="nav-link" href="page-about">About</a>
                    </li>
                    <li class="nav-item active">
                        <a class="nav-link" href="page-publications">Publications</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="page-awards">Awards</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="page-memberships">Memberships</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="page-media">Media</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="page-events">Speaker</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="page-books">Books</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="page-blog">Blog</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="javascript:void(0)" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            More <i class="mdi mdi-chevron-down nav-dropdown-arrow"></i>
                        </a>
                        <div class="dropdown-menu dropdown-menu-right nav-custom-dropdown" aria-labelledby="navbarDropdown">
                            <div class="nav-dropdown-header">
                                <span>Extended Portfolios &amp; Hubs</span>
                            </div>
                            <a class="dropdown-item nav-dropdown-item" href="page-portfolio">
                                <div class="dropdown-item-icon bg-soft-info"><i class="mdi mdi-cube-outline"></i></div>
                                <div class="dropdown-item-content">
                                    <span class="dropdown-item-title">Portfolio Projects</span>
                                    <span class="dropdown-item-desc">Architectures, agent frameworks &amp; systems</span>
                                </div>
                            </a>
                            <a class="dropdown-item nav-dropdown-item" href="page-social">
                                <div class="dropdown-item-icon bg-soft-success"><i class="mdi mdi-share-variant"></i></div>
                                <div class="dropdown-item-content">
                                    <span class="dropdown-item-title">Social &amp; Routine <span class="badge badge-pill badge-primary ml-1" style="font-size: 10px;">Feed</span></span>
                                    <span class="dropdown-item-desc">LinkedIn &amp; Instagram routine updates</span>
                                </div>
                            </a>
                            <a class="dropdown-item nav-dropdown-item" href="page-about#verified-profiles">
                                <div class="dropdown-item-icon bg-soft-warning"><i class="mdi mdi-shield-account-outline"></i></div>
                                <div class="dropdown-item-content">
                                    <span class="dropdown-item-title">38 Verified Profiles Hub</span>
                                    <span class="dropdown-item-desc">Academic, editorial &amp; executive registries</span>
                                </div>
                            </a>
                            <div class="dropdown-divider my-2"></div>
                            <a class="dropdown-item nav-dropdown-item" href="index#contact">
                                <div class="dropdown-item-icon bg-soft-danger"><i class="mdi mdi-email-outline"></i></div>
                                <div class="dropdown-item-content">
                                    <span class="dropdown-item-title">Contact Harsh</span>
                                    <span class="dropdown-item-desc">Advisory, keynotes &amp; consultations</span>
                                </div>
                            </a>
                        </div>
                    </li>
                </ul>

                <ul class="top-right list-unstyled list-inline mb-0 ml-lg-3 nav-social d-flex align-items-center">
                    <li class="list-inline-item mr-2">
                        <a href="https://scholar.google.com/citations?hl=en&user=zSt9oRMAAAAJ" target="_blank" class="nav-social-btn" title="Google Scholar (22+ Papers)">
                            <i class="mdi mdi-school"></i>
                        </a>
                    </li>
                    <li class="list-inline-item mr-2">
                        <a href="https://www.linkedin.com/in/harshverma59/" target="_blank" class="nav-social-btn" title="LinkedIn Profile">
                            <i class="mdi mdi-linkedin"></i>
                        </a>
                    </li>
                    <li class="list-inline-item mr-2">
                        <a href="https://www.instagram.com/iamharshverma/" target="_blank" class="nav-social-btn" title="Instagram Profile">
                            <i class="mdi mdi-instagram"></i>
                        </a>
                    </li>
                    <li class="list-inline-item mr-2">
                        <a href="https://github.com/iamharshverma" target="_blank" class="nav-social-btn" title="GitHub Profile">
                            <i class="mdi mdi-github-face"></i>
                        </a>
                    </li>
                    <li class="list-inline-item">
                        <button type="button" class="theme-toggle-btn" id="theme-toggle" aria-label="Toggle dark mode" title="Toggle theme">
                            <svg class="icon-moon" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
                            <svg class="icon-sun" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
                        </button>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <!-- Navbar End -->

    <!-- Hero Header Start -->
    <section class="section bg-light" style="padding-top: 130px; padding-bottom: 40px;">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <div class="scholar-hero-card mb-4">
                        <div class="row align-items-center">
                            <div class="col-lg-7 mb-4 mb-lg-0">
                                <div class="d-flex align-items-center mb-3">
                                    <span class="badge badge-pill text-white px-3 py-2 font-weight-bold mr-2" style="background: linear-gradient(135deg, #2563eb 0%, #0ea5e9 100%);">
                                        <i class="mdi mdi-school mr-1"></i> Academic Profile
                                    </span>
                                    <span class="text-white-50 small"><i class="mdi mdi-check-decagram text-info mr-1"></i> Verified Author</span>
                                </div>
                                <h1 class="text-white font-weight-bold mb-3 display-5" style="font-size: 2.2rem;">Research Publications & Scientific Contributions</h1>
                                <p class="text-light mb-4" style="line-height: 1.7; font-size: 15.5px; opacity: 0.9;">
                                    Peer-reviewed papers spanning <strong>Autonomous AI Agentic Architectures</strong>, <strong>Multi-Agent Security & Trust Graphs</strong>, <strong>Explainable AI (XAI)</strong>, <strong>Adversarial Machine Learning</strong>, and <strong>Real-Time Distributed Telemetry</strong>.
                                </p>
                                <div class="d-flex flex-wrap align-items-center">
                                    <a href="https://scholar.google.com/citations?hl=en&user=zSt9oRMAAAAJ" target="_blank" class="btn btn-primary font-weight-bold rounded px-4 py-2 mr-3 mb-2 shadow" style="background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%); border: none;">
                                        <i class="mdi mdi-school mr-1"></i> View on Google Scholar <i class="mdi mdi-open-in-new ml-1"></i>
                                    </a>
                                    <a href="https://mygsb.academia.edu/harshverma" target="_blank" class="btn btn-outline-light rounded px-3 py-2 mr-2 mb-2">
                                        <i class="mdi mdi-school-outline mr-1"></i> Academia
                                    </a>
                                    <a href="https://www.researchgate.net/profile/Harsh-Verma-43" target="_blank" class="btn btn-outline-light rounded px-3 py-2 mb-2">
                                        <i class="mdi mdi-earth mr-1"></i> ResearchGate
                                    </a>
                                </div>
                            </div>

                            <div class="col-lg-5">
                                <div class="row">
                                    <div class="col-6 mb-3">
                                        <div class="scholar-stat-box" id="scholar-stat-patents">
                                            <div class="scholar-stat-number" id="scholar-stat-patents-count">6</div>
                                            <div class="scholar-stat-label">Patents (1 Granted, 4 In Process)</div>
                                        </div>
                                    </div>
                                    <div class="col-6 mb-3">
                                        <div class="scholar-stat-box" id="scholar-stat-papers">
                                            <div class="scholar-stat-number">22</div>
                                            <div class="scholar-stat-label">Published Papers</div>
                                        </div>
                                    </div>
                                    <div class="col-6">
                                        <div class="scholar-stat-box" id="scholar-stat-journals">
                                            <div class="scholar-stat-number">6+</div>
                                            <div class="scholar-stat-label">Indexed Journals</div>
                                        </div>
                                    </div>
                                    <div class="col-6">
                                        <div class="scholar-stat-box" id="scholar-stat-span">
                                            <div class="scholar-stat-number" style="font-size: clamp(18px, 1.8vw, 24px); white-space: nowrap;">2011-Present</div>
                                            <div class="scholar-stat-label">Research Span</div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Patents Showcase Section -->
            <div class="row">
                <div class="col-12">
                    <div class="patent-showcase-box">
                        <div class="d-flex flex-wrap justify-content-between align-items-center mb-3">
                            <div>
                                <span class="badge badge-pill text-white px-3 py-1 font-weight-bold mb-1" style="background: linear-gradient(135deg, #2563eb 0%, #16a34a 100%);">
                                    <i class="mdi mdi-certificate mr-1"></i> Intellectual Property Portfolio (6 Patents Total)
                                </span>
                                <h3 class="font-weight-bold text-dark mb-0 mt-1" style="font-size: 1.4rem;">Patents &amp; Inventions</h3>
                                <p class="text-muted mb-0 small">1 Granted Patent · 1 Published Application · 4 Pending/In-Process Applications at Palo Alto Networks</p>
                            </div>
                            <a href="https://iprsearch.ipindia.gov.in/PublicSearch/PublicationSearch/" target="_blank" class="btn btn-outline-primary btn-sm rounded font-weight-bold mt-2 mt-sm-0">
                                <i class="mdi mdi-shield-search mr-1"></i> IP India Patent Search Portal <i class="mdi mdi-open-in-new ml-1"></i>
                            </a>
                        </div>
                        
                        <div class="row">
                            <!-- In-Process Patents Card: Palo Alto Networks -->
                            <div class="col-12 mb-3">
                                <div class="patent-card" style="border: 1.5px solid #6366f1; background: linear-gradient(180deg, rgba(99, 102, 241, 0.04) 0%, rgba(248, 250, 252, 1) 100%);">
                                    <div>
                                        <div class="d-flex flex-wrap justify-content-between align-items-center mb-2">
                                            <div class="d-flex flex-wrap align-items-center">
                                                <span class="badge text-white font-weight-bold px-2.5 py-1 mr-2 mb-1" style="background: linear-gradient(135deg, #4f46e5 0%, #6366f1 100%); font-size: 11.5px;">
                                                    <i class="mdi mdi-progress-clock mr-1"></i> 4 Patents In Process · Undisclosed
                                                </span>
                                                <span class="badge badge-light border text-dark font-weight-bold mb-1" style="font-size: 11px;">
                                                    <i class="mdi mdi-domain mr-1 text-primary"></i> Assignee: Palo Alto Networks
                                                </span>
                                            </div>
                                            <span class="badge badge-warning text-dark font-weight-bold px-2 py-1 mb-1" style="font-size: 11px; background-color: #fef08a; border: 1px solid #fde047;">
                                                <i class="mdi mdi-lock-outline mr-1"></i> Active Patent Office Review
                                            </span>
                                        </div>
                                        
                                        <h4 class="patent-title" style="color: #1e1b4b; font-size: 17px;">
                                            AGENTIC AI, ENTERPRISE COPILOT SYSTEMS &amp; COPILOT NAVIGATION ARCHITECTURES
                                        </h4>
                                        
                                        <div class="patent-meta d-flex flex-wrap align-items-center">
                                            <span class="patent-number" style="color: #4f46e5;">
                                                <i class="mdi mdi-file-tree-outline mr-1"></i> Suite: <strong>4 Patent Applications</strong>
                                            </span>
                                            <span class="mx-2 text-muted">•</span>
                                            <span class="text-muted">Filing Organization: <strong>Palo Alto Networks</strong></span>
                                            <span class="mx-2 text-muted">•</span>
                                            <span class="text-muted">Domain: <strong>Agentic AI &amp; Copilot Navigation</strong></span>
                                        </div>

                                        <div class="patent-desc mb-3">
                                            Proprietary suite of four in-process patent applications developing foundational intellectual property in autonomous <strong>Agentic AI</strong> orchestration workflows, <strong>Enterprise Copilot</strong> reasoning loops, and intelligent multi-modal <strong>Copilot Navigation</strong> architectures for automated contextual security operations and multi-tier enterprise decision execution.
                                        </div>

                                        <div class="d-flex flex-wrap align-items-center" style="gap: 6px;">
                                            <span class="badge badge-pill badge-light border text-muted px-2.5 py-1 font-weight-bold" style="font-size: 11px;"># Agentic AI</span>
                                            <span class="badge badge-pill badge-light border text-muted px-2.5 py-1 font-weight-bold" style="font-size: 11px;"># Enterprise Copilot Systems</span>
                                            <span class="badge badge-pill badge-light border text-muted px-2.5 py-1 font-weight-bold" style="font-size: 11px;"># Copilot Navigation</span>
                                            <span class="badge badge-pill badge-light border text-muted px-2.5 py-1 font-weight-bold" style="font-size: 11px;"># Contextual Security Operations</span>
                                            <span class="badge badge-pill badge-light border text-muted px-2.5 py-1 font-weight-bold" style="font-size: 11px;"># Autonomous Execution</span>
                                        </div>
                                    </div>
                                    <div class="d-flex flex-wrap justify-content-between align-items-center mt-3 pt-2 border-top">
                                        <div class="small text-muted font-italic">
                                            <i class="mdi mdi-information-outline mr-1"></i> Specific claims and filing serial identifiers remain non-disclosed under standard patent office review and enterprise IP protection protocols.
                                        </div>
                                        <span class="badge badge-pill badge-primary px-3 py-1 font-weight-bold" style="background-color: #4f46e5;">Palo Alto Networks IP</span>
                                    </div>
                                </div>
                            </div>

                            <!-- Patent 1 -->
                            <div class="col-lg-6 mb-3 mb-lg-0">
                                <div class="patent-card">
                                    <div>
                                        <div class="d-flex justify-content-between align-items-center mb-2">
                                            <span class="badge badge-success font-weight-bold px-2 py-1" style="background-color: #16a34a;">
                                                <i class="mdi mdi-check-decagram mr-1"></i> Granted Patent
                                            </span>
                                            <span class="badge badge-light border text-muted font-weight-bold">Issued Dec 3, 2024</span>
                                        </div>
                                        <h4 class="patent-title">SYSTEMS AND METHODS FOR PERFORMING LOAD TESTING OF A SOCIAL NETWORKING APPLICATION</h4>
                                        <div class="patent-meta">
                                            <span class="patent-number"><i class="mdi mdi-certificate mr-1"></i> Patent No: <strong>555747</strong></span>
                                            <span class="ml-2 text-muted">• Status: <strong>Granted</strong></span>
                                            <span class="ml-2 text-muted">• Authority: <strong>Indian Patent Office</strong></span>
                                        </div>
                                        <div class="patent-desc">
                                            Novel architecture and methodology for orchestrating automated, high-throughput load simulation, performance stress benchmarking, and real-time telemetry testing across social networking applications and distributed service topologies.
                                        </div>
                                    </div>
                                    <div class="d-flex flex-wrap align-items-center mt-3 pt-2 border-top">
                                        <a href="https://iprsearch.ipindia.gov.in/PublicSearch/PublicationSearch/" target="_blank" class="btn-pub-action btn-pub-primary">
                                            <i class="mdi mdi-magnify mr-1"></i> Official Patent Search (555747) <i class="mdi mdi-open-in-new ml-1"></i>
                                        </a>
                                        <button type="button" class="btn-pub-action btn-pub-outline" onclick="copyPatentDetails('SYSTEMS AND METHODS FOR PERFORMING LOAD TESTING OF A SOCIAL NETWORKING APPLICATION', '555747', 'Dec 3, 2024', 'Granted')">
                                            <i class="mdi mdi-content-copy mr-1"></i> Copy Info
                                        </button>
                                    </div>
                                </div>
                            </div>

                            <!-- Patent 2 -->
                            <div class="col-lg-6">
                                <div class="patent-card">
                                    <div>
                                        <div class="d-flex justify-content-between align-items-center mb-2">
                                            <span class="badge text-white font-weight-bold px-2 py-1" style="background-color: #0284c7;">
                                                <i class="mdi mdi-file-certificate mr-1"></i> Published Patent
                                            </span>
                                            <span class="badge badge-light border text-muted font-weight-bold">Published Jun 26, 2020</span>
                                        </div>
                                        <h4 class="patent-title">COVID PREVENTIVE AUTOMATED ENTRY POINT (COPAEP)</h4>
                                        <div class="patent-meta">
                                            <span class="patent-number" style="color: #0284c7;"><i class="mdi mdi-file-document-outline mr-1"></i> App No: <strong>IN 202011024968</strong></span>
                                            <span class="ml-2 text-muted">• Status: <strong>Published</strong></span>
                                            <span class="ml-2 text-muted">• Authority: <strong>Indian Patent Office</strong></span>
                                        </div>
                                        <div class="patent-desc">
                                            Integrated automated screening checkpoint system incorporating multi-tier sensor subsystems for non-contact thermal scanning, sanitization misting, and intelligent automated entrance symptomatic verification.
                                        </div>
                                    </div>
                                    <div class="d-flex flex-wrap align-items-center mt-3 pt-2 border-top">
                                        <a href="https://iprsearch.ipindia.gov.in/PublicSearch/PublicationSearch/" target="_blank" class="btn-pub-action btn-pub-primary" style="background-color: #0284c7; border-color: #0284c7;">
                                            <i class="mdi mdi-magnify mr-1"></i> Official Patent Search (202011024968) <i class="mdi mdi-open-in-new ml-1"></i>
                                        </a>
                                        <button type="button" class="btn-pub-action btn-pub-outline" onclick="copyPatentDetails('COVID PREVENTIVE AUTOMATED ENTRY POINT (COPAEP)', 'IN 202011024968', 'Jun 26, 2020', 'Published')">
                                            <i class="mdi mdi-content-copy mr-1"></i> Copy Info
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Controls: Search & Category Filters -->
            <div class="row mt-2 mb-4">
                <div class="col-lg-5 mb-3 mb-lg-0">
                    <div class="pub-search-box">
                        <i class="mdi mdi-magnify"></i>
                        <input type="text" id="pubSearchInput" class="form-control" placeholder="Search by title, keyword, DOI, journal, or topic (e.g. Agent, Security, IEEE)...">
                    </div>
                </div>
                <div class="col-lg-7">
                    <div class="d-flex flex-wrap align-items-center justify-content-lg-end" id="categoryFilters">
                        <button class="filter-btn active" data-filter="all">All Papers (22)</button>
                        <button class="filter-btn" data-filter="agents">AI Agentic Systems</button>
                        <button class="filter-btn" data-filter="security">AI Security & Trust</button>
                        <button class="filter-btn" data-filter="cloud_ai">Cloud & Infrastructure</button>
                        <button class="filter-btn" data-filter="software_eng">Software Eng & Ethics</button>
                        <button class="filter-btn" data-filter="iot">IoT & Performance</button>
                    </div>
                </div>
            </div>

            <!-- Publications Listing -->
            <div class="row">
                <div class="col-12">
                    <div class="d-flex justify-content-between align-items-center mb-3">
                        <span class="text-muted font-weight-bold small text-uppercase" id="showingCount">Showing all 22 publications</span>
                        <a href="https://scholar.google.com/citations?hl=en&user=zSt9oRMAAAAJ" target="_blank" class="small text-primary font-weight-bold">
                            Open Scholar Citations <i class="mdi mdi-open-in-new"></i>
                        </a>
                    </div>

                    <div id="publicationsContainer">
"""

cards_html = []
for idx, p in enumerate(papers, 1):
    tags_html = "".join([f'<span class="pub-tag">{t}</span>' for t in p.get('tags', [])])
    
    vol_str = f" • {p['volume']}" if p.get('volume') else ""
    doi_str = p.get('doi', '')
    doi_url = f"https://doi.org/{doi_str}" if not doi_str.startswith("http") else doi_str
    
    badge_class = "badge-ieee" if p.get("category") == "conference" else "badge-journal"
    
    alt_link_btn = ""
    if p.get("alt_link"):
        alt_link_btn = f'''<a href="{p['alt_link']}" target="_blank" class="btn-pub-action btn-pub-outline">
            <i class="mdi mdi-earth mr-1"></i> {p.get('alt_label', 'ResearchGate')} <i class="mdi mdi-open-in-new ml-1"></i>
        </a>'''

    bibtex_json = json.dumps(p['bibtex'])

    card = f"""
                        <!-- Publication #{idx} -->
                        <div class="publication-card" data-topic="{p.get('topic', '')}" data-category="{p.get('category', '')}" data-id="{p['id']}">
                            <div class="d-flex flex-wrap align-items-center justify-content-between">
                                <div>
                                    <span class="pub-num-badge">#{idx}</span>
                                    <span class="pub-type-badge {badge_class}">{p.get('category_label', 'Journal')}</span>
                                    <span class="pub-type-badge badge-topic">{p.get('topic_label', 'AI')}</span>
                                </div>
                                <span class="badge badge-light text-muted font-weight-bold py-1 px-2 border">{p['year']}</span>
                            </div>

                            <h3 class="pub-title">
                                <a href="{p['link']}" target="_blank">{p['title']}</a>
                            </h3>

                            <div class="pub-venue">
                                <i class="mdi mdi-book-open-page-variant mr-1 text-primary"></i>
                                {p['venue']}{vol_str} ({p['year']})
                            </div>

                            <div class="pub-authors">
                                <i class="mdi mdi-account-multiple mr-1 text-muted"></i>
                                Authors: <strong>{p['authors']}</strong>
                                <span class="ml-2 text-muted">• Publisher: {p['publisher']}</span>
                                {f'<span class="ml-2 text-muted">• DOI: <code>{doi_str}</code></span>' if doi_str else ''}
                            </div>

                            <div class="pub-abstract">
                                <strong>Abstract:</strong> {p['abstract']}
                            </div>

                            <div class="d-flex flex-wrap align-items-center justify-content-between pt-2">
                                <div class="mb-2 mb-md-0">
                                    {tags_html}
                                </div>

                                <div class="d-flex flex-wrap align-items-center">
                                    <a href="{p['link']}" target="_blank" class="btn-pub-action btn-pub-primary">
                                        <i class="mdi mdi-open-in-new mr-1"></i> Read Paper
                                    </a>
                                    <a href="{doi_url}" target="_blank" class="btn-pub-action btn-pub-outline">
                                        <i class="mdi mdi-link-variant mr-1"></i> DOI
                                    </a>
                                    {alt_link_btn}
                                    <button class="btn-pub-action btn-pub-outline btn-cite" onclick='openCiteModal({idx}, {json.dumps(p["title"])}, {bibtex_json})'>
                                        <i class="mdi mdi-format-quote-close mr-1"></i> Cite
                                    </button>
                                </div>
                            </div>
                        </div>
    """
    cards_html.append(card)

html_template += "\n".join(cards_html)

html_template += """
                    </div>

                    <!-- No Results Fallback -->
                    <div id="noResults" class="text-center py-5 d-none">
                        <i class="mdi mdi-file-search-outline text-muted display-4"></i>
                        <h4 class="mt-3 text-muted">No publications found</h4>
                        <p class="text-muted">Try adjusting your search query or switching filter categories.</p>
                        <button class="btn btn-outline-primary rounded" onclick="resetFilters()">Reset Filters</button>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- Hero Header End -->

    <!-- Citation Modal -->
    <div class="modal fade" id="citeModal" tabindex="-1" role="dialog" aria-labelledby="citeModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered modal-lg" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title font-weight-bold" id="citeModalLabel"><i class="mdi mdi-format-quote-close text-primary mr-1"></i> Export Citation</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <p class="font-weight-bold text-dark mb-2" id="citePaperTitle"></p>
                    <p class="text-muted small mb-2">BibTeX format for LaTeX, Overleaf, Mendeley, and Zotero:</p>
                    <pre class="bibtex-preview" id="bibtexContent"></pre>
                    <div id="copyAlert" class="alert alert-success d-none py-2 px-3 small">
                        <i class="mdi mdi-check mr-1"></i> BibTeX copied to clipboard!
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary rounded" data-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary rounded font-weight-bold" id="btnCopyBibtex" onclick="copyBibtexToClipboard()">
                        <i class="mdi mdi-content-copy mr-1"></i> Copy BibTeX
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- Footer Start -->
    <footer class="footer bg-light">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-12 text-center">
                    <a href="index" class="footer-logo brand-logo-wrap font-weight-bold d-inline-flex justify-content-center align-items-center" style="text-decoration: none;">
                        <span class="brand-monogram-emblem">
                            <svg class="brand-logo-svg" width="38" height="38" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <defs>
                                    <linearGradient id="hvFootGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                                        <stop offset="0%" stop-color="#1e40af" />
                                        <stop offset="55%" stop-color="#2563eb" />
                                        <stop offset="100%" stop-color="#4f46e5" />
                                    </linearGradient>
                                    <linearGradient id="hvFootAccentGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                                        <stop offset="0%" stop-color="#38bdf8" />
                                        <stop offset="100%" stop-color="#818cf8" />
                                    </linearGradient>
                                </defs>
                                <rect width="40" height="40" rx="10" fill="url(#hvFootGrad)" />
                                <rect x="0.75" y="0.75" width="38.5" height="38.5" rx="9.25" stroke="rgba(255,255,255,0.22)" stroke-width="1.5" />
                                <path d="M11 12V28M11 20H19M19 12V28" stroke="#ffffff" stroke-width="2.75" stroke-linecap="round" stroke-linejoin="round"/>
                                <path d="M23 12L28.5 28L34 12" stroke="url(#hvFootAccentGrad)" stroke-width="2.75" stroke-linecap="round" stroke-linejoin="round"/>
                                <circle cx="34" cy="12" r="1.75" fill="#38bdf8" />
                            </svg>
                        </span>
                        <span class="brand-name-text">
                            <span class="brand-first-name">Harsh</span><span class="brand-last-name">Verma</span>
                        </span>
                    </a>
                    <p class="para-desc mx-auto mt-4 text-black" style="max-width: 650px;">
                        Principal Software Engineer in AI @ Palo Alto Networks • Forbes Technology Council Member • IEEE Senior Member • Stanford GSB Scholar
                    </p>
                    <ul class="list-unstyled mb-0 mt-4 social-icon">
                        <li class="list-inline-item mr-1"><a href="https://scholar.google.com/citations?hl=en&user=zSt9oRMAAAAJ" target="_blank" class="rounded-circle" title="Google Scholar"><i class="mdi mdi-school"></i></a></li>
                        <li class="list-inline-item mr-1"><a href="https://www.linkedin.com/in/harshverma59/" target="_blank" class="rounded-circle" title="LinkedIn"><i class="mdi mdi-linkedin"></i></a></li>
                        <li class="list-inline-item mr-1"><a href="https://github.com/iamharshverma" target="_blank" class="rounded-circle" title="GitHub"><i class="mdi mdi-github-face"></i></a></li>
                        <li class="list-inline-item mr-1"><a href="https://medium.com/@harshverma59" target="_blank" class="rounded-circle" title="Medium"><i class="mdi mdi-medium"></i></a></li>
                        <li class="list-inline-item mr-1"><a href="https://twitter.com/harshverma59" target="_blank" class="rounded-circle" title="Twitter"><i class="mdi mdi-twitter"></i></a></li>
                        <li class="list-inline-item mr-1"><a href="https://www.instagram.com/aiwithharsh/" target="_blank" class="rounded-circle" title="Instagram"><i class="mdi mdi-instagram"></i></a></li>
                    </ul>
                </div>
            </div>
        </div>
    </footer>
    <footer class="footer footer-bar bg-black">
        <div class="container text-foot text-center">
            <p class="mb-0 text-white-50">&copy; <script>document.write(new Date().getFullYear())</script> Harsh Verma. All rights reserved.</p>
        </div>
    </footer>
    <!-- Footer End -->

    <!-- Back to top -->    
    <a href="#" class="back-to-top rounded text-center" id="back-to-top"> 
        <i class="mdi mdi-chevron-up d-block"> </i> 
    </a>
    <!-- Back to top -->

    <!-- JavaScript -->
    <script src="js/jquery.min.js"></script>
    <script src="js/bootstrap.bundle.min.js"></script>
    <script src="js/jquery.easing.min.js"></script>
    <script src="js/scrollspy.min.js"></script>
    <script src="js/feather.min.js"></script>
    <script src="js/app.js"></script>

    <script>
        var yearEl = document.getElementById('currentYear');
        if (yearEl) yearEl.innerText = new Date().getFullYear();

        var currentActiveBibtex = "";

        function openCiteModal(id, title, bibtex) {
            document.getElementById('citePaperTitle').innerText = title;
            document.getElementById('bibtexContent').innerText = bibtex;
            currentActiveBibtex = bibtex;
            $('#copyAlert').addClass('d-none');
            $('#citeModal').modal('show');
        }

        function copyPatentDetails(title, number, date, status) {{
            var patentText = title + "\\nPatent/App Number: " + number + "\\nStatus: " + status + " (" + date + ")\\nIssuing Authority: Indian Patent Office (IP India)\\nSearch Portal: https://iprsearch.ipindia.gov.in/PublicSearch/PublicationSearch/";
            
            if (navigator.clipboard) {{
                navigator.clipboard.writeText(patentText).then(function() {{
                    alert("Patent details copied to clipboard:\\n\\n" + patentText);
                }}).catch(function() {{
                    prompt("Copy Patent Information:", patentText);
                }});
            }} else {{
                prompt("Copy Patent Information:", patentText);
            }}
        }}

        function copyBibtexToClipboard() {
            if (!currentActiveBibtex) return;
            navigator.clipboard.writeText(currentActiveBibtex).then(function() {
                $('#copyAlert').removeClass('d-none');
                setTimeout(function() {
                    $('#copyAlert').addClass('d-none');
                }, 3000);
            }).catch(function(err) {
                // Fallback for older browsers
                var textArea = document.createElement("textarea");
                textArea.value = currentActiveBibtex;
                document.body.appendChild(textArea);
                textArea.select();
                document.execCommand("Copy");
                textArea.remove();
                $('#copyAlert').removeClass('d-none');
                setTimeout(function() {
                    $('#copyAlert').addClass('d-none');
                }, 3000);
            });
        }

        // Filtering and search logic
        $(document).ready(function() {
            var activeFilter = "all";

            function filterPublications() {
                var query = $('#pubSearchInput').val().toLowerCase().trim();
                var visibleCount = 0;

                $('.publication-card').each(function() {
                    var $card = $(this);
                    var topic = $card.attr('data-topic');
                    var category = $card.attr('data-category');
                    var cardText = $card.text().toLowerCase();

                    var matchesCategory = false;
                    if (activeFilter === "all") {
                        matchesCategory = true;
                    } else if (activeFilter === "agents") {
                        matchesCategory = (topic === "agents");
                    } else if (activeFilter === "security") {
                        matchesCategory = (topic === "security");
                    } else if (activeFilter === "cloud_ai") {
                        matchesCategory = (topic === "cloud_ai");
                    } else if (activeFilter === "software_eng") {
                        matchesCategory = (topic === "software_eng" || topic === "ethics" || topic === "leadership");
                    } else if (activeFilter === "iot") {
                        matchesCategory = (topic === "iot" || topic === "performance");
                    }

                    var matchesQuery = (query === "" || cardText.indexOf(query) !== -1);

                    if (matchesCategory && matchesQuery) {
                        $card.show();
                        visibleCount++;
                    } else {
                        $card.hide();
                    }
                });

                $('#showingCount').text("Showing " + visibleCount + " of 22 publications");

                if (visibleCount === 0) {
                    $('#noResults').removeClass('d-none');
                } else {
                    $('#noResults').addClass('d-none');
                }
            }

            $('.filter-btn').on('click', function() {
                $('.filter-btn').removeClass('active');
                $(this).addClass('active');
                activeFilter = $(this).attr('data-filter');
                filterPublications();
            });

            $('#pubSearchInput').on('keyup input', function() {
                filterPublications();
            });

            window.resetFilters = function() {
                $('#pubSearchInput').val('');
                activeFilter = "all";
                $('.filter-btn').removeClass('active');
                $('.filter-btn[data-filter="all"]').addClass('active');
                filterPublications();
            };
        });
    </script>
</body>
</html>
"""

with open('page-publications.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("Generated page-publications.html successfully.")
