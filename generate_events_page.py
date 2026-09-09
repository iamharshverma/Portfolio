#!/usr/bin/env python3
"""
generate_events_page.py
Generates an impressive, interactive, highly-styled page-events.html for Harsh Verma.
Includes:
- Judging & Mentorship
- Keynotes & Conferences
- Panel Talks & Technical Leadership
"""

import json
import os

events_data = {
    "judging": [
        {
            "id": "judge-techstars-sf",
            "title": "Techstars San Francisco Startup Mentor",
            "organization": "Techstars SF",
            "role": "Startup Mentor & Hackathon Advisor",
            "category": "Startup Mentorship",
            "date": "2025 - Present",
            "location": "San Francisco, CA",
            "description": "Mentored multiple startup cohorts and fast-paced hackathons across San Francisco at Techstars Startup Weekend, helping early-stage engineering founders refine their product-market fit, enterprise AI architectures, and technical execution.",
            "links": [
                {"name": "Techstars SF", "url": "https://www.startupweekendsf.com", "icon": "mdi-link-variant"}
            ],
            "tags": ["Techstars", "Startups", "Mentorship", "San Francisco"],
            "gradient": "from-amber-600 to-orange-500",
            "badge_color": "#d97706",
            "icon": "mdi-rocket-launch"
        },
        {
            "id": "judge-techstars-nyc",
            "title": "Techstars New York City Accelerator Startup Mentor",
            "organization": "Techstars NYC",
            "role": "Accelerator Startup Mentor",
            "category": "Startup Mentorship",
            "date": "Fall 2026",
            "location": "New York, NY",
            "description": "Appointed Startup Mentor for the Techstars NYC Fall 2026 cohort, guiding cutting-edge tech founders in agentic AI architecture, scalable cloud infrastructure, and enterprise go-to-market strategies.",
            "links": [
                {"name": "Techstars NYC Accelerator", "url": "https://www.techstars.com/accelerators/nyc", "icon": "mdi-link-variant"}
            ],
            "tags": ["Techstars NYC", "Accelerator", "Enterprise AI", "Venture Mentor"],
            "gradient": "from-blue-600 to-indigo-600",
            "badge_color": "#2563eb",
            "icon": "mdi-account-star"
        },
        {
            "id": "judge-skydeck-mentor",
            "title": "Mentor & Advisor at UC Berkeley SkyDeck",
            "organization": "UC Berkeley SkyDeck",
            "role": "Advisor & Technical Mentor",
            "category": "Startup Mentorship",
            "date": "2024 - Present",
            "location": "Berkeley, CA",
            "description": "Advised and mentored global high-growth startups at UC Berkeley SkyDeck on building secure enterprise AI architectures, scalable agentic workflows, LLM observability, and cybersecurity compliance.",
            "links": [
                {"name": "Berkeley SkyDeck", "url": "https://skydeck.berkeley.edu/", "icon": "mdi-link-variant"}
            ],
            "tags": ["Berkeley SkyDeck", "UC Berkeley", "Enterprise AI", "Security Advisor"],
            "gradient": "from-blue-800 to-sky-600",
            "badge_color": "#0284c7",
            "icon": "mdi-school"
        },
        {
            "id": "judge-skydeck-selection",
            "title": "UC Berkeley SkyDeck Selection Committee (Pad-21 & Pad-22)",
            "organization": "UC Berkeley SkyDeck",
            "role": "Selection Committee Member",
            "category": "Venture Selection",
            "date": "2025 - 2026",
            "location": "Berkeley, CA",
            "description": "Served on the elite Selection Committee evaluating top international startups applying for UC Berkeley SkyDeck cohorts Pad-21 and Pad-22, assessing technical defensibility, AI infrastructure, team capability, and market potential.",
            "links": [
                {"name": "Berkeley SkyDeck Cohorts", "url": "https://skydeck.berkeley.edu/", "icon": "mdi-link-variant"}
            ],
            "tags": ["SkyDeck Pad-21", "SkyDeck Pad-22", "Selection Committee", "Venture Screening"],
            "gradient": "from-indigo-700 to-blue-700",
            "badge_color": "#4338ca",
            "icon": "mdi-checkbox-marked-circle-outline"
        },
        {
            "id": "judge-mayfield-ai-garage",
            "title": "The Mayfield AI Garage Selection Committee & Judge",
            "organization": "Mayfield Fund & UC Berkeley",
            "role": "Selection Committee & Pitch Judge",
            "category": "Venture Selection",
            "date": "2025",
            "location": "Berkeley / Silicon Valley, CA",
            "description": "Evaluated 100+ AI startup submissions from Berkeley undergrad and alumni founders competing for $50k non-dilutive stipends, NVIDIA Inception access, and incubation in the Pad-13 program, identifying breakout early-stage AI innovations.",
            "links": [
                {"name": "Mayfield AI Garage", "url": "https://mayfield.com/", "icon": "mdi-link-variant"}
            ],
            "tags": ["Mayfield Fund", "NVIDIA Inception", "$50K Grant", "AI Garage"],
            "gradient": "from-emerald-700 to-teal-600",
            "badge_color": "#059669",
            "icon": "mdi-currency-usd"
        },
        {
            "id": "judge-genlabx-worldsfair",
            "title": "GenLabX AI Engineer World's Fair Hackathon Judge",
            "organization": "GenLabX & AI Engineer World's Fair",
            "role": "Hackathon Judge",
            "category": "Hackathon Judging",
            "date": "2025",
            "location": "San Francisco, CA",
            "description": "Served as official hackathon judge for over 100+ AI startups and engineering teams competing in San Francisco during the AI Engineer World's Fair, evaluating autonomous agent frameworks and LLM-powered applications.",
            "links": [
                {"name": "Luma Event Page", "url": "https://luma.com/genlabxaiengineer", "icon": "mdi-calendar-check"}
            ],
            "tags": ["GenLabX", "AI Engineer Fair", "100+ Startups", "SF Hackathon"],
            "gradient": "from-purple-700 to-pink-600",
            "badge_color": "#7c3aed",
            "icon": "mdi-trophy-variant"
        },
        {
            "id": "judge-lovehack-2025",
            "title": "LoveHackathon 2025 Main Final Judge",
            "organization": "LoveHackathon SF",
            "role": "Final Main Judge",
            "category": "Hackathon Judging",
            "date": "2025",
            "location": "San Francisco, CA",
            "description": "Served as Final Main Judge evaluating top finalists and innovative technical builds at the high-profile LoveHackathon 2025 in San Francisco, selecting grand prize winners across consumer AI and social intelligence.",
            "links": [
                {"name": "Luma Event Page", "url": "https://lu.ma/lovehack", "icon": "mdi-calendar-check"}
            ],
            "tags": ["LoveHack 2025", "Final Judge", "Grand Finale", "San Francisco"],
            "gradient": "from-rose-600 to-pink-600",
            "badge_color": "#e11d48",
            "icon": "mdi-heart-flash"
        },
        {
            "id": "judge-fow-pitch-aug26",
            "title": "The Future of Work Pitch Night: Worktech, Robotics & Agentic AI",
            "organization": "Future of Work Collective",
            "role": "Jury Member & Pitch Judge",
            "category": "Pitch Competition",
            "date": "August 25, 2026",
            "location": "San Francisco, CA",
            "description": "Judged high-stakes live startup pitches from visionary founders building next-generation agentic AI systems, robotic automation, and enterprise worktech platforms.",
            "links": [
                {"name": "Luma Event Page", "url": "https://luma.com/yktcpve0?tk=RWVd1n", "icon": "mdi-calendar-check"},
                {"name": "LinkedIn Feature", "url": "https://www.linkedin.com/posts/nataliabielczyk_futureofwork-pitchnight-agenticai-share-7479917479402762240-yEMP/", "icon": "mdi-linkedin"}
            ],
            "tags": ["Future of Work", "Agentic AI", "Robotics", "Pitch Jury"],
            "gradient": "from-cyan-700 to-blue-700",
            "badge_color": "#0891b2",
            "icon": "mdi-robot"
        },
        {
            "id": "judge-fow-mixer-worktech",
            "title": "Future of Work Mixer + Open Demos: Worktech, Robotics & Agentic AI",
            "organization": "Future of Work Collective",
            "role": "Jury Member & Demo Judge",
            "category": "Pitch Competition",
            "date": "2026",
            "location": "San Francisco, CA",
            "description": "Jury member evaluating open demo showcases and seed-stage pitches in workplace automation, enterprise agentic intelligence, and robotics orchestration.",
            "links": [
                {"name": "Luma Event Page", "url": "https://luma.com/k0r1yhe5", "icon": "mdi-calendar-check"},
                {"name": "LinkedIn Announcement", "url": "https://www.linkedin.com/feed/update/urn%3Ali%3Aactivity%3A7434967919094300672/", "icon": "mdi-linkedin"}
            ],
            "tags": ["Worktech", "Agentic AI", "Open Demos", "Pitch Competition"],
            "gradient": "from-blue-700 to-indigo-800",
            "badge_color": "#1d4ed8",
            "icon": "mdi-domain"
        },
        {
            "id": "judge-fow-mixer-health",
            "title": "Future of Work Mixer + Open Demos: Worktech, Robotics & Healthcare",
            "organization": "Future of Work Collective",
            "role": "Jury Member",
            "category": "Pitch Competition",
            "date": "2026",
            "location": "San Francisco, CA",
            "description": "Served as Jury Member judging pitch competitions bridging clinical robotics, healthcare AI workflows, predictive diagnostic pipelines, and modern worktech.",
            "links": [
                {"name": "Luma Event Page", "url": "https://luma.com/pgvpc0sl?tk=DYtJAq", "icon": "mdi-calendar-check"}
            ],
            "tags": ["HealthTech", "Robotics", "Worktech", "Jury Member"],
            "gradient": "from-teal-600 to-emerald-600",
            "badge_color": "#0d9488",
            "icon": "mdi-hospital-box"
        },
        {
            "id": "judge-techpioneer-2026",
            "title": "TechPioneer Hackathon 2.0 AI & Cybersecurity Judge",
            "organization": "TechPioneers Pro",
            "role": "Expert Panel Industry Judge",
            "category": "Hackathon Judging",
            "date": "August 20 - 21, 2026",
            "location": "Global / Virtual",
            "description": "Evaluated cutting-edge hackathon submissions in Artificial Intelligence and Cybersecurity at TechPioneer Hackathon 2.0, judging threat-detection models, autonomous agent security, and zero-trust engineering.",
            "certificate_id": "TPH2026-FC1EC8-4008",
            "certificate_url": "https://techpioneerspro.com/2.0/certificate/TPH2026-FC1EC8-4008",
            "links": [
                {"name": "Verified Certificate", "url": "https://techpioneerspro.com/2.0/certificate/TPH2026-FC1EC8-4008", "icon": "mdi-check-decagram"},
                {"name": "Official Judges Page", "url": "https://techpioneerspro.com/2.0/judges", "icon": "mdi-shield-account"}
            ],
            "tags": ["Cybersecurity", "AI Hackathon", "Industry Judge", "TechPioneer", "Verified Credential #TPH2026-FC1EC8-4008"],
            "gradient": "from-red-700 to-amber-700",
            "badge_color": "#b91c1c",
            "icon": "mdi-shield-check"
        },
        {
            "id": "judge-vc-conf",
            "title": "VC-Conf Expert Investor & Pitch Competition Judge",
            "organization": "VC-Conf Global",
            "role": "Expert Investor & Pitch Judge",
            "category": "Venture Selection",
            "date": "2026",
            "location": "Silicon Valley, CA",
            "description": "Participated as venture judge and expert investor at VC-Conf, analyzing seed and Series A AI startups on market size, defensibility, unit economics, and enterprise scalability.",
            "links": [
                {"name": "LinkedIn Review", "url": "https://www.linkedin.com/posts/harshverma59_ai-startups-venturecapital-share-7486229998492880896-JPIh/", "icon": "mdi-linkedin"}
            ],
            "tags": ["VC-Conf", "Venture Capital", "Seed Stage", "AI Startups"],
            "gradient": "from-emerald-800 to-green-700",
            "badge_color": "#047857",
            "icon": "mdi-cash-multiple"
        },
        {
            "id": "judge-buildwithai-global",
            "title": "#BuildwithAI Global Hack Lead Mentor",
            "organization": "Hackmakers (Sponsored by Google, AWS, Oracle, IBM)",
            "role": "Global Lead Mentor",
            "category": "Startup Mentorship",
            "date": "Global Initiative",
            "location": "Global / Virtual",
            "description": "Guided thousands of hackers and mentors internationally in building meaningful data science and AI solutions to address global societal resilience during the pandemic, sponsored by major tech giants.",
            "links": [
                {"name": "LinkedIn Global Milestone", "url": "https://www.linkedin.com/feed/update/urn:li:activity:6691402830294724608/", "icon": "mdi-linkedin"}
            ],
            "tags": ["Google", "AWS", "Oracle", "IBM", "Lead Mentor"],
            "gradient": "from-blue-600 to-cyan-600",
            "badge_color": "#0284c7",
            "icon": "mdi-account-group"
        },
        {
            "id": "judge-progressive-ventures",
            "title": "Progressive Ventures Founding Limited Partner (LP)",
            "organization": "Progressive Ventures",
            "role": "Founding LP & Technical Deal Screen",
            "category": "Venture Selection",
            "date": "2025 - Present",
            "location": "San Francisco, CA",
            "description": "Founding Limited Partner helping identify, vet, and allocate venture capital into top tier early-stage startups in the generative AI, agentic systems, and developer infrastructure domain.",
            "links": [
                {"name": "Progressive Ventures", "url": "https://luma.com/aiproducts?tk=RBRV8k", "icon": "mdi-link-variant"}
            ],
            "tags": ["Founding LP", "Venture Capital", "AI Investment", "Deal Flow"],
            "gradient": "from-slate-800 to-indigo-900",
            "badge_color": "#334155",
            "icon": "mdi-briefcase-check"
        },
        {
            "id": "judge-founders-creative",
            "title": "Founders' Creative Technical Program Committee",
            "organization": "Founders' Creative",
            "role": "Core Team Member & Program Reviewer",
            "category": "Conference Selection",
            "date": "2025 - Present",
            "location": "San Francisco, CA",
            "description": "Core team member reviewing technical proposals, research submissions, and tech invite applications to curate distinguished conference speakers and high-impact AI workshops across Silicon Valley.",
            "links": [
                {"name": "Founders Creative", "url": "https://luma.com/engsummit?utm_source=fclinkedin", "icon": "mdi-link-variant"}
            ],
            "tags": ["Founders Creative", "Paper Review", "Program Committee", "Speaker Selection"],
            "gradient": "from-violet-800 to-purple-700",
            "badge_color": "#6d28d9",
            "icon": "mdi-clipboard-text-search"
        },
        {
            "id": "judge-dent-expert",
            "title": "AI Expert & Pitch Mentor at Dent Community",
            "organization": "Dent Expert / Dent Spark / Dent Capital",
            "role": "AI Domain Expert & Final Round Mentor",
            "category": "Startup Mentorship",
            "date": "2025",
            "location": "San Francisco, CA",
            "description": "Mentored startups through intensive incubation and final round pitch showcases across the Dent Expert, Dent Spark, and Dent Capital innovation network.",
            "links": [
                {"name": "Dent Network", "url": "https://www.linkedin.com/in/harshverma59/", "icon": "mdi-linkedin"}
            ],
            "tags": ["Dent Capital", "Pitch Mentor", "AI Expert", "Showcase"],
            "gradient": "from-amber-700 to-yellow-600",
            "badge_color": "#b45309",
            "icon": "mdi-lightbulb-on"
        },
        {
            "id": "judge-packt-book-review",
            "title": "Packt Publishing Official Technical Book Reviewer",
            "organization": "Packt Publishing",
            "role": "Technical Book Reviewer",
            "category": "Book & Peer Review",
            "date": "2023 - 2025",
            "location": "Global",
            "description": "Conducted in-depth technical editorial and code reviews for major published AI books including 'The TensorFlow Workshop' and 'Machine Learning and Generative AI for Marketing'.",
            "links": [
                {"name": "The TensorFlow Workshop (Amazon)", "url": "https://www.amazon.com/TensorFlow-Workshop-hands-building-real-world/dp/1800205252", "icon": "mdi-amazon"},
                {"name": "ML & GenAI for Marketing (Amazon)", "url": "https://www.amazon.com/Machine-Learning-Generative-Marketing-data-driven/dp/1835889409/ref=sr_1_1?link_from_packtlink=yes", "icon": "mdi-amazon"}
            ],
            "tags": ["Packt Publishing", "Book Review", "TensorFlow", "Generative AI"],
            "gradient": "from-orange-700 to-amber-600",
            "badge_color": "#ea580c",
            "icon": "mdi-book-open-page-variant"
        },
        {
            "id": "judge-ieee-reviews",
            "title": "IEEE Technical Peer Reviewer (Software Engineering & XAI)",
            "organization": "IEEE",
            "role": "Peer Reviewer",
            "category": "Peer Review",
            "date": "2025 - 2026",
            "location": "Global",
            "description": "Reviewed advanced IEEE conference and journal papers: 'Automated Code Generation and Optimization Using Deep Learning: Advancing Intelligent Software Engineering Practices' and 'Integrating Explainable Artificial Intelligence into Software Engineering Workflows'.",
            "links": [
                {"name": "IEEE Author Profile", "url": "https://ieeexplore.ieee.org/", "icon": "mdi-certificate"}
            ],
            "tags": ["IEEE", "Deep Learning", "Code Generation", "XAI"],
            "gradient": "from-blue-900 to-indigo-900",
            "badge_color": "#1e3a8a",
            "icon": "mdi-check-decagram"
        },
        {
            "id": "judge-ijeetr-reviews",
            "title": "IJEETR Journal Peer Reviewer (Supply Chain & Cloud FinOps)",
            "organization": "International Journal of Engineering & Extended Technologies Research",
            "role": "Editorial Peer Reviewer",
            "category": "Peer Review",
            "date": "2025 - 2026",
            "location": "Global",
            "description": "Peer reviewed research papers: 'AI-Enabled Predictive Analytics and Autonomous Decision Systems for Resilient Supply Chain and Advanced Manufacturing under Industry 4.0/5.0' and 'AI-Powered Cloud Modernization Framework for Intelligent Risk and Financial Process Management in SAP Environments'.",
            "links": [
                {"name": "IJEETR Journal", "url": "https://ijeetr.com/", "icon": "mdi-file-document-outline"}
            ],
            "tags": ["IJEETR", "Industry 5.0", "SAP Cloud", "Supply Chain"],
            "gradient": "from-slate-700 to-zinc-800",
            "badge_color": "#475569",
            "icon": "mdi-file-find"
        },
        {
            "id": "judge-jrtcse-reviews",
            "title": "JRTCSE Journal Reviewer (15+ Peer Reviewed Papers)",
            "organization": "Journal of Recent Trends in Computer Science and Engineering",
            "role": "Editorial Board / Peer Reviewer",
            "category": "Peer Review",
            "date": "2024 - 2026",
            "location": "Global",
            "description": "Conducted rigorous peer reviews on more than 15+ scholarly papers spanning machine learning architectures, distributed cloud computing, algorithmic optimizations, and cybersecurity.",
            "links": [
                {"name": "JRTCSE Reviewer Profile", "url": "https://jrtcse.com/index.php/home/Harsh_Verma", "icon": "mdi-link-variant"}
            ],
            "tags": ["JRTCSE", "15+ Papers", "Editorial Review", "Computer Science"],
            "gradient": "from-sky-800 to-blue-900",
            "badge_color": "#0369a1",
            "icon": "mdi-file-check"
        }
    ],
    "conferences": [
        {
            "id": "conf-ieee-icacsdf-2026",
            "title": "UPES & IEEE ICACSDF 2026 Keynote Speaker",
            "event_name": "International Conference on Advancement in Cyber Security and Digital Forensics (ICACSDF 2026)",
            "role": "Keynote Speaker & Technical Reviewer",
            "date": "2026",
            "location": "Dehradun, India / Hybrid",
            "description": "Keynote speech at IEEE ICACSDF on the frontier of AI in threat detection, adversarial resilience, and autonomous digital forensics. Also served on the CMT research paper review board.",
            "links": [
                {"name": "ICACSDF Keynote Page", "url": "https://www.icacsdf.org/keynotes.html", "icon": "mdi-web"},
                {"name": "Microsoft CMT Portal", "url": "https://cmt3.research.microsoft.com/User/Login?ReturnUrl=%2F", "icon": "mdi-microsoft"}
            ],
            "tags": ["IEEE ICACSDF", "Cybersecurity", "Keynote", "Digital Forensics"],
            "gradient": "from-blue-700 to-indigo-800",
            "badge_color": "#1d4ed8",
            "icon": "mdi-microphone-variant"
        },
        {
            "id": "conf-acm-sacramento-2026",
            "title": "ACM Sacramento Keynote: Secure & Trustworthy ML/AI",
            "event_name": "Association for Computing Machinery (ACM) Sacramento Chapter",
            "role": "Keynote Speaker",
            "date": "September 10, 2026",
            "location": "Sacramento, CA / Online",
            "description": "Distinguished Keynote Address titled 'Secure and Trustworthy Machine Learning and AI for Multi-Domain Applications', analyzing enterprise LLM defense, zero-trust validation, and agent alignment.",
            "links": [
                {"name": "ACM Event Page & Registration", "url": "https://tikkl.com/acmsacramentochapter/c/harshverma59/?", "icon": "mdi-ticket-confirmation"}
            ],
            "tags": ["ACM", "Keynote", "Secure AI", "Trustworthy ML"],
            "gradient": "from-teal-700 to-cyan-700",
            "badge_color": "#0f766e",
            "icon": "mdi-shield-lock"
        },
        {
            "id": "conf-iciotcaa-2026",
            "title": "ICIoTCAA-2026 Keynote: AI-Enhanced Enterprise Security",
            "event_name": "International Conference on Internet of Things, Computing, and AI Applications (ICIoTCAA-2026)",
            "role": "Distinguished Keynote Speaker",
            "date": "2026",
            "location": "International / Virtual",
            "description": "Keynote presentation titled 'Building an AI-Enhanced Enterprise Security Solution Using Artificial Intelligence in Cybersecurity', demonstrating real-time behavioral anomaly detection and threat isolation.",
            "links": [
                {"name": "Keynote Announcement", "url": "https://sciencetechxplore.org/conference/keynoteby-ICIoTCAA-2026.php", "icon": "mdi-bullhorn"}
            ],
            "tags": ["ICIoTCAA", "IoT", "Enterprise Security", "Keynote"],
            "gradient": "from-purple-800 to-indigo-800",
            "badge_color": "#6b21a8",
            "icon": "mdi-presentation-play"
        },
        {
            "id": "conf-ai-salon-deepseek",
            "title": "AI Engineering Salon: DeepSeek & The New Paradigm in Foundational Models",
            "event_name": "AI Engineering Salon (Founders' Creative)",
            "role": "Organizer & Featured Speaker",
            "date": "February 7, 2025",
            "location": "San Francisco, CA",
            "description": "Organized and presented a deep technical breakdown on DeepSeek's architectural innovations, Mixture-of-Experts (MoE) efficiency, inference cost reductions, and implications for open source foundational models.",
            "links": [
                {"name": "Luma Event Page", "url": "https://luma.com/engsalon3?tk=hzeqZR", "icon": "mdi-calendar-check"}
            ],
            "tags": ["DeepSeek", "Foundational Models", "MoE", "AI Salon"],
            "gradient": "from-blue-600 to-emerald-600",
            "badge_color": "#0284c7",
            "icon": "mdi-brain"
        },
        {
            "id": "conf-ai-salon-trends-2025",
            "title": "AI Engineering Salon: 2025 AI Trends for Engineering Leaders",
            "event_name": "AI Engineering Salon (Founders' Creative)",
            "role": "Organizer & Key Speaker",
            "date": "January 17, 2025",
            "location": "San Francisco, CA",
            "description": "Curated and delivered an executive briefing for Silicon Valley VP of Engineering and Tech Leads on 2025 AI architectural shifts, multi-agent pipelines, cost optimization, and enterprise governance.",
            "links": [
                {"name": "Luma Event Page", "url": "https://luma.com/engsalon1?tk=9XhKKO", "icon": "mdi-calendar-check"}
            ],
            "tags": ["AI Trends 2025", "Engineering Leaders", "Enterprise Scale", "Founders Creative"],
            "gradient": "from-indigo-600 to-violet-600",
            "badge_color": "#4f46e5",
            "icon": "mdi-chart-line"
        },
        {
            "id": "conf-ai-agent-workshop",
            "title": "AI Engineering Salon: Autonomous Agent Workshop",
            "event_name": "AI Engineering Salon (Founders' Creative)",
            "role": "Workshop Lead & Instructor",
            "date": "April 2025",
            "location": "San Francisco, CA",
            "description": "Led an intensive hands-on technical workshop on designing and orchestrating multi-agent systems, tool calling, memory management, and agent-to-agent feedback loops in production.",
            "links": [
                {"name": "Luma Event Page", "url": "https://luma.com/agentworkshop?tk=lBD1Oj", "icon": "mdi-calendar-check"}
            ],
            "tags": ["Agent Workshop", "Multi-Agent", "Hands-on", "Tool Calling"],
            "gradient": "from-amber-600 to-rose-600",
            "badge_color": "#d97706",
            "icon": "mdi-hammer-wrench"
        },
        {
            "id": "conf-atagtr-hikerunner",
            "title": "Global Test Alliance #ATAGTR International Conference",
            "event_name": "Global Testing Alliance International Summit",
            "role": "Conference Speaker & Researcher",
            "date": "Research Summit",
            "location": "International / Online",
            "description": "Presented research on 'HikeRunner Load Test Framework', detailing high-concurrency distributed load testing, microservices resilience testing, and automated performance profiling.",
            "links": [
                {"name": "SlideShare Deck", "url": "https://www.slideshare.net/ATASlides/atagtr2017-hikerunner-load-test-framework", "icon": "mdi-file-powerpoint"}
            ],
            "tags": ["ATAGTR", "HikeRunner", "Distributed Systems", "Load Testing"],
            "gradient": "from-slate-700 to-blue-800",
            "badge_color": "#334155",
            "icon": "mdi-speedometer"
        }
    ],
    "panels": [
        {
            "id": "panel-autonomy-ai-agents",
            "title": "The Autonomy of AI Agents (Founders' Creative)",
            "event_name": "AI Engineering Summit by Founders' Creative",
            "role": "Host & Panel Moderator",
            "date": "2025",
            "location": "San Francisco, CA",
            "description": "Hosted and moderated an executive panel featuring top AI founders and architects on the transition from passive LLMs to goal-directed autonomous agents, evaluating deterministic control, guardrails, and real-time agency.",
            "links": [
                {"name": "Luma Summit Link", "url": "https://luma.com/engsummit?utm_source=fclinkedin", "icon": "mdi-calendar-check"},
                {"name": "LinkedIn Summary 1", "url": "https://www.linkedin.com/posts/harshverma59_ai-autonomousagents-aiengineering-activity-7311869320215572480-s8CO", "icon": "mdi-linkedin"},
                {"name": "LinkedIn Summary 2", "url": "https://www.linkedin.com/posts/harshverma59_aiengineering-aiproductdevelopment-engineeringwithai-activity-7333918177594146817-hYSQ", "icon": "mdi-linkedin"}
            ],
            "tags": ["Autonomy", "Autonomous Agents", "Panel Moderator", "Founders Creative"],
            "gradient": "from-purple-700 to-indigo-700",
            "badge_color": "#7e22ce",
            "icon": "mdi-account-voice"
        },
        {
            "id": "panel-ai-trust-reliability",
            "title": "AI Trust, Safety & Reliability Executive Panel",
            "event_name": "Hosted by The Agentic",
            "role": "Featured Panel Speaker",
            "date": "2025",
            "location": "San Francisco, CA",
            "description": "Addressed enterprise AI safety, hallucination mitigation, deterministic fallback mechanisms, and regulatory alignment in production agentic systems.",
            "links": [
                {"name": "Luma Event Link", "url": "https://luma.com/cg1j3h2d", "icon": "mdi-calendar-check"},
                {"name": "LinkedIn Post", "url": "https://www.linkedin.com/posts/harshverma59_aisafetyreliability-aisafety-aireliability-activity-7404297211829895168-EMNE", "icon": "mdi-linkedin"}
            ],
            "tags": ["AI Trust", "AI Safety", "The Agentic", "Reliability"],
            "gradient": "from-emerald-700 to-teal-700",
            "badge_color": "#047857",
            "icon": "mdi-shield-check"
        },
        {
            "id": "panel-progressive-venture-summit",
            "title": "The Agentic AI Summit 2026: People & Leadership in Agentic AI",
            "event_name": "Progressive Ventures Technology Summit",
            "role": "Frontline Keynote Panelist",
            "date": "2026",
            "location": "Silicon Valley, CA",
            "description": "Frontline panelist speaking on how organizational hierarchy, leadership mindsets, and engineering team topologies must adapt when autonomous agents become active team contributors.",
            "links": [
                {"name": "Luma Summit Link", "url": "https://luma.com/aiproducts?tk=RBRV8k", "icon": "mdi-calendar-check"},
                {"name": "Harsh Verma LinkedIn", "url": "https://www.linkedin.com/posts/harshverma59_agenticai-aileadership-autonomoussystems-activity-7427117736331272193-4dIC", "icon": "mdi-linkedin"},
                {"name": "Summit Host Post", "url": "https://www.linkedin.com/posts/malaramakrishnan_excited-to-host-our-6th-technology-summit-ugcPost-7425009116357541888-zz8_", "icon": "mdi-linkedin"}
            ],
            "tags": ["Agentic AI Summit", "AI Leadership", "Progressive Ventures", "Frontline Speaker"],
            "gradient": "from-blue-700 to-cyan-600",
            "badge_color": "#1d4ed8",
            "icon": "mdi-account-tie"
        },
        {
            "id": "panel-twill-vibe-shift",
            "title": "Rocket & Twill Present 'Vibe Shift: The Builders Behind the Models'",
            "event_name": "Twill & Rocket AI Engineering Conference",
            "role": "Featured Panelist",
            "date": "2026",
            "location": "San Francisco, CA",
            "description": "Expert panel discussion on foundational model ergonomics, LLMOps, model evaluation datasets, context-caching, and fine-tuning pipelines with top industry practitioners.",
            "links": [
                {"name": "Luma Event Link", "url": "https://luma.com/8rdw6gga?tk=nxAN0Z", "icon": "mdi-calendar-check"},
                {"name": "Twill Feature Post 1", "url": "https://www.linkedin.com/posts/wearetwill_aiengineering-mlops-aiobservability-ugcPost-7429227974249353217-LiE4", "icon": "mdi-linkedin"},
                {"name": "Twill Feature Post 2", "url": "https://www.linkedin.com/posts/wearetwill_ai-enterpriseai-machinelearning-ugcPost-7427861664626069505-ANT4", "icon": "mdi-linkedin"},
                {"name": "Twill Feature Post 3", "url": "https://www.linkedin.com/posts/wearetwill_agentic-ai-is-moving-fast-but-deploying-it-activity-7423138900010860544-zDMb", "icon": "mdi-linkedin"}
            ],
            "tags": ["Twill", "LLMOps", "Builders Behind Models", "Observability"],
            "gradient": "from-pink-700 to-rose-600",
            "badge_color": "#be185d",
            "icon": "mdi-code-braces"
        },
        {
            "id": "panel-health-tech-week",
            "title": "Health Tech Week / Health Tech Summit: AI & Cybersecurity in Healthcare",
            "event_name": "Health Tech Week San Francisco (aiify.io & HealthTechWeek)",
            "role": "Speaker & Cybersecurity in AI Panelist",
            "date": "2026",
            "location": "San Francisco, CA",
            "description": "Delivered insights on securing HIPAA-compliant healthcare LLM pipelines, autonomous clinical note extraction, federated medical learning, and patient data protection.",
            "links": [
                {"name": "Health Tech Summit (aiify.io)", "url": "https://aiify.io/events/ht26/", "icon": "mdi-web"},
                {"name": "Health Tech Week Portal", "url": "https://healthtechweek.org/", "icon": "mdi-hospital"},
                {"name": "Luma Summit", "url": "https://luma.com/HTSummit26?tk=aTK7ph", "icon": "mdi-calendar-check"},
                {"name": "LinkedIn Highlight 1", "url": "https://www.linkedin.com/posts/stevene_healthtechweek-healthtech-cybersecurity-ugcPost-7417966646679515136-7JvV", "icon": "mdi-linkedin"},
                {"name": "LinkedIn Highlight 2", "url": "https://www.linkedin.com/posts/harshverma59_healthtech-healthtechweek-healthtech-activity-7418064321072599040-rngs", "icon": "mdi-linkedin"}
            ],
            "tags": ["HealthTech", "Cybersecurity", "San Francisco", "Healthcare AI"],
            "gradient": "from-teal-700 to-emerald-700",
            "badge_color": "#0f766e",
            "icon": "mdi-medical-bag"
        },
        {
            "id": "panel-responsible-ai-summit",
            "title": "Agentic AI Summit: Advancing Responsible AI",
            "event_name": "Founders' Creative Thought Leadership Series",
            "role": "Panelist Speaker",
            "date": "2026",
            "location": "San Francisco, CA",
            "description": "Panel discussion exploring responsible deployment frameworks for autonomous agents, algorithmic accountability, data provenance, and red-teaming methodologies.",
            "links": [
                {"name": "Luma Event Link", "url": "https://luma.com/3e8jb8py?tk=HcHhFx", "icon": "mdi-calendar-check"}
            ],
            "tags": ["Responsible AI", "Founders Creative", "Agent Safety", "Red Teaming"],
            "gradient": "from-indigo-700 to-blue-800",
            "badge_color": "#3730a3",
            "icon": "mdi-scale-balance"
        }
    ]
}

def render_links(links):
    html = ""
    for link in links:
        html += f"""
        <a href="{link['url']}" target="_blank" class="btn-event-link mr-2 mb-2" title="{link['name']}">
            <i class="mdi {link['icon']} mr-1"></i> {link['name']}
        </a>
        """
    return html

def render_tags(tags):
    html = ""
    for tag in tags:
        html += f"""<span class="event-tag-pill">{tag}</span>"""
    return html

def generate_card(item, event_type):
    badge_type_text = {
        "judging": "Judging & Mentorship",
        "conferences": "Keynote & Conference",
        "panels": "Panel & Thought Leadership"
    }.get(event_type, "Event")
    
    badge_bg = item.get("badge_color", "#2563eb")
    category = item.get("category") or item.get("role") or badge_type_text
    search_keywords = f"{item['title']} {item.get('organization', '')} {item.get('event_name', '')} {item.get('role', '')} {category} {item['location']} {' '.join(item.get('tags', []))}".lower()

    links_html = render_links(item.get("links", []))
    tags_html = render_tags(item.get("tags", []))
    
    org_or_event = item.get("organization") or item.get("event_name") or ""
    
    return f"""
    <div class="col-lg-6 col-md-12 mb-4 event-card-item" data-category="{event_type}" data-search="{search_keywords}">
        <div class="event-hub-card h-100">
            <div class="event-card-header d-flex justify-content-between align-items-start mb-3">
                <div class="d-flex align-items-center">
                    <div class="event-icon-badge mr-3" style="background: {badge_bg}15; color: {badge_bg}; border: 1px solid {badge_bg}30;">
                        <i class="mdi {item.get('icon', 'mdi-star')}"></i>
                    </div>
                    <div>
                        <span class="badge badge-pill text-white font-weight-bold px-2 py-1" style="background: {badge_bg}; font-size: 11px;">
                            {category}
                        </span>
                        <div class="event-org-name font-weight-bold mt-1 text-muted" style="font-size: 13px;">
                            <i class="mdi mdi-map-marker-outline mr-1"></i> {item['location']} &bull; <i class="mdi mdi-calendar-outline ml-1 mr-1"></i> {item['date']}
                        </div>
                    </div>
                </div>
                <button class="btn btn-sm btn-light border copy-event-btn" onclick="copyEventInfo('{item['id']}', '{item['title']}')" title="Copy Event Details" aria-label="Copy Details">
                    <i class="mdi mdi-content-copy text-muted"></i>
                </button>
            </div>

            <h4 class="event-card-title mb-2">
                {item['title']}
            </h4>

            {f'<div class="event-card-org mb-2"><i class="mdi mdi-domain text-primary mr-1"></i> <strong>{org_or_event}</strong> &bull; <span class="text-primary font-weight-600">{item.get("role", "")}</span></div>' if org_or_event else ''}

            <p class="event-card-desc mb-3">
                {item['description']}
            </p>

            <div class="event-tags-wrap mb-3">
                {tags_html}
            </div>

            <div class="event-card-footer mt-auto pt-3 border-top d-flex flex-wrap align-items-center">
                {links_html}
            </div>
        </div>
    </div>
    """

def build_full_page():
    all_judging = "".join([generate_card(item, "judging") for item in events_data["judging"]])
    all_confs = "".join([generate_card(item, "conferences") for item in events_data["conferences"]])
    all_panels = "".join([generate_card(item, "panels") for item in events_data["panels"]])

    total_events = len(events_data["judging"]) + len(events_data["conferences"]) + len(events_data["panels"])
    total_judging = len(events_data["judging"])
    total_confs = len(events_data["conferences"])
    total_panels = len(events_data["panels"])

    return f"""<!DOCTYPE html>
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
    <title>Speaking Engagements - Harsh Verma | Keynotes, Conferences &amp; Judging</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Keynote speeches, hackathon judging, international conference presentations, workshop panels, and venture mentorship by Harsh Verma — Principal Software Engineer in AI at Palo Alto Networks, Forbes Tech Council Member." />
    <meta name="keywords" content="Harsh Verma, Speaking Engagements, Conference Speaker, Keynote Speaker, Hackathon Judge, AI Talks, Berkeley SkyDeck, Techstars, ACM Keynote, IEEE Speaker, Palo Alto Networks" />
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
        .events-page-wrapper {{
            background-color: #f8fafc;
            background-image: 
                radial-gradient(circle at 15% 15%, rgba(37, 99, 235, 0.05) 0%, transparent 40%),
                radial-gradient(circle at 85% 35%, rgba(124, 58, 237, 0.06) 0%, transparent 45%),
                radial-gradient(circle at 50% 85%, rgba(14, 165, 233, 0.05) 0%, transparent 50%);
            min-height: 100vh;
        }}

        /* Hero Banner */
        .events-hero-card {{
            background: linear-gradient(135deg, #090e17 0%, #0f172a 45%, #1e1b4b 100%);
            border-radius: 20px;
            color: #ffffff;
            padding: 42px 36px;
            box-shadow: 0 16px 40px rgba(15, 23, 42, 0.25);
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(99, 102, 241, 0.25);
            margin-bottom: 36px;
        }}
        .events-hero-card::before {{
            content: "";
            position: absolute;
            top: -40%;
            right: -20%;
            width: 480px;
            height: 480px;
            background: radial-gradient(circle, rgba(99, 102, 241, 0.3) 0%, rgba(14, 165, 233, 0.15) 50%, transparent 70%);
            border-radius: 50%;
            pointer-events: none;
        }}

        .stat-metric-pill {{
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 12px;
            padding: 12px 18px;
            display: inline-block;
            backdrop-filter: blur(8px);
            margin-right: 12px;
            margin-bottom: 12px;
            text-align: center;
            min-width: 130px;
        }}
        .stat-metric-val {{
            font-size: 24px;
            font-weight: 800;
            color: #60a5fa;
            line-height: 1.1;
        }}
        .stat-metric-label {{
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            color: #cbd5e1;
            margin-top: 4px;
        }}

        /* Search and Filter Controls */
        .events-controls-box {{
            background: #ffffff;
            border-radius: 16px;
            border: 1px solid #e2e8f0;
            padding: 24px;
            box-shadow: 0 4px 20px rgba(15, 23, 42, 0.04);
            margin-bottom: 32px;
        }}

        .event-search-input {{
            border-radius: 12px;
            border: 1px solid #cbd5e1;
            padding: 12px 18px 12px 42px;
            font-size: 15px;
            width: 100%;
            transition: all 0.2s ease;
            background: #f8fafc;
        }}
        .event-search-input:focus {{
            outline: none;
            border-color: #4f46e5;
            background: #ffffff;
            box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.15);
        }}
        .search-icon-pos {{
            position: absolute;
            left: 28px;
            top: 50%;
            transform: translateY(-50%);
            color: #94a3b8;
            font-size: 19px;
            pointer-events: none;
        }}

        .event-filter-pill {{
            border: 1px solid #cbd5e1;
            background: #ffffff;
            color: #475569;
            padding: 8px 18px;
            border-radius: 24px;
            font-size: 13.5px;
            font-weight: 600;
            margin-right: 8px;
            margin-bottom: 8px;
            transition: all 0.2s ease;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
        }}
        .event-filter-pill i {{
            margin-right: 6px;
        }}
        .event-filter-pill:hover {{
            background: #f1f5f9;
            border-color: #94a3b8;
            color: #0f172a;
        }}
        .event-filter-pill.active {{
            background: #4f46e5;
            color: #ffffff;
            border-color: #4f46e5;
            box-shadow: 0 4px 12px rgba(79, 70, 229, 0.25);
        }}

        /* Event Cards */
        .event-hub-card {{
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 16px;
            padding: 24px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: all 0.25s ease;
            box-shadow: 0 2px 12px rgba(15, 23, 42, 0.03);
            position: relative;
        }}
        .event-hub-card:hover {{
            border-color: #6366f1;
            transform: translateY(-3px);
            box-shadow: 0 10px 28px rgba(79, 70, 229, 0.09);
        }}

        .event-icon-badge {{
            width: 44px;
            height: 44px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 22px;
            flex-shrink: 0;
        }}

        .event-card-title {{
            font-size: 17px;
            font-weight: 700;
            color: #0f172a;
            line-height: 1.4;
        }}

        .event-card-org {{
            font-size: 13.5px;
            color: #475569;
        }}

        .event-card-desc {{
            font-size: 14px;
            color: #475569;
            line-height: 1.6;
        }}

        .event-tag-pill {{
            font-size: 11.5px;
            font-weight: 600;
            color: #475569;
            background: #f1f5f9;
            border: 1px solid #e2e8f0;
            border-radius: 6px;
            padding: 3px 8px;
            margin-right: 5px;
            margin-bottom: 5px;
            display: inline-block;
        }}

        .btn-event-link {{
            background: #f8fafc;
            border: 1px solid #cbd5e1;
            color: #1e293b;
            font-size: 12.5px;
            font-weight: 600;
            padding: 5px 12px;
            border-radius: 8px;
            display: inline-flex;
            align-items: center;
            transition: all 0.2s ease;
            text-decoration: none !important;
        }}
        .btn-event-link:hover {{
            background: #4f46e5;
            color: #ffffff !important;
            border-color: #4f46e5;
            box-shadow: 0 2px 8px rgba(79, 70, 229, 0.2);
        }}

        .copy-event-btn {{
            border-radius: 8px;
            padding: 4px 8px;
            transition: all 0.2s ease;
        }}
        .copy-event-btn:hover {{
            background: #f1f5f9;
            border-color: #94a3b8;
        }}

        /* Dark Mode Overrides */
        body.dark-mode .events-page-wrapper {{
            background-color: #090e17;
            background-image: 
                radial-gradient(circle at 15% 15%, rgba(99, 102, 241, 0.08) 0%, transparent 40%),
                radial-gradient(circle at 85% 35%, rgba(124, 58, 237, 0.08) 0%, transparent 45%),
                radial-gradient(circle at 50% 85%, rgba(14, 165, 233, 0.06) 0%, transparent 50%);
        }}
        body.dark-mode .events-controls-box,
        body.dark-mode .event-hub-card {{
            background: #0f172a;
            border-color: #1e293b;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        }}
        body.dark-mode .event-card-title {{
            color: #f1f5f9;
        }}
        body.dark-mode .event-card-desc,
        body.dark-mode .event-card-org {{
            color: #94a3b8;
        }}
        body.dark-mode .event-search-input {{
            background: #1e293b;
            border-color: #334155;
            color: #f8fafc;
        }}
        body.dark-mode .event-search-input:focus {{
            background: #0f172a;
            border-color: #6366f1;
        }}
        body.dark-mode .event-filter-pill {{
            background: #1e293b;
            border-color: #334155;
            color: #cbd5e1;
        }}
        body.dark-mode .event-filter-pill:hover {{
            background: #334155;
            color: #ffffff;
        }}
        body.dark-mode .event-filter-pill.active {{
            background: #4f46e5;
            color: #ffffff;
            border-color: #4f46e5;
        }}
        body.dark-mode .event-tag-pill {{
            background: #1e293b;
            border-color: #334155;
            color: #94a3b8;
        }}
        body.dark-mode .btn-event-link {{
            background: #1e293b;
            border-color: #334155;
            color: #cbd5e1 !important;
        }}
        body.dark-mode .btn-event-link:hover {{
            background: #4f46e5;
            border-color: #4f46e5;
            color: #ffffff !important;
        }}
        body.dark-mode .copy-event-btn {{
            background: #1e293b;
            border-color: #334155;
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
                    <li class="nav-item">
                        <a class="nav-link" href="page-about">About</a>
                    </li>
                    <li class="nav-item active">
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

    <div class="events-page-wrapper pt-5 pb-5">
        <div class="container" style="margin-top: 80px;">
            
            <!-- Hero Card -->
            <div class="events-hero-card">
                <div class="row align-items-center">
                    <div class="col-lg-8">
                        <span class="badge badge-pill font-weight-bold px-3 py-1 mb-3 text-white" style="background: rgba(99, 102, 241, 0.35); border: 1px solid rgba(165, 180, 252, 0.4);">
                            <i class="mdi mdi-microphone-variant mr-1"></i> Speaking Engagements &amp; Ecosystem Leadership
                        </span>
                        <h1 class="font-weight-bold text-white mb-2" style="font-size: 32px; letter-spacing: -0.5px;">
                            Speaking Engagements &amp; Keynotes
                        </h1>
                        <p class="text-light mb-4" style="font-size: 15.5px; line-height: 1.7; max-width: 680px; opacity: 0.9;">
                            Active ecosystem engagement across tier-1 venture accelerators, global hackathons, IEEE/ACM international conferences, and executive AI engineering summits. Dedicated to mentoring founders, reviewing peer scholarship, and defining autonomous AI standards.
                        </p>
                        <div class="d-flex flex-wrap align-items-center">
                            <div class="stat-metric-pill">
                                <div class="stat-metric-val">{total_judging}</div>
                                <div class="stat-metric-label">Judging &amp; Mentorship</div>
                            </div>
                            <div class="stat-metric-pill">
                                <div class="stat-metric-val">{total_confs}</div>
                                <div class="stat-metric-label">Conferences &amp; Keynotes</div>
                            </div>
                            <div class="stat-metric-pill">
                                <div class="stat-metric-val">{total_panels}</div>
                                <div class="stat-metric-label">Panel Discussions</div>
                            </div>
                            <div class="stat-metric-pill">
                                <div class="stat-metric-val">{total_events}+</div>
                                <div class="stat-metric-label">Total Engagements</div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 text-center mt-4 mt-lg-0">
                        <div class="p-3 rounded border border-secondary" style="background: rgba(15, 23, 42, 0.6); backdrop-filter: blur(10px);">
                            <img src="images/SectaAI_BTRPHBqq~2.jpg" alt="Harsh Verma" class="rounded shadow-sm mb-3" style="max-height: 180px; object-fit: cover; border: 2px solid rgba(255,255,255,0.2);">
                            <h6 class="text-white font-weight-bold mb-1">Harsh Verma</h6>
                            <p class="text-muted mb-2" style="font-size: 12.5px;">Principal Software Engineer in AI @ Palo Alto Networks &bull; Forbes Tech Council</p>
                            <a href="mailto:harshverma59@gmail.com?subject=Speaking%20or%20Judging%20Invitation" class="btn btn-sm btn-primary rounded font-weight-bold px-3 py-1" style="background: #4f46e5; border: none;">
                                <i class="mdi mdi-email-send-outline mr-1"></i> Invite for Keynote / Panel
                            </a>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Search and Filter Section -->
            <div class="events-controls-box">
                <div class="row align-items-center">
                    <div class="col-lg-5 mb-3 mb-lg-0">
                        <div class="position-relative">
                            <i class="mdi mdi-magnify search-icon-pos"></i>
                            <input type="text" id="eventSearchInput" class="event-search-input" placeholder="Search by topic, conference, company, or keyword (e.g. Berkeley, Keynote, Agentic)..." />
                        </div>
                    </div>
                    <div class="col-lg-7">
                        <div class="d-flex flex-wrap align-items-center justify-content-lg-end">
                            <button class="event-filter-pill active" data-filter="all">
                                <i class="mdi mdi-view-grid-outline"></i> All Engagements ({total_events})
                            </button>
                            <button class="event-filter-pill" data-filter="judging">
                                <i class="mdi mdi-gavel"></i> Judging &amp; Mentorship ({total_judging})
                            </button>
                            <button class="event-filter-pill" data-filter="conferences">
                                <i class="mdi mdi-microphone"></i> Keynotes &amp; Conferences ({total_confs})
                            </button>
                            <button class="event-filter-pill" data-filter="panels">
                                <i class="mdi mdi-account-group"></i> Panels &amp; Salons ({total_panels})
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Events Grid -->
            <div class="row" id="eventsContainer">
                {all_judging}
                {all_confs}
                {all_panels}
            </div>

            <!-- No results banner -->
            <div id="noEventsFound" class="text-center py-5 d-none">
                <div class="p-5 bg-white rounded shadow-sm border mx-auto" style="max-width: 500px;">
                    <i class="mdi mdi-calendar-remove text-muted mb-3" style="font-size: 48px;"></i>
                    <h5 class="font-weight-bold text-dark mb-2">No Matching Engagements Found</h5>
                    <p class="text-muted mb-3" style="font-size: 14px;">Try searching for a different keyword or reset the active filter category.</p>
                    <button class="btn btn-primary btn-sm rounded px-3 py-2 font-weight-bold" onclick="resetEventFilters()">
                        <i class="mdi mdi-refresh mr-1"></i> Reset All Filters
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

    <!-- Scripts -->
    <script src="js/jquery.min.js"></script>
    <script src="js/bootstrap.bundle.min.js"></script>
    <script src="js/jquery.easing.min.js"></script>
    <script src="js/scrollspy.min.js"></script>
    <script src="js/feather.min.js"></script>
    <script src="js/app.js"></script>

    <script>
        var yearEl = document.getElementById('currentYear');
        if (yearEl) yearEl.innerText = new Date().getFullYear();

        // Search & Filter Logic
        $(document).ready(function() {{
            var currentCategory = "all";
            var currentSearchQuery = "";

            function applyFilters() {{
                var matchCount = 0;
                $(".event-card-item").each(function() {{
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
                    $("#noEventsFound").removeClass("d-none");
                }} else {{
                    $("#noEventsFound").addClass("d-none");
                }}
            }}

            $(".event-filter-pill").on("click", function() {{
                $(".event-filter-pill").removeClass("active");
                $(this).addClass("active");
                currentCategory = $(this).attr("data-filter");
                applyFilters();
            }});

            $("#eventSearchInput").on("keyup input", function() {{
                currentSearchQuery = $(this).val().trim();
                applyFilters();
            }});
        }});

        function resetEventFilters() {{
            $("#eventSearchInput").val("");
            $(".event-filter-pill").removeClass("active");
            $(".event-filter-pill[data-filter='all']").addClass("active");
            $(".event-card-item").fadeIn(150);
            $("#noEventsFound").addClass("d-none");
        }}

        function copyEventInfo(id, title) {{
            var textToCopy = title + " - Harsh Verma (Principal AI Engineer | Speaker & Judge)";
            if (navigator.clipboard) {{
                navigator.clipboard.writeText(textToCopy).then(function() {{
                    alert("Copied event summary to clipboard:\\n\\n" + textToCopy);
                }}).catch(function() {{
                    prompt("Copy event summary:", textToCopy);
                }});
            }} else {{
                prompt("Copy event summary:", textToCopy);
            }}
        }}
    </script>
</body>
</html>
"""

if __name__ == "__main__":
    html_content = build_full_page()
    with open("page-events.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated page-events.html successfully with all events.")
