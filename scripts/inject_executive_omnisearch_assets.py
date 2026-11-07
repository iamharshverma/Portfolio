#!/usr/bin/env python3
"""
scripts/inject_executive_omnisearch_assets.py
Injects:
1. <link rel="stylesheet" href="css/hv-executive-refinements.css"> in <head>
2. <script src="js/hv-omnisearch.js"></script> before </body>
3. Clean Search button (renamed from Global Search, no Cmd+K icon) in navbar across all HTML files
"""

import os
import glob
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CLEAN_SEARCH_BTN = """                    <li class="list-inline-item mr-2 nav-search-li">
                        <button type="button" class="nav-global-search-btn" id="navGlobalSearchBtn" data-action="open-omnisearch" aria-label="Search" title="Search">
                            <i class="mdi mdi-magnify mr-1"></i>
                            <input type="text" class="nav-search-input" id="navSearchInput" placeholder="Search..." readonly aria-label="Search">
                            <span class="search-label-text sr-only">Search</span>
                        </button>
                    </li>"""

CSS_TAG = '    <link rel="stylesheet" href="css/hv-executive-refinements.css">\n'
JS_TAG = '    <script src="js/hv-omnisearch.js"></script>\n'

def update_html_files():
    html_files = glob.glob(os.path.join(ROOT_DIR, "*.html"))
    count = 0

    for path in sorted(html_files):
        fname = os.path.basename(path)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        changed = False

        # 1. Inject CSS if not present
        if "hv-executive-refinements.css" not in content:
            if "</head>" in content:
                content = content.replace("</head>", CSS_TAG + "</head>", 1)
                changed = True

        # 2. Inject JS if not present
        if "hv-omnisearch.js" not in content:
            if "</body>" in content:
                content = content.replace("</body>", JS_TAG + "</body>", 1)
                changed = True

        # 3. Update navbar search button if present to clean "Search" without Command K
        old_btn_pattern = re.compile(r'<li[^>]*class=[\'"][^\'"]*list-inline-item[^\'"]*mr-2[^\'"]*[\'"][^>]*>\s*<button[^>]*id=[\'"]navGlobalSearchBtn[\'"][^>]*>.*?</button>\s*</li>', re.DOTALL)
        if old_btn_pattern.search(content):
            new_content = old_btn_pattern.sub(CLEAN_SEARCH_BTN.strip(), content)
            if new_content != content:
                content = new_content
                changed = True
        elif 'id="navGlobalSearchBtn"' not in content and 'nav-global-search-btn' not in content:
            # Look for top-right ul
            match = re.search(r'(<ul[^>]*class=[\'"][^\'"]*top-right[^\'"]*[\'"][^>]*>\s*)', content)
            if match:
                content = content[:match.end()] + "\n" + CLEAN_SEARCH_BTN + "\n" + content[match.end():]
                changed = True

        if changed:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
            print(f"Updated {fname} with clean Search button and assets")

    print(f"\nCompleted asset & header update across {count} HTML files.")

if __name__ == "__main__":
    update_html_files()
