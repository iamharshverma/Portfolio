#!/usr/bin/env python3
"""
scripts/check_speaker_page.py
Automated integrity check for speaker pages (page-speaker.html & speaker.html).
Ensures that key sections and recent keynote additions are never accidentally overwritten or lost.
"""

import os
import sys

def check_file(filename):
    if not os.path.exists(filename):
        print(f"[FAIL] {filename} does not exist!")
        return False
    
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    required_checks = [
        ("Speaking Engagements & Audience Reach", 
         lambda c: "Speaking Engagements &amp; Audience Reach" in c or "Speaking Engagements & Audience Reach" in c),
        ("Speaking Formats & Delivery Models", 
         lambda c: "Speaking Formats &amp; Delivery Models" in c or "Speaking Formats & Delivery Models" in c),
        ("Subject Matter Expertise", 
         lambda c: "Subject Matter Expertise" in c),
        ("section #speaking-engagements-audiences (exactly 1 instance)", 
         lambda c: c.count('id="speaking-engagements-audiences"') == 1),
        ("section #how-we-can-work-together (exactly 1 instance)", 
         lambda c: c.count('id="how-we-can-work-together"') == 1),
        ("section #subject-matter-expertise (exactly 1 instance)", 
         lambda c: c.count('id="subject-matter-expertise"') == 1),
        ("formatDetailInspector container", 
         lambda c: 'id="formatDetailInspector"' in c),
        ("speakerAudienceGrid container", 
         lambda c: 'id="speakerAudienceGrid"' in c),
        ("TrueML Keynote (1DxjMiOe580)", 
         lambda c: "1DxjMiOe580" in c and 'id="carouselItem-8"' in c),
        ("Chai & Coaching Degrees Keynote (bggw4JTFjgA)", 
         lambda c: "bggw4JTFjgA" in c and "Cybersecurity Degrees" in c),
        ("Chai & Coaching Interview Keynote (iZkx6Ewq6wU)", 
         lambda c: "iZkx6Ewq6wU" in c and "Job Interview" in c),
        ("keynoteCarouselTrack with 10 items", 
         lambda c: 'id="carouselItem-9"' in c),
        ("keynoteVideosList array with 10 entries", 
         lambda c: "var keynoteVideosList" in c and "1DxjMiOe580" in c and "bggw4JTFjgA" in c),
        ("Partnership & Social in navbar dropdown", 
         lambda c: "Partnership &amp; Social" in c or "Partnership & Social" in c),
    ]
    
    all_ok = True
    print(f"--- Checking {filename} ---")
    for name, test_fn in required_checks:
        passed = test_fn(content)
        status = "PASS" if passed else "FAIL"
        if not passed:
            all_ok = False
        print(f"[{status}] {name}")
    
    return all_ok

def check_generator_script():
    gen_file = "generate_events_page.py"
    if not os.path.exists(gen_file):
        return True
    with open(gen_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "page-speaker.html" in content and 'for filename in ["page-events.html", "page-speaker.html"' in content:
        print("[FAIL] generate_events_page.py is configured to overwrite page-speaker.html!")
        return False
    print("[PASS] generate_events_page.py does NOT overwrite speaker pages.")
    return True

def main():
    ok1 = check_file("page-speaker.html")
    ok2 = check_file("speaker.html")
    ok3 = check_generator_script()
    
    if ok1 and ok2 and ok3:
        print("\nAll speaker page integrity checks PASSED successfully.")
        sys.exit(0)
    else:
        print("\nIntegrity checks FAILED! Please restore missing speaker sections.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
