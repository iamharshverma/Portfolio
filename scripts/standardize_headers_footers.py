#!/usr/bin/env python3
import os
import re

NAVBAR_TEMPLATE = """    <!-- Navbar Start -->
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
                            <linearGradient id="hvNavAccentGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                                <stop offset="0%" stop-color="#38bdf8" />
                                <stop offset="100%" stop-color="#818cf8" />
                            </linearGradient>
                        </defs>
                        <rect width="40" height="40" rx="10" fill="url(#hvNavGrad)" />
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
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
                <i class="mdi mdi-menu"></i>
            </button>
            <div class="collapse navbar-collapse" id="navbarCollapse">
                <ul class="navbar-nav ml-auto navbar-center" id="mySidenav">
                    <li class="nav-item{ABOUT_CLASS}">
                        <a class="nav-link" href="page-about">About</a>
                    </li>
                    <li class="nav-item{PUBLICATIONS_CLASS}">
                        <a class="nav-link" href="page-publications">Publications</a>
                    </li>
                    <li class="nav-item{AWARDS_CLASS}">
                        <a class="nav-link" href="page-awards">Awards</a>
                    </li>
                    <li class="nav-item{MEMBERSHIPS_CLASS}">
                        <a class="nav-link" href="page-memberships">Memberships</a>
                    </li>
                    <li class="nav-item{MEDIA_CLASS}">
                        <a class="nav-link" href="page-media">Media</a>
                    </li>
                    <li class="nav-item{SPEAKER_CLASS}">
                        <a class="nav-link" href="page-events">Speaker</a>
                    </li>
                    <li class="nav-item{BOOKS_CLASS}">
                        <a class="nav-link" href="page-books">Books</a>
                    </li>
                    <li class="nav-item{BLOG_CLASS}">
                        <a class="nav-link" href="page-blog">Blog</a>
                    </li>
                    <li class="nav-item dropdown{DROPDOWN_CLASS}">
                        <a class="nav-link dropdown-toggle" href="javascript:void(0);" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            More <i class="mdi mdi-chevron-down nav-dropdown-arrow"></i>
                        </a>
                        <div class="dropdown-menu dropdown-menu-right nav-custom-dropdown" aria-labelledby="navbarDropdown">
                            <div class="nav-dropdown-header">
                                <span>Extended Portfolios &amp; Hubs</span>
                            </div>
                            <a class="dropdown-item nav-dropdown-item{ANALYTICS_CLASS}" href="page-media-distribution-analytics">
                                <div class="dropdown-item-icon bg-soft-primary"><i class="mdi mdi-chart-box-outline"></i></div>
                                <div class="dropdown-item-content">
                                    <span class="dropdown-item-title">Distribution Analytics <span class="badge badge-pill badge-primary ml-1" style="font-size: 10px;">3.75B+</span></span>
                                    <span class="dropdown-item-desc">Publication reach &amp; influence pyramid</span>
                                </div>
                            </a>
                            <a class="dropdown-item nav-dropdown-item{PORTFOLIO_CLASS}" href="page-portfolio">
                                <div class="dropdown-item-icon bg-soft-info"><i class="mdi mdi-cube-outline"></i></div>
                                <div class="dropdown-item-content">
                                    <span class="dropdown-item-title">Portfolio Projects</span>
                                    <span class="dropdown-item-desc">Architectures, agent frameworks &amp; systems</span>
                                </div>
                            </a>
                            <a class="dropdown-item nav-dropdown-item{SLIDES_CLASS}" href="page-smart-slides">
                                <div class="dropdown-item-icon bg-soft-primary"><i class="mdi mdi-presentation-play"></i></div>
                                <div class="dropdown-item-content">
                                    <span class="dropdown-item-title">Smart Slides <span class="badge badge-pill badge-primary ml-1" style="font-size: 10px;">New</span></span>
                                    <span class="dropdown-item-desc">Interactive executive &amp; research slide decks</span>
                                </div>
                            </a>
                            <a class="dropdown-item nav-dropdown-item{SOCIAL_CLASS}" href="page-social">
                                <div class="dropdown-item-icon bg-soft-success"><i class="mdi mdi-share-variant"></i></div>
                                <div class="dropdown-item-content">
                                    <span class="dropdown-item-title">Social &amp; Routine <span class="badge badge-pill badge-primary ml-1" style="font-size: 10px;">Feed</span></span>
                                    <span class="dropdown-item-desc">LinkedIn &amp; Instagram routine updates</span>
                                </div>
                            </a>
                            <a class="dropdown-item nav-dropdown-item" href="page-about#verified-profiles">
                                <div class="dropdown-item-icon bg-soft-warning"><i class="mdi mdi-shield-account-outline"></i></div>
                                <div class="dropdown-item-content">
                                    <span class="dropdown-item-title">42 Verified Profiles Hub</span>
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
                        <a href="https://www.instagram.com/iamharshverma/" target="_blank" class="nav-social-btn" title="Instagram Profile">
                            <i class="mdi mdi-instagram"></i>
                        </a>
                    </li>
                    <li class="list-inline-item mr-2">
                        <a href="https://github.com/iamharshverma" target="_blank" class="nav-social-btn" title="GitHub Profile">
                            <i class="mdi mdi-github-face"></i>
                        </a>
                    </li>
                    <li class="list-inline-item mr-2">
                        <a rel="me" href="https://mastodon.social/@harshverma59" target="_blank" class="nav-social-btn" title="Mastodon Profile (@harshverma59)" aria-label="Mastodon">
                            <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: -2px;" xmlns="http://www.w3.org/2000/svg">
                                <path d="M23.268 5.313c-.35-2.578-2.617-4.61-5.304-5.004C17.51.242 15.792 0 11.813 0h-.03c-3.98 0-4.835.242-5.288.309C3.882.692 1.496 2.509.91 5.313.34 8.046.2 11.458.232 14.398c.036 3.23.36 6.438 3.197 7.223 2.11.583 4.295.66 6.435.485.495-.04 1.05-.1 1.58-.19.04-.01.07-.02.1-.03l.03-.01.02-.01c.21-.05.42-.1.62-.17.15-.05.31-.11.46-.17v-2.02c-.41.13-.82.24-1.24.32-.42.08-.85.13-1.28.15-2.03.11-4.08-.03-4.32-.82-.04-.15-.07-.33-.08-.54l.01-.01c.27.08.55.15.83.21 1.77.38 3.6.43 5.42.15 1.51-.23 3.01-.69 4.37-1.39 1.95-.99 2.54-2.67 2.68-4.06.31-3.03.25-6.52-.09-9.17zM18.8 13.91h-2.12V7.79c0-1.29-.54-1.95-1.63-1.95-1.2 0-1.8.78-1.8 2.33v3.37h-2.13V8.17c0-1.55-.6-2.33-1.8-2.33-1.09 0-1.63.66-1.63 1.95v6.12H5.56V7.65c0-1.29.33-2.31 1-3.06.67-.75 1.55-1.14 2.64-1.14 1.26 0 2.22.49 2.87 1.46l.57.96.57-.96c.65-.97 1.61-1.46 2.87-1.46 1.09 0 1.97.39 2.64 1.14.67.75 1 1.77 1 3.06v6.26z"/>
                            </svg>
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
    <!-- Navbar End -->"""

FOOTER_TEMPLATE = """    <!-- Footer Start -->
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
    <!-- Footer End -->"""

def build_navbar(active_key):
    dropdown_keys = ["analytics", "portfolio", "slides", "social"]
    return (
        NAVBAR_TEMPLATE
        .replace("{ABOUT_CLASS}", " active" if active_key == "about" else "")
        .replace("{PUBLICATIONS_CLASS}", " active" if active_key == "publications" else "")
        .replace("{AWARDS_CLASS}", " active" if active_key == "awards" else "")
        .replace("{MEMBERSHIPS_CLASS}", " active" if active_key == "memberships" else "")
        .replace("{MEDIA_CLASS}", " active" if active_key == "media" else "")
        .replace("{SPEAKER_CLASS}", " active" if active_key == "speaker" else "")
        .replace("{BOOKS_CLASS}", " active" if active_key == "books" else "")
        .replace("{BLOG_CLASS}", " active" if active_key == "blog" else "")
        .replace("{DROPDOWN_CLASS}", " active" if active_key in dropdown_keys else "")
        .replace("{ANALYTICS_CLASS}", " active" if active_key == "analytics" else "")
        .replace("{PORTFOLIO_CLASS}", " active" if active_key == "portfolio" else "")
        .replace("{SLIDES_CLASS}", " active" if active_key == "slides" else "")
        .replace("{SOCIAL_CLASS}", " active" if active_key == "social" else "")
    )

PAGES_MAP = {
    "index.html": "none",
    "page-about.html": "about",
    "page-publications.html": "publications",
    "page-awards.html": "awards",
    "page-memberships.html": "memberships",
    "page-media.html": "media",
    "page-events.html": "speaker",
    "page-books.html": "books",
    "page-blog.html": "blog",
    "page-portfolio.html": "portfolio",
    "page-smart-slides.html": "slides",
    "page-slides.html": "slides",
    "page-media-distribution-analytics.html": "analytics",
    "page-social.html": "social",
    "page-blog-detail.html": "blog",
    "page-portfolio-detail.html": "portfolio"
}

def standardize_file(filepath, active_key):
    if not os.path.exists(filepath):
        print(f"Skipping {filepath} (does not exist)")
        return
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Replace Navbar
    nav_pattern = re.compile(r"<!-- Navbar Start -->.*?<!-- Navbar End -->", re.DOTALL | re.IGNORECASE)
    if nav_pattern.search(content):
        new_nav = build_navbar(active_key)
        content = nav_pattern.sub(new_nav, content)
    else:
        # Fallback to <nav ...> ... </nav>
        generic_nav = re.compile(r"<nav[^>]*class=[\"'][^\"']*navbar-custom[^\"']*[\"'][^>]*>.*?</nav>", re.DOTALL | re.IGNORECASE)
        if generic_nav.search(content):
            new_nav = build_navbar(active_key)
            content = generic_nav.sub(new_nav, content)

    # 2. Replace Footer
    footer_pattern = re.compile(r"<!-- Footer Start -->.*?<!-- Footer End -->", re.DOTALL | re.IGNORECASE)
    if footer_pattern.search(content):
        content = footer_pattern.sub(FOOTER_TEMPLATE, content)

    # 3. Specific fixes
    # Fix broken hero image on events / speaker
    content = content.replace("images/SectaAI_BTRPHBqq~2.jpg", "images/harsh/Harsh_portfolio_pic.png")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {filepath} (active: {active_key})")

def main():
    for filename, active_key in PAGES_MAP.items():
        standardize_file(filename, active_key)

    # Also create page-speaker.html and speaker.html if page-events.html exists
    if os.path.exists("page-events.html"):
        with open("page-events.html", "r", encoding="utf-8") as f:
            events_html = f.read()
        
        # Write page-speaker.html
        with open("page-speaker.html", "w", encoding="utf-8") as f:
            f.write(events_html)
        print("Created page-speaker.html as identical mirror of page-events.html")

        # Write speaker.html
        with open("speaker.html", "w", encoding="utf-8") as f:
            f.write(events_html)
        print("Created speaker.html as identical mirror of page-events.html")

if __name__ == "__main__":
    main()
