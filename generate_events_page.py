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
            "id": "judge-dent-demos-dimsum",
            "title": "Demos & Dim Sum — #SFTechWeek",
            "organization": "Dent Capital, The MBA Fund, Deel & Manatt",
            "role": "Dent Expert Network Judging Panel",
            "category": "Demo Day & Venture Judging",
            "date": "October 7, 2026",
            "location": "Chinatown, San Francisco, CA",
            "description": "Serving on the official Dent Expert Network judging panel for 'Demos & Dim Sum' during SF Tech Week, co-hosted with Dent Capital, The MBA Fund, Deel, and Manatt. Evaluating live startup demos from high-growth founders across AI, enterprise software, and frontier technologies.",
            "links": [
                {"name": "Partiful Event Page", "url": "https://partiful.com/e/WBHEUDs7uFJo6xSAyN2S", "icon": "mdi-ticket-confirmation"},
                {"name": "LinkedIn Announcement", "url": "https://www.linkedin.com/posts/dentcapital_rsvp-to-demos-dim-sum-sftechweek-partiful-activity-7508645069487263744-Wioj", "icon": "mdi-linkedin"}
            ],
            "tags": ["SF Tech Week", "Dent Capital", "Dent Expert Network", "Demos & Dim Sum", "Startup Judging", "San Francisco"],
            "gradient": "from-amber-600 to-yellow-500",
            "badge_color": "#d97706",
            "icon": "mdi-gavel"
        },
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
            "title": "UPES & IEEE ICACSDF 2026 Keynote & Technical Session Chair",
            "event_name": "International Conference on Advancement in Cyber Security and Digital Forensics (ICACSDF 2026)",
            "role": "Keynote Speaker, Technical Session Chair & Reviewer",
            "date": "2026",
            "location": "Dehradun, India / Hybrid",
            "description": "Delivered keynote address on 'When Enterprises Become Multi-Agent Systems', analyzing adversarial resilience, security perimeters, and autonomous decisioning in modern enterprise AI. Also served as Technical Session Chair presiding over conference research paper presentations, alongside evaluating manuscripts on the Microsoft CMT research review board.",
            "links": [
                {"name": "Keynote Smart Slides (Deck r92g)", "url": "https://www.harshverma.me/page-smart-slides#deck=r92g&slide=1", "icon": "mdi-presentation-play"},
                {"name": "ICACSDF Keynote Page", "url": "https://www.icacsdf.org/keynotes.html", "icon": "mdi-web"},
                {"name": "Microsoft CMT Portal", "url": "https://cmt3.research.microsoft.com/User/Login?ReturnUrl=%2F", "icon": "mdi-microsoft"}
            ],
            "tags": ["IEEE ICACSDF", "Technical Session Chair", "Keynote Talk", "Cybersecurity", "Digital Forensics", "Multi-Agent Systems"],
            "gradient": "from-blue-700 to-indigo-800",
            "badge_color": "#1d4ed8",
            "icon": "mdi-microphone-variant",
            "thumbnail": "images/events/icacsdf.svg"
        },
        {
            "id": "conf-iciotcaa-2026",
            "title": "ICIoTCAA-2026 Keynote & Fellow Member: AI-Enhanced Enterprise Security",
            "event_name": "International Conference on Internet of Things, Computing, and AI Applications (ICIoTCAA-2026)",
            "role": "Distinguished Keynote Speaker & Inducted Fellow Member",
            "date": "2026",
            "location": "International / Virtual",
            "description": "Keynote presentation titled 'Building an AI-Enhanced Enterprise Security Solution Using Artificial Intelligence in Cybersecurity', demonstrating real-time behavioral anomaly detection and threat isolation. Inducted as an official Fellow Member at Science Tech Xplore / ICIoTCAA in recognition of advanced contributions to cybersecurity, artificial intelligence, and computing systems.",
            "links": [
                {"name": "Fellow Member Directory", "url": "https://sciencetechxplore.org/fellow-members1.php", "icon": "mdi-certificate"},
                {"name": "Keynote Announcement", "url": "https://sciencetechxplore.org/conference/keynoteby-ICIoTCAA-2026.php", "icon": "mdi-bullhorn"}
            ],
            "tags": ["ICIoTCAA", "Fellow Member", "Enterprise Security", "Keynote", "Science Tech Xplore"],
            "gradient": "from-purple-800 to-indigo-800",
            "badge_color": "#6b21a8",
            "icon": "mdi-presentation-play",
            "thumbnail": "images/events/iciotcaa.svg"
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
            "icon": "mdi-brain",
            "thumbnail": "images/events/ai_salon.svg"
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
            "icon": "mdi-chart-line",
            "thumbnail": "images/events/ai_salon.svg"
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
            "icon": "mdi-hammer-wrench",
            "thumbnail": "images/events/ai_salon.svg"
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
                {"name": "Conference Speakers Profile", "url": "https://gtr2017.agiletestingalliance.org/speakers/#harshv", "icon": "mdi-web"},
                {"name": "SlideShare Deck", "url": "https://www.slideshare.net/ATASlides/atagtr2017-hikerunner-load-test-framework", "icon": "mdi-file-powerpoint"}
            ],
            "tags": ["ATAGTR", "HikeRunner", "Distributed Systems", "Load Testing"],
            "gradient": "from-slate-700 to-blue-800",
            "badge_color": "#334155",
            "icon": "mdi-speedometer",
            "thumbnail": "images/events/atagtr.svg"
        }
    ],
    "panels": [
        {
            "id": "panel-ai-security-sftechweek",
            "title": "AI × Security during SF Tech Week: Securing the AI Supply Chain",
            "event_name": "Hosted by AI Insiders in SF Tech Week (with Pebblebed)",
            "role": "Featured Panel Speaker",
            "category": "AI Security Panel",
            "date": "October 6, 2026",
            "location": "San Francisco, CA",
            "description": "Featured speaker on 'YOUR AGENT INSTALLED WHAT? SECURING THE NEW AI SUPPLY CHAIN' hosted by AI Insiders with Pebblebed during SF Tech Week. Addressed emerging threats across the agentic supply chain: unauthorized plugin and skill installations, MCP integration risks, runtime agent sandboxing, prompt provenance, and zero-trust controls.",
            "links": [
                {"name": "Partiful Event Page", "url": "https://partiful.com/e/8LNyv0WyX7dTHjUUJmm0", "icon": "mdi-ticket-confirmation"},
                {"name": "LinkedIn Announcement", "url": "https://lnkd.in/p/eyfEarGz", "icon": "mdi-linkedin"}
            ],
            "tags": ["SF Tech Week", "AI Insiders", "Securing AI Supply Chain", "Pebblebed", "Agent Security", "Zero Trust", "San Francisco"],
            "gradient": "from-rose-600 to-indigo-700",
            "badge_color": "#e11d48",
            "icon": "mdi-shield-lock-outline"
        },
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

keynote_videos_data = [
    {
        "id": "RS_BKcbeV3o",
        "title": "ACM Sacramento Keynote: When Enterprises Become Multi-Agent Systems",
        "outlet": "ACM Distinguished Keynote Session",
        "date": "2026 Keynote Session",
        "duration": "38:42",
        "category": "acm",
        "thumb": "https://img.youtube.com/vi/RS_BKcbeV3o/hqdefault.jpg",
        "recording_url": "https://www.youtube.com/watch?v=RS_BKcbeV3o",
        "desc": "Distinguished Keynote Address titled 'When Enterprises Become Multi-Agent Systems: Secure and Trustworthy Machine Learning & AI for Multi-Domain Applications', analyzing enterprise LLM defense, zero-trust validation, and autonomous agent alignment.",
        "slides_url": "https://www.harshverma.me/page-smart-slides#deck=GxwP&slide=1",
        "tags": ["ACM Keynote", "Secure AI", "Multi-Agent Systems", "Smart Slides"]
    },
    {
        "id": "IZvHxEtMMnw",
        "title": "UC Berkeley SkyDeck Keynote: The Era of Agentic Security",
        "outlet": "UC Berkeley SkyDeck Series (B21)",
        "date": "2025 Keynote Series",
        "duration": "42:15",
        "category": "acm",
        "thumb": "https://img.youtube.com/vi/IZvHxEtMMnw/hqdefault.jpg",
        "recording_url": "https://www.youtube.com/watch?v=IZvHxEtMMnw",
        "desc": "Keynote presentation at UC Berkeley SkyDeck detailing autonomous agent divergence, runtime safety guardrails, prompt provenance, and enterprise cybersecurity architectures.",
        "slides_url": "https://www.harshverma.me/page-smart-slides#deck=u8k2&slide=1",
        "tags": ["UC Berkeley", "Agentic Security", "SkyDeck B21", "Enterprise AI"]
    },
    {
        "id": "E6kA_o57DrM",
        "title": "SZ 179: The Digital Battleground — Quantum & Cyber Security",
        "outlet": "Silicon Zombies (Startup Zone / Top Voices Unite)",
        "date": "June 2025 Keynote Symposium",
        "duration": "52:14",
        "category": "zombies",
        "thumb": "https://img.youtube.com/vi/E6kA_o57DrM/hqdefault.jpg",
        "recording_url": "https://www.youtube.com/watch?v=E6kA_o57DrM",
        "desc": "Featured keynote symposium on Silicon Zombies Episode 179 alongside Rebecca Krauthamer (CEO of QuSecure), analyzing quantum computing vulnerabilities, post-quantum cryptographic perimeters, and autonomous AI defense systems.",
        "slides_url": "https://www.harshverma.me/page-smart-slides#deck=r92g&slide=1",
        "tags": ["Silicon Zombies", "SZ 179", "Quantum Security", "Autonomous Defense"]
    },
    {
        "id": "xraised-ai-beyond-code",
        "title": "xRaised Global Leadership: AI Engineering Beyond Code",
        "outlet": "xRaised Global Leadership Series",
        "date": "2026 Executive Series",
        "duration": "28:45",
        "category": "agentic",
        "thumb": "images/events/xraised_ai_engineering.jpg",
        "stream_url": "https://xraised.com/videos/ai-engineering-beyond-code/stream",
        "recording_url": "https://xraised.com/videos/ai-engineering-beyond-code/",
        "type": "video",
        "desc": "Executive keynote interview with Harsh Verma on 'Beyond the Code: The Evolution of the Next-Generation Engineer' — exploring autonomous agent architectures, multi-model production scaling, engineering leadership, and proactive cybersecurity in frontier AI systems.",
        "slides_url": "https://www.harshverma.me/page-smart-slides#deck=m74k&slide=1",
        "tags": ["xRaised Feature", "AI Engineering", "Autonomous Systems", "Beyond Code"]
    },
    {
        "id": "MPhFC1h5GIc",
        "title": "FutureAGI Keynote: Powering Cybersecurity with GenAI & Intelligent Agents",
        "outlet": "FutureAGI Global Keynote / SF Tech Week",
        "date": "2026 Global Keynote",
        "duration": "48:30",
        "category": "agentic",
        "thumb": "https://img.youtube.com/vi/MPhFC1h5GIc/hqdefault.jpg",
        "recording_url": "https://www.youtube.com/watch?v=MPhFC1h5GIc",
        "desc": "Keynote during SF Tech Week on scaling AI infrastructure, mitigating agentic risk, powering cybersecurity with generative AI, and driving enterprise AI adoption across Silicon Valley.",
        "slides_url": "https://www.harshverma.me/page-smart-slides#deck=u8k2&slide=1",
        "tags": ["FutureAGI", "GenAI Cybersecurity", "Intelligent Agents", "SF Tech Week"]
    },
    {
        "id": "nIgJ99Bihsw",
        "title": "Enterprise AI: Building Solutions for Security, Scale & Trust",
        "outlet": "TechTalk with VLink Keynote (Ep. 55)",
        "date": "2026 Keynote Episode",
        "duration": "46:18",
        "category": "agentic",
        "thumb": "https://img.youtube.com/vi/nIgJ99Bihsw/hqdefault.jpg",
        "recording_url": "https://www.youtube.com/watch?v=nIgJ99Bihsw",
        "desc": "Deep-dive executive presentation covering enterprise AI architectures, scaling multi-agent workloads, identity boundaries, and real-time behavioral defense.",
        "slides_url": "https://www.harshverma.me/page-smart-slides#deck=m74k&slide=1",
        "tags": ["Enterprise AI", "VLink Keynote", "Security & Scale", "Trustworthy Systems"]
    },
    {
        "id": "yXy_zYlhnfc",
        "title": "Inside Vibe Shift: The Builders Behind the Models",
        "outlet": "Rocket & Twill Special Keynote Session",
        "date": "2026 Keynote Session",
        "duration": "31:40",
        "category": "agentic",
        "thumb": "https://img.youtube.com/vi/yXy_zYlhnfc/hqdefault.jpg",
        "recording_url": "https://www.youtube.com/watch?v=yXy_zYlhnfc",
        "desc": "Keynote presentation at Rocket & Twill's 'Vibe Shift' summit analyzing consumer tech inflection points, LLMOps, model evaluation datasets, and scalable enterprise architectures.",
        "slides_url": "https://www.harshverma.me/page-smart-slides#deck=m74k&slide=1",
        "tags": ["Rocket & Twill", "Vibe Shift", "Builders Behind Models", "Observability"]
    },
    {
        "id": "iZkx6Ewq6wU",
        "title": "TrueML Keynote: Big Data & ML Practices at Palo Alto Networks",
        "outlet": "TrueML Talks #35",
        "date": "Production ML Keynote",
        "duration": "40:05",
        "category": "bigdata",
        "thumb": "https://img.youtube.com/vi/iZkx6Ewq6wU/hqdefault.jpg",
        "recording_url": "https://www.youtube.com/watch?v=iZkx6Ewq6wU",
        "desc": "Production machine learning engineering patterns, distributed feature pipelines, and zero-trust validation in high-throughput enterprise security systems.",
        "slides_url": "https://www.harshverma.me/page-smart-slides#deck=GxwP&slide=1",
        "tags": ["Palo Alto Networks", "TrueML", "Feature Pipelines", "Big Data ML"]
    },
    {
        "id": "bggw4JTFjgA",
        "title": "FutureAGI Keynote: Enterprise Agentic Security & Multi-Model Orchestration",
        "outlet": "FutureAGI Global Keynote",
        "date": "2026 Virtual Keynote",
        "duration": "35:20",
        "category": "agentic",
        "thumb": "https://img.youtube.com/vi/bggw4JTFjgA/hqdefault.jpg",
        "recording_url": "https://www.youtube.com/watch?v=bggw4JTFjgA",
        "desc": "Keynote on enterprise agentic security, multi-model orchestration frameworks, deterministic evaluation, and securing autonomous agent communication channels.",
        "slides_url": "https://www.harshverma.me/page-smart-slides#deck=r92g&slide=1",
        "tags": ["FutureAGI", "Multi-Agent Systems", "Orchestration", "Zero-Trust"]
    }
]

def render_keynote_hub():
    cards_html = ""
    for idx, v in enumerate(keynote_videos_data):
        active_class = "is-pinned" if idx == 0 else ""
        pin_btn_cls = "pinned" if idx == 0 else ""
        pin_btn_txt = "Pinned" if idx == 0 else "Pin Keynote"
        tags_badges = "".join([f'<span class="hv-video-tag">{t}</span>' for t in v["tags"][:3]])
        recording_url = v.get("recording_url") or f"https://www.youtube.com/watch?v={v['id']}"
        cards_html += f"""
        <div class="hv-carousel-item keynote-video-item" data-category="{v.get('category', 'all')}" id="carouselItem-{idx}">
            <div class="hv-video-card h-100 {active_class}" id="keynoteCard-{idx}">
                <button type="button" class="hv-video-pin-btn {pin_btn_cls}" id="pinBtn-{idx}" onclick="togglePinKeynote({idx}, event)" title="Pin this Keynote to Main Stage">
                    <i class="mdi mdi-pin mr-1"></i> <span class="pin-label-text">{pin_btn_txt}</span>
                </button>
                <div class="hv-video-thumb-wrap" onmouseenter="handleKeynoteHoverStart({idx}, this)" onmouseleave="handleKeynoteHoverEnd({idx}, this)" onclick="switchKeynoteVideo({idx})">
                    <img src="{v['thumb']}" alt="{v['title']}" class="hv-video-thumb-img" loading="lazy">
                    <div class="hv-hover-preview-container" id="hoverPreview-{idx}"></div>
                    <span class="hv-hover-preview-badge"><i class="mdi mdi-play"></i> Hover to Preview</span>
                    <div class="hv-video-play-overlay">
                        <div class="hv-play-circle-btn">
                            <i class="mdi mdi-play"></i>
                        </div>
                    </div>
                    <span class="hv-video-duration-tag">{v['duration']}</span>
                </div>
                <div class="hv-video-body">
                    <div class="d-flex align-items-center justify-content-between mb-1">
                        <span class="hv-video-outlet">{v['outlet']}</span>
                        <span class="badge badge-warning text-dark font-weight-bold px-2 py-1 pinned-badge-indicator {'' if idx == 0 else 'd-none'}" id="pinnedBadge-{idx}" style="font-size: 10px;">
                            <i class="mdi mdi-pin"></i> PINNED STAGE
                        </span>
                    </div>
                    <h5 class="hv-video-title" onclick="switchKeynoteVideo({idx})" style="cursor: pointer;" title="{v['title']}">{v['title']}</h5>
                    <p class="hv-video-desc">{v['desc']}</p>
                    <div class="hv-video-meta-tags">
                        {tags_badges}
                    </div>
                    <div class="hv-video-actions">
                        <button type="button" class="hv-card-action-btn hv-btn-stage" onclick="switchKeynoteVideo({idx})" title="Watch on Stage">
                            <i class="mdi mdi-television-play hv-btn-icon"></i> <span>Stage</span>
                        </button>
                        {f'''<a href="{recording_url}" target="_blank" class="hv-card-action-btn hv-btn-youtube allow-external-nav" title="Watch on YouTube">
                            <i class="mdi mdi-youtube hv-btn-icon text-danger"></i> <span>YouTube</span>
                        </a>''' if (v.get('type') != 'video' and ('youtube.com' in recording_url or 'youtu.be' in recording_url)) else f'''<a href="{recording_url}" target="_blank" class="hv-card-action-btn hv-btn-external allow-external-nav" title="Watch on External Platform">
                            <i class="mdi mdi-open-in-new hv-btn-icon"></i> <span>External</span>
                        </a>'''}
                        <a href="{v['slides_url']}" target="_blank" class="hv-card-action-btn hv-btn-slides allow-external-nav" title="View Keynote Slides">
                            <i class="mdi mdi-presentation hv-btn-icon"></i> <span>Slides</span>
                        </a>
                    </div>
                </div>
            </div>
        </div>
        """

    first_video = keynote_videos_data[0]
    first_tags = "".join([f'<span class="hv-video-tag">{t}</span>' for t in first_video["tags"]])
    first_recording = first_video.get("recording_url") or f"https://www.youtube.com/watch?v={first_video['id']}"
    dots_html = "".join([f'<button type="button" class="hv-carousel-dot { "active" if i == 0 else "" }" onclick="scrollKeynoteToDot({i})" aria-label="Go to keynote {i+1}"></button>' for i in range(len(keynote_videos_data))])

    return f"""
    <!-- Featured Keynote Video Stage & Interactive In-Page Player Hub -->
    <div class="hv-keynote-hub-container mb-5" id="keynote-video-hub">
        <!-- Banner Header -->
        <div class="hv-keynote-feature-banner">
            <div class="row align-items-center">
                <div class="col-lg-8">
                    <div class="d-flex align-items-center mb-2 flex-wrap">
                        <span class="hv-badge-gold mr-2 mb-1">
                            <i class="mdi mdi-pin"></i> Pinned Keynotes &amp; Featured Stage
                        </span>
                        <span class="hv-badge-indigo mb-1">
                            <i class="mdi mdi-video-vintage"></i> In-Page Live Cinema &amp; Smart Slides
                        </span>
                    </div>
                    <h2 class="font-weight-bold text-white mb-2" style="font-size: 1.85rem; letter-spacing: -0.3px;">
                        International Keynotes, AI Summits &amp; Executive Masterclasses
                    </h2>
                    <p class="text-light mb-0" style="font-size: 14.5px; opacity: 0.9; max-width: 720px; line-height: 1.6;">
                        Watch recorded keynote presentations delivered by Harsh Verma across ACM, UC Berkeley SkyDeck, xRaised Global Series, FutureAGI, TechTalks, and Silicon Valley venture summits. Pin any keynote or click play to watch live on stage.
                    </p>
                </div>
                <div class="col-lg-4 text-lg-right mt-3 mt-lg-0">
                    <button type="button" class="btn btn-warning font-weight-bold px-4 py-2 text-dark shadow-sm" onclick="if(window.openBookingModal){{window.openBookingModal('Executive Keynote & Advisory Consultation', 'Keynote Speech');}}else if(window.openKeynoteBooking){{window.openKeynoteBooking();}}return false;" data-booking-trigger="true" data-type="Keynote Speech" data-topic="Executive Keynote & Advisory Consultation" style="border-radius: 24px; font-size: 13.5px;">
                        <i class="mdi mdi-calendar-star mr-1"></i> Book for Keynote / Advisory
                    </button>
                </div>
            </div>

            <!-- In-Page Featured Video Player Frame -->
            <div class="mt-4 p-3 rounded hv-keynote-stage-player-card" style="background: rgba(11, 15, 25, 0.92); border: 1px solid rgba(99, 102, 241, 0.4); border-radius: 16px; box-shadow: 0 14px 40px rgba(0,0,0,0.6);">
                <div class="row align-items-center">
                    <div class="col-xl-8 col-lg-7">
                        <div class="hv-video-modal-player-wrap rounded" id="keynoteStagePlayerWrap" style="border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
                            <iframe id="keynoteStagePlayer" src="https://www.youtube.com/embed/{first_video['id']}?rel=0&enablejsapi=1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"></iframe>
                        </div>
                    </div>
                    <div class="col-xl-4 col-lg-5 mt-3 mt-lg-0 d-flex flex-column justify-content-between">
                        <div class="p-2">
                            <div class="d-flex align-items-center justify-content-between mb-2">
                                <span class="badge badge-pill badge-danger font-weight-bold px-3 py-1" id="stageCurrentBadge">
                                    <span class="live-indicator-dot"></span> NOW PLAYING ON STAGE
                                </span>
                                <span class="text-light small font-weight-bold" id="stageDurationTag" style="opacity: 0.95;">{first_video['duration']}</span>
                            </div>
                            <h4 class="font-weight-bold text-white mb-2" id="stageVideoTitle" style="font-size: 1.25rem; line-height: 1.35;">
                                {first_video['title']}
                            </h4>
                            <div class="text-primary font-weight-600 small mb-2" id="stageVideoOutlet">
                                <i class="mdi mdi-microphone-variant mr-1"></i> {first_video['outlet']}
                            </div>
                            <p class="text-light small mb-3" id="stageVideoDesc" style="opacity: 0.88; line-height: 1.6; max-height: 120px; overflow-y: auto;">
                                {first_video['desc']}
                            </p>
                            <div class="d-flex flex-wrap gap-1 mb-3" id="stageVideoTags">
                                {first_tags}
                            </div>
                        </div>
                        <div class="pt-2 border-top border-secondary d-flex flex-wrap align-items-center">
                            <button type="button" class="btn btn-sm btn-primary font-weight-bold px-3 py-2 mr-2 mb-2" onclick="retriggerStagePlay()" style="border-radius: 8px;">
                                <i class="mdi mdi-television-play mr-1"></i> Watch On Stage
                            </button>
                            <a id="stageWatchRecordingBtn" href="{first_recording}" target="_blank" class="btn btn-sm btn-outline-danger font-weight-bold px-3 py-2 mr-2 mb-2 allow-external-nav" style="border-radius: 8px;">
                                <i class="mdi {'mdi-youtube' if 'youtube.com' in first_recording or 'youtu.be' in first_recording else 'mdi-open-in-new'} mr-1"></i> {'Watch on YouTube' if 'youtube.com' in first_recording or 'youtu.be' in first_recording else 'Watch External'} <i class="mdi mdi-open-in-new ml-1" style="font-size: 11px;"></i>
                            </a>
                            <a id="stageSlidesBtn" href="{first_video['slides_url']}" target="_blank" class="btn btn-sm btn-outline-info font-weight-bold px-3 py-2 mr-2 mb-2 allow-external-nav" style="border-radius: 8px;">
                                <i class="mdi mdi-presentation mr-1"></i> Smart Slides
                            </a>
                            <button type="button" class="btn btn-sm btn-outline-light font-weight-bold px-3 py-2 mb-2" onclick="openKeynoteTheaterMode()" style="border-radius: 8px;">
                                <i class="mdi mdi-fullscreen mr-1"></i> Theater Modal
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Keynote Carousel Toolbar & Track -->
            <div class="mt-4 pt-3 border-top border-secondary">
                <div class="hv-video-stage-toolbar my-2">
                    <div class="hv-stage-filter-group">
                        <button type="button" class="hv-stage-filter-pill active" onclick="filterKeynoteVideos('all', this)">
                            <i class="mdi mdi-view-grid-outline"></i> All Keynotes ({len(keynote_videos_data)})
                        </button>
                        <button type="button" class="hv-stage-filter-pill" onclick="filterKeynoteVideos('zombies', this)">
                            <i class="mdi mdi-shield-lock-outline"></i> Silicon Zombies &amp; Cyber
                        </button>
                        <button type="button" class="hv-stage-filter-pill" onclick="filterKeynoteVideos('acm', this)">
                            <i class="mdi mdi-school"></i> ACM &amp; SkyDeck
                        </button>
                        <button type="button" class="hv-stage-filter-pill" onclick="filterKeynoteVideos('agentic', this)">
                            <i class="mdi mdi-robot"></i> Agentic AI &amp; xRaised
                        </button>
                        <button type="button" class="hv-stage-filter-pill" onclick="filterKeynoteVideos('bigdata', this)">
                            <i class="mdi mdi-database"></i> Big Data &amp; Systems
                        </button>
                    </div>
                    <div class="d-flex align-items-center gap-2">
                        <div class="hv-quick-select-wrap mr-2">
                            <span class="text-light small font-weight-bold d-none d-sm-inline"><i class="mdi mdi-swap-horizontal text-warning"></i> Jump to:</span>
                            <select class="hv-quick-select" onchange="if(this.value!=='') switchKeynoteVideo(parseInt(this.value));">
                                {''.join([f'<option value="{idx}">{v["outlet"]}: {v["title"][:36]}...</option>' for idx, v in enumerate(keynote_videos_data)])}
                            </select>
                        </div>
                        <div class="hv-carousel-controls">
                            <button type="button" class="hv-carousel-nav-btn prev" onclick="scrollKeynoteCarousel(-1)" aria-label="Previous Keynote">
                                <i class="mdi mdi-chevron-left"></i>
                            </button>
                            <button type="button" class="hv-carousel-nav-btn next" onclick="scrollKeynoteCarousel(1)" aria-label="Next Keynote">
                                <i class="mdi mdi-chevron-right"></i>
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Visually Immersive Keynote Carousel Track -->
                <div class="hv-carousel-wrapper">
                    <div class="hv-carousel-track" id="keynoteCarouselTrack">
                        {cards_html}
                    </div>
                    <div class="hv-carousel-dots" id="keynoteCarouselDots">
                        {dots_html}
                    </div>
                </div>
            </div>
        </div>

        <!-- Theater Video Modal Component -->
        <div class="hv-video-modal-overlay" id="keynoteTheaterModal" onclick="closeKeynoteVideoModal(event)">
            <div class="hv-video-modal-card" onclick="event.stopPropagation()">
                <div class="d-flex justify-content-between align-items-center p-3 border-bottom border-secondary bg-dark text-white">
                    <div class="d-flex align-items-center">
                        <span class="badge badge-warning text-dark font-weight-bold px-2 py-1 mr-2" style="font-size: 11px;">
                            <i class="mdi mdi-video-vintage mr-1"></i> THEATER MODE
                        </span>
                        <h5 class="mb-0 font-weight-bold text-truncate" id="theaterModalTitle" style="max-width: 580px; font-size: 15px;">Keynote Cinema</h5>
                    </div>
                    <button type="button" class="btn btn-sm btn-outline-light rounded-circle" onclick="closeKeynoteVideoModal()" style="width: 32px; height: 32px; padding: 0;" title="Close Modal">
                        <i class="mdi mdi-close"></i>
                    </button>
                </div>
                <div class="hv-video-modal-player-wrap">
                    <iframe id="theaterModalIframe" src="" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                </div>
                <div class="p-3 bg-dark text-light border-top border-secondary d-flex justify-content-between align-items-center flex-wrap">
                    <div class="small text-muted" id="theaterModalOutlet">Featured Keynote Presentation</div>
                    <a id="theaterModalRecordingLink" href="#" target="_blank" class="btn btn-sm btn-danger font-weight-bold px-3 py-1">
                        <i class="mdi mdi-youtube mr-1"></i> Open in YouTube
                    </a>
                </div>
            </div>
        </div>

        <!-- Speaker Bio Press Kit Bar -->
        <div class="hv-press-kit-box mt-4">
            <div class="d-flex flex-wrap justify-content-between align-items-center mb-3">
                <div>
                    <span class="badge badge-pill badge-primary font-weight-bold px-3 py-1 mb-1">
                        <i class="mdi mdi-card-account-details-outline mr-1"></i> Official Speaker Press Kit
                    </span>
                    <h4 class="font-weight-bold text-dark mb-0 mt-1" style="font-size: 1.25rem;">
                        Conference Organizer Resources &amp; Verified Bios
                    </h4>
                </div>
                <div class="mt-2 mt-md-0">
                    <span class="text-muted small">One-click copy for conference brochures &amp; event guides</span>
                </div>
            </div>
            <div class="hv-bio-tab-nav">
                <button type="button" class="hv-bio-tab-btn active" onclick="switchSpeakerBioTab('short', this)">
                    <i class="mdi mdi-text-short mr-1"></i> Short Bio (65 words)
                </button>
                <button type="button" class="hv-bio-tab-btn" onclick="switchSpeakerBioTab('medium', this)">
                    <i class="mdi mdi-text-box-outline mr-1"></i> Medium Bio (130 words)
                </button>
                <button type="button" class="hv-bio-tab-btn" onclick="switchSpeakerBioTab('full', this)">
                    <i class="mdi mdi-file-document-outline mr-1"></i> Comprehensive Keynote Bio
                </button>
            </div>
            <div class="hv-bio-content-area" id="speakerBioContentArea">
                Harsh Verma is a Principal Software Engineer in AI at Palo Alto Networks, Forbes Technology Council Member, IEEE Senior Member, and author of two books on Enterprise AI. Recognized on the Forttuna Global 100 Power List and Nobel Technology Awards Gold (#145), he architects deterministic agentic systems, zero-trust cloud perimeters, and high-throughput data platforms, keynoting across UC Berkeley SkyDeck and international AI symposiums.
            </div>
            <div class="d-flex flex-wrap justify-content-between align-items-center">
                <button type="button" class="btn btn-sm btn-primary font-weight-bold px-3 py-2" onclick="copyCurrentBioText()" style="border-radius: 8px;">
                    <i class="mdi mdi-content-copy mr-1"></i> Copy Selected Bio to Clipboard
                </button>
                <div class="mt-2 mt-sm-0">
                    <span class="text-muted small mr-2">Speaker Headshot:</span>
                    <a href="images/harsh/Harsh_portfolio_pic.png" download="Harsh_Verma_Keynote_Headshot.png" class="btn btn-sm btn-outline-secondary font-weight-bold px-3 py-1" style="border-radius: 8px;">
                        <i class="mdi mdi-download mr-1"></i> High-Res Portrait (.PNG)
                    </a>
                </div>
            </div>
        </div>
    </div>
    """

def render_links(links):
    html = ""
    for link in links:
        url = link.get('url', '')
        is_video = 'youtube.com' in url or 'youtu.be' in url or 'xraised.com/videos' in url
        if is_video:
            html += f"""
        <a href="{url}" onclick="playUrlOnStage('{url}'); return false;" class="btn-event-link mr-2 mb-2" title="Play on Keynote Stage: {link['name']}">
            <i class="mdi {link['icon']} mr-1"></i> {link['name']}
        </a>
        """
        else:
            html += f"""
        <a href="{url}" target="_blank" class="btn-event-link mr-2 mb-2" title="{link['name']}">
            <i class="mdi {link['icon']} mr-1"></i> {link['name']}
        </a>
        """
    return html

def render_tags(tags):
    html = ""
    for tag in tags:
        html += f"""<span class="event-tag-pill">{tag}</span>"""
    return html

def get_event_thumbnail(item):
    if item.get("thumbnail"):
        return item["thumbnail"]
    
    # Check if this item has a recorded video or youtube link
    yid = item.get("youtube_id")
    if not yid:
        for link in item.get("links", []):
            url = link.get("url", "")
            if "youtube.com/watch?v=" in url:
                yid = url.split("v=")[1].split("&")[0].split("?")[0]
                break
            elif "youtu.be/" in url:
                yid = url.split("youtu.be/")[1].split("?")[0].split("&")[0]
                break
    if yid:
        return f"https://img.youtube.com/vi/{yid}/hqdefault.jpg"

    eid = item.get("id", "").lower()
    org = (item.get("organization", "") + " " + item.get("event_name", "") + " " + item.get("title", "")).lower()
    
    mapping = [
        ("xraised", "images/events/xraised_ai_engineering.jpg"),
        ("silicon-zombies", "images/events/silicon_zombies.svg"),
        ("silicon zombies", "images/events/silicon_zombies.svg"),
        ("zombie", "images/events/silicon_zombies.svg"),
        ("skydeck", "images/events/skydeck.svg"),
        ("berkeley", "images/events/skydeck.svg"),
        ("dent", "images/events/dent.svg"),
        ("techstars", "images/events/techstars.svg"),
        ("mayfield", "images/events/mayfield.svg"),
        ("genlabx", "images/events/genlabx.svg"),
        ("lovehack", "images/events/lovehack.svg"),
        ("future of work", "images/events/future_of_work.svg"),
        ("fow", "images/events/future_of_work.svg"),
        ("techpioneer", "images/events/techpioneers.svg"),
        ("vc-conf", "images/events/vc_conf.svg"),
        ("vc_conf", "images/events/vc_conf.svg"),
        ("hackmakers", "images/events/hackmakers.svg"),
        ("buildwithai", "images/events/hackmakers.svg"),
        ("progressive", "images/events/progressive_ventures.svg"),
        ("ai-salon", "images/events/ai_salon.svg"),
        ("deepseek", "images/events/ai_salon.svg"),
        ("salon", "images/events/ai_salon.svg"),
        ("founders", "images/events/founders_creative.svg"),
        ("packt", "images/events/packt.svg"),
        ("icacsdf", "images/events/icacsdf.svg"),
        ("acm", "images/events/acm.svg"),
        ("iciotcaa", "images/events/iciotcaa.svg"),
        ("atagtr", "images/events/atagtr.svg"),
        ("hikerunner", "images/events/atagtr.svg"),
        ("ai-security", "images/events/ai_insiders.svg"),
        ("insiders", "images/events/ai_insiders.svg"),
        ("pebblebed", "images/events/ai_insiders.svg"),
        ("the agentic", "images/events/the_agentic.svg"),
        ("agentic", "images/events/the_agentic.svg"),
        ("twill", "images/events/twill_rocket.svg"),
        ("rocket", "images/events/twill_rocket.svg"),
        ("health", "images/events/healthtech.svg"),
        ("trueml", "images/events/trueml.svg"),
        ("vlink", "images/events/vlink.svg"),
        ("futureagi", "images/events/futureagi.svg"),
        ("sf-techweek", "images/events/sf_tech_week.svg"),
        ("sf tech week", "images/events/sf_tech_week.svg"),
        ("ijeetr", "images/events/ijeetr.svg"),
        ("jrtcse", "images/events/jrtcse.svg"),
        ("ieee", "images/events/ieee.svg")
    ]
    for key, path in mapping:
        if key in eid or key in org:
            return path
    return "images/events/acm.svg"

def generate_card(item, event_type):
    badge_type_text = {
        "judging": "Judging & Mentorship",
        "conferences": "Keynote & Conference",
        "panels": "Panel & Thought Leadership"
    }.get(event_type, "Event")
    
    badge_bg = item.get("badge_color", "#2563eb")
    category = item.get("category") or item.get("role") or badge_type_text
    search_keywords = f"{item['title']} {item.get('organization', '')} {item.get('event_name', '')} {item.get('role', '')} {category} {item['location']} {' '.join(item.get('tags', []))}".lower()

    # Determine if this item has a recorded video
    yid = item.get("youtube_id")
    if not yid:
        for link in item.get("links", []):
            url = link.get("url", "")
            if "youtube.com/watch?v=" in url:
                yid = url.split("v=")[1].split("&")[0].split("?")[0]
                break
            elif "youtu.be/" in url:
                yid = url.split("youtu.be/")[1].split("?")[0].split("&")[0]
                break

    thumb_img = get_event_thumbnail(item)
    links_html = render_links(item.get("links", []))
    tags_html = render_tags(item.get("tags", []))
    org_or_event = item.get("organization") or item.get("event_name") or ""

    if yid:
        escaped_title = item['title'].replace("'", "\\'")
        escaped_org = org_or_event.replace("'", "\\'")
        escaped_desc = item['description'][:140].replace("'", "\\'")
        header_html = f"""
            <!-- Event Card Video Thumbnail Banner -->
            <div class="event-card-video-banner" onclick="playUrlOnStage('https://www.youtube.com/watch?v={yid}')" title="Click to Play on Keynote Stage">
                <img src="https://img.youtube.com/vi/{yid}/hqdefault.jpg" alt="{item['title']}" class="event-card-video-cover" loading="lazy">
                <div class="event-card-video-overlay">
                    <div class="event-video-play-btn">
                        <i class="mdi mdi-play"></i>
                    </div>
                    <span class="event-video-play-label">WATCH ON STAGE</span>
                </div>
                <div class="event-card-video-top-meta">
                    <span class="badge badge-danger font-weight-bold px-2 py-1 event-video-badge shadow-sm">
                        <i class="mdi mdi-youtube mr-1"></i> Recorded Keynote
                    </span>
                    <span class="badge badge-pill text-white font-weight-bold px-2 py-1 shadow-sm" style="background: {badge_bg}; font-size: 11px;">
                        {category}
                    </span>
                </div>
                <div class="event-card-video-bottom-meta">
                    <span class="event-meta-badge"><i class="mdi mdi-map-marker-outline mr-1"></i> {item['location']}</span>
                    <span class="event-meta-badge"><i class="mdi mdi-calendar-outline mr-1"></i> {item['date']}</span>
                </div>
            </div>
        """
    else:
        header_html = f"""
            <!-- Event Card Branded Header -->
            <div class="event-card-branded-header">
                <div class="event-card-org-logo-box">
                    <img src="{thumb_img}" alt="{org_or_event or item['title']}" class="event-card-org-logo-img" loading="lazy" onerror="this.onerror=null; this.src='images/events/acm.svg';">
                </div>
                <div class="event-card-header-meta flex-grow-1 min-w-0">
                    <div class="d-flex align-items-center justify-content-between mb-1">
                        <span class="badge badge-pill text-white font-weight-bold px-2 py-1" style="background: {badge_bg}; font-size: 11px;">
                            {category}
                        </span>
                        <button class="btn btn-sm btn-light border copy-event-btn" onclick="copyEventInfo('{item['id']}', '{item['title']}')" title="Copy Event Details" aria-label="Copy Details">
                            <i class="mdi mdi-content-copy text-muted"></i>
                        </button>
                    </div>
                    <div class="event-org-name font-weight-bold text-muted text-truncate" style="font-size: 12.5px;">
                        <i class="mdi mdi-map-marker-outline mr-1 text-primary"></i> {item['location']} &bull; <i class="mdi mdi-calendar-outline ml-1 mr-1 text-primary"></i> {item['date']}
                    </div>
                </div>
            </div>
        """

    return f"""
    <div class="col-lg-6 col-md-12 mb-4 event-card-item" data-category="{event_type}" data-search="{search_keywords}">
        <div class="event-hub-card h-100 d-flex flex-column">
            {header_html}
            <div class="event-card-body p-4 d-flex flex-column flex-grow-1">
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
    </div>
    """

def build_full_page():
    # Deduplicate: recorded keynotes from the top section must NOT appear as cards below!
    featured_keynote_ids = {v['id'] for v in keynote_videos_data}
    featured_keynote_urls = {v.get('recording_url', '') for v in keynote_videos_data} | {f"https://www.youtube.com/watch?v={v['id']}" for v in keynote_videos_data}

    def is_featured_in_top(item):
        if item.get('youtube_id') in featured_keynote_ids:
            return True
        if item.get('id') in ['panel-silicon-zombies-sz179', 'panel-twill-vibe-shift', 'conf-acm-sacramento-2026', 'conf-skydeck-agentic-security', 'conf-silicon-zombies-sz179', 'conf-futureagi-enterprise-agentic', 'conf-vlink-techtalk-55', 'conf-trueml-paloaltonetworks', 'conf-sf-techweek-masterclass', 'conf-xraised-ai-beyond-code']:
            return True
        for link in item.get('links', []):
            url = link.get('url', '')
            if url in featured_keynote_urls:
                return True
            for kid in featured_keynote_ids:
                if kid and kid in url:
                    return True
        return False

    filtered_judging = [item for item in events_data["judging"] if not is_featured_in_top(item)]
    filtered_confs = [item for item in events_data["conferences"] if not is_featured_in_top(item)]
    filtered_panels = [item for item in events_data["panels"] if not is_featured_in_top(item)]

    all_judging = "".join([generate_card(item, "judging") for item in filtered_judging])
    all_confs = "".join([generate_card(item, "conferences") for item in filtered_confs])
    all_panels = "".join([generate_card(item, "panels") for item in filtered_panels])

    total_events = len(filtered_judging) + len(filtered_confs) + len(filtered_panels) + len(keynote_videos_data)
    total_judging = len(filtered_judging)
    total_confs = len(filtered_confs)
    total_panels = len(filtered_panels)
    total_keynotes = len(keynote_videos_data)
    keynote_json = json.dumps(keynote_videos_data)

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
    
    <!-- Mastodon Verification -->
    <link rel="me" href="https://mastodon.social/@harshverma59">
    <a rel="me" href="https://mastodon.social/@harshverma59" style="display:none;" aria-hidden="true">Mastodon</a>
    
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
    <!-- Keynote Hub & Video Player Styles -->
    <link href="css/hv-keynote-hub.css" rel="stylesheet" type="text/css" />
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

        /* Hero Banner (Original Dark Navy Theme) */
        .events-hero-card {{
            background: linear-gradient(135deg, #090e17 0%, #0f172a 45%, #1e1b4b 100%);
            border-radius: 20px;
            color: #ffffff;
            padding: 42px 36px;
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.45);
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(99, 102, 241, 0.35);
            margin-bottom: 36px;
        }}
        .events-hero-card::before {{
            content: "";
            position: absolute;
            top: -40%;
            right: -20%;
            width: 480px;
            height: 480px;
            background: radial-gradient(circle, rgba(99, 102, 241, 0.25) 0%, rgba(14, 165, 233, 0.12) 50%, transparent 70%);
            border-radius: 50%;
            pointer-events: none;
        }}
        .events-hero-title {{
            color: #ffffff !important;
        }}
        .hero-subtitle {{
            color: #cbd5e1 !important;
            opacity: 0.95;
        }}
        .hero-lead-badge {{
            background: rgba(99, 102, 241, 0.3) !important;
            border: 1px solid rgba(165, 180, 252, 0.35) !important;
            color: #ffffff !important;
        }}

        .stat-metric-pill {{
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 12px;
            padding: 12px 18px;
            display: inline-block;
            box-shadow: none;
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
            border-radius: 18px;
            padding: 0;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: transform 0.28s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.28s ease, border-color 0.28s ease;
            box-shadow: 0 4px 16px rgba(15, 23, 42, 0.05);
            position: relative;
        }}
        .event-hub-card:hover {{
            border-color: #6366f1;
            transform: translateY(-4px);
            box-shadow: 0 16px 36px rgba(79, 70, 229, 0.12);
        }}

        /* Video Banner Header for Recorded Keynotes */
        .event-card-video-banner {{
            position: relative;
            width: 100%;
            aspect-ratio: 16 / 9;
            max-height: 220px;
            background: #090e1a;
            overflow: hidden;
            cursor: pointer;
        }}
        .event-card-video-cover {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
            transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), filter 0.35s ease;
        }}
        .event-card-video-banner:hover .event-card-video-cover {{
            transform: scale(1.05);
            filter: brightness(1.08);
        }}
        .event-card-video-overlay {{
            position: absolute;
            inset: 0;
            background: linear-gradient(180deg, rgba(9, 14, 26, 0.2) 0%, rgba(9, 14, 26, 0.72) 100%);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            transition: background 0.25s ease;
            z-index: 1;
        }}
        .event-card-video-banner:hover .event-card-video-overlay {{
            background: linear-gradient(180deg, rgba(9, 14, 26, 0.08) 0%, rgba(9, 14, 26, 0.55) 100%);
        }}
        .event-video-play-btn {{
            width: 52px;
            height: 52px;
            border-radius: 50%;
            background: rgba(220, 38, 38, 0.95);
            color: #ffffff;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 26px;
            box-shadow: 0 0 24px rgba(220, 38, 38, 0.65);
            transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.2s ease;
        }}
        .event-card-video-banner:hover .event-video-play-btn {{
            transform: scale(1.15);
            background: #ef4444;
        }}
        .event-video-play-label {{
            margin-top: 8px;
            color: #ffffff;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 0.5px;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.8);
        }}
        .event-card-video-top-meta {{
            position: absolute;
            top: 12px;
            left: 12px;
            right: 12px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            pointer-events: none;
            z-index: 2;
        }}
        .event-card-video-bottom-meta {{
            position: absolute;
            bottom: 10px;
            left: 12px;
            right: 12px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            color: rgba(255, 255, 255, 0.92);
            font-size: 11.5px;
            font-weight: 600;
            pointer-events: none;
            z-index: 2;
            text-shadow: 0 1px 3px rgba(0, 0, 0, 0.85);
        }}
        .event-meta-badge {{
            background: rgba(15, 23, 42, 0.72);
            backdrop-filter: blur(4px);
            padding: 3px 9px;
            border-radius: 6px;
            border: 1px solid rgba(255, 255, 255, 0.18);
        }}

        /* Branded Header for Non-Video Events */
        .event-card-branded-header {{
            padding: 18px 22px;
            background: #f8fafc;
            border-bottom: 1px solid #e2e8f0;
            display: flex;
            align-items: center;
            gap: 16px;
        }}
        .event-card-org-logo-box {{
            width: 56px;
            height: 56px;
            min-width: 56px;
            border-radius: 14px;
            background: #ffffff;
            border: 1px solid #e2e8f0;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 2px 8px rgba(15, 23, 42, 0.06);
            flex-shrink: 0;
            padding: 8px;
            transition: transform 0.2s ease, border-color 0.2s ease;
        }}
        .event-hub-card:hover .event-card-org-logo-box {{
            transform: scale(1.06);
            border-color: #cbd5e1;
        }}
        .event-card-org-logo-img {{
            width: 38px;
            height: 38px;
            max-width: 100%;
            max-height: 100%;
            object-fit: contain;
            display: block;
        }}
        .event-card-header-meta {{
            flex-grow: 1;
            min-width: 0;
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
        body.dark-mode .events-hero-card,
        html.dark-mode .events-hero-card {{
            background: linear-gradient(135deg, #090e17 0%, #0f172a 45%, #1e1b4b 100%) !important;
            border-color: rgba(99, 102, 241, 0.35) !important;
            color: #ffffff !important;
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.5) !important;
        }}
        body.dark-mode .events-hero-title,
        html.dark-mode .events-hero-title {{
            color: #ffffff !important;
        }}
        body.dark-mode .hero-subtitle,
        html.dark-mode .hero-subtitle {{
            color: #cbd5e1 !important;
        }}
        body.dark-mode .hero-lead-badge,
        html.dark-mode .hero-lead-badge {{
            background: rgba(99, 102, 241, 0.35) !important;
            border-color: rgba(165, 180, 252, 0.4) !important;
            color: #ffffff !important;
        }}
        body.dark-mode .stat-metric-pill,
        html.dark-mode .stat-metric-pill {{
            background: rgba(255, 255, 255, 0.08) !important;
            border-color: rgba(255, 255, 255, 0.15) !important;
            box-shadow: none !important;
        }}
        body.dark-mode .stat-metric-val,
        html.dark-mode .stat-metric-val {{
            color: #60a5fa !important;
        }}
        body.dark-mode .stat-metric-label,
        html.dark-mode .stat-metric-label {{
            color: #cbd5e1 !important;
        }}

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
        body.dark-mode .event-hub-card:hover {{
            border-color: #818cf8;
            box-shadow: 0 16px 36px rgba(99, 102, 241, 0.2);
        }}
        body.dark-mode .event-card-branded-header {{
            background: #0b1120;
            border-bottom-color: #1e293b;
        }}
        body.dark-mode .event-card-org-logo-box {{
            background: #1e293b;
            border-color: #334155;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
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
                    <li class="nav-item active">
                        <a class="nav-link" href="page-events">Speaker</a>
                    </li>
                    <li class="nav-item">
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
                            <a class="dropdown-item nav-dropdown-item" href="page-about#verified-profiles">
                                <div class="dropdown-item-icon bg-soft-warning"><i class="mdi mdi-shield-account-outline"></i></div>
                                <div class="dropdown-item-content">
                                    <span class="dropdown-item-title">47 Verified Profiles Hub</span>
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
                        <a href="https://scholar.google.com/citations?hl=en&user=zSt9oRMAAAAJ" target="_blank" class="nav-social-btn" title="Google Scholar (26+ Papers)">
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
    <!-- Navbar End -->

    <div class="events-page-wrapper pt-5 pb-5">
        <div class="container" style="margin-top: 80px;">
            
            <!-- Hero Card -->
            <div class="events-hero-card">
                <div class="row align-items-center">
                    <div class="col-lg-7 col-xl-8">
                        <span class="badge badge-pill font-weight-bold px-3 py-1 mb-3 hero-lead-badge">
                            <i class="mdi mdi-microphone-variant mr-1"></i> Speaking Engagements &amp; Ecosystem Leadership
                        </span>
                        <h1 class="font-weight-bold mb-2 events-hero-title" style="font-size: 32px; letter-spacing: -0.5px;">
                            Speaking Engagements &amp; Keynotes
                        </h1>
                        <p class="hero-subtitle mb-4" style="font-size: 15.5px; line-height: 1.7; max-width: 680px;">
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
                                <div class="stat-metric-val">{total_keynotes}</div>
                                <div class="stat-metric-label">Featured Keynotes</div>
                            </div>
                            <div class="stat-metric-pill">
                                <div class="stat-metric-val">{total_events}+</div>
                                <div class="stat-metric-label">Total Engagements</div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-5 col-xl-4 mt-4 mt-lg-0">
                        <div class="hv-speaker-profile-frame-wrap">
                            <div class="hv-speaker-profile-frame">
                                <img src="images/harsh/Harsh_portfolio_pic.png" alt="Harsh Verma - Keynote Speaker & Principal AI Engineer" class="hv-speaker-profile-img">
                                <div class="hv-speaker-card-content">
                                    <div class="hv-speaker-title-row">
                                        <h3 class="hv-speaker-card-name text-white font-weight-bold" style="color: #ffffff !important; font-size: 24px; font-weight: 700; letter-spacing: -0.2px; text-shadow: 0 2px 8px rgba(0,0,0,0.6); margin: 0;">Harsh Verma</h3>
                                        <span class="hv-speaker-highlighter-badge" title="Featured Keynote Speaker">
                                            <span class="speaker-pulse-dot"></span>
                                            Speaker
                                        </span>
                                    </div>
                                    <p class="hv-speaker-card-sub">Principal Software Engineer in AI @ Palo Alto Networks &bull; Forbes Tech Council</p>
                                    <button type="button" class="btn btn-primary font-weight-bold hv-speaker-inline-invite-btn" onclick="if(window.openBookingModal){{window.openBookingModal('Keynote Speech & Strategic Advisory', 'Keynote Speech');}}else if(window.openKeynoteBooking){{window.openKeynoteBooking();}}return false;" data-booking-trigger="true" data-type="Keynote Speech" data-topic="Keynote Speech & Strategic Advisory" title="Invite for Keynote / Panel">
                                        Invite for Keynote / Panel
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Keynote Video Showcase Stage -->
            {render_keynote_hub()}

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
    <script src="js/hv-booking-flow.js"></script>

    <script>
        var yearEl = document.getElementById('currentYear');
        if (yearEl) yearEl.innerText = new Date().getFullYear();

        // Keynote Video Stage Data (Dynamically synchronized from keynote_videos_data)
        var keynoteVideosList = {keynote_json};

        var activeKeynoteIndex = 0;

        function switchKeynoteVideo(idx) {{
            if (idx < 0 || idx >= keynoteVideosList.length) return;
            activeKeynoteIndex = idx;
            var v = keynoteVideosList[idx];

            var playerWrap = document.getElementById('keynoteStagePlayerWrap');
            if (playerWrap) {{
                if (v.stream_url || v.type === 'video') {{
                    playerWrap.innerHTML = '<video id="keynoteStagePlayer" controls autoplay playsinline style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: contain; background: #000;" poster="' + (v.thumb || '') + '" src="' + v.stream_url + '"></video>';
                    var vidEl = document.getElementById('keynoteStagePlayer');
                    if (vidEl) {{
                        vidEl.play().catch(function(e) {{ console.log('Autoplay deferred:', e); }});
                    }}
                }} else {{
                    playerWrap.innerHTML = '<iframe id="keynoteStagePlayer" src="https://www.youtube.com/embed/' + v.id + '?autoplay=1&rel=0&enablejsapi=1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"></iframe>';
                }}
            }}

            var titleEl = document.getElementById('stageVideoTitle');
            if (titleEl) titleEl.innerText = v.title;

            var outletEl = document.getElementById('stageVideoOutlet');
            if (outletEl) outletEl.innerHTML = '<i class="mdi mdi-microphone-variant mr-1"></i> ' + v.outlet;

            var descEl = document.getElementById('stageVideoDesc');
            if (descEl) descEl.innerText = v.desc;

            var durationEl = document.getElementById('stageDurationTag');
            if (durationEl) durationEl.innerText = v.duration;

            var slidesBtn = document.getElementById('stageSlidesBtn');
            if (slidesBtn) slidesBtn.href = v.slides_url;

            var recordingBtn = document.getElementById('stageWatchRecordingBtn');
            if (recordingBtn) {{
                var recUrl = v.recording_url || ('https://www.youtube.com/watch?v=' + v.id);
                recordingBtn.href = recUrl;
                if (v.stream_url || v.type === 'video') {{
                    recordingBtn.innerHTML = '<i class="mdi mdi-video mr-1"></i> Watch on xRaised <i class="mdi mdi-open-in-new ml-1" style="font-size: 11px;"></i>';
                }} else {{
                    recordingBtn.innerHTML = '<i class="mdi mdi-youtube mr-1"></i> Watch on YouTube <i class="mdi mdi-open-in-new ml-1" style="font-size: 11px;"></i>';
                }}
            }}

            var tagsEl = document.getElementById('stageVideoTags');
            if (tagsEl) {{
                var html = '';
                (v.tags || []).forEach(function(t) {{
                    html += '<span class="hv-video-tag">' + t + '</span> ';
                }});
                tagsEl.innerHTML = html;
            }}

            // Highlight card & pin state
            $('.hv-video-card').removeClass('is-pinned');
            $('.hv-video-pin-btn').removeClass('pinned').find('.pin-label-text').text('Pin Keynote');
            $('.pinned-badge-indicator').addClass('d-none');

            $('#keynoteCard-' + idx).addClass('is-pinned');
            $('#pinBtn-' + idx).addClass('pinned').find('.pin-label-text').text('Pinned');
            $('#pinnedBadge-' + idx).removeClass('d-none');

            // Sync quick select dropdown
            $('.hv-quick-select').val(idx);

            // Scroll carousel item into view
            var carouselItem = document.getElementById('carouselItem-' + idx);
            var carouselTrack = document.getElementById('keynoteCarouselTrack');
            if (carouselItem && carouselTrack) {{
                carouselTrack.scrollTo({{
                    left: carouselItem.offsetLeft - carouselTrack.offsetLeft,
                    behavior: 'smooth'
                }});
                updateCarouselDots();
            }}

            // Smooth scroll stage into view so user sees it playing!
            var stageHub = document.getElementById('keynote-video-hub');
            if (stageHub) {{
                stageHub.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
            }}
        }}

        function retriggerStagePlay() {{
            switchKeynoteVideo(activeKeynoteIndex);
        }}

        function playUrlOnStage(url) {{
            if (!url) return;
            for (var i = 0; i < keynoteVideosList.length; i++) {{
                var kv = keynoteVideosList[i];
                if ((kv.id && url.indexOf(kv.id) !== -1) || 
                    (kv.recording_url && url.indexOf(kv.recording_url) !== -1) || 
                    (kv.stream_url && url.indexOf(kv.stream_url) !== -1) || 
                    (url.indexOf('ai-engineering-beyond-code') !== -1 && kv.id === 'xraised-ai-beyond-code')) {{
                    switchKeynoteVideo(i);
                    return;
                }}
            }}

            var yid = null;
            if (url.indexOf('youtube.com/watch?v=') !== -1) {{
                yid = url.split('v=')[1].split('&')[0].split('?')[0];
            }} else if (url.indexOf('youtu.be/') !== -1) {{
                yid = url.split('youtu.be/')[1].split('?')[0].split('&')[0];
            }}

            if (yid) {{
                var playerWrap = document.getElementById('keynoteStagePlayerWrap');
                if (playerWrap) {{
                    playerWrap.innerHTML = '<iframe id="keynoteStagePlayer" src="https://www.youtube.com/embed/' + yid + '?autoplay=1&rel=0&enablejsapi=1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"></iframe>';
                }}
                var stageHub = document.getElementById('keynote-video-hub');
                if (stageHub) {{
                    stageHub.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
                }}
            }}
        }}

        function togglePinKeynote(idx, evt) {{
            if (evt) {{
                evt.stopPropagation();
            }}
            switchKeynoteVideo(idx);
        }}

        function togglePinCurrentStage() {{
            togglePinKeynote(activeKeynoteIndex);
        }}

        // Responsive Video Play-On-Hover Mechanics
        var hoverPreviewTimer = null;
        function handleKeynoteHoverStart(idx, el) {{
            clearTimeout(hoverPreviewTimer);
            hoverPreviewTimer = setTimeout(function() {{
                var previewBox = document.getElementById('hoverPreview-' + idx);
                if (previewBox && !previewBox.classList.contains('is-previewing')) {{
                    var v = keynoteVideosList[idx];
                    if (v.stream_url || v.type === 'video') {{
                        previewBox.innerHTML = '<video src="' + v.stream_url + '" autoplay muted loop playsinline style="width: 100%; height: 100%; object-fit: cover;"></video>';
                    }} else {{
                        previewBox.innerHTML = '<iframe src="https://www.youtube.com/embed/' + v.id + '?autoplay=1&mute=1&controls=0&modestbranding=1&loop=1&playlist=' + v.id + '" allow="autoplay" loading="lazy"></iframe>';
                    }}
                    previewBox.classList.add('is-previewing');
                }}
            }}, 320);
        }}

        function handleKeynoteHoverEnd(idx, el) {{
            clearTimeout(hoverPreviewTimer);
            var previewBox = document.getElementById('hoverPreview-' + idx);
            if (previewBox) {{
                previewBox.innerHTML = '';
                previewBox.classList.remove('is-previewing');
            }}
        }}

        // Keynote Carousel Controls
        function scrollKeynoteCarousel(dir) {{
            var track = document.getElementById('keynoteCarouselTrack');
            if (!track) return;
            var item = track.querySelector('.hv-carousel-item');
            var cardWidth = item ? item.offsetWidth + 18 : 340;
            track.scrollBy({{ left: dir * cardWidth, behavior: 'smooth' }});
            setTimeout(updateCarouselDots, 300);
        }}

        function scrollKeynoteToDot(idx) {{
            var track = document.getElementById('keynoteCarouselTrack');
            var item = document.getElementById('carouselItem-' + idx);
            if (track && item) {{
                track.scrollTo({{ left: item.offsetLeft - track.offsetLeft, behavior: 'smooth' }});
                updateCarouselDots();
            }}
        }}

        function updateCarouselDots() {{
            var track = document.getElementById('keynoteCarouselTrack');
            if (!track) return;
            var scrollLeft = track.scrollLeft;
            var item = track.querySelector('.hv-carousel-item');
            var cardWidth = item ? item.offsetWidth + 18 : 340;
            var activeIdx = Math.round(scrollLeft / cardWidth);
            if (activeIdx < 0) activeIdx = 0;
            if (activeIdx >= keynoteVideosList.length) activeIdx = keynoteVideosList.length - 1;
            $('.hv-carousel-dot').removeClass('active');
            $('.hv-carousel-dot').eq(activeIdx).addClass('active');
        }}

        var carouselTrackEl = document.getElementById('keynoteCarouselTrack');
        if (carouselTrackEl) {{
            carouselTrackEl.addEventListener('scroll', function() {{
                updateCarouselDots();
            }}, {{ passive: true }});
        }}

        function filterKeynoteVideos(category, btn) {{
            $('.hv-stage-filter-pill').removeClass('active');
            if (btn) $(btn).addClass('active');

            if (category === 'all') {{
                $('.keynote-video-item').fadeIn(200);
            }} else {{
                $('.keynote-video-item').each(function() {{
                    var cat = $(this).attr('data-category');
                    if (cat === category) {{
                        $(this).fadeIn(200);
                    }} else {{
                        $(this).fadeOut(150);
                    }}
                }});
            }}
            setTimeout(updateCarouselDots, 250);
        }}

        // Theater Modal Functions
        function openKeynoteTheaterMode() {{
            var v = keynoteVideosList[activeKeynoteIndex];
            window.openKeynoteVideoModal(v.id, v.title, v.outlet, v.desc, v.stream_url);
        }}

        window.openKeynoteVideoModal = function(id, title, outlet, desc, streamUrl) {{
            var modal = document.getElementById('keynoteTheaterModal');
            var wrap = modal ? modal.querySelector('.hv-video-modal-player-wrap') : null;
            var titleEl = document.getElementById('theaterModalTitle');
            var outletEl = document.getElementById('theaterModalOutlet');
            var recLink = document.getElementById('theaterModalRecordingLink');
            if (modal && wrap) {{
                if (streamUrl) {{
                    wrap.innerHTML = '<video controls autoplay playsinline style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: contain; background: #000;" src="' + streamUrl + '"></video>';
                    if (recLink) {{
                        recLink.href = 'https://xraised.com/videos/ai-engineering-beyond-code/';
                        recLink.innerHTML = '<i class="mdi mdi-video mr-1"></i> Open on xRaised';
                    }}
                }} else {{
                    wrap.innerHTML = '<iframe id="theaterModalIframe" src="https://www.youtube.com/embed/' + id + '?autoplay=1&rel=0&enablejsapi=1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"></iframe>';
                    if (recLink) {{
                        recLink.href = 'https://www.youtube.com/watch?v=' + id;
                        recLink.innerHTML = '<i class="mdi mdi-youtube mr-1"></i> Open in YouTube';
                    }}
                }}
                if (titleEl) titleEl.innerText = title;
                if (outletEl) outletEl.innerText = outlet;
                modal.classList.add('active');
                document.body.style.overflow = 'hidden';
            }}
        }};

        window.closeKeynoteVideoModal = function(e) {{
            var modal = document.getElementById('keynoteTheaterModal');
            if (modal) {{
                var wrap = modal.querySelector('.hv-video-modal-player-wrap');
                if (wrap) wrap.innerHTML = '';
                modal.classList.remove('active');
                document.body.style.overflow = '';
            }}
        }};

        $(document).keyup(function(e) {{
            if (e.key === "Escape") {{
                window.closeKeynoteVideoModal();
            }}
        }});

        // Intercept any video link on page to play on stage
        $(document).on('click', 'a[href*="youtube.com"], a[href*="youtu.be"], a[href*="xraised.com/videos"]', function(e) {{
            if (e.ctrlKey || e.metaKey || $(this).hasClass('allow-external-nav')) {{
                return;
            }}
            e.preventDefault();
            playUrlOnStage($(this).attr('href'));
        }});

        var speakerBios = {{
            short: "Harsh Verma is a Principal Software Engineer in AI at Palo Alto Networks, Forbes Technology Council Member, IEEE Senior Member, and author of two books on Enterprise AI. Recognized on the Forttuna Global 100 Power List and Nobel Technology Awards Gold (#145), he architects deterministic agentic systems, zero-trust cloud perimeters, and high-throughput data platforms, keynoting across UC Berkeley SkyDeck and international AI symposiums.",
            medium: "Harsh Verma is an internationally recognized Enterprise AI Architect, Principal Software Engineer in AI at Palo Alto Networks, and Forbes Technology Council Member. With over a decade of systems leadership, Harsh has authored 2 seminal industry books on Enterprise AI Agents and Autonomous Cyber Defense, published 25+ peer-reviewed papers on IEEE and international journals with 150+ academic citations, and earned 25 global technology honors including the Forttuna Global 100 Power List, Nobel Technology Awards Gold (#145), and Global Recognition Award for AI Innovation. He serves as an elected Fellow of Harvard Square Leaders Excellence and IEEE Senior Member. Harsh is a distinguished keynote speaker—frequently headlining UC Berkeley SkyDeck, international AI summits, and venture accelerators on agentic security architectures, distributed AI infrastructure, and autonomous enterprise defense.",
            full: "Harsh Verma is a distinguished Enterprise AI Architect, Principal Software Engineer in AI at Palo Alto Networks, Forbes Technology Council Member, and prolific author. A pioneer in agentic security architectures and deterministic AI guardrails, Harsh has architected mission-critical data platforms, distributed feature pipelines, and autonomous defense perimeters protecting global enterprise networks.\\n\\nHe is the recipient of 25 international honors including the Forttuna Global 100 Power List (2026), Nobel Technology Awards Gold (#145), Global Recognition Award for Enterprise AI Innovation, and multiple Globee & Stevie Awards. A dedicated researcher and thought leader, Harsh has published 25+ peer-reviewed papers across IEEE and international engineering journals, accumulating over 150+ academic citations, alongside authoring two seminal books on Enterprise AI Agents and Autonomous Cyber Defense. He holds senior fellowships including Harvard Square Leaders Excellence Fellow and IEEE Senior Member.\\n\\nAs an invited keynote speaker and technical advisor, Harsh headlines major technology symposiums, university venture accelerators including UC Berkeley SkyDeck, and global executive forums, delivering actionable frameworks on generative AI, zero-trust cloud security, and resilient autonomous systems."
        }};

        var currentBioType = 'short';

        function switchSpeakerBioTab(type, el) {{
            currentBioType = type;
            $('.hv-bio-tab-btn').removeClass('active');
            if (el) $(el).addClass('active');
            var contentArea = document.getElementById('speakerBioContentArea');
            if (contentArea) {{
                contentArea.innerText = speakerBios[type] || speakerBios.short;
            }}
        }}

        function copyCurrentBioText() {{
            var text = speakerBios[currentBioType] || speakerBios.short;
            if (navigator.clipboard) {{
                navigator.clipboard.writeText(text).then(function() {{
                    alert("Copied " + currentBioType.toUpperCase() + " Speaker Bio to clipboard!");
                }}).catch(function() {{
                    prompt("Copy Speaker Bio:", text);
                }});
            }} else {{
                prompt("Copy Speaker Bio:", text);
            }}
        }}

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
    for filename in ["page-events.html", "page-speaker.html", "speaker.html"]:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)
    print("Generated page-events.html, page-speaker.html, and speaker.html successfully with all events.")
