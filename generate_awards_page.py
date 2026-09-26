import json
import html

awards_data = [
    {
        "id": "award-forttuna-powerlist-2026",
        "title": "Forttuna Global 100: THE POWER LIST 2026!",
        "organization": "Forttuna Global Foundation & Leadership Councils",
        "category": "leadership",
        "category_label": "Global Leadership & Power Lists",
        "tier": "Global 100 Honoree",
        "tier_class": "tier-gold",
        "year": "2026",
        "image": "images/awards/forttuna_powerlist.svg",
        "description": "Selected into the prestigious Forttuna Global 100: The Power List 2026, recognizing outstanding leaders from across the globe who are shaping the future of business, healthcare, technology, and AI impact. Inclusion in this exclusive list is a testament to inspiring leadership, remarkable achievements, and global influence.",
        "tags": ["Global 100", "The Power List", "Healthcare & AI", "Executive Leadership"],
        "links": [
            {"label": "Power List 2026 Profile", "url": "https://global100.forttuna.com/the-power-list-2026-honorees/profile?name=harsh-verma", "icon": "mdi-account-star"},
            {"label": "Forttuna Global 100", "url": "https://global100.forttuna.com/", "icon": "mdi-earth"},
            {"label": "Council Member Profile", "url": "https://councils.forttuna.com/council-member/harsh-verma/", "icon": "mdi-account-tie"}
        ],
        "citation": "Verma, H. (2026). Forttuna Global 100: The Power List 2026 Honoree. Forttuna Global Foundation & Leadership Councils."
    },
    {
        "id": "award-nobel-tech-awards-2026",
        "title": "Nobel Technology Awards 2026: Gold Winner (#145)",
        "organization": "Nobel Technology Awards · Globee Awards Winner's Circle",
        "category": "ai-cyber",
        "category_label": "AI & Cybersecurity Innovation",
        "tier": "Gold Winner",
        "tier_class": "tier-gold",
        "year": "2026",
        "image": "images/awards/nobel_tech_awards.svg",
        "description": "Awarded Gold Winner distinction (#145) at the Nobel Technology Awards 2026 for pioneering next-generation secure AI innovation, autonomous threat mitigation, and enterprise AI architectures. Honored in the Globee Awards Winner's Circle and highlighted in a comprehensive Muse World profile.",
        "tags": ["Gold Winner", "Nobel Tech Awards", "Secure AI Innovation", "Globee Circle"],
        "links": [
            {"label": "Nobel Tech Winner Profile", "url": "https://nobletechnologyawards.com/winner-info.php?id=145", "icon": "mdi-trophy-award"},
            {"label": "Official Globee Credential", "url": "https://credential.globeeawards.com/d8cf660f-402b-44b5-a217-3e4bab2d5e42#acc.TokgJAlv", "icon": "mdi-certificate"},
            {"label": "Muse World Feature", "url": "https://www.muse.world/post/harsh-verma-innovates-to-lead-the-next-generation-of-secure-ai-innovation", "icon": "mdi-newspaper-variant-outline"},
            {"label": "LinkedIn Announcement", "url": "https://lnkd.in/p/gxq2jS6C", "icon": "mdi-linkedin"}
        ],
        "citation": "Verma, H. (2026). Gold Winner: Secure AI Next-Generation Innovation. Nobel Technology Awards & Globee Awards (Credential ID: d8cf660f-402b-44b5-a217-3e4bab2d5e42)."
    },
    {
        "id": "award-global-recognition-2026",
        "title": "2026 Global Recognition Award: AI Innovator of the Year",
        "organization": "Global Recognition Awards™ · Palo Alto Networks",
        "category": "ai-cyber",
        "category_label": "AI & Cybersecurity Innovation",
        "tier": "Winner",
        "tier_class": "tier-gold",
        "year": "2026",
        "image": "images/awards/global_recognition_award.svg",
        "description": "Received the 2026 Global Recognition Award for AI Innovator of the Year in recognition of measurable, scalable advances in enterprise AI, autonomous agentic copilot systems, and cybersecurity infrastructure at Palo Alto Networks. Profiled across global financial media including Business Insider and Markets Insider.",
        "tags": ["AI Innovator of the Year", "Palo Alto Networks", "Enterprise AI", "Business Insider"],
        "links": [
            {"label": "Global Recognition Award Winner", "url": "https://globalrecognitionawards.org/winners/2026/harsh-verma-recognized-with-a-2026-global-recognition-award/", "icon": "mdi-trophy"},
            {"label": "Markets Insider / Business Insider", "url": "https://markets.businessinsider.com/news/stocks/harsh-verma-receives-a-2026-global-recognition-award-for-measurable-advances-in-enterprise-ai-and-cybersecurity-1035986499", "icon": "mdi-chart-timeline-variant"}
        ],
        "citation": "Verma, H. (2026). Global Recognition Award for AI Innovator of the Year: Measurable Advances in Enterprise AI and Cybersecurity. Global Recognition Awards."
    },
    {
        "id": "award-stevie-ai-innovator-2026",
        "title": "American Business Awards® 2026: AI Innovator of the Year",
        "organization": "Stevie Awards · American Business Awards®",
        "category": "ai-cyber",
        "category_label": "AI & Cybersecurity Innovation",
        "tier": "Stevie Winner",
        "tier_class": "tier-gold",
        "year": "2026",
        "image": "images/awards/stevie_gold.svg",
        "description": "Winner in the premier American Business Awards® (The Stevie® Awards) in the competitive AI Innovator of the Year category for groundbreaking system contributions in generative AI workflows, autonomous agent orchestration, and enterprise machine learning deployments.",
        "tags": ["Stevie Awards", "AI Innovator of the Year", "American Business Awards", "Enterprise GenAI"],
        "links": [
            {"label": "Stevie Awards AI Winners Directory", "url": "https://aba.stevieawards.com/awards/aba-winners/AI-Category-Winners", "icon": "mdi-star-circle"}
        ],
        "citation": "Verma, H. (2026). AI Innovator of the Year. The 24th Annual American Business Awards (Stevie Awards), AI Category Winners."
    },
    {
        "id": "award-cybersecurity-excellence-silver-2026",
        "title": "2026 Cybersecurity Excellence Awards: Silver (AI Security Innovator)",
        "organization": "Cybersecurity Excellence Awards · Palo Alto Networks",
        "category": "ai-cyber",
        "category_label": "AI & Cybersecurity Innovation",
        "tier": "Silver Medal",
        "tier_class": "tier-silver",
        "year": "2026",
        "image": "images/awards/cybersecurity_silver.svg",
        "description": "Earned Silver Award recognition in the 'AI Security Innovator of the Year' category of the 2026 Cybersecurity Excellence Awards, recognizing revolutionary work in autonomous security architectures, threat intelligence reasoning, and copilot protection layers.",
        "tags": ["Silver Award", "Cybersecurity Excellence", "AI Security Innovator", "Threat Intelligence"],
        "links": [
            {"label": "Cybersecurity Excellence Profile", "url": "https://cybersecurity-excellence-awards.com/candidates/ai-innovator-of-the-year-2026/?_se=aHZlcm1hQHBhbG9hbHRvbmV0d29ya3MuY29t", "icon": "mdi-shield-check"}
        ],
        "citation": "Verma, H. (2026). Silver Award: AI Security Innovator of the Year. Cybersecurity Excellence Awards 2026."
    },
    {
        "id": "award-cybersecurity-community-choice-2026",
        "title": "Cybersecurity Excellence Awards: Community Choice Award 2026",
        "organization": "World's Top Cybersecurity Achievements · Cybersecurity Excellence Awards",
        "category": "ai-cyber",
        "category_label": "AI & Cybersecurity Innovation",
        "tier": "Community Choice",
        "tier_class": "tier-purple",
        "year": "2026",
        "image": "images/awards/cybersecurity_community.svg",
        "description": "Won the prestigious Community Choice Award in AI and Cybersecurity Innovation as part of the World's Top Cybersecurity Achievements, marking a dual triumph in the 2026 Cybersecurity Excellence Awards. Syndicated globally on Yahoo Finance and Newsfile Corp.",
        "tags": ["Community Choice", "Dual Recognition", "Yahoo Finance", "World's Top Achievements"],
        "links": [
            {"label": "Yahoo Finance Press Release", "url": "https://finance.yahoo.com/technology/ai/articles/cybersecurity-excellence-awards-2026-announces-022700731.html", "icon": "mdi-finance"},
            {"label": "Newsfile Corp Global Release", "url": "https://www.newsfilecorp.com/release/309183/Cybersecurity-Excellence-Awards-2026-Announces-Dual-Recognition-for-Principal-AI-Engineer-Harsh-Verma", "icon": "mdi-newspaper"},
            {"label": "Official Award Entry", "url": "https://cybersecurity-excellence-awards.com/candidates/ai-innovator-of-the-year-2026/?_se=aHZlcm1hQHBhbG9hbHRvbmV0d29ya3MuY29t", "icon": "mdi-shield-star"}
        ],
        "citation": "Verma, H. (2026). Community Choice Award: AI & Cybersecurity Innovation. World's Top Cybersecurity Achievements, Cybersecurity Excellence Awards (Syndicated via Yahoo Finance & Newsfile Corp)."
    },
    {
        "id": "award-globee-ai-2026",
        "title": "2nd Annual 2026 Globee Awards for AI: Silver Winner",
        "organization": "Globee Awards for Artificial Intelligence",
        "category": "ai-cyber",
        "category_label": "AI & Cybersecurity Innovation",
        "tier": "Silver Globee",
        "tier_class": "tier-silver",
        "year": "2026",
        "image": "images/awards/globee_silver.svg",
        "description": "Conferred the Silver Globee® Award in the Artificial Intelligence category for 'AI Expertise and Innovation Excellence in Intelligent Software Systems' at the 2nd Annual 2026 Globee Awards for Artificial Intelligence, highlighting world-class engineering mastery.",
        "tags": ["Silver Globee", "Globee AI Awards", "Intelligent Systems", "AI Architecture"],
        "links": [
            {"label": "Globee AI 2026 Winners List", "url": "https://globeeawards.com/2026-winners-artificial-intelligence-awards/", "icon": "mdi-trophy-outline"},
            {"label": "Globee AI Portal", "url": "https://globeeawards.com/artificial-intelligence/winners/", "icon": "mdi-web"}
        ],
        "citation": "Verma, H. (2026). Silver Globee Award: Artificial Intelligence Expertise and Innovation Excellence in Intelligent Software Systems. 2nd Annual Globee Awards for AI."
    },
    {
        "id": "award-stevie-cybersecurity-bronze-2026",
        "title": "American Business Awards®: AI Cybersecurity Expert of the Year",
        "organization": "Stevie Awards · Palo Alto Networks",
        "category": "ai-cyber",
        "category_label": "AI & Cybersecurity Innovation",
        "tier": "Bronze Stevie",
        "tier_class": "tier-bronze",
        "year": "2026",
        "image": "images/awards/stevie_bronze.svg",
        "description": "Awarded Bronze Medal distinction in the American Business Awards® for AI Cybersecurity Expert of the Year, honoring specialized contributions in creating zero-trust AI agents and robust behavioral threat detectors at Palo Alto Networks.",
        "tags": ["Bronze Stevie", "AI Cybersecurity Expert", "Palo Alto Networks", "Stevie Awards"],
        "links": [
            {"label": "American Business Awards", "url": "https://aba.stevieawards.com/", "icon": "mdi-star-box-outline"}
        ],
        "citation": "Verma, H. (2026). Bronze Medal: AI Cybersecurity Expert of the Year. The American Business Awards (Stevie Awards)."
    },
    {
        "id": "award-influencer-tech-excellence-2026",
        "title": "Influencer Magazine Awards 2026: Tech Excellence Award",
        "organization": "Influencer Magazine UK · AI Journal",
        "category": "media-speaking",
        "category_label": "Media, Keynotes & Journals",
        "tier": "Tech Excellence Winner",
        "tier_class": "tier-gold",
        "year": "2026",
        "image": "images/awards/influencer_tech_excellence.svg",
        "description": "Won the 'Tech Excellence Award' at the Influencer Magazine Awards 2026 celebrating a 'Double Triumph in AI and Cybersecurity Innovation' and pioneering breakthroughs in Human-AI Collaboration. Extensively featured across international tech publications including AI Journ, EIN Presswire, and Knox News.",
        "tags": ["Tech Excellence", "Influencer UK", "Human-AI Collaboration", "AI Journ"],
        "links": [
            {"label": "Influencer Magazine UK Feature", "url": "https://influencermagazine.uk/2026/07/harsh-verma-a-double-triumph-in-ai-and-cybersecurity-innovation/", "icon": "mdi-magazine"},
            {"label": "AI Journal Article", "url": "https://aijourn.com/principal-ai-engineer-harsh-verma-nominated-for-tech-excellence-award-at-influencer-magazine-awards-2026-as-his-work-on-human-ai-collaboration-gains-enterprise-attention/", "icon": "mdi-robot"},
            {"label": "EIN News Press Release", "url": "https://tech.einnews.com/pr_news/920520116/harsh-verma-wins-tech-excellence-award-at-influencer-magazine-awards-2026", "icon": "mdi-bullhorn"},
            {"label": "Instagram Reel Feature", "url": "https://www.instagram.com/reels/DaPUPeoMjAg/", "icon": "mdi-instagram"}
        ],
        "citation": "Verma, H. (2026). Tech Excellence Award: A Double Triumph in AI and Cybersecurity Innovation. Influencer Magazine UK Awards 2026."
    },
    {
        "id": "award-ais-data-scientist-2026",
        "title": "International AI Data Scientist Awards: AI Innovator Award",
        "organization": "Association of International AI Data Scientists (AIS)",
        "category": "academic-fellowships",
        "category_label": "Fellowships & Academic Excellence",
        "tier": "AIS Winner",
        "tier_class": "tier-blue",
        "year": "2026",
        "image": "images/awards/ais_innovator.svg",
        "description": "Conferred the AI Innovator Award at the AIS 2026 Awards in recognition of exceptional research contributions, foundational algorithm architecture, and applied innovations in deep learning, neural modeling, and multi-agent coordination.",
        "tags": ["AI Data Scientists", "AIS 2026", "Deep Learning", "Data Science"],
        "links": [
            {"label": "AIS Award Winners Directory", "url": "https://aidatascientists.com/award-winners/", "icon": "mdi-account-group"},
            {"label": "AIS YouTube Feature", "url": "https://www.youtube.com/shorts/SsvMfJPPHDk", "icon": "mdi-youtube"}
        ],
        "citation": "Verma, H. (2026). AI Innovator Award. International AI Data Scientist Awards (AIS 2026 Awards)."
    },
    {
        "id": "award-stanford-distinguished-scholar",
        "title": "Stanford Distinguished Scholar",
        "organization": "Stanford Graduate School of Business (Stanford GSB)",
        "category": "academic-fellowships",
        "category_label": "Fellowships & Academic Excellence",
        "tier": "Distinguished Scholar",
        "tier_class": "tier-gold",
        "year": "2025",
        "image": "images/awards/stanford_scholar.svg",
        "description": "Recognized and awarded as a Stanford Distinguished Scholar by the Stanford Graduate School of Business (GSB) for outstanding executive leadership, scholarship, and technological contributions to enterprise innovation.",
        "tags": ["Stanford GSB", "Distinguished Scholar", "Executive Fellow", "Stanford Alumni"],
        "links": [
            {"label": "Stanford GSB Executive Education", "url": "https://www.gsb.stanford.edu/", "icon": "mdi-school"}
        ],
        "citation": "Verma, H. (2025). Stanford Distinguished Scholar. Stanford Graduate School of Business."
    },
    {
        "id": "award-mit-bootcamp",
        "title": "MIT Innovation & Leadership Recognition",
        "organization": "Massachusetts Institute of Technology (MIT)",
        "category": "academic-fellowships",
        "category_label": "Fellowships & Academic Excellence",
        "tier": "Certificate of Recognition",
        "tier_class": "tier-blue",
        "year": "2024",
        "image": "images/awards/mit_bootcamp.svg",
        "description": "Awarded official Certificate of Recognition for successfully completing the rigorous MIT Innovation & Leadership Bootcamp and leading the architecture and deployment of the 'Convex Healthcare Product MVP' for proactive patient diagnostics.",
        "tags": ["MIT Bootcamp", "Healthcare MVP", "Innovation & Leadership", "Product Architecture"],
        "links": [
            {"label": "MIT Bootcamp Overview", "url": "https://bootcamp.mit.edu/", "icon": "mdi-school-outline"}
        ],
        "citation": "Verma, H. (2024). Certificate of Recognition: Innovation & Leadership Bootcamp (Convex Healthcare Product MVP). Massachusetts Institute of Technology."
    },
    {
        "id": "award-forbes-council-recognition",
        "title": "Forbes Technology Council: AI & Software Engineering Recognition",
        "organization": "Forbes Technology Council · Palo Alto Networks",
        "category": "leadership",
        "category_label": "Global Leadership & Power Lists",
        "tier": "Council Recognition",
        "tier_class": "tier-gold",
        "year": "2024",
        "image": "images/awards/forbes_recognition.svg",
        "description": "Recognized by the Forbes Technology Council for senior thought leadership and engineering contributions in artificial intelligence, cloud security architectures, and enterprise engineering in collaboration with Palo Alto Networks.",
        "tags": ["Forbes Tech Council", "AI Leadership", "Palo Alto Networks", "Thought Leadership"],
        "links": [
            {"label": "Forbes Council Profile", "url": "https://www.forbes.com/councils/forbestechcouncil/people/harshverma/", "icon": "mdi-web"}
        ],
        "citation": "Verma, H. (2024). Forbes Technology Council Member Recognition for Contributions in AI and Software Engineering. Forbes Media."
    },
    {
        "id": "award-google-developer-expert",
        "title": "Google Developer Expert (GDE) in Cloud AI",
        "organization": "Google Developers · Global GDE Program",
        "category": "mentorship-advisory",
        "category_label": "Mentorship, Ecosystem & Advisory",
        "tier": "Top 100 Globally",
        "tier_class": "tier-blue",
        "year": "2025",
        "image": "images/awards/gde_cloud_ai.svg",
        "description": "Selected and featured as a Google Developer Expert (GDE) in Cloud AI. Globally there are only ~1,500 total GDEs across all domains, and fewer than 100 recognized worldwide in Cloud AI, honoring elite expertise in scalable AI infrastructure, GCP architectures, and incident intelligence.",
        "tags": ["Google GDE", "Cloud AI", "Top 100 Globally", "Google Developers"],
        "links": [
            {"label": "Google GDE Directory", "url": "https://developers.google.com/community/experts/directory?text=Harsh%20Verma", "icon": "mdi-google"}
        ],
        "citation": "Verma, H. (2025). Google Developer Expert (GDE) in Cloud AI. Google Developers Expert Community."
    },
    {
        "id": "award-skydeck-advisor-elevation",
        "title": "UC Berkeley SkyDeck: Elevated to Global Advisor & Selection Committee",
        "organization": "University of California, Berkeley · SkyDeck Accelerator",
        "category": "mentorship-advisory",
        "category_label": "Mentorship, Ecosystem & Advisory",
        "tier": "Global Advisor",
        "tier_class": "tier-gold",
        "year": "2025",
        "image": "images/awards/skydeck_advisor_elevation.svg",
        "description": "Promoted from Startup Mentor to Global Advisor and appointed to the 2025–2026 Batch Selection Committee at UC Berkeley SkyDeck Accelerator, providing strategic architecture, deep-tech due diligence, and go-to-market mentorship to top startup founders.",
        "tags": ["UC Berkeley", "SkyDeck Accelerator", "Selection Committee", "Startup Advisory"],
        "links": [
            {"label": "SkyDeck Advisors Directory", "url": "https://skydeck.berkeley.edu/advisors/", "icon": "mdi-rocket-launch"}
        ],
        "citation": "Verma, H. (2025). UC Berkeley SkyDeck Global Advisor and Selection Committee Member (2025–2026 Batch). University of California, Berkeley."
    },
    {
        "id": "award-ifgict-fellowship",
        "title": "IFGICT Royal Fellowship Award",
        "organization": "International Federation of Global & Green ICT (IFGICT)",
        "category": "academic-fellowships",
        "category_label": "Fellowships & Academic Excellence",
        "tier": "Honorary Fellow",
        "tier_class": "tier-emerald",
        "year": "2024",
        "image": "images/awards/ifgict_fellowship_award.svg",
        "description": "Conferred the prestigious IFGICT Fellowship Award for pioneering contributions in sustainable information technology, eco-friendly AI compute paradigms, and international green computing standardization. Featured in Time Business News.",
        "tags": ["IFGICT Fellowship", "Green ICT", "Sustainable AI", "Time Business News"],
        "links": [
            {"label": "Time Business News Feature", "url": "https://timebusinessnews.com/harsh-verma-ifgict/", "icon": "mdi-newspaper-variant"}
        ],
        "citation": "Verma, H. (2024). IFGICT Fellowship Award: Pioneering Green and Sustainable ICT Innovation. International Federation of GICT (Published in Time Business News)."
    },
    {
        "id": "award-ioasd-lifetime-achievement",
        "title": "IOASD Annual Awards: Lifetime Achievement Award",
        "organization": "International Organization for Academic and Scientific Development",
        "category": "academic-fellowships",
        "category_label": "Fellowships & Academic Excellence",
        "tier": "Lifetime Achievement",
        "tier_class": "tier-gold",
        "year": "2025",
        "image": "images/awards/ioasd_lifetime.svg",
        "description": "Conferred the IOASD Lifetime Achievement Award—the highest distinction bestowed by the organization—for enduring scientific contributions, seminal research publications, and global impact in computational engineering.",
        "tags": ["Lifetime Achievement", "IOASD", "Scientific Honors", "Computational Science"],
        "links": [
            {"label": "IOASD Scientific Registry", "url": "http://ioasd.org/", "icon": "mdi-certificate-outline"}
        ],
        "citation": "Verma, H. (2025). Lifetime Achievement Award. IOASD Annual Awards, International Organization for Academic and Scientific Development."
    },
    {
        "id": "award-ioasd-research-excellence",
        "title": "IOASD Annual Awards: Award of Excellence in Research",
        "organization": "International Organization for Academic and Scientific Development",
        "category": "academic-fellowships",
        "category_label": "Fellowships & Academic Excellence",
        "tier": "Research Excellence",
        "tier_class": "tier-blue",
        "year": "2024",
        "image": "images/awards/ioasd_research_excellence.svg",
        "description": "Awarded the Award of Excellence in Research by IOASD for publishing groundbreaking peer-reviewed research in deep learning, cognitive machine learning (CogML), and distributed test frameworks across IEEE and leading indexing venues.",
        "tags": ["Research Excellence", "IOASD", "CogML", "IEEE Publications"],
        "links": [
            {"label": "IOASD Research Board", "url": "http://ioasd.org/", "icon": "mdi-flask"}
        ],
        "citation": "Verma, H. (2024). Award of Excellence in Research. IOASD Annual Awards."
    },
    {
        "id": "award-ioasd-outstanding-researcher",
        "title": "IOASD Annual Awards: Outstanding Researcher Award",
        "organization": "International Organization for Academic and Scientific Development",
        "category": "academic-fellowships",
        "category_label": "Fellowships & Academic Excellence",
        "tier": "Outstanding Researcher",
        "tier_class": "tier-teal",
        "year": "2023",
        "image": "images/awards/ioasd_outstanding_researcher.svg",
        "description": "Recognized with the Outstanding Researcher Award for high-citation peer contributions, rigorous research evaluation, and sustained innovations across scalable AI and automated system testing.",
        "tags": ["Outstanding Researcher", "IOASD", "Scientific Impact", "AI Innovations"],
        "links": [
            {"label": "IOASD Academic Portal", "url": "http://ioasd.org/", "icon": "mdi-school"}
        ],
        "citation": "Verma, H. (2023). Outstanding Researcher Award. IOASD Annual Awards."
    },
    {
        "id": "award-google-hackathon-mentor",
        "title": "Lead Hackathon Mentor: Google & Hackmakers Global Hack",
        "organization": "Google & Hackmakers · Global Hack Digital Defense",
        "category": "mentorship-advisory",
        "category_label": "Mentorship, Ecosystem & Advisory",
        "tier": "Lead Mentor",
        "tier_class": "tier-emerald",
        "year": "2020",
        "image": "images/awards/google_hackathon.svg",
        "description": "Served as Lead Hackathon Mentor for Global Hack / Hackmakers Global Hackathon Digital Defense organized in partnership with Google, evaluating AI/security solutions and mentoring hundreds of global participating engineers.",
        "tags": ["Google Hackathon", "Lead Mentor", "Digital Defense", "Badgr Verified"],
        "links": [
            {"label": "Badgr Official Verification", "url": "https://au.badgr.com/public/assertions/wvReoDSRTjCJsBqI9A4LMg?identity__email=harshverma59@gmail.com", "icon": "mdi-shield-check"},
            {"label": "LinkedIn Recognition Post", "url": "https://www.linkedin.com/feed/update/urn:li:activity:6691402830294724608/", "icon": "mdi-linkedin"}
        ],
        "citation": "Verma, H. (2020). Lead Hackathon Mentor Recognition: Global Hack Digital Defense. Google & Hackmakers (Badgr Assertion: wvReoDSRTjCJsBqI9A4LMg)."
    },
    {
        "id": "award-adplist-1000-minutes",
        "title": "ADPList Milestone: 1,000+ Completed Mentorship Minutes",
        "organization": "ADPList (Amazing Design People List)",
        "category": "mentorship-advisory",
        "category_label": "Mentorship, Ecosystem & Advisory",
        "tier": "1,000+ Minutes",
        "tier_class": "tier-coral",
        "year": "2025",
        "image": "images/awards/adplist_1000min.svg",
        "description": "Awarded Certificate of Achievement from ADPList for completing over 1,000 minutes (16+ hours) of 1-on-1 mentorship sessions, guiding emerging engineers, AI researchers, and founders across ADPList's 1M+ global community.",
        "tags": ["ADPList", "1,000 Minutes", "Global Mentorship", "Community Impact"],
        "links": [
            {"label": "ADPList 1,000 Minutes Certificate", "url": "https://adplist.org/community-certifications/minutes-1000-b42201", "icon": "mdi-certificate"},
            {"label": "ADPList 500 Minutes Milestone", "url": "https://adplist.org/community-certifications/minutes-500-b42201", "icon": "mdi-clock-check"}
        ],
        "citation": "Verma, H. (2025). Certificate of Achievement: 1,000 Minutes of Global Mentorship. ADPList Platform."
    },
    {
        "id": "award-adplist-25-sessions",
        "title": "ADPList Milestone: 25+ Completed Mentorship Sessions",
        "organization": "ADPList (Amazing Design People List)",
        "category": "mentorship-advisory",
        "category_label": "Mentorship, Ecosystem & Advisory",
        "tier": "25+ Sessions",
        "tier_class": "tier-purple",
        "year": "2025",
        "image": "images/awards/adplist_25sessions.svg",
        "description": "Milestone Certificate of Achievement recognizing 25+ completed individual mentorship sessions, empowering technical practitioners with architectural insights in scalable machine learning and engineering career advancement.",
        "tags": ["ADPList", "25+ Sessions", "Volunteer Mentorship", "Community Growth"],
        "links": [
            {"label": "ADPList 25 Sessions Certificate", "url": "https://adplist.org/community-certifications/sessions-25-b42201", "icon": "mdi-account-multiple-check"},
            {"label": "ADPList 10 Sessions Milestone", "url": "https://adplist.org/community-certifications/sessions-10-b42201", "icon": "mdi-account-check"}
        ],
        "citation": "Verma, H. (2025). Certificate of Achievement: 25 Completed Mentorship Sessions. ADPList Platform."
    },
    {
        "id": "award-jrtcse-peer-review-excellence",
        "title": "JRTCSE Certificate of Excellence in Research Review",
        "organization": "Journal of Recent Trends in Computer Science and Engineering",
        "category": "media-speaking",
        "category_label": "Media, Keynotes & Journals",
        "tier": "Editorial Excellence",
        "tier_class": "tier-blue",
        "year": "2024",
        "image": "images/awards/jrtcse_excellence.svg",
        "description": "Certificate of Excellence for reviewing expert research papers and sustained editorial contributions to the Journal of Recent Trends in Computer Science and Engineering (JRTCSE).",
        "tags": ["JRTCSE", "Peer Review", "Computer Science", "Editorial Board"],
        "links": [
            {"label": "JRTCSE Reviewer Index", "url": "https://jrtcse.com/index.php/home/Harsh_Verma", "icon": "mdi-book-check"}
        ],
        "citation": "Verma, H. (2024). Certificate of Excellence for Expert Research Paper Review. Journal of Recent Trends in Computer Science and Engineering (JRTCSE)."
    },
    {
        "id": "award-ata-gtr-speaker-honour",
        "title": "Certificate of Honour: Keynote Speaker @#ATAGTR2017",
        "organization": "Agile Testing Alliance (ATA) · Global Testing Retreat",
        "category": "media-speaking",
        "category_label": "Media, Keynotes & Journals",
        "tier": "Certificate of Honour",
        "tier_class": "tier-gold",
        "year": "2017",
        "image": "images/awards/ata_gtr.svg",
        "description": "Awarded Certificate of Honour for speaking on the proprietary high-throughput performance testing framework 'HikeRunner' at @#ATAGTR2017 (Global Testing Retreat 2017), introducing distributed microservice benchmarking concepts.",
        "tags": ["ATA GTR2017", "HikeRunner", "Keynote Speaker", "Agile Testing Alliance"],
        "links": [
            {"label": "ATA Meet Our Speaker Series", "url": "http://agiletestingalliance.org/agileBlogs/atagtr2017-meet-our-speaker-series-harsh-verma/", "icon": "mdi-microphone"}
        ],
        "citation": "Verma, H. (2017). Certificate of Honour for Keynote Presentation on 'HikeRunner' Performance Framework. Agile Testing Alliance #ATAGTR2017."
    }
]

with open("awards_data.json", "w", encoding="utf-8") as f:
    json.dump(awards_data, f, indent=2)

# Count stats
total_awards = len(awards_data)
global_titles = sum(1 for a in awards_data if a["year"] == "2026")
gold_medals = sum(1 for a in awards_data if "gold" in a["tier_class"] or "Gold" in a["tier"] or "Winner" in a["tier"])
academic_honors = sum(1 for a in awards_data if a["category"] in ["academic-fellowships", "leadership"])
mentorship_hours = "1,000+"

def build_card_html(award):
    aid = award["id"]
    title = html.escape(award["title"])
    org = html.escape(award["organization"])
    cat = award["category"]
    cat_label = html.escape(award["category_label"])
    tier = html.escape(award["tier"])
    tier_class = award["tier_class"]
    year = award["year"]
    img = award["image"]
    desc = html.escape(award["description"])
    tags = award["tags"]
    links = award["links"]
    citation = html.escape(award["citation"])

    tags_html = "".join([f'<span class="award-tag" onclick="filterByTag(\'{html.escape(t)}\')">#{html.escape(t)}</span>' for t in tags])
    
    links_html = ""
    for l in links:
        l_label = html.escape(l["label"])
        l_url = html.escape(l["url"])
        l_icon = l.get("icon", "mdi-open-in-new")
        links_html += f'''<a href="{l_url}" target="_blank" rel="noopener noreferrer" class="btn-award-link">
            <i class="mdi {l_icon}"></i> {l_label}
        </a>'''

    searchable_text = f"{title} {org} {cat_label} {tier} {year} {desc} {' '.join(tags)}".lower()

    return f'''
    <div class="col-lg-6 col-md-12 mb-4 award-card-col" data-category="{cat}" data-year="{year}" data-search="{html.escape(searchable_text)}">
        <div class="award-card shadow-sm h-100" id="{aid}">
            <div class="award-header-badge">
                <img src="{img}" alt="{title}" loading="lazy">
                <div class="award-image-overlay"></div>
                <span class="award-tier-pill {tier_class}">{tier}</span>
                <span class="award-year-pill"><i class="mdi mdi-calendar mr-1"></i>{year}</span>
                <span class="award-domain-tag-overlay"><i class="mdi mdi-shield-star-outline mr-1"></i>{cat_label}</span>
            </div>
            <div class="award-card-body d-flex flex-column">
                <div class="award-issuing-org text-muted mb-2">
                    <i class="mdi mdi-domain mr-1 text-primary"></i> <strong>{org}</strong>
                </div>
                <h4 class="award-title mb-3">{title}</h4>
                <p class="award-description text-muted mb-3 flex-grow-1">
                    {desc}
                </p>
                
                <div class="award-tags-container mb-3">
                    {tags_html}
                </div>

                <div class="award-actions-footer pt-3 border-top">
                    <div class="award-links-grid mb-2">
                        {links_html}
                    </div>
                    <button type="button" class="btn-copy-cite" onclick="openCiteModal('{aid}', '{html.escape(title, quote=True)}', '{html.escape(org, quote=True)}', '{year}', '{html.escape(citation, quote=True)}')">
                        <i class="mdi mdi-format-quote-close mr-1"></i> Cite / Verification Dossier
                    </button>
                </div>
            </div>
        </div>
    </div>
    '''

cards_html = "\n".join([build_card_html(a) for a in awards_data])

html_page = f'''<!DOCTYPE html>
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
    <title>Harsh Verma | Awards, Honors &amp; Global Recognitions</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Explore prestigious awards, global honors, and executive recognitions of Harsh Verma across Forttuna Global 100, Nobel Technology Awards, Stevie Awards, Global Recognition Awards, Cybersecurity Excellence, Forbes, MIT, Stanford, and Google." />
    <meta name="keywords" content="Harsh Verma, Awards, Stevie Awards, Forttuna Global 100, Nobel Technology Awards, Global Recognition Award, Cybersecurity Excellence Awards, Globee Awards, Stanford Scholar, MIT, Forbes, GDE, Palo Alto Networks" />
    <meta content="Harsh Verma" name="author" />
    <meta property="og:title" content="Harsh Verma | Awards, Honors &amp; Global Recognitions" />
    <meta property="og:description" content="Explore prestigious awards, global honors, and executive recognitions of Harsh Verma across Forttuna Global 100, Nobel Technology Awards, Stevie Awards, Global Recognition Awards, Cybersecurity Excellence, Forbes, MIT, Stanford, and Google." />
    <meta property="og:image" content="images/awards/forttuna_powerlist.svg" />
    
    <!-- Favicon -->
    <link rel="shortcut icon" href="images/favicon_new.ico">
    <!-- Bootstrap -->
    <link href="css/bootstrap.min.css" rel="stylesheet" type="text/css" />
    <!-- Icons -->
    <link href="css/materialdesignicons.min.css" rel="stylesheet" type="text/css" />
    <!-- Main CSS File -->
    <link href="css/style.css" rel="stylesheet" type="text/css" />
    <!-- Dark Mode CSS File -->
    <link href="css/dark-mode.css" rel="stylesheet" type="text/css" />
    <script src="js/dark-mode.js"></script>

    <style>
        /* Luxury Awards Page Styles */
        .awards-hero-section {{
            background: linear-gradient(135deg, #090e1a 0%, #111827 50%, #1e1b4b 100%);
            position: relative;
            padding: 130px 0 70px;
            color: #ffffff;
            overflow: hidden;
        }}
        .awards-hero-section h1,
        .awards-hero-title {{
            color: #ffffff !important;
        }}
        .awards-hero-section::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: radial-gradient(circle at 80% 20%, rgba(245, 158, 11, 0.12) 0%, transparent 50%),
                        radial-gradient(circle at 20% 80%, rgba(37, 99, 235, 0.15) 0%, transparent 60%);
            pointer-events: none;
        }}
        .awards-hero-section::after {{
            content: "";
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 40px;
            background: linear-gradient(to top, #f8fafc, transparent);
            pointer-events: none;
        }}
        body.dark-mode .awards-hero-section::after {{
            background: linear-gradient(to top, #0f172a, transparent);
        }}

        .award-hero-badge-pill {{
            background: linear-gradient(135deg, rgba(245, 158, 11, 0.2) 0%, rgba(217, 119, 6, 0.3) 100%);
            border: 1px solid rgba(245, 158, 11, 0.5);
            color: #fde68a;
            font-size: 13px;
            font-weight: 700;
            letter-spacing: 1px;
            text-transform: uppercase;
            padding: 6px 18px;
            border-radius: 30px;
            display: inline-block;
        }}

        /* Stats Ribbon */
        .awards-stats-box {{
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 20px;
            padding: 30px 24px;
            box-shadow: 0 15px 35px -5px rgba(15, 23, 42, 0.08);
            margin-top: -45px;
            position: relative;
            z-index: 10;
            transition: all 0.3s ease;
        }}
        body.dark-mode .awards-stats-box {{
            background: #1e293b;
            border-color: #334155;
            box-shadow: 0 15px 35px -5px rgba(0, 0, 0, 0.4);
        }}
        .award-stat-item {{
            text-align: center;
            padding: 10px 8px;
        }}
        .award-stat-number {{
            font-size: 32px;
            font-weight: 800;
            line-height: 1.1;
            margin-bottom: 4px;
            letter-spacing: -0.5px;
            background: linear-gradient(135deg, #2563eb 0%, #d97706 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .award-stat-label {{
            font-size: 12.5px;
            color: #64748b;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        body.dark-mode .award-stat-label {{
            color: #94a3b8;
        }}

        /* Search & Filter Bar */
        .search-container {{
            position: relative;
            max-width: 650px;
            margin: 0 auto 30px;
        }}
        .search-input-field {{
            width: 100%;
            padding: 15px 22px 15px 50px;
            border-radius: 50px;
            border: 1.5px solid #cbd5e1;
            font-size: 15.5px;
            background: #ffffff;
            color: #1e293b;
            box-shadow: 0 4px 18px rgba(15, 23, 42, 0.05);
            transition: all 0.25s ease;
        }}
        .search-input-field:focus {{
            outline: none;
            border-color: #f59e0b;
            box-shadow: 0 0 0 4px rgba(245, 158, 11, 0.15);
        }}
        .search-icon-inside {{
            position: absolute;
            left: 20px;
            top: 50%;
            transform: translateY(-50%);
            color: #94a3b8;
            font-size: 22px;
        }}
        .search-clear-btn {{
            position: absolute;
            right: 18px;
            top: 50%;
            transform: translateY(-50%);
            background: #e2e8f0;
            color: #64748b;
            border: none;
            width: 28px;
            height: 28px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            font-size: 14px;
            transition: all 0.2s ease;
        }}
        .search-clear-btn:hover {{
            background: #cbd5e1;
            color: #1e293b;
        }}

        /* Filter Pills */
        .filter-nav-wrap {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            justify-content: center;
            margin-bottom: 35px;
        }}
        .btn-filter-pill {{
            background: #ffffff;
            border: 1px solid #e2e8f0;
            color: #475569;
            font-weight: 600;
            font-size: 13.5px;
            padding: 8px 18px;
            border-radius: 30px;
            transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
            cursor: pointer;
            box-shadow: 0 2px 6px rgba(15, 23, 42, 0.03);
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }}
        .btn-filter-pill:hover {{
            background: #f8fafc;
            color: #2563eb;
            border-color: #bfdbfe;
            transform: translateY(-1px);
        }}
        .btn-filter-pill.active {{
            background: linear-gradient(135deg, #1e1b4b 0%, #2563eb 100%);
            color: #ffffff;
            border-color: #2563eb;
            box-shadow: 0 4px 14px rgba(37, 99, 235, 0.25);
        }}
        .filter-count {{
            background: rgba(0, 0, 0, 0.08);
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 11.5px;
            font-weight: 700;
        }}
        .btn-filter-pill.active .filter-count {{
            background: rgba(255, 255, 255, 0.25);
            color: #ffffff;
        }}

        /* Award Cards */
        .award-card {{
            background: #ffffff;
            border: 1px solid rgba(226, 232, 240, 0.9);
            border-radius: 18px;
            transition: transform 0.28s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.28s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.28s ease;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            height: 100%;
        }}
        .award-card:hover {{
            transform: translateY(-6px);
            box-shadow: 0 22px 40px -12px rgba(15, 23, 42, 0.14), 0 8px 16px -6px rgba(15, 23, 42, 0.06) !important;
            border-color: rgba(245, 158, 11, 0.4);
        }}
        .award-header-badge {{
            position: relative;
            width: 100%;
            height: 220px;
            padding: 0;
            margin: 0;
            background: #090e1a;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            border-top-left-radius: 17px;
            border-top-right-radius: 17px;
        }}
        .award-header-badge img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center;
            display: block;
            transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }}
        .award-card:hover .award-header-badge img {{
            transform: scale(1.05);
        }}
        .award-image-overlay {{
            position: absolute;
            inset: 0;
            background: linear-gradient(180deg, rgba(9, 14, 26, 0.35) 0%, rgba(9, 14, 26, 0.05) 50%, rgba(9, 14, 26, 0.45) 100%);
            pointer-events: none;
            z-index: 2;
        }}
        .award-tier-pill {{
            position: absolute;
            top: 14px;
            right: 14px;
            padding: 5px 13px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 0.5px;
            text-transform: uppercase;
            box-shadow: 0 4px 14px rgba(0,0,0,0.5);
            z-index: 5;
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
        }}
        .award-year-pill {{
            position: absolute;
            top: 14px;
            left: 14px;
            background: rgba(15, 23, 42, 0.88);
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.25);
            color: #f8fafc;
            padding: 4px 12px;
            border-radius: 15px;
            font-size: 11.5px;
            font-weight: 600;
            box-shadow: 0 4px 14px rgba(0,0,0,0.4);
            z-index: 5;
        }}
        .award-domain-tag-overlay {{
            position: absolute;
            bottom: 12px;
            left: 14px;
            background: rgba(15, 23, 42, 0.85);
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #93c5fd;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 0.5px;
            text-transform: uppercase;
            padding: 3px 10px;
            border-radius: 6px;
            z-index: 5;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.35);
        }}

        .tier-gold {{
            background: linear-gradient(135deg, #d97706 0%, #f59e0b 50%, #b45309 100%);
            color: #ffffff;
            border: 1px solid #fde68a;
        }}
        .tier-silver {{
            background: linear-gradient(135deg, #475569 0%, #94a3b8 100%);
            color: #ffffff;
            border: 1px solid #cbd5e1;
        }}
        .tier-bronze {{
            background: linear-gradient(135deg, #78350f 0%, #b45309 100%);
            color: #ffffff;
            border: 1px solid #fcd34d;
        }}
        .tier-purple {{
            background: linear-gradient(135deg, #6b21a8 0%, #a855f7 100%);
            color: #ffffff;
        }}
        .tier-blue {{
            background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
            color: #ffffff;
        }}
        .tier-emerald {{
            background: linear-gradient(135deg, #065f46 0%, #10b981 100%);
            color: #ffffff;
        }}
        .tier-coral {{
            background: linear-gradient(135deg, #c2410c 0%, #ea580c 100%);
            color: #ffffff;
        }}

        .award-card-body {{
            padding: 24px;
            flex-grow: 1;
        }}
        .award-cat-badge {{
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.75px;
            color: #2563eb;
            background: #eff6ff;
            padding: 3px 10px;
            border-radius: 6px;
            display: inline-block;
        }}
        body.dark-mode .award-cat-badge {{
            background: #1e3a8a;
            color: #93c5fd;
        }}
        .award-title {{
            font-size: 18.5px;
            font-weight: 700;
            color: #0f172a;
            line-height: 1.35;
        }}
        body.dark-mode .award-title {{
            color: #f8fafc;
        }}
        .award-issuing-org {{
            font-size: 13.5px;
            color: #475569;
        }}
        body.dark-mode .award-issuing-org {{
            color: #cbd5e1;
        }}
        .award-description {{
            font-size: 14.5px;
            line-height: 1.6;
            color: #334155;
        }}
        body.dark-mode .award-description {{
            color: #cbd5e1;
        }}

        .award-tags-container {{
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
        }}
        .award-tag {{
            font-size: 11px;
            font-weight: 600;
            color: #475569;
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 6px;
            padding: 3px 9px;
            cursor: pointer;
            transition: all 0.2s ease;
        }}
        .award-tag:hover {{
            background: #eff6ff;
            color: #2563eb;
            border-color: #bfdbfe;
        }}
        body.dark-mode .award-tag {{
            background: #1e293b;
            color: #cbd5e1;
            border-color: #334155;
        }}
        body.dark-mode .award-tag:hover {{
            background: #1e3a8a;
            color: #93c5fd;
            border-color: #60a5fa;
        }}

        .award-links-grid {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }}
        .btn-award-link {{
            background: #f8fafc;
            color: #1e293b;
            border: 1px solid #cbd5e1;
            font-size: 12.5px;
            font-weight: 600;
            padding: 6px 12px;
            border-radius: 8px;
            display: inline-flex;
            align-items: center;
            gap: 5px;
            transition: all 0.2s ease;
            text-decoration: none;
        }}
        .btn-award-link:hover {{
            background: #2563eb;
            color: #ffffff !important;
            border-color: #2563eb;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25);
        }}
        body.dark-mode .btn-award-link {{
            background: #1e293b;
            color: #f1f5f9;
            border-color: #475569;
        }}
        body.dark-mode .btn-award-link:hover {{
            background: #2563eb;
            color: #ffffff !important;
            border-color: #2563eb;
        }}

        .btn-copy-cite {{
            background: transparent;
            border: 1px dashed #cbd5e1;
            color: #64748b;
            font-size: 12px;
            font-weight: 600;
            padding: 7px 12px;
            border-radius: 8px;
            width: 100%;
            transition: all 0.2s ease;
            cursor: pointer;
            text-align: center;
        }}
        .btn-copy-cite:hover {{
            background: #f1f5f9;
            color: #1e293b;
            border-color: #94a3b8;
        }}
        body.dark-mode .btn-copy-cite {{
            border-color: #475569;
            color: #94a3b8;
        }}
        body.dark-mode .btn-copy-cite:hover {{
            background: #334155;
            color: #f8fafc;
            border-color: #64748b;
        }}

        /* Citation Modal */
        .cite-format-box {{
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 14px;
            font-family: monospace;
            font-size: 12.5px;
            color: #1e293b;
            white-space: pre-wrap;
            word-break: break-word;
            max-height: 180px;
            overflow-y: auto;
        }}
        body.dark-mode .cite-format-box {{
            background: #0f172a;
            border-color: #334155;
            color: #cbd5e1;
        }}

        /* Toast notification */
        #citeToast {{
            position: fixed;
            bottom: 25px;
            right: 25px;
            z-index: 9999;
            background: #1e1b4b;
            color: #ffffff;
            padding: 12px 24px;
            border-radius: 10px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            border-left: 4px solid #f59e0b;
            display: none;
            align-items: center;
            gap: 10px;
            font-size: 14px;
            font-weight: 600;
        }}

        /* Dark Mode Overrides */
        body.dark-mode .award-card {{
            background: #1e293b;
            border-color: #334155;
        }}
        body.dark-mode .award-card:hover {{
            border-color: #f59e0b;
            box-shadow: 0 20px 35px -10px rgba(0, 0, 0, 0.6) !important;
        }}
        body.dark-mode .btn-filter-pill {{
            background: #1e293b;
            border-color: #334155;
            color: #cbd5e1;
        }}
        body.dark-mode .btn-filter-pill:hover {{
            background: #334155;
            color: #fde68a;
            border-color: #f59e0b;
        }}
        body.dark-mode .btn-filter-pill.active {{
            background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
            color: #ffffff;
            border-color: #2563eb;
        }}
        body.dark-mode .search-input-field {{
            background: #1e293b;
            border-color: #334155;
            color: #f8fafc;
        }}
        body.dark-mode .search-input-field:focus {{
            border-color: #f59e0b;
            box-shadow: 0 0 0 4px rgba(245, 158, 11, 0.2);
        }}
        body.dark-mode .search-clear-btn {{
            background: #334155;
            color: #cbd5e1;
        }}

        /* Navbar Header & Nav Link Visibility */
        .navbar-custom {{
            background-color: rgba(255, 255, 255, 0.96) !important;
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            box-shadow: 0 4px 20px rgba(15, 23, 42, 0.06);
            border-bottom: 1px solid rgba(226, 232, 240, 0.8);
            padding: 16px 0;
            transition: all 0.3s ease;
        }}
        .navbar-custom .navigation .navbar-nav-link .nav-item .nav-link {{
            color: #334155 !important;
            font-weight: 600;
            font-size: 14.5px;
            transition: color 0.2s ease;
        }}
        .navbar-custom .navigation .navbar-nav-link .nav-item:hover .nav-link,
        .navbar-custom .navigation .navbar-nav-link .nav-item.active .nav-link {{
            color: #2563eb !important;
            font-weight: 700;
        }}
        body.dark-mode .navbar-custom {{
            background-color: rgba(11, 15, 25, 0.96) !important;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
        }}
        body.dark-mode .navbar-custom .navigation .navbar-nav-link .nav-item .nav-link {{
            color: #cbd5e1 !important;
        }}
        body.dark-mode .navbar-custom .navigation .navbar-nav-link .nav-item:hover .nav-link,
        body.dark-mode .navbar-custom .navigation .navbar-nav-link .nav-item.active .nav-link {{
            color: #60a5fa !important;
        }}
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
                    <li class="nav-item active">
                        <a class="nav-link" href="page-awards">Awards</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="page-memberships">Memberships</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="page-publications">Publications</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="page-portfolio">Portfolio</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="page-books">Books</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="page-events">Speaking</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="page-blog">Blog</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="index#contact">Contact</a>
                    </li>
                </ul>

                <div class="d-none d-lg-flex align-items-center ml-2">
                    <button type="button" class="theme-toggle-btn" aria-label="Toggle dark mode" title="Toggle theme">
                        <svg class="icon-moon" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
                        <svg class="icon-sun" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
                    </button>
                </div>
            </div>
        </div>
    </nav>
    <!-- Navbar End -->

    <!-- Awards Hero Section Start -->
    <section class="awards-hero-section">
        <div class="container text-center position-relative">
            <div class="row justify-content-center">
                <div class="col-lg-10">
                    <div class="mb-3">
                        <span class="award-hero-badge-pill">
                            <i class="mdi mdi-trophy-variant mr-1"></i> Executive Honors &amp; Global Recognitions
                        </span>
                    </div>
                    <h1 class="awards-hero-title text-white font-weight-bold display-4 mb-3" style="letter-spacing: -0.5px; color: #ffffff !important;">
                        Awards &amp; Distinctions
                    </h1>
                    <p class="lead mb-4" style="color: #cbd5e1; max-width: 820px; margin: 0 auto; font-size: 1.15rem; line-height: 1.6;">
                        Honoring pioneering achievements across enterprise AI innovation, autonomous cybersecurity architectures, scientific research, global power lists, and executive mentorship worldwide.
                    </p>
                    <div class="d-flex flex-wrap justify-content-center align-items-center" style="gap: 12px;">
                        <a href="#awards-grid" class="btn btn-warning rounded font-weight-bold px-4 py-2" style="background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); border: none; color: #111827;">
                            <i class="mdi mdi-trophy-award mr-1"></i> Explore {total_awards} Honors
                        </a>
                        <a href="page-memberships" class="btn btn-outline-light rounded font-weight-bold px-4 py-2">
                            <i class="mdi mdi-account-group mr-1"></i> View Memberships &amp; Fellowships
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- Awards Hero Section End -->

    <!-- Main Content Section -->
    <section class="section bg-light pt-0" id="awards-grid" style="padding-bottom: 80px;">
        <div class="container">
            <!-- Stats Ribbon -->
            <div class="awards-stats-box mb-5">
                <div class="row align-items-center">
                    <div class="col-6 col-md-3 border-right border-light-subtle">
                        <div class="award-stat-item">
                            <div class="award-stat-number">{total_awards}</div>
                            <div class="award-stat-label">Total Honors &amp; Awards</div>
                        </div>
                    </div>
                    <div class="col-6 col-md-3 border-right border-light-subtle">
                        <div class="award-stat-item">
                            <div class="award-stat-number">{gold_medals}</div>
                            <div class="award-stat-label">Gold, Silver &amp; Winners</div>
                        </div>
                    </div>
                    <div class="col-6 col-md-3 border-right border-light-subtle">
                        <div class="award-stat-item">
                            <div class="award-stat-number">{academic_honors}</div>
                            <div class="award-stat-label">Academic &amp; Leadership Titles</div>
                        </div>
                    </div>
                    <div class="col-6 col-md-3">
                        <div class="award-stat-item">
                            <div class="award-stat-number">{mentorship_hours}</div>
                            <div class="award-stat-label">Mentorship Minutes (ADPList)</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Search & Filters Header -->
            <div class="text-center mb-4">
                <h2 class="font-weight-bold text-dark mb-2" style="font-size: 2rem;">Honors Directory &amp; Verification</h2>
                <p class="text-muted" style="max-width: 680px; margin: 0 auto;">Search in real-time or filter by domain to inspect official credentials, citations, press releases, and global recognitions.</p>
            </div>

            <!-- Interactive Search Box -->
            <div class="search-container">
                <i class="mdi mdi-magnify search-icon-inside"></i>
                <input type="text" id="awardSearchInput" class="search-input-field" placeholder="Search by award title, institution (e.g. Stevie, Forttuna, MIT), domain, or tag..." oninput="handleSearch()">
                <button type="button" id="clearSearchBtn" class="search-clear-btn" style="display: none;" onclick="clearSearch()" title="Clear search">
                    <i class="mdi mdi-close"></i>
                </button>
            </div>

            <!-- Category Filter Pills -->
            <div class="filter-nav-wrap">
                <button type="button" class="btn-filter-pill active" onclick="setCategoryFilter('all', this)">
                    <i class="mdi mdi-apps"></i> All Honors <span class="filter-count" id="count-all">{total_awards}</span>
                </button>
                <button type="button" class="btn-filter-pill" onclick="setCategoryFilter('ai-cyber', this)">
                    <i class="mdi mdi-shield-lock-outline"></i> AI &amp; Cybersecurity Innovation <span class="filter-count" id="count-ai">7</span>
                </button>
                <button type="button" class="btn-filter-pill" onclick="setCategoryFilter('leadership', this)">
                    <i class="mdi mdi-crown-outline"></i> Global Leadership &amp; Power Lists <span class="filter-count" id="count-lead">2</span>
                </button>
                <button type="button" class="btn-filter-pill" onclick="setCategoryFilter('academic-fellowships', this)">
                    <i class="mdi mdi-school-outline"></i> Academic &amp; Fellowships <span class="filter-count" id="count-acad">7</span>
                </button>
                <button type="button" class="btn-filter-pill" onclick="setCategoryFilter('mentorship-advisory', this)">
                    <i class="mdi mdi-account-multiple-outline"></i> Mentorship &amp; Advisory <span class="filter-count" id="count-mentor">5</span>
                </button>
                <button type="button" class="btn-filter-pill" onclick="setCategoryFilter('media-speaking', this)">
                    <i class="mdi mdi-bullhorn-outline"></i> Media, Keynotes &amp; Journals <span class="filter-count" id="count-media">3</span>
                </button>
            </div>

            <!-- Results Count Bar -->
            <div class="d-flex justify-content-between align-items-center mb-4 px-2">
                <div class="text-muted small">
                    Showing <strong id="visibleAwardsCount" class="text-primary font-weight-bold">{total_awards}</strong> of {total_awards} honors
                </div>
                <div class="d-flex align-items-center" style="gap: 10px;">
                    <span class="badge badge-pill badge-light border text-muted px-3 py-1 font-weight-bold">
                        <i class="mdi mdi-check-decagram text-success mr-1"></i> 100% Verified Credentials
                    </span>
                </div>
            </div>

            <!-- Awards Cards Grid -->
            <div class="row" id="awardsContainer">
                {cards_html}
            </div>

            <!-- Empty State for Search -->
            <div id="noAwardsFound" class="text-center py-5" style="display: none;">
                <div class="mb-3">
                    <i class="mdi mdi-trophy-broken text-muted" style="font-size: 54px;"></i>
                </div>
                <h4 class="font-weight-bold text-dark mb-2">No honors matching your search</h4>
                <p class="text-muted mb-3">Try adjusting your keywords, searching by organization (e.g., 'Stanford', 'Stevie', 'Google'), or clear filters.</p>
                <button type="button" class="btn btn-primary btn-sm rounded font-weight-bold px-4" onclick="clearSearch()">
                    <i class="mdi mdi-refresh mr-1"></i> Reset Search &amp; Filters
                </button>
            </div>

            <!-- Cross Navigation Banner -->
            <div class="mt-5 p-4 p-md-5 rounded-lg border shadow-sm" style="background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); color: #ffffff;">
                <div class="row align-items-center">
                    <div class="col-lg-8 mb-3 mb-lg-0">
                        <span class="badge badge-warning text-dark font-weight-bold px-3 py-1 mb-2" style="background-color: #fef08a;">
                            <i class="mdi mdi-certificate mr-1"></i> Intellectual Property &amp; Memberships
                        </span>
                        <h3 class="font-weight-bold text-white mb-2" style="font-size: 1.6rem;">Explore Connected Research &amp; Governance</h3>
                        <p class="text-light mb-0" style="opacity: 0.9; font-size: 14.5px; line-height: 1.6;">
                            Review Harsh Verma's portfolio of 6 patents (1 granted, 4 in-process at Palo Alto Networks), 22+ IEEE publications, and senior council fellowships across IEEE, Forbes Technology Council, and Sigma Xi.
                        </p>
                    </div>
                    <div class="col-lg-4 text-lg-right">
                        <a href="page-publications" class="btn btn-light rounded font-weight-bold px-3 py-2 mr-2 mb-2">
                            <i class="mdi mdi-book-open-page-variant mr-1"></i> Publications &amp; Patents
                        </a>
                        <a href="page-memberships" class="btn btn-outline-light rounded font-weight-bold px-3 py-2 mb-2">
                            <i class="mdi mdi-account-group mr-1"></i> Memberships
                        </a>
                    </div>
                </div>
            </div>
        </div>
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

    <!-- Citation / Dossier Modal -->
    <div class="modal fade" id="awardCiteModal" tabindex="-1" role="dialog" aria-labelledby="awardCiteModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered modal-lg" role="document">
            <div class="modal-content border-0 shadow">
                <div class="modal-header bg-dark text-white">
                    <h5 class="modal-title font-weight-bold" id="awardCiteModalLabel">
                        <i class="mdi mdi-certificate mr-1 text-warning"></i> Award Citation &amp; Verification Dossier
                    </h5>
                    <button type="button" class="close text-white" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body p-4">
                    <div class="mb-3">
                        <span class="badge badge-primary px-3 py-1 font-weight-bold mb-2" id="modalAwardYear">2026</span>
                        <h4 class="font-weight-bold text-dark" id="modalAwardTitle">Award Title</h4>
                        <p class="text-muted mb-3" id="modalAwardOrg">Issuing Authority</p>
                    </div>

                    <div class="form-group mb-3">
                        <label class="font-weight-bold text-dark small text-uppercase">Standard Academic / APA Citation</label>
                        <div class="cite-format-box" id="modalApaCitation">Citation text...</div>
                    </div>

                    <div class="form-group mb-3">
                        <label class="font-weight-bold text-dark small text-uppercase">Press &amp; Bio Attribution Snippet</label>
                        <div class="cite-format-box" id="modalPressCitation">Press text...</div>
                    </div>
                </div>
                <div class="modal-footer bg-light">
                    <button type="button" class="btn btn-secondary btn-sm rounded font-weight-bold" data-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary btn-sm rounded font-weight-bold px-3" onclick="copyModalCitation()">
                        <i class="mdi mdi-content-copy mr-1"></i> Copy Citation to Clipboard
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- Interactive Toast Notification -->
    <div id="citeToast">
        <i class="mdi mdi-check-circle text-warning font-weight-bold" style="font-size: 20px;"></i>
        <span id="toastMessage">Citation copied to clipboard!</span>
    </div>

    <!-- Scripts -->
    <script src="js/jquery.min.js"></script>
    <script src="js/bootstrap.bundle.min.js"></script>
    <script src="js/feather.min.js"></script>

    <script>
        feather.replace();

        var currentCategory = 'all';
        var currentActiveCitation = '';

        function setCategoryFilter(category, buttonElement) {{
            currentCategory = category;
            
            // Update active pill
            var pills = document.querySelectorAll('.btn-filter-pill');
            pills.forEach(function(pill) {{
                pill.classList.remove('active');
            }});
            if (buttonElement) {{
                buttonElement.classList.add('active');
            }}

            filterAwards();
        }}

        function filterByTag(tagName) {{
            var searchInput = document.getElementById('awardSearchInput');
            searchInput.value = tagName;
            handleSearch();
            searchInput.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
        }}

        function handleSearch() {{
            var searchInput = document.getElementById('awardSearchInput');
            var clearBtn = document.getElementById('clearSearchBtn');
            if (searchInput.value.trim().length > 0) {{
                clearBtn.style.display = 'flex';
            }} else {{
                clearBtn.style.display = 'none';
            }}
            filterAwards();
        }}

        function clearSearch() {{
            var searchInput = document.getElementById('awardSearchInput');
            searchInput.value = '';
            document.getElementById('clearSearchBtn').style.display = 'none';
            setCategoryFilter('all', document.querySelector('.btn-filter-pill'));
            filterAwards();
        }}

        function filterAwards() {{
            var query = document.getElementById('awardSearchInput').value.toLowerCase().trim();
            var cards = document.querySelectorAll('.award-card-col');
            var visibleCount = 0;

            cards.forEach(function(card) {{
                var cardCat = card.getAttribute('data-category');
                var cardSearch = card.getAttribute('data-search');

                var matchesCat = (currentCategory === 'all') || (cardCat === currentCategory);
                var matchesQuery = (query === '') || (cardSearch.indexOf(query) !== -1);

                if (matchesCat && matchesQuery) {{
                    card.style.display = '';
                    visibleCount++;
                }} else {{
                    card.style.display = 'none';
                }}
            }});

            document.getElementById('visibleAwardsCount').innerText = visibleCount;
            var emptyState = document.getElementById('noAwardsFound');
            if (visibleCount === 0) {{
                emptyState.style.display = 'block';
            }} else {{
                emptyState.style.display = 'none';
            }}
        }}

        function openCiteModal(aid, title, org, year, citation) {{
            document.getElementById('modalAwardTitle').innerText = title;
            document.getElementById('modalAwardOrg').innerText = org;
            document.getElementById('modalAwardYear').innerText = year;
            document.getElementById('modalApaCitation').innerText = citation;
            
            var pressSnippet = "Harsh Verma was recognized with the " + title + " by " + org + " (" + year + ") for distinguished contributions to enterprise AI architectures and cybersecurity.";
            document.getElementById('modalPressCitation').innerText = pressSnippet;
            currentActiveCitation = citation + "\\n\\n" + pressSnippet;

            $('#awardCiteModal').modal('show');
        }}

        function copyModalCitation() {{
            if (!currentActiveCitation) return;
            if (navigator.clipboard) {{
                navigator.clipboard.writeText(currentActiveCitation).then(function() {{
                    showToast("Citation copied to clipboard!");
                    $('#awardCiteModal').modal('hide');
                }}).catch(function() {{
                    prompt("Copy Citation:", currentActiveCitation);
                }});
            }} else {{
                prompt("Copy Citation:", currentActiveCitation);
            }}
        }}

        function showToast(msg) {{
            var toast = document.getElementById('citeToast');
            document.getElementById('toastMessage').innerText = msg;
            toast.style.display = 'flex';
            setTimeout(function() {{
                toast.style.display = 'none';
            }}, 3000);
        }}
    </script>
</body>
</html>
'''

with open("page-awards.html", "w", encoding="utf-8") as f:
    f.write(html_page)

print("Created page-awards.html successfully.")
