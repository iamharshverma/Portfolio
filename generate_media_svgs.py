import os

svgs = {}

# 1. Business Insider
svgs['business_insider_badge.svg'] = '''<svg width="600" height="340" viewBox="0 0 600 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGradBI" x1="0" y1="0" x2="600" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0b132b" />
      <stop offset="50%" stop-color="#1c2541" />
      <stop offset="100%" stop-color="#0b132b" />
    </linearGradient>
    <linearGradient id="goldBI" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b" />
      <stop offset="100%" stop-color="#fbbf24" />
    </linearGradient>
    <linearGradient id="blueBI" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0066cc" />
      <stop offset="100%" stop-color="#00a3ff" />
    </linearGradient>
  </defs>
  <rect width="600" height="340" rx="16" fill="url(#bgGradBI)" />
  <rect x="1.5" y="1.5" width="597" height="337" rx="14.5" stroke="rgba(255,255,255,0.12)" stroke-width="3"/>
  <circle cx="530" cy="60" r="140" fill="#0066cc" opacity="0.12" />
  <circle cx="80" cy="280" r="120" fill="#f59e0b" opacity="0.08" />
  
  <!-- Pill -->
  <rect x="40" y="38" width="170" height="28" rx="14" fill="rgba(0,102,204,0.3)" stroke="rgba(0,163,255,0.4)" stroke-width="1.5"/>
  <text x="125" y="56" fill="#60a5fa" font-family="'Segoe UI', -apple-system, Roboto, sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">MARKETS INSIDER</text>
  
  <!-- Logo Text -->
  <text x="40" y="130" fill="#ffffff" font-family="'Georgia', serif" font-size="38" font-weight="900" letter-spacing="-0.5">BUSINESS</text>
  <text x="40" y="172" fill="url(#blueBI)" font-family="'Georgia', serif" font-size="38" font-weight="900" letter-spacing="-0.5">INSIDER</text>
  
  <rect x="40" y="196" width="520" height="1.5" fill="rgba(255,255,255,0.15)" />
  
  <text x="40" y="235" fill="#f1f5f9" font-family="'Segoe UI', -apple-system, sans-serif" font-size="18" font-weight="700">Harsh Verma • Enterprise AI &amp; Systems</text>
  <text x="40" y="265" fill="#94a3b8" font-family="'Segoe UI', -apple-system, sans-serif" font-size="14">Global Recognition Award • Rise of Agentic AI Architecture</text>
  
  <!-- Verified Badge -->
  <rect x="430" y="280" width="130" height="28" rx="6" fill="rgba(37,99,235,0.25)" stroke="#3b82f6" stroke-width="1"/>
  <text x="495" y="299" fill="#93c5fd" font-family="'Segoe UI', sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">TIER 1 PRESS</text>
</svg>'''

# 2. Yahoo Finance
svgs['yahoo_finance_badge.svg'] = '''<svg width="600" height="340" viewBox="0 0 600 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGradYF" x1="0" y1="0" x2="600" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#2d1154" />
      <stop offset="50%" stop-color="#17092b" />
      <stop offset="100%" stop-color="#0d041a" />
    </linearGradient>
    <linearGradient id="purpleGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7e22ce" />
      <stop offset="100%" stop-color="#a855f7" />
    </linearGradient>
  </defs>
  <rect width="600" height="340" rx="16" fill="url(#bgGradYF)" />
  <rect x="1.5" y="1.5" width="597" height="337" rx="14.5" stroke="rgba(168,85,247,0.25)" stroke-width="3"/>
  <circle cx="520" cy="80" r="130" fill="#a855f7" opacity="0.15" />
  
  <!-- Pill -->
  <rect x="40" y="38" width="165" height="28" rx="14" fill="rgba(126,34,206,0.3)" stroke="rgba(168,85,247,0.4)" stroke-width="1.5"/>
  <text x="122" y="56" fill="#c084fc" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">GLOBAL WIRE</text>
  
  <text x="40" y="130" fill="#ffffff" font-family="'Arial Black', sans-serif" font-size="42" font-weight="900" letter-spacing="-1">yahoo!</text>
  <text x="210" y="130" fill="#a855f7" font-family="'Segoe UI', sans-serif" font-size="34" font-weight="700">finance</text>
  
  <rect x="40" y="175" width="520" height="1.5" fill="rgba(255,255,255,0.12)" />
  
  <text x="40" y="220" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="18" font-weight="700">Cybersecurity Excellence Awards 2026</text>
  <text x="40" y="250" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="14.5">Dual Recognition for Principal AI Engineer Harsh Verma</text>
  
  <rect x="40" y="280" width="180" height="28" rx="6" fill="rgba(168,85,247,0.2)" stroke="#a855f7" stroke-width="1"/>
  <text x="130" y="299" fill="#e9d5ff" font-family="'Segoe UI', sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">NEWSFILE CORP WIRE</text>
</svg>'''

# 3. USA Today
svgs['usatoday_badge.svg'] = '''<svg width="600" height="340" viewBox="0 0 600 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGradUSA" x1="0" y1="0" x2="600" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#001838" />
      <stop offset="50%" stop-color="#002b66" />
      <stop offset="100%" stop-color="#001026" />
    </linearGradient>
  </defs>
  <rect width="600" height="340" rx="16" fill="url(#bgGradUSA)" />
  <rect x="1.5" y="1.5" width="597" height="337" rx="14.5" stroke="rgba(0,150,255,0.3)" stroke-width="3"/>
  <circle cx="500" cy="170" r="110" fill="#0096ff" opacity="0.12" />
  
  <!-- Blue USA Today Circle -->
  <circle cx="85" cy="115" r="45" fill="#0096ff" />
  <text x="150" y="112" fill="#ffffff" font-family="'Futura', 'Arial Black', sans-serif" font-size="34" font-weight="900" letter-spacing="1">USA</text>
  <text x="150" y="145" fill="#0096ff" font-family="'Futura', 'Arial Black', sans-serif" font-size="34" font-weight="900" letter-spacing="1">TODAY</text>
  
  <rect x="40" y="185" width="520" height="1.5" fill="rgba(255,255,255,0.15)" />
  
  <text x="40" y="228" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="17" font-weight="700">Identity is Replacing Network Perimeters</text>
  <text x="40" y="258" fill="#93c5fd" font-family="'Segoe UI', sans-serif" font-size="14">In The Age of Autonomous Enterprise AI Agents • Harsh Verma</text>
  
  <rect x="420" y="280" width="140" height="28" rx="6" fill="rgba(0,150,255,0.2)" stroke="#0096ff" stroke-width="1"/>
  <text x="490" y="299" fill="#bae6fd" font-family="'Segoe UI', sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">NATIONAL PRESS</text>
</svg>'''

# 4. HackerNoon
svgs['hackernoon_badge.svg'] = '''<svg width="600" height="340" viewBox="0 0 600 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGradHN" x1="0" y1="0" x2="600" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#002b11" />
      <stop offset="50%" stop-color="#001408" />
      <stop offset="100%" stop-color="#000000" />
    </linearGradient>
  </defs>
  <rect width="600" height="340" rx="16" fill="url(#bgGradHN)" />
  <rect x="1.5" y="1.5" width="597" height="337" rx="14.5" stroke="#00ff00" stroke-opacity="0.35" stroke-width="3"/>
  <circle cx="510" cy="100" r="120" fill="#00ff00" opacity="0.08" />
  
  <!-- Pixel / Hacker Art -->
  <rect x="40" y="40" width="190" height="28" rx="4" fill="rgba(0,255,0,0.15)" stroke="#00ff00" stroke-width="1.5"/>
  <text x="135" y="58" fill="#00ff00" font-family="monospace" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">&lt;EXCLUSIVE INTERVIEW&gt;</text>
  
  <text x="40" y="125" fill="#00ff00" font-family="monospace" font-size="34" font-weight="900" letter-spacing="1">HACKERNOON</text>
  <text x="40" y="160" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="20" font-weight="700">The AI Production Gap</text>
  
  <rect x="40" y="188" width="520" height="1.5" fill="rgba(0,255,0,0.25)" />
  
  <text x="40" y="230" fill="#a7f3d0" font-family="'Segoe UI', sans-serif" font-size="16" font-weight="600">"Your AI Model Isn't As Reliable As You Think"</text>
  <text x="40" y="260" fill="#94a3b8" font-family="'Segoe UI', sans-serif" font-size="13.5">Dissecting Benchmark Optimism vs Enterprise Failure Modes</text>
  
  <rect x="40" y="280" width="160" height="28" rx="4" fill="rgba(0,255,0,0.1)" stroke="#00ff00" stroke-width="1"/>
  <text x="120" y="299" fill="#00ff00" font-family="monospace" font-size="11.5" font-weight="700" text-anchor="middle">HARSH VERMA FEAT.</text>
</svg>'''

# 5. UC Berkeley SkyDeck
svgs['skydeck_badge.svg'] = '''<svg width="600" height="340" viewBox="0 0 600 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGradSD" x1="0" y1="0" x2="600" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#001a33" />
      <stop offset="50%" stop-color="#00284d" />
      <stop offset="100%" stop-color="#0b172a" />
    </linearGradient>
    <linearGradient id="goldCal" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffd54f" />
      <stop offset="100%" stop-color="#ffb300" />
    </linearGradient>
  </defs>
  <rect width="600" height="340" rx="16" fill="url(#bgGradSD)" />
  <rect x="1.5" y="1.5" width="597" height="337" rx="14.5" stroke="rgba(255,213,79,0.3)" stroke-width="3"/>
  <circle cx="510" cy="80" r="140" fill="#ffb300" opacity="0.1" />
  
  <rect x="40" y="38" width="220" height="28" rx="14" fill="rgba(255,179,0,0.2)" stroke="#ffb300" stroke-width="1.5"/>
  <text x="150" y="56" fill="#fde68a" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">UC BERKELEY SKYDECK</text>
  
  <!-- Cal Logo Style -->
  <text x="40" y="125" fill="url(#goldCal)" font-family="'Georgia', serif" font-size="34" font-weight="900">Berkeley SkyDeck</text>
  <text x="40" y="162" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="19" font-weight="700">The Era of Agentic Security</text>
  
  <rect x="40" y="188" width="520" height="1.5" fill="rgba(255,255,255,0.15)" />
  
  <text x="40" y="230" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="15.5" font-weight="600">Official Keynote • Batch 21 &amp; 22 Workshops • Advisor Network</text>
  <text x="40" y="260" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="13.5">Global Newsletter Spotlight (50K+ Network) • Harsh Verma</text>
  
  <rect x="400" y="280" width="160" height="28" rx="6" fill="rgba(255,179,0,0.2)" stroke="#ffb300" stroke-width="1"/>
  <text x="480" y="299" fill="#fde68a" font-family="'Segoe UI', sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">OFFICIAL ADVISOR</text>
</svg>'''

# 6. Times Square / Forttuna Global 100
svgs['timessquare_forttuna_badge.svg'] = '''<svg width="600" height="340" viewBox="0 0 600 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGradFT" x1="0" y1="0" x2="600" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#1f1100" />
      <stop offset="50%" stop-color="#3b2000" />
      <stop offset="100%" stop-color="#0f0900" />
    </linearGradient>
    <linearGradient id="goldFT" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b" />
      <stop offset="50%" stop-color="#fbbf24" />
      <stop offset="100%" stop-color="#d97706" />
    </linearGradient>
  </defs>
  <rect width="600" height="340" rx="16" fill="url(#bgGradFT)" />
  <rect x="1.5" y="1.5" width="597" height="337" rx="14.5" stroke="rgba(245,158,11,0.4)" stroke-width="3"/>
  <circle cx="510" cy="90" r="140" fill="#f59e0b" opacity="0.15" />
  
  <rect x="40" y="38" width="220" height="28" rx="14" fill="rgba(245,158,11,0.25)" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="150" y="56" fill="#fef08a" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">TIMES SQUARE NYC</text>
  
  <text x="40" y="125" fill="url(#goldFT)" font-family="'Georgia', serif" font-size="34" font-weight="900">FORTTUNA GLOBAL 100</text>
  <text x="40" y="162" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="19" font-weight="700">THE POWER LIST 2026 HONOREE</text>
  
  <rect x="40" y="188" width="520" height="1.5" fill="rgba(255,255,255,0.15)" />
  
  <text x="40" y="230" fill="#fef08a" font-family="'Segoe UI', sans-serif" font-size="15.5" font-weight="600">Broadway &amp; Times Square Giant Billboard Broadcast</text>
  <text x="40" y="260" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="13.5">Global Council Member • Deterministic AI &amp; Autonomous Cybersecurity</text>
  
  <rect x="410" y="280" width="150" height="28" rx="6" fill="rgba(245,158,11,0.2)" stroke="#f59e0b" stroke-width="1"/>
  <text x="485" y="299" fill="#fef08a" font-family="'Segoe UI', sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">NASDAQ SCREEN</text>
</svg>'''

# 7. Influencer Magazine UK
svgs['influencer_uk_badge.svg'] = '''<svg width="600" height="340" viewBox="0 0 600 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGradInf" x1="0" y1="0" x2="600" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#1e1035" />
      <stop offset="50%" stop-color="#2d174d" />
      <stop offset="100%" stop-color="#0f071a" />
    </linearGradient>
  </defs>
  <rect width="600" height="340" rx="16" fill="url(#bgGradInf)" />
  <rect x="1.5" y="1.5" width="597" height="337" rx="14.5" stroke="rgba(192,132,252,0.3)" stroke-width="3"/>
  <circle cx="510" cy="90" r="130" fill="#c084fc" opacity="0.12" />
  
  <rect x="40" y="38" width="180" height="28" rx="14" fill="rgba(192,132,252,0.25)" stroke="#c084fc" stroke-width="1.5"/>
  <text x="130" y="56" fill="#f3e8ff" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">LONDON • UK COVER</text>
  
  <text x="40" y="125" fill="#ffffff" font-family="'Georgia', serif" font-size="32" font-weight="900">INFLUENCER MAGAZINE</text>
  <text x="40" y="162" fill="#c084fc" font-family="'Segoe UI', sans-serif" font-size="20" font-weight="700">Tech Excellence Award Winner &amp; Cover Stories</text>
  
  <rect x="40" y="188" width="520" height="1.5" fill="rgba(255,255,255,0.15)" />
  
  <text x="40" y="230" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="15.5" font-weight="600">Double Triumph in AI &amp; Cybersecurity • The AI Production Gap</text>
  <text x="40" y="260" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="13.5">Forttuna Global 100 Power List Profile • Times Square Feature</text>
  
  <rect x="400" y="280" width="160" height="28" rx="6" fill="rgba(192,132,252,0.2)" stroke="#c084fc" stroke-width="1"/>
  <text x="480" y="299" fill="#f3e8ff" font-family="'Segoe UI', sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">MAGAZINE COVER</text>
</svg>'''

# 8. Spotify & Xraised
svgs['xraised_spotify_badge.svg'] = '''<svg width="600" height="340" viewBox="0 0 600 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGradXR" x1="0" y1="0" x2="600" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0a1f14" />
      <stop offset="50%" stop-color="#123824" />
      <stop offset="100%" stop-color="#05100a" />
    </linearGradient>
  </defs>
  <rect width="600" height="340" rx="16" fill="url(#bgGradXR)" />
  <rect x="1.5" y="1.5" width="597" height="337" rx="14.5" stroke="rgba(29,185,84,0.4)" stroke-width="3"/>
  <circle cx="510" cy="90" r="130" fill="#1db954" opacity="0.15" />
  
  <rect x="40" y="38" width="220" height="28" rx="14" fill="rgba(29,185,84,0.25)" stroke="#1db954" stroke-width="1.5"/>
  <text x="150" y="56" fill="#86efac" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">SPOTIFY &amp; AMAZON MUSIC</text>
  
  <text x="40" y="125" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="34" font-weight="900">XRAISED INTERVIEW</text>
  <text x="40" y="162" fill="#1db954" font-family="'Segoe UI', sans-serif" font-size="20" font-weight="700">Beyond the Code: AI Engineering &amp; Cyber</text>
  
  <rect x="40" y="188" width="520" height="1.5" fill="rgba(255,255,255,0.15)" />
  
  <text x="40" y="230" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="15.5" font-weight="600">Syndicated across FinancialContent &amp; AI Journ</text>
  <text x="40" y="260" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="13.5">Full Podcast &amp; Video Broadcast • Harsh Verma</text>
  
  <rect x="400" y="280" width="160" height="28" rx="6" fill="rgba(29,185,84,0.2)" stroke="#1db954" stroke-width="1"/>
  <text x="480" y="299" fill="#86efac" font-family="'Segoe UI', sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">STREAM ON SPOTIFY</text>
</svg>'''

# 9. VLink Podcast
svgs['vlink_podcast_badge.svg'] = '''<svg width="600" height="340" viewBox="0 0 600 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGradVL" x1="0" y1="0" x2="600" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="50%" stop-color="#1e3a8a" />
      <stop offset="100%" stop-color="#0f172a" />
    </linearGradient>
  </defs>
  <rect width="600" height="340" rx="16" fill="url(#bgGradVL)" />
  <rect x="1.5" y="1.5" width="597" height="337" rx="14.5" stroke="rgba(96,165,250,0.4)" stroke-width="3"/>
  <circle cx="510" cy="90" r="130" fill="#3b82f6" opacity="0.15" />
  
  <rect x="40" y="38" width="190" height="28" rx="14" fill="rgba(59,130,246,0.25)" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="135" y="56" fill="#93c5fd" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">TECH TALK WITH VLINK</text>
  
  <text x="40" y="125" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="34" font-weight="900">EPISODE 55: ENTERPRISE AI</text>
  <text x="40" y="162" fill="#60a5fa" font-family="'Segoe UI', sans-serif" font-size="19" font-weight="700">Building Solutions for Security, Scale &amp; Trust</text>
  
  <rect x="40" y="188" width="520" height="1.5" fill="rgba(255,255,255,0.15)" />
  
  <text x="40" y="230" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="15.5" font-weight="600">Full 1-Hour Guest Feature on YouTube &amp; YouTube Music</text>
  <text x="40" y="260" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="13.5">Thought Leadership Podcast • Harsh Verma</text>
  
  <rect x="400" y="280" width="160" height="28" rx="6" fill="rgba(59,130,246,0.2)" stroke="#3b82f6" stroke-width="1"/>
  <text x="480" y="299" fill="#93c5fd" font-family="'Segoe UI', sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">FULL PODCAST</text>
</svg>'''

# 10. Twill x Rocket
svgs['twill_rocket_badge.svg'] = '''<svg width="600" height="340" viewBox="0 0 600 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGradTW" x1="0" y1="0" x2="600" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#18181b" />
      <stop offset="50%" stop-color="#27272a" />
      <stop offset="100%" stop-color="#09090b" />
    </linearGradient>
  </defs>
  <rect width="600" height="340" rx="16" fill="url(#bgGradTW)" />
  <rect x="1.5" y="1.5" width="597" height="337" rx="14.5" stroke="rgba(255,255,255,0.2)" stroke-width="3"/>
  <circle cx="510" cy="90" r="130" fill="#f43f5e" opacity="0.12" />
  
  <rect x="40" y="38" width="190" height="28" rx="14" fill="rgba(244,63,94,0.25)" stroke="#f43f5e" stroke-width="1.5"/>
  <text x="135" y="56" fill="#fca5a5" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">TWILL X ROCKET</text>
  
  <text x="40" y="125" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="34" font-weight="900">VIBE SHIFT PANEL</text>
  <text x="40" y="162" fill="#f43f5e" font-family="'Segoe UI', sans-serif" font-size="19" font-weight="700">The Builders Behind the Models</text>
  
  <rect x="40" y="188" width="520" height="1.5" fill="rgba(255,255,255,0.15)" />
  
  <text x="40" y="230" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="15.5" font-weight="600">Scaling AI Engineering, Threads &amp; Culture</text>
  <text x="40" y="260" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="13.5">Full YouTube Broadcast &amp; Article Feature • Harsh Verma</text>
  
  <rect x="400" y="280" width="160" height="28" rx="6" fill="rgba(244,63,94,0.2)" stroke="#f43f5e" stroke-width="1"/>
  <text x="480" y="299" fill="#fca5a5" font-family="'Segoe UI', sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">WATCH PANEL</text>
</svg>'''

# 11. FutureAGI
svgs['futureagi_badge.svg'] = '''<svg width="600" height="340" viewBox="0 0 600 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGradFA" x1="0" y1="0" x2="600" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#022c22" />
      <stop offset="50%" stop-color="#064e3b" />
      <stop offset="100%" stop-color="#022c22" />
    </linearGradient>
  </defs>
  <rect width="600" height="340" rx="16" fill="url(#bgGradFA)" />
  <rect x="1.5" y="1.5" width="597" height="337" rx="14.5" stroke="rgba(16,185,129,0.35)" stroke-width="3"/>
  <circle cx="510" cy="90" r="130" fill="#10b981" opacity="0.12" />
  
  <rect x="40" y="38" width="180" height="28" rx="14" fill="rgba(16,185,129,0.25)" stroke="#10b981" stroke-width="1.5"/>
  <text x="130" y="56" fill="#6ee7b7" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">FUTUREAGI TALK</text>
  
  <text x="40" y="125" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="30" font-weight="900">Powering Cybersecurity</text>
  <text x="40" y="162" fill="#34d399" font-family="'Segoe UI', sans-serif" font-size="20" font-weight="700">With GenAI &amp; Intelligent Agents</text>
  
  <rect x="40" y="188" width="520" height="1.5" fill="rgba(255,255,255,0.15)" />
  
  <text x="40" y="230" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="15.5" font-weight="600">Autonomous Agentic Reasoning &amp; Guardrails</text>
  <text x="40" y="260" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="13.5">Luma Invited Masterclass &amp; YouTube Feature • Harsh Verma</text>
  
  <rect x="400" y="280" width="160" height="28" rx="6" fill="rgba(16,185,129,0.2)" stroke="#10b981" stroke-width="1"/>
  <text x="480" y="299" fill="#6ee7b7" font-family="'Segoe UI', sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">WATCH TALK</text>
</svg>'''

# 12. TrueML Talks
svgs['trueml_badge.svg'] = '''<svg width="600" height="340" viewBox="0 0 600 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGradTM" x1="0" y1="0" x2="600" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#1e1b4b" />
      <stop offset="50%" stop-color="#312e81" />
      <stop offset="100%" stop-color="#0f172a" />
    </linearGradient>
  </defs>
  <rect width="600" height="340" rx="16" fill="url(#bgGradTM)" />
  <rect x="1.5" y="1.5" width="597" height="337" rx="14.5" stroke="rgba(129,140,248,0.35)" stroke-width="3"/>
  <circle cx="510" cy="90" r="130" fill="#818cf8" opacity="0.12" />
  
  <rect x="40" y="38" width="190" height="28" rx="14" fill="rgba(129,140,248,0.25)" stroke="#818cf8" stroke-width="1.5"/>
  <text x="135" y="56" fill="#c7d2fe" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">TRUEML TALKS #35</text>
  
  <text x="40" y="125" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="30" font-weight="900">Big Data &amp; ML Practices</text>
  <text x="40" y="162" fill="#a5b4fc" font-family="'Segoe UI', sans-serif" font-size="20" font-weight="700">At Palo Alto Networks</text>
  
  <rect x="40" y="188" width="520" height="1.5" fill="rgba(255,255,255,0.15)" />
  
  <text x="40" y="230" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="15.5" font-weight="600">TrueFoundry Technical Keynote &amp; Deep-Dive</text>
  <text x="40" y="260" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="13.5">High-Throughput Feature Pipelines • Harsh Verma</text>
  
  <rect x="400" y="280" width="160" height="28" rx="6" fill="rgba(129,140,248,0.2)" stroke="#818cf8" stroke-width="1"/>
  <text x="480" y="299" fill="#c7d2fe" font-family="'Segoe UI', sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">WATCH TALK</text>
</svg>'''

# 13. SZ 179 Quantum
svgs['quantum_battleground_badge.svg'] = '''<svg width="600" height="340" viewBox="0 0 600 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGradQ" x1="0" y1="0" x2="600" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#1a0033" />
      <stop offset="50%" stop-color="#330066" />
      <stop offset="100%" stop-color="#0d001a" />
    </linearGradient>
  </defs>
  <rect width="600" height="340" rx="16" fill="url(#bgGradQ)" />
  <rect x="1.5" y="1.5" width="597" height="337" rx="14.5" stroke="rgba(192,132,252,0.35)" stroke-width="3"/>
  <circle cx="510" cy="90" r="130" fill="#c084fc" opacity="0.12" />
  
  <rect x="40" y="38" width="190" height="28" rx="14" fill="rgba(192,132,252,0.25)" stroke="#c084fc" stroke-width="1.5"/>
  <text x="135" y="56" fill="#e9d5ff" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">SZ 179 SYMPOSIUM</text>
  
  <text x="40" y="125" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="30" font-weight="900">The Digital Battleground</text>
  <text x="40" y="162" fill="#c084fc" font-family="'Segoe UI', sans-serif" font-size="20" font-weight="700">Quantum Computing &amp; Cybersecurity</text>
  
  <rect x="40" y="188" width="520" height="1.5" fill="rgba(255,255,255,0.15)" />
  
  <text x="40" y="230" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="15.5" font-weight="600">Top Voices Unite • Post-Quantum Cryptography Panel</text>
  <text x="40" y="260" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="13.5">2-Part YouTube Series &amp; Luma Summit • Harsh Verma</text>
  
  <rect x="400" y="280" width="160" height="28" rx="6" fill="rgba(192,132,252,0.2)" stroke="#c084fc" stroke-width="1"/>
  <text x="480" y="299" fill="#e9d5ff" font-family="'Segoe UI', sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">WATCH PANEL</text>
</svg>'''

# 14. Barchart
svgs['barchart_badge.svg'] = '''<svg width="600" height="340" viewBox="0 0 600 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGradBC" x1="0" y1="0" x2="600" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0f2942" />
      <stop offset="50%" stop-color="#1e4e79" />
      <stop offset="100%" stop-color="#0a1c2e" />
    </linearGradient>
  </defs>
  <rect width="600" height="340" rx="16" fill="url(#bgGradBC)" />
  <rect x="1.5" y="1.5" width="597" height="337" rx="14.5" stroke="rgba(56,189,248,0.35)" stroke-width="3"/>
  <circle cx="510" cy="90" r="130" fill="#38bdf8" opacity="0.12" />
  
  <rect x="40" y="38" width="180" height="28" rx="14" fill="rgba(56,189,248,0.25)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="130" y="56" fill="#bae6fd" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">BARCHART FINANCIAL</text>
  
  <text x="40" y="125" fill="#ffffff" font-family="'Arial Black', sans-serif" font-size="34" font-weight="900">BARCHART.COM</text>
  <text x="40" y="162" fill="#38bdf8" font-family="'Segoe UI', sans-serif" font-size="18.5" font-weight="700">From a Model Problem to a Control Problem</text>
  
  <rect x="40" y="188" width="520" height="1.5" fill="rgba(255,255,255,0.15)" />
  
  <text x="40" y="230" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="15.5" font-weight="600">Financial Markets Analysis of Enterprise AI Infrastructure</text>
  <text x="40" y="260" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="13.5">Principal Software Engineer Harsh Verma • MarketersMedia</text>
  
  <rect x="400" y="280" width="160" height="28" rx="6" fill="rgba(56,189,248,0.2)" stroke="#38bdf8" stroke-width="1"/>
  <text x="480" y="299" fill="#bae6fd" font-family="'Segoe UI', sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">READ ARTICLE</text>
</svg>'''

# 15. Street Insider
svgs['streetinsider_badge.svg'] = '''<svg width="600" height="340" viewBox="0 0 600 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGradSI" x1="0" y1="0" x2="600" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0b1b2b" />
      <stop offset="50%" stop-color="#173552" />
      <stop offset="100%" stop-color="#081420" />
    </linearGradient>
  </defs>
  <rect width="600" height="340" rx="16" fill="url(#bgGradSI)" />
  <rect x="1.5" y="1.5" width="597" height="337" rx="14.5" stroke="rgba(96,165,250,0.35)" stroke-width="3"/>
  
  <rect x="40" y="38" width="190" height="28" rx="14" fill="rgba(96,165,250,0.25)" stroke="#60a5fa" stroke-width="1.5"/>
  <text x="135" y="56" fill="#bfdbfe" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">WALL STREET WIRE</text>
  
  <text x="40" y="125" fill="#ffffff" font-family="'Georgia', serif" font-size="34" font-weight="900">StreetInsider.com</text>
  <text x="40" y="162" fill="#60a5fa" font-family="'Segoe UI', sans-serif" font-size="19" font-weight="700">Human-AI Collaboration Gains Enterprise Attention</text>
  
  <rect x="40" y="188" width="520" height="1.5" fill="rgba(255,255,255,0.15)" />
  
  <text x="40" y="230" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="15.5" font-weight="600">The Financial Capital • Tech Excellence Nomination</text>
  <text x="40" y="260" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="13.5">Principal AI Engineer Harsh Verma • Supervisory Loops</text>
  
  <rect x="400" y="280" width="160" height="28" rx="6" fill="rgba(96,165,250,0.2)" stroke="#60a5fa" stroke-width="1"/>
  <text x="480" y="299" fill="#bfdbfe" font-family="'Segoe UI', sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">FINANCIAL WIRE</text>
</svg>'''

# 16. EIN News
svgs['ein_news_badge.svg'] = '''<svg width="600" height="340" viewBox="0 0 600 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGradEIN" x1="0" y1="0" x2="600" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#1e1b4b" />
      <stop offset="50%" stop-color="#2e1065" />
      <stop offset="100%" stop-color="#0f0728" />
    </linearGradient>
  </defs>
  <rect width="600" height="340" rx="16" fill="url(#bgGradEIN)" />
  <rect x="1.5" y="1.5" width="597" height="337" rx="14.5" stroke="rgba(216,180,254,0.35)" stroke-width="3"/>
  
  <rect x="40" y="38" width="220" height="28" rx="14" fill="rgba(216,180,254,0.25)" stroke="#d8b4fe" stroke-width="1.5"/>
  <text x="150" y="56" fill="#f3e8ff" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">EIN PRESSWIRE &amp; KNOX NEWS</text>
  
  <text x="40" y="125" fill="#ffffff" font-family="'Arial Black', sans-serif" font-size="32" font-weight="900">EIN TECH NEWS</text>
  <text x="40" y="162" fill="#d8b4fe" font-family="'Segoe UI', sans-serif" font-size="19" font-weight="700">Harsh Verma Wins Tech Excellence Award 2026</text>
  
  <rect x="40" y="188" width="520" height="1.5" fill="rgba(255,255,255,0.15)" />
  
  <text x="40" y="230" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="15.5" font-weight="600">Syndicated across USA Today Network &amp; Global Wires</text>
  <text x="40" y="260" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="13.5">Influencer Magazine Awards • London • Harsh Verma</text>
  
  <rect x="400" y="280" width="160" height="28" rx="6" fill="rgba(216,180,254,0.2)" stroke="#d8b4fe" stroke-width="1"/>
  <text x="480" y="299" fill="#f3e8ff" font-family="'Segoe UI', sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">PRESS RELEASE</text>
</svg>'''

# 17. Primeful Insights
svgs['primeful_badge.svg'] = '''<svg width="600" height="340" viewBox="0 0 600 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGradPI" x1="0" y1="0" x2="600" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#1c1917" />
      <stop offset="50%" stop-color="#292524" />
      <stop offset="100%" stop-color="#0c0a09" />
    </linearGradient>
  </defs>
  <rect width="600" height="340" rx="16" fill="url(#bgGradPI)" />
  <rect x="1.5" y="1.5" width="597" height="337" rx="14.5" stroke="rgba(245,158,11,0.4)" stroke-width="3"/>
  <circle cx="510" cy="90" r="130" fill="#f59e0b" opacity="0.12" />
  
  <rect x="40" y="38" width="190" height="28" rx="14" fill="rgba(245,158,11,0.25)" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="135" y="56" fill="#fde68a" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">INDUSTRY ICONS 2026</text>
  
  <text x="40" y="125" fill="#ffffff" font-family="'Georgia', serif" font-size="34" font-weight="900">Primeful Insights</text>
  <text x="40" y="162" fill="#fbbf24" font-family="'Segoe UI', sans-serif" font-size="20" font-weight="700">Industry Icon Feature: Harsh Verma</text>
  
  <rect x="40" y="188" width="520" height="1.5" fill="rgba(255,255,255,0.15)" />
  
  <text x="40" y="230" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="15.5" font-weight="600">Executive Thought Leadership &amp; Engineering Mentorship</text>
  <text x="40" y="260" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="13.5">Leading the Next Wave of Enterprise AI Innovation</text>
  
  <rect x="400" y="280" width="160" height="28" rx="6" fill="rgba(245,158,11,0.2)" stroke="#f59e0b" stroke-width="1"/>
  <text x="480" y="299" fill="#fde68a" font-family="'Segoe UI', sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">COVER STORY</text>
</svg>'''

# 18. CIO Insightful
svgs['cio_insightful_badge.svg'] = '''<svg width="600" height="340" viewBox="0 0 600 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGradCIO" x1="0" y1="0" x2="600" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#111827" />
      <stop offset="50%" stop-color="#1f2937" />
      <stop offset="100%" stop-color="#030712" />
    </linearGradient>
  </defs>
  <rect width="600" height="340" rx="16" fill="url(#bgGradCIO)" />
  <rect x="1.5" y="1.5" width="597" height="337" rx="14.5" stroke="rgba(245,158,11,0.4)" stroke-width="3"/>
  
  <rect x="40" y="38" width="220" height="28" rx="14" fill="rgba(245,158,11,0.25)" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="150" y="56" fill="#fde68a" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">TOP 5 LEADERS 2026</text>
  
  <text x="40" y="125" fill="#ffffff" font-family="'Georgia', serif" font-size="34" font-weight="900">CIO Insightful</text>
  <text x="40" y="162" fill="#fbbf24" font-family="'Segoe UI', sans-serif" font-size="19" font-weight="700">Top 5 Most Dynamic Leaders Shaping the Future</text>
  
  <rect x="40" y="188" width="520" height="1.5" fill="rgba(255,255,255,0.15)" />
  
  <text x="40" y="230" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="15.5" font-weight="600">Enterprise AI Strategy &amp; Zero-Trust Architectures</text>
  <text x="40" y="260" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="13.5">Honoring Visionary Technical Executive Harsh Verma</text>
  
  <rect x="400" y="280" width="160" height="28" rx="6" fill="rgba(245,158,11,0.2)" stroke="#f59e0b" stroke-width="1"/>
  <text x="480" y="299" fill="#fde68a" font-family="'Segoe UI', sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">TOP 5 RANKING</text>
</svg>'''

# 19. Life Page India
svgs['lifepage_badge.svg'] = '''<svg width="600" height="340" viewBox="0 0 600 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGradLP" x1="0" y1="0" x2="600" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#064e3b" />
      <stop offset="50%" stop-color="#047857" />
      <stop offset="100%" stop-color="#022c22" />
    </linearGradient>
  </defs>
  <rect width="600" height="340" rx="16" fill="url(#bgGradLP)" />
  <rect x="1.5" y="1.5" width="597" height="337" rx="14.5" stroke="rgba(110,231,183,0.35)" stroke-width="3"/>
  
  <rect x="40" y="38" width="190" height="28" rx="14" fill="rgba(110,231,183,0.25)" stroke="#6ee7b7" stroke-width="1.5"/>
  <text x="135" y="56" fill="#a7f3d0" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">CAREER SPOTLIGHT</text>
  
  <text x="40" y="125" fill="#ffffff" font-family="'Georgia', serif" font-size="34" font-weight="900">LifePage India</text>
  <text x="40" y="162" fill="#a7f3d0" font-family="'Segoe UI', sans-serif" font-size="19" font-weight="700">Software Development &amp; Engineering Careers</text>
  
  <rect x="40" y="188" width="520" height="1.5" fill="rgba(255,255,255,0.15)" />
  
  <text x="40" y="230" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="15.5" font-weight="600">Life Experience, Engineering Craft &amp; Systems Architecture</text>
  <text x="40" y="260" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="13.5">Harsh Verma • Career Advisory &amp; Video Guide</text>
  
  <rect x="400" y="280" width="160" height="28" rx="6" fill="rgba(110,231,183,0.2)" stroke="#6ee7b7" stroke-width="1"/>
  <text x="480" y="299" fill="#a7f3d0" font-family="'Segoe UI', sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">APP INTERVIEW</text>
</svg>'''

# 20. Chai & Coaching
svgs['chai_coaching_badge.svg'] = '''<svg width="600" height="340" viewBox="0 0 600 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGradCC" x1="0" y1="0" x2="600" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#451a03" />
      <stop offset="50%" stop-color="#78350f" />
      <stop offset="100%" stop-color="#291002" />
    </linearGradient>
  </defs>
  <rect width="600" height="340" rx="16" fill="url(#bgGradCC)" />
  <rect x="1.5" y="1.5" width="597" height="337" rx="14.5" stroke="rgba(251,191,36,0.35)" stroke-width="3"/>
  <circle cx="510" cy="90" r="130" fill="#f59e0b" opacity="0.12" />
  
  <rect x="40" y="38" width="190" height="28" rx="14" fill="rgba(251,191,36,0.25)" stroke="#fbbf24" stroke-width="1.5"/>
  <text x="135" y="56" fill="#fde68a" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">YOUTUBE MASTERCLASS</text>
  
  <text x="40" y="125" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="34" font-weight="900">CHAI &amp; COACHING</text>
  <text x="40" y="162" fill="#fbbf24" font-family="'Segoe UI', sans-serif" font-size="19" font-weight="700">Cybersecurity Careers &amp; Job Interview Mastery</text>
  
  <rect x="40" y="188" width="520" height="1.5" fill="rgba(255,255,255,0.15)" />
  
  <text x="40" y="230" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="15.5" font-weight="600">2 Full Video Episodes • Tech Career Strategy &amp; Hiring</text>
  <text x="40" y="260" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="13.5">Harsh Verma • Convincing Recruiters &amp; System Leadership</text>
  
  <rect x="400" y="280" width="160" height="28" rx="6" fill="rgba(251,191,36,0.2)" stroke="#fbbf24" stroke-width="1"/>
  <text x="480" y="299" fill="#fde68a" font-family="'Segoe UI', sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">WATCH ON YOUTUBE</text>
</svg>'''

# 21. Google Developer Experts
svgs['google_experts_badge.svg'] = '''<svg width="600" height="340" viewBox="0 0 600 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGradGDE" x1="0" y1="0" x2="600" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="50%" stop-color="#1e293b" />
      <stop offset="100%" stop-color="#0b0f19" />
    </linearGradient>
  </defs>
  <rect width="600" height="340" rx="16" fill="url(#bgGradGDE)" />
  <rect x="1.5" y="1.5" width="597" height="337" rx="14.5" stroke="rgba(66,133,244,0.4)" stroke-width="3"/>
  
  <rect x="40" y="38" width="220" height="28" rx="14" fill="rgba(66,133,244,0.25)" stroke="#4285f4" stroke-width="1.5"/>
  <text x="150" y="56" fill="#93c5fd" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">GOOGLE EXPERTS DIRECTORY</text>
  
  <text x="40" y="125" fill="#4285f4" font-family="'Segoe UI', sans-serif" font-size="34" font-weight="900">Google <tspan fill="#ea4335">Developer</tspan> <tspan fill="#fbbc05">Experts</tspan></text>
  <text x="40" y="162" fill="#34a853" font-family="'Segoe UI', sans-serif" font-size="20" font-weight="700">Official Global Directory Listing: Harsh Verma</text>
  
  <rect x="40" y="188" width="520" height="1.5" fill="rgba(255,255,255,0.15)" />
  
  <text x="40" y="230" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="15.5" font-weight="600">Recognized Expert in Google Cloud &amp; Machine Learning</text>
  <text x="40" y="260" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="13.5">Community Leadership, Technical Speaking &amp; Architecture</text>
  
  <rect x="400" y="280" width="160" height="28" rx="6" fill="rgba(66,133,244,0.2)" stroke="#4285f4" stroke-width="1"/>
  <text x="480" y="299" fill="#93c5fd" font-family="'Segoe UI', sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">VIEW GDE PROFILE</text>
</svg>'''

# 22. Cybersecurity Excellence Awards
svgs['cybersecurity_excellence_badge.svg'] = '''<svg width="600" height="340" viewBox="0 0 600 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGradCEA" x1="0" y1="0" x2="600" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#311042" />
      <stop offset="50%" stop-color="#4a154b" />
      <stop offset="100%" stop-color="#1b0826" />
    </linearGradient>
  </defs>
  <rect width="600" height="340" rx="16" fill="url(#bgGradCEA)" />
  <rect x="1.5" y="1.5" width="597" height="337" rx="14.5" stroke="rgba(216,180,254,0.35)" stroke-width="3"/>
  <circle cx="510" cy="90" r="130" fill="#c084fc" opacity="0.12" />
  
  <rect x="40" y="38" width="220" height="28" rx="14" fill="rgba(216,180,254,0.25)" stroke="#d8b4fe" stroke-width="1.5"/>
  <text x="150" y="56" fill="#f3e8ff" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">AI INNOVATOR OF THE YEAR</text>
  
  <text x="40" y="125" fill="#ffffff" font-family="'Georgia', serif" font-size="30" font-weight="900">Cybersecurity Excellence</text>
  <text x="40" y="162" fill="#d8b4fe" font-family="'Segoe UI', sans-serif" font-size="20" font-weight="700">Dual Recognition &amp; Candidate Showcase 2026</text>
  
  <rect x="40" y="188" width="520" height="1.5" fill="rgba(255,255,255,0.15)" />
  
  <text x="40" y="230" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="15.5" font-weight="600">Honoring Breakthrough Contributions in Threat AI &amp; Copilots</text>
  <text x="40" y="260" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="13.5">Palo Alto Networks • Harsh Verma</text>
  
  <rect x="400" y="280" width="160" height="28" rx="6" fill="rgba(216,180,254,0.2)" stroke="#d8b4fe" stroke-width="1"/>
  <text x="480" y="299" fill="#f3e8ff" font-family="'Segoe UI', sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">VIEW CANDIDATE</text>
</svg>'''

# 23. Noble Tech Awards
svgs['noble_tech_badge.svg'] = '''<svg width="600" height="340" viewBox="0 0 600 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGradNTA" x1="0" y1="0" x2="600" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#1f1402" />
      <stop offset="50%" stop-color="#3d2806" />
      <stop offset="100%" stop-color="#140d02" />
    </linearGradient>
  </defs>
  <rect width="600" height="340" rx="16" fill="url(#bgGradNTA)" />
  <rect x="1.5" y="1.5" width="597" height="337" rx="14.5" stroke="rgba(245,158,11,0.4)" stroke-width="3"/>
  <circle cx="510" cy="90" r="130" fill="#f59e0b" opacity="0.15" />
  
  <rect x="40" y="38" width="190" height="28" rx="14" fill="rgba(245,158,11,0.25)" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="135" y="56" fill="#fef08a" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">GOLD WINNER #145</text>
  
  <text x="40" y="125" fill="#fef08a" font-family="'Georgia', serif" font-size="34" font-weight="900">Noble Technology Awards</text>
  <text x="40" y="162" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="19" font-weight="700">Inaugural Laureate Announcement &amp; Muse.world</text>
  
  <rect x="40" y="188" width="520" height="1.5" fill="rgba(255,255,255,0.15)" />
  
  <text x="40" y="230" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="15.5" font-weight="600">Leading Next-Gen Secure AI Innovation Globally</text>
  <text x="40" y="260" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="13.5">Harsh Verma • Multi-Agent Security Architectures</text>
  
  <rect x="400" y="280" width="160" height="28" rx="6" fill="rgba(245,158,11,0.2)" stroke="#f59e0b" stroke-width="1"/>
  <text x="480" y="299" fill="#fef08a" font-family="'Segoe UI', sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">GLOBAL WINNER</text>
</svg>'''

# 24. Time Business News
svgs['time_business_badge.svg'] = '''<svg width="600" height="340" viewBox="0 0 600 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGradTBN" x1="0" y1="0" x2="600" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#022c22" />
      <stop offset="50%" stop-color="#064e3b" />
      <stop offset="100%" stop-color="#021d17" />
    </linearGradient>
  </defs>
  <rect width="600" height="340" rx="16" fill="url(#bgGradTBN)" />
  <rect x="1.5" y="1.5" width="597" height="337" rx="14.5" stroke="rgba(52,211,153,0.35)" stroke-width="3"/>
  
  <rect x="40" y="38" width="200" height="28" rx="14" fill="rgba(52,211,153,0.25)" stroke="#34d399" stroke-width="1.5"/>
  <text x="140" y="56" fill="#a7f3d0" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">IFGICT FELLOWSHIP</text>
  
  <text x="40" y="125" fill="#ffffff" font-family="'Georgia', serif" font-size="34" font-weight="900">Time Business News</text>
  <text x="40" y="162" fill="#34d399" font-family="'Segoe UI', sans-serif" font-size="19" font-weight="700">Global Green ICT &amp; Sustainable AI Leadership</text>
  
  <rect x="40" y="188" width="520" height="1.5" fill="rgba(255,255,255,0.15)" />
  
  <text x="40" y="230" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="15.5" font-weight="600">Elevated to Distinguished Fellow of IFGICT</text>
  <text x="40" y="260" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="13.5">Harsh Verma • Green Compute &amp; UN Sustainable Goals</text>
  
  <rect x="400" y="280" width="160" height="28" rx="6" fill="rgba(52,211,153,0.2)" stroke="#34d399" stroke-width="1"/>
  <text x="480" y="299" fill="#a7f3d0" font-family="'Segoe UI', sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">READ ARTICLE</text>
</svg>'''

# 25. Health Tech Week
svgs['healthtech_badge.svg'] = '''<svg width="600" height="340" viewBox="0 0 600 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGradHT" x1="0" y1="0" x2="600" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#082f49" />
      <stop offset="50%" stop-color="#0c4a6e" />
      <stop offset="100%" stop-color="#031d2e" />
    </linearGradient>
  </defs>
  <rect width="600" height="340" rx="16" fill="url(#bgGradHT)" />
  <rect x="1.5" y="1.5" width="597" height="337" rx="14.5" stroke="rgba(56,189,248,0.35)" stroke-width="3"/>
  
  <rect x="40" y="38" width="210" height="28" rx="14" fill="rgba(56,189,248,0.25)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="145" y="56" fill="#bae6fd" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">KEYNOTE SPEAKER</text>
  
  <text x="40" y="125" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="34" font-weight="900">Health Tech Week</text>
  <text x="40" y="162" fill="#38bdf8" font-family="'Segoe UI', sans-serif" font-size="19" font-weight="700">Official Speaker: Harsh Verma</text>
  
  <rect x="40" y="188" width="520" height="1.5" fill="rgba(255,255,255,0.15)" />
  
  <text x="40" y="230" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="15.5" font-weight="600">Clinical AI Architectures, HIPAA &amp; Privacy Telemetry</text>
  <text x="40" y="260" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="13.5">Keynote Authority on Zero-Trust Healthcare Systems</text>
  
  <rect x="400" y="280" width="160" height="28" rx="6" fill="rgba(56,189,248,0.2)" stroke="#38bdf8" stroke-width="1"/>
  <text x="480" y="299" fill="#bae6fd" font-family="'Segoe UI', sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">SPEAKER BIO</text>
</svg>'''

# 26. NY Weekly Journal
svgs['nyweekly_badge.svg'] = '''<svg width="600" height="340" viewBox="0 0 600 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGradNYW" x1="0" y1="0" x2="600" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#1e1e24" />
      <stop offset="50%" stop-color="#2b2b36" />
      <stop offset="100%" stop-color="#121216" />
    </linearGradient>
  </defs>
  <rect width="600" height="340" rx="16" fill="url(#bgGradNYW)" />
  <rect x="1.5" y="1.5" width="597" height="337" rx="14.5" stroke="rgba(245,158,11,0.35)" stroke-width="3"/>
  <circle cx="510" cy="90" r="130" fill="#f59e0b" opacity="0.12" />
  
  <rect x="40" y="38" width="200" height="28" rx="14" fill="rgba(245,158,11,0.25)" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="140" y="56" fill="#fde68a" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">EDITORIAL PROFILE</text>
  
  <text x="40" y="125" fill="#ffffff" font-family="'Georgia', serif" font-size="34" font-weight="900">NY Weekly Journal</text>
  <text x="40" y="162" fill="#fbbf24" font-family="'Segoe UI', sans-serif" font-size="18" font-weight="700">The Engineer Rewriting Rules: AI Beyond the Code</text>
  
  <rect x="40" y="188" width="520" height="1.5" fill="rgba(255,255,255,0.15)" />
  
  <text x="40" y="230" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="15.5" font-weight="600">Inside the World &amp; Engineering Philosophy of Harsh Verma</text>
  <text x="40" y="260" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="13.5">Silicon Valley Principal AI Engineer • Systems Thinking</text>
  
  <rect x="400" y="280" width="160" height="28" rx="6" fill="rgba(245,158,11,0.2)" stroke="#f59e0b" stroke-width="1"/>
  <text x="480" y="299" fill="#fde68a" font-family="'Segoe UI', sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">READ ARTICLE</text>
</svg>'''

# 27. NewsBreak
svgs['newsbreak_badge.svg'] = '''<svg width="600" height="340" viewBox="0 0 600 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGradNB" x1="0" y1="0" x2="600" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#450a0a" />
      <stop offset="50%" stop-color="#7f1d1d" />
      <stop offset="100%" stop-color="#2a0505" />
    </linearGradient>
  </defs>
  <rect width="600" height="340" rx="16" fill="url(#bgGradNB)" />
  <rect x="1.5" y="1.5" width="597" height="337" rx="14.5" stroke="rgba(248,113,113,0.35)" stroke-width="3"/>
  <circle cx="510" cy="90" r="130" fill="#ef4444" opacity="0.12" />
  
  <rect x="40" y="38" width="200" height="28" rx="14" fill="rgba(239,68,68,0.25)" stroke="#ef4444" stroke-width="1.5"/>
  <text x="140" y="56" fill="#fecaca" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">SYNDICATED TECH WIRE</text>
  
  <text x="40" y="125" fill="#ffffff" font-family="'Arial Black', sans-serif" font-size="34" font-weight="900">NewsBreak</text>
  <text x="40" y="162" fill="#f87171" font-family="'Segoe UI', sans-serif" font-size="18.5" font-weight="700">Unified Framework for Enterprise AI</text>
  
  <rect x="40" y="188" width="520" height="1.5" fill="rgba(255,255,255,0.15)" />
  
  <text x="40" y="230" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="15.5" font-weight="600">From Orchestration to Trust, Identity &amp; Observability</text>
  <text x="40" y="260" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="13.5">AI Expert Harsh Verma • MarketersMedia Syndication</text>
  
  <rect x="400" y="280" width="160" height="28" rx="6" fill="rgba(239,68,68,0.2)" stroke="#ef4444" stroke-width="1"/>
  <text x="480" y="299" fill="#fecaca" font-family="'Segoe UI', sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">READ ON NEWSBREAK</text>
</svg>'''

os.makedirs('images/media', exist_ok=True)

for filename, content in svgs.items():
    path = os.path.join('images/media', filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip())
    print(f"Generated SVG: {path}")

print(f"Total SVGs created: {len(svgs)}")
