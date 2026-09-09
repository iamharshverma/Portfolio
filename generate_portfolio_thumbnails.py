import os

os.makedirs('images/portfolio', exist_ok=True)

thumbnails = {
    'spark_streaming_thumb.svg': {
        'gradient': ('#1e1b4b', '#0f172a', '#3b82f6', '#06b6d4'),
        'badge': 'BIG DATA • STREAMING',
        'badge_bg': '#2563eb',
        'title': 'PySpark Streaming Engine',
        'subtitle': 'Real-Time News Stream & NLP Classification',
        'art': '''
            <!-- Streaming Pipeline Art -->
            <g transform="translate(40, 60)">
                <!-- Grid background -->
                <line x1="0" y1="40" x2="520" y2="40" stroke="rgba(255,255,255,0.06)" stroke-dasharray="4 4" />
                <line x1="0" y1="90" x2="520" y2="90" stroke="rgba(255,255,255,0.06)" stroke-dasharray="4 4" />
                <line x1="0" y1="140" x2="520" y2="140" stroke="rgba(255,255,255,0.06)" stroke-dasharray="4 4" />
                
                <!-- Kafka Stream Source -->
                <rect x="10" y="55" width="90" height="70" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
                <text x="55" y="88" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle" font-family="sans-serif">KAFKA</text>
                <text x="55" y="106" fill="#94a3b8" font-size="10" text-anchor="middle" font-family="sans-serif">Event Ingestion</text>
                
                <!-- Stream Waves -->
                <path d="M 110 90 Q 140 60 170 90 T 230 90" fill="none" stroke="#38bdf8" stroke-width="3" stroke-dasharray="6 3" />
                <polygon points="230,85 240,90 230,95" fill="#38bdf8" />
                
                <!-- Spark Cluster Node -->
                <rect x="250" y="40" width="130" height="100" rx="12" fill="#1e293b" stroke="#f59e0b" stroke-width="2" />
                <circle cx="315" cy="70" r="16" fill="#f59e0b" fill-opacity="0.2" stroke="#f59e0b" stroke-width="2" />
                <path d="M307 70 L315 62 L323 70 L315 78 Z" fill="#f59e0b" />
                <text x="315" y="105" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle" font-family="sans-serif">Spark Core DAG</text>
                <text x="315" y="122" fill="#fbbf24" font-size="10" text-anchor="middle" font-family="sans-serif">Micro-batch Engine</text>
                
                <!-- Stream Out to Classifier -->
                <path d="M 390 90 L 430 90" fill="none" stroke="#10b981" stroke-width="3" stroke-dasharray="4 2" />
                <polygon points="430,85 440,90 430,95" fill="#10b981" />
                
                <!-- Classifier Output -->
                <rect x="445" y="55" width="100" height="70" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="2" />
                <text x="495" y="85" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle" font-family="sans-serif">ML INFERENCE</text>
                <text x="495" y="103" fill="#94a3b8" font-size="10" text-anchor="middle" font-family="sans-serif">Category Preds</text>
            </g>
        '''
    },
    'speech_ai_thumb.svg': {
        'gradient': ('#311042', '#0f172a', '#a855f7', '#ec4899'),
        'badge': 'NLP • SPEECH AI',
        'badge_bg': '#9333ea',
        'title': 'Automatic Speech Recognition',
        'subtitle': 'Acoustic Waveforms & CTC Transformer Decoder',
        'art': '''
            <!-- Speech AI Waveform Art -->
            <g transform="translate(40, 50)">
                <!-- Waveform Bars -->
                <g fill="#c084fc">
                    <rect x="20" y="80" width="6" height="30" rx="3" opacity="0.4" />
                    <rect x="34" y="65" width="6" height="60" rx="3" opacity="0.6" />
                    <rect x="48" y="50" width="6" height="90" rx="3" opacity="0.8" />
                    <rect x="62" y="35" width="6" height="120" rx="3" />
                    <rect x="76" y="55" width="6" height="80" rx="3" opacity="0.8" />
                    <rect x="90" y="70" width="6" height="50" rx="3" opacity="0.6" />
                    <rect x="104" y="45" width="6" height="100" rx="3" opacity="0.9" />
                    <rect x="118" y="60" width="6" height="70" rx="3" opacity="0.7" />
                    <rect x="132" y="75" width="6" height="40" rx="3" opacity="0.5" />
                </g>
                
                <!-- Connector Arrow -->
                <path d="M 160 95 L 210 95" fill="none" stroke="#f472b6" stroke-width="3" stroke-dasharray="4 2" />
                <polygon points="210,90 220,95 210,100" fill="#f472b6" />
                
                <!-- Neural Network Transformer Box -->
                <rect x="230" y="45" width="150" height="100" rx="12" fill="#1e293b" stroke="#ec4899" stroke-width="2" />
                <text x="305" y="75" fill="#f472b6" font-size="12" font-weight="700" text-anchor="middle" font-family="sans-serif">CONV-CTC MODEL</text>
                <text x="305" y="95" fill="#ffffff" font-size="11" text-anchor="middle" font-family="sans-serif">Acoustic Feature Map</text>
                <text x="305" y="115" fill="#94a3b8" font-size="10" text-anchor="middle" font-family="sans-serif">WER Optimization</text>
                
                <!-- Output Text Stream -->
                <path d="M 390 95 L 430 95" fill="none" stroke="#38bdf8" stroke-width="3" />
                <rect x="440" y="55" width="110" height="80" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
                <text x="495" y="85" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle" font-family="sans-serif">TEXT OUTPUT</text>
                <text x="495" y="105" fill="#e2e8f0" font-size="10" text-anchor="middle" font-family="sans-serif">"Speech to Text..."</text>
            </g>
        '''
    },
    'bilstm_sentiment_thumb.svg': {
        'gradient': ('#064e3b', '#0f172a', '#10b981', '#34d399'),
        'badge': 'DEEP LEARNING • NLP',
        'badge_bg': '#059669',
        'title': 'BiLSTM Attention Network',
        'subtitle': 'Bidirectional Context & Sentiment Polarity',
        'art': '''
            <!-- BiLSTM Architecture Art -->
            <g transform="translate(40, 50)">
                <!-- Forward LSTM Layer -->
                <rect x="30" y="40" width="120" height="45" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="2" />
                <text x="90" y="67" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle" font-family="sans-serif">Forward LSTM →</text>
                
                <!-- Backward LSTM Layer -->
                <rect x="30" y="105" width="120" height="45" rx="8" fill="#1e293b" stroke="#60a5fa" stroke-width="2" />
                <text x="90" y="132" fill="#60a5fa" font-size="12" font-weight="700" text-anchor="middle" font-family="sans-serif">← Backward LSTM</text>
                
                <!-- Attention Mechanism Block -->
                <rect x="220" y="40" width="150" height="110" rx="12" fill="#1e293b" stroke="#fbbf24" stroke-width="2" />
                <text x="295" y="75" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle" font-family="sans-serif">SELF-ATTENTION</text>
                <text x="295" y="98" fill="#ffffff" font-size="11" text-anchor="middle" font-family="sans-serif">Context Weighting</text>
                <text x="295" y="120" fill="#94a3b8" font-size="10" text-anchor="middle" font-family="sans-serif">Dense Softmax</text>
                
                <!-- Connecting lines -->
                <path d="M 160 62 L 210 80" stroke="#34d399" stroke-width="2" />
                <path d="M 160 127 L 210 105" stroke="#60a5fa" stroke-width="2" />
                
                <!-- Output Gauge -->
                <rect x="430" y="55" width="115" height="80" rx="10" fill="#1e293b" stroke="#a78bfa" stroke-width="2" />
                <text x="487" y="88" fill="#a78bfa" font-size="11" font-weight="700" text-anchor="middle" font-family="sans-serif">POLARITY SCORE</text>
                <text x="487" y="110" fill="#4ade80" font-size="13" font-weight="700" text-anchor="middle" font-family="sans-serif">+0.94 Positive</text>
            </g>
        '''
    },
    'cross_lingual_spark_thumb.svg': {
        'gradient': ('#1e293b', '#0f172a', '#f97316', '#fbbf24'),
        'badge': 'BIG DATA • LSH INDEXING',
        'badge_bg': '#ea580c',
        'title': 'Multilingual Spark Deduplication',
        'subtitle': 'MinHash LSH & Cross-Language Document Clustering',
        'art': '''
            <!-- Multilingual Spark Art -->
            <g transform="translate(40, 50)">
                <!-- Language Ingestion Nodes -->
                <rect x="20" y="30" width="110" height="35" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" />
                <text x="75" y="52" fill="#38bdf8" font-size="11" font-weight="600" text-anchor="middle" font-family="sans-serif">English Corpora</text>
                
                <rect x="20" y="75" width="110" height="35" rx="6" fill="#1e293b" stroke="#a855f7" stroke-width="1.5" />
                <text x="75" y="97" fill="#a855f7" font-size="11" font-weight="600" text-anchor="middle" font-family="sans-serif">Spanish / French</text>
                
                <rect x="20" y="120" width="110" height="35" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1.5" />
                <text x="75" y="142" fill="#34d399" font-size="11" font-weight="600" text-anchor="middle" font-family="sans-serif">German / Hindi</text>
                
                <!-- Central MinHash LSH Engine -->
                <rect x="200" y="45" width="160" height="95" rx="12" fill="#1e293b" stroke="#f97316" stroke-width="2" />
                <text x="280" y="75" fill="#f97316" font-size="12" font-weight="700" text-anchor="middle" font-family="sans-serif">MinHash LSH Bands</text>
                <text x="280" y="98" fill="#ffffff" font-size="11" text-anchor="middle" font-family="sans-serif">Cross-Language Hash</text>
                <text x="280" y="118" fill="#94a3b8" font-size="10" text-anchor="middle" font-family="sans-serif">Jaccard Sim Matrix</text>
                
                <!-- Connectors -->
                <path d="M 140 47 L 190 75" stroke="#38bdf8" stroke-width="2" />
                <path d="M 140 92 L 190 92" stroke="#a855f7" stroke-width="2" />
                <path d="M 140 137 L 190 110" stroke="#34d399" stroke-width="2" />
                
                <!-- Dedup Output -->
                <rect x="420" y="55" width="125" height="75" rx="10" fill="#1e293b" stroke="#22c55e" stroke-width="2" />
                <text x="482" y="85" fill="#22c55e" font-size="11" font-weight="700" text-anchor="middle" font-family="sans-serif">CANONICAL SET</text>
                <text x="482" y="105" fill="#e2e8f0" font-size="10" text-anchor="middle" font-family="sans-serif">0% Duplicates</text>
            </g>
        '''
    },
    'graph_analytics_thumb.svg': {
        'gradient': ('#1e1e38', '#0f172a', '#e11d48', '#f43f5e'),
        'badge': 'GRAPH AI • NETWORK MINING',
        'badge_bg': '#e11d48',
        'title': 'Social Network Graph Analytics',
        'subtitle': 'Graph Mining, Community Detection & PageRank',
        'art': '''
            <!-- Graph Analytics Nodes -->
            <g transform="translate(50, 45)">
                <!-- Connected Nodes Network -->
                <line x1="80" y1="50" x2="160" y2="90" stroke="rgba(244,63,94,0.4)" stroke-width="2" />
                <line x1="80" y1="50" x2="70" y2="130" stroke="rgba(244,63,94,0.4)" stroke-width="2" />
                <line x1="160" y1="90" x2="250" y2="60" stroke="rgba(244,63,94,0.4)" stroke-width="2" />
                <line x1="160" y1="90" x2="240" y2="130" stroke="rgba(244,63,94,0.4)" stroke-width="2" />
                <line x1="250" y1="60" x2="330" y2="80" stroke="rgba(244,63,94,0.4)" stroke-width="2" />
                <line x1="240" y1="130" x2="330" y2="80" stroke="rgba(244,63,94,0.4)" stroke-width="2" />
                
                <circle cx="80" cy="50" r="14" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
                <circle cx="70" cy="130" r="16" fill="#1e293b" stroke="#a855f7" stroke-width="2" />
                <circle cx="160" cy="90" r="22" fill="#e11d48" stroke="#ffffff" stroke-width="2" />
                <text x="160" y="95" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">HUB</text>
                
                <circle cx="250" cy="60" r="15" fill="#1e293b" stroke="#fbbf24" stroke-width="2" />
                <circle cx="240" cy="130" r="18" fill="#1e293b" stroke="#34d399" stroke-width="2" />
                <circle cx="330" cy="80" r="20" fill="#1e293b" stroke="#f43f5e" stroke-width="2" />
                
                <!-- Metrics Card Overlay -->
                <rect x="380" y="40" width="150" height="100" rx="10" fill="#1e293b" stroke="#f43f5e" stroke-width="2" />
                <text x="455" y="70" fill="#f43f5e" font-size="11" font-weight="700" text-anchor="middle" font-family="sans-serif">GRAPH METRICS</text>
                <text x="455" y="92" fill="#ffffff" font-size="11" text-anchor="middle" font-family="sans-serif">Betweenness: 0.89</text>
                <text x="455" y="112" fill="#94a3b8" font-size="10" text-anchor="middle" font-family="sans-serif">Modularity: 0.74</text>
            </g>
        '''
    },
    'cnn_vision_thumb.svg': {
        'gradient': ('#134e4a', '#0f172a', '#0d9488', '#2dd4bf'),
        'badge': 'COMPUTER VISION • PYTORCH',
        'badge_bg': '#0d9488',
        'title': 'Deep CNN Multi-Class Classifier',
        'subtitle': 'Convolutional Feature Maps & Deep Residual Layers',
        'art': '''
            <!-- CNN Vision Pipeline -->
            <g transform="translate(45, 45)">
                <!-- Input Matrix -->
                <rect x="20" y="40" width="70" height="90" rx="8" fill="#1e293b" stroke="#2dd4bf" stroke-width="2" />
                <text x="55" y="80" fill="#2dd4bf" font-size="11" font-weight="700" text-anchor="middle" font-family="sans-serif">RGB IN</text>
                <text x="55" y="98" fill="#94a3b8" font-size="9" text-anchor="middle" font-family="sans-serif">256x256x3</text>
                
                <!-- Conv Feature Maps -->
                <rect x="120" y="30" width="60" height="80" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" />
                <rect x="135" y="45" width="60" height="80" rx="6" fill="#1e293b" stroke="#60a5fa" stroke-width="1.5" />
                <text x="165" y="85" fill="#ffffff" font-size="10" font-weight="600" text-anchor="middle">Conv2D</text>
                
                <!-- Pooling & Dense -->
                <rect x="230" y="40" width="55" height="70" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" />
                <text x="257" y="78" fill="#f59e0b" font-size="10" font-weight="600" text-anchor="middle">Pool / Res</text>
                
                <!-- Dense Softmax -->
                <rect x="320" y="40" width="90" height="90" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="2" />
                <text x="365" y="75" fill="#c084fc" font-size="11" font-weight="700" text-anchor="middle" font-family="sans-serif">SOFTMAX</text>
                <text x="365" y="95" fill="#ffffff" font-size="10" text-anchor="middle">99.2% Acc</text>
                <text x="365" y="112" fill="#94a3b8" font-size="9" text-anchor="middle">100 Classes</text>
                
                <!-- Output Tag -->
                <rect x="440" y="55" width="95" height="60" rx="8" fill="#0d9488" />
                <text x="487" y="88" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">CLASS: #1</text>
            </g>
        '''
    },
    'microservice_gateway_thumb.svg': {
        'gradient': ('#1e1b4b', '#0f172a', '#6366f1', '#818cf8'),
        'badge': 'BACKEND • HIGH THROUGHPUT',
        'badge_bg': '#4f46e5',
        'title': 'WordDoc Frequency Microservice',
        'subtitle': 'High-Concurrency REST API & Memory-Mapped Lexer',
        'art': '''
            <!-- Microservice API Architecture -->
            <g transform="translate(45, 45)">
                <!-- Client Ingress -->
                <rect x="20" y="55" width="95" height="65" rx="10" fill="#1e293b" stroke="#818cf8" stroke-width="2" />
                <text x="67" y="85" fill="#818cf8" font-size="11" font-weight="700" text-anchor="middle" font-family="sans-serif">API INGRESS</text>
                <text x="67" y="103" fill="#94a3b8" font-size="9" text-anchor="middle" font-family="sans-serif">HTTP/2 REST</text>
                
                <path d="M 125 87 L 175 87" stroke="#818cf8" stroke-width="3" stroke-dasharray="4 2" />
                
                <!-- Gateway Load Balancer -->
                <rect x="185" y="40" width="130" height="95" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
                <text x="250" y="70" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle" font-family="sans-serif">ASYNC WORKER POOL</text>
                <text x="250" y="92" fill="#ffffff" font-size="10" text-anchor="middle">Non-blocking IO</text>
                <text x="250" y="112" fill="#94a3b8" font-size="9" text-anchor="middle">10K Req/sec</text>
                
                <!-- Redis / In-Memory Cache -->
                <rect x="360" y="45" width="160" height="85" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="2" />
                <text x="440" y="75" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle" font-family="sans-serif">SHARDED DOC STORE</text>
                <text x="440" y="97" fill="#ffffff" font-size="10" text-anchor="middle">Sub-Millisecond Lookup</text>
                <text x="440" y="115" fill="#94a3b8" font-size="9" text-anchor="middle">O(1) TF-IDF Index</text>
            </g>
        '''
    },
    'hadoop_cluster_thumb.svg': {
        'gradient': ('#262626', '#0f172a', '#eab308', '#ca8a04'),
        'badge': 'DISTRIBUTED SYSTEMS • HDFS',
        'badge_bg': '#ca8a04',
        'title': 'Hadoop Distributed Social MapReduce',
        'subtitle': 'HDFS Cluster Sharding & Distributed Graph Analytics',
        'art': '''
            <!-- Hadoop Cluster Architecture -->
            <g transform="translate(45, 45)">
                <!-- NameNode Master -->
                <rect x="20" y="45" width="120" height="85" rx="10" fill="#1e293b" stroke="#eab308" stroke-width="2" />
                <text x="80" y="75" fill="#eab308" font-size="11" font-weight="700" text-anchor="middle" font-family="sans-serif">NAMENODE MASTER</text>
                <text x="80" y="95" fill="#ffffff" font-size="10" text-anchor="middle">Metadata Manager</text>
                <text x="80" y="112" fill="#94a3b8" font-size="9" text-anchor="middle">Job Tracker</text>
                
                <!-- Split paths -->
                <path d="M 150 70 L 210 50" stroke="#eab308" stroke-width="2" />
                <path d="M 150 87 L 210 87" stroke="#eab308" stroke-width="2" />
                <path d="M 150 105 L 210 125" stroke="#eab308" stroke-width="2" />
                
                <!-- DataNodes / Mappers -->
                <rect x="220" y="30" width="110" height="35" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" />
                <text x="275" y="52" fill="#38bdf8" font-size="10" font-weight="600" text-anchor="middle">DataNode #1 / Map</text>
                
                <rect x="220" y="70" width="110" height="35" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" />
                <text x="275" y="92" fill="#38bdf8" font-size="10" font-weight="600" text-anchor="middle">DataNode #2 / Map</text>
                
                <rect x="220" y="110" width="110" height="35" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" />
                <text x="275" y="132" fill="#38bdf8" font-size="10" font-weight="600" text-anchor="middle">DataNode #3 / Map</text>
                
                <!-- Reducer Node -->
                <rect x="375" y="45" width="150" height="85" rx="10" fill="#1e293b" stroke="#22c55e" stroke-width="2" />
                <text x="450" y="75" fill="#22c55e" font-size="11" font-weight="700" text-anchor="middle" font-family="sans-serif">DISTRIBUTED REDUCER</text>
                <text x="450" y="95" fill="#ffffff" font-size="10" text-anchor="middle">Aggregation & Shuffler</text>
                <text x="450" y="112" fill="#94a3b8" font-size="9" text-anchor="middle">HDFS Final Output</text>
            </g>
        '''
    },
    'lockfree_hashtable_thumb.svg': {
        'gradient': ('#1e1b4b', '#0f172a', '#3b82f6', '#1d4ed8'),
        'badge': 'SYSTEMS • CONCURRENCY',
        'badge_bg': '#1d4ed8',
        'title': 'Lock-Free Concurrent Hash Table',
        'subtitle': 'Atomic CAS Operations & High-Contention Memory Lanes',
        'art': '''
            <!-- Lock Free Architecture -->
            <g transform="translate(45, 45)">
                <!-- Multi-threaded Cores -->
                <rect x="20" y="30" width="100" height="30" rx="6" fill="#1e293b" stroke="#60a5fa" stroke-width="1.5" />
                <text x="70" y="50" fill="#60a5fa" font-size="10" font-weight="600" text-anchor="middle">Thread Core 1</text>
                
                <rect x="20" y="70" width="100" height="30" rx="6" fill="#1e293b" stroke="#60a5fa" stroke-width="1.5" />
                <text x="70" y="90" fill="#60a5fa" font-size="10" font-weight="600" text-anchor="middle">Thread Core 2</text>
                
                <rect x="20" y="110" width="100" height="30" rx="6" fill="#1e293b" stroke="#60a5fa" stroke-width="1.5" />
                <text x="70" y="130" fill="#60a5fa" font-size="10" font-weight="600" text-anchor="middle">Thread Core N</text>
                
                <!-- CAS Lock-Free Barrier -->
                <rect x="170" y="40" width="140" height="95" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="2" />
                <text x="240" y="70" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle" font-family="sans-serif">ATOMIC CAS ENGINE</text>
                <text x="240" y="92" fill="#ffffff" font-size="10" text-anchor="middle">Compare-And-Swap</text>
                <text x="240" y="112" fill="#94a3b8" font-size="9" text-anchor="middle">Zero Thread Block</text>
                
                <!-- Segmented Buckets -->
                <rect x="350" y="40" width="175" height="95" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="2" />
                <text x="437" y="70" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle" font-family="sans-serif">CONCURRENT BUCKETS</text>
                <text x="437" y="92" fill="#ffffff" font-size="10" text-anchor="middle">Robin Hood Hashing</text>
                <text x="437" y="112" fill="#94a3b8" font-size="9" text-anchor="middle">Lock-Free Resizing</text>
            </g>
        '''
    },
    'ir_tokenizer_thumb.svg': {
        'gradient': ('#3b0764', '#0f172a', '#9333ea', '#c084fc'),
        'badge': 'NLP • INFORMATION RETRIEVAL',
        'badge_bg': '#7e22ce',
        'title': 'High-Speed Tokenizer & Stemmer',
        'subtitle': 'Porter/Snowball Morphological Stream Engine',
        'art': '''
            <!-- Tokenizer Stream Art -->
            <g transform="translate(45, 45)">
                <!-- Raw Text Stream -->
                <rect x="20" y="50" width="105" height="75" rx="8" fill="#1e293b" stroke="#c084fc" stroke-width="2" />
                <text x="72" y="80" fill="#c084fc" font-size="11" font-weight="700" text-anchor="middle" font-family="sans-serif">RAW TEXT IN</text>
                <text x="72" y="100" fill="#94a3b8" font-size="9" text-anchor="middle" font-family="sans-serif">UTF-8 Byte Stream</text>
                
                <!-- Regex / Trie Lexer -->
                <rect x="170" y="40" width="150" height="95" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
                <text x="245" y="70" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle" font-family="sans-serif">DETERMINISTIC DFA</text>
                <text x="245" y="92" fill="#ffffff" font-size="10" text-anchor="middle">Stopwords & Punctuation</text>
                <text x="245" y="112" fill="#94a3b8" font-size="9" text-anchor="middle">Zero-Allocation Pipeline</text>
                
                <!-- Stemmed Token Array -->
                <rect x="365" y="45" width="160" height="85" rx="10" fill="#1e293b" stroke="#4ade80" stroke-width="2" />
                <text x="445" y="75" fill="#4ade80" font-size="11" font-weight="700" text-anchor="middle" font-family="sans-serif">STEMMED INVERTED INDEX</text>
                <text x="445" y="95" fill="#ffffff" font-size="10" text-anchor="middle">Tokens: [comput, secur, scal]</text>
                <text x="445" y="112" fill="#94a3b8" font-size="9" text-anchor="middle">Term Freq Vectorized</text>
            </g>
        '''
    },
    'skiplist_index_thumb.svg': {
        'gradient': ('#1e293b', '#0f172a', '#0284c7', '#38bdf8'),
        'badge': 'ALGORITHMS • DATA STRUCTURES',
        'badge_bg': '#0284c7',
        'title': 'Probabilistic Skip-List Index',
        'subtitle': 'Multi-Tier Pointers & O(log N) Fast Lookups',
        'art': '''
            <!-- Skip List Levels -->
            <g transform="translate(45, 45)">
                <!-- Level 3 (Express Lane) -->
                <text x="20" y="45" fill="#38bdf8" font-size="10" font-weight="700" font-family="sans-serif">L3 Express:</text>
                <circle cx="120" cy="40" r="10" fill="#0284c7" />
                <text x="120" y="44" fill="#fff" font-size="9" text-anchor="middle">10</text>
                <line x1="130" y1="40" x2="350" y2="40" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 2" />
                <circle cx="360" cy="40" r="10" fill="#0284c7" />
                <text x="360" y="44" fill="#fff" font-size="9" text-anchor="middle">80</text>
                
                <!-- Level 2 -->
                <text x="20" y="85" fill="#38bdf8" font-size="10" font-weight="700" font-family="sans-serif">L2 Fast:</text>
                <circle cx="120" cy="80" r="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
                <circle cx="230" cy="80" r="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
                <text x="230" y="84" fill="#fff" font-size="9" text-anchor="middle">45</text>
                <circle cx="360" cy="80" r="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
                <line x1="130" y1="80" x2="220" y2="80" stroke="#38bdf8" stroke-width="1.5" />
                <line x1="240" y1="80" x2="350" y2="80" stroke="#38bdf8" stroke-width="1.5" />
                
                <!-- Level 1 (Dense) -->
                <text x="20" y="125" fill="#38bdf8" font-size="10" font-weight="700" font-family="sans-serif">L1 Base:</text>
                <circle cx="120" cy="120" r="8" fill="#64748b" />
                <circle cx="170" cy="120" r="8" fill="#64748b" />
                <circle cx="230" cy="120" r="8" fill="#64748b" />
                <circle cx="290" cy="120" r="8" fill="#64748b" />
                <circle cx="360" cy="120" r="8" fill="#64748b" />
                <line x1="128" y1="120" x2="352" y2="120" stroke="#64748b" stroke-width="1" />
                
                <!-- Complexity Overlay -->
                <rect x="400" y="45" width="130" height="85" rx="10" fill="#1e293b" stroke="#22c55e" stroke-width="2" />
                <text x="465" y="75" fill="#22c55e" font-size="11" font-weight="700" text-anchor="middle" font-family="sans-serif">TIME COMPLEXITY</text>
                <text x="465" y="95" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">O(log N)</text>
                <text x="465" y="112" fill="#94a3b8" font-size="9" text-anchor="middle">Concurrent Lock-Free</text>
            </g>
        '''
    },
    'agentic_security_thumb.svg': {
        'gradient': ('#0f172a', '#1e293b', '#6366f1', '#06b6d4'),
        'badge': 'AI SECURITY • AGENTIC SYSTEMS',
        'badge_bg': '#4338ca',
        'title': 'Agentic Security & NHI Guardrails',
        'subtitle': 'Zero-Trust Non-Human Identity & Defensive Boundary',
        'art': '''
            <!-- Agentic Security Architecture -->
            <g transform="translate(45, 45)">
                <!-- Autonomous Agent -->
                <rect x="20" y="45" width="115" height="85" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
                <circle cx="77" cy="72" r="14" fill="#38bdf8" fill-opacity="0.2" stroke="#38bdf8" stroke-width="2" />
                <text x="77" y="102" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle" font-family="sans-serif">AI AGENT FLEET</text>
                <text x="77" y="118" fill="#38bdf8" font-size="9" text-anchor="middle" font-family="sans-serif">Autonomous Tool Call</text>
                
                <!-- Defensive Boundary / Firewall -->
                <rect x="180" y="35" width="160" height="105" rx="12" fill="#1e293b" stroke="#ef4444" stroke-width="2" />
                <text x="260" y="65" fill="#f87171" font-size="11" font-weight="700" text-anchor="middle" font-family="sans-serif">AGENTIC GUARDRAILS</text>
                <text x="260" y="85" fill="#ffffff" font-size="10" text-anchor="middle">Prompt Firewall & Boundary</text>
                <text x="260" y="103" fill="#fbbf24" font-size="9" text-anchor="middle">NHI Spiffe/Spire Attest</text>
                <text x="260" y="122" fill="#94a3b8" font-size="9" text-anchor="middle">Zero-Trust Isolation</text>
                
                <!-- Cloud Enterprise Target -->
                <rect x="380" y="45" width="145" height="85" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="2" />
                <text x="452" y="75" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle" font-family="sans-serif">ENTERPRISE CLOUD</text>
                <text x="452" y="95" fill="#ffffff" font-size="10" text-anchor="middle">Protected Data Store</text>
                <text x="452" y="112" fill="#94a3b8" font-size="9" text-anchor="middle">Deterministic Audit Log</text>
            </g>
        '''
    }
}

template = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 360" width="100%" height="100%" style="background:#0f172a; border-radius: 12px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <linearGradient id="bgGrad_{name}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{grad0}" />
      <stop offset="60%" stop-color="{grad1}" />
      <stop offset="100%" stop-color="{grad2}" />
    </linearGradient>
    <linearGradient id="accentGrad_{name}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{grad2}" />
      <stop offset="100%" stop-color="{grad3}" />
    </linearGradient>
    <pattern id="dotPattern_{name}" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="rgba(255,255,255,0.08)" />
    </pattern>
  </defs>

  <!-- Background Base -->
  <rect width="640" height="360" fill="url(#bgGrad_{name})" rx="12" />
  <rect width="640" height="360" fill="url(#dotPattern_{name})" rx="12" />

  <!-- Outer Glow Frame -->
  <rect x="8" y="8" width="624" height="344" rx="10" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5" />

  <!-- Top Header Tag & Status -->
  <g transform="translate(30, 24)">
    <rect x="0" y="0" width="165" height="26" rx="13" fill="{badge_bg}" fill-opacity="0.9" />
    <text x="82" y="17" fill="#ffffff" font-size="10.5" font-weight="800" letter-spacing="0.5" text-anchor="middle">{badge}</text>
    
    <circle cx="560" cy="13" r="4" fill="#22c55e" />
    <text x="548" y="17" fill="#94a3b8" font-size="11" font-weight="600" text-anchor="end">Production Ready</text>
  </g>

  <!-- Main Central Visual Art -->
  {art}

  <!-- Bottom Title & Subtitle Banner -->
  <g transform="translate(30, 280)">
    <rect x="0" y="0" width="580" height="58" rx="8" fill="rgba(15, 23, 42, 0.75)" stroke="rgba(255,255,255,0.08)" stroke-width="1" />
    <text x="18" y="26" fill="#f8fafc" font-size="16" font-weight="700">{title}</text>
    <text x="18" y="46" fill="#94a3b8" font-size="12" font-weight="500">{subtitle}</text>
    
    <!-- Code Bracket Symbol -->
    <g transform="translate(530, 16)">
      <circle cx="14" cy="14" r="14" fill="rgba(255,255,255,0.08)" />
      <path d="M 11 9 L 6 14 L 11 19" fill="none" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" />
      <path d="M 17 9 L 22 14 L 17 19" fill="none" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" />
    </g>
  </g>
</svg>
"""

for fname, data in thumbnails.items():
    clean_name = fname.replace('.', '_')
    svg_content = template.format(
        name=clean_name,
        grad0=data['gradient'][0],
        grad1=data['gradient'][1],
        grad2=data['gradient'][2],
        grad3=data['gradient'][3],
        badge=data['badge'],
        badge_bg=data['badge_bg'],
        title=data['title'],
        subtitle=data['subtitle'],
        art=data['art']
    )
    with open(os.path.join('images/portfolio', fname), 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"Generated {fname}")

print(f"Successfully generated {len(thumbnails)} custom high-craft portfolio thumbnails!")
