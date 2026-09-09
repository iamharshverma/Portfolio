import re

html_content = '''<!DOCTYPE html>
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
    <title>Harsh Verma | Invited Memberships, Fellowships & Senior Associations</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Explore invited memberships, royal fellowships, senior council appointments, and scientific honor societies of Harsh Verma across IEEE, Forbes Technology Council, Sigma Xi, UC Berkeley SkyDeck, RSA, AAAI, and ACM." />
    <meta name="keywords" content="Harsh Verma, Invited Memberships, IEEE Senior Member, Forbes Technology Council, Sigma Xi, RSA Fellow, AAAI, ACM SIGAI, SkyDeck Advisor, GDE, Raptors.Dev, Fellowships" />
    <meta content="Harsh Verma" name="author" />
    <meta property="og:title" content="Harsh Verma | Invited Memberships, Fellowships & Senior Associations" />
    <meta property="og:description" content="Explore invited memberships, royal fellowships, senior council appointments, and scientific honor societies of Harsh Verma across IEEE, Forbes Technology Council, Sigma Xi, UC Berkeley SkyDeck, RSA, AAAI, and ACM." />
    <!-- favicon -->
    <link rel="shortcut icon" href="images/favicon_new.ico">
    <!-- Bootstrap -->
    <link href="css/bootstrap.min.css" rel="stylesheet" type="text/css" />
    <!-- Icons -->
    <link href="css/materialdesignicons.min.css" rel="stylesheet" type="text/css" />
    <!-- Main css File -->
    <link href="css/style.css" rel="stylesheet" type="text/css" />
    <!-- Dark Mode css File -->
    <link href="css/dark-mode.css" rel="stylesheet" type="text/css" />
    <script src="js/dark-mode.js"></script>
    
    <style>
        /* Modern Memberships Page Styles */
        .membership-card {
            background: #ffffff;
            border: 1px solid rgba(226, 232, 240, 0.9);
            border-radius: 16px;
            transition: transform 0.28s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.28s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.28s ease;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            height: 100%;
        }
        .membership-card:hover {
            transform: translateY(-6px);
            box-shadow: 0 20px 35px -10px rgba(15, 23, 42, 0.12), 0 8px 16px -6px rgba(15, 23, 42, 0.06) !important;
            border-color: rgba(37, 99, 235, 0.4);
        }
        .membership-header-badge {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            padding: 24px 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            min-height: 140px;
            overflow: visible;
        }
        .membership-header-badge img {
            max-height: 95px;
            max-width: 90%;
            object-fit: contain;
            filter: drop-shadow(0 4px 10px rgba(0, 0, 0, 0.3));
            transition: transform 0.3s ease;
            position: relative;
            z-index: 1;
        }
        .membership-card:hover .membership-header-badge img {
            transform: scale(1.04);
        }
        .membership-tier-pill {
            position: absolute;
            top: 12px;
            right: 12px;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 10.5px;
            font-weight: 700;
            letter-spacing: 0.5px;
            text-transform: uppercase;
            box-shadow: 0 4px 14px rgba(0,0,0,0.4);
            z-index: 10;
        }
        .tier-fellow {
            background: linear-gradient(135deg, #b45309 0%, #d97706 100%);
            color: #ffffff;
        }
        .tier-senior {
            background: linear-gradient(135deg, #0369a1 0%, #0284c7 100%);
            color: #ffffff;
        }
        .tier-council {
            background: linear-gradient(135deg, #4338ca 0%, #6366f1 100%);
            color: #ffffff;
        }
        .tier-honor {
            background: linear-gradient(135deg, #047857 0%, #10b981 100%);
            color: #ffffff;
        }
        .tier-mentor {
            background: linear-gradient(135deg, #be123c 0%, #f43f5e 100%);
            color: #ffffff;
        }
        
        .membership-body {
            padding: 24px;
            display: flex;
            flex-direction: column;
            flex-grow: 1;
        }
        .membership-title {
            font-size: 19px;
            font-weight: 700;
            color: #0f172a;
            line-height: 1.35;
            margin-bottom: 6px;
        }
        .membership-org {
            font-size: 13.5px;
            font-weight: 600;
            color: #2563eb;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
        }
        .membership-credential-id {
            display: inline-flex;
            align-items: center;
            background: #f1f5f9;
            color: #475569;
            font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
            font-size: 11px;
            font-weight: 600;
            padding: 4px 10px;
            border-radius: 6px;
            margin-bottom: 14px;
            border: 1px dashed #cbd5e1;
        }
        .membership-desc {
            font-size: 14px;
            line-height: 1.6;
            color: #475569;
            margin-bottom: 18px;
            flex-grow: 1;
        }
        .membership-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            margin-bottom: 20px;
        }
        .membership-tag {
            font-size: 11px;
            font-weight: 600;
            color: #475569;
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 6px;
            padding: 3px 8px;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .membership-tag:hover {
            background: #eff6ff;
            color: #2563eb;
            border-color: #bfdbfe;
        }
        .membership-footer {
            margin-top: auto;
            pt: 10px;
            display: flex;
            gap: 10px;
            align-items: center;
        }
        .btn-verify {
            background: #f8fafc;
            color: #1e293b;
            border: 1px solid #cbd5e1;
            font-size: 13px;
            font-weight: 600;
            padding: 8px 16px;
            border-radius: 8px;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: all 0.2s ease;
            text-decoration: none;
            width: 100%;
            justify-content: center;
        }
        .btn-verify:hover {
            background: #2563eb;
            color: #ffffff !important;
            border-color: #2563eb;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25);
        }
        
        /* Stats Ribbon */
        .membership-stats-box {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            border-radius: 20px;
            padding: 36px 30px;
            color: #ffffff;
            box-shadow: 0 15px 35px rgba(15, 23, 42, 0.15);
            margin-bottom: 48px;
            position: relative;
            overflow: hidden;
        }
        .membership-stats-box::before {
            content: "";
            position: absolute;
            top: -50%;
            right: -10%;
            width: 350px;
            height: 350px;
            background: radial-gradient(circle, rgba(59, 130, 246, 0.15) 0%, rgba(59, 130, 246, 0) 70%);
            border-radius: 50%;
            pointer-events: none;
        }
        .stat-item {
            text-align: center;
            padding: 10px 15px;
        }
        .stat-number {
            font-size: 34px;
            font-weight: 800;
            color: #60a5fa;
            line-height: 1;
            margin-bottom: 6px;
            letter-spacing: -0.5px;
        }
        .stat-label {
            font-size: 13px;
            color: #94a3b8;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        /* Filter Pills */
        .filter-nav-wrap {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            justify-content: center;
            margin-bottom: 30px;
        }
        .btn-filter-pill {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            color: #475569;
            font-weight: 600;
            font-size: 13.5px;
            padding: 8px 18px;
            border-radius: 30px;
            cursor: pointer;
            transition: all 0.2s ease;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        }
        .btn-filter-pill:hover {
            border-color: #3b82f6;
            color: #2563eb;
            background: #eff6ff;
        }
        .btn-filter-pill.active {
            background: #2563eb;
            color: #ffffff;
            border-color: #2563eb;
            box-shadow: 0 4px 14px rgba(37, 99, 235, 0.3);
        }
        .filter-count-badge {
            background: rgba(0, 0, 0, 0.08);
            color: inherit;
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 11px;
            font-weight: 700;
        }
        .btn-filter-pill.active .filter-count-badge {
            background: rgba(255, 255, 255, 0.25);
            color: #ffffff;
        }

        /* Search input */
        .search-container {
            max-width: 680px;
            margin: 0 auto 28px;
            position: relative;
        }
        .search-input-field {
            width: 100%;
            padding: 14px 20px 14px 48px;
            border-radius: 50px;
            border: 1px solid #cbd5e1;
            font-size: 15px;
            background: #ffffff;
            color: #1e293b;
            box-shadow: 0 4px 16px rgba(15, 23, 42, 0.04);
            transition: all 0.2s ease;
        }
        .search-input-field:focus {
            outline: none;
            border-color: #2563eb;
            box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.15);
        }
        .search-icon-inside {
            position: absolute;
            left: 18px;
            top: 50%;
            transform: translateY(-50%);
            color: #94a3b8;
            font-size: 20px;
        }
        .search-clear-btn {
            position: absolute;
            right: 16px;
            top: 50%;
            transform: translateY(-50%);
            background: #e2e8f0;
            color: #64748b;
            border: none;
            width: 26px;
            height: 26px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            font-size: 14px;
            transition: all 0.2s ease;
        }
        .search-clear-btn:hover {
            background: #cbd5e1;
            color: #1e293b;
        }

        /* Navbar Header & Nav Link Visibility */
        .navbar-custom {
            background-color: rgba(255, 255, 255, 0.96) !important;
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            box-shadow: 0 4px 20px rgba(15, 23, 42, 0.06);
            border-bottom: 1px solid rgba(226, 232, 240, 0.8);
            padding: 16px 0;
            transition: all 0.3s ease;
        }
        .navbar-custom .navigation .navbar-nav-link .nav-item .nav-link {
            color: #334155 !important;
            font-weight: 600;
            font-size: 14.5px;
            transition: color 0.2s ease;
        }
        .navbar-custom .navigation .navbar-nav-link .nav-item:hover .nav-link,
        .navbar-custom .navigation .navbar-nav-link .nav-item.active .nav-link {
            color: #2563eb !important;
            font-weight: 700;
        }
        .navbar-custom .nav-social li a {
            color: #2563eb !important;
        }
        .navbar-custom .navbar-toggler {
            color: #1e293b !important;
        }
        .navbar-custom .navbar-toggler span[data-feather="menu"] {
            stroke: #1e293b !important;
        }

        /* Dark Mode Overrides */
        body.dark-mode .navbar-custom {
            background-color: rgba(11, 15, 25, 0.96) !important;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
        }
        body.dark-mode .navbar-custom .navigation .navbar-nav-link .nav-item .nav-link {
            color: #cbd5e1 !important;
        }
        body.dark-mode .navbar-custom .navigation .navbar-nav-link .nav-item:hover .nav-link,
        body.dark-mode .navbar-custom .navigation .navbar-nav-link .nav-item.active .nav-link {
            color: #60a5fa !important;
        }
        body.dark-mode .navbar-custom .nav-social li a {
            color: #60a5fa !important;
        }
        body.dark-mode .navbar-custom .navbar-toggler span[data-feather="menu"] {
            stroke: #f8fafc !important;
        }
        body.dark-mode .membership-card {
            background: #1e293b;
            border-color: #334155;
        }
        body.dark-mode .membership-card:hover {
            border-color: #60a5fa;
            box-shadow: 0 20px 35px -10px rgba(0, 0, 0, 0.6) !important;
        }
        body.dark-mode .membership-title {
            color: #f8fafc;
        }
        body.dark-mode .membership-desc {
            color: #94a3b8;
        }
        body.dark-mode .membership-credential-id {
            background: #0f172a;
            color: #94a3b8;
            border-color: #334155;
        }
        body.dark-mode .membership-tag {
            background: #0f172a;
            border-color: #334155;
            color: #94a3b8;
        }
        body.dark-mode .membership-tag:hover {
            background: #1e3a8a;
            color: #93c5fd;
            border-color: #3b82f6;
        }
        body.dark-mode .btn-verify {
            background: #0f172a;
            color: #e2e8f0;
            border-color: #334155;
        }
        body.dark-mode .btn-verify:hover {
            background: #2563eb;
            color: #ffffff !important;
            border-color: #2563eb;
        }
        body.dark-mode .btn-filter-pill {
            background: #1e293b;
            border-color: #334155;
            color: #cbd5e1;
        }
        body.dark-mode .btn-filter-pill:hover {
            background: #334155;
            color: #93c5fd;
            border-color: #60a5fa;
        }
        body.dark-mode .btn-filter-pill.active {
            background: #2563eb;
            color: #ffffff;
            border-color: #2563eb;
        }
        body.dark-mode .search-input-field {
            background: #1e293b;
            border-color: #334155;
            color: #f8fafc;
        }
        body.dark-mode .search-input-field:focus {
            border-color: #60a5fa;
            box-shadow: 0 0 0 4px rgba(96, 165, 250, 0.2);
        }
        body.dark-mode .search-clear-btn {
            background: #334155;
            color: #cbd5e1;
        }
    </style>
</head>

<body>
    <!-- Navbar Start -->
    <nav class="navbar navbar-expand-lg fixed-top navbar-custom navbar-light sticky">
        <div class="container">
            <a class="navbar-brand font-weight-bold brand-logo-wrap" href="index">
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
            
            <div class="d-flex align-items-center ml-auto d-lg-none">
                <button type="button" class="theme-toggle-btn mr-2" aria-label="Toggle dark mode" title="Toggle theme">
                    <svg class="icon-moon" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
                    <svg class="icon-sun" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
                </button>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
                    <span data-feather="menu" class="fea icon-md"></span>
                </button>
            </div>

            <div class="collapse navbar-collapse navigation" id="navbarCollapse">
                <ul class="navbar-nav navbar-nav-link ml-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="index">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="page-about">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="page-events">Speaking Engagements</a>
                    </li>
                    <li class="nav-item active">
                        <a class="nav-link" href="page-memberships">Memberships</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="page-portfolio">Portfolio</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="page-publications">Publications</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="page-books">Books</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="page-blog">Blog</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="javascript:void(0)" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">More</a>
                        <div class="dropdown-menu rounded m-0" aria-labelledby="navbarDropdown">
                            <a class="dropdown-item" href="page-about">Biography &amp; Profiles</a>
                            <a class="dropdown-item" href="page-memberships">Invited Memberships &amp; Fellowships</a>
                            <a class="dropdown-item" href="page-events">Speaking Engagements</a>
                            <a class="dropdown-item" href="page-books">Authored Books</a>
                            <a class="dropdown-item" href="page-publications">Publications &amp; Research</a>
                            <a class="dropdown-item" href="page-portfolio">Portfolio Projects</a>
                            <a class="dropdown-item" href="page-blog">Blog &amp; Thought Leadership</a>
                            <a class="dropdown-item" href="https://scholar.google.com/citations?hl=en&user=zSt9oRMAAAAJ" target="_blank">Google Scholar Profile <i class="mdi mdi-open-in-new ml-1"></i></a>
                        </div>
                    </li>
                </ul>

                <ul class="top-right text-right list-unstyled list-inline mb-0 mt-2 mt-sm-0 nav-social d-flex align-items-center justify-content-end">
                    <li class="list-inline-item mr-2"><a href="https://scholar.google.com/citations?hl=en&user=zSt9oRMAAAAJ" target="_blank" title="Google Scholar Profile"><i class="mdi mdi-school"></i></a></li>
                    <li class="list-inline-item mr-2"><a href="https://www.linkedin.com/in/harshverma59/" target="_blank"><i class="mdi mdi-linkedin"></i></a></li>
                    <li class="list-inline-item mr-2"><a href="https://github.com/iamharshverma" target="_blank"><i class="mdi mdi-github-face"></i></a></li>
                    <li class="list-inline-item mr-2"><a href="https://twitter.com/harshverma59" target="_blank"><i class="mdi mdi-twitter"></i></a></li>
                    <li class="list-inline-item mr-2"><a href="https://www.instagram.com/aiwithharsh/" target="_blank"><i class="mdi mdi-instagram"></i></a></li>
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

    <!-- Hero Header -->
    <section class="bg-half-170 d-table w-100" style="background: radial-gradient(circle at 15% 25%, rgba(37, 99, 235, 0.28) 0%, transparent 45%), radial-gradient(circle at 85% 75%, rgba(79, 70, 229, 0.22) 0%, transparent 45%), radial-gradient(circle at 50% 10%, rgba(14, 165, 233, 0.18) 0%, transparent 50%), linear-gradient(135deg, #090e1a 0%, #0f172a 50%, #1e1b4b 100%);">
        <div class="container">
            <div class="row mt-5 justify-content-center">
                <div class="col-lg-10 text-center">
                    <div class="pages-heading">
                        <span class="badge badge-pill badge-primary px-3 py-2 text-uppercase mb-3 font-weight-bold" style="letter-spacing: 1.5px; font-size: 12px; background-color: #2563eb;">Invited Credentials &amp; Honors</span>
                        <h1 class="title text-white mb-3 font-weight-bold display-4">Invited Memberships &amp; Fellowships</h1>
                        <p class="para-desc mx-auto text-light mb-0" style="max-width: 780px; font-size: 17px; line-height: 1.7; color: #cbd5e1 !important;">
                            Honored as Fellow, Senior Member, and Council Member across the world's leading scientific honor societies, engineering institutions, and technology advisory councils in Artificial Intelligence, Cloud Architecture, and Cybersecurity.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Main Content Section -->
    <section class="section">
        <div class="container">
            
            <!-- Stats Ribbon -->
            <div class="membership-stats-box">
                <div class="row align-items-center">
                    <div class="col-lg-2 col-md-4 col-6 stat-item">
                        <div class="stat-number">18+</div>
                        <div class="stat-label">Total Appointments</div>
                    </div>
                    <div class="col-lg-2 col-md-4 col-6 stat-item">
                        <div class="stat-number">5</div>
                        <div class="stat-label">Fellowships Awarded</div>
                    </div>
                    <div class="col-lg-3 col-md-4 col-6 stat-item">
                        <div class="stat-number">Top 10%</div>
                        <div class="stat-label">IEEE Senior Grade</div>
                    </div>
                    <div class="col-lg-2 col-md-6 col-6 stat-item">
                        <div class="stat-number">2</div>
                        <div class="stat-label">Honor Societies</div>
                    </div>
                    <div class="col-lg-3 col-md-6 col-12 stat-item">
                        <div class="stat-number">Global</div>
                        <div class="stat-label">Advisory &amp; Mentorship</div>
                    </div>
                </div>
            </div>

            <!-- Search Field -->
            <div class="search-container">
                <i class="mdi mdi-magnify search-icon-inside"></i>
                <input type="text" id="membershipSearchInput" class="search-input-field" placeholder="Search by organization, fellowship, credential ID, role, or topic..." />
                <button type="button" id="clearSearchBtn" class="search-clear-btn" style="display: none;" title="Clear search">
                    <i class="mdi mdi-close"></i>
                </button>
            </div>

            <!-- Category Filter Pills -->
            <div class="filter-nav-wrap" id="filterNavWrap">
                <button class="btn-filter-pill active" data-filter="all">
                    All Memberships <span class="filter-count-badge">18</span>
                </button>
                <button class="btn-filter-pill" data-filter="fellowship">
                    <i class="mdi mdi-medal-outline"></i> Fellowships &amp; Senior <span class="filter-count-badge">5</span>
                </button>
                <button class="btn-filter-pill" data-filter="council">
                    <i class="mdi mdi-shield-account-outline"></i> Advisory &amp; Councils <span class="filter-count-badge">4</span>
                </button>
                <button class="btn-filter-pill" data-filter="scientific">
                    <i class="mdi mdi-atom"></i> Scientific Societies <span class="filter-count-badge">5</span>
                </button>
                <button class="btn-filter-pill" data-filter="mentorship">
                    <i class="mdi mdi-account-group-outline"></i> Experts &amp; Mentorship <span class="filter-count-badge">4</span>
                </button>
            </div>

            <!-- Results Summary Bar -->
            <div class="d-flex justify-content-between align-items-center mb-4 pb-2 border-bottom">
                <span class="text-muted font-weight-bold" id="resultsCountText">Showing all 18 invited memberships and fellowships</span>
                <div class="dropdown">
                    <button class="btn btn-sm btn-outline-secondary dropdown-toggle" type="button" id="sortDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        <i class="mdi mdi-sort-variant mr-1"></i> Sort By
                    </button>
                    <div class="dropdown-menu dropdown-menu-right" aria-labelledby="sortDropdown">
                        <a class="dropdown-item active" href="javascript:void(0)" onclick="sortCards('featured')">Featured First</a>
                        <a class="dropdown-item" href="javascript:void(0)" onclick="sortCards('alpha')">Alphabetical Order</a>
                        <a class="dropdown-item" href="javascript:void(0)" onclick="sortCards('tier')">Tier / Distinction</a>
                    </div>
                </div>
            </div>

            <!-- Memberships Grid -->
            <div class="row" id="membershipsGrid">

                <!-- 1. Forbes Technology Council -->
                <div class="col-lg-4 col-md-6 mb-4 membership-item" data-category="council" data-tier="1" data-search="forbes technology council official council member columnist enterprise ai cybersecurity zero trust advisory">
                    <div class="membership-card">
                        <div class="membership-header-badge">
                            <span class="membership-tier-pill tier-council">Council Member</span>
                            <img src="images/memberships/forbes.svg" alt="Forbes Technology Council Logo">
                        </div>
                        <div class="membership-body">
                            <h3 class="membership-title">Forbes Technology Council</h3>
                            <div class="membership-org"><i class="mdi mdi-check-decagram text-primary mr-1"></i> Official Council Member &amp; Columnist</div>
                            <div class="membership-credential-id"><i class="mdi mdi-certificate mr-1"></i> Forbes Executive Profile Verified</div>
                            <p class="membership-desc">
                                Invitation-only community for world-class CIOs, CTOs, and senior technology leaders. Contributing author publishing peer-reviewed thought leadership on Enterprise AI systems, autonomous agent perimeters, and technology ROI.
                            </p>
                            <div class="membership-tags">
                                <span class="membership-tag">#ForbesCouncil</span>
                                <span class="membership-tag">#EnterpriseAI</span>
                                <span class="membership-tag">#Cybersecurity</span>
                                <span class="membership-tag">#Advisory</span>
                            </div>
                            <div class="membership-footer">
                                <a href="https://www.forbes.com/councils/forbestechcouncil/people/harshverma/" target="_blank" class="btn-verify">
                                    <i class="mdi mdi-open-in-new"></i> View Forbes Profile
                                </a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 2. IEEE Senior Membership -->
                <div class="col-lg-4 col-md-6 mb-4 membership-item" data-category="fellowship" data-tier="1" data-search="ieee senior member institute of electrical and electronics engineers ieee computer society 95132014 engineering distributed systems">
                    <div class="membership-card">
                        <div class="membership-header-badge">
                            <span class="membership-tier-pill tier-senior">Senior Member</span>
                            <img src="images/memberships/ieee_senior.svg" alt="IEEE Senior Member Logo">
                        </div>
                        <div class="membership-body">
                            <h3 class="membership-title">IEEE &amp; IEEE Computer Society</h3>
                            <div class="membership-org"><i class="mdi mdi-check-decagram text-primary mr-1"></i> Senior Member (SMIEEE)</div>
                            <div class="membership-credential-id"><i class="mdi mdi-numeric mr-1"></i> Member ID: 95132014</div>
                            <p class="membership-desc">
                                Senior Member is the highest professional grade of IEEE, achieved by fewer than 10% of IEEE's 400,000+ members worldwide. Honors significant performance, technical leadership, and sustained contributions to AI and distributed computing.
                            </p>
                            <div class="membership-tags">
                                <span class="membership-tag">#SMIEEE</span>
                                <span class="membership-tag">#IEEEComputerSociety</span>
                                <span class="membership-tag">#Top10Percent</span>
                                <span class="membership-tag">#SeniorGrade</span>
                            </div>
                            <div class="membership-footer">
                                <a href="https://www.ieee.org/" target="_blank" class="btn-verify">
                                    <i class="mdi mdi-shield-check"></i> Verify IEEE Senior Status
                                </a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 3. Raptors.Dev Fellowship -->
                <div class="col-lg-4 col-md-6 mb-4 membership-item" data-category="fellowship" data-tier="1" data-search="raptors.dev fellowship fellow membership top engineering leaders ai architecture high scale">
                    <div class="membership-card">
                        <div class="membership-header-badge">
                            <span class="membership-tier-pill tier-fellow">Fellow</span>
                            <img src="images/memberships/raptors_dev.svg" alt="Raptors.Dev Fellowship Logo">
                        </div>
                        <div class="membership-body">
                            <h3 class="membership-title">Raptors.Dev Fellowship</h3>
                            <div class="membership-org"><i class="mdi mdi-medal text-warning mr-1"></i> Fellow Member</div>
                            <div class="membership-credential-id"><i class="mdi mdi-star-circle mr-1"></i> Elite Engineering Fellowship</div>
                            <p class="membership-desc">
                                Elite, invite-only fellowship recognizing top-tier software engineering leaders and AI researchers shaping next-generation software architectures, resilient cloud microservices, and large-scale AI deployment frameworks.
                            </p>
                            <div class="membership-tags">
                                <span class="membership-tag">#Fellowship</span>
                                <span class="membership-tag">#AIArchitecture</span>
                                <span class="membership-tag">#HighScaleSystems</span>
                            </div>
                            <div class="membership-footer">
                                <a href="https://www.raptors.dev/fellow-membership" target="_blank" class="btn-verify">
                                    <i class="mdi mdi-open-in-new"></i> Explore Fellowship
                                </a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 4. UC Berkeley SkyDeck -->
                <div class="col-lg-4 col-md-6 mb-4 membership-item" data-category="council" data-tier="2" data-search="uc berkeley skydeck global advisor startup mentor accelerator deep tech enterprise ai venture">
                    <div class="membership-card">
                        <div class="membership-header-badge">
                            <span class="membership-tier-pill tier-council">Global Advisor</span>
                            <img src="images/memberships/skydeck.svg" alt="UC Berkeley SkyDeck Logo">
                        </div>
                        <div class="membership-body">
                            <h3 class="membership-title">UC Berkeley SkyDeck</h3>
                            <div class="membership-org"><i class="mdi mdi-school text-primary mr-1"></i> Global Advisor &amp; Startup Mentor</div>
                            <div class="membership-credential-id"><i class="mdi mdi-account-tie mr-1"></i> Berkeley SkyDeck Advisor Network</div>
                            <p class="membership-desc">
                                Advising venture-backed startups and deep-tech founders at UC Berkeley's premier startup accelerator. Mentoring on AI product architecture, scalable enterprise systems, and technical defensibility.
                            </p>
                            <div class="membership-tags">
                                <span class="membership-tag">#UCBerkeley</span>
                                <span class="membership-tag">#SkyDeck</span>
                                <span class="membership-tag">#StartupAdvisor</span>
                                <span class="membership-tag">#DeepTech</span>
                            </div>
                            <div class="membership-footer">
                                <a href="https://skydeck.berkeley.edu/advisors/" target="_blank" class="btn-verify">
                                    <i class="mdi mdi-open-in-new"></i> SkyDeck Advisor Directory
                                </a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 5. Sigma Xi -->
                <div class="col-lg-4 col-md-6 mb-4 membership-item" data-category="scientific" data-tier="1" data-search="sigma xi the scientific research honor society full elected member research nobel laureates artificial intelligence">
                    <div class="membership-card">
                        <div class="membership-header-badge">
                            <span class="membership-tier-pill tier-honor">Honor Society</span>
                            <img src="images/memberships/sigmaxi.svg" alt="Sigma Xi Logo">
                        </div>
                        <div class="membership-body">
                            <h3 class="membership-title">Sigma Xi (The Scientific Research Honor Society)</h3>
                            <div class="membership-org"><i class="mdi mdi-atom text-success mr-1"></i> Full Elected Member</div>
                            <div class="membership-credential-id"><i class="mdi mdi-certificate mr-1"></i> Elected by Scientific Peers</div>
                            <p class="membership-desc">
                                Elected member of one of the world's most historic research honor societies (whose historic members include over 200 Nobel laureates), recognizing demonstrated research excellence and impact in AI &amp; computational systems.
                            </p>
                            <div class="membership-tags">
                                <span class="membership-tag">#SigmaXi</span>
                                <span class="membership-tag">#HonorSociety</span>
                                <span class="membership-tag">#ScientificResearch</span>
                                <span class="membership-tag">#AI</span>
                            </div>
                            <div class="membership-footer">
                                <a href="https://www.sigmaxi.org/" target="_blank" class="btn-verify">
                                    <i class="mdi mdi-open-in-new"></i> Sigma Xi Society
                                </a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 6. RSA Fellowship -->
                <div class="col-lg-4 col-md-6 mb-4 membership-item" data-category="fellowship" data-tier="1" data-search="rsa fellowship royal society of arts fellow frsa ethical ai social impact">
                    <div class="membership-card">
                        <div class="membership-header-badge">
                            <span class="membership-tier-pill tier-fellow">Fellow (FRSA)</span>
                            <img src="images/memberships/rsa_fellow.svg" alt="RSA Fellowship Logo">
                        </div>
                        <div class="membership-body">
                            <h3 class="membership-title">Royal Society of Arts (RSA)</h3>
                            <div class="membership-org"><i class="mdi mdi-medal text-warning mr-1"></i> Fellow of the Royal Society of Arts (FRSA)</div>
                            <div class="membership-credential-id"><i class="mdi mdi-crown mr-1"></i> Distinction: FRSA</div>
                            <p class="membership-desc">
                                Awarded the fellowship distinction (FRSA) for demonstrated impact in technology innovation, ethical artificial intelligence governance, and advancing solutions for global technological progression.
                            </p>
                            <div class="membership-tags">
                                <span class="membership-tag">#FRSA</span>
                                <span class="membership-tag">#RoyalSociety</span>
                                <span class="membership-tag">#Fellowship</span>
                                <span class="membership-tag">#EthicalAI</span>
                            </div>
                            <div class="membership-footer">
                                <a href="https://www.thersa.org/" target="_blank" class="btn-verify">
                                    <i class="mdi mdi-open-in-new"></i> Visit The RSA
                                </a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 7. IOASD Royal Fellowship -->
                <div class="col-lg-4 col-md-6 mb-4 membership-item" data-category="fellowship" data-tier="1" data-search="ioasd royal fellowship international organization for academic and scientific development frioasd-1066-2026 academic research">
                    <div class="membership-card">
                        <div class="membership-header-badge">
                            <span class="membership-tier-pill tier-fellow">Royal Fellow</span>
                            <img src="images/memberships/ioasd_fellow.svg" alt="IOASD Royal Fellow Logo">
                        </div>
                        <div class="membership-body">
                            <h3 class="membership-title">IOASD (Scientific &amp; Academic Development)</h3>
                            <div class="membership-org"><i class="mdi mdi-crown text-warning mr-1"></i> Royal Fellowship Awarded</div>
                            <div class="membership-credential-id"><i class="mdi mdi-numeric mr-1"></i> ID: FRIOASD-1066-2026</div>
                            <p class="membership-desc">
                                Awarded the prestigious Royal Fellowship (FRIOASD) by the International Organization for Academic and Scientific Development for distinguished contributions in Artificial Intelligence, Cloud Infrastructure, and Enterprise Security.
                            </p>
                            <div class="membership-tags">
                                <span class="membership-tag">#RoyalFellow</span>
                                <span class="membership-tag">#FRIOASD</span>
                                <span class="membership-tag">#AcademicHonor</span>
                            </div>
                            <div class="membership-footer">
                                <a href="https://ioasd.org/royal-fellows/membership-id-frioasd-1066-2026/" target="_blank" class="btn-verify">
                                    <i class="mdi mdi-shield-check"></i> Verify Royal Fellowship
                                </a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 8. Forttuna Technical Council -->
                <div class="col-lg-4 col-md-6 mb-4 membership-item" data-category="council" data-tier="2" data-search="forttuna technical council council member digital transformation ai ethics healthcare cyber">
                    <div class="membership-card">
                        <div class="membership-header-badge">
                            <span class="membership-tier-pill tier-council">Council Member</span>
                            <img src="images/memberships/forttuna.svg" alt="Forttuna Council Logo">
                        </div>
                        <div class="membership-body">
                            <h3 class="membership-title">Forttuna Technical Council</h3>
                            <div class="membership-org"><i class="mdi mdi-shield-account text-primary mr-1"></i> Council Member</div>
                            <div class="membership-credential-id"><i class="mdi mdi-account-check mr-1"></i> Official Council Appointment</div>
                            <p class="membership-desc">
                                Global executive council uniting industry innovators, enterprise leaders, and cybersecurity pioneers to guide cross-industry AI ethics, digital modernization, and scalable technological infrastructure.
                            </p>
                            <div class="membership-tags">
                                <span class="membership-tag">#ForttunaCouncil</span>
                                <span class="membership-tag">#TechAdvisory</span>
                                <span class="membership-tag">#DigitalStrategy</span>
                            </div>
                            <div class="membership-footer">
                                <a href="https://councils.forttuna.com/council-member/harsh-verma/" target="_blank" class="btn-verify">
                                    <i class="mdi mdi-open-in-new"></i> View Council Profile
                                </a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 9. AAAI Membership -->
                <div class="col-lg-4 col-md-6 mb-4 membership-item" data-category="scientific" data-tier="2" data-search="aaai association for the advancement of artificial intelligence member 656475 machine learning neural networks">
                    <div class="membership-card">
                        <div class="membership-header-badge">
                            <span class="membership-tier-pill tier-honor">AI Society</span>
                            <img src="images/memberships/aaai.svg" alt="AAAI Logo">
                        </div>
                        <div class="membership-body">
                            <h3 class="membership-title">AAAI (Advancement of Artificial Intelligence)</h3>
                            <div class="membership-org"><i class="mdi mdi-brain text-primary mr-1"></i> Active Member</div>
                            <div class="membership-credential-id"><i class="mdi mdi-numeric mr-1"></i> AAAI Member ID: 656475</div>
                            <p class="membership-desc">
                                The premier international scientific body devoted to promoting research in artificial intelligence, neural architectures, autonomous agents, and their responsible deployment across industry and society.
                            </p>
                            <div class="membership-tags">
                                <span class="membership-tag">#AAAI</span>
                                <span class="membership-tag">#AIResearch</span>
                                <span class="membership-tag">#MachineLearning</span>
                            </div>
                            <div class="membership-footer">
                                <a href="https://aaai.org/" target="_blank" class="btn-verify">
                                    <i class="mdi mdi-open-in-new"></i> Visit AAAI
                                </a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 10. AAAS Supporting Membership -->
                <div class="col-lg-4 col-md-6 mb-4 membership-item" data-category="scientific" data-tier="2" data-search="aaas american association for the advancement of science supporting member science journal research">
                    <div class="membership-card">
                        <div class="membership-header-badge">
                            <span class="membership-tier-pill tier-honor">Scientific Society</span>
                            <img src="images/memberships/aaas.svg" alt="AAAS Logo">
                        </div>
                        <div class="membership-body">
                            <h3 class="membership-title">AAAS (Advancement of Science)</h3>
                            <div class="membership-org"><i class="mdi mdi-book-open-page-variant text-danger mr-1"></i> Supporting Member</div>
                            <div class="membership-credential-id"><i class="mdi mdi-certificate mr-1"></i> Publisher of Science Journals</div>
                            <p class="membership-desc">
                                Supporting member of the world's largest multidisciplinary scientific society and publisher of the *Science* family of journals, advancing scientific literacy, computational discovery, and global innovation.
                            </p>
                            <div class="membership-tags">
                                <span class="membership-tag">#AAAS</span>
                                <span class="membership-tag">#Science</span>
                                <span class="membership-tag">#ScientificAdvancement</span>
                            </div>
                            <div class="membership-footer">
                                <a href="https://www.aaas.org/" target="_blank" class="btn-verify">
                                    <i class="mdi mdi-open-in-new"></i> Visit AAAS
                                </a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 11. ACM & ACM SIGAI / SIGSOFT -->
                <div class="col-lg-4 col-md-6 mb-4 membership-item" data-category="scientific" data-tier="2" data-search="acm sigai sigsoft association for computing machinery computer science software engineering">
                    <div class="membership-card">
                        <div class="membership-header-badge">
                            <span class="membership-tier-pill tier-honor">Computing Society</span>
                            <img src="images/memberships/acm_sigai.svg" alt="ACM SIGAI Logo">
                        </div>
                        <div class="membership-body">
                            <h3 class="membership-title">ACM (SIGAI &amp; SIGSOFT)</h3>
                            <div class="membership-org"><i class="mdi mdi-code-braces text-info mr-1"></i> ACM Member · SIGAI · SIGSOFT</div>
                            <div class="membership-credential-id"><i class="mdi mdi-account-card-details mr-1"></i> Active Member Record</div>
                            <p class="membership-desc">
                                Active member of the world's leading educational and scientific computing society, participating in SIGAI (Special Interest Group on Artificial Intelligence) and SIGSOFT (Software Engineering).
                            </p>
                            <div class="membership-tags">
                                <span class="membership-tag">#ACM</span>
                                <span class="membership-tag">#SIGAI</span>
                                <span class="membership-tag">#SIGSOFT</span>
                                <span class="membership-tag">#SoftwareEngineering</span>
                            </div>
                            <div class="membership-footer">
                                <a href="https://myacm.acm.org/dashboard.cfm?svc=services" target="_blank" class="btn-verify">
                                    <i class="mdi mdi-open-in-new"></i> View ACM Portal
                                </a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 12. IFGICT Fellowship -->
                <div class="col-lg-4 col-md-6 mb-4 membership-item" data-category="fellowship" data-tier="1" data-search="ifgict fellowship international federation of global green ict sustainable compute green ai">
                    <div class="membership-card">
                        <div class="membership-header-badge">
                            <span class="membership-tier-pill tier-fellow">Fellow</span>
                            <img src="images/memberships/ifgict.svg" alt="IFGICT Fellowship Logo">
                        </div>
                        <div class="membership-body">
                            <h3 class="membership-title">IFGICT (Global Green ICT)</h3>
                            <div class="membership-org"><i class="mdi mdi-leaf text-success mr-1"></i> Fellow</div>
                            <div class="membership-credential-id"><i class="mdi mdi-earth mr-1"></i> Sustainable ICT Distinction</div>
                            <p class="membership-desc">
                                Awarded fellowship by the International Federation of Global Green ICT for contributions to energy-efficient AI architectures, sustainable compute paradigms, and enterprise technology standards.
                            </p>
                            <div class="membership-tags">
                                <span class="membership-tag">#IFGICT</span>
                                <span class="membership-tag">#GreenAI</span>
                                <span class="membership-tag">#SustainableICT</span>
                                <span class="membership-tag">#Fellowship</span>
                            </div>
                            <div class="membership-footer">
                                <a href="https://timebusinessnews.com/harsh-verma-ifgict/" target="_blank" class="btn-verify">
                                    <i class="mdi mdi-newspaper"></i> Read Fellowship Announcement
                                </a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 13. Google Developer Expert (GDE) -->
                <div class="col-lg-4 col-md-6 mb-4 membership-item" data-category="mentorship" data-tier="1" data-search="google developer expert gde ai cloud google recognized tech speaker mentorship">
                    <div class="membership-card">
                        <div class="membership-header-badge">
                            <span class="membership-tier-pill tier-mentor">Google Expert</span>
                            <img src="images/memberships/gde.svg" alt="Google Developer Expert Logo">
                        </div>
                        <div class="membership-body">
                            <h3 class="membership-title">Google Developer Expert</h3>
                            <div class="membership-org"><i class="mdi mdi-google text-primary mr-1"></i> GDE in AI &amp; Cloud</div>
                            <div class="membership-credential-id"><i class="mdi mdi-account-star mr-1"></i> Google Recognized Leader</div>
                            <p class="membership-desc">
                                Recognized by Google as a global subject matter expert and community leader in AI and Google Cloud, speaking at premier tech events and guiding engineering communities worldwide.
                            </p>
                            <div class="membership-tags">
                                <span class="membership-tag">#GoogleDeveloperExpert</span>
                                <span class="membership-tag">#GDE</span>
                                <span class="membership-tag">#GoogleCloud</span>
                                <span class="membership-tag">#AICommunity</span>
                            </div>
                            <div class="membership-footer">
                                <a href="https://developers.google.com/community/experts/directory?text=Harsh%20Verma" target="_blank" class="btn-verify">
                                    <i class="mdi mdi-open-in-new"></i> Google GDE Directory
                                </a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 14. RSAC (RSA Conference) Community -->
                <div class="col-lg-4 col-md-6 mb-4 membership-item" data-category="council" data-tier="2" data-search="rsac rsa conference invite-only cybersecurity library expert speaker threat intelligence">
                    <div class="membership-card">
                        <div class="membership-header-badge">
                            <span class="membership-tier-pill tier-council">Invite-Only</span>
                            <img src="images/memberships/rsac.svg" alt="RSAC Community Logo">
                        </div>
                        <div class="membership-body">
                            <h3 class="membership-title">RSA Conference (RSAC)</h3>
                            <div class="membership-org"><i class="mdi mdi-shield-lock text-danger mr-1"></i> Invite-Only Expert Member</div>
                            <div class="membership-credential-id"><i class="mdi mdi-library mr-1"></i> RSAC Expert Library Contributor</div>
                            <p class="membership-desc">
                                Selected member of RSA Conference's curated cybersecurity library network, publishing research on autonomous AI agent threat models, zero-trust architectures, and "Clean Attack" forensics.
                            </p>
                            <div class="membership-tags">
                                <span class="membership-tag">#RSAC</span>
                                <span class="membership-tag">#Cybersecurity</span>
                                <span class="membership-tag">#ThreatIntelligence</span>
                                <span class="membership-tag">#ZeroTrust</span>
                            </div>
                            <div class="membership-footer">
                                <a href="https://portal.onersac.com/library/discover" target="_blank" class="btn-verify">
                                    <i class="mdi mdi-open-in-new"></i> RSAC Discover Portal
                                </a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 15. ADPList Mentorship -->
                <div class="col-lg-4 col-md-6 mb-4 membership-item" data-category="mentorship" data-tier="2" data-search="adplist amazing design people list top mentor ai career leadership coaching 1-on-1">
                    <div class="membership-card">
                        <div class="membership-header-badge">
                            <span class="membership-tier-pill tier-mentor">Top Mentor</span>
                            <img src="images/memberships/adplist.svg" alt="ADPList Logo">
                        </div>
                        <div class="membership-body">
                            <h3 class="membership-title">ADPList Mentorship Community</h3>
                            <div class="membership-org"><i class="mdi mdi-account-group text-danger mr-1"></i> Top Mentor (AI &amp; Tech Leadership)</div>
                            <div class="membership-credential-id"><i class="mdi mdi-star text-warning mr-1"></i> Verified Global Mentor</div>
                            <p class="membership-desc">
                                Top-rated global mentor on ADPList, providing 1-on-1 mentoring, AI architecture reviews, and engineering leadership guidance to practitioners and engineering leaders across 30+ countries.
                            </p>
                            <div class="membership-tags">
                                <span class="membership-tag">#ADPList</span>
                                <span class="membership-tag">#Mentorship</span>
                                <span class="membership-tag">#CareerCoaching</span>
                                <span class="membership-tag">#TechLeaders</span>
                            </div>
                            <div class="membership-footer">
                                <a href="https://adplist.org/mentors/harsh-verma" target="_blank" class="btn-verify">
                                    <i class="mdi mdi-calendar-check"></i> View ADPList Profile
                                </a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 16. Dent Capital Expert List -->
                <div class="col-lg-4 col-md-6 mb-4 membership-item" data-category="council" data-tier="2" data-search="dent capital expert list mentor advisor venture deep tech startup strategy">
                    <div class="membership-card">
                        <div class="membership-header-badge">
                            <span class="membership-tier-pill tier-council">Expert Advisor</span>
                            <img src="images/memberships/dent_capital.svg" alt="Dent Capital Logo">
                        </div>
                        <div class="membership-body">
                            <h3 class="membership-title">Dent Capital Expert List</h3>
                            <div class="membership-org"><i class="mdi mdi-chart-line text-primary mr-1"></i> Mentor &amp; Technical Advisor</div>
                            <div class="membership-credential-id"><i class="mdi mdi-briefcase mr-1"></i> Venture &amp; Tech Network</div>
                            <p class="membership-desc">
                                Serving on the Dent Capital Expert List, advising emerging venture capital funds, incubators, and enterprise founders on cutting-edge AI product strategies and technical roadmaps.
                            </p>
                            <div class="membership-tags">
                                <span class="membership-tag">#DentCapital</span>
                                <span class="membership-tag">#VentureAdvisory</span>
                                <span class="membership-tag">#AIStrategy</span>
                            </div>
                            <div class="membership-footer">
                                <a href="https://councils.forttuna.com/council-member/harsh-verma/" target="_blank" class="btn-verify">
                                    <i class="mdi mdi-open-in-new"></i> Learn More
                                </a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 17. HackUTD & Hackmakers -->
                <div class="col-lg-4 col-md-6 mb-4 membership-item" data-category="mentorship" data-tier="3" data-search="hackutd hackmakers odsc siim hackathon judge mentor collegiate competitions imaging">
                    <div class="membership-card">
                        <div class="membership-header-badge" style="background: linear-gradient(135deg, #1e1b4b 0%, #312e81 100%);">
                            <span class="membership-tier-pill tier-mentor">Judge &amp; Mentor</span>
                            <img src="images/communities/hackutd.png" alt="HackUTD & Community Logo" style="max-height: 80px;">
                        </div>
                        <div class="membership-body">
                            <h3 class="membership-title">HackUTD &amp; Hackmakers</h3>
                            <div class="membership-org"><i class="mdi mdi-gavel text-warning mr-1"></i> AI Challenge Judge &amp; Mentor</div>
                            <div class="membership-credential-id"><i class="mdi mdi-trophy mr-1"></i> Texas &amp; Global Hackathons</div>
                            <p class="membership-desc">
                                Serving as technical judge and AI mentor at major hackathons including HackUTD (Texas's largest collegiate hackathon) and Hackmakers international challenges, evaluating multi-agent and data engineering projects.
                            </p>
                            <div class="membership-tags">
                                <span class="membership-tag">#HackUTD</span>
                                <span class="membership-tag">#Hackmakers</span>
                                <span class="membership-tag">#HackathonJudge</span>
                                <span class="membership-tag">#Mentor</span>
                            </div>
                            <div class="membership-footer">
                                <a href="https://hackutd.co/" target="_blank" class="btn-verify">
                                    <i class="mdi mdi-open-in-new"></i> Visit HackUTD
                                </a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 18. ODSC & SIIM Communities -->
                <div class="col-lg-4 col-md-6 mb-4 membership-item" data-category="mentorship" data-tier="3" data-search="odsc siim open data science conference society for imaging informatics in medicine speaker researcher">
                    <div class="membership-card">
                        <div class="membership-header-badge" style="background: linear-gradient(135deg, #0c4a6e 0%, #0369a1 100%);">
                            <span class="membership-tier-pill tier-honor">Community</span>
                            <img src="images/communities/odsc_logo.png" alt="ODSC & SIIM Logo" style="max-height: 75px; background: rgba(255,255,255,0.9); padding: 6px 12px; border-radius: 10px;">
                        </div>
                        <div class="membership-body">
                            <h3 class="membership-title">ODSC &amp; SIIM Communities</h3>
                            <div class="membership-org"><i class="mdi mdi-account-multiple text-info mr-1"></i> Speaker &amp; Member</div>
                            <div class="membership-credential-id"><i class="mdi mdi-presentation mr-1"></i> Open Data Science &amp; Imaging</div>
                            <p class="membership-desc">
                                Active contributor and speaker across Open Data Science Conference (ODSC) and the Society for Imaging Informatics in Medicine (SIIM), presenting on machine learning pipelines and multimodal healthcare imaging.
                            </p>
                            <div class="membership-tags">
                                <span class="membership-tag">#ODSC</span>
                                <span class="membership-tag">#SIIM</span>
                                <span class="membership-tag">#DataScience</span>
                                <span class="membership-tag">#ImagingAI</span>
                            </div>
                            <div class="membership-footer">
                                <a href="https://odsc.com/" target="_blank" class="btn-verify">
                                    <i class="mdi mdi-open-in-new"></i> Visit ODSC
                                </a>
                            </div>
                        </div>
                    </div>
                </div>

            </div><!-- end row -->

            <!-- No Results State -->
            <div id="noResultsState" class="text-center py-5" style="display: none;">
                <div class="mb-3">
                    <i class="mdi mdi-file-search-outline text-muted" style="font-size: 64px;"></i>
                </div>
                <h4 class="font-weight-bold mb-2">No Memberships Found</h4>
                <p class="text-muted mb-4">No invited appointments match your search criteria. Try a different keyword or reset filters.</p>
                <button type="button" class="btn btn-primary" onclick="resetFilters()">Reset All Filters</button>
            </div>

            <!-- Call to Action Banner -->
            <div class="mt-5 pt-4 text-center">
                <div class="p-5 rounded-lg text-center" style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); color: #ffffff; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
                    <h3 class="font-weight-bold mb-3 text-white">Advisory, Committee Review &amp; Keynotes</h3>
                    <p class="text-light-muted mx-auto mb-4" style="max-width: 650px; color: #cbd5e1 !important; font-size: 16px;">
                        Interested in inviting Harsh Verma for fellowship committees, conference program review, advisory boards, or institutional panel speaking?
                    </p>
                    <div class="d-flex justify-content-center flex-wrap gap-3" style="gap: 12px;">
                        <a href="index#contact" class="btn btn-primary px-4 py-2" style="font-weight: 600; border-radius: 8px;">
                            <i class="mdi mdi-email mr-1"></i> Get in Touch
                        </a>
                        <a href="https://www.linkedin.com/in/harshverma59/" target="_blank" class="btn btn-outline-light px-4 py-2" style="font-weight: 600; border-radius: 8px;">
                            <i class="mdi mdi-linkedin mr-1"></i> Connect on LinkedIn
                        </a>
                    </div>
                </div>
            </div>

        </div><!-- end container -->
    </section>

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

    <!-- javascript -->
    <script src="js/jquery.min.js"></script>
    <script src="js/bootstrap.bundle.min.js"></script>
    <script src="js/feather.min.js"></script>
    <script src="js/app.js"></script>
    
    <script>
    // Filtering and Search Logic
    let currentFilter = 'all';
    const searchInput = document.getElementById('membershipSearchInput');
    const clearBtn = document.getElementById('clearSearchBtn');
    const filterPills = document.querySelectorAll('.btn-filter-pill');
    const items = document.querySelectorAll('.membership-item');
    const noResultsState = document.getElementById('noResultsState');
    const resultsCountText = document.getElementById('resultsCountText');

    function applyFilters() {
        const query = searchInput ? searchInput.value.toLowerCase().trim() : '';
        let visibleCount = 0;

        if (clearBtn) {
            clearBtn.style.display = query.length > 0 ? 'flex' : 'none';
        }

        items.forEach(item => {
            const category = item.getAttribute('data-category');
            const searchData = (item.getAttribute('data-search') || '').toLowerCase();
            const textContent = item.innerText.toLowerCase();
            
            const matchesCategory = (currentFilter === 'all' || category === currentFilter);
            const matchesSearch = query === '' || searchData.includes(query) || textContent.includes(query);

            if (matchesCategory && matchesSearch) {
                item.style.display = 'block';
                visibleCount++;
            } else {
                item.style.display = 'none';
            }
        });

        if (visibleCount === 0) {
            if (noResultsState) noResultsState.style.display = 'block';
        } else {
            if (noResultsState) noResultsState.style.display = 'none';
        }

        if (resultsCountText) {
            if (query) {
                resultsCountText.innerText = `Found ${visibleCount} appointment${visibleCount === 1 ? '' : 's'} matching "${query}"`;
            } else if (currentFilter !== 'all') {
                resultsCountText.innerText = `Showing ${visibleCount} appointment${visibleCount === 1 ? '' : 's'} in selected category`;
            } else {
                resultsCountText.innerText = `Showing all 18 invited memberships and fellowships`;
            }
        }
    }

    if (searchInput) {
        searchInput.addEventListener('input', applyFilters);
    }

    if (clearBtn) {
        clearBtn.addEventListener('click', function() {
            searchInput.value = '';
            applyFilters();
            searchInput.focus();
        });
    }

    filterPills.forEach(pill => {
        pill.addEventListener('click', function() {
            filterPills.forEach(p => p.classList.remove('active'));
            this.classList.add('active');
            currentFilter = this.getAttribute('data-filter');
            applyFilters();
        });
    });

    function resetFilters() {
        if (searchInput) searchInput.value = '';
        filterPills.forEach(p => p.classList.remove('active'));
        const allPill = document.querySelector('.btn-filter-pill[data-filter="all"]');
        if (allPill) allPill.classList.add('active');
        currentFilter = 'all';
        applyFilters();
    }

    function sortCards(type) {
        const grid = document.getElementById('membershipsGrid');
        const cards = Array.from(grid.querySelectorAll('.membership-item'));

        cards.sort((a, b) => {
            if (type === 'alpha') {
                const titleA = a.querySelector('.membership-title').innerText.trim().toLowerCase();
                const titleB = b.querySelector('.membership-title').innerText.trim().toLowerCase();
                return titleA.localeCompare(titleB);
            } else if (type === 'tier') {
                const tierA = parseInt(a.getAttribute('data-tier') || '99');
                const tierB = parseInt(b.getAttribute('data-tier') || '99');
                return tierA - tierB;
            } else {
                // Default order
                return 0;
            }
        });

        cards.forEach(card => grid.appendChild(card));
        applyFilters();
    }

    // Tag click filtering
    document.querySelectorAll('.membership-tag').forEach(tag => {
        tag.addEventListener('click', function(e) {
            e.stopPropagation();
            const tagText = this.innerText.replace('#', '').trim();
            if (searchInput) {
                searchInput.value = tagText;
                resetFilterPillToAll();
                applyFilters();
                searchInput.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
        });
    });

    function resetFilterPillToAll() {
        filterPills.forEach(p => p.classList.remove('active'));
        const allPill = document.querySelector('.btn-filter-pill[data-filter="all"]');
        if (allPill) allPill.classList.add('active');
        currentFilter = 'all';
    }
    </script>
</body>
</html>
'''

with open('page-memberships.html', 'w', encoding='utf-8') as f:
    f.write(html_content.strip())

print("Created page-memberships.html successfully!")
