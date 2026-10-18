import os

ROOT_DIR = '/app/applet'

files = [
    os.path.join(ROOT_DIR, 'page-smart-slides.html'),
    os.path.join(ROOT_DIR, 'page-slides.html')
]

card_html = """                <!-- Deck 8 Card: X2qH -->
                <div class="deck-card" id="deck-card-X2qH" onclick="selectDeck('X2qH')">
                    <div>
                        <div class="d-flex justify-content-between align-items-center mb-2">
                            <span class="deck-card-badge">Deck 8 • EasyChair Ref: X2qH</span>
                            <span class="badge badge-pill badge-info" style="font-size: 11px;">9 Slides</span>
                        </div>
                        <h3 class="deck-title">Agents Don't Break Rules, They Redefine Them</h3>
                        <p class="deck-desc">
                            Cybersecurity in the age of autonomous AI. Why autonomous agents don't fail by violating rules—they follow instructions literally while circumventing intent through policy drift and specification gaming.
                        </p>
                        <div class="mt-2 mb-2">
                            <a href="https://www.rsaconference.com/Library/blog/agents-dont-break-rules-they-redefine-them" target="_blank" rel="noopener noreferrer" onclick="event.stopPropagation()" class="btn btn-sm btn-outline-danger font-weight-bold px-2 py-1 d-inline-flex align-items-center" style="font-size: 11.5px; border-radius: 6px;" title="Read linked RSA Conference Blog Post">
                                <i class="mdi mdi-robot mr-1 text-danger"></i> Linked RSA Article <i class="mdi mdi-open-in-new ml-1"></i>
                            </a>
                        </div>
                    </div>
                    <div class="deck-meta-footer">
                        <span><i class="mdi mdi-account-check text-primary mr-1"></i> Author: Harsh Verma</span>
                        <span><i class="mdi mdi-shield-refresh text-warning mr-1"></i> Continuous Governance</span>
                    </div>
                </div>"""

deck_obj = """            'X2qH': {
                id: 'X2qH',
                folder: 'agents-dont-break-rules-they-redefine-them',
                title: "Agents Don't Break Rules, They Redefine Them: Cybersecurity in the Age of Autonomous AI",
                shortTitle: "Agents Don't Break Rules: Redefining Intent",
                count: 9,
                easyChairUrl: 'https://easychair.org/smart-slide/slide/X2qH#{sn:1}',
                blogUrl: 'https://www.rsaconference.com/Library/blog/agents-dont-break-rules-they-redefine-them',
                blogTitle: "RSA Conference: Agents Don't Break Rules",
                bibtex: `@misc{verma2026agentsdontbreakrules,
  author = {Verma, Harsh},
  title = {Agents Don't Break Rules, They Redefine Them: Cybersecurity in the Age of Autonomous AI},
  howpublished = {EasyChair Smart Slide Series, Ref. X2qH},
  year = {2026},
  url = {https://easychair.org/smart-slide/slide/X2qH}
}`,
                slides: [] // Populated below
            }"""

loader_code = """            if (!DECKS['X2qH'].slides.length) {
                try {
                    var res8 = await fetch('data/agents-dont-break-rules-they-redefine-them.json');
                    if (res8.ok) DECKS['X2qH'].slides = await res8.json();
                } catch(e) { console.warn('Deck 8 fallback load'); }
            }"""

for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()

    # 1. Update stats in hero
    c = c.replace('<div class="smart-stat-num">7</div>\n                                    <div class="smart-stat-label">Keynote Decks</div>',
                  '<div class="smart-stat-num">8</div>\n                                    <div class="smart-stat-label">Keynote Decks</div>')
    c = c.replace('<div class="smart-stat-num">123</div>\n                                    <div class="smart-stat-label">Total Slides</div>',
                  '<div class="smart-stat-num">132</div>\n                                    <div class="smart-stat-label">Total Slides</div>')

    # 2. Add Deck 8 Card after Deck 7
    if 'deck-card-X2qH' not in c:
        deck7_marker = '<div class="deck-card" id="deck-card-xJKk"'
        idx = c.find(deck7_marker)
        if idx != -1:
            # find end of deck-card-xJKk div
            end_card_idx = c.find('</div>\n                </div>\n            </div>', idx)
            if end_card_idx == -1:
                end_card_idx = c.find('</div>\n                </div>\n\n            </div>', idx)
            if end_card_idx == -1:
                # search for next closing tag pattern
                end_div = c.find('</div>\n                </div>', idx)
                if end_div != -1:
                    end_card_idx = end_div
            
            if end_card_idx != -1:
                insert_pos = end_card_idx + len('</div>\n                </div>')
                c = c[:insert_pos] + '\n\n' + card_html + c[insert_pos:]

    # 3. Add to DECKS object
    if "'X2qH': {" not in c:
        target = "'xJKk': {"
        idx = c.find(target)
        if idx != -1:
            end_deck7 = c.find('}\n        };', idx)
            if end_deck7 != -1:
                c = c[:end_deck7+1] + ',\n' + deck_obj + c[end_deck7+1:]

    # 4. Add to loader code
    if 'res8' not in c:
        target = "if (!DECKS['xJKk'].slides.length) {"
        idx = c.find(target)
        if idx != -1:
            end_if = c.find('}\n            }', idx)
            if end_if != -1:
                insert_pos = end_if + len('}\n            }')
                c = c[:insert_pos] + '\n\n' + loader_code + c[insert_pos:]

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(c)

    print(f'Successfully updated {os.path.basename(fn)}')
