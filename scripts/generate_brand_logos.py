#!/usr/bin/env python3
"""
Generate crisp, authentic brand logos matching the user reference screenshot:
1. Healthcare Executive
2. The Telegraph (calcutta, india)
3. Gadgets 360 (An NDTV venture)
4. The Times Group e-paper
5. Business Insider
6. DNA Daily News & Analysis
7. The Economic Times
8. ET SmallBiz
Plus additional verified publications in Harsh's media footprint:
9. USA Today
10. Yahoo Finance
11. HackerNoon
12. Forttuna Global 100
"""

import os

os.makedirs('images/media/brands', exist_ok=True)

# 1. Healthcare Executive
healthcare_svg = '''<svg width="220" height="75" viewBox="0 0 220 75" fill="none" xmlns="http://www.w3.org/2000/svg">
  <text x="5" y="32" font-family="'Georgia', serif" font-size="28" font-weight="700" fill="#0891b2" letter-spacing="-0.5">Healthcare</text>
  <text x="7" y="55" font-family="'Arial Black', -apple-system, sans-serif" font-size="22" font-weight="900" fill="#1e3a8a" letter-spacing="1.5">EXECUTIVE</text>
  <text x="8" y="69" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="8.5" font-weight="500" fill="#64748b" letter-spacing="0.4">Aiding smart business decisions</text>
</svg>'''

# 2. The Telegraph
telegraph_svg = '''<svg width="220" height="75" viewBox="0 0 220 75" fill="none" xmlns="http://www.w3.org/2000/svg">
  <text x="10" y="44" font-family="'Playfair Display', 'Times New Roman', Georgia, serif" font-size="29" font-weight="900" fill="#0f172a" letter-spacing="-0.5">The Telegraph</text>
  <text x="24" y="62" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="9.5" font-weight="800" fill="#dc2626" letter-spacing="0.6">calcutta, india</text>
</svg>'''

# 3. Gadgets 360
gadgets360_svg = '''<svg width="220" height="75" viewBox="0 0 220 75" fill="none" xmlns="http://www.w3.org/2000/svg">
  <g transform="translate(10, 10)">
    <text x="0" y="34" font-family="'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif" font-size="28" font-weight="800" fill="#475569" letter-spacing="-0.5">Gadgets</text>
    <circle cx="145" cy="24" r="21" fill="#e11d48"/>
    <text x="145" y="32" font-family="'Arial Black', -apple-system, sans-serif" font-size="16" font-weight="900" fill="#ffffff" text-anchor="middle">360</text>
    <circle cx="168" cy="8" r="3.5" fill="#e11d48"/>
    <text x="45" y="52" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="9" font-weight="600" fill="#64748b" letter-spacing="0.2">An <tspan font-weight="800" fill="#334155">NDTV</tspan> venture</text>
  </g>
</svg>'''

# 4. The Times Group e-paper
times_group_svg = '''<svg width="170" height="75" viewBox="0 0 170 75" fill="none" xmlns="http://www.w3.org/2000/svg">
  <!-- Royal Crest / Elephants motif -->
  <g transform="translate(45, 2)" stroke="#1e293b" stroke-width="1.2" fill="none">
    <!-- Left elephant -->
    <path d="M10 20 C6 18 2 14 6 10 C9 7 14 8 16 12 C18 16 16 22 14 24" />
    <circle cx="10" cy="11" r="1.2" fill="#1e293b"/>
    <!-- Right elephant -->
    <path d="M70 20 C74 18 78 14 74 10 C71 7 66 8 64 12 C62 16 64 22 66 24" />
    <circle cx="70" cy="11" r="1.2" fill="#1e293b"/>
    <!-- Shield / Sun -->
    <path d="M30 6 L50 6 C52 14 48 20 40 24 C32 20 28 14 30 6 Z" fill="#f8fafc"/>
    <circle cx="40" cy="14" r="4" fill="#1e293b"/>
  </g>
  <text x="85" y="38" font-family="'Times New Roman', Georgia, serif" font-size="11.5" font-weight="900" fill="#0f172a" text-anchor="middle" letter-spacing="1">THE TIMES GROUP</text>
  <!-- Red e-paper pill -->
  <rect x="35" y="46" width="100" height="23" rx="4" fill="#dc2626"/>
  <text x="85" y="62" font-family="'Times New Roman', Georgia, serif" font-size="15" font-style="italic" font-weight="700" fill="#ffffff" text-anchor="middle" letter-spacing="0.5">e-paper</text>
</svg>'''

# 5. Business Insider
business_insider_svg = '''<svg width="170" height="75" viewBox="0 0 170 75" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="5" y="6" width="160" height="63" rx="4" fill="#184f68"/>
  <text x="85" y="33" font-family="'Georgia', 'Times New Roman', serif" font-size="18" font-weight="900" fill="#ffffff" text-anchor="middle" letter-spacing="0.5">BUSINESS</text>
  <text x="85" y="56" font-family="'Georgia', 'Times New Roman', serif" font-size="18" font-weight="900" fill="#ffffff" text-anchor="middle" letter-spacing="0.5">INSIDER</text>
</svg>'''

# 6. DNA Daily News & Analysis
dna_svg = '''<svg width="150" height="75" viewBox="0 0 150 75" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="5" y="6" width="140" height="63" rx="4" fill="#f4cf36"/>
  <text x="75" y="46" font-family="'Impact', 'Arial Black', sans-serif" font-size="44" font-weight="900" fill="#1e293b" text-anchor="middle" letter-spacing="-1">DNA</text>
  <text x="75" y="60" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="7.5" font-weight="800" fill="#1e293b" text-anchor="middle" letter-spacing="0.6">DAILY NEWS &amp; ANALYSIS</text>
</svg>'''

# 7. The Economic Times
economic_times_svg = '''<svg width="240" height="75" viewBox="0 0 240 75" fill="none" xmlns="http://www.w3.org/2000/svg">
  <text x="120" y="47" font-family="'Times New Roman', 'Georgia', serif" font-size="22" font-weight="900" fill="#111827" text-anchor="middle" letter-spacing="0.8">THE ECONOMIC TIMES</text>
</svg>'''

# 8. ET SmallBiz
et_smallbiz_svg = '''<svg width="190" height="75" viewBox="0 0 190 75" fill="none" xmlns="http://www.w3.org/2000/svg">
  <g transform="translate(10, 10)">
    <!-- ET Red Badge -->
    <rect x="0" y="6" width="30" height="28" rx="3" fill="#dc2626"/>
    <text x="15" y="27" font-family="'Georgia', 'Times New Roman', serif" font-size="18" font-weight="900" fill="#ffffff" text-anchor="middle">ET</text>
    <!-- Paper airplane -->
    <path d="M35 12 L50 20 L40 22 L38 28 L35 12 Z" fill="#dc2626" opacity="0.85"/>
    <!-- SmallBiz Text -->
    <text x="54" y="30" font-family="'Arial Black', -apple-system, sans-serif" font-size="24" font-weight="900" fill="#1e293b" letter-spacing="-0.5">SmallBiz</text>
    <!-- Subtitle -->
    <line x1="55" y1="36" x2="165" y2="36" stroke="#e2e8f0" stroke-width="1"/>
    <text x="110" y="46" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="8" font-weight="600" fill="#64748b" text-anchor="middle" letter-spacing="0.4">www.etsmallbiz.com</text>
  </g>
</svg>'''

# 9. USA Today
usatoday_svg = '''<svg width="190" height="75" viewBox="0 0 190 75" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="34" cy="37" r="19" fill="#0066cc"/>
  <circle cx="34" cy="37" r="6" fill="#ffffff"/>
  <text x="62" y="45" font-family="'Arial Black', -apple-system, sans-serif" font-size="20" font-weight="900" fill="#0f172a" letter-spacing="-0.5">USA TODAY</text>
</svg>'''

# 10. Yahoo Finance
yahoo_finance_svg = '''<svg width="200" height="75" viewBox="0 0 200 75" fill="none" xmlns="http://www.w3.org/2000/svg">
  <text x="10" y="45" font-family="'Arial Black', -apple-system, sans-serif" font-size="23" font-weight="900" fill="#6001d2" letter-spacing="-0.5">yahoo!</text>
  <text x="102" y="45" font-family="'Segoe UI', -apple-system, sans-serif" font-size="21" font-weight="700" fill="#1e293b" letter-spacing="-0.2">finance</text>
</svg>'''

# 11. HackerNoon
hackernoon_svg = '''<svg width="200" height="75" viewBox="0 0 200 75" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="5" y="16" width="38" height="38" rx="6" fill="#00ea62"/>
  <text x="24" y="41" font-family="'Courier New', monospace" font-size="22" font-weight="900" fill="#000000" text-anchor="middle">&lt;H&gt;</text>
  <text x="50" y="43" font-family="'Arial Black', -apple-system, sans-serif" font-size="19" font-weight="900" fill="#0f172a" letter-spacing="-0.5">HACKERNOON</text>
</svg>'''

# 12. Forttuna Global 100
forttuna_svg = '''<svg width="210" height="75" viewBox="0 0 210 75" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="5" y="14" width="40" height="42" rx="6" fill="#b45309"/>
  <text x="25" y="40" font-family="'Georgia', serif" font-size="20" font-weight="900" fill="#fef3c7" text-anchor="middle">F</text>
  <text x="52" y="35" font-family="'Georgia', serif" font-size="16" font-weight="900" fill="#1e293b" letter-spacing="0.5">FORTTUNA</text>
  <text x="53" y="50" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="800" fill="#d97706" letter-spacing="1">GLOBAL 100 • NYC</text>
</svg>'''

files = {
    'images/media/brands/healthcare_executive_logo.svg': healthcare_svg,
    'images/media/brands/the_telegraph_logo.svg': telegraph_svg,
    'images/media/brands/gadgets360_logo.svg': gadgets360_svg,
    'images/media/brands/times_group_epaper_logo.svg': times_group_svg,
    'images/media/brands/business_insider_logo.svg': business_insider_svg,
    'images/media/brands/dna_india_logo.svg': dna_svg,
    'images/media/brands/economic_times_logo.svg': economic_times_svg,
    'images/media/brands/et_smallbiz_logo.svg': et_smallbiz_svg,
    'images/media/brands/usatoday_logo.svg': usatoday_svg,
    'images/media/brands/yahoo_finance_logo.svg': yahoo_finance_svg,
    'images/media/brands/hackernoon_logo.svg': hackernoon_svg,
    'images/media/brands/forttuna_global100_logo.svg': forttuna_svg,
}

for path, content in files.items():
    with open(path, 'w') as f:
        f.write(content.strip() + '\n')

print(f"Generated {len(files)} brand logos in images/media/brands/")
