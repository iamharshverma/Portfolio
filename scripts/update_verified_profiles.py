import os
import re
import json

ROOT_DIR = '/app/applet'

# 1. Update generate_about_page.py
about_gen_path = os.path.join(ROOT_DIR, 'generate_about_page.py')
with open(about_gen_path, 'r', encoding='utf-8') as f:
    about_gen = f.read()

# Add soundverse-ai right after hackernoon if not present
if '"id": "soundverse-ai"' not in about_gen:
    soundverse_entry = '''    {
        "id": "soundverse-ai",
        "category": "developer",
        "categoryLabel": "Developer & Cloud Ecosystems",
        "name": "Soundverse AI",
        "identifier": "@harshverma59",
        "url": "https://www.soundverse.ai/@harshverma59",
        "icon": "mdi-music-box-outline",
        "thumb": "images/profiles/soundverse.svg",
        "badgeColor": "#8b5cf6",
        "tag": "AI Audio Creator",
        "description": "Official creator and AI audio researcher profile on Soundverse AI (@harshverma59), exploring generative audio architectures, diffusion music models, and AI soundscapes."
    },'''
    
    target = '"id": "hackernoon",'
    idx = about_gen.find(target)
    if idx != -1:
        end_entry = about_gen.find('},', idx)
        if end_entry != -1:
            about_gen = about_gen[:end_entry+2] + '\n' + soundverse_entry + about_gen[end_entry+2:]

# Add big-judges right after topmate if not present
if '"id": "big-judges"' not in about_gen:
    big_judges_entry = '''    {
        "id": "big-judges",
        "category": "advisory",
        "categoryLabel": "Advisory & Mentorship",
        "name": "Business Intelligence Group",
        "identifier": "Official Awards Judge",
        "url": "https://judges.bintelligence.com/harsh-verma",
        "icon": "mdi-gavel",
        "thumb": "images/profiles/big_judges.svg",
        "badgeColor": "#f76814",
        "tag": "Industry Awards Judge",
        "description": "Official Judge for Business Intelligence Group (BIG) industry recognition programs, evaluating breakthrough AI innovations, enterprise systems, and executive achievements."
    },'''
    
    target = '"id": "topmate",'
    idx = about_gen.find(target)
    if idx != -1:
        end_entry = about_gen.find('},', idx)
        if end_entry != -1:
            about_gen = about_gen[:end_entry+2] + '\n' + big_judges_entry + about_gen[end_entry+2:]

# Update generate_profile_card_html in generate_about_page.py to support thumb SVG
old_card_icon = '''                    <div class="profile-card-icon-wrap mr-3">
                        <i class="mdi {link['icon']}"></i>
                    </div>'''
new_card_icon = '''                    <div class="profile-card-icon-wrap mr-3">
                        {icon_markup}
                    </div>'''
if old_card_icon in about_gen:
    about_gen = about_gen.replace(old_card_icon, new_card_icon)
    # also add icon_markup logic in generate_profile_card_html
    target_func = 'def generate_profile_card_html(link):'
    func_idx = about_gen.find(target_func)
    if func_idx != -1:
        logic = '''    thumb_img = link.get("thumb")
    if not thumb_img:
        slug = link["id"].replace("-", "_")
        for p in [f"images/profiles/{slug}.svg", f"images/profiles/{link['id']}.svg"]:
            if os.path.exists(p):
                thumb_img = p
                break
    if thumb_img:
        icon_markup = f'<img src="{thumb_img}" class="profile-card-thumb-img" alt="{link[\\"name\\"]} Thumbnail" loading="lazy">'
    else:
        icon_markup = f'<i class="mdi {link[\\"icon\\"]}"></i>'
'''
        insert_idx = about_gen.find('data_search =', func_idx)
        if insert_idx != -1:
            about_gen = about_gen[:insert_idx] + logic + '    ' + about_gen[insert_idx:]

# Update count strings in generate_about_page.py
about_gen = about_gen.replace('47 Profiles', '{len(PROFILE_LINKS)} Profiles')
about_gen = about_gen.replace('All (47)', 'All ({len(PROFILE_LINKS)})')

with open(about_gen_path, 'w', encoding='utf-8') as f:
    f.write(about_gen)
print("Updated generate_about_page.py")

# 2. Update page-about.html with cards and count
about_html_path = os.path.join(ROOT_DIR, 'page-about.html')
with open(about_html_path, 'r', encoding='utf-8') as f:
    about_html = f.read()

# Update header badge and filter count
about_html = re.sub(r'47 Profiles', '49 Profiles', about_html)
about_html = re.sub(r'All \((?:47|52)\)', 'All (49)', about_html)

# Add soundverse card in page-about.html
if 'data-category="developer" data-search="soundverse ai' not in about_html:
    soundverse_card_html = '''
    <div class="col-lg-4 col-md-6 mb-4 profile-card-item" data-category="developer" data-search="soundverse ai @harshverma59 ai music creator audio diffusion generative music ai soundscapes developer & cloud ecosystems">
        <div class="profile-hub-card h-100">
            <div class="d-flex justify-content-between align-items-start mb-3">
                <div class="d-flex align-items-center">
                    <div class="profile-card-icon-wrap mr-3">
                        <img src="images/profiles/soundverse.svg" class="profile-card-thumb-img" alt="Soundverse AI Thumbnail" loading="lazy">
                    </div>
                    <div>
                        <span class="profile-category-pill">Developer &amp; Cloud Ecosystems</span>
                        <h5 class="profile-card-title mb-0 mt-1">Soundverse AI</h5>
                    </div>
                </div>
            </div>
            
            <div class="profile-card-identifier mb-2">
                <span class="badge badge-light border font-weight-bold text-dark px-2 py-1">
                    <i class="mdi mdi-check-circle text-primary mr-1"></i> @harshverma59
                </span>
                <span class="badge badge-pill text-white font-weight-bold px-2 py-1 ml-1" style="background: #8b5cf6; font-size: 11px;">
                    <i class="mdi mdi-waveform mr-1"></i> AI Music Creator
                </span>
            </div>

            <p class="profile-card-desc mb-3">Official creator and AI audio researcher profile on Soundverse AI (@harshverma59), exploring generative audio architectures, diffusion music models, and AI soundscapes.</p>

            <div class="d-flex align-items-center justify-content-between pt-3 border-top mt-auto">
                <a href="https://www.soundverse.ai/@harshverma59" target="_blank" class="btn-hub-action btn-hub-primary" title="Visit Soundverse AI">
                    <i class="mdi mdi-open-in-new mr-1"></i> Open Profile
                </a>
                <button type="button" class="btn-hub-action btn-hub-outline" onclick="copyLinkUrl('https://www.soundverse.ai/@harshverma59', 'Soundverse AI Profile')" title="Copy URL">
                    <i class="mdi mdi-content-copy mr-1"></i> Copy Link
                </button>
            </div>
        </div>
    </div>
'''
    target = 'data-category="developer" data-search="hackernoon'
    idx = about_html.find(target)
    if idx != -1:
        end_card = about_html.find('</div>\n    </div>', idx)
        if end_card != -1:
            insert_pos = end_card + len('</div>\n    </div>')
            about_html = about_html[:insert_pos] + soundverse_card_html + about_html[insert_pos:]

# Add big-judges card in page-about.html
if 'data-category="advisory" data-search="business intelligence group' not in about_html:
    big_judges_card_html = '''
    <!-- Business Intelligence Group (BIG) Judges Card -->
    <div class="col-lg-4 col-md-6 mb-4 profile-card-item" data-category="advisory" data-search="business intelligence group big judges official awards judge harsh verma industry awards panel advisory & mentorship">
        <div class="profile-hub-card h-100">
            <div class="d-flex justify-content-between align-items-start mb-3">
                <div class="d-flex align-items-center">
                    <div class="profile-card-icon-wrap mr-3">
                        <img src="images/profiles/big_judges.svg" class="profile-card-thumb-img" alt="Business Intelligence Group Judges Thumbnail" loading="lazy">
                    </div>
                    <div>
                        <span class="profile-category-pill">Advisory &amp; Mentorship</span>
                        <h5 class="profile-card-title mb-0 mt-1">Business Intelligence Group</h5>
                    </div>
                </div>
            </div>
            
            <div class="profile-card-identifier mb-2 d-flex flex-wrap align-items-center" style="gap: 4px;">
                <span class="badge badge-light border font-weight-bold text-dark px-2 py-1">
                    <i class="mdi mdi-check-circle text-primary mr-1"></i> Official Awards Judge
                </span>
                <span class="badge badge-warning text-white font-weight-bold px-2 py-1" style="background: #F76814;">
                    <i class="mdi mdi-gavel mr-1"></i> Industry Awards Panel
                </span>
            </div>

            <p class="profile-card-desc mb-3">Official Judge for Business Intelligence Group (BIG) industry recognition programs, evaluating breakthrough AI innovations, enterprise systems, and executive achievements.</p>

            <div class="d-flex align-items-center justify-content-between pt-3 border-top mt-auto flex-wrap" style="gap: 6px;">
                <a href="https://judges.bintelligence.com/harsh-verma" target="_blank" class="btn-hub-action btn-hub-primary" title="Visit Business Intelligence Group Judge Profile">
                    <i class="mdi mdi-open-in-new mr-1"></i> Open Profile
                </a>
                <button type="button" class="btn-hub-action btn-hub-outline" onclick="copyLinkUrl('https://judges.bintelligence.com/harsh-verma', 'Business Intelligence Group Judge Profile')" title="Copy URL">
                    <i class="mdi mdi-content-copy mr-1"></i> Copy Link
                </button>
            </div>
        </div>
    </div>
'''
    target = 'data-category="advisory" data-search="topmate'
    idx = about_html.find(target)
    if idx != -1:
        end_card = about_html.find('</div>\n    </div>', idx)
        if end_card != -1:
            insert_pos = end_card + len('</div>\n    </div>')
            about_html = about_html[:insert_pos] + big_judges_card_html + about_html[insert_pos:]

with open(about_html_path, 'w', encoding='utf-8') as f:
    f.write(about_html)
print("Updated page-about.html with cards and 49 Profiles count")

# 3. Update sync_site_stats.py
sync_path = os.path.join(ROOT_DIR, 'scripts', 'sync_site_stats.py')
with open(sync_path, 'r', encoding='utf-8') as f:
    sync_content = f.read()

sync_content = sync_content.replace('"profiles_count": 47,', '"profiles_count": 49,')
sync_content = sync_content.replace('"profiles_display": "47"', '"profiles_display": "49"')
sync_content = re.sub(
    r'(<span class="dropdown-item-title">)\s*(?:38|42|47|52)\+?\s*Verified Profiles Hub\s*(</span>)',
    r'\g<1>49 Verified Profiles Hub\g<2>',
    sync_content
)
sync_content = re.sub(
    r'dropdown "42 Verified Profiles Hub" -> "(?:47|49) Verified Profiles Hub"',
    'dropdown "42 Verified Profiles Hub" -> "49 Verified Profiles Hub"',
    sync_content
)
sync_content = re.sub(
    r'r\'\(\?:38\|42\|47\)',
    'r\'(?:38|42|47|49)',
    sync_content
)
sync_content = sync_content.replace(
    '<span class="dropdown-item-title">49 Verified Profiles Hub</span>',
    '<span class="dropdown-item-title">49 Verified Profiles Hub</span>'
)

with open(sync_path, 'w', encoding='utf-8') as f:
    f.write(sync_content)
print("Updated scripts/sync_site_stats.py")

# 4. Update standardize_headers_footers.py
std_path = os.path.join(ROOT_DIR, 'scripts', 'standardize_headers_footers.py')
if os.path.exists(std_path):
    with open(std_path, 'r', encoding='utf-8') as f:
        std_content = f.read()
    std_content = std_content.replace('47 Verified Profiles Hub', '49 Verified Profiles Hub')
    with open(std_path, 'w', encoding='utf-8') as f:
        f.write(std_content)
    print("Updated scripts/standardize_headers_footers.py")

# 5. Update data/copilot-knowledge.js and js/hv-copilot.js
copilot_data_path = os.path.join(ROOT_DIR, 'data', 'copilot-knowledge.js')
with open(copilot_data_path, 'r', encoding='utf-8') as f:
    copilot_data = f.read()

copilot_data = copilot_data.replace('49 Verified Academic &amp; Industry Hubs', '49 Verified Academic &amp; Industry Hubs')
copilot_data = copilot_data.replace('49 Verified Academic &amp; Industry Hubs', '49 Verified Academic &amp; Industry Hubs')

# Add entries to verifiedProfiles in copilot-knowledge if present
if 'judges.bintelligence.com' not in copilot_data:
    new_entries = '''    { name: "Business Intelligence Group (BIG) Judges", url: "https://judges.bintelligence.com/harsh-verma", id: "Official Awards Judge" },
    { name: "Soundverse AI", url: "https://www.soundverse.ai/@harshverma59", id: "@harshverma59" },'''
    copilot_data = copilot_data.replace('verifiedProfiles: [', 'verifiedProfiles: [\n' + new_entries)

with open(copilot_data_path, 'w', encoding='utf-8') as f:
    f.write(copilot_data)
print("Updated data/copilot-knowledge.js")

copilot_js_path = os.path.join(ROOT_DIR, 'js', 'hv-copilot.js')
with open(copilot_js_path, 'r', encoding='utf-8') as f:
    copilot_js = f.read()

copilot_js = copilot_js.replace('49 Verified Academic &amp; Industry Hubs', '49 Verified Academic &amp; Industry Hubs')
copilot_js = copilot_js.replace('49 Verified Academic/Professional Registries', '49 Verified Academic/Professional Registries')

with open(copilot_js_path, 'w', encoding='utf-8') as f:
    f.write(copilot_js)
print("Updated js/hv-copilot.js")

# 6. Update js/hv-site-stats.js
site_stats_path = os.path.join(ROOT_DIR, 'js', 'hv-site-stats.js')
if os.path.exists(site_stats_path):
    with open(site_stats_path, 'r', encoding='utf-8') as f:
        ss = f.read()
    ss = re.sub(r'profilesCount:\s*(?:47|42|52)', 'profilesCount: 49', ss)
    with open(site_stats_path, 'w', encoding='utf-8') as f:
        f.write(ss)
    print("Updated js/hv-site-stats.js")

# 7. Update all HTML files and generators to ensure 49 Verified Profiles Hub in navbar
import glob
for fn in glob.glob(os.path.join(ROOT_DIR, '*.html')) + glob.glob(os.path.join(ROOT_DIR, 'generate_*.py')):
    with open(fn, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    c_new = c.replace('47 Verified Profiles Hub', '49 Verified Profiles Hub')
    c_new = c_new.replace('Full Biography &amp; 49 Verified Profiles', 'Full Biography &amp; 49 Verified Profiles')
    c_new = c_new.replace('Full Biography &amp; 49 Verified Profiles', 'Full Biography &amp; 49 Verified Profiles')
    if c_new != c:
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(c_new)
        print(f"Synchronized navbar in {os.path.basename(fn)}")
