import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

clean_projects_section = '''<!-- Projects/Work Start -->
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
                        <div class="card border-0 custom-project-card position-relative d-block overflow-hidden rounded-lg shadow-sm bg-white h-100">
                            <div class="card-body p-0 position-relative">
                                <div class="proj-thumb-wrapper position-relative overflow-hidden" style="background: #0b0f19; height: 215px; width: 100%; display: block;">
                                    <img src="images/portfolio/agentic_security_thumb.svg" class="proj-thumb-img" alt="Agentic Security Guardrails" width="640" height="360" style="width: 100%; height: 215px; object-fit: cover; display: block;">
                                    <div class="proj-overlay position-absolute w-100 h-100 d-flex align-items-center justify-content-center" style="top:0; left:0; background: rgba(11,15,25,0.85);">
                                        <div class="text-center p-3">
                                            <a href="https://github.com/iamharshverma" target="_blank" class="btn btn-sm btn-primary rounded-pill px-3 mr-2 mb-2 font-weight-bold"><i class="mdi mdi-github-face mr-1"></i> GitHub Repo</a>
                                            <a href="page-portfolio" class="btn btn-sm btn-outline-light rounded-pill px-3 mb-2 font-weight-bold"><i class="mdi mdi-information-outline mr-1"></i> Details</a>
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
                        <div class="card border-0 custom-project-card position-relative d-block overflow-hidden rounded-lg shadow-sm bg-white h-100">
                            <div class="card-body p-0 position-relative">
                                <div class="proj-thumb-wrapper position-relative overflow-hidden" style="background: #0b0f19; height: 215px; width: 100%; display: block;">
                                    <img src="images/portfolio/spark_streaming_thumb.svg" class="proj-thumb-img" alt="PySpark Streaming MultiNews Classification" width="640" height="360" style="width: 100%; height: 215px; object-fit: cover; display: block;">
                                    <div class="proj-overlay position-absolute w-100 h-100 d-flex align-items-center justify-content-center" style="top:0; left:0; background: rgba(11,15,25,0.85);">
                                        <div class="text-center p-3">
                                            <a href="https://github.com/iamharshverma/PySparkStreaming-MultiNewsClassification" target="_blank" class="btn btn-sm btn-primary rounded-pill px-3 mr-2 mb-2 font-weight-bold"><i class="mdi mdi-github-face mr-1"></i> GitHub Repo</a>
                                            <a href="page-portfolio" class="btn btn-sm btn-outline-light rounded-pill px-3 mb-2 font-weight-bold"><i class="mdi mdi-information-outline mr-1"></i> Details</a>
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
                        <div class="card border-0 custom-project-card position-relative d-block overflow-hidden rounded-lg shadow-sm bg-white h-100">
                            <div class="card-body p-0 position-relative">
                                <div class="proj-thumb-wrapper position-relative overflow-hidden" style="background: #0b0f19; height: 215px; width: 100%; display: block;">
                                    <img src="images/portfolio/speech_ai_thumb.svg" class="proj-thumb-img" alt="NLP Automatic Speech Recognition" width="640" height="360" style="width: 100%; height: 215px; object-fit: cover; display: block;">
                                    <div class="proj-overlay position-absolute w-100 h-100 d-flex align-items-center justify-content-center" style="top:0; left:0; background: rgba(11,15,25,0.85);">
                                        <div class="text-center p-3">
                                            <a href="https://github.com/iamharshverma/NLP-Automatic-Speech-Recognization" target="_blank" class="btn btn-sm btn-primary rounded-pill px-3 mr-2 mb-2 font-weight-bold"><i class="mdi mdi-github-face mr-1"></i> GitHub Repo</a>
                                            <a href="page-portfolio" class="btn btn-sm btn-outline-light rounded-pill px-3 mb-2 font-weight-bold"><i class="mdi mdi-information-outline mr-1"></i> Details</a>
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
                        <div class="card border-0 custom-project-card position-relative d-block overflow-hidden rounded-lg shadow-sm bg-white h-100">
                            <div class="card-body p-0 position-relative">
                                <div class="proj-thumb-wrapper position-relative overflow-hidden" style="background: #0b0f19; height: 215px; width: 100%; display: block;">
                                    <img src="images/portfolio/bilstm_sentiment_thumb.svg" class="proj-thumb-img" alt="NLP BiLSTM Sentiment Analysis" width="640" height="360" style="width: 100%; height: 215px; object-fit: cover; display: block;">
                                    <div class="proj-overlay position-absolute w-100 h-100 d-flex align-items-center justify-content-center" style="top:0; left:0; background: rgba(11,15,25,0.85);">
                                        <div class="text-center p-3">
                                            <a href="https://github.com/iamharshverma/NLP-BiLSTM_SentimentAnalysis" target="_blank" class="btn btn-sm btn-primary rounded-pill px-3 mr-2 mb-2 font-weight-bold"><i class="mdi mdi-github-face mr-1"></i> GitHub Repo</a>
                                            <a href="page-portfolio" class="btn btn-sm btn-outline-light rounded-pill px-3 mb-2 font-weight-bold"><i class="mdi mdi-information-outline mr-1"></i> Details</a>
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
                        <div class="card border-0 custom-project-card position-relative d-block overflow-hidden rounded-lg shadow-sm bg-white h-100">
                            <div class="card-body p-0 position-relative">
                                <div class="proj-thumb-wrapper position-relative overflow-hidden" style="background: #0b0f19; height: 215px; width: 100%; display: block;">
                                    <img src="images/portfolio/cross_lingual_spark_thumb.svg" class="proj-thumb-img" alt="PySpark Cross-Language Article Deduplication" width="640" height="360" style="width: 100%; height: 215px; object-fit: cover; display: block;">
                                    <div class="proj-overlay position-absolute w-100 h-100 d-flex align-items-center justify-content-center" style="top:0; left:0; background: rgba(11,15,25,0.85);">
                                        <div class="text-center p-3">
                                            <a href="https://github.com/iamharshverma/PySpark-LargeScaleDataCollection_Preprocessing_Cross_language_Articles_Duplication_Detection" target="_blank" class="btn btn-sm btn-primary rounded-pill px-3 mr-2 mb-2 font-weight-bold"><i class="mdi mdi-github-face mr-1"></i> GitHub Repo</a>
                                            <a href="page-portfolio" class="btn btn-sm btn-outline-light rounded-pill px-3 mb-2 font-weight-bold"><i class="mdi mdi-information-outline mr-1"></i> Details</a>
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
                        <div class="card border-0 custom-project-card position-relative d-block overflow-hidden rounded-lg shadow-sm bg-white h-100">
                            <div class="card-body p-0 position-relative">
                                <div class="proj-thumb-wrapper position-relative overflow-hidden" style="background: #0b0f19; height: 215px; width: 100%; display: block;">
                                    <img src="images/portfolio/graph_analytics_thumb.svg" class="proj-thumb-img" alt="Big Data Yelp & Social Network Graph Mining" width="640" height="360" style="width: 100%; height: 215px; object-fit: cover; display: block;">
                                    <div class="proj-overlay position-absolute w-100 h-100 d-flex align-items-center justify-content-center" style="top:0; left:0; background: rgba(11,15,25,0.85);">
                                        <div class="text-center p-3">
                                            <a href="https://github.com/iamharshverma/BigData-Yelp-Business-Data-and-Social-Network-Analysis" target="_blank" class="btn btn-sm btn-primary rounded-pill px-3 mr-2 mb-2 font-weight-bold"><i class="mdi mdi-github-face mr-1"></i> GitHub Repo</a>
                                            <a href="page-portfolio" class="btn btn-sm btn-outline-light rounded-pill px-3 mb-2 font-weight-bold"><i class="mdi mdi-information-outline mr-1"></i> Details</a>
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
                        <div class="card border-0 custom-project-card position-relative d-block overflow-hidden rounded-lg shadow-sm bg-white h-100">
                            <div class="card-body p-0 position-relative">
                                <div class="proj-thumb-wrapper position-relative overflow-hidden" style="background: #0b0f19; height: 215px; width: 100%; display: block;">
                                    <img src="images/portfolio/cnn_vision_thumb.svg" class="proj-thumb-img" alt="Deep Learning CNN MultiClass Image Classifier" width="640" height="360" style="width: 100%; height: 215px; object-fit: cover; display: block;">
                                    <div class="proj-overlay position-absolute w-100 h-100 d-flex align-items-center justify-content-center" style="top:0; left:0; background: rgba(11,15,25,0.85);">
                                        <div class="text-center p-3">
                                            <a href="https://github.com/iamharshverma/Deep_Learning-CNN_MultiClass_ImageClassifier" target="_blank" class="btn btn-sm btn-primary rounded-pill px-3 mr-2 mb-2 font-weight-bold"><i class="mdi mdi-github-face mr-1"></i> GitHub Repo</a>
                                            <a href="page-portfolio" class="btn btn-sm btn-outline-light rounded-pill px-3 mb-2 font-weight-bold"><i class="mdi mdi-information-outline mr-1"></i> Details</a>
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
                        <div class="card border-0 custom-project-card position-relative d-block overflow-hidden rounded-lg shadow-sm bg-white h-100">
                            <div class="card-body p-0 position-relative">
                                <div class="proj-thumb-wrapper position-relative overflow-hidden" style="background: #0b0f19; height: 215px; width: 100%; display: block;">
                                    <img src="images/portfolio/lockfree_hashtable_thumb.svg" class="proj-thumb-img" alt="Lock-Free Concurrent Hash Table" width="640" height="360" style="width: 100%; height: 215px; object-fit: cover; display: block;">
                                    <div class="proj-overlay position-absolute w-100 h-100 d-flex align-items-center justify-content-center" style="top:0; left:0; background: rgba(11,15,25,0.85);">
                                        <div class="text-center p-3">
                                            <a href="https://github.com/iamharshverma/JavaHashTableCustomImplementation" target="_blank" class="btn btn-sm btn-primary rounded-pill px-3 mr-2 mb-2 font-weight-bold"><i class="mdi mdi-github-face mr-1"></i> GitHub Repo</a>
                                            <a href="page-portfolio" class="btn btn-sm btn-outline-light rounded-pill px-3 mb-2 font-weight-bold"><i class="mdi mdi-information-outline mr-1"></i> Details</a>
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
                        <div class="card border-0 custom-project-card position-relative d-block overflow-hidden rounded-lg shadow-sm bg-white h-100">
                            <div class="card-body p-0 position-relative">
                                <div class="proj-thumb-wrapper position-relative overflow-hidden" style="background: #0b0f19; height: 215px; width: 100%; display: block;">
                                    <img src="images/portfolio/microservice_gateway_thumb.svg" class="proj-thumb-img" alt="WordDoc Frequency Microservice API" width="640" height="360" style="width: 100%; height: 215px; object-fit: cover; display: block;">
                                    <div class="proj-overlay position-absolute w-100 h-100 d-flex align-items-center justify-content-center" style="top:0; left:0; background: rgba(11,15,25,0.85);">
                                        <div class="text-center p-3">
                                            <a href="https://github.com/iamharshverma/APIMicroServiceForWordDocFrequencyCount" target="_blank" class="btn btn-sm btn-primary rounded-pill px-3 mr-2 mb-2 font-weight-bold"><i class="mdi mdi-github-face mr-1"></i> GitHub Repo</a>
                                            <a href="page-portfolio" class="btn btn-sm btn-outline-light rounded-pill px-3 mb-2 font-weight-bold"><i class="mdi mdi-information-outline mr-1"></i> Details</a>
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
                        <div class="card border-0 custom-project-card position-relative d-block overflow-hidden rounded-lg shadow-sm bg-white h-100">
                            <div class="card-body p-0 position-relative">
                                <div class="proj-thumb-wrapper position-relative overflow-hidden" style="background: #0b0f19; height: 215px; width: 100%; display: block;">
                                    <img src="images/portfolio/hadoop_cluster_thumb.svg" class="proj-thumb-img" alt="BigData Hadoop Social Network" width="640" height="360" style="width: 100%; height: 215px; object-fit: cover; display: block;">
                                    <div class="proj-overlay position-absolute w-100 h-100 d-flex align-items-center justify-content-center" style="top:0; left:0; background: rgba(11,15,25,0.85);">
                                        <div class="text-center p-3">
                                            <a href="https://github.com/iamharshverma/BigData-Hadoop_SocialNetwork" target="_blank" class="btn btn-sm btn-primary rounded-pill px-3 mr-2 mb-2 font-weight-bold"><i class="mdi mdi-github-face mr-1"></i> GitHub Repo</a>
                                            <a href="page-portfolio" class="btn btn-sm btn-outline-light rounded-pill px-3 mb-2 font-weight-bold"><i class="mdi mdi-information-outline mr-1"></i> Details</a>
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
                        <div class="card border-0 custom-project-card position-relative d-block overflow-hidden rounded-lg shadow-sm bg-white h-100">
                            <div class="card-body p-0 position-relative">
                                <div class="proj-thumb-wrapper position-relative overflow-hidden" style="background: #0b0f19; height: 215px; width: 100%; display: block;">
                                    <img src="images/portfolio/ir_tokenizer_thumb.svg" class="proj-thumb-img" alt="Tokanize and Stemming" width="640" height="360" style="width: 100%; height: 215px; object-fit: cover; display: block;">
                                    <div class="proj-overlay position-absolute w-100 h-100 d-flex align-items-center justify-content-center" style="top:0; left:0; background: rgba(11,15,25,0.85);">
                                        <div class="text-center p-3">
                                            <a href="https://github.com/iamharshverma/TokanizeAndStemming" target="_blank" class="btn btn-sm btn-primary rounded-pill px-3 mr-2 mb-2 font-weight-bold"><i class="mdi mdi-github-face mr-1"></i> GitHub Repo</a>
                                            <a href="page-portfolio" class="btn btn-sm btn-outline-light rounded-pill px-3 mb-2 font-weight-bold"><i class="mdi mdi-information-outline mr-1"></i> Details</a>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-3">
                                    <div class="d-flex align-items-center justify-content-between mb-2">
                                        <span class="badge badge-info px-2 py-1 font-weight-bold" style="font-size: 11px;">INFORMATION RETRIEVAL • NLP</span>
                                        <small class="text-muted"><i class="mdi mdi-format-list-bulleted-type text-info mr-1"></i> Lexer</small>
                                    </div>
                                    <h5 class="mb-2" style="font-size: 17px; line-height: 1.35;">
                                        <a href="https://github.com/iamharshverma/TokanizeAndStemming" target="_blank" class="text-dark font-weight-bold proj-title-link">Lexer &amp; Inverted Index Pipeline</a>
                                    </h5>
                                    <p class="text-muted small mb-3" style="line-height: 1.5; min-height: 42px;">
                                        Lexical analyzer and Porter stemming algorithms with inverted index posting lists for high-speed sub-millisecond full-text retrieval.
                                    </p>
                                    <div class="d-flex flex-wrap mb-3" style="gap: 5px;">
                                        <span class="badge badge-light border text-muted">Porter Stemmer</span>
                                        <span class="badge badge-light border text-muted">Inverted Index</span>
                                        <span class="badge badge-light border text-muted">Lexer</span>
                                        <span class="badge badge-light border text-muted">Stopwords</span>
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

                    <!-- Project 12: Skip List Index -->
                    <div class="col-lg-4 col-md-6 col-12 mt-4 pt-2 home-proj-card" data-category="security">
                        <div class="card border-0 custom-project-card position-relative d-block overflow-hidden rounded-lg shadow-sm bg-white h-100">
                            <div class="card-body p-0 position-relative">
                                <div class="proj-thumb-wrapper position-relative overflow-hidden" style="background: #0b0f19; height: 215px; width: 100%; display: block;">
                                    <img src="images/portfolio/skiplist_index_thumb.svg" class="proj-thumb-img" alt="SkipList Implementation" width="640" height="360" style="width: 100%; height: 215px; object-fit: cover; display: block;">
                                    <div class="proj-overlay position-absolute w-100 h-100 d-flex align-items-center justify-content-center" style="top:0; left:0; background: rgba(11,15,25,0.85);">
                                        <div class="text-center p-3">
                                            <a href="https://github.com/iamharshverma/SkipLists" target="_blank" class="btn btn-sm btn-primary rounded-pill px-3 mr-2 mb-2 font-weight-bold"><i class="mdi mdi-github-face mr-1"></i> GitHub Repo</a>
                                            <a href="page-portfolio" class="btn btn-sm btn-outline-light rounded-pill px-3 mb-2 font-weight-bold"><i class="mdi mdi-information-outline mr-1"></i> Details</a>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-3">
                                    <div class="d-flex align-items-center justify-content-between mb-2">
                                        <span class="badge badge-success px-2 py-1 font-weight-bold" style="font-size: 11px;">DATA STRUCTURES • ALGORITHMS</span>
                                        <small class="text-muted"><i class="mdi mdi-layers-triple text-success mr-1"></i> O(log N)</small>
                                    </div>
                                    <h5 class="mb-2" style="font-size: 17px; line-height: 1.35;">
                                        <a href="https://github.com/iamharshverma/SkipLists" target="_blank" class="text-dark font-weight-bold proj-title-link">SkipList Probabilistic Multi-Tier Index</a>
                                    </h5>
                                    <p class="text-muted small mb-3" style="line-height: 1.5; min-height: 42px;">
                                        Probabilistic layered indexing structure delivering O(log N) search and insertion performance without tree-rebalancing locks.
                                    </p>
                                    <div class="d-flex flex-wrap mb-3" style="gap: 5px;">
                                        <span class="badge badge-light border text-muted">Skip List</span>
                                        <span class="badge badge-light border text-muted">O(log N)</span>
                                        <span class="badge badge-light border text-muted">Lock-Free Ready</span>
                                        <span class="badge badge-light border text-muted">Java</span>
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

pattern = re.compile(r'<!-- Projects/Work Start -->.*?<!-- Projects End -->', re.DOTALL)
if pattern.search(html):
    html = pattern.sub(clean_projects_section, html)
    print("Found and replaced projects section in index.html!")
else:
    print("Pattern still not found, checking fallback...")
    start_str = '<!-- Projects/Work Start -->'
    end_str = '<!-- Projects End -->'
    s_idx = html.find(start_str)
    e_idx = html.find(end_str)
    if s_idx != -1 and e_idx != -1:
        html = html[:s_idx] + clean_projects_section + html[e_idx + len(end_str):]
        print("Replaced by substring indexing!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("index.html updated successfully!")
