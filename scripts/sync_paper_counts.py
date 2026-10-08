#!/usr/bin/env python3
"""
Synchronizes research paper counts uniformly across the entire site.
Source of truth: papers_data.json
Ensures all occurrences of published paper numbers, badges, stat cards,
and scholar links match the exact count of papers in papers_data.json.
"""
import os
import re
import json

def get_authoritative_paper_count():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(base_dir, 'papers_data.json')
    if not os.path.exists(json_path):
        json_path = 'papers_data.json'
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if isinstance(data, list):
        return len(data)
    elif isinstance(data, dict) and 'papers' in data:
        return len(data['papers'])
    return 25

def sync_paper_counts(count=None):
    if count is None:
        count = get_authoritative_paper_count()
    
    count_str = str(count)
    count_plus = f"{count}+"
    print(f"[Sync] Synchronizing site-wide paper counter to: {count_plus} (Raw: {count_str})")

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 1. Update page-books.html
    books_path = os.path.join(base_dir, 'page-books.html')
    if os.path.exists(books_path):
        with open(books_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update link: View XX+ Published Papers
        content = re.sub(
            r'View\s+\d+\+?\s+Published\s+Papers',
            f'View {count_plus} Published Papers',
            content,
            flags=re.IGNORECASE
        )
        
        # Update hero stat card: <div class="stat-val">22+</div> followed by <div class="stat-lbl">Research Papers</div>
        content = re.sub(
            r'(<div class="stat-val"[^>]*>)\s*\d+\+?\s*(</div>\s*<div class="stat-lbl">\s*Research Papers\s*</div>)',
            rf'\g<1>{count_plus}\g<2>',
            content,
            flags=re.IGNORECASE
        )

        with open(books_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("  -> Updated page-books.html")

    # 2. Update page-awards.html and generate_awards_page.py
    for fname in ['page-awards.html', 'generate_awards_page.py']:
        fpath = os.path.join(base_dir, fname)
        if os.path.exists(fpath):
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            content = re.sub(
                r'\d+\+?\s+IEEE\s+publications',
                f'{count_plus} IEEE publications',
                content,
                flags=re.IGNORECASE
            )
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  -> Updated {fname}")

    # 3. Update page-publications.html & generate_publications_html.py
    for fname in ['page-publications.html', 'generate_publications_html.py']:
        fpath = os.path.join(base_dir, fname)
        if os.path.exists(fpath):
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            # In scholar-stat-papers box
            content = re.sub(
                r'(<div class="scholar-stat-box" id="scholar-stat-papers">\s*<div class="scholar-stat-number"[^>]*>)\s*\d+\s*(</div>)',
                rf'\g<1>{count_str}\g<2>',
                content
            )
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  -> Updated {fname}")

    # 4. Update standardize_headers_footers.py
    std_path = os.path.join(base_dir, 'scripts', 'standardize_headers_footers.py')
    if os.path.exists(std_path):
        with open(std_path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = re.sub(
            r'Google Scholar \(\d+\+? Papers\)',
            f'Google Scholar ({count_plus} Papers)',
            content
        )
        with open(std_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("  -> Updated standardize_headers_footers.py")

    # 5. Update copilot knowledge base
    copilot_path = os.path.join(base_dir, 'data', 'copilot-knowledge.js')
    if os.path.exists(copilot_path):
        with open(copilot_path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = re.sub(
            r'count:\s*"\d+\+?\s*Papers"',
            f'count: "{count_plus} Papers"',
            content
        )
        with open(copilot_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("  -> Updated data/copilot-knowledge.js")

    print("[Sync] Completed successfully! All paper counters are uniform.")

if __name__ == '__main__':
    sync_paper_counts()
