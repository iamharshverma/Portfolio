import os

ROOT_DIR = '/app/applet'

files = [
    os.path.join(ROOT_DIR, 'page-smart-slides.html'),
    os.path.join(ROOT_DIR, 'page-slides.html')
]

card_html = """                <!-- Deck 9 Card: JSZf -->
                <div class="deck-card" id="deck-card-JSZf" onclick="selectDeck('JSZf')">
                    <div>
                        <div class="d-flex justify-content-between align-items-center mb-2">
                            <span class="deck-card-badge">Deck 9 • EasyChair Ref: JSZf</span>
                            <span class="badge badge-pill badge-info" style="font-size: 11px;">16 Slides</span>
                        </div>
                        <h3 class="deck-title">Why Multi-Agent Systems Are a Cybersecurity Nightmare</h3>
                        <p class="deck-desc">
                            Deep-dive into inter-agent trust chains, cascade prompt injections, memory and vector store poisoning, and machine-to-machine agentic IAM architecture.
                        </p>
                        <div class="mt-2 mb-2">
                            <a href="https://www.rsaconference.com/Library/blog/why-multi-agent-systems-are-a-cybersecurity-nightmare" target="_blank" rel="noopener noreferrer" onclick="event.stopPropagation()" class="btn btn-sm btn-outline-danger font-weight-bold px-2 py-1 d-inline-flex align-items-center" style="font-size: 11.5px; border-radius: 6px;" title="Read linked RSA Conference Blog Post">
                                <i class="mdi mdi-shield-alert mr-1 text-danger"></i> Linked RSA Article <i class="mdi mdi-open-in-new ml-1"></i>
                            </a>
                        </div>
                    </div>
                    <div class="deck-meta-footer">
                        <span><i class="mdi mdi-account-check text-primary mr-1"></i> Author: Harsh Verma</span>
                        <span><i class="mdi mdi-shield-bug text-danger mr-1"></i> Multi-Agent Defense</span>
                    </div>
                </div>"""

deck_obj = """            'JSZf': {
                id: 'JSZf',
                folder: 'why-multi-agent-systems-cybersecurity-nightmare',
                title: 'Why Multi-Agent Systems Are a Cybersecurity Nightmare: Deep-Dive into Inter-Agent Trust Chains, Cascade Injections & Agentic IAM',
                shortTitle: 'Why Multi-Agent Systems Are a Cybersecurity Nightmare',
                count: 16,
                easyChairUrl: 'https://easychair.org/smart-slide/slide/JSZf#{sn:1}',
                blogUrl: 'https://www.rsaconference.com/Library/blog/why-multi-agent-systems-are-a-cybersecurity-nightmare',
                blogTitle: 'RSA Conference: Why Multi-Agent Systems Are a Cybersecurity Nightmare',
                bibtex: `@misc{verma2026whymultiagentsystemscybersecuritynightmare,
  author = {Verma, Harsh},
  title = {Why Multi-Agent Systems Are a Cybersecurity Nightmare},
  howpublished = {EasyChair Smart Slide Series, Ref. JSZf},
  year = {2026},
  url = {https://easychair.org/smart-slide/slide/JSZf}
}`,
                slides: [] // Populated below
            }"""

loader_code = """            if (!DECKS['JSZf'].slides.length) {
                try {
                    var res9 = await fetch('data/why-multi-agent-systems-cybersecurity-nightmare.json');
                    if (res9.ok) DECKS['JSZf'].slides = await res9.json();
                } catch(e) { console.warn('Deck 9 fallback load'); }
            }"""

for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()

    # 1. Update stats in hero
    c = c.replace('<div class="smart-stat-num">8</div>\n                                    <div class="smart-stat-label">Keynote Decks</div>',
                  '<div class="smart-stat-num">9</div>\n                                    <div class="smart-stat-label">Keynote Decks</div>')
    c = c.replace('<div class="smart-stat-num">132</div>\n                                    <div class="smart-stat-label">Total Slides</div>',
                  '<div class="smart-stat-num">148</div>\n                                    <div class="smart-stat-label">Total Slides</div>')

    # 2. Add Deck 9 Card after Deck 8
    if 'deck-card-JSZf' not in c:
        deck8_marker = '<div class="deck-card" id="deck-card-X2qH"'
        idx = c.find(deck8_marker)
        if idx != -1:
            # find end of deck-card-X2qH div
            end_card_idx = c.find('</div>\n                </div>\n            </div>', idx)
            if end_card_idx == -1:
                end_card_idx = c.find('</div>\n                </div>\n\n            </div>', idx)
            if end_card_idx == -1:
                end_div = c.find('</div>\n                </div>', idx)
                if end_div != -1:
                    end_card_idx = end_div
            
            if end_card_idx != -1:
                insert_pos = end_card_idx + len('</div>\n                </div>')
                c = c[:insert_pos] + '\n\n' + card_html + c[insert_pos:]

    # 3. Add to DECKS object
    if "'JSZf': {" not in c:
        target = "'X2qH': {"
        idx = c.find(target)
        if idx != -1:
            end_deck8 = c.find('}\n        };', idx)
            if end_deck8 != -1:
                c = c[:end_deck8+1] + ',\n' + deck_obj + c[end_deck8+1:]

    # 4. Add to loader code
    if 'res9' not in c:
        target = "if (!DECKS['X2qH'].slides.length) {"
        idx = c.find(target)
        if idx != -1:
            end_if = c.find('}\n            }', idx)
            if end_if != -1:
                insert_pos = end_if + len('}\n            }')
                c = c[:insert_pos] + '\n\n' + loader_code + c[insert_pos:]

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(c)

    print(f'Successfully updated {os.path.basename(fn)}')
