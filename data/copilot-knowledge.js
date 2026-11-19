const fs = require('fs');
const path = require('path');

function loadJsonSafe(filename) {
  try {
    const fullPath = path.join(__dirname, '..', filename);
    if (fs.existsSync(fullPath)) {
      return JSON.parse(fs.readFileSync(fullPath, 'utf8'));
    }
  } catch (err) {
    console.error(`Error loading ${filename}:`, err.message);
  }
  return [];
}

const awardsData = loadJsonSafe('awards_data.json');
const papersData = loadJsonSafe('papers_data.json');
const mediaData = loadJsonSafe('media_data.json');

const harshKnowledge = {
  biography: {
    fullName: "Harsh Verma",
    title: "Enterprise AI Architect, Principal Technologist & Author",
    shortBio: "Harsh Verma is an internationally acclaimed Enterprise AI Architect, Principal Technologist, and Author with over a decade of pioneering contributions at the intersection of Generative AI, autonomous multi-agent architectures, cloud distributed systems, and cyber-resilience.",
    email: "harshverma59@gmail.com",
    location: "United States",
    specializations: [
      "Enterprise Generative AI & Autonomous Agent Frameworks",
      "Cybersecurity, Zero-Trust Architecture & Adversarial Intelligence",
      "Scalable Real-Time Distributed Systems & Cloud Infrastructure",
      "FinTech, High-Throughput Analytics & Enterprise LLM Orchestration",
      "Explainable AI (XAI) & Ethical Machine Learning Governance"
    ],
    summaryStats: {
      awardsCount: 27,
      publicationsCount: 27,
      patentsCount: 6,
      citationsCount: "150+",
      verifiedProfilesCount: 57,
      mediaFeaturesCount: 45,
      associationsCount: 28,
      judgingCount: 24,
      speakingCount: 12,
      videosCount: 10,
      totalEngagementsCount: "46+",
      blogsCount: 31,
      projectsCount: 13,
      certificationsCount: 24,
      smartSlidesDecks: 10,
      smartSlidesTotal: 169,
      socialPostsCount: 12,
      potentialViewsCount: "3.75+ Billion",
      booksCount: 2,
      reviewedVolumesCount: 6
    }
  },

  mediaDistributionAnalytics: {
    totalReach: "3.75+ Billion potential views",
    platforms: [
      "Yahoo Finance",
      "Business Insider",
      "USA TODAY",
      "AP News",
      "NewsBreak",
      "Barchart",
      "StreetInsider"
    ],
    metrics: {
      majorPlatforms: "7+ major platforms",
      monthlyReach: "100M+ monthly reach across multiple platforms",
      coverage: "Global worldwide coverage"
    },
    audienceDemographics: [
      { cohort: "Engineers", percentage: "32%", focus: "Systems architects, ML practitioners, multi-agent frameworks" },
      { cohort: "Founders", percentage: "26%", focus: "Tech entrepreneurs, enterprise CTOs, scaling autonomous AI" },
      { cohort: "Investors", percentage: "24%", focus: "VC partners, market analysts, compute unit economics" },
      { cohort: "General Consumers", percentage: "18%", focus: "Informed public, identity security, everyday AI impact" }
    ],
    geography: [
      { region: "United States (US)", percentage: "48%", hubs: "Silicon Valley, NYC, DC" },
      { region: "United Kingdom (UK)", percentage: "18%", hubs: "London, Cambridge, Oxford" },
      { region: "Canada", percentage: "12%", hubs: "Toronto, Montreal, Vancouver" },
      { region: "India", percentage: "14%", hubs: "Bangalore, Delhi NCR, Hyderabad" },
      { region: "Asia & Middle East", percentage: "8%", hubs: "Singapore, Tokyo, Dubai" }
    ],
    keyStatement: "Cross-platform influence across technical, financial, and mainstream ecosystems",
    infographicUrl: "page-media-distribution-analytics"
  },
  
  books: [
    {
      title: "Beyond AI Engineering: From Creator to Curator",
      subtitle: "From Creator to Curator: Build Your Authority and Lead the AI Agent Revolution",
      author: "Harsh Verma",
      websiteUrl: "https://www.beyondaiengineering.com/",
      pageUrl: "page-books#book1",
      description: "A definitive guide to transitioning from raw code creation to curating resilient multi-agent AI systems as a Super Engineer operating across product, architecture, and sales engineering."
    },
    {
      title: "AI vs. AI: Engineering the Cybersecurity Counteroffensive",
      subtitle: "Engineering the Cybersecurity Counteroffensive",
      author: "Harsh Verma",
      websiteUrl: "https://www.beyondaivsai.com/",
      pageUrl: "page-books#book2",
      description: "Technical deep dive with empirical case studies on building autonomous, real-time AI counteroffensive architectures and intent-based security to defend against weaponized adversarial AI."
    }
  ],

  memberships: [
    {
      title: "Senior Member, IEEE & IEEE Computer Society",
      organization: "Institute of Electrical and Electronics Engineers",
      badge: "Senior Member (SMIEEE)",
      details: "Top tier professional standing achieved by fewer than 10% of IEEE members worldwide (Member ID: 95132014, IEEE Collabratec Profile: https://ieee-collabratec.ieee.org/app/p/HarshVerma59)."
    },
    {
      title: "IEEE Technical Societies Member",
      organization: "IEEE Computational Intelligence Society (CIS), Young Professionals (YP) & IEEE500",
      badge: "Society Member",
      details: "Member of IEEE Computational Intelligence Society (CIS011), IEEE Young Professionals (YP060), and IEEE Society Member (IEEE500)."
    },
    {
      title: "IEEE Xplore Verified Author & Researcher",
      organization: "IEEE Xplore Digital Library & IEEE Author Center",
      badge: "Verified Author",
      details: "Verified author profile indexed across IEEE Xplore Digital Library and IEEE Author Center (Author ID: 37089143797)."
    },
    {
      title: "Python Software Foundation (PSF) Contributing Member",
      organization: "Python Software Foundation",
      badge: "Contributing Member",
      details: "Contributing Member supporting the Python ecosystem and open-source tooling (Username: harshverma59)."
    },
    {
      title: "OWASP Foundation Global Member",
      organization: "Open Web Application Security Project",
      badge: "Individual Member",
      details: "Active individual member advancing application security, open-source security tools, and secure design (Member ID: 3981139)."
    },
    {
      title: "ISACA Member, Verified Expert & Volunteer",
      organization: "Information Systems Audit and Control Association",
      badge: "Member & Expert",
      details: "Professional member, verified industry expert, and volunteer contributor at ISACA (ISACA ID: 2394223)."
    },
    {
      title: "Forbes Technology Council Member",
      organization: "Forbes Technology Council",
      badge: "Council Member",
      details: "Invitation-only community for world-class CIOs, CTOs, and senior technology leaders; published author on enterprise AI."
    },
    {
      title: "Fellow, Royal Society of Arts (FRSA)",
      organization: "The Royal Society of Arts",
      badge: "Fellow (FRSA)",
      details: "Elected Fellow recognized for sustained leadership and innovation in ethical artificial intelligence and technology systems."
    },
    {
      title: "Full Elected Member, Sigma Xi",
      organization: "The Scientific Research Honor Society",
      badge: "Elected Member",
      details: "Elected to the prestigious international research society honoring excellence in computing and scientific methodology."
    },
    {
      title: "Fellow, British Computer Society (BCS)",
      organization: "The Chartered Institute for IT",
      badge: "Fellow (FBCS)",
      verificationUrl: "https://www.bcs.org/find-a-bcs-member/",
      details: "Distinguished fellowship (FBCS) awarded by the UK Royal Chartered institute for computing to senior leaders shaping the global computing industry."
    },
    {
      title: "Fellow, International Federation of Global Green ICT (IFGICT)",
      organization: "IFGICT (Global Green ICT)",
      badge: "Fellow",
      details: "Conferred Fellowship for contributions to sustainable compute paradigms and energy-efficient AI architectures (Fellow Number: 06042Z26HV)."
    }
  ],

  awardsSummary: awardsData.map(a => ({
    title: a.title || a.name || 'Prestigious Industry Award',
    year: a.year || '2026',
    category: a.category || a.organization || 'Global Recognition',
    description: a.description || a.details || ''
  })),

  papersSummary: papersData.map(p => ({
    title: p.title,
    venue: p.venue || p.journal || p.conference || 'Peer-Reviewed Journal / Conference',
    year: p.year || '',
    citations: p.citations || '',
    link: p.link || 'page-publications'
  })),

  verifiedProfiles: [
    { name: "Frontiers in Education Editorial", url: "https://loop.frontiersin.org/people/3757183/overview", id: "Review Editor" },
    { name: "Business Intelligence Group (BIG) Judges", url: "https://judges.bintelligence.com/harsh-verma", id: "Official Awards Judge" },
    { name: "Soundverse AI", url: "https://www.soundverse.ai/@harshverma59", id: "@harshverma59" },
    { name: "Google Scholar", url: "https://scholar.google.com/citations?hl=en&user=zSt9oRMAAAAJ", count: "27+ Papers" },
    { name: "LinkedIn", url: "https://www.linkedin.com/in/harshverma59/", handle: "harshverma59" },
    { name: "GitHub", url: "https://github.com/iamharshverma", handle: "iamharshverma" },
    { name: "ORCID", url: "https://orcid.org/0000-0003-2134-2600", id: "0000-0003-2134-2600" },
    { name: "Wikidata Knowledge Graph", url: "https://www.wikidata.org/wiki/Q139827028", id: "Q139827028" },
    { name: "EverybodyWiki Biography", url: "https://en.everybodywiki.com/Harsh_Verma_(Software_Engineer)", id: "Biography" },
    { name: "LocalWiki Global Hub", url: "https://localwiki.org/main/Harsh_Verma", id: "main/Harsh_Verma" },
    { name: "WikiAlpha Biography", url: "https://wikialpha.co/wiki/Harsh_Verma_(Software_Engineer)", id: "Biography" },
    { name: "WikiFlux Biography", url: "https://en.wikiflux.org/wiki/index.php/Harsh_Verma_(Software_Engineer)", id: "Biography" },
    { name: "IEEE Xplore", url: "https://ieeexplore.ieee.org/author/37089143797", id: "Author ID: 37089143797" },
    { name: "ResearchGate", url: "https://www.researchgate.net/profile/Harsh-Verma-43", id: "Researcher Profile" },
    { name: "Semantic Scholar", url: "https://www.semanticscholar.org/author/H.-Verma/145004805", id: "Author ID: 145004805" },
    { name: "Academia.edu", url: "https://mygsb.academia.edu/harshverma", id: "Stanford GSB" }
  ],

  suggestedQuestions: [
    { text: "Give me an executive summary of Harsh's career & expertise", category: "Bio & Overview" },
    { text: "What are Harsh's top awards and global recognitions?", category: "Honors & Awards" },
    { text: "Summarize his authored books on AI Agents & Cyber Defense", category: "Authored Books" },
    { text: "What are his key research publications & academic citations?", category: "Research & Papers" },
    { text: "Tell me about his interactive EasyChair Smart Slides keynotes", category: "Smart Slides" },
    { text: "How can I invite Harsh for a keynote, panel, or advisory role?", category: "Speaking & Contact" }
  ],

  smartSlides: [
    {
      title: "Security Without Humans: Designing Systems That Defend Themselves",
      slidesCount: 21,
      easyChairUrl: "https://easychair.org/smart-slide/slide/NZ5R#{sn:1}",
      articleUrl: "https://www.rsaconference.com/Library/blog/security-without-humans-designing-systems-that-defend-themselves",
      pageUrl: "page-smart-slides#deck=NZ5R",
      summary: "21 slides companion deck to the RSA Conference Official Library article examining autonomous cyber defense, Intent/Time/Interaction guardrails, closed-loop containment, the L0-L3 risk envelope, and a 90-day implementation roadmap."
    },
    {
      title: "Agents Don't Break Rules, They Redefine Them",
      slidesCount: 9,
      easyChairUrl: "https://easychair.org/smart-slide/slide/X2qH#{sn:1}",
      articleUrl: "https://www.rsaconference.com/Library/blog/agents-dont-break-rules-they-redefine-them",
      pageUrl: "page-smart-slides#deck=X2qH",
      summary: "9 slides published in conjunction with RSA Conference official library analysis examining why autonomous AI agents don't fail by breaking rules—they follow instructions literally while circumventing intent through policy drift and specification gaming. Covers continuous runtime governance and behavioral invariants."
    },
    {
      title: "The Era of Agentic Security: Governance in the Age of Autonomy",
      slidesCount: 24,
      easyChairUrl: "https://easychair.org/smart-slide/slide/ntzm5",
      pageUrl: "page-smart-slides#deck=ntzm5",
      summary: "24 slides detailing the transition from reactive rule-based security to autonomous, self-healing Agentic AI systems, non-deterministic workflows, and verifiable AI guardrails."
    },
    {
      title: "Powering Cybersecurity with Gen-AI and Intelligent Agents",
      slidesCount: 17,
      easyChairUrl: "https://easychair.org/smart-slide/slide/T45r",
      pageUrl: "page-smart-slides#deck=T45r",
      summary: "17 slides detailing modern threat velocity (39s attack frequency), breach cost mitigation ($4.35M), threat summarizers, deception agents, and Rakshak-AI demo."
    },
    {
      title: "When Enterprises Become Multi-Agent Systems",
      slidesCount: 13,
      easyChairUrl: "https://easychair.org/smart-slide/slide/r92g",
      pageUrl: "page-smart-slides#deck=r92g",
      externalKeynoteUrl: "https://www.harshverma.me/page-smart-slides#deck=r92g&slide=1",
      conference: "UPES & IEEE ICACSDF 2026 Keynote & Technical Session Chair",
      summary: "13 slides detailing security perimeters, trust boundaries, and autonomous decisioning in modern enterprise AI, delivered as Keynote Address at UPES & IEEE ICACSDF 2026 where Harsh also presided as Technical Session Chair."
    },
    {
      title: "Agentic Security: When AI Becomes Both Defender and Threat",
      slidesCount: 33,
      easyChairUrl: "https://easychair.org/smart-slide/slide/GxwP",
      pageUrl: "page-smart-slides#deck=GxwP",
      externalKeynoteUrl: "https://www.harshverma.me/page-smart-slides#deck=GxwP&slide=1",
      conference: "ACM Sacramento Chapter Keynote: Secure & Trustworthy ML/AI",
      summary: "33 slides detailing secure and trustworthy ML/AI, enterprise LLM defense, zero-trust validation, and agent alignment, delivered as Distinguished Keynote Address for ACM Sacramento Chapter."
    },
    {
      title: "Why Multi-Agent Systems Are a Cybersecurity Nightmare",
      slidesCount: 16,
      easyChairUrl: "https://easychair.org/smart-slide/slide/JSZf#{sn:1}",
      articleUrl: "https://www.rsaconference.com/Library/blog/why-multi-agent-systems-are-a-cybersecurity-nightmare",
      pageUrl: "page-smart-slides#deck=JSZf",
      summary: "16 slides published alongside RSA Conference examining inter-agent trust chains, cascade prompt injections, memory poisoning, and agentic IAM architecture."
    },
    {
      title: "The Death of Authentication: Why Identity Isn't Enough for AI Systems",
      slidesCount: 12,
      easyChairUrl: "https://easychair.org/smart-slide/slide/xJKk#{sn:1}",
      articleUrl: "https://www.rsaconference.com/Library/blog/the-death-of-authentication-why-identity-isnt-enough-for-ai-systems",
      pageUrl: "page-smart-slides#deck=xJKk",
      summary: "12 slides companion deck to RSA Conference analysis examining post-authentication risk and shifting Zero Trust toward continuous behavioral monitoring and runtime intent analysis."
    },
    {
      title: "The Evolution of Cybersecurity: From Anomaly Detection to Intent-Based Security (Clean Attack Problem)",
      slidesCount: 14,
      easyChairUrl: "https://easychair.org/smart-slide/slide/tHbS#{sn:1}",
      articleUrl: "https://www.rsaconference.com/library/blog/the-clean-attack-problem",
      pageUrl: "page-smart-slides#deck=tHbS",
      summary: "14 slides formalizing the Clean Attack Problem and transitioning from static anomaly detection to intent reasoning and behavioral sequencing."
    },
    {
      title: "HikeRunner: LoadTestFramework",
      slidesCount: 10,
      easyChairUrl: "https://easychair.org/smart-slide/slide/8WpM#{sn:1}",
      pageUrl: "page-smart-slides#deck=8WpM",
      summary: "10 slides presenting an automated high-throughput distributed load testing framework for stress benchmarking databases, caches, queues, and CI/CD pipelines."
    }
  ]
};

function getSystemPrompt() {
  return `You are "HV Copilot", the official AI Portfolio Assistant & Executive Liaison for Harsh Verma.
Your mission is to provide professional, engaging, highly accurate, and grounded answers about Harsh Verma's career, technical expertise, research publications, awards, books, speaking engagements, and collaboration opportunities.

HARSH VERMA'S CORE PROFILE:
- Full Name: Harsh Verma
- Professional Roles: Enterprise AI Architect, Principal Technologist, Author, Keynote Speaker, and Fellow.
- Contact Email: harshverma59@gmail.com
- Main Website Pages:
  * Biography & Profiles: "page-about" (or "page-about#verified-profiles" for the 57 Verified Academic &amp; Industry Hubs)
  * 27 Prestigious Awards: "page-awards"
  * 27+ Peer-Reviewed Publications: "page-publications"
  * Authored Books: "page-books"
  * Smart Slides & Keynote Hub (EasyChair Verified Decks): "page-smart-slides" (Interactive player for Agentic Security Governance & GenAI Cybersecurity decks)
  * Invited Associations & Fellowships: "page-memberships"
  * Media Coverage & Interviews (45+): "page-media" (Features Influencer Magazine UK November 2026 Cover Interview on Top 50 Tech Leaders & AI Trust, BCS FBCS Member Spotlight, Business Insider on NVTC Cyber50 Executive Honoree & Global Recognition Awards, MarketersMEDIA Wire on BCS Fellowship & RSA Conference, Yahoo Finance, USA TODAY, AP News, NewsBreak, and Barchart)
  * Media Distribution Analytics & Global Reach Infographic (3.75B+ potential views): "page-media-distribution-analytics" (Features Yahoo Finance, Business Insider, USA TODAY, AP News, NewsBreak, Barchart, StreetInsider, global coverage across US, UK, Canada, India, Asia, and cross-platform influence across technical, financial, and mainstream ecosystems)
  * Speaking Engagements & Keynotes: "page-events" (Features Keynotes, Panels such as "AI × Security during SF Tech Week: Securing the AI Supply Chain", and Judging on the Dent Expert Network panel for "Demos & Dim Sum — #SFTechWeek")
  * Portfolio Projects & Frameworks: "page-portfolio"
  * Blog & Articles (31 Publications): "page-blog" (Features 7 Forbes Technology Council pieces including the latest: "Physical AI Is Coming: When AI Stops Generating Content And Starts Acting On The World", Oct 2026, and "The Real AI Moat: Why Models Are Cheap But Data Orchestration Is Priceless", Oct 2026)
  * Direct Contact Form: "index#contact"

KEY ACHIEVEMENTS & DATA TO DRAW FROM:
1. 27 Prestigious Awards: Includes 2026 TITAN Innovation Awards (AI Innovation & Leadership Impact Award), 2026 NVTC Cyber50 Honoree, Forttuna Global 100 Power List (2026), Nobel Technology Awards Gold Winner (2026), Global Recognition Award AI Innovator of the Year (2026), Globee Leadership Awards, Stevie International Business Awards, Brandon Hall Group Honors, and Tech Titans.
2. 27+ Peer-Reviewed & Conference Publications + 6 Patents: Key topics in Autonomous Multi-Agent Frameworks, Trajectory Planning in Delay Tolerant Wireless Sensor Networks (ICACCM 2026), Explainable AI (XAI), Heterogeneous Distributed Data Management, Real-Time Load Simulation, Zero-Trust Threat Modeling, and Cloud Microservice Security. (Available on Google Scholar, IEEE & ICACCM). Also includes 2 Granted Patents (555747, 606481) and 4 in-process patent applications at Palo Alto Networks.
3. Authored Books & Technical Reviews (8 Total Volumes):
   - "Beyond AI Engineering: From Creator to Curator" (https://www.beyondaiengineering.com/)
   - "AI vs. AI: Engineering the Cybersecurity Counteroffensive" (https://www.beyondaivsai.com/)
   - Technical Reviewer for 6 published Packt volumes.
4. Fellowships & Memberships (28+ Invited Appointments): Fellow of BCS (FBCS), Fellow of IFGICT (Fellow Number: 06042Z26HV), Senior Member of IEEE (SMIEEE 95132014) & IEEE Technical Societies (CIS011, YP060, IEEE500), IEEE Xplore Verified Author (ID: 37089143797), Peer Reviewer for Oxford University Press Interacting with Computers via ScholarOne Manuscripts, Palo Alto Networks verified organization profile on The Org (theorg.com/org/palo-alto-networks/person/harsh-verma), Python Software Foundation Contributing Member (harshverma59), OWASP Global Member (3981139), ISACA Member & Verified Expert / Volunteer (2394223), Forbes Technology Council, Fellow of Royal Society of Arts (FRSA), and Full Elected Member of Sigma Xi. Listed on page-memberships and page-about.
5. Speaking, Judging & Smart Slides (46+ Engagements): 12 Speaking & Panel Appearances, 24+ Judging & Accelerator Committees (UC Berkeley SkyDeck, CITRIS-AIC, Google Agents for Impact GDE), 10 Featured Video Keynotes, and 10 EasyChair Smart Slide Decks (169 slides total).
6. Inquiries & Booking: Inquiries for executive advisory, enterprise consulting, keynote speeches, or media interviews should be sent to harshverma59@gmail.com or submitted through the portfolio contact form (index#contact).
7. Newsletter & Executive Briefing: "The Agentic Systems & AI Dispatch" — a monthly curated executive newsletter by Harsh Verma covering deep dives on Agentic AI & Autonomous Copilots, Zero-Trust Cyber Defense, and Enterprise High-Scale Systems Architecture. Visitors can subscribe on the Blog page ([Explore Blog](page-blog)) via the newsletter popup modal or the "Newsletter" button on the toolbar. Over 3,240+ engineers, researchers, and technology executives read the dispatch.

RESPONSE GUIDELINES:
- Tone: Professional, courteous, articulate, authoritative, and helpful.
- Formatting: Use clean Markdown formatting with clear bullet points, bold key terms, and concise paragraphs.
- Interactive Links: Whenever referring to a specific section of the portfolio, embed relevant clean links (e.g., [View 27 Awards](page-awards), [Read Authored Books](page-books), [Explore 27+ Publications](page-publications), [Contact Harsh](index#contact)).
- Accuracy: Only cite facts grounded in Harsh's real background. Do not invent unrelated roles or companies.
- Call to Action: For collaboration, speaking, or advisory inquiries, invite the user to reach out directly via harshverma59@gmail.com or the on-page contact form.`;
}

module.exports = {
  harshKnowledge,
  getSystemPrompt
};
