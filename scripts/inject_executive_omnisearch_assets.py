#!/usr/bin/env python3
"""
scripts/inject_executive_omnisearch_assets.py
Injects:
1. <link rel="stylesheet" href="css/hv-executive-refinements.css"> in <head>
2. <script src="js/hv-omnisearch.js"></script> before </body>
3. Global Search button in navbar if not present
Across all 28 HTML files in the repository.
"""

import os
import glob
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SEARCH_BTN_HTML = """                    <li class="list-inline-item mr-2">
                        <button type="button" class="nav-global-search-btn" id="navGlobalSearchBtn" data-action="open-omnisearch" aria-label="Global Search (Cmd+K)" title="Global Search (Cmd+K / Ctrl+K)">
                            <i class="mdi mdi-magnify mr-1"></i>
                            <span class="d-none d-xl-inline search-label-text">Global Search</span>
                            <span class="search-kbd-shortcut"><kbd class="nav-kbd">⌘K</kbd></span>
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

        # 3. Inject Navbar Global Search button if navbar exists and button isn't there
        if 'id="navGlobalSearchBtn"' not in content and 'nav-global-search-btn' not in content:
            # Look for top-right ul
            match = re.search(r'(<ul[^>]*class=[\'"][^\'"]*top-right[^\'"]*[\'"][^>]*>\s*)', content)
            if match:
                content = content[:match.end()] + "\n" + SEARCH_BTN_HTML + "\n" + content[match.end():]
                changed = True

        if changed:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
            print(f"Updated {fname} with Omnisearch & Executive Refinements")

    print(f"\nCompleted asset injection across {count} HTML files.")

if __name__ == "__main__":
    update_html_files()
