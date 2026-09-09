import os

thumbnails = {
    "agentic_security_thumb.svg": {
        "title": "Agentic Security & NHI Guardrails",
        "category": "AI SECURITY • ZERO-TRUST",
        "category_color": "#ef4444",
        "bg_start": "#0b0f19",
        "bg_end": "#1e1b4b",
        "accent": "#6366f1",
        "accent2": "#06b6d4",
        "badge": "Non-Human Identity Guardrails",
        "badge_color": "#10b981",
        "content_svg": """
            <!-- Agent Node 1 -->
            <g transform="translate(40, 95)">
                <rect width="135" height="90" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2" filter="drop-shadow(0 4px 12px rgba(56,189,248,0.25))"/>
                <circle cx="28" cy="30" r="14" fill="#0284c7" fill-opacity="0.3" stroke="#38bdf8" stroke-width="1.5"/>
                <path d="M22 30h12M28 24v12" stroke="#38bdf8" stroke-width="2" stroke-linecap="round"/>
                <text x="50" y="34" fill="#ffffff" font-size="12" font-weight="700">Autonomous</text>
                <text x="50" y="48" fill="#94a3b8" font-size="10">AI Agent Fleet</text>
                <rect x="12" y="62" width="111" height="18" rx="4" fill="#0f172a"/>
                <text x="67" y="75" fill="#38bdf8" font-size="9.5" font-family="monospace" text-anchor="middle">tool_call.exec()</text>
            </g>

            <!-- Attack / Flow Vector -->
            <path d="M185 140 L 245 140" stroke="#f43f5e" stroke-width="3" stroke-dasharray="6,4" stroke-linecap="round"/>
            <polygon points="250,140 240,135 240,145" fill="#f43f5e"/>
            <text x="215" y="130" fill="#f43f5e" font-size="9" font-weight="700" text-anchor="middle">UNTRUSTED</text>

            <!-- Shield Guardrail / Prompt Firewall -->
            <g transform="translate(255, 65)">
                <rect width="180" height="150" rx="12" fill="#111827" stroke="#6366f1" stroke-width="2.5" filter="drop-shadow(0 8px 24px rgba(99,102,241,0.35))"/>
                
                <!-- Shield Icon -->
                <path d="M90 22 L130 38 V78 C130 102 90 118 90 118 C90 118 50 102 50 78 V38 Z" fill="#4338ca" fill-opacity="0.4" stroke="#818cf8" stroke-width="2"/>
                <path d="M80 65 L88 73 L102 58" fill="none" stroke="#22c55e" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
                
                <text x="90" y="135" fill="#ffffff" font-size="11.5" font-weight="800" text-anchor="middle">PROMPT FIREWALL</text>
                <text x="90" y="147" fill="#a5b4fc" font-size="9.5" text-anchor="middle">SPIFFE/SPIRE Attested</text>
            </g>

            <!-- Target Enterprise API -->
            <path d="M445 140 L 505 140" stroke="#10b981" stroke-width="3" stroke-linecap="round"/>
            <polygon points="510,140 500,135 500,145" fill="#10b981"/>
            <text x="475" y="130" fill="#10b981" font-size="9" font-weight="700" text-anchor="middle">AUTHORIZED</text>

            <g transform="translate(515, 95)">
                <rect width="90" height="90" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
                <circle cx="45" cy="35" r="16" fill="#065f46" stroke="#34d399" stroke-width="1.5"/>
                <text x="45" y="40" fill="#ffffff" font-size="14" font-weight="800" text-anchor="middle">API</text>
                <text x="45" y="68" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">Enterprise</text>
                <text x="45" y="80" fill="#94a3b8" font-size="9" text-anchor="middle">Secured Tools</text>
            </g>

            <!-- Bottom Stats Ticker -->
            <g transform="translate(40, 260)">
                <rect width="565" height="50" rx="8" fill="#0f172a" stroke="rgba(255,255,255,0.1)"/>
                <text x="25" y="30" fill="#94a3b8" font-size="11">Architecture:</text>
                <text x="105" y="30" fill="#ffffff" font-size="11" font-weight="700">Zero-Trust NHI Boundary</text>
                <circle cx="280" cy="26" r="3" fill="#6366f1"/>
                <text x="295" y="30" fill="#94a3b8" font-size="11">Latency:</text>
                <text x="345" y="30" fill="#10b981" font-size="11" font-weight="700">&lt; 1.2ms Guardrail Check</text>
                <circle cx="510" cy="26" r="4" fill="#22c55e"/>
                <text x="522" y="30" fill="#22c55e" font-size="10.5" font-weight="700">ACTIVE</text>
            </g>
        """
    },
    "spark_streaming_thumb.svg": {
        "title": "PySpark Streaming News Pipeline",
        "category": "BIG DATA • DISTRIBUTED STREAMING",
        "category_color": "#3b82f6",
        "bg_start": "#0b0f19",
        "bg_end": "#172554",
        "accent": "#38bdf8",
        "accent2": "#f59e0b",
        "badge": "Kafka Ingest • Spark DAG",
        "badge_color": "#38bdf8",
        "content_svg": """
            <!-- Kafka Ingestion Node -->
            <g transform="translate(35, 95)">
                <rect width="130" height="100" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="2" filter="drop-shadow(0 4px 14px rgba(245,158,11,0.2))"/>
                <rect x="12" y="14" width="28" height="28" rx="6" fill="#78350f" stroke="#fbbf24" stroke-width="1.5"/>
                <text x="26" y="33" fill="#ffffff" font-size="14" font-weight="900" text-anchor="middle">K</text>
                <text x="48" y="27" fill="#ffffff" font-size="12" font-weight="700">Apache Kafka</text>
                <text x="48" y="40" fill="#fbbf24" font-size="9.5">Event Cluster</text>
                <rect x="12" y="55" width="106" height="32" rx="4" fill="#0f172a"/>
                <text x="18" y="70" fill="#94a3b8" font-size="9">Topic: <tspan fill="#38bdf8">multinews-raw</tspan></text>
                <text x="18" y="82" fill="#10b981" font-size="9">Throughput: 50k evt/s</text>
            </g>

            <!-- Stream Arrow 1 -->
            <path d="M175 145 L 235 145" stroke="#38bdf8" stroke-width="3" stroke-linecap="round" stroke-dasharray="5,4"/>
            <polygon points="240,145 230,140 230,150" fill="#38bdf8"/>

            <!-- PySpark Distributed Worker Cluster -->
            <g transform="translate(245, 75)">
                <rect width="210" height="135" rx="12" fill="#111827" stroke="#38bdf8" stroke-width="2" filter="drop-shadow(0 6px 20px rgba(56,189,248,0.25))"/>
                
                <text x="20" y="28" fill="#38bdf8" font-size="12" font-weight="800">SPARK STREAMING ENGINE</text>
                <text x="20" y="42" fill="#94a3b8" font-size="9.5">Micro-batch DAG Pipeline</text>
                
                <!-- Worker 1 -->
                <rect x="15" y="55" width="85" height="30" rx="5" fill="#1e293b" stroke="rgba(255,255,255,0.15)"/>
                <text x="22" y="74" fill="#ffffff" font-size="9.5" font-family="monospace">Worker 01 [NLP]</text>
                
                <!-- Worker 2 -->
                <rect x="110" y="55" width="85" height="30" rx="5" fill="#1e293b" stroke="rgba(255,255,255,0.15)"/>
                <text x="117" y="74" fill="#ffffff" font-size="9.5" font-family="monospace">Worker 02 [TF-IDF]</text>

                <!-- Worker 3 -->
                <rect x="15" y="92" width="85" height="30" rx="5" fill="#1e293b" stroke="rgba(255,255,255,0.15)"/>
                <text x="22" y="111" fill="#ffffff" font-size="9.5" font-family="monospace">Worker 03 [Class]</text>

                <!-- Worker 4 -->
                <rect x="110" y="92" width="85" height="30" rx="5" fill="#1e293b" stroke="rgba(255,255,255,0.15)"/>
                <text x="117" y="111" fill="#ffffff" font-size="9.5" font-family="monospace">Worker 04 [Sink]</text>
            </g>

            <!-- Stream Arrow 2 -->
            <path d="M465 145 L 515 145" stroke="#10b981" stroke-width="3" stroke-linecap="round"/>
            <polygon points="520,145 510,140 510,150" fill="#10b981"/>

            <!-- Real-Time Classification Output -->
            <g transform="translate(525, 85)">
                <rect width="85" height="115" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
                <text x="42" y="24" fill="#10b981" font-size="10.5" font-weight="700" text-anchor="middle">Live Classes</text>
                <rect x="8" y="35" width="69" height="20" rx="4" fill="#0f172a"/>
                <text x="12" y="49" fill="#38bdf8" font-size="8.5">World News</text>
                <rect x="8" y="60" width="69" height="20" rx="4" fill="#0f172a"/>
                <text x="12" y="74" fill="#a78bfa" font-size="8.5">Tech &amp; AI</text>
                <rect x="8" y="85" width="69" height="20" rx="4" fill="#0f172a"/>
                <text x="12" y="99" fill="#f43f5e" font-size="8.5">Finance</text>
            </g>

            <!-- Bottom Ticker -->
            <g transform="translate(35, 260)">
                <rect width="575" height="50" rx="8" fill="#0f172a" stroke="rgba(255,255,255,0.1)"/>
                <text x="20" y="30" fill="#94a3b8" font-size="11">Tech Stack:</text>
                <text x="90" y="30" fill="#ffffff" font-size="11" font-weight="700">PySpark Streaming • Kafka • NLP DAG • Python</text>
                <text x="470" y="30" fill="#38bdf8" font-size="11" font-weight="700">&gt; 98.4% Precision</text>
            </g>
        """
    },
    "speech_ai_thumb.svg": {
        "title": "Automatic Speech Recognition (ASR)",
        "category": "NLP • ACOUSTIC DEEP LEARNING",
        "category_color": "#9333ea",
        "bg_start": "#0b0f19",
        "bg_end": "#2e1065",
        "accent": "#c084fc",
        "accent2": "#06b6d4",
        "badge": "Audio DSP • CTC Decoder",
        "badge_color": "#c084fc",
        "content_svg": """
            <!-- Audio Waveform Input -->
            <g transform="translate(35, 80)">
                <rect width="160" height="135" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
                <text x="15" y="24" fill="#c084fc" font-size="11" font-weight="700">RAW AUDIO SIGNAL</text>
                <text x="15" y="38" fill="#94a3b8" font-size="9.5">16kHz Mel-Spectrogram</text>
                
                <!-- Soundwave visualization -->
                <path d="M15 100 Q 25 50, 35 100 T 55 100 T 75 40 T 95 130 T 115 60 T 135 110 T 145 100" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
                <path d="M15 100 Q 25 70, 35 100 T 55 100 T 75 60 T 95 115 T 115 80 T 135 105 T 145 100" fill="none" stroke="#c084fc" stroke-width="1.5" opacity="0.6"/>
            </g>

            <path d="M205 145 L 245 145" stroke="#c084fc" stroke-width="2.5" stroke-linecap="round"/>

            <!-- Acoustic Neural Model -->
            <g transform="translate(255, 75)">
                <rect width="180" height="145" rx="10" fill="#111827" stroke="#c084fc" stroke-width="2" filter="drop-shadow(0 6px 18px rgba(192,132,252,0.25))"/>
                <text x="15" y="24" fill="#ffffff" font-size="11" font-weight="800">CONV-TRANSFORMER</text>
                <text x="15" y="38" fill="#a855f7" font-size="9.5">CTC Acoustic Decoder</text>
                
                <!-- Neural Nodes -->
                <g transform="translate(15, 50)">
                    <circle cx="15" cy="15" r="7" fill="#6366f1"/>
                    <circle cx="15" cy="40" r="7" fill="#6366f1"/>
                    <circle cx="15" cy="65" r="7" fill="#6366f1"/>
                    
                    <circle cx="75" cy="15" r="7" fill="#a855f7"/>
                    <circle cx="75" cy="40" r="7" fill="#a855f7"/>
                    <circle cx="75" cy="65" r="7" fill="#a855f7"/>

                    <circle cx="135" cy="27" r="7" fill="#38bdf8"/>
                    <circle cx="135" cy="53" r="7" fill="#38bdf8"/>
                    
                    <!-- Connections -->
                    <line x1="22" y1="15" x2="68" y2="15" stroke="rgba(255,255,255,0.2)"/>
                    <line x1="22" y1="15" x2="68" y2="40" stroke="rgba(255,255,255,0.2)"/>
                    <line x1="22" y1="40" x2="68" y2="40" stroke="rgba(255,255,255,0.2)"/>
                    <line x1="22" y1="65" x2="68" y2="65" stroke="rgba(255,255,255,0.2)"/>
                    <line x1="82" y1="15" x2="128" y2="27" stroke="rgba(255,255,255,0.2)"/>
                    <line x1="82" y1="40" x2="128" y2="53" stroke="rgba(255,255,255,0.2)"/>
                </g>
            </g>

            <path d="M445 145 L 485 145" stroke="#34d399" stroke-width="2.5" stroke-linecap="round"/>

            <!-- Text Transcription Output -->
            <g transform="translate(495, 80)">
                <rect width="115" height="135" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
                <text x="15" y="24" fill="#34d399" font-size="11" font-weight="700">OUTPUT TEXT</text>
                <rect x="10" y="38" width="95" height="85" rx="6" fill="#0f172a"/>
                <text x="16" y="56" fill="#ffffff" font-size="9" font-family="monospace">"Distributed</text>
                <text x="16" y="70" fill="#ffffff" font-size="9" font-family="monospace"> speech AI</text>
                <text x="16" y="84" fill="#ffffff" font-size="9" font-family="monospace"> pipeline</text>
                <text x="16" y="98" fill="#ffffff" font-size="9" font-family="monospace"> transcribed"</text>
                <text x="16" y="114" fill="#10b981" font-size="8.5">WER: 4.2%</text>
            </g>

            <!-- Bottom Ticker -->
            <g transform="translate(35, 260)">
                <rect width="575" height="50" rx="8" fill="#0f172a" stroke="rgba(255,255,255,0.1)"/>
                <text x="20" y="30" fill="#94a3b8" font-size="11">Architecture:</text>
                <text x="100" y="30" fill="#ffffff" font-size="11" font-weight="700">Spectrogram Mel-Bands • PyTorch CTC Loss • Transformer</text>
            </g>
        """
    },
    "bilstm_sentiment_thumb.svg": {
        "title": "BiLSTM Sentiment Analysis & Attention",
        "category": "NLP • DEEP LEARNING",
        "category_color": "#10b981",
        "bg_start": "#0b0f19",
        "bg_end": "#064e3b",
        "accent": "#34d399",
        "accent2": "#60a5fa",
        "badge": "Attention Mechanism • 94% Acc",
        "badge_color": "#34d399",
        "content_svg": """
            <!-- Bidirectional LSTM Diagram -->
            <g transform="translate(45, 75)">
                <rect width="550" height="165" rx="12" fill="#111827" stroke="#10b981" stroke-width="2" filter="drop-shadow(0 6px 20px rgba(16,185,129,0.25))"/>
                
                <!-- Forward Pass -->
                <text x="25" y="30" fill="#34d399" font-size="11" font-weight="800">FORWARD LSTM LAYER (h_forward)</text>
                <g transform="translate(25, 42)">
                    <rect x="0" y="0" width="80" height="32" rx="6" fill="#1e293b" stroke="#34d399"/>
                    <text x="40" y="20" fill="#ffffff" font-size="10" text-anchor="middle">Word₁</text>
                    <path d="M80 16 L120 16" stroke="#34d399" stroke-width="2"/>
                    
                    <rect x="120" y="0" width="80" height="32" rx="6" fill="#1e293b" stroke="#34d399"/>
                    <text x="160" y="20" fill="#ffffff" font-size="10" text-anchor="middle">Word₂</text>
                    <path d="M200 16 L240 16" stroke="#34d399" stroke-width="2"/>

                    <rect x="240" y="0" width="80" height="32" rx="6" fill="#1e293b" stroke="#34d399"/>
                    <text x="280" y="20" fill="#ffffff" font-size="10" text-anchor="middle">Word₃</text>
                    <path d="M320 16 L360 16" stroke="#34d399" stroke-width="2"/>

                    <rect x="360" y="0" width="80" height="32" rx="6" fill="#1e293b" stroke="#34d399"/>
                    <text x="400" y="20" fill="#ffffff" font-size="10" text-anchor="middle">Word₄</text>
                </g>

                <!-- Backward Pass -->
                <text x="25" y="105" fill="#60a5fa" font-size="11" font-weight="800">BACKWARD LSTM LAYER (h_backward)</text>
                <g transform="translate(25, 115)">
                    <rect x="0" y="0" width="80" height="32" rx="6" fill="#1e293b" stroke="#60a5fa"/>
                    <text x="40" y="20" fill="#ffffff" font-size="10" text-anchor="middle">Word₁</text>
                    <path d="M120 16 L80 16" stroke="#60a5fa" stroke-width="2"/>
                    
                    <rect x="120" y="0" width="80" height="32" rx="6" fill="#1e293b" stroke="#60a5fa"/>
                    <text x="160" y="20" fill="#ffffff" font-size="10" text-anchor="middle">Word₂</text>
                    <path d="M240 16 L200 16" stroke="#60a5fa" stroke-width="2"/>

                    <rect x="240" y="0" width="80" height="32" rx="6" fill="#1e293b" stroke="#60a5fa"/>
                    <text x="280" y="20" fill="#ffffff" font-size="10" text-anchor="middle">Word₃</text>
                    <path d="M360 16 L320 16" stroke="#60a5fa" stroke-width="2"/>

                    <rect x="360" y="0" width="80" height="32" rx="6" fill="#1e293b" stroke="#60a5fa"/>
                    <text x="400" y="20" fill="#ffffff" font-size="10" text-anchor="middle">Word₄</text>
                </g>

                <!-- Attention Score Output -->
                <g transform="translate(470, 42)">
                    <rect width="65" height="105" rx="8" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
                    <text x="32" y="22" fill="#fbbf24" font-size="9" font-weight="700" text-anchor="middle">ATTN</text>
                    <text x="32" y="42" fill="#10b981" font-size="14" font-weight="900" text-anchor="middle">+0.96</text>
                    <text x="32" y="62" fill="#94a3b8" font-size="8.5" text-anchor="middle">Positive</text>
                    <rect x="8" y="75" width="49" height="18" rx="3" fill="#047857"/>
                    <text x="32" y="87" fill="#ffffff" font-size="8.5" font-weight="700" text-anchor="middle">94% Acc</text>
                </g>
            </g>

            <!-- Bottom Ticker -->
            <g transform="translate(45, 260)">
                <rect width="550" height="50" rx="8" fill="#0f172a" stroke="rgba(255,255,255,0.1)"/>
                <text x="20" y="30" fill="#94a3b8" font-size="11">Context Engine:</text>
                <text x="120" y="30" fill="#ffffff" font-size="11" font-weight="700">Self-Attention Matrix • Word2Vec / GloVe Embeddings • Softmax</text>
            </g>
        """
    },
    "cross_lingual_spark_thumb.svg": {
        "title": "Cross-Language Spark MinHash LSH",
        "category": "BIG DATA • LSH INDEXING",
        "category_color": "#f59e0b",
        "bg_start": "#0b0f19",
        "bg_end": "#451a03",
        "accent": "#fbbf24",
        "accent2": "#38bdf8",
        "badge": "MinHash LSH • Multilingual",
        "badge_color": "#fbbf24",
        "content_svg": """
            <g transform="translate(35, 75)">
                <!-- Multilingual Input Corpus -->
                <rect width="150" height="150" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
                <text x="15" y="24" fill="#fbbf24" font-size="11" font-weight="700">MULTILINGUAL CORPUS</text>
                <text x="15" y="38" fill="#94a3b8" font-size="9.5">En • Es • Fr • De • Zh</text>
                <rect x="12" y="50" width="126" height="25" rx="4" fill="#0f172a"/>
                <text x="18" y="66" fill="#ffffff" font-size="9">Doc A (English Shingles)</text>
                <rect x="12" y="82" width="126" height="25" rx="4" fill="#0f172a"/>
                <text x="18" y="98" fill="#ffffff" font-size="9">Doc B (Spanish Translation)</text>
                <rect x="12" y="114" width="126" height="25" rx="4" fill="#0f172a"/>
                <text x="18" y="130" fill="#ffffff" font-size="9">Doc C (French Edition)</text>
            </g>

            <path d="M195 150 L 235 150" stroke="#fbbf24" stroke-width="2.5" stroke-linecap="round"/>

            <!-- Distributed MinHash LSH Buckets -->
            <g transform="translate(245, 75)">
                <rect width="200" height="150" rx="10" fill="#111827" stroke="#fbbf24" stroke-width="2" filter="drop-shadow(0 6px 18px rgba(245,158,11,0.25))"/>
                <text x="15" y="24" fill="#fbbf24" font-size="11" font-weight="800">MINHASH LSH BUCKETING</text>
                <text x="15" y="38" fill="#94a3b8" font-size="9.5">PySpark Parallel Jaccard</text>
                
                <rect x="15" y="50" width="170" height="26" rx="4" fill="#1e293b"/>
                <text x="22" y="67" fill="#38bdf8" font-size="9.5">Hash Bucket #412 [J=0.89]</text>
                
                <rect x="15" y="82" width="170" height="26" rx="4" fill="#1e293b"/>
                <text x="22" y="99" fill="#10b981" font-size="9.5">Hash Bucket #890 [J=0.94]</text>

                <rect x="15" y="114" width="170" height="26" rx="4" fill="#1e293b"/>
                <text x="22" y="131" fill="#f43f5e" font-size="9.5">Hash Bucket #104 [J=0.12]</text>
            </g>

            <path d="M455 150 L 495 150" stroke="#10b981" stroke-width="2.5" stroke-linecap="round"/>

            <!-- Deduplication Results -->
            <g transform="translate(505, 75)">
                <rect width="100" height="150" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
                <text x="15" y="24" fill="#10b981" font-size="11" font-weight="700">DEDUPED</text>
                <rect x="10" y="45" width="80" height="85" rx="6" fill="#0f172a"/>
                <circle cx="50" cy="72" r="16" fill="#065f46" stroke="#34d399" stroke-width="1.5"/>
                <text x="50" y="78" fill="#ffffff" font-size="16" font-weight="900" text-anchor="middle">✓</text>
                <text x="50" y="105" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">99.8% Match</text>
                <text x="50" y="118" fill="#94a3b8" font-size="8" text-anchor="middle">Zero Collisions</text>
            </g>

            <!-- Bottom Ticker -->
            <g transform="translate(35, 260)">
                <rect width="570" height="50" rx="8" fill="#0f172a" stroke="rgba(255,255,255,0.1)"/>
                <text x="20" y="30" fill="#94a3b8" font-size="11">Algorithm:</text>
                <text x="90" y="30" fill="#ffffff" font-size="11" font-weight="700">k-Shingling • MinHash Signatures • Locality Sensitive Hashing (LSH)</text>
            </g>
        """
    },
    "graph_analytics_thumb.svg": {
        "title": "Yelp & Social Network Graph Mining",
        "category": "GRAPH AI • NETWORK MINING",
        "category_color": "#ef4444",
        "bg_start": "#0b0f19",
        "bg_end": "#450a0a",
        "accent": "#f87171",
        "accent2": "#60a5fa",
        "badge": "PageRank • Community Detection",
        "badge_color": "#f87171",
        "content_svg": """
            <!-- Graph Visualization Art -->
            <g transform="translate(45, 70)">
                <rect width="550" height="175" rx="12" fill="#111827" stroke="#ef4444" stroke-width="2" filter="drop-shadow(0 6px 20px rgba(239,68,68,0.25))"/>
                
                <!-- Central PageRank Hub Node -->
                <circle cx="275" cy="88" r="28" fill="#991b1b" stroke="#f87171" stroke-width="3" filter="drop-shadow(0 0 12px rgba(248,113,113,0.6))"/>
                <text x="275" y="92" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">HUB</text>
                <text x="275" y="104" fill="#fca5a5" font-size="8" text-anchor="middle">PR: 0.98</text>

                <!-- Connected Nodes -->
                <!-- Cluster A (Left) -->
                <circle cx="120" cy="55" r="16" fill="#1e3a8a" stroke="#60a5fa" stroke-width="2"/>
                <text x="120" y="59" fill="#ffffff" font-size="9" text-anchor="middle">A1</text>
                <circle cx="90" cy="120" r="14" fill="#1e3a8a" stroke="#60a5fa" stroke-width="2"/>
                <text x="90" y="124" fill="#ffffff" font-size="8.5" text-anchor="middle">A2</text>
                <circle cx="165" cy="115" r="15" fill="#1e3a8a" stroke="#60a5fa" stroke-width="2"/>
                <text x="165" y="119" fill="#ffffff" font-size="9" text-anchor="middle">A3</text>

                <!-- Cluster B (Right) -->
                <circle cx="430" cy="55" r="16" fill="#065f46" stroke="#34d399" stroke-width="2"/>
                <text x="430" y="59" fill="#ffffff" font-size="9" text-anchor="middle">B1</text>
                <circle cx="460" cy="120" r="14" fill="#065f46" stroke="#34d399" stroke-width="2"/>
                <text x="460" y="124" fill="#ffffff" font-size="8.5" text-anchor="middle">B2</text>
                <circle cx="390" cy="115" r="15" fill="#065f46" stroke="#34d399" stroke-width="2"/>
                <text x="390" y="119" fill="#ffffff" font-size="9" text-anchor="middle">B3</text>

                <!-- Graph Edges -->
                <line x1="120" y1="55" x2="90" y2="120" stroke="#3b82f6" stroke-width="1.5"/>
                <line x1="120" y1="55" x2="165" y2="115" stroke="#3b82f6" stroke-width="1.5"/>
                <line x1="90" y1="120" x2="165" y2="115" stroke="#3b82f6" stroke-width="1.5"/>
                
                <line x1="430" y1="55" x2="460" y2="120" stroke="#10b981" stroke-width="1.5"/>
                <line x1="430" y1="55" x2="390" y2="115" stroke="#10b981" stroke-width="1.5"/>
                <line x1="460" y1="120" x2="390" y2="115" stroke="#10b981" stroke-width="1.5"/>

                <!-- Hub Connections -->
                <line x1="165" y1="115" x2="250" y2="88" stroke="#f87171" stroke-width="2.5"/>
                <line x1="120" y1="55" x2="250" y2="80" stroke="#f87171" stroke-width="2"/>
                <line x1="390" y1="115" x2="300" y2="88" stroke="#f87171" stroke-width="2.5"/>
                <line x1="430" y1="55" x2="300" y2="80" stroke="#f87171" stroke-width="2"/>
                
                <text x="25" y="30" fill="#f87171" font-size="11" font-weight="700">YELP USER NETWORK</text>
                <text x="525" y="30" fill="#34d399" font-size="11" font-weight="700" text-anchor="end">MODULARITY: 0.82</text>
            </g>

            <!-- Bottom Ticker -->
            <g transform="translate(45, 260)">
                <rect width="550" height="50" rx="8" fill="#0f172a" stroke="rgba(255,255,255,0.1)"/>
                <text x="20" y="30" fill="#94a3b8" font-size="11">Algorithms:</text>
                <text x="95" y="30" fill="#ffffff" font-size="11" font-weight="700">PageRank Centrality • Girvan-Newman Modularity • NetworkX</text>
            </g>
        """
    },
    "cnn_vision_thumb.svg": {
        "title": "Deep CNN MultiClass Image Classifier",
        "category": "COMPUTER VISION • PYTORCH",
        "category_color": "#06b6d4",
        "bg_start": "#0b0f19",
        "bg_end": "#083344",
        "accent": "#22d3ee",
        "accent2": "#a855f7",
        "badge": "ResNet Conv2D • 99.2% Acc",
        "badge_color": "#22d3ee",
        "content_svg": """
            <!-- CNN Layer Pipeline -->
            <g transform="translate(35, 75)">
                <!-- Input Tensor (32x32x3) -->
                <rect x="0" y="25" width="70" height="100" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
                <text x="35" y="20" fill="#38bdf8" font-size="10" font-weight="700" text-anchor="middle">RGB Tensor</text>
                <text x="35" y="75" fill="#ffffff" font-size="11" font-family="monospace" text-anchor="middle">32x32x3</text>

                <!-- Conv2D Layer 1 -->
                <path d="M75 75 L105 75" stroke="#38bdf8" stroke-width="2"/>
                <rect x="110" y="15" width="75" height="120" rx="6" fill="#0e7490" fill-opacity="0.5" stroke="#22d3ee" stroke-width="2"/>
                <text x="147" y="10" fill="#22d3ee" font-size="10" font-weight="700" text-anchor="middle">Conv2D + ReLu</text>
                <text x="147" y="75" fill="#ffffff" font-size="10" font-family="monospace" text-anchor="middle">64 Filters</text>

                <!-- MaxPool -->
                <path d="M190 75 L220 75" stroke="#22d3ee" stroke-width="2"/>
                <rect x="225" y="35" width="65" height="80" rx="6" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
                <text x="257" y="30" fill="#c084fc" font-size="10" font-weight="700" text-anchor="middle">MaxPool</text>
                <text x="257" y="75" fill="#ffffff" font-size="10" font-family="monospace" text-anchor="middle">16x16x64</text>

                <!-- Conv2D Layer 2 -->
                <path d="M295 75 L325 75" stroke="#a855f7" stroke-width="2"/>
                <rect x="330" y="10" width="80" height="130" rx="6" fill="#6b21a8" fill-opacity="0.5" stroke="#c084fc" stroke-width="2"/>
                <text x="370" y="5" fill="#c084fc" font-size="10" font-weight="700" text-anchor="middle">Residual Block</text>
                <text x="370" y="75" fill="#ffffff" font-size="10" font-family="monospace" text-anchor="middle">128 Filters</text>

                <!-- Fully Connected & Softmax -->
                <path d="M415 75 L445 75" stroke="#34d399" stroke-width="2"/>
                <rect x="450" y="20" width="120" height="110" rx="8" fill="#111827" stroke="#34d399" stroke-width="2"/>
                <text x="510" y="15" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">Dense Softmax</text>
                <text x="460" y="45" fill="#ffffff" font-size="9">Class 01: 99.2%</text>
                <text x="460" y="65" fill="#94a3b8" font-size="9">Class 02: 0.5%</text>
                <text x="460" y="85" fill="#94a3b8" font-size="9">Class 03: 0.2%</text>
                <text x="460" y="105" fill="#94a3b8" font-size="9">Class 04: 0.1%</text>
            </g>

            <!-- Bottom Ticker -->
            <g transform="translate(35, 260)">
                <rect width="570" height="50" rx="8" fill="#0f172a" stroke="rgba(255,255,255,0.1)"/>
                <text x="20" y="30" fill="#94a3b8" font-size="11">Architecture:</text>
                <text x="100" y="30" fill="#ffffff" font-size="11" font-weight="700">Deep ResNet Backbone • Spatial Dropout • Batch Normalization</text>
            </g>
        """
    },
    "lockfree_hashtable_thumb.svg": {
        "title": "Lock-Free Concurrent Hash Table",
        "category": "SYSTEMS • CONCURRENCY",
        "category_color": "#6366f1",
        "bg_start": "#0b0f19",
        "bg_end": "#1e1b4b",
        "accent": "#818cf8",
        "accent2": "#34d399",
        "badge": "Atomic CAS • Zero Contention",
        "badge_color": "#818cf8",
        "content_svg": """
            <!-- CPU Multi-threading & CAS Diagram -->
            <g transform="translate(40, 75)">
                <!-- Thread 1 -->
                <rect x="0" y="10" width="110" height="40" rx="6" fill="#1e293b" stroke="#818cf8" stroke-width="1.5"/>
                <text x="55" y="34" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">CPU Core #0</text>
                
                <!-- Thread 2 -->
                <rect x="0" y="60" width="110" height="40" rx="6" fill="#1e293b" stroke="#818cf8" stroke-width="1.5"/>
                <text x="55" y="84" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">CPU Core #1</text>

                <!-- Thread 3 -->
                <rect x="0" y="110" width="110" height="40" rx="6" fill="#1e293b" stroke="#818cf8" stroke-width="1.5"/>
                <text x="55" y="134" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">CPU Core #2</text>

                <!-- CAS Engine Box -->
                <g transform="translate(145, 0)">
                    <rect width="230" height="160" rx="10" fill="#111827" stroke="#818cf8" stroke-width="2" filter="drop-shadow(0 6px 18px rgba(129,140,248,0.25))"/>
                    <text x="20" y="26" fill="#818cf8" font-size="11" font-weight="800">ATOMIC CAS ENGINE</text>
                    <text x="20" y="42" fill="#94a3b8" font-size="9">compareAndSet(bucket, expected, new)</text>
                    
                    <rect x="15" y="55" width="200" height="28" rx="4" fill="#1e293b"/>
                    <text x="25" y="73" fill="#34d399" font-size="9.5" font-family="monospace">Bucket[0x04]: Key="uid_89"</text>
                    
                    <rect x="15" y="90" width="200" height="28" rx="4" fill="#1e293b"/>
                    <text x="25" y="108" fill="#38bdf8" font-size="9.5" font-family="monospace">Bucket[0x08]: Key="tok_31"</text>

                    <rect x="15" y="125" width="200" height="28" rx="4" fill="#1e293b"/>
                    <text x="25" y="143" fill="#fbbf24" font-size="9.5" font-family="monospace">Bucket[0x0C]: CAS Lock-Free</text>
                </g>

                <!-- Performance Metrics -->
                <g transform="translate(405, 0)">
                    <rect width="155" height="160" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
                    <text x="20" y="26" fill="#34d399" font-size="11" font-weight="800">BENCHMARK</text>
                    <text x="20" y="55" fill="#ffffff" font-size="10">Throughput:</text>
                    <text x="20" y="75" fill="#34d399" font-size="16" font-weight="900">14.2M ops/s</text>
                    
                    <text x="20" y="105" fill="#ffffff" font-size="10">Lock Contention:</text>
                    <text x="20" y="125" fill="#38bdf8" font-size="15" font-weight="900">0.00% (Zero)</text>
                </g>
            </g>

            <!-- Bottom Ticker -->
            <g transform="translate(40, 260)">
                <rect width="560" height="50" rx="8" fill="#0f172a" stroke="rgba(255,255,255,0.1)"/>
                <text x="20" y="30" fill="#94a3b8" font-size="11">Core Primitives:</text>
                <text x="120" y="30" fill="#ffffff" font-size="11" font-weight="700">AtomicReferenceArray • Unsafe Memory Barrier • JMM Volatile</text>
            </g>
        """
    },
    "microservice_gateway_thumb.svg": {
        "title": "WordDoc Frequency Microservice",
        "category": "BACKEND • HIGH THROUGHPUT",
        "category_color": "#4f46e5",
        "bg_start": "#0b0f19",
        "bg_end": "#1e1b4b",
        "accent": "#6366f1",
        "accent2": "#10b981",
        "badge": "Sub-millisecond API",
        "badge_color": "#6366f1",
        "content_svg": """
            <g transform="translate(40, 75)">
                <!-- Client Request -->
                <rect x="0" y="35" width="110" height="80" rx="8" fill="#1e293b" stroke="#6366f1" stroke-width="2"/>
                <text x="55" y="65" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">REST Client</text>
                <text x="55" y="80" fill="#94a3b8" font-size="9" text-anchor="middle">POST /api/v1/parse</text>

                <path d="M115 75 L155 75" stroke="#6366f1" stroke-width="2.5"/>

                <!-- Microservice Gateway & Worker Pool -->
                <g transform="translate(165, 0)">
                    <rect width="240" height="160" rx="10" fill="#111827" stroke="#6366f1" stroke-width="2" filter="drop-shadow(0 6px 20px rgba(99,102,241,0.25))"/>
                    <text x="20" y="26" fill="#818cf8" font-size="11" font-weight="800">CONCURRENT LEXER ENGINE</text>
                    <text x="20" y="42" fill="#94a3b8" font-size="9">Non-blocking async worker pool</text>
                    
                    <rect x="15" y="55" width="210" height="28" rx="4" fill="#1e293b"/>
                    <text x="25" y="73" fill="#38bdf8" font-size="9.5">Worker #1: Token Stream Lexing</text>
                    
                    <rect x="15" y="90" width="210" height="28" rx="4" fill="#1e293b"/>
                    <text x="25" y="108" fill="#34d399" font-size="9.5">Worker #2: Frequency Counting</text>

                    <rect x="15" y="125" width="210" height="28" rx="4" fill="#1e293b"/>
                    <text x="25" y="143" fill="#fbbf24" font-size="9.5">Worker #3: JSON Serialization</text>
                </g>

                <path d="M410 75 L445 75" stroke="#10b981" stroke-width="2.5"/>

                <!-- Response Stats -->
                <g transform="translate(455, 10)">
                    <rect width="105" height="140" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
                    <text x="15" y="25" fill="#10b981" font-size="10" font-weight="700">JSON Output</text>
                    <text x="15" y="50" fill="#ffffff" font-size="9">Latency:</text>
                    <text x="15" y="66" fill="#10b981" font-size="13" font-weight="900">0.8 ms</text>
                    <text x="15" y="95" fill="#ffffff" font-size="9">Capacity:</text>
                    <text x="15" y="112" fill="#38bdf8" font-size="13" font-weight="900">25k req/s</text>
                </g>
            </g>

            <!-- Bottom Ticker -->
            <g transform="translate(40, 260)">
                <rect width="560" height="50" rx="8" fill="#0f172a" stroke="rgba(255,255,255,0.1)"/>
                <text x="20" y="30" fill="#94a3b8" font-size="11">Architecture:</text>
                <text x="105" y="30" fill="#ffffff" font-size="11" font-weight="700">Microservice Cluster • RESTful API • Non-blocking IO • Fast Serialization</text>
            </g>
        """
    },
    "hadoop_cluster_thumb.svg": {
        "title": "Hadoop Distributed Social Network",
        "category": "DISTRIBUTED • HDFS CLUSTER",
        "category_color": "#eab308",
        "bg_start": "#0b0f19",
        "bg_end": "#422006",
        "accent": "#facc15",
        "accent2": "#38bdf8",
        "badge": "MapReduce • Terabyte Graph",
        "badge_color": "#facc15",
        "content_svg": """
            <g transform="translate(40, 75)">
                <!-- NameNode Master -->
                <rect x="0" y="30" width="120" height="90" rx="8" fill="#1e293b" stroke="#facc15" stroke-width="2"/>
                <text x="60" y="55" fill="#facc15" font-size="11" font-weight="800" text-anchor="middle">NAMENODE</text>
                <text x="60" y="70" fill="#ffffff" font-size="9.5" text-anchor="middle">HDFS Master</text>
                <text x="60" y="90" fill="#94a3b8" font-size="8.5" text-anchor="middle">Block Metastore</text>

                <path d="M125 75 L165 75" stroke="#facc15" stroke-width="2"/>

                <!-- MapReduce Nodes -->
                <g transform="translate(175, 0)">
                    <rect width="230" height="160" rx="10" fill="#111827" stroke="#facc15" stroke-width="2" filter="drop-shadow(0 6px 20px rgba(250,204,21,0.2))"/>
                    <text x="20" y="26" fill="#facc15" font-size="11" font-weight="800">DATANODE CLUSTER (MapReduce)</text>
                    
                    <rect x="15" y="45" width="95" height="45" rx="5" fill="#1e293b" stroke="rgba(255,255,255,0.1)"/>
                    <text x="62" y="65" fill="#ffffff" font-size="9" text-anchor="middle">DataNode 01</text>
                    <text x="62" y="80" fill="#38bdf8" font-size="8" text-anchor="middle">Map(K1, V1)</text>

                    <rect x="120" y="45" width="95" height="45" rx="5" fill="#1e293b" stroke="rgba(255,255,255,0.1)"/>
                    <text x="167" y="65" fill="#ffffff" font-size="9" text-anchor="middle">DataNode 02</text>
                    <text x="167" y="80" fill="#38bdf8" font-size="8" text-anchor="middle">Map(K1, V1)</text>

                    <rect x="15" y="100" width="95" height="45" rx="5" fill="#1e293b" stroke="rgba(255,255,255,0.1)"/>
                    <text x="62" y="120" fill="#ffffff" font-size="9" text-anchor="middle">DataNode 03</text>
                    <text x="62" y="135" fill="#10b981" font-size="8" text-anchor="middle">Reduce(K2, List)</text>

                    <rect x="120" y="100" width="95" height="45" rx="5" fill="#1e293b" stroke="rgba(255,255,255,0.1)"/>
                    <text x="167" y="120" fill="#ffffff" font-size="9" text-anchor="middle">DataNode 04</text>
                    <text x="167" y="135" fill="#10b981" font-size="8" text-anchor="middle">Reduce(K2, List)</text>
                </g>

                <path d="M410 75 L445 75" stroke="#10b981" stroke-width="2"/>

                <!-- HDFS Sharded Output -->
                <g transform="translate(455, 20)">
                    <rect width="105" height="120" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
                    <text x="15" y="25" fill="#10b981" font-size="10" font-weight="700">HDFS Output</text>
                    <text x="15" y="50" fill="#ffffff" font-size="9">Graph Nodes:</text>
                    <text x="15" y="66" fill="#facc15" font-size="13" font-weight="900">12.5M</text>
                    <text x="15" y="90" fill="#ffffff" font-size="9">Replication:</text>
                    <text x="15" y="106" fill="#38bdf8" font-size="12" font-weight="900">3x Fault-Tol</text>
                </g>
            </g>

            <!-- Bottom Ticker -->
            <g transform="translate(40, 260)">
                <rect width="560" height="50" rx="8" fill="#0f172a" stroke="rgba(255,255,255,0.1)"/>
                <text x="20" y="30" fill="#94a3b8" font-size="11">Infrastructure:</text>
                <text x="110" y="30" fill="#ffffff" font-size="11" font-weight="700">Apache Hadoop • HDFS • YARN Resource Manager • MapReduce</text>
            </g>
        """
    },
    "ir_tokenizer_thumb.svg": {
        "title": "Lexer & Inverted Index Engine",
        "category": "INFORMATION RETRIEVAL • NLP",
        "category_color": "#06b6d4",
        "bg_start": "#0b0f19",
        "bg_end": "#083344",
        "accent": "#22d3ee",
        "accent2": "#a78bfa",
        "badge": "Porter Stemmer • Inverted Index",
        "badge_color": "#22d3ee",
        "content_svg": """
            <g transform="translate(40, 75)">
                <!-- Text Stream Input -->
                <rect x="0" y="20" width="120" height="110" rx="8" fill="#1e293b" stroke="#22d3ee" stroke-width="2"/>
                <text x="15" y="25" fill="#22d3ee" font-size="10.5" font-weight="700">RAW TEXT STREAM</text>
                <text x="15" y="55" fill="#ffffff" font-size="9" font-family="monospace">"Information"</text>
                <text x="15" y="75" fill="#ffffff" font-size="9" font-family="monospace">"Retrieval"</text>
                <text x="15" y="95" fill="#ffffff" font-size="9" font-family="monospace">"Searching"</text>

                <path d="M125 75 L165 75" stroke="#22d3ee" stroke-width="2"/>

                <!-- Tokenizer & Porter Stemmer -->
                <g transform="translate(175, 0)">
                    <rect width="220" height="160" rx="10" fill="#111827" stroke="#22d3ee" stroke-width="2" filter="drop-shadow(0 6px 18px rgba(34,211,238,0.25))"/>
                    <text x="20" y="26" fill="#22d3ee" font-size="11" font-weight="800">LEXICAL TOKEN PIPELINE</text>
                    
                    <rect x="15" y="45" width="190" height="28" rx="4" fill="#1e293b"/>
                    <text x="25" y="63" fill="#a78bfa" font-size="9.5" font-family="monospace">Tokenize → ["info", "retriev", "search"]</text>
                    
                    <rect x="15" y="80" width="190" height="28" rx="4" fill="#1e293b"/>
                    <text x="25" y="98" fill="#34d399" font-size="9.5" font-family="monospace">Stopwords Filter (O(1) Hash)</text>

                    <rect x="15" y="115" width="190" height="28" rx="4" fill="#1e293b"/>
                    <text x="25" y="133" fill="#fbbf24" font-size="9.5" font-family="monospace">Porter Stemmer Suffix Rules</text>
                </g>

                <path d="M400 75 L435 75" stroke="#10b981" stroke-width="2"/>

                <!-- Inverted Index Output -->
                <g transform="translate(445, 15)">
                    <rect width="115" height="130" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
                    <text x="12" y="24" fill="#10b981" font-size="10" font-weight="700">Inverted Index</text>
                    <text x="12" y="48" fill="#ffffff" font-size="8.5" font-family="monospace">"inform" → [D1, D4]</text>
                    <text x="12" y="68" fill="#ffffff" font-size="8.5" font-family="monospace">"retriev" → [D2, D3]</text>
                    <text x="12" y="88" fill="#ffffff" font-size="8.5" font-family="monospace">"search" → [D1, D2]</text>
                    <text x="12" y="112" fill="#38bdf8" font-size="8.5" font-weight="700">Lookup: O(1)</text>
                </g>
            </g>

            <!-- Bottom Ticker -->
            <g transform="translate(40, 260)">
                <rect width="560" height="50" rx="8" fill="#0f172a" stroke="rgba(255,255,255,0.1)"/>
                <text x="20" y="30" fill="#94a3b8" font-size="11">Components:</text>
                <text x="110" y="30" fill="#ffffff" font-size="11" font-weight="700">Tokenizer • Stopwords Filter • Porter Stemming • Inverted Posting Lists</text>
            </g>
        """
    },
    "skiplist_index_thumb.svg": {
        "title": "Skip List Probabilistic Multi-Tier Index",
        "category": "DATA STRUCTURES • ALGORITHMS",
        "category_color": "#10b981",
        "bg_start": "#0b0f19",
        "bg_end": "#064e3b",
        "accent": "#34d399",
        "accent2": "#60a5fa",
        "badge": "O(log N) Search • Lock-Free Ready",
        "badge_color": "#34d399",
        "content_svg": """
            <!-- Skip List Multi-Tier Hierarchy -->
            <g transform="translate(45, 75)">
                <rect width="550" height="165" rx="12" fill="#111827" stroke="#10b981" stroke-width="2" filter="drop-shadow(0 6px 20px rgba(16,185,129,0.25))"/>
                
                <!-- Level 3 -->
                <text x="20" y="30" fill="#34d399" font-size="10" font-weight="800">LEVEL 3 (Express)</text>
                <g transform="translate(140, 15)">
                    <circle cx="20" cy="12" r="10" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
                    <text x="20" y="16" fill="#ffffff" font-size="9" text-anchor="middle">5</text>
                    <line x1="30" y1="12" x2="270" y2="12" stroke="#34d399" stroke-width="2" stroke-dasharray="4,3"/>
                    <circle cx="280" cy="12" r="10" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
                    <text x="280" y="16" fill="#ffffff" font-size="9" text-anchor="middle">35</text>
                </g>

                <!-- Level 2 -->
                <text x="20" y="75" fill="#60a5fa" font-size="10" font-weight="800">LEVEL 2 (Fast)</text>
                <g transform="translate(140, 60)">
                    <circle cx="20" cy="12" r="10" fill="#1e293b" stroke="#60a5fa" stroke-width="2"/>
                    <text x="20" y="16" fill="#ffffff" font-size="9" text-anchor="middle">5</text>
                    <line x1="30" y1="12" x2="130" y2="12" stroke="#60a5fa" stroke-width="2"/>
                    <circle cx="140" cy="12" r="10" fill="#1e293b" stroke="#60a5fa" stroke-width="2"/>
                    <text x="140" y="16" fill="#ffffff" font-size="9" text-anchor="middle">19</text>
                    <line x1="150" y1="12" x2="270" y2="12" stroke="#60a5fa" stroke-width="2"/>
                    <circle cx="280" cy="12" r="10" fill="#1e293b" stroke="#60a5fa" stroke-width="2"/>
                    <text x="280" y="16" fill="#ffffff" font-size="9" text-anchor="middle">35</text>
                </g>

                <!-- Level 1 (Base linked list) -->
                <text x="20" y="125" fill="#a78bfa" font-size="10" font-weight="800">LEVEL 1 (Base)</text>
                <g transform="translate(140, 110)">
                    <circle cx="20" cy="12" r="10" fill="#1e293b" stroke="#a78bfa" stroke-width="2"/>
                    <text x="20" y="16" fill="#ffffff" font-size="9" text-anchor="middle">5</text>
                    <line x1="30" y1="12" x2="70" y2="12" stroke="#a78bfa" stroke-width="1.5"/>
                    <circle cx="80" cy="12" r="10" fill="#1e293b" stroke="#a78bfa" stroke-width="2"/>
                    <text x="80" y="16" fill="#ffffff" font-size="9" text-anchor="middle">11</text>
                    <line x1="90" y1="12" x2="130" y2="12" stroke="#a78bfa" stroke-width="1.5"/>
                    <circle cx="140" cy="12" r="10" fill="#1e293b" stroke="#a78bfa" stroke-width="2"/>
                    <text x="140" y="16" fill="#ffffff" font-size="9" text-anchor="middle">19</text>
                    <line x1="150" y1="12" x2="190" y2="12" stroke="#a78bfa" stroke-width="1.5"/>
                    <circle cx="200" cy="12" r="10" fill="#1e293b" stroke="#a78bfa" stroke-width="2"/>
                    <text x="200" y="16" fill="#ffffff" font-size="9" text-anchor="middle">24</text>
                    <line x1="210" y1="12" x2="270" y2="12" stroke="#a78bfa" stroke-width="1.5"/>
                    <circle cx="280" cy="12" r="10" fill="#1e293b" stroke="#a78bfa" stroke-width="2"/>
                    <text x="280" y="16" fill="#ffffff" font-size="9" text-anchor="middle">35</text>
                </g>
                
                <!-- Complexity Badge -->
                <g transform="translate(460, 40)">
                    <rect width="70" height="90" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
                    <text x="35" y="25" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">SEARCH</text>
                    <text x="35" y="48" fill="#ffffff" font-size="13" font-weight="900" text-anchor="middle">O(log N)</text>
                    <text x="35" y="68" fill="#94a3b8" font-size="8.5" text-anchor="middle">Binary Skip</text>
                </g>
            </g>

            <!-- Bottom Ticker -->
            <g transform="translate(45, 260)">
                <rect width="550" height="50" rx="8" fill="#0f172a" stroke="rgba(255,255,255,0.1)"/>
                <text x="20" y="30" fill="#94a3b8" font-size="11">Efficiency:</text>
                <text x="85" y="30" fill="#ffffff" font-size="11" font-weight="700">Probabilistic Height Promotion • Multi-Level Forward Pointers</text>
            </g>
        """
    }
}

os.makedirs('images/portfolio', exist_ok=True)

for filename, data in thumbnails.items():
    svg_code = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 360" width="640" height="360" style="background:{data['bg_start']}; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; display: block;">
  <defs>
    <linearGradient id="bgGrad_{filename.replace('.', '_')}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{data['bg_start']}" />
      <stop offset="60%" stop-color="{data['bg_end']}" />
      <stop offset="100%" stop-color="{data['accent']}" stop-opacity="0.3" />
    </linearGradient>
    <pattern id="gridPattern_{filename.replace('.', '_')}" x="0" y="0" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>
    </pattern>
  </defs>

  <!-- Background Base -->
  <rect width="640" height="360" fill="url(#bgGrad_{filename.replace('.', '_')})" />
  <rect width="640" height="360" fill="url(#gridPattern_{filename.replace('.', '_')})" />

  <!-- Top Window Header Bar -->
  <rect x="0" y="0" width="640" height="38" fill="rgba(15, 23, 42, 0.85)" />
  <line x1="0" y1="38" x2="640" y2="38" stroke="rgba(255,255,255,0.1)" stroke-width="1" />
  
  <!-- Traffic Light Window Controls -->
  <circle cx="20" cy="19" r="5" fill="#ef4444" />
  <circle cx="36" cy="19" r="5" fill="#f59e0b" />
  <circle cx="52" cy="19" r="5" fill="#10b981" />

  <!-- Category & Status Badge -->
  <rect x="75" y="8" width="240" height="22" rx="11" fill="rgba(255,255,255,0.08)" />
  <text x="195" y="23" fill="{data['category_color']}" font-size="10" font-weight="800" letter-spacing="0.5" text-anchor="middle">{data['category']}</text>

  <rect x="440" y="8" width="180" height="22" rx="11" fill="rgba(16,185,129,0.15)" stroke="rgba(16,185,129,0.4)" stroke-width="1" />
  <circle cx="455" cy="19" r="3.5" fill="{data['badge_color']}" />
  <text x="535" y="23" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">{data['badge']}</text>

  <!-- Inner Content Graphics -->
  {data['content_svg']}
</svg>"""

    filepath = os.path.join('images/portfolio', filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg_code)
    print(f"Generated {filepath} successfully!")

print("All 12 rich SVG thumbnails created with explicit 640x360 dimensions!")
