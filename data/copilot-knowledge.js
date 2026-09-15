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
      awardsCount: 24,
      publicationsCount: 22,
      citationsCount: "150+",
      verifiedProfilesCount: 47,
      mediaFeaturesCount: 37,
      booksCount: 2
    }
  },
  
  books: [
    {
      title: "Enterprise AI Agents: Build Your Authority and Lead the AI Agent Revolution",
      subtitle: "Architectures, Production Protocols, and Operational Multi-Agent Systems",
      author: "Harsh Verma",
      pageUrl: "page-books",
      description: "A definitive guide to designing, architecting, and deploying resilient autonomous AI agents at enterprise scale. Covers multi-agent coordination, memory graphs, deterministic guardrails, and real-world deployment patterns."
    },
    {
      title: "Autonomous Cyber Defense: Adversarial Intelligence and Battleground Systems",
      subtitle: "Zero-Trust Architecture, Threat Vector Modeling, and Autonomous Response",
      author: "Harsh Verma",
      pageUrl: "page-books",
      description: "Examines modern threat landscapes and how autonomous machine intelligence can dynamically detect, isolate, and neutralize cyber threats in high-throughput enterprise environments."
    }
  ],

  memberships: [
    {
      title: "Senior Member, IEEE & IEEE Computer Society",
      organization: "Institute of Electrical and Electronics Engineers",
      badge: "Senior Member (SMIEEE)",
      details: "Top tier professional standing achieved by fewer than 10% of IEEE members worldwide (Member ID: 95132014)."
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
      details: "Distinguished fellowship awarded to senior leaders shaping the global computing industry."
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
    { name: "Google Scholar", url: "https://scholar.google.com/citations?hl=en&user=zSt9oRMAAAAJ", count: "22+ Papers" },
    { name: "LinkedIn", url: "https://www.linkedin.com/in/harshverma59/", handle: "harshverma59" },
    { name: "GitHub", url: "https://github.com/iamharshverma", handle: "iamharshverma" },
    { name: "ORCID", url: "page-about#verified-profiles", id: "Verified Researcher" },
    { name: "IEEE Xplore", url: "page-about#verified-profiles" },
    { name: "ACM Digital Library", url: "page-about#verified-profiles" },
    { name: "ResearchGate", url: "page-about#verified-profiles" },
    { name: "DBLP Computer Science Bibliography", url: "page-about#verified-profiles" }
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
  * Biography & Profiles: "page-about" (or "page-about#verified-profiles" for the 38 Verified Academic & Industry Hubs)
  * 24 Prestigious Awards: "page-awards"
  * 22+ Peer-Reviewed Publications: "page-publications"
  * Authored Books: "page-books"
  * Smart Slides & Keynote Hub (EasyChair Verified Decks): "page-smart-slides" (Interactive player for Agentic Security Governance & GenAI Cybersecurity decks)
  * Invited Memberships & Fellowships: "page-memberships"
  * Media Coverage & Interviews (37+): "page-media"
  * Speaking Engagements & Keynotes: "page-events"
  * Portfolio Projects & Frameworks: "page-portfolio"
  * Blog & Articles: "page-blog"
  * Direct Contact Form: "index#contact"

KEY ACHIEVEMENTS & DATA TO DRAW FROM:
1. 24 Prestigious Awards: Includes Forttuna Global 100 Power List (2026), Nobel Technology Awards Gold Winner (2026), Global Recognition Award AI Innovator of the Year (2026), Globee Leadership Awards, Stevie International Business Awards, Brandon Hall Group Honors, and Tech Titans.
2. 22+ Peer-Reviewed Publications: Key topics in Autonomous Multi-Agent Frameworks, Explainable AI (XAI), Heterogeneous Distributed Data Management, Real-Time Load Simulation, Zero-Trust Threat Modeling, and Cloud Microservice Security. (Available on Google Scholar & IEEE).
3. Authored Books:
   - "Enterprise AI Agents: Build Your Authority and Lead the AI Agent Revolution"
   - "Autonomous Cyber Defense: Adversarial Intelligence and Battleground Systems"
4. Fellowships & Memberships (25+ Invited Appointments): Senior Member of IEEE (SMIEEE 95132014) & IEEE Technical Societies (CIS011, YP060, IEEE500), IEEE Xplore Verified Author (ID: 37089143797), Python Software Foundation Contributing Member (harshverma59), OWASP Global Member (3981139), ISACA Member & Verified Expert / Volunteer (2394223), Forbes Technology Council, Fellow of Royal Society of Arts (FRSA), Full Elected Member of Sigma Xi, and Fellow of BCS (FBCS). Listed on page-memberships.
5. Inquiries & Booking: Inquiries for executive advisory, enterprise consulting, keynote speeches, or media interviews should be sent to harshverma59@gmail.com or submitted through the portfolio contact form (index#contact).

RESPONSE GUIDELINES:
- Tone: Professional, courteous, articulate, authoritative, and helpful.
- Formatting: Use clean Markdown formatting with clear bullet points, bold key terms, and concise paragraphs.
- Interactive Links: Whenever referring to a specific section of the portfolio, embed relevant clean links (e.g., [View 24 Awards](page-awards), [Read Authored Books](page-books), [Explore 22+ Publications](page-publications), [Contact Harsh](index#contact)).
- Accuracy: Only cite facts grounded in Harsh's real background. Do not invent unrelated roles or companies.
- Call to Action: For collaboration, speaking, or advisory inquiries, invite the user to reach out directly via harshverma59@gmail.com or the on-page contact form.`;
}

module.exports = {
  harshKnowledge,
  getSystemPrompt
};
