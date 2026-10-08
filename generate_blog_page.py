#!/usr/bin/env python3
"""
Generate a modern, highly interactive, searchable Blog and Publications page
featuring all articles across Forbes Technology Council, HackerNoon, The AI Journal,
RSA Conference, Founders Creative, and Podcasts/Interviews.
"""

import json
import os

articles_data = [
    # --- Forbes Technology Council ---
    {
        "id": "forbes-real-ai-moat",
        "title": "The Real AI Moat: Why Models Are Cheap But Data Orchestration Is Priceless",
        "platform": "Forbes",
        "platform_full": "Forbes Technology Council",
        "platform_badge": "Forbes Council",
        "platform_icon": "mdi-database-sync",
        "platform_color": "#111827",
        "category": "Enterprise AI Strategy",
        "url": "https://www.forbes.com/councils/forbestechcouncil/2026/10/02/the-real-ai-moat-why-models-are-cheap-but-data-orchestration-is-priceless/",
        "author_profile": "https://www.forbes.com/councils/forbestechcouncil/people/harshverma/",
        "thumbnail": "images/blog/thumbnails/forbes-real-ai-moat.jpg",
        "date": "October 2, 2026",
        "read_time": "6 min read",
        "featured": True,
        "description": "As frontier models commoditize and open-source alternatives catch up, owning raw models offers little defensibility. The true enterprise AI moat lies in continuous data orchestration, clean operational governance, domain-specific data pipelines, and high-fidelity contextual retrieval.",
        "tags": ["Forbes Tech Council", "Data Orchestration", "AI Moat", "Enterprise AI", "Systems Architecture"]
    },
    {
        "id": "forbes-beyond-code",
        "title": "Beyond The Code: The Evolution Of The Next-Generation Engineer",
        "platform": "Forbes",
        "platform_full": "Forbes Technology Council",
        "platform_badge": "Forbes Council",
        "platform_icon": "mdi-shield-star",
        "platform_color": "#111827",
        "category": "Engineering Leadership",
        "url": "https://www.forbes.com/councils/forbestechcouncil/2026/04/20/beyond-the-code-the-evolution-of-the-next-generation-engineer/",
        "author_profile": "https://www.forbes.com/councils/forbestechcouncil/people/harshverma/",
        "thumbnail": "images/blog/thumbnails/forbes-beyond-code.jpg",
        "date": "April 20, 2026",
        "read_time": "5 min read",
        "featured": True,
        "description": "As code generation becomes commoditized, the next generation of engineers will differentiate through systems architecture, deterministic safety guardrails, prompt unit economics, and holistic cognitive system design.",
        "tags": ["Forbes Tech Council", "Next-Gen Engineer", "Systems Architecture", "AI Evolution", "Leadership"]
    },
    {
        "id": "forbes-intelligence-dollar",
        "title": "The Intelligence Per Dollar Metric: How Influential Leaders Measure AI Success",
        "platform": "Forbes",
        "platform_full": "Forbes Technology Council",
        "platform_badge": "Forbes Council",
        "platform_icon": "mdi-chart-line-variant",
        "platform_color": "#111827",
        "category": "AI Economics & ROI",
        "url": "https://www.forbes.com/councils/forbestechcouncil/2026/05/18/the-intelligence-per-dollar-metric-how-influential-leaders-measure-ai-success/",
        "author_profile": "https://www.forbes.com/councils/forbestechcouncil/people/harshverma/",
        "thumbnail": "images/blog/thumbnails/forbes-intelligence-dollar.jpg",
        "date": "May 18, 2026",
        "read_time": "6 min read",
        "featured": True,
        "description": "Moving past vanity parameter counts to evaluate enterprise AI investments through cost-performance efficiency, token ROI, deterministic output density, and measurable business throughput.",
        "tags": ["Forbes Tech Council", "AI ROI", "Unit Economics", "Executive Metrics", "Cloud Spend"]
    },
    {
        "id": "forbes-personalized-ai",
        "title": "Personalized AI Systems: The Hidden Trade-Off Behind Smarter AI (Personalization vs. Privacy)",
        "platform": "Forbes",
        "platform_full": "Forbes Technology Council",
        "platform_badge": "Forbes Council",
        "platform_icon": "mdi-lock-outline",
        "platform_color": "#111827",
        "category": "Privacy & Security",
        "url": "https://www.forbes.com/councils/forbestechcouncil/2026/06/11/personalized-ai-systems-the-hidden-trade-off-behind-smarter-ai-personalization-vs-privacy/",
        "author_profile": "https://www.forbes.com/councils/forbestechcouncil/people/harshverma/",
        "thumbnail": "images/blog/thumbnails/forbes-personalized-ai.jpg",
        "date": "June 11, 2026",
        "read_time": "5 min read",
        "featured": False,
        "description": "An architectural examination of the fundamental tension between contextual user personalization and enterprise zero-trust data privacy in modern retrieval and agent ecosystems.",
        "tags": ["Forbes Tech Council", "Privacy", "Personalization", "Data Sovereignty", "Zero Trust"]
    },
    {
        "id": "forbes-first-agent-experiment",
        "title": "Your First AI Agent Is An Experiment, Not A Product",
        "platform": "Forbes",
        "platform_full": "Forbes Technology Council",
        "platform_badge": "Forbes Council",
        "platform_icon": "mdi-flask-outline",
        "platform_color": "#111827",
        "category": "Agent Product Strategy",
        "url": "https://www.forbes.com/councils/forbestechcouncil/2026/07/23/your-first-ai-agent-is-an-experiment-not-a-product/",
        "author_profile": "https://www.forbes.com/councils/forbestechcouncil/people/harshverma/",
        "thumbnail": "images/blog/thumbnails/forbes-first-agent-experiment.jpg",
        "date": "July 23, 2026",
        "read_time": "5 min read",
        "featured": False,
        "description": "Autonomous agents behave like evolving operational actors rather than predictable static code. Why founders and enterprise teams must adopt bounded experimental sandboxes before productizing.",
        "tags": ["Forbes Tech Council", "Agentic AI", "Product Strategy", "Experimentation", "Fail-Safe Design"]
    },
    {
        "id": "forbes-pure-determinism",
        "title": "Engineering The Predictable: Why Pure Determinism Is Becoming The New Premium In AI Architecture",
        "platform": "Forbes",
        "platform_full": "Forbes Technology Council",
        "platform_badge": "Forbes Council",
        "platform_icon": "mdi-cog-sync",
        "platform_color": "#111827",
        "category": "System Architecture",
        "url": "https://www.forbes.com/councils/forbestechcouncil/2026/08/25/engineering-the-predictable-why-pure-determinism-is-becoming-the-new-premium-in-ai-architecture/",
        "author_profile": "https://www.forbes.com/councils/forbestechcouncil/people/harshverma/",
        "thumbnail": "images/blog/thumbnails/forbes-pure-determinism.jpg",
        "date": "August 25, 2026",
        "read_time": "6 min read",
        "featured": True,
        "description": "In mission-critical enterprise environments, repeatability and mathematical predictability command a higher commercial premium than stochastic creativity. How to design deterministic control layers over generative models.",
        "tags": ["Forbes Tech Council", "Determinism", "AI Architecture", "Enterprise Security", "Reliability"]
    },

    # --- HackerNoon Spotlight & Articles ---
    {
        "id": "hn-interview",
        "title": "The Production Gap: Your AI Model Isn’t as Reliable as You Think [Feature Interview]",
        "platform": "HackerNoon",
        "platform_full": "HackerNoon Feature Interview",
        "platform_badge": "Featured Interview",
        "platform_icon": "mdi-account-voice",
        "platform_color": "#00ea62",
        "category": "Interviews",
        "url": "https://hackernoon.com/the-production-gap-your-ai-model-isnt-as-reliable-as-you-think-interview",
        "author_profile": "https://hackernoon.com/u/harshverma59",
        "thumbnail": "images/blog/thumbnails/hn-interview.png",
        "date": "2026",
        "read_time": "8 min read",
        "featured": True,
        "description": "In-depth HackerNoon interview breaking down the critical gap between benchmark performance and enterprise production reality, detailing architectural strategies for resilient model deployment.",
        "tags": ["HackerNoon", "Interview", "AI Reliability", "Production ML", "Enterprise AI"]
    },
    {
        "id": "hn-identity-perimeter",
        "title": "Identity Is the New Perimeter: Managing AI Agents as Digital Actors",
        "platform": "HackerNoon",
        "platform_full": "HackerNoon (Spotify Tech Brief Podcast)",
        "platform_badge": "Article & Podcast",
        "platform_icon": "mdi-podcast",
        "platform_color": "#00ea62",
        "category": "AI Security",
        "url": "https://hackernoon.com/identity-is-the-new-perimeter-managing-ai-agents-as-digital-actors",
        "author_profile": "https://hackernoon.com/u/harshverma59",
        "spotify_url": "https://open.spotify.com/episode/0aDrp6DxLSSlWQ6gwfbi0l",
        "podcast_feed": "https://feeds.transistor.fm/cybersecurity-tech-brief-by-hackernoon",
        "thumbnail": "images/blog/thumbnails/hn-identity-perimeter.png",
        "date": "2026",
        "read_time": "7 min read",
        "featured": True,
        "has_audio": True,
        "description": "AI agents are transforming cybersecurity from network perimeter defenses to continuous identity-first authorization. Featured on HackerNoon's Cybersecurity Tech Brief podcast on Spotify.",
        "tags": ["HackerNoon", "AI Security", "Identity Access", "Spotify Podcast", "Agent Governance"]
    },
    {
        "id": "hn-clean-attack",
        "title": "The Clean Attack Problem: When Nothing Looks Wrong, but Everything Is Compromised",
        "platform": "HackerNoon",
        "platform_full": "HackerNoon & RSAC",
        "platform_badge": "HackerNoon",
        "platform_icon": "mdi-shield-alert",
        "platform_color": "#00ea62",
        "category": "Cybersecurity",
        "url": "https://hackernoon.com/the-clean-attack-problem-when-nothing-looks-wrong-but-everything-is-compromised",
        "author_profile": "https://hackernoon.com/u/harshverma59",
        "thumbnail": "images/blog/thumbnails/hn-clean-attack.png",
        "date": "2026",
        "read_time": "6 min read",
        "featured": True,
        "description": "Modern cyber threats no longer trigger noisy alarms. By abusing authorized API credentials and valid business logic, AI-driven attacks operate entirely within legitimate parameters.",
        "tags": ["HackerNoon", "Cybersecurity", "Zero Trust", "Silent Exploits", "Threat Modeling"]
    },
    {
        "id": "hn-speed-reliability",
        "title": "The Trade-Off Between Speed and Reliability in Modern AI Systems",
        "platform": "HackerNoon",
        "platform_full": "HackerNoon",
        "platform_badge": "HackerNoon",
        "platform_icon": "mdi-speedometer",
        "platform_color": "#00ea62",
        "category": "System Architecture",
        "url": "https://hackernoon.com/the-trade-off-between-speed-and-reliability-in-modern-ai-systems",
        "author_profile": "https://hackernoon.com/u/harshverma59",
        "thumbnail": "images/blog/thumbnails/hn-speed-reliability.png",
        "date": "2026",
        "read_time": "6 min read",
        "featured": False,
        "description": "'Move fast and break things' causes catastrophic failure in mission-critical AI. Why leading architectural teams prioritize deterministic verification over raw inference speed.",
        "tags": ["HackerNoon", "AI Reliability", "Latency vs Quality", "Deterministic Guardrails"]
    },
    {
        "id": "hn-governance",
        "title": "AI Governance Is Failing Because We’re Regulating Models Instead of Behavior",
        "platform": "HackerNoon",
        "platform_full": "HackerNoon",
        "platform_badge": "HackerNoon",
        "platform_icon": "mdi-gavel",
        "platform_color": "#00ea62",
        "category": "Governance & Policy",
        "url": "https://hackernoon.com/ai-governance-is-failing-because-were-regulating-models-instead-of-behavior",
        "author_profile": "https://hackernoon.com/u/harshverma59",
        "thumbnail": "images/blog/thumbnails/hn-governance.png",
        "date": "2026",
        "read_time": "6 min read",
        "featured": False,
        "description": "An analysis of why static model audits fail to capture multi-agent emergent behavior, and why runtime behavioral observability is the only defensible governance framework.",
        "tags": ["HackerNoon", "AI Governance", "Compliance", "Model Audits", "Behavioral Safety"]
    },
    {
        "id": "hn-observability",
        "title": "The Observability Crisis in AI Systems: Why Your Logs Are Lying to You",
        "platform": "HackerNoon",
        "platform_full": "HackerNoon",
        "platform_badge": "HackerNoon",
        "platform_icon": "mdi-eye-off-outline",
        "platform_color": "#00ea62",
        "category": "Observability",
        "url": "https://hackernoon.com/the-observability-crisis-in-ai-systems-why-your-logs-are-lying-to-you",
        "author_profile": "https://hackernoon.com/u/harshverma59",
        "thumbnail": "images/blog/thumbnails/hn-observability.png",
        "date": "2026",
        "read_time": "7 min read",
        "featured": False,
        "description": "Standard logging stacks report HTTP 200s while models silently hallucinate, leak context, and drift. How semantic telemetry and cognitive tracing resolve the observability gap.",
        "tags": ["HackerNoon", "Observability", "Telemetry", "Debugging AI", "Tracing"]
    },
    {
        "id": "hn-reputation",
        "title": "Reputation Systems for AI Agents: The Missing Layer of Trust",
        "platform": "HackerNoon",
        "platform_full": "HackerNoon",
        "platform_badge": "HackerNoon",
        "platform_icon": "mdi-shield-star-outline",
        "platform_color": "#00ea62",
        "category": "Trust & Safety",
        "url": "https://hackernoon.com/reputation-systems-for-ai-agents-the-missing-layer-of-trust",
        "author_profile": "https://hackernoon.com/u/harshverma59",
        "thumbnail": "images/blog/thumbnails/hn-reputation.png",
        "date": "2026",
        "read_time": "6 min read",
        "featured": False,
        "description": "Introducing behavioral scoring protocols and cryptographic audit trails to quantify trust before allowing autonomous agents to execute high-stakes cross-enterprise tasks.",
        "tags": ["HackerNoon", "Trust Scores", "Multi-Agent", "Reputation", "Decentralized Trust"]
    },
    {
        "id": "hn-distributed-intelligence",
        "title": "Distributed Intelligence: Why Multi-Agent Systems Are the Successor to Microservices",
        "platform": "HackerNoon",
        "platform_full": "HackerNoon",
        "platform_badge": "HackerNoon",
        "platform_icon": "mdi-lan",
        "platform_color": "#00ea62",
        "category": "Distributed Systems",
        "url": "https://hackernoon.com/distributed-intelligence-why-multi-agent-systems-are-the-successor-to-microservices-for-enterprise",
        "author_profile": "https://hackernoon.com/u/harshverma59",
        "thumbnail": "images/blog/thumbnails/hn-distributed-intelligence.png",
        "date": "2026",
        "read_time": "7 min read",
        "featured": False,
        "description": "Just as microservices decomposed monolithic codebases, autonomous multi-agent networks are decomposing complex reasoning workflows into distributed, collaborative nodes.",
        "tags": ["HackerNoon", "Multi-Agent Systems", "Distributed Intelligence", "Microservices", "Architecture"]
    },
    {
        "id": "hn-identity-intent",
        "title": "From Identity to Intent: Autonomous AI Agents Are the New Insider Threat",
        "platform": "HackerNoon",
        "platform_full": "HackerNoon",
        "platform_badge": "HackerNoon",
        "platform_icon": "mdi-incognito",
        "platform_color": "#00ea62",
        "category": "Cybersecurity",
        "url": "https://hackernoon.com/from-identity-to-intent-autonomous-ai-agents-are-the-new-insider-threat",
        "author_profile": "https://hackernoon.com/u/harshverma59",
        "thumbnail": "images/blog/thumbnails/hn-identity-intent.png",
        "date": "2026",
        "read_time": "6 min read",
        "featured": False,
        "description": "When AI agents are granted access to internal production pipelines, authentication alone cannot prevent prompt injection or goal hijacking. We need continuous intent validation.",
        "tags": ["HackerNoon", "Insider Threat", "Agent Security", "Zero Trust", "Intent Analysis"]
    },
    {
        "id": "hn-trust-scores",
        "title": "Trust Scores for AI: Should Agents Earn Permissions Over Time? Trust Isn’t Granted, It’s Earned",
        "platform": "HackerNoon",
        "platform_full": "HackerNoon",
        "platform_badge": "HackerNoon",
        "platform_icon": "mdi-certificate-outline",
        "platform_color": "#00ea62",
        "category": "Access Control",
        "url": "https://hackernoon.com/trust-scores-for-ai-should-agents-earn-permissions-over-time-trust-isnt-granted-its-earned",
        "author_profile": "https://hackernoon.com/u/harshverma59",
        "thumbnail": "images/blog/thumbnails/hn-trust-scores.png",
        "date": "2026",
        "read_time": "6 min read",
        "featured": False,
        "description": "A dynamic least-privilege architecture where autonomous digital actors start in sandboxed environments and earn higher API thresholds through validated track records.",
        "tags": ["HackerNoon", "Dynamic Permissions", "Least Privilege", "Trust Scoring", "Agent Policy"]
    },
    {
        "id": "hn-ai-orchestrator",
        "title": "The Rise of the AI Orchestrator: The Latest, Most Important Enterprise Role",
        "platform": "HackerNoon",
        "platform_full": "HackerNoon",
        "platform_badge": "HackerNoon",
        "platform_icon": "mdi-account-cog",
        "platform_color": "#00ea62",
        "category": "Engineering Leadership",
        "url": "https://hackernoon.com/the-rise-of-the-ai-orchestrator-the-latest-most-important-enterprise-role",
        "author_profile": "https://hackernoon.com/u/harshverma59",
        "thumbnail": "images/blog/thumbnails/hn-ai-orchestrator.png",
        "date": "2026",
        "read_time": "6 min read",
        "featured": False,
        "description": "Enterprises don't struggle to access LLMs; they struggle to orchestrate multiple models, routing state, memory, tool executions, and security guardrails across departments.",
        "tags": ["HackerNoon", "AI Orchestration", "Enterprise Roles", "Cognitive Mesh", "Workflow"]
    },
    {
        "id": "hn-autonomy-trap",
        "title": "What Most AI Startup Founders Get Wrong About AI Agents: The Autonomy Trap",
        "platform": "HackerNoon",
        "platform_full": "HackerNoon",
        "platform_badge": "HackerNoon",
        "platform_icon": "mdi-rocket-launch-outline",
        "platform_color": "#00ea62",
        "category": "Startups & Strategy",
        "url": "https://hackernoon.com/what-most-ai-startup-founders-get-wrong-about-ai-agents-the-autonomy-trap",
        "author_profile": "https://hackernoon.com/u/harshverma59",
        "thumbnail": "images/blog/thumbnails/hn-autonomy-trap.png",
        "date": "2026",
        "read_time": "6 min read",
        "featured": False,
        "description": "Unconstrained autonomy produces brittle demos that collapse in real customer deployments. Why the most valuable agentic startups build scoped, deterministic workflows.",
        "tags": ["HackerNoon", "Startup Founders", "Autonomy Trap", "Product Design", "Venture"]
    },

    # --- RSA Conference (RSAC) ---
    {
        "id": "rsac-clean-attack",
        "title": "The Clean Attack Problem: When Nothing Looks Wrong but Everything is Compromised",
        "platform": "RSA Conference",
        "platform_full": "RSA Conference Expert Library",
        "platform_badge": "RSA Conference",
        "platform_icon": "mdi-shield-check",
        "platform_color": "#c41230",
        "category": "Cybersecurity",
        "url": "https://www.rsaconference.com/library/blog/the-clean-attack-problem",
        "author_profile": "https://www.rsaconference.com/experts/Harsh%20Verma",
        "thumbnail": "images/blog/thumbnails/hn-clean-attack.png",
        "date": "August 2026",
        "read_time": "7 min read",
        "featured": True,
        "description": "Published on RSA Conference official library: How AI agents mimic legitimate human interactions, adapt to organizational context, and operate within approved API policies to evade legacy SOC detection.",
        "tags": ["RSA Conference", "RSAC Expert", "Clean Attacks", "Behavioral Security", "Enterprise SOC"]
    },
    {
        "id": "rsac-death-of-authentication",
        "title": "The Death of Authentication: Why Identity Isn't Enough for AI Systems",
        "platform": "RSA Conference",
        "platform_full": "RSA Conference Expert Library",
        "platform_badge": "RSA Conference",
        "platform_icon": "mdi-shield-check",
        "platform_color": "#c41230",
        "category": "Cybersecurity",
        "url": "https://www.rsaconference.com/Library/blog/the-death-of-authentication-why-identity-isnt-enough-for-ai-systems",
        "author_profile": "https://www.rsaconference.com/experts/Harsh%20Verma",
        "thumbnail": "images/blog/thumbnails/rsac-death-of-authentication.jpg",
        "date": "September 2026",
        "read_time": "8 min read",
        "featured": True,
        "description": "Published on RSA Conference official library: For decades cybersecurity assumed verifying identity ensures legitimate behavior. In autonomous AI workflows, attacks happen with valid credentials and approved permissions. Why Zero Trust must evolve to continuous behavioral monitoring and runtime intent analysis.",
        "tags": ["RSA Conference", "RSAC Expert", "Zero Trust", "AI Security", "Intent Analysis"]
    },
    {
        "id": "rsac-agents-rules",
        "title": "Agents Don't Break Rules, They Redefine Them",
        "platform": "RSA Conference",
        "platform_full": "RSA Conference Expert Library",
        "platform_badge": "RSA Conference",
        "platform_icon": "mdi-shield-check",
        "platform_color": "#c41230",
        "category": "Cybersecurity",
        "url": "https://www.rsaconference.com/Library/blog/agents-dont-break-rules-they-redefine-them",
        "author_profile": "https://www.rsaconference.com/experts/Harsh%20Verma",
        "thumbnail": "images/blog/thumbnails/rsac-agents-rules.jpg",
        "date": "September 24, 2026",
        "read_time": "7 min read",
        "featured": True,
        "description": "Published on RSA Conference official library: Autonomous AI agents don't fail by breaking rules—they follow instructions literally while circumventing intent through blind optimization and policy drift. Why AI security requires continuous runtime governance instead of static boundaries.",
        "tags": ["RSA Conference", "RSAC Expert", "Agentic AI", "Policy Drift", "Continuous Governance", "AI Security"]
    },

    # --- The AI Journal (aijourn.com) ---
    {
        "id": "aij-agentic-framework",
        "title": "Harsh Verma Publishes Nuanced Framework on Rise of Agentic AI and Enterprise System Era",
        "platform": "The AI Journal",
        "platform_full": "The AI Journal",
        "platform_badge": "AI Journal",
        "platform_icon": "mdi-newspaper-variant",
        "platform_color": "#2563eb",
        "category": "System Architecture",
        "url": "https://aijourn.com/harsh-verma-publishes-nuanced-framework-on-rise-of-agentic-ai-and-enterprise-system-era-arguing-ai-system-architecture-has-replaced-model-building-as-the-core-discipline/",
        "author_profile": "https://aijourn.com/",
        "thumbnail": "images/blog/thumbnails/aij-agentic-framework.jpg",
        "date": "May 2026",
        "read_time": "6 min read",
        "featured": True,
        "description": "Argues that AI system architecture—context routing, deterministic verification, persistent memory, and latency orchestration—has decisively replaced raw model training as the primary core discipline.",
        "tags": ["The AI Journal", "Agentic AI", "Enterprise Era", "System Architecture", "Framework"]
    },
    {
        "id": "aij-high-stakes",
        "title": "How AI Agents Will Collaborate with Human Experts in High-Stakes Environments",
        "platform": "The AI Journal",
        "platform_full": "The AI Journal",
        "platform_badge": "AI Journal",
        "platform_icon": "mdi-account-group",
        "platform_color": "#2563eb",
        "category": "Human-AI Collaboration",
        "url": "https://aijourn.com/how-ai-agents-will-collaborate-with-human-experts-in-high-stakes-environments/",
        "author_profile": "https://aijourn.com/",
        "thumbnail": "images/blog/thumbnails/aij-high-stakes.jpg",
        "date": "May 2026",
        "read_time": "6 min read",
        "featured": False,
        "description": "Analyzing how human-in-the-loop and human-on-the-loop protocols should be structured across high-consequence domains including automated threat response, medicine, and critical infrastructure.",
        "tags": ["The AI Journal", "Human-AI Collaboration", "High Stakes", "Decision Systems", "Safety"]
    },
    {
        "id": "aij-beyond-code",
        "title": "Harsh Verma on Engineering Beyond the Code: The Future of AI and Cybersecurity",
        "platform": "The AI Journal",
        "platform_full": "The AI Journal",
        "platform_badge": "AI Journal Feature",
        "platform_icon": "mdi-shield-search",
        "platform_color": "#2563eb",
        "category": "Interviews & Profiles",
        "url": "https://aijourn.com/harsh-verma-on-engineering-beyond-the-code-the-future-of-ai-and-cybersecurity/",
        "author_profile": "https://aijourn.com/",
        "thumbnail": "images/blog/thumbnails/aij-beyond-code.jpg",
        "date": "March 2026",
        "read_time": "7 min read",
        "featured": False,
        "description": "Featured conversation on the convergence of large-scale artificial intelligence, autonomous security operations, and the future career trajectory of AI systems engineers.",
        "tags": ["The AI Journal", "Feature Profile", "Cybersecurity", "Next-Gen Engineering", "Palo Alto Networks"]
    },
    {
        "id": "aij-nomination",
        "title": "Principal AI Engineer Harsh Verma Nominated for Tech Excellence Award at Influencer Magazine Awards 2026",
        "platform": "The AI Journal",
        "platform_full": "The AI Journal",
        "platform_badge": "Award Recognition",
        "platform_icon": "mdi-trophy-award",
        "platform_color": "#2563eb",
        "category": "Industry Recognition",
        "url": "https://aijourn.com/principal-ai-engineer-harsh-verma-nominated-for-tech-excellence-award-at-influencer-magazine-awards-2026-as-his-work-on-human-ai-collaboration-gains-enterprise-attention/",
        "author_profile": "https://aijourn.com/",
        "thumbnail": "images/blog/thumbnails/aij-nomination.jpg",
        "date": "June 2026",
        "read_time": "4 min read",
        "featured": False,
        "description": "Coverage of Harsh Verma's nomination for Tech Excellence Award 2026, highlighting his research and architectural leadership in agentic trust models and enterprise human-AI collaboration.",
        "tags": ["The AI Journal", "Award Nomination", "Tech Excellence", "Industry Leader", "Recognition"]
    },
    {
        "id": "aij-intern-agent",
        "title": "Your First AI Agent Is Your New Intern: Here’s How to Manage It",
        "platform": "The AI Journal",
        "platform_full": "The AI Journal",
        "platform_badge": "AI Journal",
        "platform_icon": "mdi-account-star",
        "platform_color": "#2563eb",
        "category": "Management & Strategy",
        "url": "https://aijourn.com/your-first-ai-agent-is-your-new-intern-heres-how-to-manage-it/",
        "author_profile": "https://aijourn.com/",
        "thumbnail": "images/blog/thumbnails/aij-intern-agent.png",
        "date": "June 2026",
        "read_time": "5 min read",
        "featured": False,
        "description": "A grounded leadership guide for managing AI agents: establishing bounded roles, implementing stage-gated code reviews, and avoiding delegation traps in engineering organizations.",
        "tags": ["The AI Journal", "Agent Management", "Leadership", "Mental Models", "Delegation"]
    },
    {
        "id": "aij-future-cto",
        "title": "Designing the Intelligence Layer: Why Future Tech Leaders Must Be AI Architects First",
        "platform": "The AI Journal",
        "platform_full": "The AI Journal",
        "platform_badge": "AI Journal",
        "platform_icon": "mdi-domain",
        "platform_color": "#2563eb",
        "category": "Executive Leadership",
        "url": "https://aijourn.com/designing-the-intelligence-layer-why-future-tech-leaders-must-be-ai-architects-first/",
        "author_profile": "https://aijourn.com/",
        "thumbnail": "images/blog/thumbnails/aij-future-cto.png",
        "date": "August 2026",
        "read_time": "6 min read",
        "featured": True,
        "description": "Why the modern CTO and VP of Engineering must evolve from managing cloud infrastructure to engineering the cognitive orchestration layer that powers all enterprise workflows.",
        "tags": ["The AI Journal", "CTO Architecture", "Intelligence Layer", "Executive Leadership", "AI Strategy"]
    },

    # --- Founders Creative & Substack ---
    {
        "id": "fc-co-innovation",
        "title": "Unlocking Corporate–Startup Co-Innovation with AI",
        "platform": "Founders Creative",
        "platform_full": "Founders Creative & Substack",
        "platform_badge": "Founders Creative",
        "platform_icon": "mdi-lightbulb-on-outline",
        "platform_color": "#ff6600",
        "category": "Venture & Innovation",
        "url": "https://www.founderscreative.org/unlocking-corporate-startup-co-innovation-with-ai/",
        "author_profile": "https://www.founderscreative.org/author/harsh/",
        "substack_url": "https://founderscreative.substack.com/p/unlocking-corporatestartup-co-innovation",
        "thumbnail": "images/blog/thumbnails/fc-co-innovation.png",
        "date": "2026",
        "read_time": "5 min read",
        "featured": True,
        "description": "How enterprise corporations and agile venture-backed AI startups can build collaborative co-innovation loops, de-risking pilot integrations and unlocking rapid enterprise market validation.",
        "tags": ["Founders Creative", "Substack", "Corporate Innovation", "Startups", "Venture Capital"]
    },

    # --- Engineering & Career Archives ---
    {
        "id": "medium-helm-gke",
        "title": "Helm with YugabyteDB: Google Kubernetes Engine (GKE) Distributed Deployment",
        "platform": "Medium",
        "platform_full": "Medium Engineering",
        "platform_badge": "Technical Guide",
        "platform_icon": "mdi-kubernetes",
        "platform_color": "#12b886",
        "category": "Cloud Infrastructure",
        "url": "https://medium.com/@harshverma59/helm-with-yugabytedb-gke-google-kubernetes-engine-9099b62548cd",
        "author_profile": "https://medium.com/@harshverma59",
        "thumbnail": "images/blog/helm_blog.jpg",
        "date": "Cloud Engineering",
        "read_time": "8 min read",
        "featured": False,
        "description": "A comprehensive practical guide to managing distributed cloud-native relational databases on Google Kubernetes Engine (GKE) using Helm package management.",
        "tags": ["Medium", "Kubernetes", "GKE", "YugabyteDB", "Distributed SQL"]
    },
    {
        "id": "lifepage-interview",
        "title": "Software Architecture, Engineering Process & Career Insights with LifePage",
        "platform": "LifePage",
        "platform_full": "LifePage Career Talks",
        "platform_badge": "Career Talk",
        "platform_icon": "mdi-school-outline",
        "platform_color": "#e11d48",
        "category": "Interviews",
        "url": "https://www.lifepage.in/page/harsh",
        "author_profile": "https://www.lifepage.in/page/harsh",
        "thumbnail": "images/blog/LifePage.png",
        "date": "Career Talk",
        "read_time": "10 min read",
        "featured": False,
        "description": "Comprehensive interview detailing software development lifecycles, navigating real-world architectural trade-offs, and career roadmap guidance for aspiring software engineers.",
        "tags": ["LifePage", "Career Guidance", "Software Development", "Mentorship"]
    }
]

def generate_blog_html():
    total_articles = len(articles_data)

    # Core Research Domain Mapping (Category Filter)
    MAIN_CATEGORY_MAP = {
        # Forbes (6)
        "forbes-real-ai-moat": "AI Research",
        "forbes-beyond-code": "Engineering",
        "forbes-intelligence-dollar": "AI Research",
        "forbes-personalized-ai": "Cybersecurity",
        "forbes-first-agent-experiment": "AI Research",
        "forbes-pure-determinism": "Engineering",
        # HackerNoon (12)
        "hn-production-gap": "Interviews",
        "hn-identity-perimeter": "Cybersecurity",
        "hn-clean-attack": "Cybersecurity",
        "hn-speed-reliability": "AI Research",
        "hn-ai-governance": "AI Research",
        "hn-observability-crisis": "AI Research",
        "hn-reputation-systems": "AI Research",
        "hn-distributed-intelligence": "Engineering",
        "hn-identity-intent": "Cybersecurity",
        "hn-trust-scores": "Cybersecurity",
        "hn-ai-orchestrator": "Engineering",
        "hn-startup-autonomy": "AI Research",
        # RSA Conference (3)
        "rsac-clean-attack": "Cybersecurity",
        "rsac-death-auth": "Cybersecurity",
        "rsac-agents-rules": "Cybersecurity",
        # The AI Journal (6)
        "aij-agentic-framework": "AI Research",
        "aij-high-stakes": "AI Research",
        "aij-beyond-code": "Interviews",
        "aij-nomination": "Interviews",
        "aij-intern-agent": "AI Research",
        "aij-future-cto": "Engineering",
        # Founders Creative (1)
        "fc-co-innovation": "Engineering",
        # Medium (1)
        "medium-helm-gke": "Engineering",
        # LifePage (1)
        "lifepage-interview": "Interviews"
    }

    for art in articles_data:
        art['main_category'] = MAIN_CATEGORY_MAP.get(art['id'], 'AI Research')

    # Category counts
    ai_count = sum(1 for a in articles_data if a['main_category'] == 'AI Research')
    cyber_count = sum(1 for a in articles_data if a['main_category'] == 'Cybersecurity')
    eng_count = sum(1 for a in articles_data if a['main_category'] == 'Engineering')
    interview_count = sum(1 for a in articles_data if a['main_category'] == 'Interviews')

    categories_summary = [
        {"name": "All Categories", "filter": "all", "count": total_articles, "icon": "mdi-view-grid-outline"},
        {"name": "AI Research", "filter": "AI Research", "count": ai_count, "icon": "mdi-brain"},
        {"name": "Cybersecurity", "filter": "Cybersecurity", "count": cyber_count, "icon": "mdi-shield-lock-outline"},
        {"name": "Engineering", "filter": "Engineering", "count": eng_count, "icon": "mdi-cog-sync"},
        {"name": "Interviews & Spotlights", "filter": "Interviews", "count": interview_count, "icon": "mdi-microphone-variant"}
    ]

    forbes_count = sum(1 for a in articles_data if a['platform'] == 'Forbes')
    hn_count = sum(1 for a in articles_data if a['platform'] == 'HackerNoon')
    aij_count = sum(1 for a in articles_data if a['platform'] == 'The AI Journal')
    rsac_count = sum(1 for a in articles_data if a['platform'] == 'RSA Conference')
    fc_count = sum(1 for a in articles_data if a['platform'] == 'Founders Creative')
    audio_count = sum(1 for a in articles_data if a.get('has_audio') or a.get('category') == 'Interviews')

    # Platform pills HTML
    platforms_summary = [
        {"name": "All Platforms", "filter": "all", "count": total_articles, "icon": "mdi-newspaper-variant-multiple"},
        {"name": "Forbes Tech Council", "filter": "Forbes", "count": forbes_count, "icon": "mdi-shield-star"},
        {"name": "HackerNoon", "filter": "HackerNoon", "count": hn_count, "icon": "mdi-code-braces"},
        {"name": "The AI Journal", "filter": "The AI Journal", "count": aij_count, "icon": "mdi-newspaper-variant"},
        {"name": "RSA Conference", "filter": "RSA Conference", "count": rsac_count, "icon": "mdi-shield-check"},
        {"name": "Founders Creative", "filter": "Founders Creative", "count": fc_count, "icon": "mdi-lightbulb-on-outline"},
        {"name": "Interviews & Media", "filter": "Interviews", "count": audio_count, "icon": "mdi-microphone-variant"}
    ]

    cards_html = []
    for art in articles_data:
        platform_class = f"platform-{art['platform'].lower().replace(' ', '-')}"
        category_class = f"cat-{art['category'].lower().replace(' ', '-').replace('&', 'and')}"
        tags_str = " ".join([f"tag-{t.lower().replace(' ', '-')}" for t in art['tags']])
        search_terms = f"{art['title']} {art['description']} {art['platform']} {art['platform_full']} {art['main_category']} {art['category']} {' '.join(art['tags'])}".lower()

        # Category topic badge styling
        main_cat = art['main_category']
        if main_cat == 'AI Research':
            topic_icon = 'mdi-brain'
            topic_badge_class = 'topic-ai'
        elif main_cat == 'Cybersecurity':
            topic_icon = 'mdi-shield-lock-outline'
            topic_badge_class = 'topic-cyber'
        elif main_cat == 'Engineering':
            topic_icon = 'mdi-cog-sync'
            topic_badge_class = 'topic-eng'
        else:
            topic_icon = 'mdi-microphone-variant'
            topic_badge_class = 'topic-interview'

        # Platform badge color styling
        badge_style = ""
        if art['platform'] == 'Forbes':
            badge_class = "badge-forbes"
        elif art['platform'] == 'HackerNoon':
            badge_class = "badge-hackernoon"
        elif art['platform'] == 'The AI Journal':
            badge_class = "badge-aijournal"
        elif art['platform'] == 'RSA Conference':
            badge_class = "badge-rsac"
        elif art['platform'] == 'Founders Creative':
            badge_class = "badge-founderscreative"
        else:
            badge_class = "badge-secondary"

        # Tag pills
        tags_html = "".join([f'<span class="badge badge-light-custom mr-1 mb-1" onclick="filterByTag(\'{t}\')">#{t}</span>' for t in art['tags'][:3]])

        # Extra audio badge or interview badge
        extra_badges = ""
        if art.get('has_audio') and art.get('spotify_url'):
            extra_badges += f'''
            <a href="{art['spotify_url']}" target="_blank" class="badge badge-spotify ml-1" title="Listen on Spotify">
                <i class="mdi mdi-spotify mr-1"></i>Spotify Podcast
            </a>
            '''
        if art.get('substack_url'):
            extra_badges += f'''
            <a href="{art['substack_url']}" target="_blank" class="badge badge-substack ml-1" title="Read on Substack">
                <i class="mdi mdi-email-newsletter mr-1"></i>Substack
            </a>
            '''

        card_html = f'''
        <div class="col-lg-4 col-md-6 mb-4 pb-2 blog-card-item" 
             data-platform="{art['platform']}" 
             data-category="{art['category']}" 
             data-main-category="{art['main_category']}"
             data-featured="{'true' if art.get('featured') else 'false'}"
             data-search="{search_terms}">
            <div class="blog-card rounded shadow-sm h-100 d-flex flex-column">
                <div class="position-relative overflow-hidden blog-thumbnail-wrap">
                    <img src="{art['thumbnail']}" class="img-fluid w-100 blog-img" alt="{art['title']}" loading="lazy" onerror="this.onerror=null;this.src='images/blog/01.jpg';">
                    <div class="blog-platform-badge {badge_class}">
                        <i class="mdi {art['platform_icon']} mr-1"></i>{art['platform_badge']}
                    </div>
                    {f'<div class="blog-featured-ribbon"><i class="mdi mdi-star"></i> Featured</div>' if art.get('featured') else ''}
                </div>
                <div class="content p-3 p-lg-4 d-flex flex-column flex-grow-1">
                    <div class="d-flex align-items-center justify-content-between text-muted small mb-2">
                        <span class="badge badge-topic-pill {topic_badge_class}" onclick="filterByCategory('{main_cat}')" title="Filter by category: {main_cat}" style="cursor: pointer;">
                            <i class="mdi {topic_icon} mr-1"></i>{main_cat}
                        </span>
                        <div class="d-flex align-items-center text-muted">
                            <span class="d-flex align-items-center font-weight-medium mr-2">
                                <i class="mdi mdi-calendar-blank-outline mr-1"></i>{art['date']}
                            </span>
                            <span class="d-flex align-items-center">
                                <i class="mdi mdi-clock-outline mr-1"></i>{art['read_time']}
                            </span>
                        </div>
                    </div>
                    <h5 class="card-title mb-2">
                        <a href="{art['url']}" target="_blank" class="title text-dark font-weight-bold" title="{art['title']}">
                            {art['title']}
                        </a>
                    </h5>
                    <p class="text-muted small mb-3 flex-grow-1 blog-desc">
                        {art['description']}
                    </p>
                    <div class="blog-tags mb-3">
                        {tags_html}
                        {extra_badges}
                    </div>
                    <div class="post-meta pt-2 border-top d-flex align-items-center justify-content-between mt-auto">
                        <a href="{art.get('author_profile', art['url'])}" target="_blank" class="text-muted small font-weight-medium" title="View Author Profile on {art['platform']}">
                            <i class="mdi {art['platform_icon']} mr-1 text-primary"></i>{art['platform_full']}
                        </a>
                        <a href="{art['url']}" target="_blank" class="btn btn-sm btn-outline-primary rounded-pill font-weight-bold px-3 py-1">
                            Read Article <i class="mdi mdi-arrow-top-right ml-1"></i>
                        </a>
                    </div>
                </div>
            </div>
        </div>
        '''
        cards_html.append(card_html)

    cards_joined = "\n".join(cards_html)

    # Category chips HTML
    category_chips_html = []
    for c in categories_summary:
        active_class = "active" if c['filter'] == 'all' else ""
        category_chips_html.append(f'''
        <button type="button" class="btn btn-category-pill {active_class} mr-2 mb-2" data-category-filter="{c['filter']}">
            <i class="mdi {c['icon']} mr-1"></i>{c['name']} 
            <span class="badge badge-pill badge-dark ml-1">{c['count']}</span>
        </button>
        ''')
    category_chips_joined = "".join(category_chips_html)

    # Platform secondary filter chips HTML
    platform_chips_html = []
    for p in platforms_summary:
        active_class = "active" if p['filter'] == 'all' else ""
        platform_chips_html.append(f'''
        <button type="button" class="btn btn-sm btn-platform-chip {active_class} mr-1 mb-2" data-platform-filter="{p['filter']}">
            {p['name']} <span class="badge badge-pill badge-light ml-1">{p['count']}</span>
        </button>
        ''')
    platform_chips_joined = "".join(platform_chips_html)

    html_content = f'''<!DOCTYPE html>
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
    <title>Harsh Verma | Thought Leadership, Forbes Council & Tech Publications</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Explore published articles, technical research, and thought leadership by Harsh Verma across Forbes Technology Council, HackerNoon, RSA Conference, The AI Journal, and Founders Creative." />
    <meta name="keywords" content="Harsh Verma, Forbes Technology Council, HackerNoon, RSA Conference, The AI Journal, Agentic AI, AI Architecture, Cybersecurity, Zero Trust, Tech Publications" />
    <meta content="Harsh Verma" name="author" />
    <meta property="og:title" content="Harsh Verma | Thought Leadership, Forbes Council & Tech Publications" />
    <meta property="og:description" content="Explore published articles, technical research, and thought leadership by Harsh Verma across Forbes Technology Council, HackerNoon, RSA Conference, The AI Journal, and Founders Creative." />
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
    <!-- RSS Feed Discovery -->
    <link rel="alternate" type="application/rss+xml" title="Harsh Verma - Tech Articles &amp; AI Engineering RSS Feed" href="rss.xml" />
    <!-- Blog Newsletter Subscription Modal Styles -->
    <link href="css/hv-blog-newsletter.css" rel="stylesheet" type="text/css" />
    <!-- HV AI Copilot Styles -->
    <link rel="stylesheet" href="css/hv-copilot.css" />
    
    <style>
        /* Modern Blog Page Styles */
        .blog-card {{
            background: #ffffff;
            border: 1px solid rgba(0, 0, 0, 0.08);
            transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        }}
        .blog-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 16px 32px rgba(0, 0, 0, 0.09) !important;
            border-color: rgba(79, 70, 229, 0.3);
        }}
        .blog-thumbnail-wrap {{
            height: 200px;
            background-color: #f1f5f9;
        }}
        .blog-img {{
            height: 100%;
            object-fit: cover;
            transition: transform 0.4s ease;
        }}
        .blog-card:hover .blog-img {{
            transform: scale(1.04);
        }}
        .blog-platform-badge {{
            position: absolute;
            top: 12px;
            left: 12px;
            padding: 4px 10px;
            font-size: 11px;
            font-weight: 700;
            border-radius: 20px;
            letter-spacing: 0.3px;
            text-transform: uppercase;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
            z-index: 2;
        }}
        .badge-forbes {{
            background: #111827;
            color: #ffffff;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }}
        .badge-hackernoon {{
            background: #003b17;
            color: #00ea62;
            border: 1px solid #00ea62;
        }}
        .badge-aijournal {{
            background: #1e3a8a;
            color: #93c5fd;
            border: 1px solid rgba(147, 197, 253, 0.3);
        }}
        .badge-rsac {{
            background: #7f1d1d;
            color: #fecaca;
            border: 1px solid rgba(254, 202, 202, 0.3);
        }}
        .badge-founderscreative {{
            background: #7c2d12;
            color: #ffedd5;
            border: 1px solid rgba(255, 237, 213, 0.3);
        }}
        .blog-featured-ribbon {{
            position: absolute;
            top: 12px;
            right: 12px;
            background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
            color: #ffffff;
            padding: 3px 8px;
            font-size: 10px;
            font-weight: 800;
            border-radius: 12px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            z-index: 2;
            box-shadow: 0 2px 6px rgba(217, 119, 6, 0.4);
        }}
        .card-title {{
            font-size: 17px;
            line-height: 1.4;
        }}
        .card-title a {{
            color: #1e293b;
            text-decoration: none;
            transition: color 0.2s;
        }}
        .card-title a:hover {{
            color: #4f46e5 !important;
        }}
        .blog-desc {{
            display: -webkit-box;
            -webkit-line-clamp: 3;
            -webkit-box-orient: vertical;
            overflow: hidden;
            line-height: 1.55;
            color: #64748b !important;
        }}
        .badge-light-custom {{
            background: #f1f5f9;
            color: #475569;
            font-weight: 600;
            font-size: 11px;
            padding: 4px 8px;
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.15s;
        }}
        .badge-light-custom:hover {{
            background: #e2e8f0;
            color: #1e293b;
        }}
        .badge-spotify {{
            background: #1db954;
            color: #000000;
            font-weight: 700;
            font-size: 11px;
            padding: 4px 8px;
            border-radius: 6px;
            text-decoration: none !important;
        }}
        .badge-substack {{
            background: #ff6600;
            color: #ffffff;
            font-weight: 700;
            font-size: 11px;
            padding: 4px 8px;
            border-radius: 6px;
            text-decoration: none !important;
        }}
        /* Category and Platform Filter Styling */
        .category-filter-card {{
            background: #ffffff;
            border: 1px solid rgba(0, 0, 0, 0.08);
            border-radius: 18px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
        }}
        .btn-category-pill {{
            background: #ffffff;
            color: #334155;
            border: 1.5px solid #e2e8f0;
            border-radius: 30px;
            font-size: 13.5px;
            font-weight: 600;
            padding: 8px 18px;
            transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
            display: inline-flex;
            align-items: center;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03);
        }}
        .btn-category-pill:hover {{
            background: #f8fafc;
            color: #1e1b4b;
            border-color: #94a3b8;
            transform: translateY(-1px);
        }}
        .btn-category-pill.active {{
            background: linear-gradient(135deg, #2563eb 0%, #4f46e5 100%) !important;
            color: #ffffff !important;
            border-color: #2563eb !important;
            box-shadow: 0 4px 14px rgba(37, 99, 235, 0.35);
        }}
        .btn-category-pill .badge {{
            background: rgba(0, 0, 0, 0.08);
            color: inherit;
            font-weight: 700;
            font-size: 11px;
            padding: 3px 8px;
        }}
        .btn-category-pill.active .badge {{
            background: rgba(255, 255, 255, 0.28);
            color: #ffffff;
        }}
        .btn-platform-chip {{
            background: #f1f5f9;
            color: #475569;
            border: 1px solid #cbd5e1;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
            padding: 4px 12px;
            transition: all 0.2s ease;
        }}
        .btn-platform-chip:hover {{
            background: #e2e8f0;
            color: #0f172a;
        }}
        .btn-platform-chip.active {{
            background: #0f172a !important;
            color: #ffffff !important;
            border-color: #0f172a !important;
        }}
        .btn-platform-chip .badge {{
            background: rgba(0, 0, 0, 0.1);
            color: inherit;
            font-size: 10px;
            padding: 2px 6px;
        }}
        .btn-platform-chip.active .badge {{
            background: rgba(255, 255, 255, 0.25);
            color: #ffffff;
        }}

        /* Category Topic Badges on Cards */
        .badge-topic-pill {{
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 0.3px;
            padding: 4px 10px;
            border-radius: 12px;
            display: inline-flex;
            align-items: center;
            transition: all 0.2s ease;
        }}
        .badge-topic-pill:hover {{
            transform: scale(1.04);
        }}
        .badge-topic-pill.topic-ai {{
            background: rgba(99, 102, 241, 0.12);
            color: #4f46e5;
            border: 1px solid rgba(99, 102, 241, 0.3);
        }}
        .badge-topic-pill.topic-cyber {{
            background: rgba(225, 29, 72, 0.12);
            color: #e11d48;
            border: 1px solid rgba(225, 29, 72, 0.3);
        }}
        .badge-topic-pill.topic-eng {{
            background: rgba(14, 165, 233, 0.12);
            color: #0284c7;
            border: 1px solid rgba(14, 165, 233, 0.3);
        }}
        .badge-topic-pill.topic-interview {{
            background: rgba(16, 185, 129, 0.12);
            color: #059669;
            border: 1px solid rgba(16, 185, 129, 0.3);
        }}
        .search-box-wrap {{
            position: relative;
            max-width: 520px;
        }}
        .search-box-wrap input {{
            height: 48px;
            padding-left: 44px;
            padding-right: 40px;
            border-radius: 24px;
            border: 1px solid #cbd5e1;
            font-size: 14px;
            transition: all 0.2s ease;
        }}
        .search-box-wrap input:focus {{
            border-color: #4f46e5;
            box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.15);
            outline: none;
        }}
        .search-icon-pos {{
            position: absolute;
            left: 16px;
            top: 50%;
            transform: translateY(-50%);
            color: #94a3b8;
            font-size: 20px;
            pointer-events: none;
        }}
        .search-clear-btn {{
            position: absolute;
            right: 14px;
            top: 50%;
            transform: translateY(-50%);
            background: none;
            border: none;
            color: #94a3b8;
            font-size: 18px;
            cursor: pointer;
            display: none;
            padding: 0;
        }}
        .search-clear-btn:hover {{
            color: #475569;
        }}
        .author-channel-card {{
            background: #ffffff;
            border: 1px solid rgba(0, 0, 0, 0.08);
            border-radius: 12px;
            padding: 16px 20px;
            transition: all 0.2s ease;
            text-decoration: none !important;
            display: flex;
            align-items: center;
        }}
        .author-channel-card:hover {{
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.06);
            border-color: rgba(79, 70, 229, 0.3);
        }}

        /* Dark Mode Adjustments */
        body.dark-mode .blog-card {{
            background: #1e293b;
            border-color: rgba(255, 255, 255, 0.08);
        }}
        body.dark-mode .blog-card:hover {{
            border-color: rgba(99, 102, 241, 0.5);
            box-shadow: 0 16px 32px rgba(0, 0, 0, 0.4) !important;
        }}
        body.dark-mode .card-title a {{
            color: #f1f5f9;
        }}
        body.dark-mode .card-title a:hover {{
            color: #818cf8 !important;
        }}
        body.dark-mode .blog-desc {{
            color: #94a3b8 !important;
        }}
        body.dark-mode .badge-light-custom {{
            background: #334155;
            color: #cbd5e1;
        }}
        body.dark-mode .badge-light-custom:hover {{
            background: #475569;
            color: #ffffff;
        }}
        body.dark-mode .category-filter-card {{
            background: #1e293b;
            border-color: rgba(255, 255, 255, 0.08);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        }}
        body.dark-mode .btn-category-pill {{
            background: #1e293b;
            color: #cbd5e1;
            border-color: #334155;
        }}
        body.dark-mode .btn-category-pill:hover {{
            background: #334155;
            color: #ffffff;
            border-color: #475569;
        }}
        body.dark-mode .btn-category-pill.active {{
            background: linear-gradient(135deg, #3b82f6 0%, #6366f1 100%) !important;
            border-color: #3b82f6 !important;
            color: #ffffff !important;
            box-shadow: 0 4px 14px rgba(59, 130, 246, 0.4);
        }}
        body.dark-mode .btn-platform-chip {{
            background: #0f172a;
            color: #94a3b8;
            border-color: #334155;
        }}
        body.dark-mode .btn-platform-chip:hover {{
            background: #1e293b;
            color: #f1f5f9;
        }}
        body.dark-mode .btn-platform-chip.active {{
            background: #38bdf8 !important;
            color: #0f172a !important;
            border-color: #38bdf8 !important;
        }}
        body.dark-mode .btn-platform-chip.active .badge {{
            background: rgba(15, 23, 42, 0.3);
            color: #0f172a;
        }}
        body.dark-mode .badge-topic-pill.topic-ai {{
            background: rgba(99, 102, 241, 0.22);
            color: #a5b4fc;
            border-color: rgba(99, 102, 241, 0.45);
        }}
        body.dark-mode .badge-topic-pill.topic-cyber {{
            background: rgba(225, 29, 72, 0.22);
            color: #fda4af;
            border-color: rgba(225, 29, 72, 0.45);
        }}
        body.dark-mode .badge-topic-pill.topic-eng {{
            background: rgba(14, 165, 233, 0.22);
            color: #7dd3fc;
            border-color: rgba(14, 165, 233, 0.45);
        }}
        body.dark-mode .badge-topic-pill.topic-interview {{
            background: rgba(16, 185, 129, 0.22);
            color: #6ee7b7;
            border-color: rgba(16, 185, 129, 0.45);
        }}
        body.dark-mode .search-box-wrap input {{
            background: #1e293b;
            color: #f1f5f9;
            border-color: #334155;
        }}
        body.dark-mode .search-box-wrap input:focus {{
            border-color: #6366f1;
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2);
        }}
        body.dark-mode .author-channel-card {{
            background: #1e293b;
            border-color: rgba(255, 255, 255, 0.08);
        }}
        body.dark-mode .author-channel-card:hover {{
            background: #24334a;
            border-color: rgba(99, 102, 241, 0.4);
        }}
        body.dark-mode .author-channel-card h6 {{
            color: #f1f5f9 !important;
        }}
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
                    <li class="nav-item">
                        <a class="nav-link" href="page-events">Speaker</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="page-books">Books</a>
                    </li>
                    <li class="nav-item active">
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
    <!-- Navbar End -->

    <!-- Hero Start -->
    <section class="bg-half bg-light d-table w-100" style="background: url('images/home/hero-bg4_new.jpg') center center; background-size: cover;">
        <div class="bg-overlay" style="background: rgba(15, 23, 42, 0.85);"></div>
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-12 text-center">
                    <div class="page-next-level">
                        <div class="d-inline-flex align-items-center px-3 py-1 rounded-pill mb-3" style="background: rgba(99, 102, 241, 0.2); border: 1px solid rgba(99, 102, 241, 0.4); color: #c7d2fe; font-size: 13px; font-weight: 600;">
                            <i class="mdi mdi-feather mr-1"></i> Thought Leadership &bull; Technical Architecture &bull; AI Security
                        </div>
                        <h1 class="title text-white font-weight-bold mb-3" style="font-size: 38px; letter-spacing: -0.5px;">Articles &amp; Thought Leadership</h1>
                        <p class="text-white-50 mx-auto mb-4" style="max-width: 720px; font-size: 16px; line-height: 1.6;">
                            Explorations in agentic systems architecture, zero-trust AI security, determinism, multi-agent orchestration, and enterprise technology strategy published across global platforms.
                        </p>
                        <div class="page-next">
                            <nav aria-label="breadcrumb" class="d-inline-block">
                                <ul class="breadcrumb rounded mb-0 mt-2" style="background: rgba(255, 255, 255, 0.1);">
                                    <li class="breadcrumb-item"><a href="index" class="text-white">Home</a></li>
                                    <li class="breadcrumb-item active text-primary font-weight-bold" aria-current="page">Blog &amp; Articles</li>
                                </ul>
                            </nav>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- Hero End -->

    <!-- Verified Contributor Profiles Hub -->
    <section class="py-4 border-bottom" style="background: rgba(248, 250, 252, 0.8);">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-2 col-md-3 mb-3 mb-md-0">
                    <span class="text-uppercase small font-weight-bold text-muted" style="letter-spacing: 0.5px;">Verified Columnist:</span>
                </div>
                <div class="col-lg-10 col-md-9">
                    <div class="row no-gutters">
                        <div class="col-6 col-md-3 p-1">
                            <a href="https://www.forbes.com/councils/forbestechcouncil/people/harshverma/" target="_blank" class="author-channel-card shadow-sm h-100">
                                <i class="mdi mdi-shield-star text-dark mr-2" style="font-size: 22px;"></i>
                                <div class="text-truncate">
                                    <div class="font-weight-bold text-dark small">Forbes Council</div>
                                    <div class="text-muted" style="font-size: 11px;">Author Profile &rarr;</div>
                                </div>
                            </a>
                        </div>
                        <div class="col-6 col-md-3 p-1">
                            <a href="https://hackernoon.com/u/harshverma59" target="_blank" class="author-channel-card shadow-sm h-100">
                                <i class="mdi mdi-code-braces mr-2" style="color: #00ea62; font-size: 22px;"></i>
                                <div class="text-truncate">
                                    <div class="font-weight-bold text-dark small">HackerNoon</div>
                                    <div class="text-muted" style="font-size: 11px;">@harshverma59 &rarr;</div>
                                </div>
                            </a>
                        </div>
                        <div class="col-6 col-md-3 p-1">
                            <a href="https://www.rsaconference.com/experts/Harsh%20Verma" target="_blank" class="author-channel-card shadow-sm h-100">
                                <i class="mdi mdi-shield-check text-danger mr-2" style="font-size: 22px;"></i>
                                <div class="text-truncate">
                                    <div class="font-weight-bold text-dark small">RSA Conference</div>
                                    <div class="text-muted" style="font-size: 11px;">RSAC Expert &rarr;</div>
                                </div>
                            </a>
                        </div>
                        <div class="col-6 col-md-3 p-1">
                            <a href="https://open.spotify.com/episode/0aDrp6DxLSSlWQ6gwfbi0l" target="_blank" class="author-channel-card shadow-sm h-100">
                                <i class="mdi mdi-spotify text-success mr-2" style="font-size: 22px;"></i>
                                <div class="text-truncate">
                                    <div class="font-weight-bold text-dark small">Spotify Podcast</div>
                                    <div class="text-muted" style="font-size: 11px;">Tech Brief Audio &rarr;</div>
                                </div>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Main Content Section -->
    <section class="section py-5">
        <div class="container">
            <!-- Search & Filter Controls -->
            <div class="row justify-content-between align-items-center mb-4 pb-2">
                <div class="col-lg-6 col-md-7 mb-3 mb-md-0">
                    <div class="search-box-wrap">
                        <i class="mdi mdi-magnify search-icon-pos"></i>
                        <input type="text" id="blogSearchInput" class="form-control" placeholder="Search by topic, keyword (e.g. Agentic AI, Zero Trust, Forbes, Governance)..." autocomplete="off">
                        <button type="button" id="blogSearchClear" class="search-clear-btn" title="Clear search">
                            <i class="mdi mdi-close-circle"></i>
                        </button>
                    </div>
                </div>
                <div class="col-lg-6 col-md-5 d-flex justify-content-md-end align-items-center">
                    <span id="resultsCountBadge" class="text-muted small mr-3 font-weight-medium">Showing all {total_articles} publications</span>
                    <div class="dropdown">
                        <button class="btn btn-sm btn-outline-secondary dropdown-toggle rounded-pill px-3 py-1 font-weight-medium" type="button" id="sortDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            <i class="mdi mdi-sort mr-1"></i>Sort By
                        </button>
                        <div class="dropdown-menu dropdown-menu-right" aria-labelledby="sortDropdown">
                            <a class="dropdown-item active" href="javascript:void(0)" onclick="sortArticles('featured')">Featured First</a>
                            <a class="dropdown-item" href="javascript:void(0)" onclick="sortArticles('title')">Alphabetical Title</a>
                            <a class="dropdown-item" href="javascript:void(0)" onclick="sortArticles('platform')">By Publication</a>
                        </div>
                    </div>
                </div>
            </div>



            <!-- Articles Grid -->
            <div class="row" id="blogArticlesGrid">
                {cards_joined}
            </div>

            <!-- No Results Message (Hidden by default) -->
            <div id="noResultsBox" class="col-12 text-center py-5" style="display: none;">
                <div class="p-5 rounded border bg-light-custom mx-auto" style="max-width: 500px;">
                    <i class="mdi mdi-text-box-search-outline text-muted" style="font-size: 54px;"></i>
                    <h5 class="mt-3 font-weight-bold text-dark">No Articles Found</h5>
                    <p class="text-muted small">We couldn't find any articles matching your query. Try a different keyword or reset filters.</p>
                    <button type="button" class="btn btn-primary btn-sm rounded-pill px-4" onclick="resetFilters()">
                        <i class="mdi mdi-refresh mr-1"></i>Reset All Filters
                    </button>
                </div>
            </div>

            <!-- Bottom Callout -->
            <div class="row mt-5 pt-4">
                <div class="col-12">
                    <div class="p-4 p-md-5 rounded shadow-sm" style="background: linear-gradient(135deg, #1e1b4b 0%, #312e81 100%); color: #ffffff;">
                        <div class="row align-items-center">
                            <div class="col-lg-8 mb-3 mb-lg-0">
                                <h4 class="font-weight-bold text-white mb-2">Want to Collaborate or Feature an Article?</h4>
                                <p class="text-white-50 mb-0">
                                    Harsh Verma frequently authors in-depth architectural whitepapers, keynotes, and guest technical columns exploring the frontiers of agentic AI and enterprise cybersecurity.
                                </p>
                            </div>
                            <div class="col-lg-4 text-lg-right">
                                <a href="index#contact" class="btn btn-light rounded-pill font-weight-bold px-4 py-2 mr-2">
                                    <i class="mdi mdi-email-outline mr-1"></i>Get In Touch
                                </a>
                                <a href="https://www.linkedin.com/in/harshverma59/" target="_blank" class="btn btn-outline-light rounded-pill font-weight-bold px-3 py-2">
                                    <i class="mdi mdi-linkedin mr-1"></i>Connect
                                </a>
                            </div>
                        </div>
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

                    <!-- Footer Newsletter Subscription Input & RSS Feed Button -->
                    <div class="footer-subscribe-wrapper my-4">
                        <div class="row justify-content-center">
                            <div class="col-lg-8 col-md-10 col-12">
                                <div class="footer-subscribe-card">
                                    <span class="badge badge-pill badge-primary-soft text-primary font-weight-bold px-3 py-1 mb-2">
                                        <i class="mdi mdi-email-newsletter mr-1"></i> Executive Tech Dispatch
                                    </span>
                                    <h5 class="footer-subscribe-title font-weight-bold mb-1">
                                        Subscribe to Technical Articles &amp; AI Briefings
                                    </h5>
                                    <p class="footer-subscribe-desc text-muted small mb-3">
                                        Join 3,240+ technology executives and engineers. Subscribe via email or follow directly via RSS readers.
                                    </p>
                                    <form class="footer-newsletter-form" id="footerNewsletterForm" onsubmit="return handleFooterNewsletterSubmit(event)">
                                        <div class="footer-form-row d-flex flex-column flex-sm-row align-items-stretch justify-content-center">
                                            <div class="footer-input-wrap flex-grow-1 position-relative mr-sm-2 mb-2 mb-sm-0">
                                                <i class="mdi mdi-email-outline footer-input-icon"></i>
                                                <input type="email" class="form-control footer-email-input" id="footerNewsletterEmail" placeholder="Enter your business email address..." required autocomplete="email" aria-label="Enter email to subscribe to tech articles">
                                            </div>
                                            <button type="submit" class="btn btn-primary footer-subscribe-btn px-4 mb-2 mb-sm-0 mr-sm-2 font-weight-medium text-nowrap" id="footerSubscribeBtn">
                                                <span class="btn-text"><i class="mdi mdi-send mr-1"></i> Subscribe</span>
                                                <span class="btn-spinner d-none"><i class="mdi mdi-loading mdi-spin mr-1"></i> Subscribing...</span>
                                            </button>
                                            <a href="rss.xml" class="btn footer-rss-btn px-3 mb-2 mb-sm-0 font-weight-medium text-nowrap" id="footerRssBtn" title="Follow tech articles via RSS Feed (Feedly, Inoreader, RSS readers)" target="_blank" rel="noopener noreferrer" onclick="handleFooterRssClick(event)">
                                                <i class="mdi mdi-rss mr-1 rss-icon"></i> <span class="rss-text">RSS Feed</span>
                                            </a>
                                        </div>
                                        <div id="footerNewsletterFeedback" class="footer-newsletter-feedback mt-2 text-center small font-weight-medium" style="display: none;"></div>
                                    </form>
                                </div>
                            </div>
                        </div>
                    </div>

                    <ul class="list-unstyled mb-0 mt-4 social-icon">
                        <li class="list-inline-item mr-1"><a href="https://scholar.google.com/citations?hl=en&user=zSt9oRMAAAAJ" target="_blank" class="rounded-circle"><i class="mdi mdi-school"></i></a></li>
                        <li class="list-inline-item mr-1"><a href="https://www.linkedin.com/in/harshverma59/" target="_blank" class="rounded-circle"><i class="mdi mdi-linkedin"></i></a></li>
                        <li class="list-inline-item mr-1"><a href="https://github.com/iamharshverma" target="_blank" class="rounded-circle"><i class="mdi mdi-github-face"></i></a></li>
                        <li class="list-inline-item mr-1"><a href="https://twitter.com/harshverma59" target="_blank" class="rounded-circle"><i class="mdi mdi-twitter"></i></a></li>
                        <li class="list-inline-item mr-1"><a href="https://medium.com/@harshverma59" target="_blank" class="rounded-circle"><i class="mdi mdi-medium"></i></a></li>
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

    <a href="#" class="btn btn-icon btn-soft-primary back-to-top"><i data-feather="arrow-up" class="icons"></i></a>

    <!-- Javascript -->
    <script src="js/jquery.min.js"></script>
    <script src="js/bootstrap.bundle.min.js"></script>
    <script src="js/jquery.easing.min.js"></script>
    <script src="js/feather.min.js"></script>
    <script src="js/app.js"></script>

    <script>
    // Client-side Search and Dual Category/Platform Filter Engine
    let currentCategoryFilter = 'all';
    let currentPlatformFilter = 'all';
    let currentSearch = '';

    function applyFilters() {{
        const searchInput = document.getElementById('blogSearchInput');
        const clearBtn = document.getElementById('blogSearchClear');
        const searchTerm = (searchInput ? searchInput.value : '').toLowerCase().trim();
        currentSearch = searchTerm;

        if (clearBtn) {{
            clearBtn.style.display = searchTerm ? 'block' : 'none';
        }}

        const cards = document.querySelectorAll('.blog-card-item');
        let visibleCount = 0;

        cards.forEach(card => {{
            const platform = card.getAttribute('data-platform') || '';
            const category = card.getAttribute('data-category') || '';
            const mainCategory = card.getAttribute('data-main-category') || '';
            const searchData = card.getAttribute('data-search') || '';

            // Category match
            let matchesCategory = false;
            if (currentCategoryFilter === 'all') {{
                matchesCategory = true;
            }} else if (currentCategoryFilter === 'Interviews') {{
                matchesCategory = (mainCategory === 'Interviews' || category === 'Interviews' || card.querySelector('.badge-spotify') !== null);
            }} else {{
                matchesCategory = (mainCategory === currentCategoryFilter);
            }}

            // Platform match
            let matchesPlatform = false;
            if (currentPlatformFilter === 'all') {{
                matchesPlatform = true;
            }} else if (currentPlatformFilter === 'Interviews') {{
                matchesPlatform = (mainCategory === 'Interviews' || category === 'Interviews' || card.querySelector('.badge-spotify') !== null);
            }} else {{
                matchesPlatform = (platform === currentPlatformFilter);
            }}

            // Search text match
            let matchesSearch = true;
            if (searchTerm) {{
                matchesSearch = searchData.includes(searchTerm);
            }}

            if (matchesCategory && matchesPlatform && matchesSearch) {{
                card.style.display = 'block';
                visibleCount++;
            }} else {{
                card.style.display = 'none';
            }}
        }});

        // Update count badge & active filter summary
        const badge = document.getElementById('resultsCountBadge');
        const noResults = document.getElementById('noResultsBox');
        const summary = document.getElementById('activeFilterSummary');

        if (badge) {{
            let catLabel = currentCategoryFilter === 'all' ? '' : `${{currentCategoryFilter}} `;
            badge.innerText = `Showing ${{visibleCount}} of {total_articles} ${{catLabel}}publications`;
        }}

        if (summary) {{
            let catText = currentCategoryFilter === 'all' ? 'All Categories' : currentCategoryFilter;
            let platText = currentPlatformFilter === 'all' ? 'All Platforms' : currentPlatformFilter;
            summary.innerHTML = `<span class="badge badge-light-custom"><i class="mdi mdi-check mr-1 text-success"></i>${{catText}} &bull; ${{platText}}</span>`;
        }}

        if (noResults) {{
            noResults.style.display = visibleCount === 0 ? 'block' : 'none';
        }}
    }}

    // Category Buttons click handler
    document.querySelectorAll('.btn-category-pill').forEach(btn => {{
        btn.addEventListener('click', function() {{
            document.querySelectorAll('.btn-category-pill').forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            currentCategoryFilter = this.getAttribute('data-category-filter');
            applyFilters();
        }});
    }});

    // Platform Chips click handler
    document.querySelectorAll('.btn-platform-chip').forEach(btn => {{
        btn.addEventListener('click', function() {{
            document.querySelectorAll('.btn-platform-chip').forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            currentPlatformFilter = this.getAttribute('data-platform-filter');
            applyFilters();
        }});
    }});

    // Quick filter directly by Category
    function filterByCategory(cat) {{
        document.querySelectorAll('.btn-category-pill').forEach(b => b.classList.remove('active'));
        const targetBtn = document.querySelector(`.btn-category-pill[data-category-filter="${{cat}}"]`);
        if (targetBtn) {{
            targetBtn.classList.add('active');
            currentCategoryFilter = cat;
        }} else {{
            const allBtn = document.querySelector('.btn-category-pill[data-category-filter="all"]');
            if (allBtn) allBtn.classList.add('active');
            currentCategoryFilter = 'all';
        }}
        applyFilters();
        const container = document.getElementById('categoryFilterContainer');
        if (container) {{
            container.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
        }}
    }}

    // Search Input listeners
    const searchInput = document.getElementById('blogSearchInput');
    if (searchInput) {{
        searchInput.addEventListener('input', applyFilters);
    }}

    const clearBtn = document.getElementById('blogSearchClear');
    if (clearBtn) {{
        clearBtn.addEventListener('click', function() {{
            searchInput.value = '';
            applyFilters();
            searchInput.focus();
        }});
    }}

    function filterByTag(tag) {{
        const input = document.getElementById('blogSearchInput');
        if (input) {{
            input.value = tag;
            // Reset categories to all so tag results are not restricted
            document.querySelectorAll('.btn-category-pill').forEach(b => b.classList.remove('active'));
            const allCatBtn = document.querySelector('.btn-category-pill[data-category-filter="all"]');
            if (allCatBtn) allCatBtn.classList.add('active');
            currentCategoryFilter = 'all';

            document.querySelectorAll('.btn-platform-chip').forEach(b => b.classList.remove('active'));
            const allPlatBtn = document.querySelector('.btn-platform-chip[data-platform-filter="all"]');
            if (allPlatBtn) allPlatBtn.classList.add('active');
            currentPlatformFilter = 'all';

            applyFilters();
            input.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
        }}
    }}

    function resetFilters() {{
        const input = document.getElementById('blogSearchInput');
        if (input) input.value = '';
        
        document.querySelectorAll('.btn-category-pill').forEach(b => b.classList.remove('active'));
        const allCatBtn = document.querySelector('.btn-category-pill[data-category-filter="all"]');
        if (allCatBtn) allCatBtn.classList.add('active');
        currentCategoryFilter = 'all';

        document.querySelectorAll('.btn-platform-chip').forEach(b => b.classList.remove('active'));
        const allPlatBtn = document.querySelector('.btn-platform-chip[data-platform-filter="all"]');
        if (allPlatBtn) allPlatBtn.classList.add('active');
        currentPlatformFilter = 'all';

        applyFilters();
    }}

    function sortArticles(type) {{
        const grid = document.getElementById('blogArticlesGrid');
        const cards = Array.from(grid.querySelectorAll('.blog-card-item'));

        cards.sort((a, b) => {{
            if (type === 'featured') {{
                const aFeat = a.getAttribute('data-featured') === 'true' ? 1 : 0;
                const bFeat = b.getAttribute('data-featured') === 'true' ? 1 : 0;
                return bFeat - aFeat;
            }} else if (type === 'title') {{
                const aTitle = a.querySelector('.card-title a').innerText.trim().toLowerCase();
                const bTitle = b.querySelector('.card-title a').innerText.trim().toLowerCase();
                return aTitle.localeCompare(bTitle);
            }} else if (type === 'platform') {{
                const aPlat = a.getAttribute('data-platform').toLowerCase();
                const bPlat = b.getAttribute('data-platform').toLowerCase();
                return aPlat.localeCompare(bPlat);
            }}
            return 0;
        }});

        cards.forEach(card => grid.appendChild(card));
        applyFilters();
    }}

    // Check URL parameters or hash on load (e.g. #cybersecurity, #ai-research, #engineering)
    document.addEventListener('DOMContentLoaded', function() {{
        try {{
            const urlParams = new URLSearchParams(window.location.search);
            const catParam = urlParams.get('category') || (window.location.hash ? window.location.hash.replace('#', '') : '');
            if (catParam) {{
                const clean = catParam.toLowerCase().replace(/[^a-z]/g, '');
                const pills = document.querySelectorAll('.btn-category-pill');
                for (let pill of pills) {{
                    const val = pill.getAttribute('data-category-filter').toLowerCase().replace(/[^a-z]/g, '');
                    if (val === clean || (clean === 'ai' && val === 'airesearch') || (clean === 'cyber' && val === 'cybersecurity')) {{
                        pill.click();
                        break;
                    }}
                }}
            }}
        }} catch(e) {{}}
    }});
    </script>
    <!-- HV AI Copilot Assistant Engine -->
    <script src="js/hv-copilot.js"></script>
    <!-- Blog Newsletter Subscription Modal Engine -->
    <script src="js/hv-blog-newsletter.js"></script>
</body>
</html>
'''
    with open('page-blog.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Generated page-blog.html with {total_articles} articles successfully!")

if __name__ == '__main__':
    generate_blog_html()
