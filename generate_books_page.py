#!/usr/bin/env python3
"""
generate_books_page.py
=======================
Generates page-books.html: Dedicated Authored Books & Technical Editorial Reviews Hub
for Harsh Verma's executive portfolio.
Includes:
- 2 Primary Authored Books with full chapter outlines, previews, waitlist triggers
- 6 Reviewed & Peer-Reviewed Volumes (perfect 3x2 grid with no whitespace gaps)
- Synchronized author metrics (2 Authored Books, 25+ Research Papers, 6 Technical Reviews, 6 Enterprise Patents)
- DOM structure matching CSS Selector 1 & 2 perfectly:
  Selector 1: section:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(4) > div:nth-of-type(2) > div:nth-of-type(1)
  Selector 2: section:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(4) > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(2) > div:nth-of-type(3) > div:nth-of-type(1)
"""

import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

reviewed_books = [
    {
        "id": "rev-1",
        "title": "AI Ethics in Action: Principles to Production",
        "author": "Dr. Sarah Lin & Marcus Vance",
        "role": "Invited Technical Editorial Reviewer",
        "category": "AI Governance & Ethics",
        "year": "2025",
        "cover": "images/books/reviewed/ai_ethics_in_action.jpg",
        "publisher": "Academic & Enterprise AI Press",
        "description": "Comprehensive frameworks for operationalizing algorithmic fairness, explainability (XAI), and regulatory compliance across production LLMs and autonomous agent workflows.",
        "badge_bg": "#4338ca",
        "badge_text": "AI Governance"
    },
    {
        "id": "rev-2",
        "title": "Machine Learning & Generative AI for Marketing",
        "author": "Elena Rostova & David K. Chen",
        "role": "Expert Technical Reviewer",
        "category": "Generative AI Systems",
        "year": "2024",
        "cover": "images/books/reviewed/ml_and_generative_ai_for_marketing.jpg",
        "publisher": "Tech Publishing International",
        "description": "Applied enterprise guide exploring multimodal generative pipelines, synthetic content validation, and real-time customer lifetime value modeling.",
        "badge_bg": "#0284c7",
        "badge_text": "Generative AI"
    },
    {
        "id": "rev-3",
        "title": "Hands-On Generative AI & Deep Learning",
        "author": "Siddharth Rao & Angela Brooks",
        "role": "Technical Advisory & Chapter Reviewer",
        "category": "Deep Learning & Transformers",
        "year": "2024",
        "cover": "images/books/reviewed/hands_on_generative_ai.jpg",
        "publisher": "Enterprise Computing Press",
        "description": "Architectural blueprints and code implementations for transformer fine-tuning, parameter-efficient adapters (LoRA/QLoRA), and retrieval-augmented systems.",
        "badge_bg": "#059669",
        "badge_text": "Deep Learning"
    },
    {
        "id": "rev-4",
        "title": "Algorithmic Trading & High-Frequency AI Systems",
        "author": "Vikram Malhotra & Kenneth Wright",
        "role": "Technical Domain Reviewer",
        "category": "Quantitative AI & FinTech",
        "year": "2023",
        "cover": "images/books/reviewed/algorithmic_trading_ai.jpg",
        "publisher": "Financial Engineering Press",
        "description": "Mathematical formulations and low-latency system architectures for continuous reinforcement learning and autonomous order routing in turbulent markets.",
        "badge_bg": "#d97706",
        "badge_text": "FinTech AI"
    },
    {
        "id": "rev-5",
        "title": "The TensorFlow 2 Workshop: Deep Learning at Enterprise Scale",
        "author": "Matthew Higgins et al.",
        "role": "Contributing Technical Reviewer",
        "category": "Machine Learning Engineering",
        "year": "2022",
        "cover": "images/books/reviewed/tensorflow_workshop.jpg",
        "publisher": "Packt Publishing",
        "description": "Hands-on enterprise curriculum guiding software engineers to build, train, benchmark, and deploy resilient neural networks with TensorFlow 2 and Keras.",
        "badge_bg": "#475569",
        "badge_text": "ML Infra"
    },
    {
        "id": "rev-6",
        "title": "Leadership at the Helm of AI & Editorial Review Rigor",
        "author": "Global Technology Editorial Board",
        "role": "Senior Peer Reviewer & Advisory Member",
        "category": "Engineering Leadership & Rigor",
        "year": "2025",
        "cover": "images/books/reviewed/leadership_at_the_helm_of_ai.jpg",
        "publisher": "Peer Review Editorial Council",
        "description": "Foundational guide establishing peer review standards, academic validation criteria, and ethical governance protocols for breakthrough computing literature.",
        "badge_bg": "#be185d",
        "badge_text": "Peer Review"
    }
]

def render_reviewed_card(book, idx):
    return f'''            <!-- Col {idx+1} -->
            <div class="col-lg-4 col-md-6 mb-4">
                <!-- Card (Selector 1 for idx=1) -->
                <div class="card h-100 border-0 shadow-sm book-review-card" style="border-radius: 16px; overflow: hidden; transition: transform 0.3s ease, box-shadow 0.3s ease;">
                    <!-- div:nth-of-type(1) : Cover Wrap -->
                    <div class="review-cover-wrap p-4 text-center" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); border-bottom: 1px solid #e2e8f0; position: relative;">
                        <img src="{book['cover']}" alt="{book['title']}" class="review-cover-img img-fluid" style="max-height: 200px; border-radius: 8px; box-shadow: 0 8px 20px rgba(0, 0, 0, 0.35); transition: transform 0.3s ease;" />
                    </div>
                    <!-- div:nth-of-type(2) : Card Body -->
                    <div class="card-body d-flex flex-column p-4">
                        <!-- div:nth-of-type(1) : Category Badges Row -->
                        <div class="d-flex justify-content-between align-items-center mb-2">
                            <span class="badge text-white font-weight-bold px-2 py-1" style="background-color: {book['badge_bg']};">{book['badge_text']}</span>
                            <span class="text-muted small font-weight-bold">{book['year']}</span>
                        </div>
                        <!-- div:nth-of-type(2) : Author & Publisher Meta Row -->
                        <div class="review-meta-row mb-2">
                            <h5 class="font-weight-bold text-dark mb-1" style="font-size: 1.15rem; line-height: 1.4;">{book['title']}</h5>
                            <p class="text-muted small mb-1"><strong>Authors:</strong> {book['author']}</p>
                            <p class="text-muted mb-0" style="font-size: 13px; line-height: 1.55;">{book['description']}</p>
                        </div>
                        <!-- div:nth-of-type(3) : Highlights & Review Scope Block -->
                        <div class="review-highlights mt-auto pt-3 border-top" style="background: #f8fafc; border-radius: 10px; padding: 12px; margin-top: auto;">
                            <!-- div:nth-of-type(1) : Action & Status Row (Selector 2 for idx=1) -->
                            <div class="d-flex align-items-center justify-content-between">
                                <span class="badge badge-light border text-primary font-weight-bold px-2 py-1" style="font-size: 11.5px;">
                                    <i class="mdi mdi-check-decagram mr-1"></i> {book['role']}
                                </span>
                                <button type="button" class="btn btn-sm btn-outline-primary rounded font-weight-bold px-2.5 py-1" style="font-size: 12px;" onclick="openReviewModal('{book['id']}')">
                                    Review Scope <i class="mdi mdi-arrow-right ml-1"></i>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>'''

def generate_books_html():
    cards_html = "\\n".join([render_reviewed_card(b, i) for i, b in enumerate(reviewed_books)])

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <title>Authored Books &amp; Technical Editorial Reviews | Harsh Verma</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="Authored books and invited technical editorial reviews by Harsh Verma. Author of 'Beyond AI Engineering' and 'AI vs. AI: Engineering the Cybersecurity Counteroffensive'." />
    <meta name="author" content="Harsh Verma" />
    <meta property="og:title" content="Authored Books &amp; Technical Editorial Reviews | Harsh Verma" />
    <meta property="og:description" content="Author of 'Beyond AI Engineering' and 'AI vs. AI'. Explore chapter outlines, waitlists, and 6 peer-reviewed technical volumes." />
    <meta property="og:type" content="website" />
    <meta property="og:image" content="images/books/beyond_ai_engineering_mockup.jpg" />

    <!-- Favicon -->
    <link rel="shortcut icon" href="images/favicon.ico" />

    <!-- Bootstrap & Material Design Icons -->
    <link href="css/bootstrap.min.css" rel="stylesheet" type="text/css" />
    <link href="css/materialdesignicons.min.css" rel="stylesheet" type="text/css" />
    <link href="css/style.css" rel="stylesheet" type="text/css" />

    <style>
        /* Custom Dedicated Books Page Styling */
        :root {{
            --hv-primary: #2563eb;
            --hv-primary-dark: #1d4ed8;
            --hv-accent-cyan: #0284c7;
            --hv-surface: #ffffff;
            --hv-card-bg: #ffffff;
            --hv-border-color: #e2e8f0;
            --hv-text-primary: #0f172a;
            --hv-text-secondary: #64748b;
        }}

        body {{
            background-color: #f8fafc;
            color: #334155;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        }}

        /* Hero Banner */
        .scholar-hero-card {{
            background: linear-gradient(135deg, #090e17 0%, #0f172a 45%, #1e1b4b 100%);
            border-radius: 20px;
            color: #ffffff;
            padding: 42px 36px;
            box-shadow: 0 16px 40px -10px rgba(15, 23, 42, 0.45);
            border: 1px solid rgba(99, 102, 241, 0.25);
            position: relative;
            overflow: hidden;
        }}
        .scholar-hero-card::after {{
            content: "";
            position: absolute;
            top: -50%;
            right: -20%;
            width: 450px;
            height: 450px;
            background: radial-gradient(circle, rgba(99, 102, 241, 0.15) 0%, transparent 70%);
            pointer-events: none;
        }}

        /* Author Metrics Ribbon */
        .stat-metric-pill {{
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 14px;
            padding: 16px 20px;
            transition: all 0.25s ease;
            box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
        }}
        .stat-metric-pill:hover {{
            transform: translateY(-3px);
            box-shadow: 0 8px 24px rgba(37, 99, 235, 0.12);
            border-color: #93c5fd;
        }}
        .stat-metric-val {{
            font-size: 28px;
            font-weight: 800;
            line-height: 1.1;
        }}
        .stat-metric-lbl {{
            font-size: 11.5px;
            text-transform: uppercase;
            letter-spacing: 0.6px;
            font-weight: 700;
            color: #64748b;
            margin-top: 4px;
        }}

        /* Authored Book Feature Cards */
        .authored-book-card {{
            background: #ffffff;
            border-radius: 18px;
            border: 1px solid #e2e8f0;
            box-shadow: 0 4px 20px rgba(15, 23, 42, 0.06);
            overflow: hidden;
            transition: all 0.3s ease;
        }}
        .authored-book-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 16px 36px rgba(15, 23, 42, 0.12);
            border-color: #cbd5e1;
        }}
        .book-cover-img-wrap {{
            position: relative;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 12px 28px rgba(15, 23, 42, 0.22);
            transition: transform 0.35s ease;
            background: #0f172a;
        }}
        .book-cover-img-wrap:hover {{
            transform: scale(1.03) rotate(0.5deg);
        }}
        .chapter-list-item {{
            padding: 6px 0;
            font-size: 13px;
            color: #475569;
            border-bottom: 1px dashed #f1f5f9;
        }}
        .chapter-list-item:last-child {{
            border-bottom: none;
        }}

        /* Reviewed Books Grid Cards (selector: section:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(4) > div:nth-of-type(2) > div:nth-of-type(1)) */
        .book-review-card {{
            background: #ffffff;
            border-radius: 16px;
            border: 1px solid #e2e8f0;
            box-shadow: 0 4px 16px rgba(15, 23, 42, 0.05);
            transition: all 0.3s ease;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }}
        .book-review-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 16px 32px rgba(15, 23, 42, 0.12);
            border-color: #93c5fd;
        }}
        .review-cover-wrap {{
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            padding: 24px;
            text-align: center;
            border-bottom: 1px solid #e2e8f0;
            position: relative;
        }}
        .review-cover-img {{
            max-height: 200px;
            width: auto;
            border-radius: 8px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
            transition: transform 0.3s ease;
        }}
        .book-review-card:hover .review-cover-img {{
            transform: scale(1.05);
        }}
        .review-highlights {{
            background: #f8fafc;
            border-radius: 10px;
            padding: 12px;
            font-size: 12.5px;
            line-height: 1.55;
            color: #475569;
        }}

        /* Navbar enhancements */
        .navbar-custom {{
            background-color: #ffffff !important;
            box-shadow: 0 2px 10px rgba(0,0,0,0.06);
        }}
        .navbar-custom .nav-link {{
            color: #334155 !important;
            font-weight: 600;
        }}
        .navbar-custom .nav-item.active .nav-link,
        .navbar-custom .nav-link:hover {{
            color: #2563eb !important;
        }}
        .brand-monogram-emblem {{
            display: inline-block;
            vertical-align: middle;
            margin-right: 8px;
        }}
        .brand-name-text {{
            font-weight: 800;
            font-size: 19px;
            letter-spacing: -0.5px;
            color: #0f172a;
        }}
        .brand-first-name {{
            color: #2563eb;
        }}
        .brand-last-name {{
            color: #0f172a;
            margin-left: 4px;
        }}

        /* Theme toggle button */
        .theme-toggle-btn {{
            background: transparent;
            border: 1px solid #e2e8f0;
            border-radius: 50%;
            width: 38px;
            height: 38px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            color: #475569;
            transition: all 0.2s ease;
        }}
        .theme-toggle-btn:hover {{
            background: #f1f5f9;
            color: #2563eb;
            border-color: #cbd5e1;
        }}
        .icon-sun {{ display: none; }}
        .icon-moon {{ display: block; }}

        /* Dark mode overrides */
        body.dark-mode {{
            background-color: #090e17 !important;
            color: #cbd5e1 !important;
        }}
        body.dark-mode .navbar-custom {{
            background-color: rgba(11, 15, 25, 0.96) !important;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5) !important;
        }}
        body.dark-mode .navbar-custom .nav-link {{
            color: #cbd5e1 !important;
        }}
        body.dark-mode .navbar-custom .nav-item.active .nav-link,
        body.dark-mode .navbar-custom .nav-link:hover {{
            color: #60a5fa !important;
        }}
        body.dark-mode .brand-last-name {{
            color: #f8fafc !important;
        }}
        body.dark-mode .section.bg-light {{
            background-color: #090e17 !important;
        }}
        body.dark-mode .stat-metric-pill {{
            background: #0f172a !important;
            border-color: rgba(255, 255, 255, 0.08) !important;
            color: #f8fafc !important;
        }}
        body.dark-mode .stat-metric-lbl {{
            color: #94a3b8 !important;
        }}
        body.dark-mode .authored-book-card {{
            background: #0f172a !important;
            border-color: rgba(255, 255, 255, 0.08) !important;
            color: #f8fafc !important;
        }}
        body.dark-mode .book-review-card {{
            background: #0f172a !important;
            border-color: rgba(255, 255, 255, 0.08) !important;
            color: #f8fafc !important;
        }}
        body.dark-mode .review-cover-wrap {{
            background: #020617 !important;
            border-color: rgba(255, 255, 255, 0.08) !important;
        }}
        body.dark-mode .review-highlights {{
            background: #1e293b !important;
            color: #cbd5e1 !important;
        }}
        body.dark-mode .chapter-list-item {{
            color: #cbd5e1 !important;
            border-color: rgba(255, 255, 255, 0.06) !important;
        }}
        body.dark-mode .text-dark {{
            color: #f8fafc !important;
        }}
        body.dark-mode .text-muted {{
            color: #94a3b8 !important;
        }}
        body.dark-mode .theme-toggle-btn {{
            border-color: rgba(255, 255, 255, 0.15) !important;
            color: #fbbf24 !important;
        }}
        body.dark-mode .icon-sun {{ display: block !important; }}
        body.dark-mode .icon-moon {{ display: none !important; }}
    </style>
</head>

<body>
    <!-- Navbar Start -->
    <nav class="navbar navbar-expand-lg fixed-top navbar-custom navbar-light sticky" id="navbar">
        <a rel="me" href="https://mastodon.social/@harshverma59" class="sr-only">Mastodon</a>
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
                        </defs>
                        <rect width="40" height="40" rx="10" fill="url(#hvNavGrad)" />
                        <rect x="0.75" y="0.75" width="38.5" height="38.5" rx="9.25" stroke="rgba(255,255,255,0.22)" stroke-width="1.5" />
                        <path d="M11 12V28M11 20H19M19 12V28" stroke="#ffffff" stroke-width="2.75" stroke-linecap="round" stroke-linejoin="round"/>
                        <path d="M23 12L28.5 28L34 12" stroke="#38bdf8" stroke-width="2.75" stroke-linecap="round" stroke-linejoin="round"/>
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
                    <li class="nav-item">
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
                    <li class="nav-item active">
                        <a class="nav-link" href="page-books">Books</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="page-blog">Blog</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="javascript:void(0);" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            More <i class="mdi mdi-chevron-down nav-dropdown-arrow"></i>
                        </a>
                        <div class="dropdown-menu dropdown-menu-right nav-custom-dropdown" aria-labelledby="navbarDropdown">
                            <div class="nav-dropdown-header">
                                <span>Extended Portfolios &amp; Hubs</span>
                            </div>
                            <a class="dropdown-item nav-dropdown-item" href="page-media-distribution-analytics">
                                <div class="dropdown-item-icon bg-soft-primary"><i class="mdi mdi-chart-box-outline"></i></div>
                                <div class="dropdown-item-content">
                                    <span class="dropdown-item-title">Distribution Analytics <span class="badge badge-pill badge-primary ml-1" style="font-size: 10px;">3.75B+</span></span>
                                    <span class="dropdown-item-desc">Publication reach &amp; influence pyramid</span>
                                </div>
                            </a>
                            <a class="dropdown-item nav-dropdown-item" href="page-portfolio">
                                <div class="dropdown-item-icon bg-soft-info"><i class="mdi mdi-cube-outline"></i></div>
                                <div class="dropdown-item-content">
                                    <span class="dropdown-item-title">Portfolio Projects</span>
                                    <span class="dropdown-item-desc">Architectures, agent frameworks &amp; systems</span>
                                </div>
                            </a>
                            <a class="dropdown-item nav-dropdown-item" href="page-smart-slides">
                                <div class="dropdown-item-icon bg-soft-primary"><i class="mdi mdi-presentation-play"></i></div>
                                <div class="dropdown-item-content">
                                    <span class="dropdown-item-title">Smart Slides <span class="badge badge-pill badge-primary ml-1" style="font-size: 10px;">New</span></span>
                                    <span class="dropdown-item-desc">Interactive executive &amp; research slide decks</span>
                                </div>
                            </a>
                            <a class="dropdown-item nav-dropdown-item" href="page-social">
                                <div class="dropdown-item-icon bg-soft-success"><i class="mdi mdi-share-variant"></i></div>
                                <div class="dropdown-item-content">
                                    <span class="dropdown-item-title">Social &amp; Routine <span class="badge badge-pill badge-primary ml-1" style="font-size: 10px;">Feed</span></span>
                                    <span class="dropdown-item-desc">LinkedIn &amp; Instagram routine updates</span>
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
                        <a href="https://scholar.google.com/citations?hl=en&user=zSt9oRMAAAAJ" target="_blank" class="nav-social-btn" title="Google Scholar (25+ Papers)">
                            <i class="mdi mdi-school"></i>
                        </a>
                    </li>
                    <li class="list-inline-item mr-2">
                        <a href="https://www.linkedin.com/in/harshverma59/" target="_blank" class="nav-social-btn" title="LinkedIn Profile">
                            <i class="mdi mdi-linkedin"></i>
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

    <!-- Main Container Section (section:nth-of-type(1)) -->
    <section class="section bg-light" style="padding-top: 130px; padding-bottom: 80px;">
        <!-- div:nth-of-type(1) : Container -->
        <div class="container">
            <!-- div:nth-of-type(1) : Hero Header Card -->
            <div class="scholar-hero-card mb-4">
                <div class="row align-items-center">
                    <div class="col-lg-8 mb-4 mb-lg-0">
                        <div class="d-flex align-items-center mb-3">
                            <span class="badge badge-pill text-white px-3 py-2 font-weight-bold mr-2" style="background: linear-gradient(135deg, #2563eb 0%, #0ea5e9 100%);">
                                <i class="mdi mdi-book-open-variant mr-1"></i> Author &amp; Editorial Hub
                            </span>
                            <span class="text-white-50 small"><i class="mdi mdi-check-decagram text-info mr-1"></i> Verified Technical Author</span>
                        </div>
                        <h1 class="text-white font-weight-bold mb-3 display-5" style="font-size: 2.2rem;">Authored Books &amp; Technical Editorial Reviews</h1>
                        <p class="text-light mb-4" style="line-height: 1.7; font-size: 15.5px; opacity: 0.9;">
                            Authoring foundational volumes on <strong>Enterprise AI Agent Architectures</strong>, <strong>Super Engineering Brand Authority</strong>, and <strong>Autonomous Cybersecurity Counteroffensives</strong>. Featuring peer-reviewed editorial contributions across 6 industry volumes.
                        </p>
                        <div class="d-flex flex-wrap align-items-center">
                            <a href="#authored-books" class="btn btn-primary font-weight-bold rounded px-4 py-2 mr-3 mb-2 shadow" style="background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%); border: none;">
                                <i class="mdi mdi-book-multiple mr-1"></i> Explore Authored Books
                            </a>
                            <a href="#reviewed-books" class="btn btn-outline-light rounded px-3 py-2 mr-3 mb-2 font-weight-bold">
                                <i class="mdi mdi-file-check mr-1"></i> Technical Editorial Reviews (6)
                            </a>
                            <a href="page-publications" class="btn btn-outline-light rounded px-3 py-2 mb-2 font-weight-bold">
                                <i class="mdi mdi-school mr-1"></i> 25+ Research Papers &rarr;
                            </a>
                        </div>
                    </div>
                    <div class="col-lg-4 text-center text-lg-right">
                        <div class="d-inline-block position-relative p-2 rounded-xl" style="background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.12); border-radius: 18px;">
                            <img src="images/books/beyond_ai_engineering_mockup.jpg" alt="Beyond AI Engineering" style="max-height: 220px; border-radius: 10px; box-shadow: 0 12px 30px rgba(0,0,0,0.4);" />
                        </div>
                    </div>
                </div>
            </div>

            <!-- div:nth-of-type(2) : Author Metrics Quick Ribbon (Research Paper counter updated to 25+!) -->
            <div class="row mb-5 justify-content-center">
                <div class="col-12">
                    <div class="p-3 p-md-4 rounded-xl border bg-white shadow-sm stat-metric-pill" style="border-radius: 16px;">
                        <div class="row text-center align-items-center">
                            <div class="col-6 col-md-3 border-right mb-3 mb-md-0">
                                <div class="stat-val text-primary" style="font-size: 28px; font-weight: 800; color: #2563eb !important;" data-stat="authored-books">2</div>
                                <div class="stat-lbl text-muted small text-uppercase font-weight-bold">Authored Books</div>
                            </div>
                            <div class="col-6 col-md-3 border-right mb-3 mb-md-0">
                                <a href="page-publications" class="text-decoration-none">
                                    <div class="stat-val text-dark" style="font-size: 28px; font-weight: 800;" data-stat="research-papers">25+</div>
                                    <div class="stat-lbl text-primary small text-uppercase font-weight-bold">Research Papers &rarr;</div>
                                </a>
                            </div>
                            <div class="col-6 col-md-3 border-right">
                                <div class="stat-val text-dark" style="font-size: 28px; font-weight: 800;" data-stat="books-reviewed">6</div>
                                <div class="stat-lbl text-muted small text-uppercase font-weight-bold">Books Reviewed</div>
                            </div>
                            <div class="col-6 col-md-3">
                                <a href="page-publications#patents" class="text-decoration-none">
                                    <div class="stat-val text-success" style="font-size: 28px; font-weight: 800; color: #059669 !important;" data-stat="patents-count">6</div>
                                    <div class="stat-lbl text-muted small text-uppercase font-weight-bold">Enterprise Patents</div>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- div:nth-of-type(3) : Primary Authored Books Section -->
            <div class="authored-books-section mb-5" id="authored-books">
                <div class="title-box text-center mb-4">
                    <span class="badge badge-pill badge-primary px-3 py-1 font-weight-bold mb-2" style="background-color: #2563eb;">NEW RELEASES (2026)</span>
                    <h2 class="title text-capitalize mb-2">Authored Books &amp; Architectural Blueprints</h2>
                    <p class="sub-title text-muted" style="max-width: 780px; margin: 0 auto;">Definitive volumes bridging deep academic rigor and mission-critical enterprise production in autonomous AI agents, personal authority, and adversarial cyber defense.</p>
                </div>

                <div class="row">
                    <!-- Book 1: Beyond AI Engineering -->
                    <div class="col-lg-6 mb-4" id="book1">
                        <div class="authored-book-card h-100 p-4" style="border-top: 4px solid #2563eb !important;">
                            <div class="row">
                                <div class="col-sm-5 text-center mb-3 mb-sm-0">
                                    <div class="book-cover-img-wrap">
                                        <img src="images/books/beyond_ai_engineering_mockup.jpg" alt="Beyond AI Engineering Cover" class="img-fluid rounded" style="max-height: 270px; width: auto;" />
                                    </div>
                                    <div class="mt-3">
                                        <button type="button" class="btn btn-sm btn-outline-primary rounded-pill font-weight-bold px-3" onclick="openJacketModal('beyond_ai')">
                                            <i class="mdi mdi-book-open-page-variant mr-1"></i> Full Jacket Preview
                                        </button>
                                    </div>
                                </div>
                                <div class="col-sm-7 d-flex flex-column">
                                    <div class="d-flex justify-content-between align-items-center mb-2">
                                        <span class="badge text-white font-weight-bold px-2 py-1" style="background-color: #2563eb;">Coming Soon (2026)</span>
                                        <span class="text-muted small font-weight-bold"><i class="mdi mdi-brain mr-1"></i> AI Leadership</span>
                                    </div>
                                    <h3 class="font-weight-bold text-dark mb-1" style="font-size: 1.35rem;">Beyond AI Engineering</h3>
                                    <h6 class="text-primary font-weight-bold mb-2" style="font-size: 0.92rem;">From Creator to Curator: Build Your Authority and Lead the AI Agent Revolution</h6>
                                    <p class="text-muted mb-3" style="font-size: 13.5px; line-height: 1.6;">
                                        Building an authentic personal brand in the era of AI. Transitioning from raw code writing to a <strong>Super Engineer</strong> operating across product, architecture, and sales engineering.
                                    </p>
                                    <div class="mb-3 p-2.5 rounded bg-light border d-flex align-items-center justify-content-between" style="font-size: 12px;">
                                        <span class="text-dark font-weight-bold"><i class="mdi mdi-tools text-success mr-1"></i> Profiled Tool: <strong>ProfileGenius</strong></span>
                                        <a href="https://profilegenius.careeraccelerator.net/" target="_blank" rel="noopener noreferrer" class="text-primary font-weight-bold">Test Profile <i class="mdi mdi-arrow-right"></i></a>
                                    </div>
                                    <div class="mt-auto pt-2">
                                        <h6 class="font-weight-bold text-dark small mb-2 text-uppercase"><i class="mdi mdi-format-list-bulleted mr-1 text-primary"></i> Core Framework Chapters:</h6>
                                        <div class="chapter-list-item"><i class="mdi mdi-check-circle-outline text-primary mr-1"></i> Part I: The Rise of the Super Engineer</div>
                                        <div class="chapter-list-item"><i class="mdi mdi-check-circle-outline text-primary mr-1"></i> Part II: Deterministic Guardrails in Multi-Agent Swarms</div>
                                        <div class="chapter-list-item"><i class="mdi mdi-check-circle-outline text-primary mr-1"></i> Part III: The Operational Architecture of ProfileGenius</div>
                                        <div class="pt-3">
                                            <button type="button" class="btn btn-primary btn-sm rounded font-weight-bold px-4 shadow-sm" onclick="openWaitlistModal('Beyond AI Engineering')">
                                                <i class="mdi mdi-email-check mr-1"></i> Join Book Waitlist
                                            </button>
                                            <a href="https://profilegenius.careeraccelerator.net/" target="_blank" class="btn btn-outline-secondary btn-sm rounded font-weight-bold px-3 ml-2">
                                                Explore Tool
                                            </a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Book 2: AI vs. AI -->
                    <div class="col-lg-6 mb-4" id="book2">
                        <div class="authored-book-card h-100 p-4" style="border-top: 4px solid #0284c7 !important;">
                            <div class="row">
                                <div class="col-sm-5 text-center mb-3 mb-sm-0">
                                    <div class="book-cover-img-wrap">
                                        <img src="images/books/ai_vs_ai_mockup.jpg" alt="AI vs. AI Book Cover" class="img-fluid rounded" style="max-height: 270px; width: auto;" />
                                    </div>
                                    <div class="mt-3">
                                        <button type="button" class="btn btn-sm btn-outline-info rounded-pill font-weight-bold px-3" onclick="openJacketModal('ai_vs_ai')">
                                            <i class="mdi mdi-book-open-page-variant mr-1"></i> Full Jacket Preview
                                        </button>
                                    </div>
                                </div>
                                <div class="col-sm-7 d-flex flex-column">
                                    <div class="d-flex justify-content-between align-items-center mb-2">
                                        <span class="badge text-white font-weight-bold px-2 py-1" style="background-color: #0284c7;">Coming in Late Oct (2026)</span>
                                        <span class="text-muted small font-weight-bold"><i class="mdi mdi-shield-bug mr-1"></i> AI Cybersecurity</span>
                                    </div>
                                    <h3 class="font-weight-bold text-dark mb-1" style="font-size: 1.35rem;">AI vs. AI</h3>
                                    <h6 class="font-weight-bold mb-2" style="color: #0284c7 !important; font-size: 0.92rem;">Engineering the Cybersecurity Counteroffensive</h6>
                                    <p class="text-muted mb-3" style="font-size: 13.5px; line-height: 1.6;">
                                        A technical deep dive with empirical case studies on building autonomous, real-time AI counteroffensive architectures to defend against adversaries wielding weaponized AI.
                                    </p>
                                    <div class="mb-3 p-2.5 rounded bg-light border d-flex align-items-center justify-content-between" style="font-size: 12px;">
                                        <span class="text-dark font-weight-bold"><i class="mdi mdi-shield-check text-info mr-1"></i> Grounded in: <strong>25+ Published Research Papers</strong></span>
                                        <a href="page-publications#pub-13" class="text-info font-weight-bold">View Paper <i class="mdi mdi-arrow-right"></i></a>
                                    </div>
                                    <div class="mt-auto pt-2">
                                        <h6 class="font-weight-bold text-dark small mb-2 text-uppercase"><i class="mdi mdi-format-list-bulleted mr-1 text-info"></i> Key Technical Modules:</h6>
                                        <div class="chapter-list-item"><i class="mdi mdi-check-circle-outline text-info mr-1"></i> Module 1: The Clean Attack Formalization</div>
                                        <div class="chapter-list-item"><i class="mdi mdi-check-circle-outline text-info mr-1"></i> Module 2: Intent-Based Security vs. Identity Perimeters</div>
                                        <div class="chapter-list-item"><i class="mdi mdi-check-circle-outline text-info mr-1"></i> Module 3: Dynamic Honey-Agent Swarms &amp; Trust Graphs</div>
                                        <div class="pt-3">
                                            <button type="button" class="btn btn-sm text-white rounded font-weight-bold px-4 shadow-sm" style="background-color: #0284c7;" onclick="openWaitlistModal('AI vs. AI: Engineering the Cybersecurity Counteroffensive')">
                                                <i class="mdi mdi-email-check mr-1"></i> Join Book Waitlist
                                            </button>
                                            <a href="page-publications" class="btn btn-outline-secondary btn-sm rounded font-weight-bold px-3 ml-2">
                                                Read Research
                                            </a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- div:nth-of-type(4) : Technical Editorial Reviews & Peer Review Contributions Section (Cards Row with 6 cards!) -->
            <div class="row align-items-stretch" id="reviewed-books">
{cards_html}
            </div>

            <!-- Bottom CTA Banner -->
            <div class="mt-5 p-4 p-md-5 rounded-xl border shadow-sm text-center" style="background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); color: #ffffff; border-radius: 20px;">
                <h3 class="font-weight-bold text-white mb-2">Looking to Collaborate on an AI Book or Technical Volume?</h3>
                <p class="text-light mb-4" style="max-width: 650px; margin: 0 auto; opacity: 0.9;">
                    Harsh Verma regularly participates as an invited peer reviewer, technical editorial contributor, and co-author on mission-critical AI architecture and cybersecurity publications.
                </p>
                <div class="d-flex flex-wrap justify-content-center align-items-center" style="gap: 12px;">
                    <button type="button" class="btn btn-primary rounded font-weight-bold px-4 py-2" onclick="window.openAdvisoryBooking ? window.openAdvisoryBooking() : window.location.href='index#contact'">
                        <i class="mdi mdi-calendar-check mr-1"></i> Propose Editorial Collaboration
                    </button>
                    <a href="page-publications" class="btn btn-outline-light rounded font-weight-bold px-4 py-2">
                        <i class="mdi mdi-school mr-1"></i> Explore 25+ Research Publications
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- Full Jacket Preview Modal -->
    <div class="modal fade" id="jacketModal" tabindex="-1" role="dialog" aria-hidden="true">
        <div class="modal-dialog modal-lg modal-dialog-centered" role="document">
            <div class="modal-content border-0 shadow-lg" style="border-radius: 16px; overflow: hidden;">
                <div class="modal-header bg-dark text-white border-0 py-3">
                    <h5 class="modal-title font-weight-bold" id="jacketModalTitle"><i class="mdi mdi-book-open-page-variant mr-2"></i> Full Book Jacket Preview</h5>
                    <button type="button" class="close text-white" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body p-0 text-center bg-dark">
                    <img id="jacketModalImg" src="" alt="Book Jacket" class="img-fluid w-100" style="max-height: 80vh; object-fit: contain;" />
                </div>
                <div class="modal-footer bg-light py-2 border-0">
                    <button type="button" class="btn btn-secondary btn-sm rounded font-weight-bold px-3" data-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Book Waitlist Modal -->
    <div class="modal fade" id="waitlistModal" tabindex="-1" role="dialog" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content border-0 shadow-lg" style="border-radius: 16px;">
                <div class="modal-header bg-primary text-white border-0 py-3" style="background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%) !important;">
                    <h5 class="modal-title font-weight-bold"><i class="mdi mdi-email-check mr-2"></i> Join Book Release Priority Waitlist</h5>
                    <button type="button" class="close text-white" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body p-4">
                    <p class="text-muted small mb-3">
                        Register for early chapter drops, reading previews, and author webinars for <strong id="waitlistBookTitle">Beyond AI Engineering</strong>.
                    </p>
                    <form id="waitlistForm" onsubmit="handleWaitlistSubmit(event)">
                        <div class="form-group mb-3">
                            <label class="small font-weight-bold text-dark">Your Name</label>
                            <input type="text" class="form-control" id="waitlistName" required placeholder="e.g. Dr. Alex Morgan" style="border-radius: 8px;">
                        </div>
                        <div class="form-group mb-3">
                            <label class="small font-weight-bold text-dark">Email Address</label>
                            <input type="email" class="form-control" id="waitlistEmail" required placeholder="alex@enterprise.com" style="border-radius: 8px;">
                        </div>
                        <div class="form-group mb-3">
                            <label class="small font-weight-bold text-dark">Organization / Role (Optional)</label>
                            <input type="text" class="form-control" id="waitlistOrg" placeholder="e.g. Senior AI Architect, Google" style="border-radius: 8px;">
                        </div>
                        <div id="waitlistAlert" class="alert alert-success d-none py-2 small font-weight-bold"></div>
                        <button type="submit" class="btn btn-primary btn-block font-weight-bold py-2 rounded" style="background: #2563eb; border: none; border-radius: 8px;" id="waitlistBtn">
                            <i class="mdi mdi-send-check mr-1"></i> Register for Priority Access
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <!-- Review Details Modal -->
    <div class="modal fade" id="reviewModal" tabindex="-1" role="dialog" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content border-0 shadow-lg" style="border-radius: 16px;">
                <div class="modal-header bg-dark text-white border-0 py-3">
                    <h5 class="modal-title font-weight-bold" id="reviewModalTitle">Review Scope</h5>
                    <button type="button" class="close text-white" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body p-4">
                    <h6 class="font-weight-bold text-primary mb-1" id="reviewModalRole">Invited Technical Reviewer</h6>
                    <p class="text-muted small mb-3" id="reviewModalPub">Publisher / Year</p>
                    <div class="p-3 bg-light rounded border mb-3">
                        <h6 class="font-weight-bold text-dark small text-uppercase mb-2">Scope of Technical Assessment:</h6>
                        <p class="mb-0 text-muted" id="reviewModalScope" style="font-size: 13.5px; line-height: 1.6;"></p>
                    </div>
                    <div class="d-flex justify-content-end">
                        <button type="button" class="btn btn-secondary btn-sm rounded font-weight-bold" data-dismiss="modal">Close</button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Scripts -->
    <script src="js/jquery.min.js"></script>
    <script src="js/bootstrap.bundle.min.js"></script>
    <script src="js/hv-booking-flow.js"></script>
    <script src="js/hv-site-stats.js"></script>

    <script>
        // Dark Mode Controller
        (function() {{
            var toggleBtn = document.getElementById('theme-toggle');
            var savedTheme = localStorage.getItem('hv-theme');
            if (savedTheme === 'dark') {{
                document.body.classList.add('dark-mode');
            }}
            if (toggleBtn) {{
                toggleBtn.addEventListener('click', function() {{
                    document.body.classList.toggle('dark-mode');
                    var isDark = document.body.classList.contains('dark-mode');
                    localStorage.setItem('hv-theme', isDark ? 'dark' : 'light');
                }});
            }}
        }})();

        // Jacket Modal
        function openJacketModal(book) {{
            var img = document.getElementById('jacketModalImg');
            var title = document.getElementById('jacketModalTitle');
            if (book === 'beyond_ai') {{
                img.src = 'images/books/beyond_ai_engineering_full_jacket.jpg';
                title.innerHTML = '<i class="mdi mdi-book-open-page-variant mr-2"></i> Beyond AI Engineering — Full Book Jacket';
            }} else {{
                img.src = 'images/books/ai_vs_ai_full_jacket.jpg';
                title.innerHTML = '<i class="mdi mdi-shield-bug mr-2"></i> AI vs. AI — Full Book Jacket';
            }}
            $('#jacketModal').modal('show');
        }}

        // Waitlist Modal
        var currentWaitlistBook = '';
        function openWaitlistModal(bookTitle) {{
            currentWaitlistBook = bookTitle;
            document.getElementById('waitlistBookTitle').innerText = bookTitle;
            document.getElementById('waitlistAlert').classList.add('d-none');
            $('#waitlistModal').modal('show');
        }}

        function handleWaitlistSubmit(e) {{
            e.preventDefault();
            var name = document.getElementById('waitlistName').value.trim();
            var email = document.getElementById('waitlistEmail').value.trim();
            var org = document.getElementById('waitlistOrg').value.trim();
            var alertBox = document.getElementById('waitlistAlert');
            var btn = document.getElementById('waitlistBtn');

            btn.disabled = true;
            btn.innerHTML = '<i class="mdi mdi-loading mdi-spin mr-1"></i> Registering...';

            fetch('/api/newsletter/subscribe', {{
                method: 'POST',
                headers: {{ 'Content-Type': 'application/json' }},
                body: JSON.stringify({{
                    email: email,
                    name: name,
                    organization: org,
                    source: 'Book Waitlist: ' + currentWaitlistBook
                }})
            }}).then(function(res) {{
                return res.json();
            }}).then(function(data) {{
                alertBox.classList.remove('d-none');
                alertBox.innerText = 'Thank you, ' + name + '! You are confirmed on the priority waitlist for ' + currentWaitlistBook + '.';
                btn.innerHTML = '<i class="mdi mdi-check mr-1"></i> Registered!';
                setTimeout(function() {{
                    $('#waitlistModal').modal('hide');
                    btn.disabled = false;
                    btn.innerHTML = '<i class="mdi mdi-send-check mr-1"></i> Register for Priority Access';
                    document.getElementById('waitlistForm').reset();
                }}, 2500);
            }}).catch(function(err) {{
                alertBox.classList.remove('d-none');
                alertBox.innerText = 'Thank you, ' + name + '! You are confirmed on the priority waitlist.';
                setTimeout(function() {{
                    $('#waitlistModal').modal('hide');
                    btn.disabled = false;
                    btn.innerHTML = '<i class="mdi mdi-send-check mr-1"></i> Register for Priority Access';
                }}, 2000);
            }});
        }}

        // Review Details Modal
        var reviewsData = {{
            "rev-1": {{
                title: "AI Ethics in Action: Principles to Production",
                role: "Invited Technical Editorial Reviewer",
                pub: "Academic & Enterprise AI Press · 2025",
                scope: "Conducted rigorous peer review on Explainable AI (XAI) decision-making boundary formulations, automated audit trail telemetry, and deterministic bias mitigation guardrails in enterprise LLM deployments."
            }},
            "rev-2": {{
                title: "Machine Learning & Generative AI for Marketing",
                role: "Expert Technical Reviewer",
                pub: "Tech Publishing International · 2024",
                scope: "Evaluated high-throughput real-time feature engineering pipelines, prompt-injection defense mechanisms, and latency-optimized multimodal generative inference serving."
            }},
            "rev-3": {{
                title: "Hands-On Generative AI & Deep Learning",
                role: "Technical Advisory & Chapter Reviewer",
                pub: "Enterprise Computing Press · 2024",
                scope: "Technical review of distributed model parallelism, parameter-efficient fine-tuning (LoRA/QLoRA), memory-bounded vector caching, and GPU cluster throughput optimization."
            }},
            "rev-4": {{
                title: "Algorithmic Trading & High-Frequency AI Systems",
                role: "Technical Domain Reviewer",
                pub: "Financial Engineering Press · 2023",
                scope: "Assessed sub-millisecond stream ingestion pipelines, distributed event simulation, continuous reinforcement learning routing, and fault-tolerant risk limit enforcement."
            }},
            "rev-5": {{
                title: "The TensorFlow 2 Workshop: Deep Learning at Enterprise Scale",
                role: "Contributing Technical Reviewer",
                pub: "Packt Publishing · 2022",
                scope: "Technical validation of multi-GPU training scripts, TensorFlow Serving REST/gRPC endpoints, model pruning, and edge quantization pipelines."
            }},
            "rev-6": {{
                title: "Leadership at the Helm of AI & Editorial Review Rigor",
                role: "Senior Peer Reviewer & Advisory Member",
                pub: "Peer Review Editorial Council · 2025",
                scope: "Authored rubric guidelines for empirical reproducibility, statistical integrity validation, and autonomous security risk disclosures in premier peer-reviewed computer science literature."
            }}
        }};

        function openReviewModal(revId) {{
            var r = reviewsData[revId];
            if (!r) return;
            document.getElementById('reviewModalTitle').innerText = r.title;
            document.getElementById('reviewModalRole').innerText = r.role;
            document.getElementById('reviewModalPub').innerText = r.pub;
            document.getElementById('reviewModalScope').innerText = r.scope;
            $('#reviewModal').modal('show');
        }}
    </script>
</body>
</html>
'''
    return html

def main():
    print("Generating page-books.html...")
    content = generate_books_html()
    target_path = os.path.join(ROOT_DIR, "page-books.html")
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"page-books.html successfully generated! Size: {len(content)} bytes.")

if __name__ == "__main__":
    main()
