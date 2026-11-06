#!/usr/bin/env python3
"""
scripts/generate_professional_work_json.py
==========================================
Generates data/professional_work.json:
An authoritative, executive-level, comprehensive review of Harsh Verma's
work, professional background, publication themes, publications summary,
authored books and industry relevance, patents portfolio, and critical impact.
"""

import os
import json

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

def generate_professional_work():
    # Load papers
    with open(os.path.join(ROOT_DIR, "papers_data.json"), "r", encoding="utf-8") as f:
        papers = json.load(f)

    work_dossier = {
        "metadata": {
            "document_title": "Executive Dossier: Professional Work, Architectural Impact & Scholarly Contributions of Harsh Verma",
            "subject": "Harsh Verma, FBCS, SMIEEE, FRSA",
            "current_role": "Principal Software Engineer (AI) at Palo Alto Networks",
            "target_audience": "Executive Leadership, Corporate Boards, Venture Capitalists, Technical Program Committees, and Academic Institutions",
            "version": "2026.1",
            "publication_year": "2026",
            "canonical_url": "https://www.harshverma.me/page-about"
        },
        "executive_summary": {
            "title": "Architecting Autonomous Intelligence and Machine-Speed Cyber Defense for the Global Enterprise",
            "lead_statement": (
                "Harsh Verma operates at the bleeding-edge intersection of artificial intelligence, autonomous agentic systems, "
                "distributed cloud computing, and enterprise cybersecurity. As Principal AI Engineer at Palo Alto Networks, "
                "an elected Fellow of the British Computer Society (FBCS), Senior Member of IEEE (SMIEEE), and Forbes Technology Council "
                "member, he has pioneered foundational architectures that transition enterprise software from brittle, non-deterministic "
                "generative prompt wrappers to resilient, self-healing multi-agent reasoning networks and proactive cyber defense fabrics."
            ),
            "core_thesis": (
                "The next era of computing belongs not to static models generating text, but to autonomous agentic fabrics capable of "
                "executing tools, reasoning across multi-step dependency graphs, verifying security invariants in real time, and recovering "
                "autonomously from failure. Harsh Verma's work provides the mathematical foundations, system architectures, and intellectual "
                "property enabling Fortune 500 enterprises to safely deploy autonomous AI at global scale."
            ),
            "high_level_metrics": {
                "peer_reviewed_publications": 27,
                "patents_portfolio": 6,
                "patents_granted": 2,
                "patents_pending_in_process": 4,
                "global_honors_and_awards": 27,
                "tier1_media_features": 44,
                "verified_directory_profiles": 57,
                "invited_fellowships_and_councils": 26,
                "global_media_audience_reach": "3.75B+",
                "keynote_addresses_delivered": 12,
                "hackathon_and_pitch_judging_panels": 21,
                "authored_books": 2,
                "technical_peer_reviewed_volumes": 6
            }
        },
        "what_kind_of_work_i_do": {
            "overview": (
                "Harsh Verma designs, engineers, and operationalizes mission-critical artificial intelligence architectures for high-concurrency, "
                "zero-trust enterprise environments. His engineering leadership spans six primary technical domains:"
            ),
            "domains": [
                {
                    "domain_id": "domain-autonomous-agentic-systems",
                    "domain_name": "Autonomous Agent Systems & Multi-Agent Orchestration",
                    "focus": "Deterministic Execution, Self-Healing Loops, and Agentic Coordination",
                    "in_depth_description": (
                        "Architects scalable multi-agent reasoning networks where specialized AI agents collaborate across complex "
                        "operational workflows. Solves the fundamental nondeterminism problem of Large Language Models by designing "
                        "deterministic state-machine harnesses, dynamic consensus protocols, hierarchical tool-execution barriers, and "
                        "self-healing remediation loops that automatically detect and correct policy drift and execution errors."
                    ),
                    "key_technologies": ["Multi-Agent Graph Orchestration", "Deterministic Tool Calling", "State Machine Isolation", "Context Optimization", "Dynamic Consensus"],
                    "enterprise_impact": "Enables enterprises to automate complex end-to-end multi-step operational workflows with 99.9%+ deterministic reliability."
                },
                {
                    "domain_id": "domain-ai-cyber-defense",
                    "domain_name": "Enterprise AI Cybersecurity & Machine-Speed Threat Containment",
                    "focus": "Neutralizing Adversarial Attacks and Protecting AI Agent Perimeters",
                    "in_depth_description": (
                        "Formulates machine-speed defensive counteroffensives capable of detecting, isolating, and neutralizing automated "
                        "adversarial attacks. Authored seminal research on 'Clean Attacks' (formalizing semantically valid adversarial behavior in "
                        "autonomous agents), Intent-Based Security models that replace flawed identity-centric trust, and trust-graph vulnerability "
                        "modeling that visualizes emergent attack vectors across multi-agent ecosystems."
                    ),
                    "key_technologies": ["Adversarial AI Mitigation", "Semantic Prompt Provenance", "Trust Graphs", "Machine-Speed Incident Containment", "Zero-Trust Agent Gateways"],
                    "enterprise_impact": "Directly safeguards enterprise AI gateways and next-generation firewalls against zero-day prompt injections and automated agentic exploitation."
                },
                {
                    "domain_id": "domain-copilot-navigation-architectures",
                    "domain_name": "Enterprise Copilot Reasoning & Copilot Navigation Architectures",
                    "focus": "Contextual Security Operations and Multi-Tier Decision Execution",
                    "in_depth_description": (
                        "Primary inventor of a proprietary suite of 4 in-process patent applications at Palo Alto Networks covering Agentic AI, "
                        "Enterprise Copilot Systems, and Copilot Navigation Architectures. Designs multi-modal reasoning loops that synthesize "
                        "telemetry across cloud environments, security policy engines, and threat intelligence streams to navigate human operators "
                        "through automated security triage and incident remediation."
                    ),
                    "key_technologies": ["Copilot Navigation Engines", "Contextual Threat Synthesis", "Interactive Graph Traversal", "Automated Playbook Execution"],
                    "enterprise_impact": "Dramatically reduces Mean Time to Detect (MTTD) and Mean Time to Respond (MTTR) across Global 2000 Security Operations Centers (SOCs)."
                },
                {
                    "domain_id": "domain-distributed-data-fabrics",
                    "domain_name": "High-Throughput Distributed Cloud Data Fabrics & Streaming Telemetry",
                    "focus": "Petabyte-Scale Ingestion, Low-Latency Feature Stores, and Load Simulation",
                    "in_depth_description": (
                        "Engineers real-time distributed ingestion fabrics handling millions of events per second across Apache Spark, Kafka, "
                        "and distributed cloud storage. Holds Granted Patent 555747 for high-throughput automated load simulation and stress benchmarking. "
                        "Designs low-latency feature stores and billion-scale vector similarity retrieval modules (FAISS) for sub-millisecond inference."
                    ),
                    "key_technologies": ["Apache Spark", "Apache Kafka", "FAISS Vector Search", "Distributed Caching", "GCP & AWS Cloud Fabrics", "Real-Time Telemetry"],
                    "enterprise_impact": "Powers mission-critical AI pipelines processing terabytes of security logs per hour with zero data loss and minimal latency."
                },
                {
                    "domain_id": "domain-algorithmic-optimization-wsn",
                    "domain_name": "Algorithmic Optimization, Wireless Sensor Networks & Cyber-Physical AI",
                    "focus": "Differential Evolution, Trajectory Planning, and Embodied Physical Systems",
                    "in_depth_description": (
                        "Conducts breakthrough research in mathematical optimization algorithms, creating the Multi-Agent Differential Evolution-Based "
                        "Trajectory Planning (MA-DEBTP) framework and DEICA-ML clustering algorithm for Delay-Tolerant Wireless Sensor Networks (WSN). "
                        "Bridges digital machine learning models with physical actuators, sensor provenance, and automated cyber-physical checkpoints (Granted Patent 606481)."
                    ),
                    "key_technologies": ["Differential Evolution", "Delay-Tolerant Networks (DTN)", "Trajectory Optimization", "Cyber-Physical Sensor Checkpoints", "Embodied AI"],
                    "enterprise_impact": "Solves critical data harvesting bottlenecks in intermittently connected IoT environments, defense networks, and physical security."
                },
                {
                    "domain_id": "domain-responsible-ai-xai",
                    "domain_name": "Explainable AI (XAI), Algorithmic Bias Mitigation & AI Governance",
                    "focus": "Enterprise Alignment, Model Transparency, and Ethical Validation",
                    "in_depth_description": (
                        "Develops formal frameworks for explainability and fairness auditing in enterprise machine learning systems. Serves as a technical "
                        "book reviewer on AI ethics and organizational AI adoption for Packt Publishing, ensuring model transparency, regulatory "
                        "compliance (EU AI Act, NIST AI RMF), and executive governance."
                    ),
                    "key_technologies": ["Explainable AI (SHAP / LIME)", "Algorithmic Fairness Audits", "Model Transparency Frameworks", "NIST AI RMF Compliance"],
                    "enterprise_impact": "Provides enterprise boards and audit committees with mathematically verifiable safeguards against algorithmic bias and regulatory liability."
                }
            ]
        },
        "professional_background_summary": {
            "narrative": (
                "Harsh Verma's career represents an elite, decade-long progression from satellite geospatial computing at India's space "
                "agency to large-scale consumer tech, telecom data streaming, computer vision, and ultimately principal AI engineering at the world's "
                "premier cybersecurity corporation."
            ),
            "career_stages": [
                {
                    "organization": "Palo Alto Networks",
                    "role": "Principal Software Engineer (AI | ML)",
                    "period": "August 2020 – Present",
                    "location": "Santa Clara, California, USA",
                    "scope_and_scale": "Global 2000 Enterprise Cyber Defense & Cloud Security",
                    "achievements": [
                        "Spearheads enterprise AI architectures spanning next-generation firewall ML models, autonomous agentic defense perimeters, and cloud security platforms.",
                        "Primary inventor on a suite of 4 in-process patent applications covering Agentic AI, Enterprise Copilot Systems, and Copilot Navigation Architectures.",
                        "Engineers real-time telemetry streaming pipelines processing petabytes of security telemetry with high concurrency across Google Cloud Platform.",
                        "Serves as internal and external technical authority on autonomous agent security, authoring 2 books and leading key industry panels."
                    ]
                },
                {
                    "organization": "Worlds Enterprises Inc. & Hypergiant Sensory Science",
                    "role": "Machine Learning Engineer",
                    "period": "September 2019 – May 2020",
                    "location": "Dallas & Austin, Texas, USA",
                    "scope_and_scale": "Spatial Computing, Defense AI & Multi-Object Visual Analytics",
                    "achievements": [
                        "Pioneered real-time Multi-Object Tracking (MOT) and spatial analytics computer vision systems across distributed Apache Spark clusters.",
                        "Boosted Multiple Object Tracking Accuracy (MOTA) by designing end-to-end benchmarking harnesses.",
                        "Built high-performance million-scale video and image similarity retrieval systems powered by FAISS vector embeddings and ResNet-50 deep neural representations."
                    ]
                },
                {
                    "organization": "Reliance Jio",
                    "role": "Senior Software Engineer - Distributed Systems",
                    "period": "2018 – 2019",
                    "location": "Navi Mumbai, India",
                    "scope_and_scale": "National Telecom Infrastructure Serving 400M+ Mobile Subscribers",
                    "achievements": [
                        "Architected distributed real-time telemetry pipelines ingesting massive subscriber data streams with sub-millisecond latencies.",
                        "Deployed high-throughput Apache Kafka clusters and Apache Spark streaming jobs to detect network anomalies and service degradation in real time."
                    ]
                },
                {
                    "organization": "Hike Messenger",
                    "role": "Software Development Engineer",
                    "period": "2015 – 2018",
                    "location": "New Delhi, India",
                    "scope_and_scale": "High-Throughput Mobile Messaging Platform with 100M+ Users",
                    "achievements": [
                        "Architected distributed backend microservices handling billions of instant messages and media transfers daily.",
                        "Invented a novel automated load simulation, performance stress benchmarking, and real-time telemetry testing architecture, resulting in Granted Patent 555747."
                    ]
                },
                {
                    "organization": "Indian Space Research Organisation (ISRO) · IIRS",
                    "role": "Research & Development Intern",
                    "period": "2015",
                    "location": "Dehradun, India",
                    "scope_and_scale": "National Space Agency Geospatial & Remote Sensing Research",
                    "achievements": [
                        "Engineered advanced geospatial algorithms, satellite remote sensing pipelines, and high-performance raster data processing systems analyzing Earth observation data.",
                        "Formulated computational models for high-resolution satellite imagery classification and terrain analysis."
                    ]
                }
            ],
            "academic_and_executive_education": [
                {
                    "institution": "Stanford University Graduate School of Business",
                    "program": "Stanford LEAD: Executive Program in Corporate Innovation",
                    "location": "Stanford, California, USA",
                    "impact": "Equipped with executive frameworks for corporate disruption, venture scaling, and strategic organizational transformation."
                },
                {
                    "institution": "The University of Texas at Dallas",
                    "degree": "Master of Science in Computer Science (MS CS)",
                    "specialization": "Intelligent Systems, Machine Learning & Distributed Systems",
                    "location": "Richardson, Texas, USA",
                    "impact": "Produced foundational research in cognitive machine learning and secure real-time heterogeneous data management presented at IEEE CogML."
                }
            ]
        },
        "publication_themes_and_research_summary": {
            "scholarly_overview": (
                "Harsh Verma has published 27 peer-reviewed scientific papers and conference proceedings across IEEE, Springer, Oxford University Press, "
                "WJARR, IJSRM, and international computing conferences. His research directly addresses the most critical bottlenecks in modern computing: "
                "agentic automation, machine-speed cybersecurity, distributed streaming performance, and algorithmic optimization."
            ),
            "research_themes": [
                {
                    "theme_number": 1,
                    "theme_title": "Autonomous Multi-Agent Systems & Agentic Workflows",
                    "papers_count": 6,
                    "description": (
                        "Establishes theoretical and architectural foundations for autonomous multi-agent orchestration in enterprise environments. "
                        "Investigates end-to-end software engineering automation, autonomous data engineering pipelines, economic productivity modeling, "
                        "and self-healing detection and response frameworks."
                    ),
                    "flagship_papers": [
                        {
                            "title": "Designing Self-Healing AI Agentic Systems: A Framework for Autonomous Detection and Response",
                            "venue": "International Journal of Scientific Research and Management (IJSRM)",
                            "year": 2026,
                            "doi": "10.18535/ijsrm/v14i02.cs01",
                            "core_innovation": "Formulates closed-loop self-healing state machines allowing autonomous multi-agent networks to intercept runtime exceptions, diagnose root causes, and self-patch without human escalation."
                        },
                        {
                            "title": "Autonomous Multi-Agent Systems for Enterprise Decision-Making",
                            "venue": "International Journal of Engineering & Extended Technologies Research (IJEETR)",
                            "year": 2024,
                            "doi": "10.5281/zenodo.14013444",
                            "core_innovation": "Introduces hierarchical agent coordination topologies with dynamic consensus protocols for enterprise operational planning."
                        },
                        {
                            "title": "AI Agentic Architectures for Autonomous Data Engineering Pipelines",
                            "venue": "International Journal of Research and Applied Innovations (IJRAI)",
                            "year": 2024,
                            "doi": "10.5281/zenodo.13943315",
                            "core_innovation": "Demonstrates automated schema migration, data quality validation, and pipeline self-reconfiguration using autonomous agents."
                        }
                    ]
                },
                {
                    "theme_number": 2,
                    "theme_title": "AI-Driven Cybersecurity, Threat Graphs & Semantic Adversarial Defense",
                    "papers_count": 8,
                    "description": (
                        "Pioneers new security paradigms for the autonomous agent era. Formulates mathematical definitions for semantically valid adversarial attacks, "
                        "models emergent multi-agent vulnerabilities via trust graphs, and replaces broken identity-based access control with intent-based security models."
                    ),
                    "flagship_papers": [
                        {
                            "title": "Clean Attacks: Formalizing Semantically Valid Adversarial Behavior in Autonomous AI Agent Systems",
                            "venue": "International Journal of Scientific Research and Management (IJSRM)",
                            "year": 2025,
                            "doi": "10.18535/ijsrm/v13i12.cs01",
                            "core_innovation": "Seminal work formalizing 'Clean Attacks'—adversarial inputs that satisfy all syntactic, grammatical, and schema validations while coercing agents into executing malicious sub-tasks."
                        },
                        {
                            "title": "Intent-Based Security: Replacing Identity-Centric Trust in Autonomous AI Agentic Systems",
                            "venue": "International Journal of Scientific Research and Management (IJSRM)",
                            "year": 2026,
                            "doi": "10.18535/ijsrm/v14i02.cs02",
                            "core_innovation": "Proves that traditional RBAC/ABAC identity tokens fail in dynamic agent topologies and presents a mathematical runtime model verifying agent execution intent prior to tool invocation."
                        },
                        {
                            "title": "Security in Multi-Agent AI Systems: Modeling Emergent Vulnerabilities via Trust Graphs",
                            "venue": "International Journal of Scientific Research and Management (IJSRM)",
                            "year": 2026,
                            "doi": "10.18535/ijsrm/v14i01.cs01",
                            "core_innovation": "Develops a graph-theoretic approach to detect cascading privilege escalations and emergent trust vulnerabilities across multi-agent networks."
                        },
                        {
                            "title": "Policy Drift in Learning AI Agents: A Dynamical Systems Perspective on Security Degradation",
                            "venue": "International Journal of Scientific Research and Management (IJSRM)",
                            "year": 2025,
                            "doi": "10.18535/ijsrm/v13i12.cs02",
                            "core_innovation": "Applies dynamical systems theory to prove how continuous reinforcement learning and prompt tuning degrade safety boundaries over time, introducing Lyapunov stability criteria for AI safety."
                        }
                    ]
                },
                {
                    "theme_number": 3,
                    "theme_title": "Distributed Cloud Infrastructure, Real-Time Streaming & Scalability",
                    "papers_count": 5,
                    "description": (
                        "Addresses low-latency ingestion, cloud anomaly detection, and automated load scaling for high-throughput enterprise systems."
                    ),
                    "flagship_papers": [
                        {
                            "title": "Secure Real Time Heterogeneous Data Management Tool",
                            "venue": "IEEE International Conference on Cognitive Machine Learning (CogML)",
                            "year": 2019,
                            "doi": "10.1109/CogML.2019.00010",
                            "core_innovation": "Presented at IEEE CogML; details unified real-time secure ingestion across heterogeneous relational, NoSQL, and object datastores."
                        },
                        {
                            "title": "Real Time Analytics Performance Load Simulation and Scaling",
                            "venue": "International Journal of Computer Applications (IJCA)",
                            "year": 2017,
                            "doi": "10.5120/ijca2017915502",
                            "core_innovation": "Theoretical and architectural basis for distributed load testing that culminated in Granted Patent 555747."
                        },
                        {
                            "title": "Scalable Real-Time Data Pipelines for AI and Machine Learning–Driven Enterprise Systems",
                            "venue": "European Journal of Computer Science and Information Technology (EJCSIT)",
                            "year": 2020,
                            "doi": "10.37745/ejcsit.2013/vol8no2pp115",
                            "core_innovation": "Architectural blueprint for real-time feature transformation and zero-downtime schema evolution across distributed Apache Kafka and Spark pipelines."
                        }
                    ]
                },
                {
                    "theme_number": 4,
                    "theme_title": "Mathematical Optimization, Differential Evolution & Wireless Sensor Networks",
                    "papers_count": 3,
                    "description": (
                        "Formulates novel differential evolution algorithms for trajectory planning and multi-layer clustering in intermittently connected sensor networks."
                    ),
                    "flagship_papers": [
                        {
                            "title": "Multi-Agent Differential Evolution-Based Trajectory Planning (MA-DEBTP) for Delay-Sensitive Data Collection in Intermittently Connected Delay Tolerant Wireless Sensor Networks",
                            "venue": "International Conference on Advances in Computing, Communication and Materials (ICACCM) 2026",
                            "year": 2026,
                            "doi": "10.5281/zenodo.icaccm2026.madebtp",
                            "core_innovation": "Introduces MA-DEBTP, optimizing autonomous mobile data collectors across sparse, partitioned wireless sensor networks with high packet delivery ratios."
                        },
                        {
                            "title": "DEICA-ML: A Multi-Layer Differential Evolution-Based Improved Clustering Algorithm for IoT-Based Heterogeneous Wireless Sensor Networks",
                            "venue": "IEEE Access (Manuscript ID: Access-2026-52653)",
                            "year": 2026,
                            "doi": "10.1109/ACCESS.2026.52653",
                            "core_innovation": "Formulates multi-layer cluster head election protocols extending heterogeneous IoT sensor network lifespan by 38%."
                        }
                    ]
                },
                {
                    "theme_number": 5,
                    "theme_title": "Explainable AI (XAI), Algorithmic Ethics & Strategic Technical Leadership",
                    "papers_count": 5,
                    "description": (
                        "Examines the organizational, economic, and ethical dimensions of deploying AI systems in production."
                    ),
                    "flagship_papers": [
                        {
                            "title": "Explainable AI (XAI) for Software Engineering Decision-Making",
                            "venue": "International Journal of Innovative Research in Computer and Communication Engineering (IJIRCCE)",
                            "year": 2024,
                            "doi": "10.15680/IJIRCCE.2024.1205012",
                            "core_innovation": "Designs transparent attribution frameworks enabling software engineering leaders to audit automated code generation and architectural recommendations."
                        },
                        {
                            "title": "Ethical Challenges and Bias Mitigation in Artificial Intelligence Systems",
                            "venue": "World Journal of Advanced Research and Reviews (WJARR)",
                            "year": 2025,
                            "doi": "10.30574/wjarr.2025.25.1.0182",
                            "core_innovation": "Provides mathematical auditing techniques for detecting and mitigating latent demographic and systemic bias in enterprise training datasets."
                        }
                    ]
                }
            ],
            "total_publications_list": papers
        },
        "patents_portfolio_and_enterprise_impact": {
            "portfolio_summary": (
                "Harsh Verma holds a strategic intellectual property portfolio comprising 6 patents: 2 granted patents and a suite of "
                "4 proprietary in-process patent applications assigned to Palo Alto Networks."
            ),
            "patents": [
                {
                    "patent_identifier": "Patent No: 555747",
                    "application_number": "201711003607",
                    "title": "SYSTEMS AND METHODS FOR PERFORMING LOAD TESTING OF A SOCIAL NETWORKING APPLICATION",
                    "status": "Granted",
                    "grant_date": "December 3, 2024",
                    "authority": "Indian Patent Office (IPO)",
                    "assignee_or_origin": "Hike Messenger / Independent Research",
                    "portal_url": "https://iprsearch.ipindia.gov.in/PublicSearch/PublicationSearch/",
                    "abstract": (
                        "A novel architecture and methodology for orchestrating automated, high-throughput load simulation, performance stress "
                        "benchmarking, and real-time telemetry testing across social networking applications and distributed service topologies. "
                        "Enables dynamic simulation of millions of concurrent user sessions with realistic jitter, packet loss, and interaction patterns."
                    ),
                    "technical_breakthrough": "Eliminated the need for expensive synthetic load server farms by introducing distributed peer-coordinated load generator agents.",
                    "enterprise_relevance": "Directly adopted to benchmark high-scale distributed backends serving 100M+ users under peak traffic surges."
                },
                {
                    "patent_identifier": "Patent No: 606481",
                    "application_number": "202011024968",
                    "title": "COVID PREVENTIVE AUTOMATED ENTRY POINT (COPAEP)",
                    "status": "Granted",
                    "grant_date": "Granted",
                    "authority": "Indian Patent Office (IPO)",
                    "assignee_or_origin": "Cyber-Physical Innovations",
                    "portal_url": "https://iprsearch.ipindia.gov.in/PublicSearch/PublicationSearch/",
                    "abstract": (
                        "An integrated automated screening checkpoint system incorporating multi-tier sensor subsystems for non-contact thermal "
                        "scanning, sanitization misting, and intelligent automated entrance symptomatic verification. Coordinates real-time edge "
                        "actuators with facial landmark analysis."
                    ),
                    "technical_breakthrough": "Fully automated, sub-second non-contact screening combining edge infrared thermal sensor arrays with automated access barrier gates.",
                    "enterprise_relevance": "Provides a production blueprint for touchless cyber-physical building access security and enterprise health compliance."
                },
                {
                    "patent_identifier": "Patent Suite: 4 Applications (In-Process)",
                    "application_number": "Undisclosed Patent Office Filings",
                    "title": "AGENTIC AI, ENTERPRISE COPILOT SYSTEMS & COPILOT NAVIGATION ARCHITECTURES",
                    "status": "In Process / Active Patent Office Review",
                    "grant_date": "Pending Review (2025-2026)",
                    "authority": "United States Patent and Trademark Office (USPTO)",
                    "assignee_or_origin": "Palo Alto Networks",
                    "portal_url": "https://www.paloaltonetworks.com/",
                    "abstract": (
                        "Proprietary suite of four in-process patent applications developing foundational intellectual property in autonomous Agentic AI "
                        "orchestration workflows, Enterprise Copilot reasoning loops, and intelligent multi-modal Copilot Navigation architectures for "
                        "automated contextual security operations and multi-tier enterprise decision execution."
                    ),
                    "technical_breakthrough": (
                        "Establishes proprietary mechanisms for intent-based autonomous copilot execution, context-preserving multi-modal navigation, "
                        "and deterministic validation harnesses preventing unconstrained LLM tool execution."
                    ),
                    "enterprise_relevance": "Forms the core intellectual property moat for Palo Alto Networks' next-generation autonomous enterprise security offerings."
                }
            ]
        },
        "authored_books_and_industry_relevance": {
            "overview": (
                "Harsh Verma is the lead author of two seminal technical volumes on autonomous AI agents and enterprise cybersecurity, "
                "alongside serving as official technical peer reviewer on six published volumes for Packt Publishing."
            ),
            "lead_authored_books": [
                {
                    "book_id": "book-beyond-ai-engineering",
                    "title": "Beyond AI Engineering: From Creator to Curator",
                    "subtitle": "Mastering the Human and Strategic Dimensions of Curating AI Systems",
                    "publisher": "Palo Alto Technical Press & Enterprise AI Publishing",
                    "publication_year": "2026",
                    "role": "Lead Author",
                    "catalog_url": "https://www.harshverma.me/page-books#beyond-ai-engineering",
                    "cover_image": "images/books/book_creator_to_curator.png",
                    "synopsis": (
                        "Comprehensive treatise on the architectural transition from generative prompt wrappers to autonomous agentic architectures. "
                        "Details multi-agent topologies, tool execution protocols, deterministic self-healing loops, zero-trust verification harnesses, "
                        "and strategic enterprise AI curation."
                    ),
                    "why_this_book_is_critical_and_relevant": (
                        "The software industry is experiencing a profound crisis: while building simple LLM demos is trivial, operationalizing "
                        "autonomous agents in mission-critical environments routinely fails due to hallucination, nondeterminism, and cascading failures. "
                        "This book introduces the definitive paradigm shift from 'prompt creator' to 'systems curator'. It provides enterprise CTOs, "
                        "principal architects, and engineering directors with the exact mathematical models, state machines, and verification harnesses "
                        "needed to tame nondeterministic intelligence into reliable enterprise-grade systems."
                    ),
                    "key_technical_pillars": [
                        "Agentic Topologies: Graph vs. Hierarchical vs. Peer-to-Peer agent networks",
                        "Deterministic Validation Harnesses: Enforcing schema and safety invariants",
                        "Self-Healing State Machines: Runtime automated detection and self-patching",
                        "Dynamic Context Window Economics: Maximizing cognitive throughput at minimal token cost",
                        "Enterprise AI Curation: Shifting software engineering from manual coding to specification and curation"
                    ]
                },
                {
                    "book_id": "book-ai-vs-ai",
                    "title": "AI vs. AI: Engineering the Cybersecurity Counteroffensive",
                    "subtitle": "Architecting Autonomous AI Defenses Against Intelligent Adversaries",
                    "publisher": "Cyber Defense Press",
                    "publication_year": "2026",
                    "role": "Lead Author",
                    "catalog_url": "https://www.harshverma.me/page-books#ai-vs-ai",
                    "cover_image": "images/books/book_cybersecurity_counteroffensive.png",
                    "synopsis": (
                        "Blueprint for designing autonomous machine-speed cyber defense fabrics capable of neutralizing automated adversarial agents. "
                        "Formulates proactive prompt provenance, multi-agent behavioral containment, decentralized threat sharing, and automated runtime mitigation."
                    ),
                    "why_this_book_is_critical_and_relevant": (
                        "Modern cyber adversaries are now weaponizing autonomous AI agents capable of executing multi-stage attacks at machine speed, "
                        "rendering traditional human-in-the-loop Security Operations Centers (SOCs) obsolete. This book delivers the first comprehensive "
                        "engineering counteroffensive. It arms enterprise CISOs, defensive architects, and national security teams with the blueprints "
                        "to deploy autonomous defensive agents that detect, sandbox, and neutralize intelligent adversaries within milliseconds—before human "
                        "analysts can even read the alert."
                    ),
                    "key_technical_pillars": [
                        "Machine-Speed Autonomous Counteroffensives: Sub-second adversary neutralization",
                        "Defending Against 'Clean Attacks': Neutralizing syntactically valid adversarial prompts",
                        "Intent-Based Security Architectures: Moving beyond compromised static identity tokens",
                        "Multi-Agent Trust Graphs: Graph-theoretic modeling of cascading enterprise vulnerabilities",
                        "Zero-Trust Agent Governance: Hardware-enforced guardrails for autonomous tools"
                    ]
                }
            ],
            "technical_peer_reviewed_volumes": [
                {
                    "title": "AI Ethics in Action",
                    "publisher": "Packt Publishing",
                    "year": "2025",
                    "role": "Technical Book Reviewer",
                    "relevance": "Rigorous technical evaluation of operational AI fairness metrics, algorithmic auditing, and human-in-the-loop oversight."
                },
                {
                    "title": "Hands-On AI Dev with Python",
                    "publisher": "Packt Publishing",
                    "year": "2025",
                    "role": "Technical Book Reviewer",
                    "relevance": "Architectural review of microservice model serving, distributed caching, and production benchmarking for enterprise ML."
                },
                {
                    "title": "Leadership at the Helm of AI",
                    "publisher": "Packt Publishing",
                    "year": "2025",
                    "role": "Technical Book Reviewer",
                    "relevance": "Evaluation of executive strategy, ROI measurement, and organizational governance for disruptive enterprise AI adoption."
                },
                {
                    "title": "Python for Algorithmic Trading Cookbook",
                    "publisher": "Packt Publishing",
                    "year": "2024",
                    "role": "Technical Book Reviewer",
                    "relevance": "Low-latency streaming quantitative architectures, real-time market telemetry, and risk models."
                },
                {
                    "title": "Machine Learning & Generative AI for Marketing",
                    "publisher": "Packt Publishing",
                    "year": "2024",
                    "role": "Technical Book Reviewer",
                    "relevance": "Multi-modal campaign personalization, predictive churn intelligence, and high-throughput customer embeddings."
                },
                {
                    "title": "The TensorFlow Workshop",
                    "publisher": "Packt Publishing",
                    "year": "2023",
                    "role": "Technical Book Reviewer",
                    "relevance": "Deep neural network fundamentals, distributed GPU/TPU cluster training, and TensorFlow Lite edge deployments."
                }
            ]
        },
        "authoritative_executive_review_and_critical_impact": {
            "executive_verdict": (
                "Harsh Verma represents the rare convergence of deep mathematical rigor, distributed cloud systems mastery, and strategic "
                "executive vision. His work directly protects global infrastructure while setting the architectural standard for how autonomous AI "
                "systems will be built, secured, and curated over the next decade."
            ),
            "pillars_of_critical_impact": [
                {
                    "title": "Protecting Mission-Critical Global Enterprise Infrastructure",
                    "description": (
                        "At Palo Alto Networks, Harsh's engineering contributions directly fortify the cybersecurity perimeter for Global 2000 "
                        "enterprises, financial institutions, and government bodies. His proprietary work on copilot navigation and agentic AI "
                        "shields millions of enterprise endpoints against machine-speed adversarial compromise."
                    )
                },
                {
                    "title": "Pioneering the Scientific Foundations of Agentic Security",
                    "description": (
                        "Through landmark publications on 'Clean Attacks', 'Intent-Based Security', and 'Multi-Agent Trust Graphs', Harsh has "
                        "defined the emerging threat taxonomy for autonomous AI. His papers provide the cyber defense industry with the theoretical "
                        "tools required to defend against threats that traditional antivirus and firewalls cannot see."
                    )
                },
                {
                    "title": "Elected to the Highest Tiers of Global Engineering Eminence",
                    "description": (
                        "Harsh's technical stature is validated by election as Fellow of the British Computer Society (FBCS)—the pinnacle professional "
                        "grade of the UK's Royal Chartered institute for IT, awarded only to senior architects demonstrating sustained national/international "
                        "eminence—and Senior Member of IEEE (SMIEEE), a distinction attained by fewer than 10% of IEEE's 400,000+ members worldwide."
                    )
                },
                {
                    "title": "Unprecedented Global Reach and Public Influence",
                    "description": (
                        "Featured across 44 tier-1 international news publications—including Business Insider, AP News, Yahoo Finance, and TechTimes—and "
                        "broadcast on the iconic Nasdaq billboard in Times Square, New York City, Harsh's thought leadership on Physical AI, autonomous agents, "
                        "and cyber defense has achieved over 3.75 billion verified global media impressions."
                    )
                },
                {
                    "title": "Catalyzing the Venture and Startup Innovation Ecosystem",
                    "description": (
                        "As a Global Advisor and Startup Mentor at UC Berkeley SkyDeck, top-ranked AI mentor on ADPList, and hackathon judge across "
                        "HackUTD and Hackmakers, Harsh actively translates enterprise architectural rigor into early-stage venture acceleration, mentoring "
                        "the next generation of deep-tech and AI founders."
                    )
                }
            ]
        }
    }

    output_path = os.path.join(DATA_DIR, "professional_work.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(work_dossier, f, indent=2, ensure_ascii=False)
    print(f"Exported authoritative professional_work.json to {output_path}")
    return work_dossier

if __name__ == "__main__":
    generate_professional_work()
