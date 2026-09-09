#!/usr/bin/env python3
"""
Generates page-about.html for Harsh Verma's portfolio with full executive bio,
distinguished honors/awards, strategic pillars, and interactive 38-link verified profile hub.
"""

import json

PROFILE_LINKS = [
    # Category: councils (Executive, Councils & Global Honors)
    {
        "id": "forbes-council",
        "category": "councils",
        "categoryLabel": "Executive & Tech Councils",
        "name": "Forbes Technology Council",
        "identifier": "Official Council Member",
        "url": "https://councils.forbes.com/profile/Harsh-Verma-Principal-Software-Engineer-AI-Palo-Alto-Networks/2a1e2c7a-5541-4c49-acee-0ec37da532a5",
        "icon": "mdi-alpha-f-circle",
        "badgeColor": "#111827",
        "tag": "Council Member",
        "description": "Executive profile on the Forbes Technology Council — an invitation-only organization for senior-level technology executives."
    },
    {
        "id": "forbes-people",
        "category": "councils",
        "categoryLabel": "Executive & Tech Councils",
        "name": "Forbes Author Directory",
        "identifier": "Forbes Contributor",
        "url": "https://www.forbes.com/councils/forbestechcouncil/people/harshverma/",
        "icon": "mdi-newspaper-variant-outline",
        "badgeColor": "#0f172a",
        "tag": "Forbes Author",
        "description": "Forbes contributor profile and published thought leadership on Agentic AI, AI Security, and Enterprise Architecture."
    },
    {
        "id": "forttuna-powerlist",
        "category": "councils",
        "categoryLabel": "Executive & Tech Councils",
        "name": "Forttuna Global 100 Power List (2026)",
        "identifier": "Power List Honoree",
        "url": "https://global100.forttuna.com/the-power-list-2026-honorees/profile?name=harsh-verma",
        "icon": "mdi-trophy-award",
        "badgeColor": "#d97706",
        "tag": "Global 100 Honoree",
        "description": "Recognized among the Forttuna Global 100 Power List 2026 honorees for outstanding global innovation and AI leadership."
    },
    {
        "id": "forttuna-council",
        "category": "councils",
        "categoryLabel": "Executive & Tech Councils",
        "name": "Forttuna Technology Council",
        "identifier": "Council Member",
        "url": "https://councils.forttuna.com/council-member/harsh-verma/",
        "icon": "mdi-shield-crown-outline",
        "badgeColor": "#b45309",
        "tag": "Council Member",
        "description": "Official Forttuna Technology Council member steering committee on next-gen enterprise technologies and scalable AI."
    },
    {
        "id": "marquis-whoswho",
        "category": "councils",
        "categoryLabel": "Executive & Tech Councils",
        "name": "Marquis Who's Who in America",
        "identifier": "Biographical Honoree",
        "url": "https://mbo.marquiswhoswho.com/Biography/4005428487/fav",
        "icon": "mdi-certificate-outline",
        "badgeColor": "#4338ca",
        "tag": "Who's Who in America",
        "description": "Official biographical inclusion in Marquis Who's Who in America for sustained contributions to artificial intelligence and engineering."
    },
    {
        "id": "rsac-expert",
        "category": "councils",
        "categoryLabel": "Executive & Tech Councils",
        "name": "RSA Conference (RSAC) Expert",
        "identifier": "Speaker & Cybersecurity Expert",
        "url": "https://www.rsaconference.com/experts/Harsh%20Verma",
        "icon": "mdi-shield-check-outline",
        "badgeColor": "#dc2626",
        "tag": "RSAC Expert",
        "description": "RSA Conference verified expert directory profile focusing on AI-driven cybersecurity, defensive AI, and agent governance."
    },

    # Category: research (Research, Academic & Citations)
    {
        "id": "google-scholar",
        "category": "research",
        "categoryLabel": "Research & Citations",
        "name": "Google Scholar",
        "identifier": "Scholar ID: zSt9oRMAAAAJ",
        "url": "https://scholar.google.com/citations?user=zSt9oRMAAAAJ&hl=en",
        "icon": "mdi-school",
        "badgeColor": "#2563eb",
        "tag": "Scholar Profile",
        "description": "Author citation profile indexing 22+ peer-reviewed papers across IEEE, cognitive ML, agentic AI, and cybersecurity."
    },
    {
        "id": "semantic-scholar",
        "category": "research",
        "categoryLabel": "Research & Citations",
        "name": "Semantic Scholar",
        "identifier": "Author ID: 145004805",
        "url": "https://www.semanticscholar.org/author/H.-Verma/145004805",
        "icon": "mdi-brain",
        "badgeColor": "#0284c7",
        "tag": "AI Citation Graph",
        "description": "Allen Institute for AI Semantic Scholar profile with automated citation graphs and influential research metrics."
    },
    {
        "id": "orcid",
        "category": "research",
        "categoryLabel": "Research & Citations",
        "name": "ORCID Registry",
        "identifier": "0000-0003-2134-2600",
        "url": "https://orcid.org/0000-0003-2134-2600",
        "icon": "mdi-identifier",
        "badgeColor": "#16a34a",
        "tag": "Verified ORCID",
        "description": "Persistent digital identifier connecting validated research outputs, IEEE publications, and academic affiliations."
    },
    {
        "id": "openreview",
        "category": "research",
        "categoryLabel": "Research & Citations",
        "name": "OpenReview Profile",
        "identifier": "ID: ~Harsh_Verma3",
        "url": "https://openreview.net/profile?id=%7EHarsh_Verma3",
        "icon": "mdi-file-eye-outline",
        "badgeColor": "#8b5cf6",
        "tag": "Peer Review ID",
        "description": "Open scientific peer-review platform profile for machine learning research evaluations and academic submissions."
    },
    {
        "id": "researchgate",
        "category": "research",
        "categoryLabel": "Research & Citations",
        "name": "ResearchGate",
        "identifier": "Harsh-Verma-43",
        "url": "https://www.researchgate.net/profile/Harsh-Verma-43",
        "icon": "mdi-flask-outline",
        "badgeColor": "#059669",
        "tag": "Research Network",
        "description": "Scientific network profile showcasing preprints, publications, citation metrics, and collaborative research projects."
    },
    {
        "id": "ssrn",
        "category": "research",
        "categoryLabel": "Research & Citations",
        "name": "SSRN (Elsevier)",
        "identifier": "Author ID: 11144549",
        "url": "https://papers.ssrn.com/sol3/cf_dev/AbsByAuth.cfm?per_id=11144549",
        "icon": "mdi-file-document-outline",
        "badgeColor": "#ea580c",
        "tag": "Elsevier SSRN",
        "description": "Social Science Research Network author repository featuring papers on technology strategy, economics of AI, and cyber systems."
    },
    {
        "id": "ijsrm",
        "category": "research",
        "categoryLabel": "Research & Citations",
        "name": "IJSRM Journal Author",
        "identifier": "harshverma59",
        "url": "https://ijsrm.net/author/harshverma59",
        "icon": "mdi-book-open-outline",
        "badgeColor": "#0284c7",
        "tag": "IJSRM Author",
        "description": "International Journal of Scientific Research and Management verified author page and published scholarly articles."
    },
    {
        "id": "academia-edu",
        "category": "research",
        "categoryLabel": "Research & Citations",
        "name": "Academia.edu",
        "identifier": "Stanford GSB / harshverma",
        "url": "https://mygsb.academia.edu/harshverma",
        "icon": "mdi-school-outline",
        "badgeColor": "#4f46e5",
        "tag": "Academic Profile",
        "description": "Academic repository profile sharing research papers, case studies, and engineering briefs."
    },

    # Category: developer (Developer, Cloud & AI Ecosystems)
    {
        "id": "google-dev",
        "category": "developer",
        "categoryLabel": "Developer & Cloud Ecosystems",
        "name": "Google Developer Profile",
        "identifier": "u/harshverma59",
        "url": "https://me.developers.google.com/u/harshverma59",
        "icon": "mdi-google",
        "badgeColor": "#4285f4",
        "tag": "Google Developer",
        "description": "Official Google Developer profile tracking Cloud certifications, Gemini/Vertex AI badges, and ecosystem contributions."
    },
    {
        "id": "google-gdg",
        "category": "developer",
        "categoryLabel": "Developer & Cloud Ecosystems",
        "name": "Google Developer Group (GDG)",
        "identifier": "Community Lead / Speaker",
        "url": "https://gdg.community.dev/u/mn4snq/#/about",
        "icon": "mdi-google-circles-communities",
        "badgeColor": "#34a853",
        "tag": "GDG Community",
        "description": "GDG community profile for tech talks, developer workshops, and Google Cloud AI mentorship events."
    },
    {
        "id": "google-skills",
        "category": "developer",
        "categoryLabel": "Developer & Cloud Ecosystems",
        "name": "Google Skills Hub",
        "identifier": "skills.google",
        "url": "https://www.skills.google/",
        "icon": "mdi-cloud-check-outline",
        "badgeColor": "#fbbc05",
        "tag": "Google Cloud Skills",
        "description": "Google Cloud and GenAI engineering learning path accreditations and technical badges."
    },
    {
        "id": "github",
        "category": "developer",
        "categoryLabel": "Developer & Cloud Ecosystems",
        "name": "GitHub",
        "identifier": "iamharshverma",
        "url": "https://github.com/iamharshverma",
        "icon": "mdi-github",
        "badgeColor": "#181717",
        "tag": "Open Source Code",
        "description": "Open-source repositories, AI toolkits, agent frameworks, and distributed cloud computing code samples."
    },
    {
        "id": "devpost",
        "category": "developer",
        "categoryLabel": "Developer & Cloud Ecosystems",
        "name": "Devpost Profile",
        "identifier": "harshverma59",
        "url": "https://devpost.com/harshverma59",
        "icon": "mdi-code-braces",
        "badgeColor": "#003e54",
        "tag": "Hackathons & Builds",
        "description": "Portfolio of hackathon projects, prototype builds, and competitive engineering innovation submissions."
    },
    {
        "id": "substack",
        "category": "developer",
        "categoryLabel": "Developer & Cloud Ecosystems",
        "name": "Substack Newsletter",
        "identifier": "@aiwithharsh",
        "url": "https://substack.com/@aiwithharsh",
        "icon": "mdi-email-newsletter",
        "badgeColor": "#ff6719",
        "tag": "AI with Harsh",
        "description": "Author newsletter covering autonomous agent architectures, AI cybersecurity, and enterprise engineering practices."
    },
    {
        "id": "medium",
        "category": "developer",
        "categoryLabel": "Developer & Cloud Ecosystems",
        "name": "Medium Publications",
        "identifier": "@harshverma59",
        "url": "https://medium.com/@harshverma59",
        "icon": "mdi-medium",
        "badgeColor": "#000000",
        "tag": "Technical Blog",
        "description": "Articles breaking down complex machine learning systems, multi-agent frameworks, and real-time distributed data pipelines."
    },
    {
        "id": "hackernoon",
        "category": "developer",
        "categoryLabel": "Developer & Cloud Ecosystems",
        "name": "HackerNoon Tech Contributor",
        "identifier": "@harshverma59",
        "url": "https://hackernoon.com/u/harshverma59",
        "icon": "mdi-xml",
        "badgeColor": "#00ff00",
        "tag": "HackerNoon Author",
        "description": "Technical Council author profile publishing analyses on LLM agent security, AI reliability, and enterprise cloud tooling."
    },

    # Category: media (Media Features, Press & Filmography)
    {
        "id": "ny-weekly-journal",
        "category": "media",
        "categoryLabel": "Media Features & Press",
        "name": "New York Weekly Journal",
        "identifier": "Press Feature",
        "url": "https://nyweeklyjournal.com/blog/the-engineer-rewriting-the-rules-by-thinking-%E2%80%9Cai-beyond-the-code%E2%80%9D-inside-the-world-of-harsh-verma",
        "icon": "mdi-newspaper",
        "badgeColor": "#1e293b",
        "tag": "Press Spotlight",
        "description": "Special feature article: 'The Engineer Rewriting the Rules by Thinking AI Beyond the Code: Inside the World of Harsh Verma'."
    },
    {
        "id": "xraised-interview",
        "category": "media",
        "categoryLabel": "Media Features & Press",
        "name": "xRaised Global Interview Series",
        "identifier": "Video Episode",
        "url": "https://xraised.com/videos/ai-engineering-beyond-code/",
        "icon": "mdi-video-vintage",
        "badgeColor": "#7c3aed",
        "tag": "Global Video Feature",
        "description": "Featured video interview discussing AI Engineering beyond code, autonomous system design, and the future of tech careers."
    },
    {
        "id": "influencer-magazine",
        "category": "media",
        "categoryLabel": "Media Features & Press",
        "name": "Influencer Magazine UK",
        "identifier": "Tech Leader Spotlight",
        "url": "https://influencermagazine.uk/harsh-verma/",
        "icon": "mdi-bullhorn-outline",
        "badgeColor": "#ec4899",
        "tag": "UK Media Feature",
        "description": "Executive profile spotlighting Harsh's trajectory in AI innovation, thought leadership, and global business impact."
    },
    {
        "id": "lifepage",
        "category": "media",
        "categoryLabel": "Media Features & Press",
        "name": "LifePage India Career Talk",
        "identifier": "Career Interview",
        "url": "https://www.lifepage.in/page/harsh",
        "icon": "mdi-account-voice",
        "badgeColor": "#059669",
        "tag": "Career Mentorship",
        "description": "In-depth career interview sharing insights on the software development lifecycle, AI skills, and engineering guidance."
    },
    {
        "id": "imdb",
        "category": "media",
        "categoryLabel": "Media Features & Press",
        "name": "IMDb Profile",
        "identifier": "imdb.me/harshverma",
        "url": "https://imdb.me/harshverma",
        "icon": "mdi-movie-open-outline",
        "badgeColor": "#f5c518",
        "tag": "Official IMDb",
        "description": "Official IMDb profile cataloging technology podcast appearances, video series, and media credits."
    },

    # Category: advisory (Advisory, Mentorship & Accelerators)
    {
        "id": "adplist",
        "category": "advisory",
        "categoryLabel": "Advisory & Mentorship",
        "name": "ADPList Executive Mentor",
        "identifier": "Top AI Mentor",
        "url": "https://adplist.org/mentors/harsh-verma",
        "icon": "mdi-account-group-outline",
        "badgeColor": "#2563eb",
        "tag": "ADPList Mentor",
        "description": "Top-rated mentor on ADPList providing 1-on-1 career guidance to engineers, AI practitioners, and tech leaders globally."
    },
    {
        "id": "masschallenge",
        "category": "advisory",
        "categoryLabel": "Advisory & Mentorship",
        "name": "MassChallenge Accelerator",
        "identifier": "Mentor & Judge",
        "url": "https://accelerate.masschallenge.org/profile/",
        "icon": "mdi-rocket-launch-outline",
        "badgeColor": "#9333ea",
        "tag": "Startup Accelerator",
        "description": "Mentor and innovation judge for the global MassChallenge startup accelerator supporting high-impact AI ventures."
    },
    {
        "id": "f6s",
        "category": "advisory",
        "categoryLabel": "Advisory & Mentorship",
        "name": "F6S Startup Community",
        "identifier": "harshverma59",
        "url": "https://www.f6s.com/harshverma59",
        "icon": "mdi-handshake-outline",
        "badgeColor": "#1e40af",
        "tag": "F6S Founder Network",
        "description": "F6S profile connecting with founders, early-stage AI startups, accelerator programs, and venture ecosystems."
    },
    {
        "id": "founders-creative",
        "category": "advisory",
        "categoryLabel": "Advisory & Mentorship",
        "name": "Founders Creative",
        "identifier": "harsh",
        "url": "https://www.founderscreative.org/author/harsh/",
        "icon": "mdi-lightbulb-on-outline",
        "badgeColor": "#0284c7",
        "tag": "Founders Advisor",
        "description": "Author and advisory contributor helping early-stage founders scale technology roadmaps and architect AI solutions."
    },

    # Category: direct (Direct Connect & Professional Networks)
    {
        "id": "harshverma-bio",
        "category": "direct",
        "categoryLabel": "Direct Connect & Networks",
        "name": "HarshVerma.bio",
        "identifier": "Universal Bio Hub",
        "url": "https://harshverma.bio/",
        "icon": "mdi-link-variant",
        "badgeColor": "#3b82f6",
        "tag": "Official Bio Hub",
        "description": "Centralized universal bio link aggregating all books, speaking engagements, newsletters, and verified profiles."
    },
    {
        "id": "linkedin",
        "category": "direct",
        "categoryLabel": "Direct Connect & Networks",
        "name": "LinkedIn Profile",
        "identifier": "in/harshverma59",
        "url": "https://www.linkedin.com/in/harshverma59/",
        "icon": "mdi-linkedin",
        "badgeColor": "#0a66c2",
        "tag": "Primary Professional",
        "description": "Principal Software Engineer in AI at Palo Alto Networks. Connect for industry insights, advisory, and keynote speaking."
    },
    {
        "id": "instagram",
        "category": "direct",
        "categoryLabel": "Direct Connect & Networks",
        "name": "Instagram",
        "identifier": "@aiwithharsh",
        "url": "https://www.instagram.com/aiwithharsh",
        "icon": "mdi-instagram",
        "badgeColor": "#e1306c",
        "tag": "Visual AI Insights",
        "description": "Daily bite-sized AI architecture breakdowns, book previews, speaking event highlights, and tech updates."
    },
    {
        "id": "favikon",
        "category": "direct",
        "categoryLabel": "Direct Connect & Networks",
        "name": "Favikon Creator Spotlight",
        "identifier": "harshverma59",
        "url": "https://spotlight.favikon.com/harshverma59/",
        "icon": "mdi-star-shooting-outline",
        "badgeColor": "#f59e0b",
        "tag": "Creator Ranking",
        "description": "Favikon creator spotlight scoring ranking top influential creators and thought leaders in Artificial Intelligence."
    },
    {
        "id": "mediakit",
        "category": "direct",
        "categoryLabel": "Direct Connect & Networks",
        "name": "Media Kit & Speaker Bio",
        "identifier": "@harshverma59",
        "url": "https://mediakit.bio/@harshverma59",
        "icon": "mdi-card-account-details-outline",
        "badgeColor": "#6366f1",
        "tag": "Press & Speaker Kit",
        "description": "Official media kit with high-res headshots, keynote topics, speaking rider, and executive background briefs."
    },
    {
        "id": "rocketreach",
        "category": "direct",
        "categoryLabel": "Direct Connect & Networks",
        "name": "RocketReach Enterprise Verification",
        "identifier": "Palo Alto Networks",
        "url": "https://rocketreach.co/harsh-verma-email_54769519",
        "icon": "mdi-domain",
        "badgeColor": "#0284c7",
        "tag": "Enterprise Directory",
        "description": "Verified executive contact and professional record at Palo Alto Networks on RocketReach."
    },
    {
        "id": "contactout",
        "category": "direct",
        "categoryLabel": "Direct Connect & Networks",
        "name": "ContactOut Profile",
        "identifier": "Harsh-Verma-1722953",
        "url": "https://contactout.com/Harsh-Verma-1722953",
        "icon": "mdi-contacts",
        "badgeColor": "#10b981",
        "tag": "Professional Contact",
        "description": "ContactOut verified professional profile and enterprise AI engineering network directory."
    }
]

def generate_profile_card_html(link):
    category_slug = link["category"]
    data_search = f"{link['name']} {link['identifier']} {link['tag']} {link['description']} {link['categoryLabel']}".lower()
    
    return f"""
    <div class="col-lg-4 col-md-6 mb-4 profile-card-item" data-category="{category_slug}" data-search="{data_search}">
        <div class="profile-hub-card h-100">
            <div class="d-flex justify-content-between align-items-start mb-3">
                <div class="d-flex align-items-center">
                    <div class="profile-card-icon-wrap mr-3">
                        <i class="mdi {link['icon']}"></i>
                    </div>
                    <div>
                        <span class="profile-category-pill">{link['categoryLabel']}</span>
                        <h5 class="profile-card-title mb-0 mt-1">{link['name']}</h5>
                    </div>
                </div>
            </div>
            
            <div class="profile-card-identifier mb-2">
                <span class="badge badge-light border font-weight-bold text-dark px-2 py-1">
                    <i class="mdi mdi-check-circle text-primary mr-1"></i> {link['identifier']}
                </span>
            </div>

            <p class="profile-card-desc mb-3">{link['description']}</p>

            <div class="d-flex align-items-center justify-content-between pt-3 border-top mt-auto">
                <a href="{link['url']}" target="_blank" class="btn-hub-action btn-hub-primary" title="Visit {link['name']}">
                    <i class="mdi mdi-open-in-new mr-1"></i> Open Profile
                </a>
                <button type="button" class="btn-hub-action btn-hub-outline" onclick="copyLinkUrl('{link['url']}', '{link['name']}')" title="Copy URL">
                    <i class="mdi mdi-content-copy mr-1"></i> Copy Link
                </button>
            </div>
        </div>
    </div>
    """

def generate_html():
    cards_html = "\n".join([generate_profile_card_html(link) for link in PROFILE_LINKS])
    links_json_str = json.dumps(PROFILE_LINKS)

    html_content = f"""<!DOCTYPE html>
<html lang="en">

<head>
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-30250521-4"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){{dataLayer.push(arguments);}}
        gtag('js', new Date());
        gtag('config', 'UA-30250521-4');
    </script>
    <meta charset="UTF-8">
    <title>About Harsh Verma | Principal AI Engineer, Author & Advisor</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Biography, leadership profile, honors, and verified digital presence of Harsh Verma — Principal Software Engineer in AI at Palo Alto Networks, Forbes Technology Council Member, IEEE Senior Member, and Author." />
    <meta name="keywords" content="Harsh Verma, About Harsh Verma, Principal AI Engineer, Palo Alto Networks, Forbes Technology Council, IEEE Senior Member, Global Recognition Award, UC Berkeley Skydeck, AI Leadership, Agentic AI" />
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
        /* Executive About Page Styling */
        .about-page-environment {{
            background-color: #f8fafc;
            background-image: 
                radial-gradient(circle at 10% 10%, rgba(37, 99, 235, 0.05) 0%, transparent 40%),
                radial-gradient(circle at 90% 40%, rgba(2, 132, 199, 0.06) 0%, transparent 45%),
                radial-gradient(circle at 50% 90%, rgba(59, 130, 246, 0.04) 0%, transparent 50%);
            min-height: 100vh;
        }}

        /* Executive Hero Header */
        .about-hero-card {{
            background: linear-gradient(135deg, #070c18 0%, #0f172a 45%, #1e3a8a 100%);
            border-radius: 20px;
            color: #ffffff;
            padding: 40px;
            box-shadow: 0 16px 40px rgba(11, 17, 32, 0.3);
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(59, 130, 246, 0.25);
            margin-bottom: 36px;
        }}
        .about-hero-card::before {{
            content: "";
            position: absolute;
            top: -50%;
            right: -20%;
            width: 500px;
            height: 500px;
            background: radial-gradient(circle, rgba(59, 130, 246, 0.25) 0%, rgba(14, 165, 233, 0.15) 45%, transparent 70%);
            border-radius: 50%;
            pointer-events: none;
        }}

        .portrait-frame {{
            position: relative;
            border-radius: 18px;
            overflow: hidden;
            box-shadow: 0 12px 32px rgba(0, 0, 0, 0.35);
            border: 3px solid rgba(255, 255, 255, 0.15);
            max-width: 320px;
            margin: 0 auto;
        }}
        .portrait-frame img {{
            width: 100%;
            height: auto;
            display: block;
            object-fit: cover;
            transition: transform 0.4s ease;
        }}
        .portrait-frame:hover img {{
            transform: scale(1.03);
        }}

        .hero-badge-pill {{
            background: rgba(37, 99, 235, 0.2);
            color: #93c5fd;
            border: 1px solid rgba(59, 130, 246, 0.4);
            padding: 5px 12px;
            border-radius: 30px;
            font-size: 12.5px;
            font-weight: 700;
            display: inline-flex;
            align-items: center;
            margin-right: 8px;
            margin-bottom: 8px;
        }}
        .hero-badge-pill i {{
            margin-right: 5px;
        }}

        /* Biography Section Card */
        .executive-bio-box {{
            background: #ffffff;
            border-radius: 16px;
            border: 1px solid #e2e8f0;
            padding: 36px;
            box-shadow: 0 4px 24px rgba(15, 23, 42, 0.05);
            margin-bottom: 36px;
        }}
        .executive-bio-p {{
            font-size: 16px;
            line-height: 1.8;
            color: #334155;
            margin-bottom: 20px;
        }}
        .executive-bio-p:last-child {{
            margin-bottom: 0;
        }}

        /* Honors & Awards Cards */
        .award-highlight-card {{
            background: #ffffff;
            border-radius: 14px;
            border: 1px solid #e2e8f0;
            padding: 24px;
            height: 100%;
            transition: all 0.25s ease;
            box-shadow: 0 4px 16px rgba(15, 23, 42, 0.03);
        }}
        .award-highlight-card:hover {{
            border-color: #2563eb;
            transform: translateY(-3px);
            box-shadow: 0 10px 28px rgba(37, 99, 235, 0.09);
        }}
        .award-icon-box {{
            width: 48px;
            height: 48px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            margin-bottom: 16px;
        }}

        /* Strategic Focus Pillars */
        .pillar-card {{
            background: #f8fafc;
            border-radius: 14px;
            border: 1px solid #e2e8f0;
            padding: 22px;
            height: 100%;
            transition: all 0.25s ease;
        }}
        .pillar-card:hover {{
            background: #ffffff;
            border-color: #3b82f6;
            box-shadow: 0 8px 24px rgba(59, 130, 246, 0.08);
            transform: translateY(-2px);
        }}

        /* Interactive Profile Hub Cards */
        .profile-hub-box {{
            background: #ffffff;
            border-radius: 16px;
            border: 1px solid #e2e8f0;
            padding: 34px;
            box-shadow: 0 4px 24px rgba(15, 23, 42, 0.04);
            margin-bottom: 36px;
        }}
        .profile-search-input-wrap {{
            position: relative;
            width: 100%;
        }}
        .profile-search-input-wrap i {{
            position: absolute;
            left: 16px;
            top: 50%;
            transform: translateY(-50%);
            font-size: 20px;
            color: #94a3b8;
        }}
        .profile-search-input {{
            width: 100%;
            padding: 12px 18px 12px 48px;
            border-radius: 10px;
            border: 1px solid #cbd5e1;
            font-size: 14.5px;
            transition: border-color 0.2s ease, box-shadow 0.2s ease;
            background: #f8fafc;
        }}
        .profile-search-input:focus {{
            outline: none;
            border-color: #2563eb;
            background: #ffffff;
            box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15);
        }}

        .filter-btn-pill {{
            border: 1px solid #cbd5e1;
            background: #ffffff;
            color: #475569;
            padding: 7px 15px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 600;
            margin-right: 8px;
            margin-bottom: 8px;
            transition: all 0.2s ease;
            cursor: pointer;
        }}
        .filter-btn-pill:hover {{
            background: #f1f5f9;
            border-color: #94a3b8;
            color: #0f172a;
        }}
        .filter-btn-pill.active {{
            background: #2563eb;
            color: #ffffff;
            border-color: #2563eb;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25);
        }}

        .profile-hub-card {{
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 14px;
            padding: 22px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: all 0.25s ease;
            height: 100%;
        }}
        .profile-hub-card:hover {{
            background: #ffffff;
            border-color: #2563eb;
            transform: translateY(-3px);
            box-shadow: 0 8px 24px rgba(37, 99, 235, 0.08);
        }}
        .profile-card-icon-wrap {{
            width: 44px;
            height: 44px;
            border-radius: 10px;
            background: rgba(37, 99, 235, 0.1);
            color: #2563eb;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 22px;
            flex-shrink: 0;
        }}
        .profile-category-pill {{
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: #64748b;
        }}
        .profile-card-title {{
            font-size: 15.5px;
            font-weight: 700;
            color: #0f172a;
            line-height: 1.35;
        }}
        .profile-card-desc {{
            font-size: 13.5px;
            color: #475569;
            line-height: 1.55;
        }}

        .btn-hub-action {{
            padding: 6px 13px;
            border-radius: 8px;
            font-size: 12.5px;
            font-weight: 600;
            text-decoration: none !important;
            transition: all 0.2s ease;
            display: inline-flex;
            align-items: center;
            border: 1px solid transparent;
            cursor: pointer;
        }}
        .btn-hub-primary {{
            background: #2563eb;
            color: #ffffff !important;
        }}
        .btn-hub-primary:hover {{
            background: #1d4ed8;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25);
        }}
        .btn-hub-outline {{
            background: #ffffff;
            color: #475569 !important;
            border-color: #cbd5e1;
        }}
        .btn-hub-outline:hover {{
            background: #f1f5f9;
            color: #0f172a !important;
            border-color: #94a3b8;
        }}

        /* Dark mode overrides */
        body.dark-mode .about-page-environment {{
            background-color: #080d1a;
            background-image: 
                radial-gradient(circle at 10% 10%, rgba(37, 99, 235, 0.1) 0%, transparent 40%),
                radial-gradient(circle at 90% 40%, rgba(2, 132, 199, 0.08) 0%, transparent 45%),
                radial-gradient(circle at 50% 90%, rgba(59, 130, 246, 0.06) 0%, transparent 50%);
        }}
        body.dark-mode .executive-bio-box,
        body.dark-mode .award-highlight-card,
        body.dark-mode .profile-hub-box {{
            background: #111827;
            border-color: #1f2937;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.4);
        }}
        body.dark-mode .executive-bio-p {{
            color: #cbd5e1;
        }}
        body.dark-mode .pillar-card,
        body.dark-mode .profile-hub-card {{
            background: #1a2234;
            border-color: #243048;
        }}
        body.dark-mode .pillar-card:hover,
        body.dark-mode .profile-hub-card:hover {{
            background: #1f293d;
            border-color: #3b82f6;
        }}
        body.dark-mode .profile-card-title {{
            color: #f3f4f6;
        }}
        body.dark-mode .profile-card-desc {{
            color: #94a3b8;
        }}
        body.dark-mode .profile-search-input {{
            background: #1f2937;
            border-color: #374151;
            color: #f3f4f6;
        }}
        body.dark-mode .profile-search-input:focus {{
            background: #111827;
            border-color: #3b82f6;
        }}
        body.dark-mode .filter-btn-pill {{
            background: #1f2937;
            border-color: #374151;
            color: #cbd5e1;
        }}
        body.dark-mode .filter-btn-pill:hover {{
            background: #374151;
            color: #ffffff;
        }}
        body.dark-mode .filter-btn-pill.active {{
            background: #2563eb;
            color: #ffffff;
            border-color: #2563eb;
        }}
        body.dark-mode .btn-hub-outline {{
            background: #1f2937;
            color: #cbd5e1 !important;
            border-color: #374151;
        }}
        body.dark-mode .btn-hub-outline:hover {{
            background: #374151;
            color: #ffffff !important;
        }}
    </style>
</head>

<body>
    <!-- Navbar Start -->
    <nav class="navbar navbar-expand-lg fixed-top navbar-custom navbar-light sticky">
        <div class="container">
            <a class="navbar-brand" href="index">
                <span class="text-primary font-weight-bold" style="font-size: 22px; letter-spacing: -0.5px;">Harsh Verma</span>
            </a>

            <div class="d-flex align-items-center d-lg-none">
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
                    <li class="nav-item active">
                        <a class="nav-link" href="page-about">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="page-events">Speaking Engagements</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="page-publications">Publications</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="page-books">Books</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="page-portfolio">Portfolio</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="page-blog">Blog</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="index#contact">Contact</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="javascript:void(0)" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">More
                        </a>
                        <div class="dropdown-menu rounded m-0" aria-labelledby="navbarDropdown">
                            <div class="container ml-0 ml-md-0">
                                <div class="row">
                                    <div class="col-md-12">
                                        <a class="dropdown-item" href="page-about">Biography &amp; Profiles</a>
                                        <a class="dropdown-item" href="page-events">Speaking Engagements</a>
                                        <a class="dropdown-item" href="page-books">Authored Books</a>
                                        <a class="dropdown-item" href="page-publications">Publications &amp; Research</a>
                                        <a class="dropdown-item" href="page-portfolio">Portfolio Projects</a>
                                        <a class="dropdown-item" href="page-blog">Blog &amp; Articles</a>
                                        <a class="dropdown-item" href="https://scholar.google.com/citations?hl=en&user=zSt9oRMAAAAJ" target="_blank">Google Scholar Profile <i class="mdi mdi-open-in-new ml-1"></i></a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </li>
                </ul>

                <ul class="top-right text-right list-unstyled list-inline mb-0 mt-2 mt-sm-0 nav-social d-flex align-items-center justify-content-end">
                    <li class="list-inline-item mr-2"><a href="https://scholar.google.com/citations?hl=en&user=zSt9oRMAAAAJ" target="_blank" title="Google Scholar Profile"><i class="mdi mdi-school"></i></a></li>
                    <li class="list-inline-item mr-2"><a href="https://www.linkedin.com/in/harshverma59/" target="_blank" title="LinkedIn Profile"><i class="mdi mdi-linkedin"></i></a></li>
                    <li class="list-inline-item mr-2"><a href="https://github.com/iamharshverma" target="_blank" title="GitHub Profile"><i class="mdi mdi-github-face"></i></a></li>
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

    <!-- Main Content Start -->
    <section class="section about-page-environment" style="padding-top: 130px; padding-bottom: 60px;">
        <div class="container">
            
            <!-- Hero Header Start -->
            <div class="row">
                <div class="col-12">
                    <div class="about-hero-card">
                        <div class="row align-items-center">
                            <div class="col-lg-4 text-center mb-4 mb-lg-0">
                                <div class="portrait-frame">
                                    <img src="images/SectaAI_BTRPHBqq~2.jpg" alt="Harsh Verma - Principal Software Engineer in AI">
                                </div>
                            </div>
                            <div class="col-lg-8">
                                <div class="pl-lg-3">
                                    <div class="d-flex flex-wrap align-items-center mb-2">
                                        <span class="hero-badge-pill" style="background: rgba(14, 165, 233, 0.25); border-color: rgba(14, 165, 233, 0.5); color: #38bdf8;">
                                            <i class="mdi mdi-shield-check"></i> Principal AI Engineer @ Palo Alto Networks
                                        </span>
                                        <span class="hero-badge-pill">
                                            <i class="mdi mdi-certificate"></i> IEEE Senior Member
                                        </span>
                                        <span class="hero-badge-pill" style="background: rgba(234, 179, 8, 0.2); border-color: rgba(234, 179, 8, 0.5); color: #fde047;">
                                            <i class="mdi mdi-trophy"></i> Global Recognition Award 2026
                                        </span>
                                        <span class="hero-badge-pill">
                                            <i class="mdi mdi-domain"></i> Forbes Technology Council
                                        </span>
                                    </div>

                                    <h1 class="font-weight-bold text-white mb-2" style="font-size: 2.5rem; letter-spacing: -0.5px;">Harsh Verma</h1>
                                    <p class="lead text-white-50 mb-3" style="font-size: 1.15rem; line-height: 1.5;">
                                        Advancing Autonomous Agent Systems, AI Security & Responsible Enterprise Scale
                                    </p>

                                    <div class="row text-center mt-3 pt-3 border-top" style="border-color: rgba(255,255,255,0.1) !important;">
                                        <div class="col-4 col-md-3 mb-2">
                                            <h4 class="font-weight-bold text-white mb-0">12+</h4>
                                            <small class="text-white-50 font-weight-bold">Years in AI/Tech</small>
                                        </div>
                                        <div class="col-4 col-md-3 mb-2">
                                            <h4 class="font-weight-bold text-white mb-0">22+</h4>
                                            <small class="text-white-50 font-weight-bold">Published Papers</small>
                                        </div>
                                        <div class="col-4 col-md-3 mb-2">
                                            <h4 class="font-weight-bold text-white mb-0">6</h4>
                                            <small class="text-white-50 font-weight-bold">Patents (1 Granted, 4 In Process)</small>
                                        </div>
                                        <div class="col-12 col-md-3 mb-2 mt-2 mt-md-0 d-flex align-items-center justify-content-center">
                                            <a href="https://www.linkedin.com/in/harshverma59/" target="_blank" class="btn btn-primary btn-sm rounded font-weight-bold px-3 w-100" style="background: linear-gradient(135deg, #2563eb 0%, #0284c7 100%); border: none;">
                                                <i class="mdi mdi-linkedin mr-1"></i> Connect
                                            </a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- Hero Header End -->

            <!-- Executive Biography Box -->
            <div class="row">
                <div class="col-12">
                    <div class="executive-bio-box">
                        <div class="d-flex align-items-center mb-4">
                            <span class="badge badge-pill text-white px-3 py-1 font-weight-bold mr-2" style="background: linear-gradient(135deg, #2563eb 0%, #0284c7 100%);">
                                <i class="mdi mdi-account-card-details-outline mr-1"></i> Executive Biography
                            </span>
                            <h2 class="font-weight-bold text-dark mb-0 ml-2" style="font-size: 1.6rem;">About Harsh Verma</h2>
                        </div>

                        <div class="executive-bio-content">
                            <p class="executive-bio-p">
                                Harsh Verma is a Principal Software Engineer in AI at Palo Alto Networks, focused on advancing autonomous agent systems and intelligent AI strategies. Harsh is also a Forbes Technology Council member and, as a speaker, mentor, and advisor, he brings both technical depth and strategic guidance to leaders adopting next-generation AI capabilities. He drives responsible, scalable AI adoption. His work influences how enterprises innovate, secure, and operationalize the next generation of intelligent systems. Harsh specializes in offering scalable AI solutions, mentoring aspiring entrepreneurs, delivering impactful conference talks, and advising startups on their AI strategies. Whether it's navigating AI implementation or fostering innovation with AI, Harsh is committed to delivering meaningful results in the tech industry.
                            </p>
                            <p class="executive-bio-p">
                                His contributions have been recognized through globally respected awards and institutions, reinforcing both impact and influence. He is a recipient of the Global Recognition Award (2026) for measurable advances in enterprise AI and cybersecurity, and also the Globee Awards, which recognize excellence &amp; innovation across global business leadership. He acts as a Senior Member of IEEE, which reflects peer-reviewed recognition of his sustained technical and professional contributions to the field, an honor reserved for individuals demonstrating significant performance and impact.
                            </p>
                            <p class="executive-bio-p">
                                Beyond the enterprise, Harsh plays a visible role in shaping the broader Data &amp; AI ecosystem. Through advising and mentorship at leading accelerators, UC Berkeley Skydeck, judging global AI innovation forums, and publishing thought leadership in Forbes and Hackernoon as a Technical Council Member, he contributes to defining how AI leadership itself is evolving. His work influences not only the organizations he serves but also the next generation of AI systems, leaders, and standards.
                            </p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Strategic Pillars & Awards Row -->
            <div class="row mb-4">
                <!-- Honors & Accreditations -->
                <div class="col-lg-6 mb-4">
                    <div class="h-100 p-4 bg-white rounded shadow-sm border">
                        <div class="d-flex align-items-center mb-3">
                            <span class="badge badge-pill text-white px-3 py-1 font-weight-bold mr-2" style="background: linear-gradient(135deg, #d97706 0%, #b45309 100%);">
                                <i class="mdi mdi-trophy-outline mr-1"></i> Global Accreditations
                            </span>
                            <h3 class="font-weight-bold text-dark mb-0 ml-2" style="font-size: 1.3rem;">Honors &amp; Awards</h3>
                        </div>

                        <div class="row">
                            <div class="col-sm-6 mb-3">
                                <div class="award-highlight-card">
                                    <div class="award-icon-box" style="background: rgba(234, 179, 8, 0.15); color: #d97706;">
                                        <i class="mdi mdi-trophy-award"></i>
                                    </div>
                                    <h5 class="font-weight-bold text-dark mb-1" style="font-size: 15px;">Global Recognition Award (2026)</h5>
                                    <p class="text-muted mb-0" style="font-size: 13px; line-height: 1.5;">Honored for measurable advances in enterprise AI architectures and autonomous cybersecurity defense.</p>
                                </div>
                            </div>
                            <div class="col-sm-6 mb-3">
                                <div class="award-highlight-card">
                                    <div class="award-icon-box" style="background: rgba(37, 99, 235, 0.15); color: #2563eb;">
                                        <i class="mdi mdi-certificate"></i>
                                    </div>
                                    <h5 class="font-weight-bold text-dark mb-1" style="font-size: 15px;">Globee Business Awards</h5>
                                    <p class="text-muted mb-0" style="font-size: 13px; line-height: 1.5;">Recognized for excellence and innovation across global business leadership and technology acceleration.</p>
                                </div>
                            </div>
                            <div class="col-sm-6 mb-3 mb-sm-0">
                                <div class="award-highlight-card">
                                    <div class="award-icon-box" style="background: rgba(16, 185, 129, 0.15); color: #059669;">
                                        <i class="mdi mdi-shield-check"></i>
                                    </div>
                                    <h5 class="font-weight-bold text-dark mb-1" style="font-size: 15px;">Senior Member of IEEE</h5>
                                    <p class="text-muted mb-0" style="font-size: 13px; line-height: 1.5;">Peer-reviewed recognition of sustained technical performance and lasting contributions to IEEE disciplines.</p>
                                </div>
                            </div>
                            <div class="col-sm-6">
                                <div class="award-highlight-card">
                                    <div class="award-icon-box" style="background: rgba(124, 58, 237, 0.15); color: #7c3aed;">
                                        <i class="mdi mdi-domain"></i>
                                    </div>
                                    <h5 class="font-weight-bold text-dark mb-1" style="font-size: 15px;">Forbes Technology Council</h5>
                                    <p class="text-muted mb-0" style="font-size: 13px; line-height: 1.5;">Invitation-only council for senior technology executives; contributing author on next-generation AI systems.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Strategic Focus Pillars -->
                <div class="col-lg-6 mb-4">
                    <div class="h-100 p-4 bg-white rounded shadow-sm border">
                        <div class="d-flex align-items-center mb-3">
                            <span class="badge badge-pill text-white px-3 py-1 font-weight-bold mr-2" style="background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);">
                                <i class="mdi mdi-compass-outline mr-1"></i> Core Domains
                            </span>
                            <h3 class="font-weight-bold text-dark mb-0 ml-2" style="font-size: 1.3rem;">Strategic Expertise</h3>
                        </div>

                        <div class="row">
                            <div class="col-12 mb-3">
                                <div class="pillar-card">
                                    <div class="d-flex align-items-center mb-1">
                                        <i class="mdi mdi-robot mr-2 text-primary" style="font-size: 20px;"></i>
                                        <h5 class="font-weight-bold text-dark mb-0" style="font-size: 15px;">Autonomous Agent Systems &amp; Multi-Agent Workflows</h5>
                                    </div>
                                    <p class="text-muted mb-0" style="font-size: 13.5px; line-height: 1.55;">Engineering resilient, goal-oriented agentic topologies, tool-calling pipelines, self-healing runtime orchestration, and deterministic validation harnesses.</p>
                                </div>
                            </div>
                            <div class="col-12 mb-3">
                                <div class="pillar-card">
                                    <div class="d-flex align-items-center mb-1">
                                        <i class="mdi mdi-shield-lock-outline mr-2 text-success" style="font-size: 20px;"></i>
                                        <h5 class="font-weight-bold text-dark mb-0" style="font-size: 15px;">Enterprise AI Security &amp; Cyber Defense</h5>
                                    </div>
                                    <p class="text-muted mb-0" style="font-size: 13.5px; line-height: 1.55;">Pioneering defensive AI guardrails, proactive adversarial mitigation, data governance, and secure AI adoption strategies at Palo Alto Networks.</p>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="pillar-card">
                                    <div class="d-flex align-items-center mb-1">
                                        <i class="mdi mdi-rocket-launch-outline mr-2 text-warning" style="font-size: 20px;"></i>
                                        <h5 class="font-weight-bold text-dark mb-0" style="font-size: 15px;">Executive Advisory &amp; UC Berkeley SkyDeck Mentorship</h5>
                                    </div>
                                    <p class="text-muted mb-0" style="font-size: 13.5px; line-height: 1.55;">Advising high-growth startups, judging global AI innovation forums, and mentoring the next generation of engineers through ADPList and global accelerators.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Digital Presence & Verified Profiles Hub -->
            <div class="row">
                <div class="col-12">
                    <div class="profile-hub-box" id="verified-profiles">
                        <div class="d-flex flex-wrap justify-content-between align-items-center mb-4">
                            <div>
                                <span class="badge badge-pill text-white px-3 py-1 font-weight-bold mb-1" style="background: linear-gradient(135deg, #10b981 0%, #0284c7 100%);">
                                    <i class="mdi mdi-check-decagram mr-1"></i> Verified Digital Directory
                                </span>
                                <h2 class="font-weight-bold text-dark mb-0 mt-1" style="font-size: 1.5rem;">
                                    Verified Profiles &amp; Web Presence Hub <span class="badge badge-primary font-weight-bold ml-2">38 Profiles</span>
                                </h2>
                                <p class="text-muted mb-0 mt-1" style="font-size: 14px;">
                                    Explore Harsh Verma's verified accreditations, executive councils, research indexes, developer ecosystems, and media features across the web.
                                </p>
                            </div>
                            <a href="https://harshverma.bio/" target="_blank" class="btn btn-outline-primary btn-sm rounded font-weight-bold mt-3 mt-sm-0">
                                <i class="mdi mdi-link-variant mr-1"></i> Visit HarshVerma.bio <i class="mdi mdi-open-in-new ml-1"></i>
                            </a>
                        </div>

                        <!-- Search & Category Filters -->
                        <div class="row mb-4">
                            <div class="col-lg-5 mb-3 mb-lg-0">
                                <div class="profile-search-input-wrap">
                                    <i class="mdi mdi-magnify"></i>
                                    <input type="text" id="profileSearchInput" class="profile-search-input" placeholder="Search profiles by platform, topic, or ID (e.g., Forbes, Scholar, Google, RSAC)...">
                                </div>
                            </div>
                            <div class="col-lg-7">
                                <div class="d-flex flex-wrap align-items-center justify-content-lg-end" id="profileCategoryFilters">
                                    <button type="button" class="filter-btn-pill active" data-filter="all">All (38)</button>
                                    <button type="button" class="filter-btn-pill" data-filter="councils">Executive &amp; Councils</button>
                                    <button type="button" class="filter-btn-pill" data-filter="research">Research &amp; Citations</button>
                                    <button type="button" class="filter-btn-pill" data-filter="developer">Developer &amp; AI Hubs</button>
                                    <button type="button" class="filter-btn-pill" data-filter="media">Media &amp; Press</button>
                                    <button type="button" class="filter-btn-pill" data-filter="advisory">Advisory &amp; Mentorship</button>
                                    <button type="button" class="filter-btn-pill" data-filter="direct">Direct Connect</button>
                                </div>
                            </div>
                        </div>

                        <!-- Dynamic Profile Cards Grid -->
                        <div class="row" id="profileCardsGrid">
                            {cards_html}
                        </div>

                        <!-- Empty State Notice -->
                        <div id="noProfilesFound" class="text-center py-5 d-none">
                            <i class="mdi mdi-file-search-outline text-muted" style="font-size: 54px;"></i>
                            <h5 class="font-weight-bold text-dark mt-3 mb-1">No matching profiles found</h5>
                            <p class="text-muted mb-3" style="font-size: 14px;">Try searching for different keywords or clear your active category filter.</p>
                            <button type="button" class="btn btn-outline-primary btn-sm rounded font-weight-bold" onclick="resetProfileFilters()">
                                Reset Filters &amp; View All Profiles
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Navigation Quick CTAs -->
            <div class="row">
                <div class="col-md-6 mb-4">
                    <div class="p-4 bg-white rounded border shadow-sm h-100 d-flex flex-column justify-content-between">
                        <div>
                            <span class="badge badge-primary px-3 py-1 font-weight-bold mb-2">Authored Books</span>
                            <h4 class="font-weight-bold text-dark mb-2">Explore Books on AI Leadership &amp; Cyber Defense</h4>
                            <p class="text-muted" style="font-size: 14px;">Dive into "Beyond AI Engineering: From Creator to Curator" and "AI vs. AI: Engineering the Cybersecurity Counteroffensive".</p>
                        </div>
                        <div>
                            <a href="page-books" class="btn btn-primary btn-sm rounded font-weight-bold px-3">
                                Explore Authored Books <i class="mdi mdi-arrow-right ml-1"></i>
                            </a>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 mb-4">
                    <div class="p-4 bg-white rounded border shadow-sm h-100 d-flex flex-column justify-content-between">
                        <div>
                            <span class="badge badge-info text-white px-3 py-1 font-weight-bold mb-2">Research &amp; IP</span>
                            <h4 class="font-weight-bold text-dark mb-2">Browse 22+ Published Papers &amp; 6 Patents</h4>
                            <p class="text-muted" style="font-size: 14px;">Review peer-reviewed IEEE publications, CogML datasets, granted patents, and 4 in-process Palo Alto Networks patents on Agentic AI and Copilot Navigation.</p>
                        </div>
                        <div>
                            <a href="page-publications" class="btn btn-outline-primary btn-sm rounded font-weight-bold px-3">
                                Browse Publications &amp; Patents <i class="mdi mdi-arrow-right ml-1"></i>
                            </a>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </section>
    <!-- Main Content End -->

    <!-- Footer Start -->
    <footer class="footer bg-light">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-12 text-center">
                    <a href="index" class="footer-logo text-black font-weight-bold" style="font-size: 24px;">Harsh Verma</a>
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
    <a href="#" class="btn btn-icon btn-soft-primary back-to-top"><i data-feather="arrow-up" class="icons"></i></a>

    <!-- Javascript -->
    <script src="js/jquery.min.js"></script>
    <script src="js/bootstrap.bundle.min.js"></script>
    <script src="js/jquery.easing.min.js"></script>
    <script src="js/scrollspy.min.js"></script>
    <script src="js/feather.min.js"></script>
    <script src="js/app.js"></script>

    <script>
        // Interactive Profile Search and Filter Logic
        $(document).ready(function() {{
            if (typeof feather !== 'undefined') {{
                feather.replace();
            }}

            var currentCategory = "all";
            var currentSearchQuery = "";

            function applyFilters() {{
                var matchCount = 0;
                $(".profile-card-item").each(function() {{
                    var cardCategory = $(this).attr("data-category");
                    var searchData = $(this).attr("data-search") || "";

                    var categoryMatch = (currentCategory === "all" || cardCategory === currentCategory);
                    var searchMatch = (!currentSearchQuery || searchData.indexOf(currentSearchQuery.toLowerCase()) !== -1);

                    if (categoryMatch && searchMatch) {{
                        $(this).fadeIn(150);
                        matchCount++;
                    }} else {{
                        $(this).fadeOut(150);
                    }}
                }});

                if (matchCount === 0) {{
                    $("#noProfilesFound").removeClass("d-none");
                }} else {{
                    $("#noProfilesFound").addClass("d-none");
                }}
            }}

            // Category Filter Click
            $(".filter-btn-pill").on("click", function() {{
                $(".filter-btn-pill").removeClass("active");
                $(this).addClass("active");
                currentCategory = $(this).attr("data-filter");
                applyFilters();
            }});

            // Search Input Event
            $("#profileSearchInput").on("keyup input", function() {{
                currentSearchQuery = $(this).val().trim();
                applyFilters();
            }});
        }});

        function resetProfileFilters() {{
            $("#profileSearchInput").val("");
            $(".filter-btn-pill").removeClass("active");
            $(".filter-btn-pill[data-filter='all']").addClass("active");
            $(".profile-card-item").fadeIn(150);
            $("#noProfilesFound").addClass("d-none");
        }}

        function copyLinkUrl(url, name) {{
            if (navigator.clipboard) {{
                navigator.clipboard.writeText(url).then(function() {{
                    alert("Copied " + name + " link to clipboard:\\n" + url);
                }}).catch(function() {{
                    prompt("Copy link:", url);
                }});
            }} else {{
                prompt("Copy link:", url);
            }}
        }}
    </script>
</body>
</html>
"""
    with open("page-about.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Generated page-about.html successfully with all 38 verified profiles.")

if __name__ == "__main__":
    generate_html()
