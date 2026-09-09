const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

async function buildBookCovers() {
  const booksDir = path.join(__dirname, '../images/books');
  if (!fs.existsSync(booksDir)) {
    fs.mkdirSync(booksDir, { recursive: true });
  }

  // 1. AI VS AI - Front Cover (1200 x 1800)
  const aiVsAiFrontSvg = `
  <svg width="1200" height="1800" viewBox="0 0 1200 1800" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <linearGradient id="bgGrad" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#020408"/>
        <stop offset="40%" stop-color="#050a14"/>
        <stop offset="100%" stop-color="#010306"/>
      </linearGradient>
      <radialGradient id="blueGlow" cx="25%" cy="45%" r="35%">
        <stop offset="0%" stop-color="#00b4d8" stop-opacity="0.35"/>
        <stop offset="60%" stop-color="#0077b6" stop-opacity="0.12"/>
        <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
      </radialGradient>
      <radialGradient id="redGlow" cx="75%" cy="45%" r="35%">
        <stop offset="0%" stop-color="#ff0055" stop-opacity="0.35"/>
        <stop offset="60%" stop-color="#d00000" stop-opacity="0.12"/>
        <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
      </radialGradient>
      <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="6" result="blur"/>
        <feMerge>
          <feMergeNode in="blur"/>
          <feMergeNode in="SourceGraphic"/>
        </feMerge>
      </filter>
      <filter id="subtleGlow">
        <feGaussianBlur stdDeviation="3" result="blur"/>
        <feMerge>
          <feMergeNode in="blur"/>
          <feMergeNode in="SourceGraphic"/>
        </feMerge>
      </filter>
    </defs>

    <!-- Background -->
    <rect width="1200" height="1800" fill="url(#bgGrad)"/>
    <circle cx="300" cy="850" r="450" fill="url(#blueGlow)"/>
    <circle cx="900" cy="850" r="450" fill="url(#redGlow)"/>

    <!-- Subtle Tech Circuit Grid -->
    <g stroke="rgba(255,255,255,0.04)" stroke-width="1.5">
      <line x1="0" y1="200" x2="1200" y2="200"/>
      <line x1="0" y1="400" x2="1200" y2="400"/>
      <line x1="0" y1="600" x2="1200" y2="600"/>
      <line x1="0" y1="1200" x2="1200" y2="1200"/>
      <line x1="0" y1="1400" x2="1200" y2="1400"/>
      <line x1="0" y1="1600" x2="1200" y2="1600"/>
      <line x1="200" y1="0" x2="200" y2="1800"/>
      <line x1="400" y1="0" x2="400" y2="1800"/>
      <line x1="600" y1="0" x2="600" y2="1800"/>
      <line x1="800" y1="0" x2="800" y2="1800"/>
      <line x1="1000" y1="0" x2="1000" y2="1800"/>
    </g>

    <!-- Neural Constellation Heads Illustration -->
    <!-- Blue Network (Left Head Silhouette Facing Right) -->
    <g filter="url(#glow)">
      <!-- Constellation Nodes & Links Blue -->
      <path d="M 280 620 L 330 580 L 400 590 L 450 630 L 490 690 L 510 760 L 520 830 L 490 890 L 520 960 L 530 1020 L 480 1080 L 440 1120 L 380 1150 L 330 1200" fill="none" stroke="#38bdf8" stroke-width="2.5" opacity="0.85"/>
      <path d="M 280 620 L 290 730 L 320 840 L 330 960 L 360 1060 L 380 1150" fill="none" stroke="#0ea5e9" stroke-width="2" opacity="0.65"/>
      <path d="M 330 580 L 370 680 L 400 780 L 420 900 L 440 1020 L 440 1120" fill="none" stroke="#38bdf8" stroke-width="1.8" opacity="0.7"/>
      <path d="M 400 590 L 430 710 L 460 820 L 470 940 L 490 1040" fill="none" stroke="#7dd3fc" stroke-width="1.5" opacity="0.75"/>
      <path d="M 450 630 L 370 680 L 320 840 L 420 900 L 490 890" fill="none" stroke="#0284c7" stroke-width="1.2" opacity="0.6"/>
      <path d="M 490 690 L 460 820 L 520 830 L 420 900 L 520 960" fill="none" stroke="#38bdf8" stroke-width="1.5" opacity="0.8"/>
      <path d="M 510 760 L 400 780 L 330 960 L 470 940 L 530 1020" fill="none" stroke="#00f2fe" stroke-width="1.5" opacity="0.75"/>

      <!-- Blue Glowing Nodes -->
      <circle cx="280" cy="620" r="5" fill="#e0f2fe"/>
      <circle cx="330" cy="580" r="6" fill="#bae6fd"/>
      <circle cx="400" cy="590" r="7" fill="#7dd3fc"/>
      <circle cx="450" cy="630" r="8" fill="#38bdf8"/>
      <circle cx="490" cy="690" r="7" fill="#e0f2fe"/>
      <circle cx="510" cy="760" r="9" fill="#ffffff"/>
      <circle cx="520" cy="830" r="8" fill="#7dd3fc"/>
      <circle cx="490" cy="890" r="8.5" fill="#38bdf8"/>
      <circle cx="520" cy="960" r="9" fill="#ffffff"/>
      <circle cx="530" cy="1020" r="8" fill="#7dd3fc"/>
      <circle cx="480" cy="1080" r="7" fill="#38bdf8"/>
      <circle cx="440" cy="1120" r="6" fill="#bae6fd"/>
      <circle cx="380" cy="1150" r="6" fill="#7dd3fc"/>
      <circle cx="330" cy="1200" r="5" fill="#38bdf8"/>
      
      <circle cx="370" cy="680" r="5.5" fill="#38bdf8"/>
      <circle cx="430" cy="710" r="6" fill="#e0f2fe"/>
      <circle cx="400" cy="780" r="6.5" fill="#7dd3fc"/>
      <circle cx="460" cy="820" r="7" fill="#ffffff"/>
      <circle cx="420" cy="900" r="7.5" fill="#38bdf8"/>
      <circle cx="470" cy="940" r="7" fill="#7dd3fc"/>
      <circle cx="440" cy="1020" r="6" fill="#38bdf8"/>
      <circle cx="290" cy="730" r="4.5" fill="#0ea5e9"/>
      <circle cx="320" cy="840" r="5.5" fill="#38bdf8"/>
      <circle cx="330" cy="960" r="5" fill="#0284c7"/>
      <circle cx="360" cy="1060" r="5.5" fill="#38bdf8"/>
    </g>

    <!-- Red Network (Right Head Silhouette Facing Left) -->
    <g filter="url(#glow)">
      <!-- Constellation Nodes & Links Red -->
      <path d="M 920 620 L 870 580 L 800 590 L 750 630 L 710 690 L 690 760 L 680 830 L 710 890 L 680 960 L 670 1020 L 720 1080 L 760 1120 L 820 1150 L 870 1200" fill="none" stroke="#f43f5e" stroke-width="2.5" opacity="0.85"/>
      <path d="M 920 620 L 910 730 L 880 840 L 870 960 L 840 1060 L 820 1150" fill="none" stroke="#e11d48" stroke-width="2" opacity="0.65"/>
      <path d="M 870 580 L 830 680 L 800 780 L 780 900 L 760 1020 L 760 1120" fill="none" stroke="#f43f5e" stroke-width="1.8" opacity="0.7"/>
      <path d="M 800 590 L 770 710 L 740 820 L 730 940 L 710 1040" fill="none" stroke="#fda4af" stroke-width="1.5" opacity="0.75"/>
      <path d="M 750 630 L 830 680 L 880 840 L 780 900 L 710 890" fill="none" stroke="#be123c" stroke-width="1.2" opacity="0.6"/>
      <path d="M 710 690 L 740 820 L 680 830 L 780 900 L 680 960" fill="none" stroke="#f43f5e" stroke-width="1.5" opacity="0.8"/>
      <path d="M 690 760 L 800 780 L 870 960 L 730 940 L 670 1020" fill="none" stroke="#ff2d55" stroke-width="1.5" opacity="0.75"/>

      <!-- Red Glowing Nodes -->
      <circle cx="920" cy="620" r="5" fill="#ffe4e6"/>
      <circle cx="870" cy="580" r="6" fill="#fecdd3"/>
      <circle cx="800" cy="590" r="7" fill="#fda4af"/>
      <circle cx="750" cy="630" r="8" fill="#f43f5e"/>
      <circle cx="710" cy="690" r="7" fill="#ffe4e6"/>
      <circle cx="690" cy="760" r="9" fill="#ffffff"/>
      <circle cx="680" cy="830" r="8" fill="#fda4af"/>
      <circle cx="710" cy="890" r="8.5" fill="#f43f5e"/>
      <circle cx="680" cy="960" r="9" fill="#ffffff"/>
      <circle cx="670" cy="1020" r="8" fill="#fda4af"/>
      <circle cx="720" cy="1080" r="7" fill="#f43f5e"/>
      <circle cx="760" cy="1120" r="6" fill="#fecdd3"/>
      <circle cx="820" cy="1150" r="6" fill="#fda4af"/>
      <circle cx="870" cy="1200" r="5" fill="#f43f5e"/>
      
      <circle cx="830" cy="680" r="5.5" fill="#f43f5e"/>
      <circle cx="770" cy="710" r="6" fill="#ffe4e6"/>
      <circle cx="800" cy="780" r="6.5" fill="#fda4af"/>
      <circle cx="740" cy="820" r="7" fill="#ffffff"/>
      <circle cx="780" cy="900" r="7.5" fill="#f43f5e"/>
      <circle cx="730" cy="940" r="7" fill="#fda4af"/>
      <circle cx="760" cy="1020" r="6" fill="#f43f5e"/>
      <circle cx="910" cy="730" r="4.5" fill="#e11d48"/>
      <circle cx="880" cy="840" r="5.5" fill="#f43f5e"/>
      <circle cx="870" cy="960" r="5" fill="#be123c"/>
      <circle cx="840" cy="1060" r="5.5" fill="#f43f5e"/>
    </g>

    <!-- Center Collision Energy / Sparks -->
    <g filter="url(#glow)">
      <line x1="520" y1="830" x2="680" y2="830" stroke="rgba(255,255,255,0.6)" stroke-width="1.8" stroke-dasharray="4,6"/>
      <line x1="520" y1="960" x2="680" y2="960" stroke="rgba(255,255,255,0.6)" stroke-width="1.8" stroke-dasharray="4,6"/>
      <circle cx="600" cy="830" r="4" fill="#ffffff"/>
      <circle cx="600" cy="895" r="5.5" fill="#ffffff"/>
      <circle cx="600" cy="960" r="4" fill="#ffffff"/>
    </g>

    <!-- Top Typography -->
    <text x="600" y="240" text-anchor="middle" font-family="'Inter', 'Arial Black', sans-serif" font-size="118" font-weight="900" fill="#ffffff" letter-spacing="8" filter="url(#subtleGlow)">AI VS AI</text>
    
    <text x="600" y="335" text-anchor="middle" font-family="'Inter', Arial, sans-serif" font-size="40" font-weight="800" fill="#ffffff" letter-spacing="4">ENGINEERING THE</text>
    <text x="600" y="395" text-anchor="middle" font-family="'Inter', Arial, sans-serif" font-size="40" font-weight="800" fill="#ffffff" letter-spacing="4">CYBERSECURITY</text>
    <text x="600" y="465" text-anchor="middle" font-family="'Inter', 'Arial Black', sans-serif" font-size="52" font-weight="900" fill="#ffffff" letter-spacing="5" filter="url(#subtleGlow)">COUNTER-OFFENSIVE</text>

    <!-- Bottom Thesis & Author -->
    <rect x="150" y="1460" width="900" height="2" fill="rgba(255,255,255,0.15)"/>
    
    <text x="600" y="1520" text-anchor="middle" font-family="'Inter', Arial, sans-serif" font-size="24" font-weight="700" fill="#e2e8f0" letter-spacing="3">ARCHITECTING AUTONOMOUS AI DEFENSES</text>
    <text x="600" y="1560" text-anchor="middle" font-family="'Inter', Arial, sans-serif" font-size="24" font-weight="700" fill="#cbd5e1" letter-spacing="3">AGAINST INTELLIGENT ADVERSARIES</text>
    
    <text x="600" y="1685" text-anchor="middle" font-family="'Inter', 'Arial Black', sans-serif" font-size="48" font-weight="900" fill="#ffffff" letter-spacing="6">HARSH VERMA</text>
  </svg>
  `;

  // 2. BEYOND AI ENGINEERING - Front Cover (1200 x 1800)
  const beyondAiFrontSvg = `
  <svg width="1200" height="1800" viewBox="0 0 1200 1800" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <linearGradient id="beyondBg" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#020617"/>
        <stop offset="35%" stop-color="#071530"/>
        <stop offset="70%" stop-color="#0a192f"/>
        <stop offset="100%" stop-color="#020617"/>
      </linearGradient>
      <linearGradient id="goldGrad" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0%" stop-color="#fef08a"/>
        <stop offset="45%" stop-color="#f59e0b"/>
        <stop offset="80%" stop-color="#d97706"/>
        <stop offset="100%" stop-color="#b45309"/>
      </linearGradient>
      <radialGradient id="sunGlow" cx="65%" cy="48%" r="40%">
        <stop offset="0%" stop-color="#fbbf24" stop-opacity="0.4"/>
        <stop offset="40%" stop-color="#f59e0b" stop-opacity="0.15"/>
        <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
      </radialGradient>
      <radialGradient id="cyberGlow" cx="25%" cy="38%" r="35%">
        <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.4"/>
        <stop offset="60%" stop-color="#0284c7" stop-opacity="0.1"/>
        <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
      </radialGradient>
      <filter id="glowGold">
        <feGaussianBlur stdDeviation="8" result="blur"/>
        <feMerge>
          <feMergeNode in="blur"/>
          <feMergeNode in="SourceGraphic"/>
        </feMerge>
      </filter>
      <filter id="subtle">
        <feGaussianBlur stdDeviation="3" result="blur"/>
        <feMerge>
          <feMergeNode in="blur"/>
          <feMergeNode in="SourceGraphic"/>
        </feMerge>
      </filter>
    </defs>

    <!-- Background -->
    <rect width="1200" height="1800" fill="url(#beyondBg)"/>
    <circle cx="800" cy="850" r="500" fill="url(#sunGlow)"/>
    <circle cx="350" cy="700" r="450" fill="url(#cyberGlow)"/>

    <!-- Architectural Skyline Silhouette Background -->
    <g fill="#050e24" opacity="0.8">
      <rect x="80" y="900" width="80" height="500"/>
      <rect x="180" y="820" width="110" height="580"/>
      <polygon points="180,820 235,760 290,820"/>
      <rect x="310" y="860" width="90" height="540"/>
      <rect x="420" y="780" width="130" height="620"/>
      <polygon points="420,780 485,710 550,780"/>
      <rect x="570" y="830" width="100" height="570"/>
      <rect x="690" y="790" width="120" height="610"/>
      <polygon points="690,790 750,720 810,790"/>
      <rect x="830" y="840" width="110" height="560"/>
      <rect x="960" y="800" width="140" height="600"/>
    </g>

    <!-- Golden City Spire in Foreground -->
    <g fill="url(#goldGrad)" opacity="0.85" filter="url(#glowGold)">
      <!-- Golden Center Towers -->
      <rect x="490" y="860" width="70" height="400"/>
      <polygon points="490,860 525,790 560,860"/>
      <rect x="580" y="820" width="80" height="440"/>
      <polygon points="580,820 620,730 660,820"/>
      <rect x="680" y="870" width="60" height="390"/>
    </g>

    <!-- Architectural Hardhat / Compass Center Emblem -->
    <g transform="translate(600, 1220)" filter="url(#glowGold)">
      <!-- Gear Outer Ring -->
      <circle cx="0" cy="0" r="130" fill="none" stroke="url(#goldGrad)" stroke-width="18"/>
      <!-- Gear Teeth -->
      <rect x="-16" y="-155" width="32" height="30" fill="url(#goldGrad)"/>
      <rect x="-16" y="125" width="32" height="30" fill="url(#goldGrad)"/>
      <rect x="-155" y="-16" width="30" height="32" fill="url(#goldGrad)"/>
      <rect x="125" y="-16" width="30" height="32" fill="url(#goldGrad)"/>
      <rect x="-115" y="-115" width="30" height="30" transform="rotate(45)" fill="url(#goldGrad)"/>
      <rect x="85" y="-115" width="30" height="30" transform="rotate(45)" fill="url(#goldGrad)"/>
      <rect x="-115" y="85" width="30" height="30" transform="rotate(45)" fill="url(#goldGrad)"/>
      <rect x="85" y="85" width="30" height="30" transform="rotate(45)" fill="url(#goldGrad)"/>
      <!-- Inner Dome & Hardhat Contour -->
      <path d="M -75 25 C -75 -60 75 -60 75 25 Z" fill="url(#goldGrad)"/>
      <ellipse cx="0" cy="30" rx="95" ry="16" fill="url(#goldGrad)"/>
    </g>

    <!-- AI Cybernetic Avatar Silhouette (Left) -->
    <g opacity="0.9" filter="url(#subtle)">
      <!-- Cybernetic head profile -->
      <path d="M 220 540 C 300 480 440 500 470 600 C 490 670 470 740 430 780 C 400 810 370 820 330 830 L 310 930 L 220 950 Z" fill="none" stroke="#38bdf8" stroke-width="3"/>
      <!-- Visor and neural circuitry -->
      <ellipse cx="380" cy="620" rx="55" ry="25" fill="#0284c7" opacity="0.6"/>
      <circle cx="380" cy="620" r="12" fill="#e0f2fe"/>
      <path d="M 330 520 L 420 560 L 400 660 L 460 700" stroke="#7dd3fc" stroke-width="2" fill="none"/>
      <path d="M 260 620 L 320 620 L 350 720" stroke="#38bdf8" stroke-width="1.8" fill="none"/>
      <circle cx="420" cy="560" r="5" fill="#ffffff"/>
      <circle cx="400" cy="660" r="6" fill="#38bdf8"/>
      <circle cx="460" cy="700" r="5" fill="#7dd3fc"/>
    </g>

    <!-- Human Creator / Architect with Stylus (Right) -->
    <g opacity="0.95" filter="url(#subtle)">
      <!-- Human silhouette holding radiant pen -->
      <path d="M 980 540 C 920 480 830 500 800 580 C 780 640 790 710 830 760 L 860 840 L 980 890 Z" fill="none" stroke="#fbbf24" stroke-width="3"/>
      <line x1="770" y1="680" x2="630" y2="760" stroke="#fef08a" stroke-width="4" stroke-linecap="round"/>
      <circle cx="630" cy="760" r="14" fill="#ffffff" filter="url(#glowGold)"/>
      <!-- Radiating Sparks from the Creator Stylus -->
      <line x1="630" y1="760" x2="590" y2="730" stroke="#fef08a" stroke-width="2"/>
      <line x1="630" y1="760" x2="580" y2="780" stroke="#fde047" stroke-width="2"/>
      <line x1="630" y1="760" x2="610" y2="820" stroke="#fde047" stroke-width="2"/>
      <line x1="630" y1="760" x2="660" y2="800" stroke="#fef08a" stroke-width="2"/>
    </g>

    <!-- Top Eyebrow & Author -->
    <text x="600" y="160" text-anchor="middle" font-family="'Inter', Arial, sans-serif" font-size="34" font-weight="800" fill="#f1f5f9" letter-spacing="6">FROM CREATOR TO CURATOR</text>
    <text x="600" y="240" text-anchor="middle" font-family="'Inter', 'Arial Black', sans-serif" font-size="44" font-weight="900" fill="#ffffff" letter-spacing="5">HARSH VERMA</text>

    <!-- Main Title: BEYOND AI ENGINEERING -->
    <text x="600" y="470" text-anchor="middle" font-family="'Inter', 'Arial Black', sans-serif" font-size="96" font-weight="900" fill="#ffffff" letter-spacing="6" filter="url(#subtle)">BEYOND AI</text>
    <text x="600" y="580" text-anchor="middle" font-family="'Inter', 'Arial Black', sans-serif" font-size="94" font-weight="900" fill="#ffffff" letter-spacing="6" filter="url(#subtle)">ENGINEERING</text>

    <!-- Bottom Subtitle / Blueprint -->
    <rect x="120" y="1450" width="960" height="2" fill="rgba(255,255,255,0.15)"/>
    
    <text x="600" y="1515" text-anchor="middle" font-family="'Inter', Arial, sans-serif" font-size="25" font-weight="700" font-style="italic" fill="#cbd5e1" letter-spacing="1">Professional Blueprint IN THE AGENTIC AI Era:</text>
    <text x="600" y="1555" text-anchor="middle" font-family="'Inter', Arial, sans-serif" font-size="25" font-weight="800" font-style="italic" fill="#38bdf8" letter-spacing="1">Curate Intent, Orchestrate Authority, Inspire Trust.</text>

    <!-- Publisher Branding: Bookspert -->
    <g transform="translate(600, 1680)">
      <!-- Bookspert open book logo mark -->
      <path d="M -50 -15 C -35 -22 -15 -22 0 -12 C 15 -22 35 -22 50 -15 L 50 10 C 35 3 15 3 0 13 C -15 3 -35 3 -50 10 Z" fill="#ffffff" opacity="0.9"/>
      <text x="0" y="40" text-anchor="middle" font-family="'Inter', Arial, sans-serif" font-size="34" font-weight="800" fill="#ffffff" letter-spacing="2">Bookspert</text>
    </g>
  </svg>
  `;

  // 3. AI VS AI - Full Jacket Wrap (2800 x 1800)
  const aiVsAiWrapSvg = `
  <svg width="2800" height="1800" viewBox="0 0 2800 1800" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <linearGradient id="wrapBg" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#020408"/>
        <stop offset="50%" stop-color="#040914"/>
        <stop offset="100%" stop-color="#010204"/>
      </linearGradient>
      <linearGradient id="spineBg" x1="0" y1="0" x2="1" y2="0">
        <stop offset="0%" stop-color="#030712"/>
        <stop offset="50%" stop-color="#0f172a"/>
        <stop offset="100%" stop-color="#030712"/>
      </linearGradient>
    </defs>

    <!-- Base Canvas -->
    <rect width="2800" height="1800" fill="url(#wrapBg)"/>

    <!-- Left: Back Cover (0 to 1250) -->
    <g transform="translate(100, 100)">
      <text x="0" y="160" font-family="'Inter', 'Arial Black', sans-serif" font-size="52" font-weight="900" fill="#ffffff">About the book</text>
      
      <text x="0" y="260" font-family="'Inter', Arial, sans-serif" font-size="28" font-weight="400" fill="#e2e8f0" line-height="1.6">
        <tspan x="0" dy="0">The next cyberattack won't be launched by a human. It will be launched by an AI and</tspan>
        <tspan x="0" dy="42">it will adapt faster than your defenses can respond.</tspan>
        
        <tspan x="0" dy="68">In a world where machines probe, exploit, and evolve in real time, traditional</tspan>
        <tspan x="0" dy="42">cybersecurity is already obsolete. Static rules. Human-in-the-loop decisions.</tspan>
        <tspan x="0" dy="42">Reactive defenses. They're all too slow for what's coming.</tspan>
        
        <tspan x="0" dy="68" font-weight="700" fill="#38bdf8">The battlefield has changed. It's no longer human vs. machine.</tspan>
        <tspan x="0" dy="48" font-weight="900" font-size="34" fill="#ffffff">It's AI vs. AI.</tspan>
        
        <tspan x="0" dy="68">In <tspan font-weight="700" fill="#ffffff">AI vs. AI: Cybersecurity Counter-Offensive</tspan>, Harsh Verma takes you inside</tspan>
        <tspan x="0" dy="42">this new reality—where autonomous systems don't just assist security teams, they</tspan>
        <tspan x="0" dy="42">become the front line. Where intelligent agents detect, decide, and act in</tspan>
        <tspan x="0" dy="42">milliseconds. Where defense must evolve at the same speed as attack—or fail.</tspan>
      </text>

      <text x="0" y="840" font-family="'Inter', 'Arial Black', sans-serif" font-size="30" font-weight="800" fill="#ffffff">Inside, you'll discover:</text>
      
      <g font-family="'Inter', Arial, sans-serif" font-size="26" fill="#cbd5e1" font-weight="500">
        <circle cx="15" cy="890" r="4" fill="#38bdf8"/>
        <text x="35" y="898">How AI-driven attacks are reshaping the threat landscape</text>
        
        <circle cx="15" cy="940" r="4" fill="#38bdf8"/>
        <text x="35" y="948">Why current security architectures break against adaptive adversaries</text>
        
        <circle cx="15" cy="990" r="4" fill="#38bdf8"/>
        <text x="35" y="998">The rise of autonomous defense systems that learn and respond in real time</text>
        
        <circle cx="15" cy="1040" r="4" fill="#38bdf8"/>
        <text x="35" y="1048">Practical frameworks to design systems that anticipate, adapt, and counter</text>
      </g>

      <text x="0" y="1140" font-family="'Inter', Arial, sans-serif" font-size="26" fill="#e2e8f0">
        <tspan x="0" dy="0" font-weight="700" fill="#ffffff">This is not a theoretical future. It's already unfolding.</tspan>
        <tspan x="0" dy="46">For cybersecurity professionals, AI engineers, and technology leaders, this book is</tspan>
        <tspan x="0" dy="38">a strategic guide to surviving and winning in the age of intelligent threats.</tspan>
        <tspan x="0" dy="58" font-weight="800" fill="#f43f5e">Because when machines attack, machines must fight back.</tspan>
      </text>

      <!-- Author photo box & Barcode bottom -->
      <g transform="translate(0, 1340)">
        <rect x="0" y="0" width="160" height="190" fill="#1e293b" rx="6"/>
        <text x="80" y="105" text-anchor="middle" font-family="sans-serif" font-size="16" fill="#94a3b8">AUTHOR PHOTO</text>
        <text x="0" y="240" font-family="'Inter', 'Arial Black', sans-serif" font-size="34" font-weight="900" fill="#ffffff">HARSH VERMA</text>
      </g>

      <g transform="translate(750, 1380)">
        <!-- ISBN Barcode representation -->
        <rect x="0" y="0" width="340" height="150" fill="#ffffff" rx="6"/>
        <text x="20" y="35" font-family="monospace" font-size="20" font-weight="bold" fill="#000000">ISBN 978-1-950000-00-0</text>
        <g fill="#000000">
          <rect x="25" y="50" width="4" height="70"/>
          <rect x="33" y="50" width="8" height="70"/>
          <rect x="45" y="50" width="3" height="70"/>
          <rect x="52" y="50" width="10" height="70"/>
          <rect x="68" y="50" width="5" height="70"/>
          <rect x="78" y="50" width="12" height="70"/>
          <rect x="95" y="50" width="4" height="70"/>
          <rect x="105" y="50" width="7" height="70"/>
          <rect x="120" y="50" width="14" height="70"/>
          <rect x="140" y="50" width="5" height="70"/>
          <rect x="155" y="50" width="9" height="70"/>
          <rect x="170" y="50" width="4" height="70"/>
          <rect x="180" y="50" width="12" height="70"/>
          <rect x="198" y="50" width="6" height="70"/>
          <rect x="210" y="50" width="10" height="70"/>
          <rect x="225" y="50" width="4" height="70"/>
          <rect x="235" y="50" width="14" height="70"/>
          <rect x="255" y="50" width="6" height="70"/>
          <rect x="268" y="50" width="12" height="70"/>
          <rect x="285" y="50" width="5" height="70"/>
          <rect x="295" y="50" width="10" height="70"/>
        </g>
      </g>
    </g>

    <!-- Center: Spine (1250 to 1450) -->
    <rect x="1260" y="0" width="180" height="1800" fill="url(#spineBg)"/>
    <line x1="1260" y1="0" x2="1260" y2="1800" stroke="rgba(255,255,255,0.1)"/>
    <line x1="1440" y1="0" x2="1440" y2="1800" stroke="rgba(255,255,255,0.1)"/>
    
    <g transform="translate(1350, 900) rotate(90)">
      <text x="-400" y="14" font-family="'Inter', 'Arial Black', sans-serif" font-size="34" font-weight="900" fill="#ffffff" letter-spacing="4">AI VS. AI: ENGINEERING THE CYBERSECURITY COUNTER-OFFENSIVE</text>
      <text x="500" y="14" font-family="'Inter', 'Arial Black', sans-serif" font-size="34" font-weight="900" fill="#38bdf8" letter-spacing="4">HARSH VERMA</text>
    </g>

    <!-- Right: Front Cover (1450 to 2800) -->
    <!-- Embedded Right Front Cover -->
    <g transform="translate(1500, 0)">
      ${aiVsAiFrontSvg.replace(/<svg[^>]*>/, '').replace(/<\/svg>/, '')}
    </g>
  </svg>
  `;

  // 4. BEYOND AI ENGINEERING - Full Jacket Wrap (2800 x 1800)
  const beyondAiWrapSvg = `
  <svg width="2800" height="1800" viewBox="0 0 2800 1800" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <linearGradient id="bWrapBg" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#020617"/>
        <stop offset="50%" stop-color="#08142c"/>
        <stop offset="100%" stop-color="#020617"/>
      </linearGradient>
      <linearGradient id="bSpineBg" x1="0" y1="0" x2="1" y2="0">
        <stop offset="0%" stop-color="#030712"/>
        <stop offset="50%" stop-color="#0c1d3d"/>
        <stop offset="100%" stop-color="#030712"/>
      </linearGradient>
    </defs>

    <!-- Base Canvas -->
    <rect width="2800" height="1800" fill="url(#bWrapBg)"/>

    <!-- Left: Back Cover (0 to 1250) -->
    <g transform="translate(100, 100)">
      <text x="0" y="140" font-family="'Inter', 'Arial Black', sans-serif" font-size="38" font-weight="900" fill="#ffffff" line-height="1.3">
        <tspan x="0" dy="0">Beyond AI Engineering: Mastering the Human</tspan>
        <tspan x="0" dy="48">and Strategic Dimensions of Curating AI</tspan>
        <tspan x="0" dy="48">Systems.</tspan>
      </text>
      
      <text x="0" y="320" font-family="'Inter', Arial, sans-serif" font-size="25" font-weight="400" fill="#e2e8f0" line-height="1.65">
        <tspan x="0" dy="0">Artificial intelligence is transforming the world of engineering faster than ever</tspan>
        <tspan x="0" dy="38">before. The engineers who thrive in this new era will not simply be coders they</tspan>
        <tspan x="0" dy="38">will become leaders strategists curators and innovators capable of working</tspan>
        <tspan x="0" dy="38">alongside AI to create real world impact.</tspan>
        
        <tspan x="0" dy="60">Beyond AI Engineering explores how the role of the engineer is evolving in a</tspan>
        <tspan x="0" dy="38">world driven by automation machine learning and intelligent systems. Through</tspan>
        <tspan x="0" dy="38">practical insights real world examples and career strategies this book shows</tspan>
        <tspan x="0" dy="38">how engineers can adapt grow and lead in the age of AI.</tspan>
        
        <tspan x="0" dy="60">From mastering AI workflows and building personal brands to developing</tspan>
        <tspan x="0" dy="38">leadership communication and ethical thinking this book provides a roadmap</tspan>
        <tspan x="0" dy="38">for engineers who want to stay ahead in a rapidly changing technological</tspan>
        <tspan x="0" dy="38">landscape.</tspan>
        
        <tspan x="0" dy="60" font-weight="700" fill="#38bdf8">The future of engineering has already begun. The question is not whether AI</tspan>
        <tspan x="0" dy="38" font-weight="700" fill="#ffffff">will change your career but how you will evolve with it.</tspan>
      </text>

      <!-- Author Bio Section -->
      <text x="0" y="890" font-family="'Inter', 'Arial Black', sans-serif" font-size="34" font-weight="900" fill="#ffffff">HARSH VERMA</text>
      
      <text x="0" y="940" font-family="'Inter', Arial, sans-serif" font-size="23" font-weight="400" fill="#cbd5e1" line-height="1.6">
        <tspan x="0" dy="0">Harsh is an AI and cybersecurity engineer passionate about helping the next</tspan>
        <tspan x="0" dy="36">generation of engineers thrive in the age of artificial intelligence. With years</tspan>
        <tspan x="0" dy="36">of experience working at the intersection of AI cybersecurity and emerging</tspan>
        <tspan x="0" dy="36">technologies he focuses on building innovative systems while exploring how</tspan>
        <tspan x="0" dy="36">engineers can evolve beyond traditional technical roles.</tspan>
        
        <tspan x="0" dy="52">Through his work Harsh advocates for a new generation of engineers who</tspan>
        <tspan x="0" dy="36">combine technical expertise with leadership creativity communication and</tspan>
        <tspan x="0" dy="36">ethical responsibility. His mission is to help engineers adapt grow and lead</tspan>
        <tspan x="0" dy="36">in a rapidly changing world shaped by AI.</tspan>
      </text>

      <!-- Author photo box & Bookspert Publisher bottom -->
      <g transform="translate(0, 1340)">
        <rect x="0" y="0" width="160" height="190" fill="#1e293b" rx="6"/>
        <text x="80" y="105" text-anchor="middle" font-family="sans-serif" font-size="16" fill="#94a3b8">AUTHOR PHOTO</text>
      </g>

      <g transform="translate(0, 1570)">
        <text x="0" y="30" font-family="'Inter', Arial, sans-serif" font-size="38" font-weight="900" fill="#ffffff">Bookspert</text>
        <text x="0" y="65" font-family="'Inter', Arial, sans-serif" font-size="22" font-weight="500" fill="#94a3b8">bookspert.com</text>
      </g>
    </g>

    <!-- Center: Spine (1250 to 1450) -->
    <rect x="1260" y="0" width="180" height="1800" fill="url(#bSpineBg)"/>
    <line x1="1260" y1="0" x2="1260" y2="1800" stroke="rgba(255,255,255,0.1)"/>
    <line x1="1440" y1="0" x2="1440" y2="1800" stroke="rgba(255,255,255,0.1)"/>
    
    <g transform="translate(1350, 900) rotate(90)">
      <text x="-400" y="14" font-family="'Inter', 'Arial Black', sans-serif" font-size="34" font-weight="900" fill="#ffffff" letter-spacing="4">BEYOND AI ENGINEERING</text>
      <text x="450" y="14" font-family="'Inter', 'Arial Black', sans-serif" font-size="34" font-weight="900" fill="#f59e0b" letter-spacing="4">HARSH VERMA</text>
    </g>

    <!-- Right: Front Cover (1450 to 2800) -->
    <!-- Embedded Right Front Cover -->
    <g transform="translate(1500, 0)">
      ${beyondAiFrontSvg.replace(/<svg[^>]*>/, '').replace(/<\/svg>/, '')}
    </g>
  </svg>
  `;

  console.log('Rendering Book Covers with Sharp...');

  // Convert SVGs to JPEGs
  await sharp(Buffer.from(aiVsAiFrontSvg)).jpeg({ quality: 95 }).toFile(path.join(booksDir, 'ai_vs_ai_cover.jpg'));
  await sharp(Buffer.from(beyondAiFrontSvg)).jpeg({ quality: 95 }).toFile(path.join(booksDir, 'beyond_ai_engineering_cover.jpg'));
  await sharp(Buffer.from(aiVsAiWrapSvg)).jpeg({ quality: 95 }).toFile(path.join(booksDir, 'ai_vs_ai_full_jacket.jpg'));
  await sharp(Buffer.from(beyondAiWrapSvg)).jpeg({ quality: 95 }).toFile(path.join(booksDir, 'beyond_ai_engineering_full_jacket.jpg'));

  // Also composite real author portrait photo if available onto the covers/wraps!
  const portraitPath = path.join(__dirname, '../images/harsh/Harsh_portfolio_pic.png');
  if (fs.existsSync(portraitPath)) {
    console.log('Compositing real author photo...');
    const authorResized = await sharp(portraitPath).resize(160, 190, { fit: 'cover' }).toBuffer();
    
    // Composite onto full wraps
    const aiWrapBuf = await sharp(path.join(booksDir, 'ai_vs_ai_full_jacket.jpg'))
      .composite([{ input: authorResized, top: 1440, left: 100 }])
      .jpeg({ quality: 95 })
      .toBuffer();
    fs.writeFileSync(path.join(booksDir, 'ai_vs_ai_full_jacket.jpg'), aiWrapBuf);

    const beyondWrapBuf = await sharp(path.join(booksDir, 'beyond_ai_engineering_full_jacket.jpg'))
      .composite([{ input: authorResized, top: 1440, left: 100 }])
      .jpeg({ quality: 95 })
      .toBuffer();
    fs.writeFileSync(path.join(booksDir, 'beyond_ai_engineering_full_jacket.jpg'), beyondWrapBuf);
  }

  console.log('Successfully generated all book covers and jackets!');
}

buildBookCovers().catch(console.error);
