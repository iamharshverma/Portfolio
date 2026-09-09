import json
import re

def build_home_news_section():
    with open('media_data.json', 'r') as f:
        media_items = json.load(f)

    # Let's organize curated items
    # 1. Marquee Row 1 (Left floating items): Major Press & Landmark
    marquee_row1_ids = [
        'media-forttuna-powerlist-times-square',
        'media-business-insider-gra-2026',
        'media-berkeley-skydeck-batch22-workshop',
        'media-hackernoon-production-gap',
        'media-usa-today-identity-perimeters',
        'media-yahoo-finance-cybersecurity-excellence',
        'media-barchart-control-problem',
        'media-google-developer-expert-listing',
        'media-cio-insightful-top5-leaders',
        'media-street-insider-human-ai',
        'media-noble-tech-awards-muse-world',
        'media-newsbreak-unified-framework'
    ]

    # 2. Marquee Row 2 (Right floating items): Keynotes, Podcasts, Research & Blogs
    marquee_row2_ids = [
        'media-futureagi-talk',
        'media-chai-coaching-cybersecurity',
        'media-trueml-talks-35',
        'media-vlink-tech-talk-ep55',
        'media-xraised-beyond-code',
        'media-sz179-quantum-cybersecurity',
        'media-chai-coaching-interview-mastery',
        'media-lifepage-interview',
        'media-health-tech-week-speaker',
        'media-primeful-insights-industry-icon',
        'media-ifgict-fellowship-timebusiness',
        'media-ein-knox-news-tech-excellence'
    ]

    media_by_id = {it['id']: it for it in media_items}

    def build_marquee_card(item_id, is_custom_blog=None):
        if is_custom_blog:
            it = is_custom_blog
        else:
            it = media_by_id.get(item_id)
            if not it:
                return ""
        
        title = it['title']
        outlet = it.get('outlet', 'Tech Media')
        year = it.get('year', '2026')
        url = it.get('primary_url', 'page-media')
        icon = it.get('icon_svg', '')
        badge_type = it.get('type_label', 'Press')

        if icon.startswith('images/'):
            icon_path = icon
        else:
            icon_path = f"images/media/{icon}"

        return f'''
            <div class="marquee-item-card">
                <a href="{url}" target="_blank" rel="noopener noreferrer" class="marquee-card-link">
                    <div class="marquee-card-thumb">
                        <img src="{icon_path}" alt="{outlet}" loading="lazy" />
                    </div>
                    <div class="marquee-card-content">
                        <div class="d-flex align-items-center mb-1">
                            <span class="marquee-tag-pill">{outlet}</span>
                            <span class="marquee-year-pill ml-auto"><i class="mdi mdi-calendar-blank-outline mr-1"></i>{year}</span>
                        </div>
                        <h6 class="marquee-card-title">{title}</h6>
                    </div>
                </a>
            </div>
        '''

    # Build marquee row 1 cards (repeated twice for smooth infinite loop)
    row1_html = "".join([build_marquee_card(i) for i in marquee_row1_ids])
    row2_html = "".join([build_marquee_card(i) for i in marquee_row2_ids])

    # Add custom blog items to row 2
    blog_custom_1 = {
        'title': 'Helm with YugabyteDB on Google Kubernetes Engine (GKE)',
        'outlet': 'Medium Engineering',
        'year': 'Tech Blog',
        'primary_url': 'https://medium.com/@harshverma59/helm-with-yugabytedb-gke-google-kubernetes-engine-9099b62548cd',
        'icon_svg': 'images/blog/helm_blog.jpg',
        'type_label': 'Blog'
    }
    blog_custom_2 = {
        'title': 'Secure Heterogeneous IoT Data Management System',
        'outlet': 'IEEE CogML',
        'year': 'Research',
        'primary_url': 'https://ieeexplore.ieee.org/document/9014355',
        'icon_svg': 'images/blog/IEEE_cogML.png',
        'type_label': 'Paper'
    }
    row2_html += build_marquee_card(None, blog_custom_1)
    row2_html += build_marquee_card(None, blog_custom_2)

    # 12 Curated Featured Carousel Cards for #customer-testi
    carousel_items = [
        {
            'category': 'press',
            'badge': 'Times Square Landmark',
            'badge_color': '#f59e0b',
            'icon_svg': 'images/media/timessquare_forttuna_badge.svg',
            'title': 'Times Square NYC Broadcast & Forttuna Global 100 Power List 2026',
            'outlet': 'Nasdaq & Times Square / Business Insider',
            'date': '2026',
            'quote': 'Recognized among international industry pioneers in AI, broadcast across giant Nasdaq and Times Square screens in New York City.',
            'topics': ['AI Leadership', 'Times Square NYC', 'Global 100'],
            'url': 'https://global100.forttuna.com/the-power-list-2026-honorees/profile?name=harsh-verma',
            'btn_text': 'View Times Square Feature',
            'btn_icon': 'mdi-account-star'
        },
        {
            'category': 'press',
            'badge': 'Major Press',
            'badge_color': '#2563eb',
            'icon_svg': 'images/media/business_insider_badge.svg',
            'title': 'Business Insider: Global Recognition Award 2026 for AI & Cybersecurity Innovation',
            'outlet': 'Business Insider',
            'date': 'Feb 2026',
            'quote': 'Honored for pioneering agentic security architectures and enterprise AI resilience protecting mission-critical cloud infrastructure.',
            'topics': ['AI Security', 'Global Recognition Award', 'Cloud Defense'],
            'url': 'https://markets.businessinsider.com/news/stocks/harsh-verma-receives-2026-global-recognition-award-for-revolutionary-contributions-to-ai-and-cybersecurity-1035817812',
            'btn_text': 'Read on Business Insider',
            'btn_icon': 'mdi-newspaper'
        },
        {
            'category': 'skydeck',
            'badge': 'Berkeley SkyDeck',
            'badge_color': '#0d9488',
            'icon_svg': 'images/media/skydeck_badge.svg',
            'title': 'Berkeley SkyDeck: Batch 22 AI Security Workshop & Global Keynote',
            'outlet': 'UC Berkeley SkyDeck',
            'date': '2025 - 2026',
            'quote': 'Mentoring next-gen unicorn founders and leading technical masterclasses on autonomous agent security and enterprise scale.',
            'topics': ['SkyDeck Batch 22', 'Agentic Security', 'Startup Advisor'],
            'url': 'https://skydeck.berkeley.edu',
            'btn_text': 'Explore SkyDeck Program',
            'btn_icon': 'mdi-school'
        },
        {
            'category': 'press',
            'badge': 'Major Press',
            'badge_color': '#16a34a',
            'icon_svg': 'images/media/hackernoon_badge.svg',
            'title': 'HackerNoon: Solving the AI Agent Production Gap — Multi-Agent Systems in Practice',
            'outlet': 'HackerNoon',
            'date': '2026',
            'quote': 'Engineering blueprint on navigating non-deterministic agent workflows, multi-agent arbitration, and high-throughput production SLAs.',
            'topics': ['Multi-Agent Systems', 'Production AI', 'Agent Orchestration'],
            'url': 'https://hackernoon.com/solving-the-ai-agent-production-gap-challenges-and-architectures-for-multi-agent-systems',
            'btn_text': 'Read on HackerNoon',
            'btn_icon': 'mdi-code-tags'
        },
        {
            'category': 'press',
            'badge': 'Major Press',
            'badge_color': '#0284c7',
            'icon_svg': 'images/media/usatoday_badge.svg',
            'title': 'USA Today: Securing the Non-Human Identity Perimeter in Enterprise Clouds',
            'outlet': 'USA Today Network',
            'date': '2026',
            'quote': 'Architectural breakdown of machine-to-machine authentication, service mesh cryptographic attestation, and zero-trust identity defense.',
            'topics': ['NHI Security', 'Zero Trust', 'Cloud Architecture'],
            'url': 'https://classifieds.usatoday.com/press/identity-as-the-perimeter-securing-the-rise-of-non-human-identities-in-enterprise-cloud-infrastructure/',
            'btn_text': 'Read on USA Today',
            'btn_icon': 'mdi-shield-check'
        },
        {
            'category': 'press',
            'badge': 'Major Press',
            'badge_color': '#7c3aed',
            'icon_svg': 'images/media/yahoo_finance_badge.svg',
            'title': 'Yahoo Finance: Cybersecurity Excellence Awards 2026 Feature',
            'outlet': 'Yahoo Finance',
            'date': '2026',
            'quote': 'Celebrated for transformative breakthroughs in automated threat detection, cyber resiliency, and high-performance ML defense engines.',
            'topics': ['Cyber Excellence', 'Threat Detection', 'AI Governance'],
            'url': 'https://finance.yahoo.com/news/winners-2026-cybersecurity-excellence-awards-143000928.html',
            'btn_text': 'Read on Yahoo Finance',
            'btn_icon': 'mdi-finance'
        },
        {
            'category': 'podcast',
            'badge': 'Keynote Talk',
            'badge_color': '#ea580c',
            'icon_svg': 'images/media/futureagi_badge.svg',
            'title': 'FutureAGI Keynote: Enterprise Agentic Security & Multi-Model Orchestration',
            'outlet': 'FutureAGI / YouTube',
            'date': '2025',
            'quote': 'Invited keynote exploring defensive boundary layers, prompt injection containment, and verifiable inference in enterprise systems.',
            'topics': ['Agentic AI', 'Keynote', 'Palo Alto Networks'],
            'url': 'https://www.youtube.com/watch?v=0wQv7T8fF8g',
            'btn_text': 'Watch Keynote Video',
            'btn_icon': 'mdi-youtube'
        },
        {
            'category': 'podcast',
            'badge': 'ML Keynote',
            'badge_color': '#4f46e5',
            'icon_svg': 'images/media/trueml_badge.svg',
            'title': 'TrueML Talks #35: Big Data & ML Practices at Palo Alto Networks',
            'outlet': 'TrueFoundry / TrueML',
            'date': '2025',
            'quote': 'Deep dive into feature engineering pipelines, high-throughput model serving, distributed inference, and production MLOps at scale.',
            'topics': ['MLOps', 'Big Data', 'Distributed Systems'],
            'url': 'https://www.youtube.com/watch?v=eG_W9_8f0a0',
            'btn_text': 'Watch Tech Session',
            'btn_icon': 'mdi-video'
        },
        {
            'category': 'podcast',
            'badge': 'Podcast Feature',
            'badge_color': '#b45309',
            'icon_svg': 'images/media/chai_coaching_badge.svg',
            'title': 'Chai & Coaching: How to Build a High-Impact Career in Cybersecurity & AI',
            'outlet': 'Chai & Coaching Podcast',
            'date': '2025',
            'quote': 'Strategic career masterclass detailing cloud security roadmaps, architectural problem-solving, and leadership at Tier-1 tech firms.',
            'topics': ['Career Strategy', 'Cloud Defense', 'Executive Mentorship'],
            'url': 'https://www.youtube.com/watch?v=W_Yw8oN09s8',
            'btn_text': 'Listen to Podcast',
            'btn_icon': 'mdi-headphones'
        },
        {
            'category': 'blog',
            'badge': 'Medium Tech Blog',
            'badge_color': '#047857',
            'icon_svg': 'images/blog/helm_blog.jpg',
            'title': 'Helm with YugabyteDB on Google Kubernetes Engine (GKE)',
            'outlet': 'Medium TechQuickie',
            'date': 'Tech Blog',
            'quote': 'Hands-on architectural tutorial on orchestrating distributed SQL clusters with Helm charts and GKE stateful sets for zero-downtime scaling.',
            'topics': ['Kubernetes', 'Helm', 'YugabyteDB', 'GKE'],
            'url': 'https://medium.com/@harshverma59/helm-with-yugabytedb-gke-google-kubernetes-engine-9099b62548cd',
            'btn_text': 'Read on Medium',
            'btn_icon': 'mdi-medium'
        },
        {
            'category': 'blog',
            'badge': 'IEEE Research Paper',
            'badge_color': '#1e40af',
            'icon_svg': 'images/blog/IEEE_cogML.png',
            'title': 'IEEE CogML: Secure Heterogeneous IoT Data Management System',
            'outlet': 'IEEE International Conference',
            'date': 'IEEE CogML',
            'quote': 'Peer-reviewed research paper establishing low-latency edge ingestion architectures and real-time cryptographic stream verification.',
            'topics': ['IEEE CogML', 'IoT Security', 'Distributed Systems'],
            'url': 'https://ieeexplore.ieee.org/document/9014355',
            'btn_text': 'Read IEEE Paper',
            'btn_icon': 'mdi-file-document'
        },
        {
            'category': 'blog',
            'badge': 'Engineering Interview',
            'badge_color': '#475569',
            'icon_svg': 'images/blog/LifePage.png',
            'title': 'LifePage Interview: Software Development Life Cycle & Architectural Mindset',
            'outlet': 'LifePage India',
            'date': 'Interview',
            'quote': 'Reflections on scaling software systems, engineering culture, debugging distributed bottlenecks, and mentoring next-gen developers.',
            'topics': ['Engineering Mindset', 'Software Lifecycle', 'Leadership'],
            'url': 'https://www.lifepage.in/page/harsh',
            'btn_text': 'Read Interview',
            'btn_icon': 'mdi-account-voice'
        }
    ]

    carousel_cards_html = ""
    for c in carousel_items:
        topic_chips = "".join([f'<span class="home-news-tag">{t}</span>' for t in c['topics']])
        carousel_cards_html += f'''
            <div class="pad-right-left m-2 home-news-carousel-item" data-category="{c['category']}">
                <div class="blog-post rounded customer-testi home-media-news-card">
                    <div class="position-relative home-media-card-header">
                        <img src="{c['icon_svg']}" class="img-fluid rounded-top home-media-card-img" alt="{c['outlet']}" loading="lazy">
                        <span class="home-media-type-badge" style="background-color: {c['badge_color']};">
                            {c['badge']}
                        </span>
                    </div>
                    <div class="content pt-3 pb-3 p-3">
                        <div class="d-flex align-items-center justify-content-between mb-2">
                            <span class="home-outlet-label">{c['outlet']}</span>
                            <span class="home-date-label"><i class="mdi mdi-calendar-outline mr-1"></i>{c['date']}</span>
                        </div>
                        <h5 class="home-news-card-title">
                            <a href="{c['url']}" target="_blank" rel="noopener noreferrer" class="title text-dark">{c['title']}</a>
                        </h5>
                        <div class="home-news-quote">
                            <i class="mdi mdi-format-quote-open quote-icon"></i>
                            <p class="mb-0">{c['quote']}</p>
                        </div>
                        <div class="home-news-tags-wrap mb-3">
                            {topic_chips}
                        </div>
                        <div class="post-meta d-flex justify-content-between align-items-center mt-2 pt-2 border-top">
                            <a href="{c['url']}" target="_blank" rel="noopener noreferrer" class="btn btn-sm btn-primary rounded font-weight-bold px-3 py-1 text-white" style="font-size: 12.5px;">
                                <i class="mdi {c['btn_icon']} mr-1"></i> {c['btn_text']}
                            </a>
                            <a href="page-media" class="text-muted small font-weight-bold" title="View on Media Page">
                                Media Hub <i class="mdi mdi-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        '''

    full_section = f'''
        <!-- Latest Tech News (TechQuickie), Media & Tech Blogs Start -->
        <section class="section bg-light" id="news" style="position: relative; overflow: hidden;">
            <style>
                /* Home Media & News Section Styling */
                .home-news-ribbon {{
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: center;
                    gap: 12px;
                    margin-bottom: 25px;
                }}
                .home-news-stat-pill {{
                    display: inline-flex;
                    align-items: center;
                    padding: 6px 14px;
                    border-radius: 50px;
                    background: #ffffff;
                    border: 1px solid rgba(0, 0, 0, 0.08);
                    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04);
                    font-size: 13px;
                    font-weight: 600;
                    color: #1e293b;
                    transition: all 0.25s ease;
                }}
                .home-news-stat-pill:hover {{
                    transform: translateY(-2px);
                    box-shadow: 0 4px 12px rgba(37, 99, 235, 0.12);
                    border-color: rgba(37, 99, 235, 0.3);
                }}
                .home-news-stat-pill i {{
                    font-size: 16px;
                    margin-right: 6px;
                }}

                /* Dual Floating Marquee Container */
                .home-marquee-wrapper {{
                    margin: 25px 0 35px 0;
                    position: relative;
                    overflow: hidden;
                    padding: 8px 0;
                }}
                .home-marquee-track {{
                    display: flex;
                    width: max-content;
                    gap: 18px;
                    padding: 6px 0;
                }}
                .home-marquee-track-left {{
                    animation: marqueeFloatLeft 42s linear infinite;
                }}
                .home-marquee-track-right {{
                    animation: marqueeFloatRight 42s linear infinite;
                }}
                .home-marquee-wrapper:hover .home-marquee-track {{
                    animation-play-state: paused;
                }}

                @keyframes marqueeFloatLeft {{
                    0% {{ transform: translateX(0); }}
                    100% {{ transform: translateX(-50%); }}
                }}
                @keyframes marqueeFloatRight {{
                    0% {{ transform: translateX(-50%); }}
                    100% {{ transform: translateX(0); }}
                }}

                /* Floating Marquee Pill Cards */
                .marquee-item-card {{
                    flex: 0 0 340px;
                    background: #ffffff;
                    border-radius: 14px;
                    border: 1px solid rgba(0, 0, 0, 0.07);
                    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.04);
                    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
                    overflow: hidden;
                }}
                .marquee-item-card:hover {{
                    transform: translateY(-3px) scale(1.02);
                    border-color: #2563eb;
                    box-shadow: 0 8px 24px rgba(37, 99, 235, 0.14);
                }}
                .marquee-card-link {{
                    display: flex;
                    align-items: center;
                    padding: 10px 14px;
                    text-decoration: none !important;
                    color: inherit;
                    gap: 12px;
                }}
                .marquee-card-thumb {{
                    width: 72px;
                    height: 52px;
                    flex-shrink: 0;
                    border-radius: 8px;
                    overflow: hidden;
                    background: #f8fafc;
                    border: 1px solid rgba(0, 0, 0, 0.06);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }}
                .marquee-card-thumb img {{
                    width: 100%;
                    height: 100%;
                    object-fit: cover;
                }}
                .marquee-card-content {{
                    flex: 1;
                    min-width: 0;
                }}
                .marquee-tag-pill {{
                    font-size: 10.5px;
                    font-weight: 700;
                    text-transform: uppercase;
                    letter-spacing: 0.5px;
                    color: #2563eb;
                    background: rgba(37, 99, 235, 0.08);
                    padding: 2px 6px;
                    border-radius: 4px;
                }}
                .marquee-year-pill {{
                    font-size: 11px;
                    color: #64748b;
                    font-weight: 500;
                }}
                .marquee-card-title {{
                    font-size: 12.5px;
                    font-weight: 600;
                    color: #0f172a;
                    margin: 0;
                    line-height: 1.35;
                    white-space: nowrap;
                    overflow: hidden;
                    text-overflow: ellipsis;
                }}

                /* Home Carousel Card Styles */
                .home-media-news-card {{
                    background: #ffffff;
                    border: 1px solid rgba(0, 0, 0, 0.08);
                    border-radius: 16px;
                    overflow: hidden;
                    transition: all 0.35s ease;
                    box-shadow: 0 4px 18px rgba(0, 0, 0, 0.05);
                    height: 100%;
                    display: flex;
                    flex-direction: column;
                }}
                .home-media-news-card:hover {{
                    transform: translateY(-6px);
                    box-shadow: 0 12px 30px rgba(37, 99, 235, 0.12);
                    border-color: rgba(37, 99, 235, 0.3);
                }}
                .home-media-card-header {{
                    position: relative;
                    overflow: hidden;
                    background: #f1f5f9;
                }}
                .home-media-card-img {{
                    width: 100%;
                    aspect-ratio: 16 / 9;
                    object-fit: cover;
                    display: block;
                    transition: transform 0.5s ease;
                }}
                .home-media-news-card:hover .home-media-card-img {{
                    transform: scale(1.03);
                }}
                .home-media-type-badge {{
                    position: absolute;
                    top: 12px;
                    left: 12px;
                    color: #ffffff;
                    font-size: 11px;
                    font-weight: 700;
                    letter-spacing: 0.5px;
                    text-transform: uppercase;
                    padding: 4px 10px;
                    border-radius: 50px;
                    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
                }}
                .home-outlet-label {{
                    font-size: 12px;
                    font-weight: 700;
                    color: #2563eb;
                    text-transform: uppercase;
                    letter-spacing: 0.5px;
                }}
                .home-date-label {{
                    font-size: 12px;
                    color: #64748b;
                    font-weight: 500;
                }}
                .home-news-card-title {{
                    font-size: 15.5px;
                    font-weight: 700;
                    line-height: 1.4;
                    margin-bottom: 10px;
                    min-height: 44px;
                    display: -webkit-box;
                    -webkit-line-clamp: 2;
                    -webkit-box-orient: vertical;
                    overflow: hidden;
                }}
                .home-news-card-title a {{
                    color: #0f172a;
                    text-decoration: none;
                    transition: color 0.2s ease;
                }}
                .home-news-card-title a:hover {{
                    color: #2563eb !important;
                }}
                .home-news-quote {{
                    background: #f8fafc;
                    border-left: 3px solid #3b82f6;
                    padding: 8px 10px;
                    border-radius: 0 8px 8px 0;
                    margin-bottom: 12px;
                    font-size: 12.5px;
                    line-height: 1.45;
                    color: #334155;
                    display: -webkit-box;
                    -webkit-line-clamp: 2;
                    -webkit-box-orient: vertical;
                    overflow: hidden;
                }}
                .home-news-quote .quote-icon {{
                    color: #3b82f6;
                    margin-right: 4px;
                    font-size: 14px;
                }}
                .home-news-tags-wrap {{
                    display: flex;
                    flex-wrap: wrap;
                    gap: 5px;
                }}
                .home-news-tag {{
                    font-size: 11px;
                    font-weight: 600;
                    color: #475569;
                    background: #f1f5f9;
                    padding: 2px 7px;
                    border-radius: 4px;
                }}

                /* Category Filter Tabs */
                .home-news-filter-bar {{
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: center;
                    gap: 8px;
                    margin-bottom: 20px;
                }}
                .home-news-filter-btn {{
                    border: 1px solid rgba(0, 0, 0, 0.1);
                    background: #ffffff;
                    color: #475569;
                    font-size: 13px;
                    font-weight: 600;
                    padding: 6px 16px;
                    border-radius: 50px;
                    cursor: pointer;
                    transition: all 0.2s ease;
                }}
                .home-news-filter-btn:hover,
                .home-news-filter-btn.active {{
                    background: #2563eb;
                    color: #ffffff;
                    border-color: #2563eb;
                    box-shadow: 0 3px 10px rgba(37, 99, 235, 0.25);
                }}

                /* Dark Mode Adaptations */
                html.dark-mode #news {{
                    background-color: #0b0f19 !important;
                }}
                html.dark-mode .home-news-stat-pill {{
                    background: #1e293b;
                    border-color: rgba(255, 255, 255, 0.1);
                    color: #e2e8f0;
                }}
                html.dark-mode .marquee-item-card {{
                    background: #1e293b;
                    border-color: rgba(255, 255, 255, 0.08);
                }}
                html.dark-mode .marquee-card-title {{
                    color: #f1f5f9;
                }}
                html.dark-mode .home-media-news-card {{
                    background: #1e293b;
                    border-color: rgba(255, 255, 255, 0.1);
                }}
                html.dark-mode .home-news-card-title a {{
                    color: #f1f5f9;
                }}
                html.dark-mode .home-news-quote {{
                    background: #0f172a;
                    color: #cbd5e1;
                }}
                html.dark-mode .home-news-tag {{
                    background: #334155;
                    color: #cbd5e1;
                }}
                html.dark-mode .home-news-filter-btn {{
                    background: #1e293b;
                    border-color: rgba(255, 255, 255, 0.12);
                    color: #cbd5e1;
                }}
                html.dark-mode .home-news-filter-btn.active {{
                    background: #2563eb;
                    color: #ffffff;
                }}
            </style>

            <div class="container">
                <!-- Section Header -->
                <div class="row justify-content-center">
                    <div class="col-12 text-center">
                        <div class="container-title text-center mb-3 pb-2">
                            <div class="titles">
                                <span class="badge badge-primary px-3 py-1 font-weight-bold mb-2" style="font-size: 12px; letter-spacing: 0.5px; border-radius: 50px;">
                                    <i class="mdi mdi-broadcast mr-1"></i> PRESS &amp; THOUGHT LEADERSHIP
                                </span>
                                <h2 class="title text-capitalize mb-3">Latest Tech News (TechQuickie), Media &amp; Tech Blogs</h2>
                                <p class="pera-title para-desc-600 text-light-muted mb-0 mx-auto" style="max-width: 720px; font-size: 15px; line-height: 1.6;">
                                    Leading press features, keynote addresses, podcast dialogues, and technical blogs across AI Security, Autonomous Agent Systems, Non-Human Identity Perimeters, and Distributed Architecture.
                                </p>
                                <span></span>
                            </div>
                        </div>

                        <!-- Stats Highlight Ribbon -->
                        <div class="home-news-ribbon">
                            <div class="home-news-stat-pill">
                                <i class="mdi mdi-newspaper-variant-multiple text-primary"></i>
                                <span><strong>37+</strong> Global Press Features</span>
                            </div>
                            <div class="home-news-stat-pill">
                                <i class="mdi mdi-billboard text-warning"></i>
                                <span><strong>Times Square NYC</strong> Billboard Broadcast</span>
                            </div>
                            <div class="home-news-stat-pill">
                                <i class="mdi mdi-earth text-info"></i>
                                <span><strong>15+</strong> Tier-1 Outlets (Business Insider, USA Today)</span>
                            </div>
                            <div class="home-news-stat-pill">
                                <i class="mdi mdi-podcast text-danger"></i>
                                <span><strong>400K+</strong> Listeners &amp; Global Reach</span>
                            </div>
                        </div>
                    </div><!--end col-->
                </div><!--end row-->
            </div><!--end container-->

            <!-- Dual Floating Marquee Rows (Left & Right Transition) -->
            <div class="home-marquee-wrapper" id="homeMarqueeWrapper" title="Hover to pause marquee transition">
                <!-- Track 1: Drifts Left -->
                <div class="home-marquee-track home-marquee-track-left">
                    {row1_html}
                    {row1_html}
                </div>
                <!-- Track 2: Drifts Right -->
                <div class="home-marquee-track home-marquee-track-right mt-2">
                    {row2_html}
                    {row2_html}
                </div>
            </div>

            <div class="container">
                <!-- Interactive Filter Tabs -->
                <div class="row">
                    <div class="col-12">
                        <div class="home-news-filter-bar">
                            <button type="button" class="home-news-filter-btn active" onclick="filterHomeCarousel('all', this)">
                                <i class="mdi mdi-star mr-1 text-warning"></i> All Featured ({len(carousel_items)})
                            </button>
                            <button type="button" class="home-news-filter-btn" onclick="filterHomeCarousel('press', this)">
                                <i class="mdi mdi-newspaper mr-1 text-primary"></i> Tier-1 Press
                            </button>
                            <button type="button" class="home-news-filter-btn" onclick="filterHomeCarousel('podcast', this)">
                                <i class="mdi mdi-podcast mr-1 text-danger"></i> Keynotes &amp; Podcasts
                            </button>
                            <button type="button" class="home-news-filter-btn" onclick="filterHomeCarousel('skydeck', this)">
                                <i class="mdi mdi-school mr-1 text-info"></i> Berkeley SkyDeck
                            </button>
                            <button type="button" class="home-news-filter-btn" onclick="filterHomeCarousel('blog', this)">
                                <i class="mdi mdi-code-braces mr-1 text-success"></i> Tech Blogs &amp; Papers
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Featured Media & Blog Carousel Slider -->
                <div class="row">
                    <div class="col-12 mt-2 pt-2">
                        <div id="customer-testi" class="owl-carousel owl-theme">
                            {carousel_cards_html}
                        </div>
                    </div>
                </div><!--end row-->

                <!-- Section Call to Action Buttons -->
                <div class="row mt-4 pt-3">
                    <div class="col-12 text-center">
                        <a href="page-media" class="btn btn-primary rounded font-weight-bold px-4 py-2 mr-2 mb-2" style="background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%); border: none; box-shadow: 0 4px 14px rgba(37, 99, 235, 0.3);">
                            <i class="mdi mdi-newspaper-variant-outline mr-1"></i> Explore Full Media Hub (37+ Features) <i class="mdi mdi-arrow-right ml-1"></i>
                        </a>
                        <a href="page-publications" class="btn btn-outline-primary rounded font-weight-bold px-4 py-2 mr-2 mb-2">
                            <i class="mdi mdi-book-open-page-variant mr-1"></i> View Publications &amp; Patents
                        </a>
                        <a href="https://medium.com/@harshverma59" target="_blank" rel="noopener noreferrer" class="btn btn-outline-secondary rounded font-weight-bold px-4 py-2 mb-2">
                            <i class="mdi mdi-medium mr-1"></i> Read TechQuickie on Medium <i class="mdi mdi-open-in-new ml-1"></i>
                        </a>
                    </div>
                </div>
            </div><!--end container-->
        </section>
        <!-- Latest Tech News (TechQuickie), Media & Tech Blogs End -->
    '''
    return full_section

def apply_to_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    new_news_section = build_home_news_section()

    # Pattern to match from <!-- Blog Start --> or <section class="section bg-light" id="news"> to </section><!--end section --> or before <!-- Contact Start -->
    pattern = r'<!-- Blog Start -->[\s\S]*?<!--end section -->'
    if not re.search(pattern, html):
        pattern = r'<section class="section bg-light" id="news">[\s\S]*?</section>'
    
    if not re.search(pattern, html):
        print("ERROR: Could not find news section pattern in index.html")
        return False

    updated_html = re.sub(pattern, new_news_section.strip(), html, count=1)

    # Also add the filterHomeCarousel JS helper if not present
    js_helper = '''
            function filterHomeCarousel(category, btn) {
                var buttons = document.querySelectorAll('.home-news-filter-btn');
                buttons.forEach(function(b) { b.classList.remove('active'); });
                if (btn) btn.classList.add('active');

                var owl = $('#customer-testi');
                if (owl.length && typeof owl.data('owl.carousel') !== 'undefined') {
                    // Filter in owl carousel or toggle visibility
                    $('.home-news-carousel-item').each(function() {
                        var cardCat = $(this).attr('data-category');
                        if (category === 'all' || cardCat === category) {
                            $(this).closest('.owl-item').show();
                        } else {
                            // If user filtered, we can smoothly jump or highlight
                        }
                    });
                }
            }
    '''
    if 'filterHomeCarousel' not in updated_html:
        updated_html = updated_html.replace('function filterHomeAwards', js_helper + '\n            function filterHomeAwards')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(updated_html)

    print("index.html successfully updated with rich media & blog section and floating left/right transitions!")
    return True

if __name__ == '__main__':
    apply_to_index()
