import os

# Create SVG badges
badges = {
    "stanford_scholar.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <defs>
    <linearGradient id="g-stanford" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8C1515"/>
      <stop offset="100%" stop-color="#4D0000"/>
    </linearGradient>
    <linearGradient id="gold-leaf" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FCD34D"/>
      <stop offset="100%" stop-color="#F59E0B"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" rx="16" fill="url(#g-stanford)"/>
  <rect x="8" y="8" width="384" height="224" rx="12" fill="none" stroke="#F59E0B" stroke-width="2" stroke-dasharray="6,4" opacity="0.6"/>
  <!-- Laurel Wreath -->
  <g fill="url(#gold-leaf)" opacity="0.9" transform="translate(200, 75) scale(0.65)">
    <path d="M-45,-20 C-60,0 -50,30 -20,45 C-10,35 -20,15 -30,0 Z"/>
    <path d="M-60,10 C-75,30 -60,60 -30,70 C-22,58 -30,40 -40,25 Z"/>
    <path d="M45,-20 C60,0 50,30 20,45 C10,35 20,15 30,0 Z"/>
    <path d="M60,10 C75,30 60,60 30,70 C22,58 30,40 40,25 Z"/>
    <circle cx="0" cy="55" r="7"/>
    <path d="M0,0 L8,24 L32,24 L12,38 L20,62 L0,48 L-20,62 L-12,38 L-32,24 L-8,24 Z" fill="url(#gold-leaf)"/>
  </g>
  <text x="200" y="150" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="600" text-anchor="middle" letter-spacing="3">STANFORD GRADUATE SCHOOL OF BUSINESS</text>
  <text x="200" y="180" fill="#FDE68A" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="19" font-weight="800" text-anchor="middle" letter-spacing="1">DISTINGUISHED SCHOLAR</text>
  <text x="200" y="206" fill="#FCA5A5" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="600" text-anchor="middle" letter-spacing="2">HONORARY EXECUTIVE FELLOW</text>
</svg>''',

    "mit_bootcamp.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <defs>
    <linearGradient id="g-mit" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E293B"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" rx="16" fill="url(#g-mit)"/>
  <rect x="8" y="8" width="384" height="224" rx="12" fill="none" stroke="#A31F34" stroke-width="2" opacity="0.7"/>
  <!-- MIT Stripes Geometric Icon -->
  <g transform="translate(145, 30)">
    <rect x="0" y="0" width="16" height="55" fill="#A31F34" rx="2"/>
    <rect x="24" y="0" width="16" height="35" fill="#FFFFFF" rx="2"/>
    <rect x="48" y="0" width="16" height="55" fill="#A31F34" rx="2"/>
    <rect x="72" y="20" width="16" height="35" fill="#FFFFFF" rx="2"/>
    <rect x="96" y="0" width="16" height="55" fill="#A31F34" rx="2"/>
  </g>
  <text x="200" y="125" fill="#CBD5E1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="3">MASSACHUSETTS INSTITUTE OF TECHNOLOGY</text>
  <text x="200" y="156" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="18" font-weight="800" text-anchor="middle">INNOVATION &amp; LEADERSHIP</text>
  <text x="200" y="180" fill="#F87171" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1.5">CERTIFICATE OF RECOGNITION</text>
  <text x="200" y="206" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" text-anchor="middle">Convex Healthcare Product MVP Architecture</text>
</svg>''',

    "google_hackathon.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <defs>
    <linearGradient id="g-ghack" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A"/>
      <stop offset="100%" stop-color="#1E1B4B"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" rx="16" fill="url(#g-ghack)"/>
  <rect x="8" y="8" width="384" height="224" rx="12" fill="none" stroke="#4285F4" stroke-width="1.5" opacity="0.6"/>
  <!-- Google 4-Color Shield -->
  <g transform="translate(200, 58) scale(0.85)">
    <circle cx="-30" cy="0" r="10" fill="#4285F4"/>
    <circle cx="-10" cy="0" r="10" fill="#EA4335"/>
    <circle cx="10" cy="0" r="10" fill="#FBBC05"/>
    <circle cx="30" cy="0" r="10" fill="#34A853"/>
    <path d="M0,-25 L15,-10 L-15,-10 Z" fill="#60A5FA"/>
  </g>
  <text x="200" y="125" fill="#93C5FD" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="2">GOOGLE &amp; HACKMAKERS GLOBAL HACK</text>
  <text x="200" y="156" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="18" font-weight="800" text-anchor="middle">LEAD HACKATHON MENTOR</text>
  <text x="200" y="180" fill="#34D399" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">DIGITAL DEFENSE WORLD HACK</text>
  <text x="200" y="206" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" text-anchor="middle">Verified on Badgr &amp; Global Hack Registry</text>
</svg>''',

    "ata_gtr.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <defs>
    <linearGradient id="g-ata" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#312E81"/>
      <stop offset="100%" stop-color="#1E1B4B"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" rx="16" fill="url(#g-ata)"/>
  <rect x="8" y="8" width="384" height="224" rx="12" fill="none" stroke="#F59E0B" stroke-width="1.5" opacity="0.6"/>
  <g transform="translate(200, 52)">
    <circle cx="0" cy="0" r="26" fill="#F59E0B" opacity="0.2"/>
    <path d="M-12,-15 L12,-15 L16,10 L0,20 L-16,10 Z" fill="#F59E0B"/>
    <polygon points="0,-8 5,6 -6,-3 6,-3 -5,6" fill="#312E81"/>
  </g>
  <text x="200" y="120" fill="#FDE68A" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="2">AGILE TESTING ALLIANCE · #ATAGTR2017</text>
  <text x="200" y="152" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="18" font-weight="800" text-anchor="middle">CERTIFICATE OF HONOUR</text>
  <text x="200" y="178" fill="#C7D2FE" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Keynote Speaker: Developed 'HikeRunner' Tool</text>
  <text x="200" y="204" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" text-anchor="middle">High-Scale Enterprise Performance Architecture</text>
</svg>''',

    "forttuna_powerlist.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <defs>
    <linearGradient id="g-fort" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B132B"/>
      <stop offset="100%" stop-color="#1C2541"/>
    </linearGradient>
    <linearGradient id="gold-fort" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FCD34D"/>
      <stop offset="50%" stop-color="#F59E0B"/>
      <stop offset="100%" stop-color="#B45309"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" rx="16" fill="url(#g-fort)"/>
  <rect x="8" y="8" width="384" height="224" rx="12" fill="none" stroke="url(#gold-fort)" stroke-width="2"/>
  <!-- Crown / Star -->
  <g transform="translate(200, 52) scale(0.9)" fill="url(#gold-fort)">
    <path d="M-30,15 L-20,-15 L-5,5 L10,-18 L25,5 L40,-15 L50,15 Z" transform="translate(-10,0)"/>
    <circle cx="-20" cy="-18" r="3"/>
    <circle cx="0" cy="-21" r="3.5"/>
    <circle cx="20" cy="-18" r="3"/>
  </g>
  <text x="200" y="118" fill="url(#gold-fort)" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="3">FORTTUNA GLOBAL 100</text>
  <text x="200" y="150" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="20" font-weight="800" text-anchor="middle" letter-spacing="1">THE POWER LIST 2026</text>
  <text x="200" y="176" fill="#FDE68A" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1.5">OFFICIAL CERTIFICATE OF RECOGNITION</text>
  <text x="200" y="204" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" text-anchor="middle">Top Global Influencers Shaping AI &amp; Innovation</text>
</svg>''',

    "forbes_recognition.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <defs>
    <linearGradient id="g-forbes" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#000000"/>
      <stop offset="100%" stop-color="#1E293B"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" rx="16" fill="url(#g-forbes)"/>
  <rect x="8" y="8" width="384" height="224" rx="12" fill="none" stroke="#2563EB" stroke-width="1.5" opacity="0.6"/>
  <text x="200" y="70" fill="#FFFFFF" font-family="Georgia, 'Times New Roman', serif" font-size="34" font-weight="bold" font-style="italic" text-anchor="middle" letter-spacing="1">Forbes</text>
  <text x="200" y="98" fill="#60A5FA" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="3">TECHNOLOGY COUNCIL</text>
  <text x="200" y="145" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="17" font-weight="800" text-anchor="middle">EXCELLENCE RECOGNITION</text>
  <text x="200" y="172" fill="#93C5FD" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="600" text-anchor="middle">AI &amp; Enterprise Software Engineering</text>
  <text x="200" y="202" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" text-anchor="middle">In Collaboration with Palo Alto Networks</text>
</svg>''',

    "global_recognition_award.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <defs>
    <linearGradient id="g-gra" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#450A0A"/>
      <stop offset="100%" stop-color="#1C1917"/>
    </linearGradient>
    <linearGradient id="gold-gra" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FCD34D"/>
      <stop offset="100%" stop-color="#D97706"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" rx="16" fill="url(#g-gra)"/>
  <rect x="8" y="8" width="384" height="224" rx="12" fill="none" stroke="url(#gold-gra)" stroke-width="2"/>
  <!-- Trophy Emblem -->
  <g transform="translate(200, 52) scale(0.85)" fill="url(#gold-gra)">
    <path d="M-22,-20 L22,-20 L18,5 C14,18 0,22 0,22 C0,22 -14,18 -18,5 Z"/>
    <path d="M-22,-15 C-32,-15 -35,-5 -22,0 L-20,-5 Z"/>
    <path d="M22,-15 C32,-15 35,-5 22,0 L20,-5 Z"/>
    <rect x="-6" y="22" width="12" height="12"/>
    <rect x="-16" y="34" width="32" height="6" rx="2"/>
  </g>
  <text x="200" y="122" fill="url(#gold-gra)" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="2.5">2026 GLOBAL RECOGNITION AWARDS™</text>
  <text x="200" y="152" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="18" font-weight="800" text-anchor="middle">AI INNOVATOR OF THE YEAR</text>
  <text x="200" y="178" fill="#FCA5A5" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Palo Alto Networks Enterprise AI Leadership</text>
  <text x="200" y="204" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" text-anchor="middle">Featured in Business Insider &amp; Markets Insider</text>
</svg>''',

    "stevie_bronze.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <defs>
    <linearGradient id="g-stevie-b" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E1B4B"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>
    <linearGradient id="bronze-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F59E0B"/>
      <stop offset="50%" stop-color="#B45309"/>
      <stop offset="100%" stop-color="#78350F"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" rx="16" fill="url(#g-stevie-b)"/>
  <rect x="8" y="8" width="384" height="224" rx="12" fill="none" stroke="url(#bronze-grad)" stroke-width="2"/>
  <!-- Medal Emblem -->
  <g transform="translate(200, 52) scale(0.85)">
    <circle cx="0" cy="0" r="24" fill="url(#bronze-grad)"/>
    <circle cx="0" cy="0" r="19" fill="#1E1B4B"/>
    <text x="0" y="6" fill="#FBBF24" font-family="serif" font-size="18" font-weight="bold" text-anchor="middle">★</text>
    <path d="M-12,-24 L-18,-42 L-6,-42 Z" fill="#B45309"/>
    <path d="M12,-24 L18,-42 L6,-42 Z" fill="#B45309"/>
  </g>
  <text x="200" y="120" fill="url(#bronze-grad)" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="2">AMERICAN BUSINESS AWARDS® · STEVIE AWARDS</text>
  <text x="200" y="150" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="17" font-weight="800" text-anchor="middle">AI CYBERSECURITY EXPERT OF THE YEAR</text>
  <text x="200" y="176" fill="#FCD34D" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="800" text-anchor="middle" letter-spacing="1">BRONZE STEVIE® WINNER</text>
  <text x="200" y="204" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" text-anchor="middle">Palo Alto Networks AI Security Architecture</text>
</svg>''',

    "stevie_gold.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <defs>
    <linearGradient id="g-stevie-g" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#022C22"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>
    <linearGradient id="gold-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FDE68A"/>
      <stop offset="50%" stop-color="#F59E0B"/>
      <stop offset="100%" stop-color="#B45309"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" rx="16" fill="url(#g-stevie-g)"/>
  <rect x="8" y="8" width="384" height="224" rx="12" fill="none" stroke="url(#gold-grad)" stroke-width="2"/>
  <!-- Gold Stevie Figure Emblem -->
  <g transform="translate(200, 50) scale(0.9)" fill="url(#gold-grad)">
    <circle cx="0" cy="-16" r="8"/>
    <path d="M-12,-4 L12,-4 L8,24 L-8,24 Z"/>
    <path d="M-22,-10 L-10,-4 L-16,14 Z"/>
    <path d="M22,-10 L10,-4 L16,14 Z"/>
    <rect x="-18" y="26" width="36" height="5" rx="2"/>
  </g>
  <text x="200" y="120" fill="url(#gold-grad)" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="2">AMERICAN BUSINESS AWARDS® 2026</text>
  <text x="200" y="150" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="18" font-weight="800" text-anchor="middle">AI INNOVATOR OF THE YEAR</text>
  <text x="200" y="176" fill="#FDE68A" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="800" text-anchor="middle" letter-spacing="1">OFFICIAL STEVIE® AWARDS WINNER</text>
  <text x="200" y="204" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" text-anchor="middle">Premier Business &amp; Technology Awards</text>
</svg>''',

    "ioasd_lifetime.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <defs>
    <linearGradient id="g-ioasd-l" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#022C22"/>
      <stop offset="100%" stop-color="#064E3B"/>
    </linearGradient>
    <linearGradient id="gold-ioasd" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FCD34D"/>
      <stop offset="100%" stop-color="#D97706"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" rx="16" fill="url(#g-ioasd-l)"/>
  <rect x="8" y="8" width="384" height="224" rx="12" fill="none" stroke="url(#gold-ioasd)" stroke-width="2"/>
  <g transform="translate(200, 50) scale(0.85)" fill="url(#gold-ioasd)">
    <circle cx="0" cy="0" r="26" fill="none" stroke="url(#gold-ioasd)" stroke-width="2"/>
    <path d="M-15,-8 L0,-20 L15,-8 L15,15 L-15,15 Z"/>
    <circle cx="0" cy="2" r="5" fill="#022C22"/>
  </g>
  <text x="200" y="118" fill="url(#gold-ioasd)" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="2">IOASD ANNUAL AWARDS</text>
  <text x="200" y="148" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="18" font-weight="800" text-anchor="middle">LIFETIME ACHIEVEMENT AWARD</text>
  <text x="200" y="174" fill="#6EE7B7" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">HIGHEST SCIENTIFIC DISTINCTION</text>
  <text x="200" y="202" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" text-anchor="middle">Intl. Org. for Academic &amp; Scientific Development</text>
</svg>''',

    "ioasd_research_excellence.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <defs>
    <linearGradient id="g-ioasd-r" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E3A8A"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" rx="16" fill="url(#g-ioasd-r)"/>
  <rect x="8" y="8" width="384" height="224" rx="12" fill="none" stroke="#60A5FA" stroke-width="1.5" opacity="0.7"/>
  <g transform="translate(200, 52) scale(0.85)" fill="#60A5FA">
    <path d="M-20,-10 L0,-24 L20,-10 L20,18 L-20,18 Z"/>
    <circle cx="0" cy="4" r="6" fill="#1E3A8A"/>
  </g>
  <text x="200" y="120" fill="#93C5FD" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="2">IOASD ANNUAL AWARDS</text>
  <text x="200" y="150" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="17" font-weight="800" text-anchor="middle">AWARD OF EXCELLENCE IN RESEARCH</text>
  <text x="200" y="176" fill="#FCD34D" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Peer-Reviewed Computational Science &amp; CogML</text>
  <text x="200" y="204" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" text-anchor="middle">International Scientific Recognition</text>
</svg>''',

    "ioasd_outstanding_researcher.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <defs>
    <linearGradient id="g-ioasd-o" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#134E4A"/>
      <stop offset="100%" stop-color="#042F2E"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" rx="16" fill="url(#g-ioasd-o)"/>
  <rect x="8" y="8" width="384" height="224" rx="12" fill="none" stroke="#2DD4BF" stroke-width="1.5" opacity="0.7"/>
  <g transform="translate(200, 52) scale(0.85)" fill="#2DD4BF">
    <circle cx="0" cy="0" r="22" fill="none" stroke="#2DD4BF" stroke-width="2"/>
    <text x="0" y="7" font-family="serif" font-size="20" font-weight="bold" text-anchor="middle" fill="#2DD4BF">★</text>
  </g>
  <text x="200" y="120" fill="#99F6E4" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="2">IOASD ANNUAL AWARDS</text>
  <text x="200" y="150" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="17" font-weight="800" text-anchor="middle">OUTSTANDING RESEARCHER AWARD</text>
  <text x="200" y="176" fill="#5EEAD4" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="600" text-anchor="middle">High Impact AI Research &amp; Scholarly Review</text>
  <text x="200" y="204" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" text-anchor="middle">IOASD International Board of Fellows</text>
</svg>''',

    "cybersecurity_silver.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <defs>
    <linearGradient id="g-cea-s" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A"/>
      <stop offset="100%" stop-color="#334155"/>
    </linearGradient>
    <linearGradient id="silver-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F8FAFC"/>
      <stop offset="50%" stop-color="#CBD5E1"/>
      <stop offset="100%" stop-color="#64748B"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" rx="16" fill="url(#g-cea-s)"/>
  <rect x="8" y="8" width="384" height="224" rx="12" fill="none" stroke="url(#silver-grad)" stroke-width="2"/>
  <!-- Shield Icon -->
  <g transform="translate(200, 52) scale(0.85)" fill="url(#silver-grad)">
    <path d="M0,-24 L22,-12 L22,8 C22,20 0,30 0,30 C0,30 -22,20 -22,8 L-22,-12 Z"/>
    <path d="M0,-16 L14,-7 L14,7 C14,15 0,22 0,22 C0,22 -14,15 -14,7 L-14,-7 Z" fill="#0F172A"/>
  </g>
  <text x="200" y="120" fill="url(#silver-grad)" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="2">2026 CYBERSECURITY EXCELLENCE AWARDS</text>
  <text x="200" y="148" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="16" font-weight="800" text-anchor="middle">AI SECURITY INNOVATOR OF THE YEAR</text>
  <text x="200" y="174" fill="#E2E8F0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="800" text-anchor="middle" letter-spacing="1">SILVER AWARD WINNER</text>
  <text x="200" y="202" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" text-anchor="middle">Palo Alto Networks Autonomous Defense Innovations</text>
</svg>''',

    "cybersecurity_community.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <defs>
    <linearGradient id="g-cea-c" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3B0764"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>
    <linearGradient id="gold-comm" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FDE047"/>
      <stop offset="100%" stop-color="#CA8A04"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" rx="16" fill="url(#g-cea-c)"/>
  <rect x="8" y="8" width="384" height="224" rx="12" fill="none" stroke="url(#gold-comm)" stroke-width="2"/>
  <!-- People / Star Icon -->
  <g transform="translate(200, 52) scale(0.85)" fill="url(#gold-comm)">
    <circle cx="0" cy="-10" r="10"/>
    <path d="M-16,14 C-16,5 16,5 16,14 Z"/>
    <circle cx="-22" cy="-5" r="7"/>
    <path d="M-34,16 C-34,10 -10,10 -10,16 Z"/>
    <circle cx="22" cy="-5" r="7"/>
    <path d="M10,16 C10,10 34,10 34,16 Z"/>
  </g>
  <text x="200" y="118" fill="url(#gold-comm)" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="2">WORLD'S TOP CYBERSECURITY ACHIEVEMENTS</text>
  <text x="200" y="148" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="17" font-weight="800" text-anchor="middle">COMMUNITY CHOICE AWARD WINNER</text>
  <text x="200" y="174" fill="#FDE047" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" text-anchor="middle">AI &amp; Cybersecurity Global Innovation</text>
  <text x="200" y="202" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" text-anchor="middle">Featured on Yahoo Finance &amp; Newsfile Corp</text>
</svg>''',

    "globee_silver.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <defs>
    <linearGradient id="g-globee" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E1B4B"/>
      <stop offset="100%" stop-color="#4C1D95"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" rx="16" fill="url(#g-globee)"/>
  <rect x="8" y="8" width="384" height="224" rx="12" fill="none" stroke="#A78BFA" stroke-width="1.5" opacity="0.8"/>
  <!-- Globe / AI Icon -->
  <g transform="translate(200, 52) scale(0.85)" stroke="#A78BFA" stroke-width="2" fill="none">
    <circle cx="0" cy="0" r="22"/>
    <ellipse cx="0" cy="0" rx="10" ry="22"/>
    <line x1="-22" y1="0" x2="22" y2="0"/>
    <circle cx="0" cy="0" r="4" fill="#F59E0B"/>
  </g>
  <text x="200" y="120" fill="#DDD6FE" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="2">2ND ANNUAL 2026 GLOBEE AWARDS FOR AI</text>
  <text x="200" y="148" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="16" font-weight="800" text-anchor="middle">INTELLIGENT SOFTWARE SYSTEMS</text>
  <text x="200" y="174" fill="#E2E8F0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="800" text-anchor="middle" letter-spacing="1">SILVER GLOBEE® WINNER</text>
  <text x="200" y="202" fill="#C4B5FD" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" text-anchor="middle">AI Expertise &amp; Innovation Excellence</text>
</svg>''',

    "nobel_tech_awards.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <defs>
    <linearGradient id="g-nobel" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B0F19"/>
      <stop offset="100%" stop-color="#1E293B"/>
    </linearGradient>
    <linearGradient id="gold-nobel" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FEF08A"/>
      <stop offset="50%" stop-color="#EAB308"/>
      <stop offset="100%" stop-color="#A16207"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" rx="16" fill="url(#g-nobel)"/>
  <rect x="8" y="8" width="384" height="224" rx="12" fill="none" stroke="url(#gold-nobel)" stroke-width="2"/>
  <!-- Gold Medal Medallion -->
  <g transform="translate(200, 52) scale(0.9)" fill="url(#gold-nobel)">
    <circle cx="0" cy="0" r="26" fill="none" stroke="url(#gold-nobel)" stroke-width="3"/>
    <path d="M-8,-14 L8,-14 L12,4 L0,14 L-12,4 Z"/>
    <circle cx="0" cy="-2" r="4" fill="#0B0F19"/>
  </g>
  <text x="200" y="120" fill="url(#gold-nobel)" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="2">NOBEL TECHNOLOGY AWARDS 2026</text>
  <text x="200" y="148" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="18" font-weight="800" text-anchor="middle">GOLD WINNER (#145)</text>
  <text x="200" y="174" fill="#FEF08A" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">GLOBEE WINNERS CIRCLE &amp; MUSE HONOREE</text>
  <text x="200" y="202" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" text-anchor="middle">Pioneering Secure Enterprise AI Next-Gen Innovation</text>
</svg>''',

    "ais_innovator.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <defs>
    <linearGradient id="g-ais" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E1B4B"/>
      <stop offset="100%" stop-color="#0E7490"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" rx="16" fill="url(#g-ais)"/>
  <rect x="8" y="8" width="384" height="224" rx="12" fill="none" stroke="#22D3EE" stroke-width="1.5" opacity="0.7"/>
  <!-- Brain / Neural Node Icon -->
  <g transform="translate(200, 52) scale(0.85)" fill="#22D3EE">
    <circle cx="0" cy="0" r="7"/>
    <circle cx="-18" cy="-10" r="5"/>
    <circle cx="18" cy="-10" r="5"/>
    <circle cx="-15" cy="14" r="5"/>
    <circle cx="15" cy="14" r="5"/>
    <line x1="0" y1="0" x2="-18" y2="-10" stroke="#22D3EE" stroke-width="2"/>
    <line x1="0" y1="0" x2="18" y2="-10" stroke="#22D3EE" stroke-width="2"/>
    <line x1="0" y1="0" x2="-15" y2="14" stroke="#22D3EE" stroke-width="2"/>
    <line x1="0" y1="0" x2="15" y2="14" stroke="#22D3EE" stroke-width="2"/>
  </g>
  <text x="200" y="120" fill="#67E8F9" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="2">INTERNATIONAL AI DATA SCIENTIST AWARDS</text>
  <text x="200" y="150" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="18" font-weight="800" text-anchor="middle">AI INNOVATOR AWARD 2026</text>
  <text x="200" y="176" fill="#A5F3FC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Contributions &amp; Professional Work in AI</text>
  <text x="200" y="204" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" text-anchor="middle">AIS 2026 Global Data Science Honors</text>
</svg>''',

    "influencer_tech_excellence.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <defs>
    <linearGradient id="g-influencer" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#881337"/>
      <stop offset="100%" stop-color="#1E1B4B"/>
    </linearGradient>
    <linearGradient id="rose-gold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FDA4AF"/>
      <stop offset="100%" stop-color="#FB7185"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" rx="16" fill="url(#g-influencer)"/>
  <rect x="8" y="8" width="384" height="224" rx="12" fill="none" stroke="url(#rose-gold)" stroke-width="2"/>
  <!-- Award Diamond -->
  <g transform="translate(200, 52) scale(0.85)" fill="url(#rose-gold)">
    <polygon points="0,-22 22,0 0,22 -22,0"/>
    <polygon points="0,-12 12,0 0,12 -12,0" fill="#881337"/>
  </g>
  <text x="200" y="120" fill="#FDA4AF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="2">INFLUENCER MAGAZINE AWARDS UK 2026</text>
  <text x="200" y="150" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="18" font-weight="800" text-anchor="middle">TECH EXCELLENCE AWARD</text>
  <text x="200" y="176" fill="#FECDD3" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" text-anchor="middle">DOUBLE TRIUMPH IN AI &amp; CYBERSECURITY</text>
  <text x="200" y="204" fill="#CBD5E1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" text-anchor="middle">Featured on AI Journ, EIN News, Knox News</text>
</svg>''',

    "ifgict_fellowship_award.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <defs>
    <linearGradient id="g-ifgict" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#064E3B"/>
      <stop offset="100%" stop-color="#022C22"/>
    </linearGradient>
    <linearGradient id="gold-ifgict" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FCD34D"/>
      <stop offset="100%" stop-color="#F59E0B"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" rx="16" fill="url(#g-ifgict)"/>
  <rect x="8" y="8" width="384" height="224" rx="12" fill="none" stroke="url(#gold-ifgict)" stroke-width="2"/>
  <g transform="translate(200, 52) scale(0.85)" fill="url(#gold-ifgict)">
    <circle cx="0" cy="0" r="24" fill="none" stroke="url(#gold-ifgict)" stroke-width="2"/>
    <path d="M-10,-10 C-5,-18 5,-18 10,-10 C15,0 0,15 0,15 C0,15 -15,0 -10,-10 Z"/>
  </g>
  <text x="200" y="120" fill="url(#gold-ifgict)" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="2">INTERNATIONAL FEDERATION OF GICT</text>
  <text x="200" y="150" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="18" font-weight="800" text-anchor="middle">IFGICT FELLOWSHIP AWARD</text>
  <text x="200" y="176" fill="#A7F3D0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" text-anchor="middle">SUSTAINABLE ICT &amp; AI LEADERSHIP</text>
  <text x="200" y="204" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" text-anchor="middle">Featured in Time Business News</text>
</svg>''',

    "jrtcse_excellence.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <defs>
    <linearGradient id="g-jrtcse" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E3A8A"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" rx="16" fill="url(#g-jrtcse)"/>
  <rect x="8" y="8" width="384" height="224" rx="12" fill="none" stroke="#F59E0B" stroke-width="1.5" opacity="0.7"/>
  <!-- Journal Book Icon -->
  <g transform="translate(200, 52) scale(0.85)" fill="#F59E0B">
    <path d="M-22,-16 L0,-8 L22,-16 L22,14 L0,22 L-22,14 Z"/>
    <line x1="0" y1="-8" x2="0" y2="22" stroke="#1E3A8A" stroke-width="2"/>
  </g>
  <text x="200" y="120" fill="#FDE68A" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="2">JRTCSE JOURNAL</text>
  <text x="200" y="148" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="16" font-weight="800" text-anchor="middle">CERTIFICATE OF EXCELLENCE</text>
  <text x="200" y="174" fill="#93C5FD" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Peer Review &amp; Editorial Research Contribution</text>
  <text x="200" y="202" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" text-anchor="middle">Journal of Recent Trends in Computer Science &amp; Eng.</text>
</svg>''',

    "skydeck_advisor_elevation.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <defs>
    <linearGradient id="g-sky" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#002046"/>
      <stop offset="100%" stop-color="#003262"/>
    </linearGradient>
    <linearGradient id="gold-sky" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FDB515"/>
      <stop offset="100%" stop-color="#C4820A"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" rx="16" fill="url(#g-sky)"/>
  <rect x="8" y="8" width="384" height="224" rx="12" fill="none" stroke="url(#gold-sky)" stroke-width="2"/>
  <!-- SkyDeck Rocket / Star -->
  <g transform="translate(200, 52) scale(0.85)" fill="url(#gold-sky)">
    <path d="M0,-24 C10,-15 12,0 12,16 L0,12 L-12,16 C-12,0 -10,-15 0,-24 Z"/>
    <polygon points="0,14 4,24 -4,24" fill="#EA580C"/>
  </g>
  <text x="200" y="120" fill="url(#gold-sky)" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="2">UNIVERSITY OF CALIFORNIA, BERKELEY</text>
  <text x="200" y="148" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="17" font-weight="800" text-anchor="middle">GLOBAL ADVISOR &amp; SELECTION COMMITTEE</text>
  <text x="200" y="174" fill="#FDE047" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" text-anchor="middle">ELEVATED FROM MENTOR · 2025–2026 BATCH</text>
  <text x="200" y="202" fill="#93C5FD" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" text-anchor="middle">UC Berkeley SkyDeck Global Startup Accelerator</text>
</svg>''',

    "gde_cloud_ai.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <defs>
    <linearGradient id="g-gde" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#202124"/>
      <stop offset="100%" stop-color="#171717"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" rx="16" fill="url(#g-gde)"/>
  <rect x="8" y="8" width="384" height="224" rx="12" fill="none" stroke="#4285F4" stroke-width="1.5" opacity="0.8"/>
  <!-- Google Expert Icon -->
  <g transform="translate(200, 52) scale(0.9)">
    <polygon points="0,-22 20,-10 20,12 0,22 -20,12 -20,-10" fill="#4285F4"/>
    <text x="0" y="7" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">&lt;/&gt;</text>
  </g>
  <text x="200" y="120" fill="#93C5FD" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="2">GOOGLE DEVELOPERS</text>
  <text x="200" y="148" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="18" font-weight="800" text-anchor="middle">GOOGLE DEVELOPER EXPERT (GDE)</text>
  <text x="200" y="174" fill="#34D399" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">CLOUD AI · TOP 100 WORLDWIDE</text>
  <text x="200" y="202" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" text-anchor="middle">Global Recognition for Incident Response &amp; AI</text>
</svg>''',

    "adplist_1000min.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <defs>
    <linearGradient id="g-adp1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0A1128"/>
      <stop offset="100%" stop-color="#1C1917"/>
    </linearGradient>
    <linearGradient id="adp-coral" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF7A6E"/>
      <stop offset="100%" stop-color="#FF4336"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" rx="16" fill="url(#g-adp1)"/>
  <rect x="8" y="8" width="384" height="224" rx="12" fill="none" stroke="url(#adp-coral)" stroke-width="2"/>
  <!-- Clock / Heart Icon -->
  <g transform="translate(200, 50) scale(0.85)" fill="url(#adp-coral)">
    <circle cx="0" cy="0" r="22" fill="none" stroke="url(#adp-coral)" stroke-width="3"/>
    <line x1="0" y1="0" x2="0" y2="-12" stroke="url(#adp-coral)" stroke-width="3" stroke-linecap="round"/>
    <line x1="0" y1="0" x2="10" y2="0" stroke="url(#adp-coral)" stroke-width="3" stroke-linecap="round"/>
  </g>
  <text x="200" y="118" fill="url(#adp-coral)" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="2">ADPLIST GLOBAL MENTORSHIP</text>
  <text x="200" y="148" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="18" font-weight="800" text-anchor="middle">1,000+ MENTORSHIP MINUTES</text>
  <text x="200" y="174" fill="#FCA5A5" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" text-anchor="middle">MILESTONE CERTIFICATE OF ACHIEVEMENT</text>
  <text x="200" y="202" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" text-anchor="middle">16+ Hours Guiding Global Engineers &amp; Founders</text>
</svg>''',

    "adplist_25sessions.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <defs>
    <linearGradient id="g-adp2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E1B4B"/>
      <stop offset="100%" stop-color="#312E81"/>
    </linearGradient>
    <linearGradient id="adp-purple" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#C084FC"/>
      <stop offset="100%" stop-color="#9333EA"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" rx="16" fill="url(#g-adp2)"/>
  <rect x="8" y="8" width="384" height="224" rx="12" fill="none" stroke="url(#adp-purple)" stroke-width="2"/>
  <!-- Sessions Checkmarks Icon -->
  <g transform="translate(200, 50) scale(0.85)" fill="url(#adp-purple)">
    <circle cx="0" cy="0" r="22" fill="none" stroke="url(#adp-purple)" stroke-width="3"/>
    <polyline points="-10,0 -3,8 11,-6" fill="none" stroke="url(#adp-purple)" stroke-width="3" stroke-linecap="round"/>
  </g>
  <text x="200" y="118" fill="url(#adp-purple)" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="2">ADPLIST GLOBAL MENTORSHIP</text>
  <text x="200" y="148" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="18" font-weight="800" text-anchor="middle">25+ MENTORSHIP SESSIONS</text>
  <text x="200" y="174" fill="#DDD6FE" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" text-anchor="middle">MILESTONE CERTIFICATE OF ACHIEVEMENT</text>
  <text x="200" y="202" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" text-anchor="middle">Volunteer Mentorship to 1M+ Global Learning Community</text>
</svg>'''
}

for filename, content in badges.items():
    path = os.path.join("images", "awards", filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
print(f"Created {len(badges)} awards SVG badges in images/awards/")
