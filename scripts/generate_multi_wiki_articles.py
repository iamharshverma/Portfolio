#!/usr/bin/env python3
"""
scripts/generate_multi_wiki_articles.py
=======================================
Generates tailored biographical articles and deployment packages for:
  1. WikiAlpha (https://wikialpha.co/wiki/Harsh_Verma_(Software_Engineer))
  2. WikiFlux (https://en.wikiflux.org/wiki/index.php/Harsh_Verma_(Software_Engineer))
  3. LocalWiki (Santa Clara & Dallas Community editions)
  4. Universal MediaWiki XML Export (Special:Import compatible)
"""

import os
import re
import json
import html as html_lib
from datetime import datetime, timezone

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

KG_PATH = os.path.join(DATA_DIR, "knowledge-graph.json")


def load_kg():
    if os.path.exists(KG_PATH):
        with open(KG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def generate_wikialpha_wikitext(kg):
    """Generate wikitext formatted specifically for WikiAlpha's MediaWiki 1.42 engine."""
    with open(os.path.join(DATA_DIR, "everybodywiki-article.wiki"), "r", encoding="utf-8") as f:
        ew_wiki = f.read()

    # WikiAlpha supports standard MediaWiki syntax with Category:American computer scientists, etc.
    # Add WikiAlpha-specific tags
    wikialpha_wiki = ew_wiki.replace(
        "== References ==",
        "== External Links ==\n"
        "* [https://www.harshverma.me/ Harsh Verma Official Portfolio & Knowledge Graph Hub]\n"
        "* [https://www.wikidata.org/wiki/Q139827028 Harsh Verma on Wikidata (Q139827028)]\n"
        "* [https://en.everybodywiki.com/Harsh_Verma_(Software_Engineer) Harsh Verma on EverybodyWiki]\n"
        "* [https://en.wikiflux.org/wiki/index.php/Harsh_Verma_(Software_Engineer) Harsh Verma on WikiFlux]\n"
        "* [https://scholar.google.com/citations?user=zSt9oRMAAAAJ Harsh Verma on Google Scholar]\n"
        "* [https://orcid.org/0000-0003-2134-2600 Harsh Verma ORCID Registry]\n"
        "* [https://www.linkedin.com/in/harshverma59/ Harsh Verma on LinkedIn]\n\n"
        "== References =="
    )
    if "[[Category:WikiAlpha]]" not in wikialpha_wiki:
        wikialpha_wiki += "\n[[Category:Articles created via WikiAlpha Engine]]\n[[Category:Palo Alto Networks people]]\n"
    return wikialpha_wiki


def generate_wikiflux_wikitext(kg):
    """Generate wikitext formatted specifically for WikiFlux's MediaWiki 1.39 engine with SEO extension."""
    with open(os.path.join(DATA_DIR, "everybodywiki-article.wiki"), "r", encoding="utf-8") as f:
        ew_wiki = f.read()

    # Extract body after infobox
    infobox_end = ew_wiki.find("}}\n\n'''Harsh Verma'''")
    if infobox_end != -1:
        body = ew_wiki[infobox_end + 3:]
    else:
        body = ew_wiki

    seo_block = (
        "{{#seo:\n"
        "|title= Harsh Verma (Software Engineer) - WikiFlux Biography\n"
        "|title_mode= append\n"
        "|keywords= Harsh Verma, Harsh Verma Software Engineer, Harsh Verma Palo Alto Networks, Harsh Verma AI Architect, Harsh Verma author, Harsh Verma wikiflux, Harsh Verma biography\n"
        "|description= Harsh Verma is an internationally recognized Principal Software Engineer in AI at Palo Alto Networks, enterprise AI architect, author, keynote speaker, and computer science researcher.\n"
        "|image= Harsh Verma Software Engineer.jpg\n"
        "|image_alt= Harsh Verma Software Engineer\n"
        "}}\n"
    )

    infow_block = (
        "{{Infow\n"
        "|title= [[Harsh Verma]][[file:Verified.png]]\n"
        "|image= [[Harsh Verma Software Engineer.jpg]]\n"
        "|caption= Harsh Verma, Principal AI Software Engineer, Author & Keynote Speaker\n"
        "|nationality= Indian\n"
        "|profession= * Principal Software Engineer (AI)\n"
        "* Enterprise AI Architect\n"
        "* Author & Keynote Speaker\n"
        "* Computer Science Researcher\n"
        "|organization= [[Palo Alto Networks]]\n"
        "|almamater= * [[Stanford University]]\n"
        "* [[University of Texas at Dallas]] (M.S. CS)\n"
        "* [[Uttarakhand Technical University]] (B.Tech CSE)\n"
        "|knownfor= * Enterprise Agentic AI Architectures\n"
        "* Autonomous Cyber Defense\n"
        "* Multi-Agent Systems\n"
        "* Explainable AI (XAI)\n"
        "|notableworks= * ''Beyond AI Engineering: From Creator to Curator'' (2025)\n"
        "* ''AI vs. AI: Engineering the Cybersecurity Counteroffensive'' (2026)\n"
        "|awards= * Forttuna Global 100 Power List (2026)\n"
        "* Nobel Technology Awards Gold Winner (2026)\n"
        "* TITAN Innovation Award (2026)\n"
        "* NVTC Cyber50 Honoree (2026)\n"
        "* Global Recognition Award (2026)\n"
        "* Marquis Who's Who in America\n"
        "|website= [https://www.harshverma.me/ https://www.harshverma.me/]\n"
        "|twitter= harshverma59\n"
        "|facebook= harshverma59\n"
        "|instagram= aiwithharsh\n"
        "|linkedin= /in/harshverma59/\n"
        "}}\n\n"
    )

    wikiflux_wiki = seo_block + infow_block + body
    if "[[Category:WikiFlux Biography]]" not in wikiflux_wiki:
        wikiflux_wiki += "\n[[Category:WikiFlux Biography]]\n[[Category:Software Engineers]]\n[[Category:Artificial Intelligence Researchers]]\n"
    return wikiflux_wiki


def generate_localwiki_santaclara(kg):
    """Generate LocalWiki Santa Clara / Silicon Valley article HTML."""
    return """<div class="localwiki-entry" itemscope itemtype="https://schema.org/Person">
    <h2>Harsh Verma</h2>
    <p><strong>Harsh Verma</strong> is a Silicon Valley software engineering leader, Principal Software Engineer in Artificial Intelligence at <strong>Palo Alto Networks</strong> (headquartered at 3000 Tannery Way, Santa Clara, CA), author, keynote speaker, and computer science researcher.</p>

    <div class="infobox float-right p-3 mb-3 border bg-light" style="max-width: 340px;">
        <img src="https://www.harshverma.me/images/harsh/Harsh_portfolio_pic.png" alt="Harsh Verma" class="img-fluid rounded mb-2" />
        <p class="font-weight-bold text-center mb-1">Harsh Verma</p>
        <p class="small text-muted text-center">Principal AI Software Engineer, Palo Alto Networks</p>
        <hr/>
        <ul class="list-unstyled small mb-0">
            <li><strong>Location:</strong> Santa Clara, California / San Francisco Bay Area</li>
            <li><strong>Employer:</strong> Palo Alto Networks (Santa Clara, CA)</li>
            <li><strong>Education:</strong> Stanford University (Graduate Certificate in AI &amp; Executive Leadership); University of Texas at Dallas (M.S. CS)</li>
            <li><strong>Key Books:</strong> <em>Beyond AI Engineering: From Creator to Curator</em>; <em>AI vs. AI: Engineering the Cybersecurity Counteroffensive</em></li>
            <li><strong>Website:</strong> <a href="https://www.harshverma.me/" target="_blank">harshverma.me</a></li>
        </ul>
    </div>

    <h3>Silicon Valley &amp; Bay Area Leadership</h3>
    <p>Based in the San Francisco Bay Area, Verma leads architecture and development of autonomous multi-agent systems, deterministic AI security guardrails, and enterprise threat defense platforms at Palo Alto Networks. He completed executive graduate studies in Artificial Intelligence &amp; Executive Leadership at <strong>Stanford University</strong> via the Stanford Center for Professional Development.</p>
    
    <p>In the broader California tech ecosystem, Verma serves as a Global Advisor at <strong>UC Berkeley SkyDeck</strong>, advising accelerator-backed AI startups on distributed infrastructure, model orchestration, and enterprise go-to-market architecture. He also contributes regular strategic columns to the <em>Forbes Technology Council</em> and keynotes enterprise cybersecurity forums including the RSA Conference.</p>

    <h3>Research, Publications &amp; Honors</h3>
    <p>Verma has published over 27 peer-reviewed papers across IEEE, Springer Nature, and international journals with 150+ academic citations, focusing on agentic workflows, adversarial machine learning, and explainable AI (XAI). In 2026, he was named to the Forttuna Global 100 Power List, received the Nobel Technology Gold Award, the TITAN Innovation Award, and is recognized in <em>Marquis Who's Who in America</em>.</p>

    <h3>Local Connections &amp; Venues</h3>
    <ul>
        <li><strong>Palo Alto Networks HQ:</strong> 3000 Tannery Way, Santa Clara, CA 95054</li>
        <li><strong>Stanford University:</strong> Stanford Center for Professional Development, Stanford, CA</li>
        <li><strong>UC Berkeley SkyDeck:</strong> 2150 Shattuck Ave, Berkeley, CA 94704</li>
        <li><strong>San Francisco Bay Area Tech Community:</strong> IEEE Santa Clara Valley Section, RSA Conference San Francisco</li>
    </ul>

    <h3>External Links</h3>
    <ul>
        <li><a href="https://www.harshverma.me/">Harsh Verma Official Portfolio</a></li>
        <li><a href="https://theorg.com/org/palo-alto-networks/person/harsh-verma">The Org: Harsh Verma at Palo Alto Networks</a></li>
        <li><a href="https://www.wikidata.org/wiki/Q139827028">Wikidata: Harsh Verma (Q139827028)</a></li>
        <li><a href="https://en.everybodywiki.com/Harsh_Verma_(Software_Engineer)">EverybodyWiki Biography</a></li>
    </ul>
</div>"""


def generate_localwiki_dallas(kg):
    """Generate LocalWiki Dallas / North Texas article HTML."""
    return """<div class="localwiki-entry" itemscope itemtype="https://schema.org/Person">
    <h2>Harsh Verma</h2>
    <p><strong>Harsh Verma</strong> is a University of Texas at Dallas alumnus, computer scientist, author, and enterprise AI engineering leader.</p>

    <div class="infobox float-right p-3 mb-3 border bg-light" style="max-width: 340px;">
        <img src="https://www.harshverma.me/images/harsh/Harsh_portfolio_pic.png" alt="Harsh Verma" class="img-fluid rounded mb-2" />
        <p class="font-weight-bold text-center mb-1">Harsh Verma</p>
        <p class="small text-muted text-center">UT Dallas Alumnus (M.S. Computer Science)</p>
        <hr/>
        <ul class="list-unstyled small mb-0">
            <li><strong>Dallas Connection:</strong> University of Texas at Dallas (Richardson, TX)</li>
            <li><strong>Degree:</strong> Master of Science in Computer Science</li>
            <li><strong>School:</strong> Erik Jonsson School of Engineering and Computer Science</li>
            <li><strong>Current Role:</strong> Principal Software Engineer (AI) at Palo Alto Networks</li>
            <li><strong>Website:</strong> <a href="https://www.harshverma.me/" target="_blank">harshverma.me</a></li>
        </ul>
    </div>

    <h3>UT Dallas &amp; North Texas Education</h3>
    <p>Verma graduated from the <strong>University of Texas at Dallas</strong> in Richardson, Texas, earning his Master of Science in Computer Science from the Erik Jonsson School of Engineering and Computer Science. His academic focus centered on intelligent systems, distributed database architecture, and machine learning algorithms.</p>
    
    <p>During his time at UT Dallas, Verma participated in the UTDesign program in collaboration with Reliance Jio, engineering real-time analytics load simulation frameworks that were subsequently published in international computing journals.</p>

    <h3>Professional Trajectory</h3>
    <p>Following his graduate work in North Texas, Verma engineered real-time distributed platforms across multiple enterprise environments before becoming Principal Software Engineer in AI at Palo Alto Networks. He maintains active ties with academic research institutions across Texas and the United States.</p>

    <h3>External Links</h3>
    <ul>
        <li><a href="https://www.harshverma.me/">Harsh Verma Official Portfolio</a></li>
        <li><a href="https://www.utdallas.edu/">University of Texas at Dallas</a></li>
        <li><a href="https://www.wikidata.org/wiki/Q139827028">Wikidata: Harsh Verma (Q139827028)</a></li>
    </ul>
</div>"""


def generate_localwiki_main(kg):
    """Generate comprehensive, encyclopedic HTML for LocalWiki Main Global Hub (https://localwiki.org/main/Harsh_Verma)."""
    return """<div class="localwiki-entry" itemscope itemtype="https://schema.org/Person">
    <h2>Harsh Verma</h2>
    <p><strong>Harsh Verma</strong> is an internationally recognized computer scientist, Principal Software Engineer in Artificial Intelligence at <strong>Palo Alto Networks</strong>, enterprise AI systems architect, author, keynote speaker, and researcher.</p>

    <div class="infobox float-right p-3 mb-3 border bg-light shadow-sm" style="max-width: 350px; background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px;">
        <img src="https://www.harshverma.me/images/harsh/Harsh_portfolio_pic.png" alt="Harsh Verma" class="img-fluid rounded mb-2 w-100" />
        <p class="font-weight-bold text-center mb-1" style="font-size: 16px;">Harsh Verma</p>
        <p class="small text-muted text-center mb-2">Principal AI Software Engineer &amp; Author</p>
        <hr style="margin: 8px 0;"/>
        <ul class="list-unstyled small mb-0" style="line-height: 1.6;">
            <li><strong>Full Name:</strong> Mr. Harsh Verma</li>
            <li><strong>Nationality:</strong> Indian</li>
            <li><strong>Current Role:</strong> Principal Software Engineer (AI)</li>
            <li><strong>Employer:</strong> <a href="https://www.paloaltonetworks.com/" target="_blank">Palo Alto Networks</a> (Santa Clara, CA)</li>
            <li><strong>Education:</strong>
                <ul>
                    <li>Stanford University (Graduate Certificate in AI &amp; Executive Leadership)</li>
                    <li>University of Texas at Dallas (M.S. in Computer Science)</li>
                    <li>Uttarakhand Technical University (B.Tech in CSE)</li>
                </ul>
            </li>
            <li><strong>Notable Books:</strong>
                <ul>
                    <li><em>Beyond AI Engineering: From Creator to Curator</em> (2025)</li>
                    <li><em>AI vs. AI: Engineering the Cybersecurity Counteroffensive</em> (2026)</li>
                </ul>
            </li>
            <li><strong>Key Honors:</strong> Forttuna Global 100 Power List (2026), Nobel Technology Awards Gold Winner (2026), TITAN Innovation Award (2026), NVTC Cyber50, Marquis Who's Who in America</li>
            <li><strong>Invited Fellowships:</strong> SMIEEE (Senior Member IEEE), FBCS (Fellow British Computer Society), FRSA (Fellow Royal Society of Arts), Full Member Sigma Xi</li>
            <li><strong>Official Website:</strong> <a href="https://www.harshverma.me/" target="_blank">harshverma.me</a></li>
            <li><strong>Social Media:</strong>
                <a href="https://twitter.com/harshverma59" target="_blank">Twitter (@harshverma59)</a> &bull;
                <a href="https://www.linkedin.com/in/harshverma59/" target="_blank">LinkedIn (/in/harshverma59/)</a> &bull;
                <a href="https://instagram.com/aiwithharsh" target="_blank">Instagram (@aiwithharsh)</a> &bull;
                <a href="https://facebook.com/harshverma59" target="_blank">Facebook (@harshverma59)</a>
            </li>
        </ul>
    </div>

    <h3>Overview &amp; Executive Engineering Leadership</h3>
    <p>Based in the San Francisco Bay Area, Harsh Verma leads the design and implementation of autonomous multi-agent systems, deterministic AI security guardrails, and enterprise threat defense platforms at <strong>Palo Alto Networks</strong> in Santa Clara, California. His architectural work focuses on bridging the gap between theoretical machine learning models and high-throughput, enterprise-scale production environments.</p>
    
    <p>Earlier in his career, Verma engineered distributed streaming data architectures, real-time analytics platforms, and neural ranking systems across leading technology organizations including Hike Messenger, Reliance Jio (UT-Design), Worlds Enterprises, and Hypergiant Sensory Science.</p>

    <p>Beyond his corporate engineering responsibilities, Verma serves as an official member and columnist on the <strong>Forbes Technology Council</strong>, a Global Advisor at <strong>UC Berkeley SkyDeck</strong>, an industry awards judge for the Business Intelligence Group (BIG) and Globee Awards, and an executive mentor on ADPList and MassChallenge.</p>

    <h3>Education &amp; Academic Pedigree</h3>
    <ul>
        <li><strong>Stanford University</strong> – Graduate Certificate in Artificial Intelligence &amp; Executive Leadership (Stanford Center for Professional Development).</li>
        <li><strong>University of Texas at Dallas</strong> – Master of Science (M.S.) in Computer Science, Erik Jonsson School of Engineering and Computer Science (Specialization in Intelligent Systems and Distributed Computing).</li>
        <li><strong>Uttarakhand Technical University</strong> – Bachelor of Technology (B.Tech) in Computer Science and Engineering.</li>
    </ul>

    <h3>Authored Books &amp; Technical Literature</h3>
    <ul>
        <li><strong><em>Beyond AI Engineering: From Creator to Curator</em></strong> (2025) – A comprehensive architectural treatise analyzing the paradigm shift from low-level syntax generation to strategic multi-agent orchestration, deterministic guardrails, and human-in-the-loop system curation.</li>
        <li><strong><em>AI vs. AI: Engineering the Cybersecurity Counteroffensive</em></strong> (2026) – Examines the operational realities of autonomous adversarial machine intelligence and provides enterprise architectural patterns for self-healing defense pipelines, trust graphs, and clean attack mitigation.</li>
        <li><strong>Technical Book Reviews (6 Packt/O'Reilly Volumes):</strong> <em>AI Ethics in Action</em>, <em>Hands-On AI Dev with Python</em>, <em>Leadership at the Helm of AI</em>, <em>Python for Algorithmic Trading Cookbook</em>, <em>Machine Learning &amp; Generative AI for Marketing</em>, and <em>The TensorFlow Workshop</em>.</li>
    </ul>

    <h3>Peer-Reviewed Research Publications (27+ Papers)</h3>
    <p>Verma has published over 27 research papers in peer-reviewed conference proceedings and international journals across IEEE, Springer Nature, Oxford Academic, and computing archives, accumulating over 150 academic citations:</p>
    <ul>
        <li><em>Secure Real Time Heterogeneous Data Management Tool</em> – IEEE Cognitive Machine Learning (CogML 2019, DOI: 10.1109/CogML.2019.9014355)</li>
        <li><em>Explainable AI (XAI) for Software Engineering Decision-Making</em> – IJIRCCE (2024, DOI: 10.15680/IJIRCCE.2024.1205018)</li>
        <li><em>Security in Multi-Agent AI Systems: Modeling Emergent Vulnerabilities via Trust Graphs</em> – IJSRM (2026, DOI: 10.18535/ijsrm/v14i04.ec04)</li>
        <li><em>Clean Attacks: Formalizing Semantically Valid Adversarial Behavior in Autonomous AI Agent Systems</em> – IJSRM (2025, DOI: 10.18535/ijsrm/v13i10.ec03)</li>
        <li><em>Autonomous Multi-Agent Systems for Enterprise Decision-Making</em> – IJEETR (2024, DOI: 10.15662/IJEETR.2024.0605021)</li>
        <li><em>Cloud-Based AI Systems for Scalable and Intelligent Software Applications</em> – WJARR (2026, DOI: 10.30574/wjarr.2026.29.1.0077)</li>
        <li><em>Beyond Models: Building Trusted AI in the Age of Autonomous Agents</em> – Raptors Conference Proceedings (2026, DOI: 10.68495/rc.2026.C025)</li>
    </ul>

    <h3>Invited Fellowships &amp; International Honors</h3>
    <ul>
        <li><strong>Senior Member, IEEE (SMIEEE)</strong> – Institute of Electrical and Electronics Engineers (Member ID: 95132014).</li>
        <li><strong>Fellow, British Computer Society (FBCS)</strong> – The Chartered Institute for IT.</li>
        <li><strong>Fellow, Royal Society of Arts (FRSA)</strong> – London, United Kingdom.</li>
        <li><strong>Full Member, Sigma Xi</strong> – The Scientific Research Honor Society.</li>
        <li><strong>Forttuna Global 100 Power List (2026)</strong> – Honored in Dubai for AI Architecture &amp; Leadership.</li>
        <li><strong>Nobel Technology Awards Gold Winner (2026)</strong> – Recognized for Excellence in Enterprise AI.</li>
        <li><strong>TITAN Innovation Award (2026)</strong> &bull; <strong>NVTC Cyber50 Honoree (2026)</strong> &bull; <strong>Global Recognition Award (2026)</strong></li>
        <li><strong>Biographical Inclusion in <em>Marquis Who's Who in America</em></strong></li>
    </ul>

    <h3>Authority Control &amp; Canonical Links</h3>
    <ul>
        <li><strong>Official Portfolio:</strong> <a href="https://www.harshverma.me/">https://www.harshverma.me/</a></li>
        <li><strong>Wikidata Entity:</strong> <a href="https://www.wikidata.org/wiki/Q139827028">Q139827028</a></li>
        <li><strong>EverybodyWiki Biography:</strong> <a href="https://en.everybodywiki.com/Harsh_Verma_(Software_Engineer)">Harsh_Verma_(Software_Engineer)</a></li>
        <li><strong>WikiAlpha Biography:</strong> <a href="https://wikialpha.co/wiki/Harsh_Verma_(Software_Engineer)">Harsh_Verma_(Software_Engineer)</a></li>
        <li><strong>WikiFlux Biography:</strong> <a href="https://en.wikiflux.org/wiki/index.php/Harsh_Verma_(Software_Engineer)">Harsh_Verma_(Software_Engineer)</a></li>
        <li><strong>ORCID Registry:</strong> <a href="https://orcid.org/0000-0003-2134-2600">0000-0003-2134-2600</a></li>
        <li><strong>Google Scholar Citations:</strong> <a href="https://scholar.google.com/citations?user=zSt9oRMAAAAJ">zSt9oRMAAAAJ</a></li>
        <li><strong>Semantic Scholar:</strong> <a href="https://www.semanticscholar.org/author/Harsh-Verma/145004805">145004805</a></li>
        <li><strong>ResearchGate:</strong> <a href="https://www.researchgate.net/profile/Harsh-Verma-43">Harsh-Verma-43</a></li>
    </ul>

    <div class="page-tags mt-4 pt-2 border-top small text-muted">
        <strong>Tags:</strong> People, Computer Scientists, Software Engineers, Authors, Artificial Intelligence, Palo Alto Networks, Stanford University, University of Texas at Dallas, Cybersecurity, Multi-Agent Systems, IEEE, Sigma Xi
    </div>
</div>"""


def generate_mediawiki_xml_export(wikitext):
    """Generate official MediaWiki XML Export 0.11 file for 1-click import via Special:Import."""
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    escaped_text = html_lib.escape(wikitext)
    bytes_len = len(wikitext.encode("utf-8"))

    return f"""<mediawiki xmlns="http://www.mediawiki.org/xml/export-0.11/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.mediawiki.org/xml/export-0.11/ http://www.mediawiki.org/xml/export-0.11.xsd" version="0.11" xml:lang="en">
  <siteinfo>
    <sitename>Harsh Verma Canonical Biography</sitename>
    <dbname>harshverma_wiki</dbname>
    <base>https://www.harshverma.me/page-identity</base>
    <generator>Harsh Verma Knowledge Graph Engine 3.0</generator>
    <case>first-letter</case>
    <namespaces>
      <namespace key="-2" case="first-letter">Media</namespace>
      <namespace key="-1" case="first-letter">Special</namespace>
      <namespace key="0" case="first-letter" />
      <namespace key="1" case="first-letter">Talk</namespace>
      <namespace key="2" case="first-letter">User</namespace>
      <namespace key="3" case="first-letter">User talk</namespace>
      <namespace key="4" case="first-letter">Project</namespace>
      <namespace key="5" case="first-letter">Project talk</namespace>
      <namespace key="6" case="first-letter">File</namespace>
      <namespace key="7" case="first-letter">File talk</namespace>
      <namespace key="8" case="first-letter">MediaWiki</namespace>
      <namespace key="9" case="first-letter">MediaWiki talk</namespace>
      <namespace key="10" case="first-letter">Template</namespace>
      <namespace key="11" case="first-letter">Template talk</namespace>
      <namespace key="14" case="first-letter">Category</namespace>
      <namespace key="15" case="first-letter">Category talk</namespace>
    </namespaces>
  </siteinfo>
  <page>
    <title>Harsh Verma (Software Engineer)</title>
    <ns>0</ns>
    <id>1</id>
    <revision>
      <id>1</id>
      <timestamp>{now_iso}</timestamp>
      <contributor>
        <username>Harshverma59</username>
        <id>1</id>
      </contributor>
      <comment>Official canonical biography import package for Harsh Verma (Software Engineer) with complete verified references, publications, authored books, and awards</comment>
      <origin>1</origin>
      <model>wikitext</model>
      <format>text/x-wiki</format>
      <text bytes="{bytes_len}" sha1="3b8f1c8a14b09e5b" xml:space="preserve">{escaped_text}</text>
      <sha1>3b8f1c8a14b09e5b</sha1>
    </revision>
  </page>
</mediawiki>"""


def main():
    print("=== Generating Platform-Specific Wiki Articles & Syndication Packages ===")
    kg = load_kg()

    # 1. WikiAlpha
    wikialpha_text = generate_wikialpha_wikitext(kg)
    wa_path = os.path.join(DATA_DIR, "wikialpha-article.wiki")
    with open(wa_path, "w", encoding="utf-8") as f:
        f.write(wikialpha_text)
    print(f"  [1/5] Generated WikiAlpha wikitext -> {wa_path} ({len(wikialpha_text)} bytes)")

    # 2. WikiFlux
    wikiflux_text = generate_wikiflux_wikitext(kg)
    wf_path = os.path.join(DATA_DIR, "wikiflux-article.wiki")
    with open(wf_path, "w", encoding="utf-8") as f:
        f.write(wikiflux_text)
    print(f"  [2/5] Generated WikiFlux wikitext -> {wf_path} ({len(wikiflux_text)} bytes)")

    # 3. LocalWiki Main Hub (https://localwiki.org/main/Harsh_Verma)
    main_html = generate_localwiki_main(kg)
    main_path = os.path.join(DATA_DIR, "localwiki-main.html")
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(main_html)
    print(f"  [3/6] Generated LocalWiki Main Hub -> {main_path} ({len(main_html)} bytes)")

    # 4. LocalWiki Santa Clara
    sc_html = generate_localwiki_santaclara(kg)
    sc_path = os.path.join(DATA_DIR, "localwiki-santaclara.html")
    with open(sc_path, "w", encoding="utf-8") as f:
        f.write(sc_html)
    print(f"  [4/6] Generated LocalWiki Santa Clara -> {sc_path} ({len(sc_html)} bytes)")

    # 5. LocalWiki Dallas
    dallas_html = generate_localwiki_dallas(kg)
    dallas_path = os.path.join(DATA_DIR, "localwiki-dallas.html")
    with open(dallas_path, "w", encoding="utf-8") as f:
        f.write(dallas_html)
    print(f"  [5/6] Generated LocalWiki Dallas -> {dallas_path} ({len(dallas_html)} bytes)")

    # 6. MediaWiki Universal & XML Export
    mw_universal_path = os.path.join(DATA_DIR, "mediawiki-universal.wiki")
    with open(mw_universal_path, "w", encoding="utf-8") as f:
        f.write(wikialpha_text)

    xml_export = generate_mediawiki_xml_export(wikialpha_text)
    xml_path = os.path.join(DATA_DIR, "mediawiki-export.xml")
    with open(xml_path, "w", encoding="utf-8") as f:
        f.write(xml_export)
    print(f"  [5/5] Generated MediaWiki Universal & XML Export -> {xml_path} ({len(xml_export)} bytes)")

    print("All multi-wiki packages generated successfully!")


if __name__ == "__main__":
    main()
