import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Build Projects HTML
projects_html = '''        <!-- Projects/Work Start -->
        <section class="section bg-light" id="projects">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-12 text-center">
                        <div class="container-title text-center mb-4 pb-2">
                            <div class="titles">
                                <span class="badge badge-primary px-3 py-2 text-uppercase mb-2 font-weight-bold" style="letter-spacing: 1px; font-size: 11px;">
                                    <i class="mdi mdi-code-tags mr-1"></i> Open-Source &amp; Research Engineering
                                </span>
                                <h2 class="title text-capitalize mb-3">Work &amp; Past Projects</h2>
                                <p class="para-desc-600 text-muted mb-0 mx-auto" style="max-width: 720px; font-size: 15.5px; line-height: 1.6;">
                                    Production-grade architectures spanning <b>Distributed Systems</b>, <b>Agentic AI Security</b>, <b>Speech &amp; NLP Transformers</b>, and <b>High-Concurrency Systems</b>.
                                </p>
                                <div class="home-projects-stats d-flex flex-wrap justify-content-center align-items-center mt-3" style="gap: 12px;">
                                    <span class="badge badge-light border px-3 py-2 text-dark font-weight-bold"><i class="mdi mdi-github-face mr-1 text-primary"></i> 12+ Open Repositories</span>
                                    <span class="badge badge-light border px-3 py-2 text-dark font-weight-bold"><i class="mdi mdi-server-network mr-1 text-success"></i> High-Concurrency &amp; Distributed</span>
                                    <span class="badge badge-light border px-3 py-2 text-dark font-weight-bold"><i class="mdi mdi-shield-check mr-1 text-info"></i> Zero-Trust &amp; Agentic AI</span>
                                </div>
                            </div>
                        </div>
                    </div><!--end col-->
                </div><!--end row-->

                <!-- Interactive Category Filter Buttons -->
                <div class="row mb-4">
                    <div class="col-12 text-center">
                        <div class="home-project-filters d-flex flex-wrap justify-content-center" style="gap: 8px;">
                            <button type="button" class="btn btn-sm home-proj-filter-btn active rounded-pill px-3 py-2 font-weight-bold" onclick="filterHomeProjects('all', this)">
                                All Projects (12)
                            </button>
                            <button type="button" class="btn btn-sm home-proj-filter-btn rounded-pill px-3 py-2 font-weight-bold" onclick="filterHomeProjects('bigdata', this)">
                                <i class="mdi mdi-database mr-1"></i> Big Data &amp; Distributed (4)
                            </button>
                            <button type="button" class="btn btn-sm home-proj-filter-btn rounded-pill px-3 py-2 font-weight-bold" onclick="filterHomeProjects('nlp', this)">
                                <i class="mdi mdi-brain mr-1"></i> AI &amp; NLP (4)
                            </button>
                            <button type="button" class="btn btn-sm home-proj-filter-btn rounded-pill px-3 py-2 font-weight-bold" onclick="filterHomeProjects('security', this)">
                                <i class="mdi mdi-shield-key mr-1"></i> Security &amp; Systems (3)
                            </button>
                            <button type="button" class="btn btn-sm home-proj-filter-btn rounded-pill px-3 py-2 font-weight-bold" onclick="filterHomeProjects('vision', this)">
                                <i class="mdi mdi-eye mr-1"></i> Computer Vision (1)
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Projects Grid -->
                <div class="row" id="homeProjectsGrid">

                    <!-- Project 1: Agentic Security -->
                    <div class="col-lg-4 col-md-6 col-12 mt-4 pt-2 home-proj-card" data-category="security">
                        <div class="card border-0 work-container work-modern position-relative d-block overflow-hidden rounded shadow-sm bg-white h-100" style="transition: transform 0.3s ease, box-shadow 0.3s ease;">
                            <div class="card-body p-0 position-relative">
                                <div class="proj-thumb-wrapper position-relative overflow-hidden" style="background: #0f172a; aspect-ratio: 16/9;">
                                    <img src="images/portfolio/agentic_security_thumb.svg" class="img-fluid w-100 h-100" alt="Agentic Security Guardrails" style="object-fit: cover;" referrerpolicy="no-referrer">
                                    <div class="proj-overlay position-absolute w-100 h-100 d-flex align-items-center justify-content-center" style="top:0; left:0; background: rgba(15,23,42,0.85); opacity: 0; transition: opacity 0.3s ease;">
                                        <div class="text-center p-3">
                                            <a href="https://github.com/iamharshverma" target="_blank" class="btn btn-sm btn-primary rounded-pill px-3 mr-2 mb-2"><i class="mdi mdi-github-face mr-1"></i> GitHub Repo</a>
                                            <a href="page-portfolio" class="btn btn-sm btn-outline-light rounded-pill px-3 mb-2"><i class="mdi mdi-information-outline mr-1"></i> Details</a>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-3">
                                    <div class="d-flex align-items-center justify-content-between mb-2">
                                        <span class="badge badge-danger px-2 py-1 font-weight-bold" style="font-size: 11px;">AI SECURITY • ZERO-TRUST</span>
                                        <small class="text-muted"><i class="mdi mdi-lock-check text-success mr-1"></i> Production Ready</small>
                                    </div>
                                    <h5 class="mb-2" style="font-size: 17px; line-height: 1.35;">
                                        <a href="https://github.com/iamharshverma" target="_blank" class="text-dark font-weight-bold proj-title-link">Agentic Security &amp; NHI Guardrails</a>
                                    </h5>
                                    <p class="text-muted small mb-3" style="line-height: 1.5; min-height: 42px;">
                                        Zero-Trust Non-Human Identity (NHI) boundary and runtime prompt firewall protecting autonomous multi-agent tool calls.
                                    </p>
                                    <div class="d-flex flex-wrap mb-3" style="gap: 5px;">
                                        <span class="badge badge-light border text-muted">Agentic AI</span>
                                        <span class="badge badge-light border text-muted">SPIFFE/SPIRE</span>
                                        <span class="badge badge-light border text-muted">Zero-Trust</span>
                                        <span class="badge badge-light border text-muted">FastAPI</span>
                                    </div>
                                    <div class="d-flex align-items-center justify-content-between pt-2 border-top">
                                        <a href="https://github.com/iamharshverma" target="_blank" class="text-primary font-weight-bold small d-inline-flex align-items-center">
                                            <i class="mdi mdi-github-face mr-1 font-16"></i> View Source Code <i class="mdi mdi-chevron-right ml-1"></i>
                                        </a>
                                        <span class="text-muted small"><i class="mdi mdi-star text-warning"></i> Open Source</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div><!--end col-->

                    <!-- Project 2: PySpark Streaming -->
                    <div class="col-lg-4 col-md-6 col-12 mt-4 pt-2 home-proj-card" data-category="bigdata">
                        <div class="card border-0 work-container work-modern position-relative d-block overflow-hidden rounded shadow-sm bg-white h-100" style="transition: transform 0.3s ease, box-shadow 0.3s ease;">
                            <div class="card-body p-0 position-relative">
                                <div class="proj-thumb-wrapper position-relative overflow-hidden" style="background: #0f172a; aspect-ratio: 16/9;">
                                    <img src="images/portfolio/spark_streaming_thumb.svg" class="img-fluid w-100 h-100" alt="PySpark Streaming MultiNews Classification" style="object-fit: cover;" referrerpolicy="no-referrer">
                                    <div class="proj-overlay position-absolute w-100 h-100 d-flex align-items-center justify-content-center" style="top:0; left:0; background: rgba(15,23,42,0.85); opacity: 0; transition: opacity 0.3s ease;">
                                        <div class="text-center p-3">
                                            <a href="https://github.com/iamharshverma/PySparkStreaming-MultiNewsClassification" target="_blank" class="btn btn-sm btn-primary rounded-pill px-3 mr-2 mb-2"><i class="mdi mdi-github-face mr-1"></i> GitHub Repo</a>
                                            <a href="page-portfolio" class="btn btn-sm btn-outline-light rounded-pill px-3 mb-2"><i class="mdi mdi-information-outline mr-1"></i> Details</a>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-3">
                                    <div class="d-flex align-items-center justify-content-between mb-2">
                                        <span class="badge badge-primary px-2 py-1 font-weight-bold" style="font-size: 11px;">BIG DATA • STREAMING</span>
                                        <small class="text-muted"><i class="mdi mdi-check-circle text-success mr-1"></i> Verified</small>
                                    </div>
                                    <h5 class="mb-2" style="font-size: 17px; line-height: 1.35;">
                                        <a href="https://github.com/iamharshverma/PySparkStreaming-MultiNewsClassification" target="_blank" class="text-dark font-weight-bold proj-title-link">PySpark Streaming MultiNews Classifier</a>
                                    </h5>
                                    <p class="text-muted small mb-3" style="line-height: 1.5; min-height: 42px;">
                                        Distributed Apache Spark Streaming pipeline with Kafka event ingestion for real-time multilingual news topic classification.
                                    </p>
                                    <div class="d-flex flex-wrap mb-3" style="gap: 5px;">
                                        <span class="badge badge-light border text-muted">PySpark</span>
                                        <span class="badge badge-light border text-muted">Apache Kafka</span>
                                        <span class="badge badge-light border text-muted">NLP DAG</span>
                                        <span class="badge badge-light border text-muted">Micro-batch</span>
                                    </div>
                                    <div class="d-flex align-items-center justify-content-between pt-2 border-top">
                                        <a href="https://github.com/iamharshverma/PySparkStreaming-MultiNewsClassification" target="_blank" class="text-primary font-weight-bold small d-inline-flex align-items-center">
                                            <i class="mdi mdi-github-face mr-1 font-16"></i> View Source Code <i class="mdi mdi-chevron-right ml-1"></i>
                                        </a>
                                        <span class="text-muted small"><i class="mdi mdi-star text-warning"></i> 250+ Commits</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div><!--end col-->

                    <!-- Project 3: Speech AI -->
                    <div class="col-lg-4 col-md-6 col-12 mt-4 pt-2 home-proj-card" data-category="nlp">
                        <div class="card border-0 work-container work-modern position-relative d-block overflow-hidden rounded shadow-sm bg-white h-100" style="transition: transform 0.3s ease, box-shadow 0.3s ease;">
                            <div class="card-body p-0 position-relative">
                                <div class="proj-thumb-wrapper position-relative overflow-hidden" style="background: #0f172a; aspect-ratio: 16/9;">
                                    <img src="images/portfolio/speech_ai_thumb.svg" class="img-fluid w-100 h-100" alt="NLP Automatic Speech Recognition" style="object-fit: cover;" referrerpolicy="no-referrer">
                                    <div class="proj-overlay position-absolute w-100 h-100 d-flex align-items-center justify-content-center" style="top:0; left:0; background: rgba(15,23,42,0.85); opacity: 0; transition: opacity 0.3s ease;">
                                        <div class="text-center p-3">
                                            <a href="https://github.com/iamharshverma/NLP-Automatic-Speech-Recognization" target="_blank" class="btn btn-sm btn-primary rounded-pill px-3 mr-2 mb-2"><i class="mdi mdi-github-face mr-1"></i> GitHub Repo</a>
                                            <a href="page-portfolio" class="btn btn-sm btn-outline-light rounded-pill px-3 mb-2"><i class="mdi mdi-information-outline mr-1"></i> Details</a>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-3">
                                    <div class="d-flex align-items-center justify-content-between mb-2">
                                        <span class="badge badge-purple px-2 py-1 font-weight-bold text-white" style="font-size: 11px; background: #9333ea;">NLP • SPEECH AI</span>
                                        <small class="text-muted"><i class="mdi mdi-waveform text-info mr-1"></i> Audio DSP</small>
                                    </div>
                                    <h5 class="mb-2" style="font-size: 17px; line-height: 1.35;">
                                        <a href="https://github.com/iamharshverma/NLP-Automatic-Speech-Recognization" target="_blank" class="text-dark font-weight-bold proj-title-link">Automatic Speech Recognition (ASR)</a>
                                    </h5>
                                    <p class="text-muted small mb-3" style="line-height: 1.5; min-height: 42px;">
                                        Acoustic spectrogram feature extraction and Connectionist Temporal Classification (CTC) neural speech-to-text decoder.
                                    </p>
                                    <div class="d-flex flex-wrap mb-3" style="gap: 5px;">
                                        <span class="badge badge-light border text-muted">PyTorch</span>
                                        <span class="badge badge-light border text-muted">CTC Loss</span>
                                        <span class="badge badge-light border text-muted">Spectrogram</span>
                                        <span class="badge badge-light border text-muted">Transformers</span>
                                    </div>
                                    <div class="d-flex align-items-center justify-content-between pt-2 border-top">
                                        <a href="https://github.com/iamharshverma/NLP-Automatic-Speech-Recognization" target="_blank" class="text-primary font-weight-bold small d-inline-flex align-items-center">
                                            <i class="mdi mdi-github-face mr-1 font-16"></i> View Source Code <i class="mdi mdi-chevron-right ml-1"></i>
                                        </a>
                                        <span class="text-muted small"><i class="mdi mdi-star text-warning"></i> Open Source</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div><!--end col-->

                    <!-- Project 4: BiLSTM Sentiment -->
                    <div class="col-lg-4 col-md-6 col-12 mt-4 pt-2 home-proj-card" data-category="nlp">
                        <div class="card border-0 work-container work-modern position-relative d-block overflow-hidden rounded shadow-sm bg-white h-100" style="transition: transform 0.3s ease, box-shadow 0.3s ease;">
                            <div class="card-body p-0 position-relative">
                                <div class="proj-thumb-wrapper position-relative overflow-hidden" style="background: #0f172a; aspect-ratio: 16/9;">
                                    <img src="images/portfolio/bilstm_sentiment_thumb.svg" class="img-fluid w-100 h-100" alt="NLP BiLSTM Sentiment Analysis" style="object-fit: cover;" referrerpolicy="no-referrer">
                                    <div class="proj-overlay position-absolute w-100 h-100 d-flex align-items-center justify-content-center" style="top:0; left:0; background: rgba(15,23,42,0.85); opacity: 0; transition: opacity 0.3s ease;">
                                        <div class="text-center p-3">
                                            <a href="https://github.com/iamharshverma/NLP-BiLSTM_SentimentAnalysis" target="_blank" class="btn btn-sm btn-primary rounded-pill px-3 mr-2 mb-2"><i class="mdi mdi-github-face mr-1"></i> GitHub Repo</a>
                                            <a href="page-portfolio" class="btn btn-sm btn-outline-light rounded-pill px-3 mb-2"><i class="mdi mdi-information-outline mr-1"></i> Details</a>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-3">
                                    <div class="d-flex align-items-center justify-content-between mb-2">
                                        <span class="badge badge-success px-2 py-1 font-weight-bold" style="font-size: 11px;">DEEP LEARNING • NLP</span>
                                        <small class="text-muted"><i class="mdi mdi-chart-bell-curve text-success mr-1"></i> 94% Accuracy</small>
                                    </div>
                                    <h5 class="mb-2" style="font-size: 17px; line-height: 1.35;">
                                        <a href="https://github.com/iamharshverma/NLP-BiLSTM_SentimentAnalysis" target="_blank" class="text-dark font-weight-bold proj-title-link">BiLSTM Sentiment &amp; Attention Network</a>
                                    </h5>
                                    <p class="text-muted small mb-3" style="line-height: 1.5; min-height: 42px;">
                                        Bidirectional LSTM recurrent network paired with self-attention mechanisms for deep contextual sentiment polarity evaluation.
                                    </p>
                                    <div class="d-flex flex-wrap mb-3" style="gap: 5px;">
                                        <span class="badge badge-light border text-muted">BiLSTM</span>
                                        <span class="badge badge-light border text-muted">Attention</span>
                                        <span class="badge badge-light border text-muted">TensorFlow</span>
                                        <span class="badge badge-light border text-muted">Word Embeddings</span>
                                    </div>
                                    <div class="d-flex align-items-center justify-content-between pt-2 border-top">
                                        <a href="https://github.com/iamharshverma/NLP-BiLSTM_SentimentAnalysis" target="_blank" class="text-primary font-weight-bold small d-inline-flex align-items-center">
                                            <i class="mdi mdi-github-face mr-1 font-16"></i> View Source Code <i class="mdi mdi-chevron-right ml-1"></i>
                                        </a>
                                        <span class="text-muted small"><i class="mdi mdi-star text-warning"></i> Open Source</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div><!--end col-->

                    <!-- Project 5: Cross Language MinHash -->
                    <div class="col-lg-4 col-md-6 col-12 mt-4 pt-2 home-proj-card" data-category="bigdata">
                        <div class="card border-0 work-container work-modern position-relative d-block overflow-hidden rounded shadow-sm bg-white h-100" style="transition: transform 0.3s ease, box-shadow 0.3s ease;">
                            <div class="card-body p-0 position-relative">
                                <div class="proj-thumb-wrapper position-relative overflow-hidden" style="background: #0f172a; aspect-ratio: 16/9;">
                                    <img src="images/portfolio/cross_lingual_spark_thumb.svg" class="img-fluid w-100 h-100" alt="PySpark Cross-Language Article Deduplication" style="object-fit: cover;" referrerpolicy="no-referrer">
                                    <div class="proj-overlay position-absolute w-100 h-100 d-flex align-items-center justify-content-center" style="top:0; left:0; background: rgba(15,23,42,0.85); opacity: 0; transition: opacity 0.3s ease;">
                                        <div class="text-center p-3">
                                            <a href="https://github.com/iamharshverma/PySpark-LargeScaleDataCollection_Preprocessing_Cross_language_Articles_Duplication_Detection" target="_blank" class="btn btn-sm btn-primary rounded-pill px-3 mr-2 mb-2"><i class="mdi mdi-github-face mr-1"></i> GitHub Repo</a>
                                            <a href="page-portfolio" class="btn btn-sm btn-outline-light rounded-pill px-3 mb-2"><i class="mdi mdi-information-outline mr-1"></i> Details</a>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-3">
                                    <div class="d-flex align-items-center justify-content-between mb-2">
                                        <span class="badge badge-warning px-2 py-1 font-weight-bold text-dark" style="font-size: 11px;">BIG DATA • LSH INDEXING</span>
                                        <small class="text-muted"><i class="mdi mdi-translate text-primary mr-1"></i> Multilingual</small>
                                    </div>
                                    <h5 class="mb-2" style="font-size: 17px; line-height: 1.35;">
                                        <a href="https://github.com/iamharshverma/PySpark-LargeScaleDataCollection_Preprocessing_Cross_language_Articles_Duplication_Detection" target="_blank" class="text-dark font-weight-bold proj-title-link">Cross-Language Spark Deduplication</a>
                                    </h5>
                                    <p class="text-muted small mb-3" style="line-height: 1.5; min-height: 42px;">
                                        Large-scale distributed MinHash Local Sensitivity Hashing (LSH) pipeline for near-duplicate article detection across languages.
                                    </p>
                                    <div class="d-flex flex-wrap mb-3" style="gap: 5px;">
                                        <span class="badge badge-light border text-muted">PySpark</span>
                                        <span class="badge badge-light border text-muted">MinHash LSH</span>
                                        <span class="badge badge-light border text-muted">Jaccard Sim</span>
                                        <span class="badge badge-light border text-muted">Distributed</span>
                                    </div>
                                    <div class="d-flex align-items-center justify-content-between pt-2 border-top">
                                        <a href="https://github.com/iamharshverma/PySpark-LargeScaleDataCollection_Preprocessing_Cross_language_Articles_Duplication_Detection" target="_blank" class="text-primary font-weight-bold small d-inline-flex align-items-center">
                                            <i class="mdi mdi-github-face mr-1 font-16"></i> View Source Code <i class="mdi mdi-chevron-right ml-1"></i>
                                        </a>
                                        <span class="text-muted small"><i class="mdi mdi-star text-warning"></i> Open Source</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div><!--end col-->

                    <!-- Project 6: Graph Analytics -->
                    <div class="col-lg-4 col-md-6 col-12 mt-4 pt-2 home-proj-card" data-category="bigdata">
                        <div class="card border-0 work-container work-modern position-relative d-block overflow-hidden rounded shadow-sm bg-white h-100" style="transition: transform 0.3s ease, box-shadow 0.3s ease;">
                            <div class="card-body p-0 position-relative">
                                <div class="proj-thumb-wrapper position-relative overflow-hidden" style="background: #0f172a; aspect-ratio: 16/9;">
                                    <img src="images/portfolio/graph_analytics_thumb.svg" class="img-fluid w-100 h-100" alt="Big Data Yelp & Social Network Graph Mining" style="object-fit: cover;" referrerpolicy="no-referrer">
                                    <div class="proj-overlay position-absolute w-100 h-100 d-flex align-items-center justify-content-center" style="top:0; left:0; background: rgba(15,23,42,0.85); opacity: 0; transition: opacity 0.3s ease;">
                                        <div class="text-center p-3">
                                            <a href="https://github.com/iamharshverma/BigData-Yelp-Business-Data-and-Social-Network-Analysis" target="_blank" class="btn btn-sm btn-primary rounded-pill px-3 mr-2 mb-2"><i class="mdi mdi-github-face mr-1"></i> GitHub Repo</a>
                                            <a href="page-portfolio" class="btn btn-sm btn-outline-light rounded-pill px-3 mb-2"><i class="mdi mdi-information-outline mr-1"></i> Details</a>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-3">
                                    <div class="d-flex align-items-center justify-content-between mb-2">
                                        <span class="badge badge-danger px-2 py-1 font-weight-bold" style="font-size: 11px;">GRAPH AI • NETWORK MINING</span>
                                        <small class="text-muted"><i class="mdi mdi-graph-outline text-danger mr-1"></i> PageRank</small>
                                    </div>
                                    <h5 class="mb-2" style="font-size: 17px; line-height: 1.35;">
                                        <a href="https://github.com/iamharshverma/BigData-Yelp-Business-Data-and-Social-Network-Analysis" target="_blank" class="text-dark font-weight-bold proj-title-link">Yelp &amp; Social Graph Analytics</a>
                                    </h5>
                                    <p class="text-muted small mb-3" style="line-height: 1.5; min-height: 42px;">
                                        Graph mining, community detection algorithms, and PageRank influencer centrality analysis on large-scale social connectivity graphs.
                                    </p>
                                    <div class="d-flex flex-wrap mb-3" style="gap: 5px;">
                                        <span class="badge badge-light border text-muted">Graph Mining</span>
                                        <span class="badge badge-light border text-muted">PageRank</span>
                                        <span class="badge badge-light border text-muted">NetworkX</span>
                                        <span class="badge badge-light border text-muted">Community Modularity</span>
                                    </div>
                                    <div class="d-flex align-items-center justify-content-between pt-2 border-top">
                                        <a href="https://github.com/iamharshverma/BigData-Yelp-Business-Data-and-Social-Network-Analysis" target="_blank" class="text-primary font-weight-bold small d-inline-flex align-items-center">
                                            <i class="mdi mdi-github-face mr-1 font-16"></i> View Source Code <i class="mdi mdi-chevron-right ml-1"></i>
                                        </a>
                                        <span class="text-muted small"><i class="mdi mdi-star text-warning"></i> Open Source</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div><!--end col-->

                    <!-- Project 7: CNN Classifier -->
                    <div class="col-lg-4 col-md-6 col-12 mt-4 pt-2 home-proj-card" data-category="vision">
                        <div class="card border-0 work-container work-modern position-relative d-block overflow-hidden rounded shadow-sm bg-white h-100" style="transition: transform 0.3s ease, box-shadow 0.3s ease;">
                            <div class="card-body p-0 position-relative">
                                <div class="proj-thumb-wrapper position-relative overflow-hidden" style="background: #0f172a; aspect-ratio: 16/9;">
                                    <img src="images/portfolio/cnn_vision_thumb.svg" class="img-fluid w-100 h-100" alt="Deep Learning CNN MultiClass Image Classifier" style="object-fit: cover;" referrerpolicy="no-referrer">
                                    <div class="proj-overlay position-absolute w-100 h-100 d-flex align-items-center justify-content-center" style="top:0; left:0; background: rgba(15,23,42,0.85); opacity: 0; transition: opacity 0.3s ease;">
                                        <div class="text-center p-3">
                                            <a href="https://github.com/iamharshverma/Deep_Learning-CNN_MultiClass_ImageClassifier" target="_blank" class="btn btn-sm btn-primary rounded-pill px-3 mr-2 mb-2"><i class="mdi mdi-github-face mr-1"></i> GitHub Repo</a>
                                            <a href="page-portfolio" class="btn btn-sm btn-outline-light rounded-pill px-3 mb-2"><i class="mdi mdi-information-outline mr-1"></i> Details</a>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-3">
                                    <div class="d-flex align-items-center justify-content-between mb-2">
                                        <span class="badge badge-info px-2 py-1 font-weight-bold" style="font-size: 11px;">COMPUTER VISION • PYTORCH</span>
                                        <small class="text-muted"><i class="mdi mdi-eye-check text-info mr-1"></i> 99.2% Acc</small>
                                    </div>
                                    <h5 class="mb-2" style="font-size: 17px; line-height: 1.35;">
                                        <a href="https://github.com/iamharshverma/Deep_Learning-CNN_MultiClass_ImageClassifier" target="_blank" class="text-dark font-weight-bold proj-title-link">Deep CNN Multi-Class Classifier</a>
                                    </h5>
                                    <p class="text-muted small mb-3" style="line-height: 1.5; min-height: 42px;">
                                        Deep convolutional residual neural network architecture with spatial dropout and batch normalization for multi-class image recognition.
                                    </p>
                                    <div class="d-flex flex-wrap mb-3" style="gap: 5px;">
                                        <span class="badge badge-light border text-muted">PyTorch</span>
                                        <span class="badge badge-light border text-muted">Conv2D</span>
                                        <span class="badge badge-light border text-muted">ResNet</span>
                                        <span class="badge badge-light border text-muted">Spatial Softmax</span>
                                    </div>
                                    <div class="d-flex align-items-center justify-content-between pt-2 border-top">
                                        <a href="https://github.com/iamharshverma/Deep_Learning-CNN_MultiClass_ImageClassifier" target="_blank" class="text-primary font-weight-bold small d-inline-flex align-items-center">
                                            <i class="mdi mdi-github-face mr-1 font-16"></i> View Source Code <i class="mdi mdi-chevron-right ml-1"></i>
                                        </a>
                                        <span class="text-muted small"><i class="mdi mdi-star text-warning"></i> Open Source</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div><!--end col-->

                    <!-- Project 8: Lock-Free Hash Table -->
                    <div class="col-lg-4 col-md-6 col-12 mt-4 pt-2 home-proj-card" data-category="security">
                        <div class="card border-0 work-container work-modern position-relative d-block overflow-hidden rounded shadow-sm bg-white h-100" style="transition: transform 0.3s ease, box-shadow 0.3s ease;">
                            <div class="card-body p-0 position-relative">
                                <div class="proj-thumb-wrapper position-relative overflow-hidden" style="background: #0f172a; aspect-ratio: 16/9;">
                                    <img src="images/portfolio/lockfree_hashtable_thumb.svg" class="img-fluid w-100 h-100" alt="Lock-Free Concurrent Hash Table" style="object-fit: cover;" referrerpolicy="no-referrer">
                                    <div class="proj-overlay position-absolute w-100 h-100 d-flex align-items-center justify-content-center" style="top:0; left:0; background: rgba(15,23,42,0.85); opacity: 0; transition: opacity 0.3s ease;">
                                        <div class="text-center p-3">
                                            <a href="https://github.com/iamharshverma/JavaHashTableCustomImplementation" target="_blank" class="btn btn-sm btn-primary rounded-pill px-3 mr-2 mb-2"><i class="mdi mdi-github-face mr-1"></i> GitHub Repo</a>
                                            <a href="page-portfolio" class="btn btn-sm btn-outline-light rounded-pill px-3 mb-2"><i class="mdi mdi-information-outline mr-1"></i> Details</a>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-3">
                                    <div class="d-flex align-items-center justify-content-between mb-2">
                                        <span class="badge badge-primary px-2 py-1 font-weight-bold" style="font-size: 11px;">SYSTEMS • CONCURRENCY</span>
                                        <small class="text-muted"><i class="mdi mdi-memory text-primary mr-1"></i> Atomic CAS</small>
                                    </div>
                                    <h5 class="mb-2" style="font-size: 17px; line-height: 1.35;">
                                        <a href="https://github.com/iamharshverma/JavaHashTableCustomImplementation" target="_blank" class="text-dark font-weight-bold proj-title-link">Lock-Free Concurrent Hash Table</a>
                                    </h5>
                                    <p class="text-muted small mb-3" style="line-height: 1.5; min-height: 42px;">
                                        Custom lock-free concurrent hash map leveraging atomic Compare-And-Swap (CAS) operations to eliminate thread contention locks.
                                    </p>
                                    <div class="d-flex flex-wrap mb-3" style="gap: 5px;">
                                        <span class="badge badge-light border text-muted">Atomic CAS</span>
                                        <span class="badge badge-light border text-muted">Lock-Free</span>
                                        <span class="badge badge-light border text-muted">Java JMM</span>
                                        <span class="badge badge-light border text-muted">Robin Hood Hashing</span>
                                    </div>
                                    <div class="d-flex align-items-center justify-content-between pt-2 border-top">
                                        <a href="https://github.com/iamharshverma/JavaHashTableCustomImplementation" target="_blank" class="text-primary font-weight-bold small d-inline-flex align-items-center">
                                            <i class="mdi mdi-github-face mr-1 font-16"></i> View Source Code <i class="mdi mdi-chevron-right ml-1"></i>
                                        </a>
                                        <span class="text-muted small"><i class="mdi mdi-star text-warning"></i> Open Source</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div><!--end col-->

                    <!-- Project 9: Microservice Gateway -->
                    <div class="col-lg-4 col-md-6 col-12 mt-4 pt-2 home-proj-card" data-category="security">
                        <div class="card border-0 work-container work-modern position-relative d-block overflow-hidden rounded shadow-sm bg-white h-100" style="transition: transform 0.3s ease, box-shadow 0.3s ease;">
                            <div class="card-body p-0 position-relative">
                                <div class="proj-thumb-wrapper position-relative overflow-hidden" style="background: #0f172a; aspect-ratio: 16/9;">
                                    <img src="images/portfolio/microservice_gateway_thumb.svg" class="img-fluid w-100 h-100" alt="WordDoc Frequency Microservice API" style="object-fit: cover;" referrerpolicy="no-referrer">
                                    <div class="proj-overlay position-absolute w-100 h-100 d-flex align-items-center justify-content-center" style="top:0; left:0; background: rgba(15,23,42,0.85); opacity: 0; transition: opacity 0.3s ease;">
                                        <div class="text-center p-3">
                                            <a href="https://github.com/iamharshverma/APIMicroServiceForWordDocFrequencyCount" target="_blank" class="btn btn-sm btn-primary rounded-pill px-3 mr-2 mb-2"><i class="mdi mdi-github-face mr-1"></i> GitHub Repo</a>
                                            <a href="page-portfolio" class="btn btn-sm btn-outline-light rounded-pill px-3 mb-2"><i class="mdi mdi-information-outline mr-1"></i> Details</a>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-3">
                                    <div class="d-flex align-items-center justify-content-between mb-2">
                                        <span class="badge badge-purple px-2 py-1 font-weight-bold text-white" style="font-size: 11px; background: #4f46e5;">BACKEND • HIGH THROUGHPUT</span>
                                        <small class="text-muted"><i class="mdi mdi-lightning-bolt text-warning mr-1"></i> Sub-ms</small>
                                    </div>
                                    <h5 class="mb-2" style="font-size: 17px; line-height: 1.35;">
                                        <a href="https://github.com/iamharshverma/APIMicroServiceForWordDocFrequencyCount" target="_blank" class="text-dark font-weight-bold proj-title-link">WordDoc Frequency Microservice</a>
                                    </h5>
                                    <p class="text-muted small mb-3" style="line-height: 1.5; min-height: 42px;">
                                        High-concurrency microservice engine with non-blocking IO worker pool for sub-millisecond document token frequency parsing.
                                    </p>
                                    <div class="d-flex flex-wrap mb-3" style="gap: 5px;">
                                        <span class="badge badge-light border text-muted">Microservices</span>
                                        <span class="badge badge-light border text-muted">REST API</span>
                                        <span class="badge badge-light border text-muted">Non-Blocking IO</span>
                                        <span class="badge badge-light border text-muted">Lexer Engine</span>
                                    </div>
                                    <div class="d-flex align-items-center justify-content-between pt-2 border-top">
                                        <a href="https://github.com/iamharshverma/APIMicroServiceForWordDocFrequencyCount" target="_blank" class="text-primary font-weight-bold small d-inline-flex align-items-center">
                                            <i class="mdi mdi-github-face mr-1 font-16"></i> View Source Code <i class="mdi mdi-chevron-right ml-1"></i>
                                        </a>
                                        <span class="text-muted small"><i class="mdi mdi-star text-warning"></i> Open Source</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div><!--end col-->

                    <!-- Project 10: Hadoop Social MapReduce -->
                    <div class="col-lg-4 col-md-6 col-12 mt-4 pt-2 home-proj-card" data-category="bigdata">
                        <div class="card border-0 work-container work-modern position-relative d-block overflow-hidden rounded shadow-sm bg-white h-100" style="transition: transform 0.3s ease, box-shadow 0.3s ease;">
                            <div class="card-body p-0 position-relative">
                                <div class="proj-thumb-wrapper position-relative overflow-hidden" style="background: #0f172a; aspect-ratio: 16/9;">
                                    <img src="images/portfolio/hadoop_cluster_thumb.svg" class="img-fluid w-100 h-100" alt="BigData Hadoop Social Network" style="object-fit: cover;" referrerpolicy="no-referrer">
                                    <div class="proj-overlay position-absolute w-100 h-100 d-flex align-items-center justify-content-center" style="top:0; left:0; background: rgba(15,23,42,0.85); opacity: 0; transition: opacity 0.3s ease;">
                                        <div class="text-center p-3">
                                            <a href="https://github.com/iamharshverma/BigData-Hadoop_SocialNetwork" target="_blank" class="btn btn-sm btn-primary rounded-pill px-3 mr-2 mb-2"><i class="mdi mdi-github-face mr-1"></i> GitHub Repo</a>
                                            <a href="page-portfolio" class="btn btn-sm btn-outline-light rounded-pill px-3 mb-2"><i class="mdi mdi-information-outline mr-1"></i> Details</a>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-3">
                                    <div class="d-flex align-items-center justify-content-between mb-2">
                                        <span class="badge badge-warning px-2 py-1 font-weight-bold text-dark" style="font-size: 11px;">DISTRIBUTED • HDFS CLUSTER</span>
                                        <small class="text-muted"><i class="mdi mdi-server text-success mr-1"></i> MapReduce</small>
                                    </div>
                                    <h5 class="mb-2" style="font-size: 17px; line-height: 1.35;">
                                        <a href="https://github.com/iamharshverma/BigData-Hadoop_SocialNetwork" target="_blank" class="text-dark font-weight-bold proj-title-link">Hadoop Distributed Social Network</a>
                                    </h5>
                                    <p class="text-muted small mb-3" style="line-height: 1.5; min-height: 42px;">
                                        MapReduce distributed computation pipeline processing multi-terabyte social network interaction graphs on HDFS cluster nodes.
                                    </p>
                                    <div class="d-flex flex-wrap mb-3" style="gap: 5px;">
                                        <span class="badge badge-light border text-muted">Hadoop</span>
                                        <span class="badge badge-light border text-muted">MapReduce</span>
                                        <span class="badge badge-light border text-muted">HDFS</span>
                                        <span class="badge badge-light border text-muted">Graph Sharding</span>
                                    </div>
                                    <div class="d-flex align-items-center justify-content-between pt-2 border-top">
                                        <a href="https://github.com/iamharshverma/BigData-Hadoop_SocialNetwork" target="_blank" class="text-primary font-weight-bold small d-inline-flex align-items-center">
                                            <i class="mdi mdi-github-face mr-1 font-16"></i> View Source Code <i class="mdi mdi-chevron-right ml-1"></i>
                                        </a>
                                        <span class="text-muted small"><i class="mdi mdi-star text-warning"></i> Open Source</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div><!--end col-->

                    <!-- Project 11: IR Tokenizer & Stemmer -->
                    <div class="col-lg-4 col-md-6 col-12 mt-4 pt-2 home-proj-card" data-category="nlp">
                        <div class="card border-0 work-container work-modern position-relative d-block overflow-hidden rounded shadow-sm bg-white h-100" style="transition: transform 0.3s ease, box-shadow 0.3s ease;">
                            <div class="card-body p-0 position-relative">
                                <div class="proj-thumb-wrapper position-relative overflow-hidden" style="background: #0f172a; aspect-ratio: 16/9;">
                                    <img src="images/portfolio/ir_tokenizer_thumb.svg" class="img-fluid w-100 h-100" alt="Tokanize and Stemming" style="object-fit: cover;" referrerpolicy="no-referrer">
                                    <div class="proj-overlay position-absolute w-100 h-100 d-flex align-items-center justify-content-center" style="top:0; left:0; background: rgba(15,23,42,0.85); opacity: 0; transition: opacity 0.3s ease;">
                                        <div class="text-center p-3">
                                            <a href="https://github.com/iamharshverma/TokanizeAndStemming" target="_blank" class="btn btn-sm btn-primary rounded-pill px-3 mr-2 mb-2"><i class="mdi mdi-github-face mr-1"></i> GitHub Repo</a>
                                            <a href="page-portfolio" class="btn btn-sm btn-outline-light rounded-pill px-3 mb-2"><i class="mdi mdi-information-outline mr-1"></i> Details</a>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-3">
                                    <div class="d-flex align-items-center justify-content-between mb-2">
                                        <span class="badge badge-purple px-2 py-1 font-weight-bold text-white" style="font-size: 11px; background: #7e22ce;">NLP • SEARCH INDEXING</span>
                                        <small class="text-muted"><i class="mdi mdi-text-search text-info mr-1"></i> Lexer DFA</small>
                                    </div>
                                    <h5 class="mb-2" style="font-size: 17px; line-height: 1.35;">
                                        <a href="https://github.com/iamharshverma/TokanizeAndStemming" target="_blank" class="text-dark font-weight-bold proj-title-link">High-Speed Tokenizer &amp; Stemmer</a>
                                    </h5>
                                    <p class="text-muted small mb-3" style="line-height: 1.5; min-height: 42px;">
                                        Deterministic finite-state automaton (DFA) lexical analyzer and streaming Porter stemming engine for search indexing.
                                    </p>
                                    <div class="d-flex flex-wrap mb-3" style="gap: 5px;">
                                        <span class="badge badge-light border text-muted">Lexical DFA</span>
                                        <span class="badge badge-light border text-muted">Porter Stemming</span>
                                        <span class="badge badge-light border text-muted">Inverted Index</span>
                                        <span class="badge badge-light border text-muted">NLP IR</span>
                                    </div>
                                    <div class="d-flex align-items-center justify-content-between pt-2 border-top">
                                        <a href="https://github.com/iamharshverma/TokanizeAndStemming" target="_blank" class="text-primary font-weight-bold small d-inline-flex align-items-center">
                                            <i class="mdi mdi-github-face mr-1 font-16"></i> View Source Code <i class="mdi mdi-chevron-right ml-1"></i>
                                        </a>
                                        <span class="text-muted small"><i class="mdi mdi-star text-warning"></i> Open Source</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div><!--end col-->

                    <!-- Project 12: Skip Lists Index -->
                    <div class="col-lg-4 col-md-6 col-12 mt-4 pt-2 home-proj-card" data-category="security">
                        <div class="card border-0 work-container work-modern position-relative d-block overflow-hidden rounded shadow-sm bg-white h-100" style="transition: transform 0.3s ease, box-shadow 0.3s ease;">
                            <div class="card-body p-0 position-relative">
                                <div class="proj-thumb-wrapper position-relative overflow-hidden" style="background: #0f172a; aspect-ratio: 16/9;">
                                    <img src="images/portfolio/skiplist_index_thumb.svg" class="img-fluid w-100 h-100" alt="Skip-List Implementation" style="object-fit: cover;" referrerpolicy="no-referrer">
                                    <div class="proj-overlay position-absolute w-100 h-100 d-flex align-items-center justify-content-center" style="top:0; left:0; background: rgba(15,23,42,0.85); opacity: 0; transition: opacity 0.3s ease;">
                                        <div class="text-center p-3">
                                            <a href="https://github.com/iamharshverma/SkipLists" target="_blank" class="btn btn-sm btn-primary rounded-pill px-3 mr-2 mb-2"><i class="mdi mdi-github-face mr-1"></i> GitHub Repo</a>
                                            <a href="page-portfolio" class="btn btn-sm btn-outline-light rounded-pill px-3 mb-2"><i class="mdi mdi-information-outline mr-1"></i> Details</a>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-3">
                                    <div class="d-flex align-items-center justify-content-between mb-2">
                                        <span class="badge badge-info px-2 py-1 font-weight-bold" style="font-size: 11px;">ALGORITHMS • DATA STRUCTURES</span>
                                        <small class="text-muted"><i class="mdi mdi-speedometer text-success mr-1"></i> O(log N)</small>
                                    </div>
                                    <h5 class="mb-2" style="font-size: 17px; line-height: 1.35;">
                                        <a href="https://github.com/iamharshverma/SkipLists" target="_blank" class="text-dark font-weight-bold proj-title-link">Probabilistic Skip-List Index</a>
                                    </h5>
                                    <p class="text-muted small mb-3" style="line-height: 1.5; min-height: 42px;">
                                        Concurrent probabilistic multi-tiered skip-list data structure providing verified O(log N) search and insert complexity.
                                    </p>
                                    <div class="d-flex flex-wrap mb-3" style="gap: 5px;">
                                        <span class="badge badge-light border text-muted">Skip Lists</span>
                                        <span class="badge badge-light border text-muted">O(log N)</span>
                                        <span class="badge badge-light border text-muted">Concurrency</span>
                                        <span class="badge badge-light border text-muted">Data Structures</span>
                                    </div>
                                    <div class="d-flex align-items-center justify-content-between pt-2 border-top">
                                        <a href="https://github.com/iamharshverma/SkipLists" target="_blank" class="text-primary font-weight-bold small d-inline-flex align-items-center">
                                            <i class="mdi mdi-github-face mr-1 font-16"></i> View Source Code <i class="mdi mdi-chevron-right ml-1"></i>
                                        </a>
                                        <span class="text-muted small"><i class="mdi mdi-star text-warning"></i> Open Source</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div><!--end col-->

                </div><!--end row-->

                <!-- Call to action row -->
                <div class="row mt-5 pt-3">
                    <div class="col-12 text-center">
                        <div class="p-4 rounded border bg-white shadow-sm d-inline-block" style="max-width: 800px;">
                            <h5 class="mb-2 font-weight-bold text-dark">Explore Complete Engineering &amp; Research Portfolio</h5>
                            <p class="text-muted small mb-3">View all open-source libraries, benchmarks, and research implementations across AI security and distributed systems.</p>
                            <div class="d-flex flex-wrap justify-content-center align-items-center" style="gap: 12px;">
                                <a href="page-portfolio" class="btn btn-primary rounded-pill px-4 py-2 font-weight-bold shadow-sm">
                                    <i class="mdi mdi-folder-multiple-outline mr-1"></i> Browse Complete Portfolio (25+) <i class="mdi mdi-arrow-right ml-1"></i>
                                </a>
                                <a href="page-publications" class="btn btn-outline-primary rounded-pill px-4 py-2 font-weight-bold">
                                    <i class="mdi mdi-book-open-page-variant mr-1"></i> Scientific Papers &amp; Patents
                                </a>
                                <a href="https://github.com/iamharshverma" target="_blank" class="btn btn-dark rounded-pill px-4 py-2 font-weight-bold">
                                    <i class="mdi mdi-github-face mr-1"></i> GitHub Profile
                                </a>
                            </div>
                        </div>
                    </div><!--end col-->
                </div><!--end row-->

            </div>
            <!-- End container -->
        </section>
        <!-- Projects End -->'''

# Build Contact HTML
contact_html = '''        <!-- Contact Start -->
        <section class="section bg-white" id="contact" style="position: relative;">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-12 text-center">
                        <div class="container-title text-center mb-4 pb-2">
                            <div class="titles">
                                <span class="badge badge-primary px-3 py-2 text-uppercase mb-2 font-weight-bold" style="letter-spacing: 1px; font-size: 11px;">
                                    <i class="mdi mdi-email-send-outline mr-1"></i> Direct Inquiries &amp; Speaking
                                </span>
                                <h2 class="title text-capitalize mb-3">Get in Touch with Harsh</h2>
                                <p class="para-desc-600 text-muted mb-0 mx-auto" style="max-width: 700px; font-size: 15.5px; line-height: 1.6;">
                                    Have an AI security advisory, research collaboration, keynote invitation, or startup advisory query? Reach out directly using the form below or direct channels.
                                </p>
                            </div>
                        </div>
                    </div><!--end col-->
                </div><!--end row-->

                <div class="row">
                    <!-- Direct Contact Channels Column (Left) -->
                    <div class="col-lg-5 col-md-6 col-12 mt-4 pt-2">
                        <div class="contact-card-sidebar p-4 rounded shadow-sm border bg-light h-100">
                            <h4 class="font-weight-bold text-dark mb-3">Direct Contact Channels</h4>
                            <p class="text-muted small mb-4">
                                Direct inquiries are monitored daily. For high-priority conference keynotes or enterprise advisory, please specify your organization in the inquiry.
                            </p>

                            <!-- Direct Email & LinkedIn Profile Card (Merged) -->
                            <div class="contact-channel-item d-flex align-items-start mb-3 p-3 bg-white rounded border">
                                <div class="contact-icon-box icon-box-primary">
                                    <i class="mdi mdi-contact-mail"></i>
                                </div>
                                <div class="flex-grow-1 min-w-0">
                                    <h6 class="mb-1 font-weight-bold text-dark">Direct Email &amp; LinkedIn</h6>
                                    <p class="text-muted small mb-2">Direct mailbox with 24-hour response SLA &amp; executive messaging</p>
                                    <div class="d-flex flex-column" style="gap: 8px;">
                                        <div class="d-flex align-items-center">
                                            <i class="mdi mdi-email-outline text-primary mr-2" style="font-size: 16px; line-height: 1;"></i>
                                            <a href="mailto:harshverma59@gmail.com" class="text-primary font-weight-bold small text-truncate">harshverma59@gmail.com</a>
                                        </div>
                                        <div class="d-flex align-items-center">
                                            <i class="mdi mdi-linkedin text-linkedin mr-2" style="font-size: 16px; line-height: 1;"></i>
                                            <a href="https://www.linkedin.com/in/harshverma59/" target="_blank" rel="noopener noreferrer" class="text-linkedin font-weight-bold small d-inline-flex align-items-center text-truncate">
                                                linkedin.com/in/harshverma59 <i class="mdi mdi-open-in-new ml-1" style="font-size: 13px;"></i>
                                            </a>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- Location Card -->
                            <div class="contact-channel-item d-flex align-items-start mb-3 p-3 bg-white rounded border">
                                <div class="contact-icon-box icon-box-success">
                                    <i class="mdi mdi-map-marker-outline"></i>
                                </div>
                                <div class="flex-grow-1 min-w-0">
                                    <h6 class="mb-1 font-weight-bold text-dark">Location &amp; Hub</h6>
                                    <p class="text-muted small mb-2">San Francisco Bay Area &bull; Silicon Valley, California, USA</p>
                                    <div class="d-flex flex-wrap align-items-center" style="gap: 8px;">
                                        <a href="https://maps.google.com/?q=San+Francisco+Bay+Area+California" target="_blank" rel="noopener noreferrer" class="text-success font-weight-bold small d-inline-flex align-items-center">
                                            View on Google Maps <i class="mdi mdi-open-in-new ml-1"></i>
                                        </a>
                                    </div>
                                </div>
                            </div>

                            <!-- Speaking & Advisory Card -->
                            <div class="contact-channel-item d-flex align-items-start mb-3 p-3 bg-white rounded border">
                                <div class="contact-icon-box icon-box-purple">
                                    <i class="mdi mdi-microphone-outline"></i>
                                </div>
                                <div class="flex-grow-1 min-w-0">
                                    <h6 class="mb-1 font-weight-bold text-dark">Advisory &amp; Engagements</h6>
                                    <p class="text-muted small mb-0">
                                        Forbes Tech Council &bull; UC Berkeley SkyDeck &bull; IEEE Senior Member &bull; Keynote Panels
                                    </p>
                                </div>
                            </div>

                            <!-- Quick Socials -->
                            <div class="pt-3 border-top mt-1">
                                <span class="text-muted small font-weight-bold d-block mb-2">Connect via Professional Networks:</span>
                                <div class="d-flex flex-wrap" style="gap: 8px;">
                                    <a href="https://www.linkedin.com/in/harshverma59/" target="_blank" class="btn btn-sm btn-outline-primary contact-network-pill rounded-pill px-3 font-weight-bold">
                                        <i class="mdi mdi-linkedin mr-1"></i> LinkedIn
                                    </a>
                                    <a href="https://scholar.google.com/citations?hl=en&user=zSt9oRMAAAAJ" target="_blank" class="btn btn-sm btn-outline-info contact-network-pill rounded-pill px-3 font-weight-bold">
                                        <i class="mdi mdi-school mr-1"></i> Scholar
                                    </a>
                                    <a href="https://github.com/iamharshverma" target="_blank" class="btn btn-sm btn-outline-dark contact-network-pill rounded-pill px-3 font-weight-bold">
                                        <i class="mdi mdi-github-face mr-1"></i> GitHub
                                    </a>
                                    <a href="https://twitter.com/harshverma59" target="_blank" class="btn btn-sm btn-outline-secondary contact-network-pill rounded-pill px-3 font-weight-bold">
                                        <i class="mdi mdi-twitter mr-1"></i> Twitter
                                    </a>
                                </div>
                            </div>

                        </div>
                    </div><!--end col-->

                    <!-- Interactive Contact Form Column (Right) -->
                    <div class="col-lg-7 col-md-6 col-12 mt-4 pt-2">
                        <div class="contact-form-wrapper p-4 p-md-5 rounded shadow-sm border bg-white">
                            <div class="d-flex flex-wrap align-items-center justify-content-between mb-3">
                                <div>
                                    <h4 class="font-weight-bold text-dark mb-1">Send a Message</h4>
                                    <p class="text-muted small mb-0">Direct route to <b>harshverma59@gmail.com</b></p>
                                </div>
                                <div>
                                    <button type="button" class="btn btn-sm btn-outline-secondary rounded-pill px-3" onclick="fillTestContactForm(event)" title="Fill with sample inquiry to test email pipeline">
                                        <i class="mdi mdi-lightning-bolt-outline mr-1 text-warning"></i> Auto-fill Test Inquiry
                                    </button>
                                </div>
                            </div>

                            <!-- Topic selector pills -->
                            <div class="mb-3">
                                <label class="text-muted small font-weight-bold mb-2 d-block">Select Inquiry Subject / Topic:</label>
                                <div class="d-flex flex-wrap" style="gap: 6px;">
                                    <button type="button" class="btn btn-xs contact-topic-pill border rounded-pill px-3 py-1 font-weight-bold active" data-topic="Agentic AI & Security Advisory">
                                        🤖 Agentic AI &amp; Security
                                    </button>
                                    <button type="button" class="btn btn-xs contact-topic-pill border rounded-pill px-3 py-1 font-weight-bold" data-topic="Keynote / Conference Speaking Invitation">
                                        🎙️ Keynote &amp; Speaking
                                    </button>
                                    <button type="button" class="btn btn-xs contact-topic-pill border rounded-pill px-3 py-1 font-weight-bold" data-topic="UC Berkeley SkyDeck / Startup Advisory">
                                        🏛️ SkyDeck Advisory
                                    </button>
                                    <button type="button" class="btn btn-xs contact-topic-pill border rounded-pill px-3 py-1 font-weight-bold" data-topic="Research Collaboration & Patents">
                                        🔬 Research &amp; Papers
                                    </button>
                                    <button type="button" class="btn btn-xs contact-topic-pill border rounded-pill px-3 py-1 font-weight-bold" data-topic="General Professional Connect">
                                        ☕ General Connect
                                    </button>
                                </div>
                            </div>

                            <!-- Feedback container -->
                            <div id="message"></div>

                            <!-- Form -->
                            <form method="post" action="/api/contact" name="contact-form" id="contact-form">
                                <div class="row">
                                    <div class="col-md-6">
                                        <div class="form-group mb-3">
                                            <label for="name" class="font-weight-bold text-dark small mb-1">Your Full Name <span class="text-danger">*</span></label>
                                            <div class="position-relative">
                                                <input name="name" id="name" type="text" class="form-control rounded" placeholder="e.g. Dr. Alex Morgan" required style="padding-left: 14px; height: 46px;">
                                            </div>
                                        </div>
                                    </div><!--end col-->

                                    <div class="col-md-6">
                                        <div class="form-group mb-3">
                                            <label for="email" class="font-weight-bold text-dark small mb-1">Your Email Address <span class="text-danger">*</span></label>
                                            <div class="position-relative">
                                                <input name="email" id="email" type="email" class="form-control rounded" placeholder="e.g. alex@organization.com" required style="padding-left: 14px; height: 46px;">
                                            </div>
                                        </div> 
                                    </div><!--end col-->

                                    <div class="col-md-6">
                                        <div class="form-group mb-3">
                                            <label for="organization" class="font-weight-bold text-dark small mb-1">Organization / Company <span class="text-muted font-weight-normal">(Optional)</span></label>
                                            <input name="organization" id="organization" type="text" class="form-control rounded" placeholder="e.g. Stanford University / Tech Corp" style="height: 46px;">
                                        </div>
                                    </div><!--end col-->

                                    <div class="col-md-6">
                                        <div class="form-group mb-3">
                                            <label for="subject" class="font-weight-bold text-dark small mb-1">Subject / Focus <span class="text-danger">*</span></label>
                                            <input name="subject" id="subject" class="form-control rounded" placeholder="e.g. Agentic AI & Security Advisory" value="Agentic AI & Security Advisory" required style="height: 46px;">
                                        </div>                                                                               
                                    </div><!--end col-->

                                    <div class="col-12">
                                        <div class="form-group mb-3">
                                            <label for="comments" class="font-weight-bold text-dark small mb-1">Your Detailed Message <span class="text-danger">*</span></label>
                                            <textarea name="comments" id="comments" rows="5" class="form-control rounded" placeholder="Please share details about your inquiry, event date, research collaboration, or agenda..." required style="resize: vertical;"></textarea>
                                        </div>
                                    </div><!--end col-->
                                </div><!--end row-->

                                <div class="row align-items-center">
                                    <div class="col-md-7 mb-2 mb-md-0">
                                        <div class="d-flex align-items-center text-muted small">
                                            <i class="mdi mdi-shield-check text-success font-18 mr-1"></i>
                                            <span>Target recipient: <b>harshverma59@gmail.com</b></span>
                                        </div>
                                    </div>
                                    <div class="col-md-5 text-md-right">
                                        <button type="submit" id="submit" name="send" class="btn btn-primary rounded-pill px-4 py-2 font-weight-bold shadow-sm w-100 w-md-auto">
                                            <i class="mdi mdi-send mr-1"></i> Send Message
                                        </button> 
                                    </div><!--end col-->
                                </div><!--end row-->
                            </form><!--end form-->
                        </div><!--end custom-form-->
                    </div><!--end col-->
                </div><!--end row-->
            </div><!--end container-->
        </section><!--end section-->
        <!-- Contact End -->'''

# Replace Projects Section
proj_pattern = re.compile(r'<!-- Projects/Work Start -->.*?<!-- Projects End -->', re.DOTALL)
if proj_pattern.search(html):
    html = proj_pattern.sub(projects_html, html)
    print("Replaced Projects Section!")
else:
    print("Warning: Projects section pattern not found!")

# Replace Contact Section
contact_pattern = re.compile(r'<!-- Contact Start -->.*?<!-- Contact End -->', re.DOTALL)
if contact_pattern.search(html):
    html = contact_pattern.sub(contact_html, html)
    print("Replaced Contact Section!")
else:
    print("Warning: Contact section pattern not found!")

# Add custom filtering script if not present
filter_script = '''
            function filterHomeProjects(category, btn) {
                var buttons = document.querySelectorAll('.home-proj-filter-btn');
                buttons.forEach(function(b) { b.classList.remove('active'); });
                if (btn) btn.classList.add('active');

                var cards = document.querySelectorAll('.home-proj-card');
                cards.forEach(function(card) {
                    var cat = card.getAttribute('data-category');
                    if (category === 'all' || cat === category) {
                        card.style.display = 'block';
                    } else {
                        card.style.display = 'none';
                    }
                });
            }
'''

if 'function filterHomeProjects' not in html:
    html = html.replace('function filterHomeAwards', filter_script + '\n            function filterHomeAwards')
    print("Added filterHomeProjects script!")

# Add custom CSS styles for projects & contact if not present
custom_styles = '''
        /* Custom Styles for Projects & Contact Enhancement */
        .home-proj-filter-btn {
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            color: #475569;
            transition: all 0.2s ease;
        }
        .home-proj-filter-btn:hover, .home-proj-filter-btn.active {
            background: #2563eb !important;
            border-color: #2563eb !important;
            color: #ffffff !important;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25);
        }
        .home-proj-card:hover .card {
            transform: translateY(-6px);
            box-shadow: 0 16px 32px rgba(0, 0, 0, 0.08) !important;
        }
        .home-proj-card:hover .proj-overlay {
            opacity: 1 !important;
        }
        .proj-title-link:hover {
            color: #2563eb !important;
            text-decoration: underline;
        }
        .contact-topic-pill {
            background: #f8fafc;
            color: #475569;
            border-color: #cbd5e1 !important;
            font-size: 12px;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .contact-topic-pill:hover, .contact-topic-pill.active {
            background: #1e293b !important;
            color: #ffffff !important;
            border-color: #1e293b !important;
        }
        .dark-mode .home-proj-card .card {
            background: #1e293b !important;
        }
        .dark-mode .home-proj-card .proj-title-link {
            color: #f8fafc !important;
        }
        .dark-mode .contact-card-sidebar,
        .dark-mode .contact-form-wrapper {
            background: #1e293b !important;
            border-color: #334155 !important;
        }
        .dark-mode .contact-card-sidebar .bg-white {
            background: #0f172a !important;
            border-color: #334155 !important;
        }
'''

if 'Custom Styles for Projects & Contact Enhancement' not in html:
    html = html.replace('</head>', '<style>' + custom_styles + '</style>\n    </head>')
    print("Added custom CSS styles in head!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully updated index.html with enhanced Projects and Contact sections!")
