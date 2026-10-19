#!/usr/bin/env python3
"""
scripts/create_board_bio_pdf.py
Dependency-free, standards-compliant PDF 1.4 generator for Harsh Verma's Executive Board Biography.
Outputs: files/Harsh_Verma_Board_Biography.pdf
"""

import os

class SimplePDF:
    def __init__(self):
        self.objects = []
        self.pages = []
        self.fonts = {}
        
    def add_object(self, content):
        self.objects.append(content)
        return len(self.objects)  # 1-indexed object ID
        
    def build(self):
        # 1: Catalog, 2: Pages
        catalog_id = 1
        pages_id = 2
        font_regular_id = 3
        font_bold_id = 4
        
        # Reserved slots
        self.objects = [None, None, None, None]
        
        # Fonts
        self.objects[font_regular_id - 1] = "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>"
        self.objects[font_bold_id - 1] = "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>"
        
        page_ids = []
        for p_stream in self.pages:
            stream_bytes = p_stream.encode('latin1')
            stream_obj = f"<< /Length {len(stream_bytes)} >>\nstream\n{p_stream}\nendstream"
            stream_id = self.add_object(stream_obj)
            
            page_obj = f"""<<
  /Type /Page
  /Parent {pages_id} 0 R
  /MediaBox [0 0 612 792]
  /Contents {stream_id} 0 R
  /Resources <<
    /Font <<
      /F1 {font_regular_id} 0 R
      /F2 {font_bold_id} 0 R
    >>
  >>
>>"""
            p_id = self.add_object(page_obj)
            page_ids.append(p_id)
            
        # Fill Catalog & Pages
        self.objects[catalog_id - 1] = f"<< /Type /Catalog /Pages {pages_id} 0 R >>"
        kids_str = " ".join([f"{pid} 0 R" for pid in page_ids])
        self.objects[pages_id - 1] = f"<< /Type /Pages /Kids [{kids_str}] /Count {len(page_ids)} >>"
        
        # Serialize PDF
        out = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
        offsets = []
        for i, obj in enumerate(self.objects):
            offsets.append(len(out))
            obj_bytes = obj.encode('latin1') if isinstance(obj, str) else obj
            out.extend(f"{i + 1} 0 obj\n".encode('latin1'))
            out.extend(obj_bytes)
            out.extend(b"\nendobj\n")
            
        xref_offset = len(out)
        out.extend(f"xref\n0 {len(self.objects) + 1}\n0000000000 65535 f \n".encode('latin1'))
        for off in offsets:
            out.extend(f"{off:010d} 00000 n \n".encode('latin1'))
            
        out.extend(f"""trailer
<<
  /Size {len(self.objects) + 1}
  /Root {catalog_id} 0 R
>>
startxref
{xref_offset}
%%EOF
""".encode('latin1'))
        return bytes(out)

def escape_pdf_str(text):
    return text.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')

def build_board_dossier():
    pdf = SimplePDF()
    
    # ==========================
    # PAGE 1
    # ==========================
    s1 = []
    
    # Navy Header Background (y: 692 to 792)
    s1.append("0.059 0.090 0.165 rg")  # Navy #0f172a
    s1.append("0 692 612 100 re f")
    
    # Header Accent line
    s1.append("0.851 0.467 0.024 rg")  # Gold #d97706
    s1.append("0 689 612 3 re f")
    
    # Header Text
    s1.append("BT")
    s1.append("/F2 20 Tf")
    s1.append("1 1 1 rg")
    s1.append("40 750 Td")
    s1.append("(HARSH VERMA) Tj")
    s1.append("ET")
    
    s1.append("BT")
    s1.append("/F2 9.5 Tf")
    s1.append("0.961 0.620 0.043 rg")  # Gold
    s1.append("40 734 Td")
    s1.append("(BOARD & STRATEGIC ADVISORY | AI GOVERNANCE & CYBERSECURITY) Tj")
    s1.append("ET")
    
    s1.append("BT")
    s1.append("/F1 8.5 Tf")
    s1.append("0.85 0.90 1 rg")
    s1.append("40 718 Td")
    s1.append("(Forbes Tech Council | BCS Fellow \\(FBCS\\) | IEEE Senior Member | Principal AI Engineer @ Palo Alto Networks) Tj")
    s1.append("ET")
    
    s1.append("BT")
    s1.append("/F1 7.5 Tf")
    s1.append("0.70 0.75 0.85 rg")
    s1.append("40 704 Td")
    s1.append("(San Francisco Bay Area, CA  *  harshverma59@gmail.com  *  linkedin.com/in/harshverma59  *  harshverma.me/advisory) Tj")
    s1.append("ET")
    
    # Section 1: Executive Summary
    y = 660
    s1.append("BT /F2 10.5 Tf 0.145 0.388 0.922 rg 40 " + str(y) + " Td (EXECUTIVE SUMMARY & BOARDROOM VALUE PROPOSITION) Tj ET")
    y -= 4
    s1.append(f"0.886 0.910 0.941 RG 1 w 40 {y} m 572 {y} l S")
    y -= 14
    
    summary_lines = [
        "Harsh Verma is an accomplished technology executive, strategic advisor, and AI governance leader bringing over 15 years",
        "of experience scaling high-concurrency distributed systems, autonomous multi-agent networks, and zero-trust cybersecurity",
        "perimeters. As Principal Software Engineer in AI at Palo Alto Networks, Forbes Technology Council member, and Fellow of the",
        "British Computer Society (FBCS), Harsh provides startup advisory boards, technology advisory councils, and corporate governance",
        "initiatives with decisive technical foresight, regulatory compliance rigor (EU AI Act, NIST AI RMF), and defensible architecture validation."
    ]
    for line in summary_lines:
        s1.append(f"BT /F1 8.2 Tf 0.2 0.25 0.33 rg 40 {y} Td ({escape_pdf_str(line)}) Tj ET")
        y -= 12
        
    y -= 8
    
    # Metrics Box
    s1.append("0.972 0.980 0.988 rg 40 " + str(y - 32) + " 532 36 re f")
    s1.append("0.886 0.910 0.941 RG 1 w 40 " + str(y - 32) + " 532 36 re S")
    
    metrics = [
        ("15+ Years", "Tech Leadership"),
        ("120+ Startups", "Evaluated & Diligenced"),
        ("10+ Programs", "SkyDeck, Techstars, etc."),
        ("27+ Papers", "Peer-Reviewed Research"),
        ("6 Patents", "Systems Architecture")
    ]
    col_w = 532 / len(metrics)
    for idx, (m_val, m_lbl) in enumerate(metrics):
        mx = 40 + idx * col_w + 10
        s1.append(f"BT /F2 10 Tf 0.059 0.090 0.165 rg {mx} {y - 14} Td ({m_val}) Tj ET")
        s1.append(f"BT /F1 7 Tf 0.392 0.455 0.545 rg {mx} {y - 25} Td ({m_lbl}) Tj ET")
        
    y -= 48
    
    # Section 2: Areas of Strategic Expertise (6 Pillars)
    s1.append(f"BT /F2 10.5 Tf 0.145 0.388 0.922 rg 40 {y} Td (AREAS OF STRATEGIC EXPERTISE) Tj ET")
    y -= 4
    s1.append(f"0.886 0.910 0.941 RG 1 w 40 {y} m 572 {y} l S")
    y -= 15
    
    competencies = [
        ("1. AI Strategy & Enterprise Transformation", "Advising C-suite teams on adoption roadmaps, token unit economics, multi-cloud inference routing, and transitioning brittle prototypes into resilient, sovereign production architectures."),
        ("2. Cybersecurity & Enterprise Risk Governance", "Architecting zero-trust behavioral authorization, ephemeral agent execution sandboxing, defense against prompt injection, and continuous API security monitoring for autonomous systems."),
        ("3. AI Governance & Responsible Innovation", "Structuring institutional AI governance frameworks, human-in-the-loop escalation controls, and compliance alignment with the EU AI Act, NIST AI Risk Management Framework, and SEC disclosures."),
        ("4. Venture & Technical Due Diligence", "Evaluating proprietary data moats, underlying software craftsmanship, vendor switching costs, model wrapper risks, and intellectual property defensibility for venture capital and private equity investors."),
        ("5. Startup Growth & Technology Leadership", "Mentoring venture-backed founders through architectural scaling milestones, technical debt triage, engineering talent recruitment, and board-level technology roadmapping."),
        ("6. Agentic AI & Emerging Technology", "Guiding organizations on stateful agent deliberation networks, long-context memory stores, safe tool-use protocols, and distributed streaming pipeline architectures.")
    ]
    
    for title, desc in competencies:
        s1.append(f"BT /F2 8.5 Tf 0.059 0.090 0.165 rg 40 {y} Td ({escape_pdf_str(title)}) Tj ET")
        y -= 11
        s1.append(f"BT /F1 7.8 Tf 0.278 0.333 0.412 rg 40 {y} Td ({escape_pdf_str(desc)}) Tj ET")
        y -= 16
        
    y -= 6
    
    # Section 3: Documented Case Studies
    s1.append(f"BT /F2 10.5 Tf 0.145 0.388 0.922 rg 40 {y} Td (DOCUMENTED ADVISORY INTERVENTIONS \\(CASE STUDIES\\)) Tj ET")
    y -= 4
    s1.append(f"0.886 0.910 0.941 RG 1 w 40 {y} m 572 {y} l S")
    y -= 14
    
    case_studies = [
        ("Case 1: Venture Moat Strategy (Series Seed)", "Challenge: Founder faced rapid commoditization due to dependence on standard LLM wrappers.", "Outcome: Re-architected system toward proprietary streaming data capture and custom evaluation benchmarks; reduced vendor reliance by 65% and successfully closed institutional Series A."),
        ("Case 2: Autonomous Agent Privilege & Security (Enterprise Scale-Up)", "Challenge: Multi-agent automation system was executing privileged tool calls with broad unisolated database writes.", "Outcome: Implemented zero-trust behavioral authorization and ephemeral MCP tool sandboxes; cleared enterprise SOC2/CISO audits and unlocked Fortune 500 contracts.")
    ]
    
    for c_title, c_chal, c_out in case_studies:
        s1.append(f"BT /F2 8.2 Tf 0.059 0.090 0.165 rg 40 {y} Td ({escape_pdf_str(c_title)}) Tj ET")
        y -= 10
        s1.append(f"BT /F1 7.5 Tf 0.3 0.35 0.45 rg 40 {y} Td ({escape_pdf_str(c_chal)}) Tj ET")
        y -= 10
        s1.append(f"BT /F1 7.5 Tf 0.020 0.588 0.412 rg 40 {y} Td ({escape_pdf_str(c_out)}) Tj ET")
        y -= 14

    # Footer Page 1
    s1.append("BT /F1 7.5 Tf 0.6 0.65 0.7 rg 40 24 Td (Harsh Verma  *  Executive Board Biography & Strategic Advisory Dossier  *  Page 1 of 2) Tj ET")
    
    pdf.pages.append("\n".join(s1))
    
    # ==========================
    # PAGE 2
    # ==========================
    s2 = []
    
    # Mini Header Page 2
    s2.append("BT /F2 9.5 Tf 0.059 0.090 0.165 rg 40 755 Td (HARSH VERMA  |  EXECUTIVE BOARD BIOGRAPHY \\(CONTINUED\\)) Tj ET")
    s2.append("0.145 0.388 0.922 RG 1.5 w 40 748 m 572 748 l S")
    
    y2 = 726
    
    # Governance Creed
    s2.append(f"BT /F2 10.5 Tf 0.145 0.388 0.922 rg 40 {y2} Td (GOVERNANCE & ADVISORY PHILOSOPHY) Tj ET")
    y2 -= 4
    s2.append(f"0.886 0.910 0.941 RG 1 w 40 {y2} m 572 {y2} l S")
    y2 -= 16
    
    s2.append(f"BT /F2 9.5 Tf 0.851 0.467 0.024 rg 40 {y2} Td (\\\"Technology creates opportunity. Governance turns that opportunity into sustainable value.\\\") Tj ET")
    y2 -= 16
    
    gov_pillars = [
        ("Strategic Foresight:", "Anticipating architectural inflection points and market shifts before consensus."),
        ("Responsible Innovation:", "Balancing product velocity with strict data isolation, safety telemetry, and corporate reputation."),
        ("Enterprise Resilience:", "Designing systems resilient to adversarial attacks, supply-chain risks, and non-deterministic failures."),
        ("Long-Term Value Creation:", "Prioritizing sovereign tech assets, durable unit economics, and governance accountability.")
    ]
    for p_title, p_desc in gov_pillars:
        s2.append(f"BT /F2 8.2 Tf 0.059 0.090 0.165 rg 40 {y2} Td ({escape_pdf_str(p_title)}) Tj ET")
        s2.append(f"BT /F1 8.2 Tf 0.278 0.333 0.412 rg 160 {y2} Td ({escape_pdf_str(p_desc)}) Tj ET")
        y2 -= 14
        
    y2 -= 10
    
    # Professional Distinctions
    s2.append(f"BT /F2 10.5 Tf 0.145 0.388 0.922 rg 40 {y2} Td (PROFESSIONAL DISTINCTION & AFFILIATIONS) Tj ET")
    y2 -= 4
    s2.append(f"0.886 0.910 0.941 RG 1 w 40 {y2} m 572 {y2} l S")
    y2 -= 16
    
    distinctions = [
        ("Forbes Technology Council:", "Official Member & Contributing Executive Author on AI & Cybersecurity Strategy"),
        ("British Computer Society (BCS):", "Fellow (FBCS) - Recognized for senior professional contribution and leadership in computing"),
        ("IEEE (Senior Member):", "Elevated to the Top 8% of worldwide engineering professional membership (SMIEEE)"),
        ("Palo Alto Networks:", "Principal Software Engineer in AI & Distributed Systems Architecture"),
        ("UC Berkeley SkyDeck & Techstars:", "Keynote Speaker, Technical Mentor & Startup Cohort Evaluator"),
        ("Scholarly Record:", "27+ Peer-Reviewed Research Papers published in IEEE, ACM, Springer & international proceedings; 6 Patents")
    ]
    for d_title, d_desc in distinctions:
        s2.append(f"BT /F2 8.2 Tf 0.059 0.090 0.165 rg 40 {y2} Td ({escape_pdf_str(d_title)}) Tj ET")
        s2.append(f"BT /F1 8.2 Tf 0.278 0.333 0.412 rg 200 {y2} Td ({escape_pdf_str(d_desc)}) Tj ET")
        y2 -= 14
        
    y2 -= 10
    
    # Board Mandates
    s2.append(f"BT /F2 10.5 Tf 0.145 0.388 0.922 rg 40 {y2} Td (BOARD & ADVISORY ENGAGEMENT MANDATES) Tj ET")
    y2 -= 4
    s2.append(f"0.886 0.910 0.941 RG 1 w 40 {y2} m 572 {y2} l S")
    y2 -= 16
    
    mandates = [
        ("Startup Advisory Boards (Series A-C):", "Quarterly strategy reviews, architectural sounding board, investor syndicate access, FAST agreements."),
        ("Technology Advisory Councils:", "Advisory for C-suite on AI roadmap prioritization, multi-cloud strategy, and technological de-risking."),
        ("AI Governance & Risk Committees:", "Fiduciary counsel on autonomous deployments, EU AI Act compliance, and automated eval harnesses."),
        ("Cybersecurity Advisory Roles:", "Boardroom cyber risk oversight, zero-trust transformations, and CISO executive advisory sessions."),
        ("VC / PE Technical Due Diligence:", "Deep technical audits, data moat evaluations, and engineering velocity analysis for investments."),
        ("Independent Corporate Director:", "Independent board seat bringing frontier AI fluency, security governance, and technical judgment.")
    ]
    for m_title, m_desc in mandates:
        s2.append(f"BT /F2 8.2 Tf 0.059 0.090 0.165 rg 40 {y2} Td ({escape_pdf_str(m_title)}) Tj ET")
        y2 -= 10
        s2.append(f"BT /F1 7.8 Tf 0.3 0.35 0.45 rg 40 {y2} Td ({escape_pdf_str(m_desc)}) Tj ET")
        y2 -= 14
        
    y2 -= 12
    
    # Contact Callout Box
    s2.append(f"0.941 0.957 1 rg 40 {y2 - 46} 532 46 re f")
    s2.append(f"0.749 0.859 0.996 RG 1 w 40 {y2 - 46} 532 46 re S")
    
    s2.append(f"BT /F2 9 Tf 0.145 0.388 0.922 rg 52 {y2 - 14} Td (INITIATE A CONFIDENTIAL BOARD OR ADVISORY DISCUSSION) Tj ET")
    s2.append(f"BT /F1 7.5 Tf 0.3 0.35 0.45 rg 52 {y2 - 25} Td (All inquiries from nomination committees, venture partners, and executive search firms are handled under strict confidentiality.) Tj ET")
    s2.append(f"BT /F2 8 Tf 0.059 0.090 0.165 rg 52 {y2 - 37} Td (Direct Contact: harshverma59@gmail.com   |   LinkedIn: linkedin.com/in/harshverma59   |   Web: harshverma.me/advisory) Tj ET")
    
    # Footer Page 2
    s2.append("BT /F1 7.5 Tf 0.6 0.65 0.7 rg 40 24 Td (Harsh Verma  *  Executive Board Biography & Strategic Advisory Dossier  *  Page 2 of 2  *  \\(c\\) 2026 Harsh Verma) Tj ET")
    
    pdf.pages.append("\n".join(s2))
    
    pdf_bytes = pdf.build()
    
    out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "files")
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "Harsh_Verma_Board_Biography.pdf")
    with open(out_file, "wb") as f:
        f.write(pdf_bytes)
        
    print(f"Successfully generated {out_file} ({len(pdf_bytes)} bytes)")

if __name__ == "__main__":
    build_board_dossier()
