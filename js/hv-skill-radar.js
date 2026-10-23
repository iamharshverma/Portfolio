/**
 * Interactive Technical Skill Radar Chart (D3.js v7)
 * Harsh Verma Portfolio Website
 * Visualizes proficiency levels across AI/ML, Cloud, Security & Architecture.
 */

(function () {
  'use strict';

  // Benchmark datasets across technical specializations
  const RADAR_DATASETS = {
    all: {
      title: "Core Technical Domains",
      description: "Comprehensive cross-section of Harsh Verma's principal engineering capabilities spanning enterprise AI, distributed cloud, cyber resilience, and high-throughput systems.",
      skills: [
        {
          name: "Deep Learning",
          shortName: "Deep Learning",
          score: 95,
          baseline: 72,
          category: "AI & Machine Learning",
          icon: "images/skills/Deep_Learning.png",
          experience: "10+ Years",
          tags: ["PyTorch", "Transformers", "Distributed Training", "CUDA", "TensorRT"],
          desc: "Enterprise neural network architectures, custom model fine-tuning, high-throughput model quantization, and distributed GPU training orchestration."
        },
        {
          name: "NLP & LLM Systems",
          shortName: "NLP & LLMs",
          score: 94,
          baseline: 70,
          category: "AI & Machine Learning",
          icon: "images/skills/NLP.png",
          experience: "9+ Years",
          tags: ["RAG Pipelines", "Vector Embeddings", "Semantic Search", "Prompt Engineering"],
          desc: "End-to-end Retrieval Augmented Generation (RAG) backbones, semantic vector caching, cross-encoder ranking, and enterprise agent reasoning."
        },
        {
          name: "Computer Vision",
          shortName: "Computer Vision",
          score: 92,
          baseline: 68,
          category: "AI & Machine Learning",
          icon: "images/skills/CV.png",
          experience: "8+ Years",
          tags: ["Spatial Computing", "CNNs", "Object Detection", "GIS Research"],
          desc: "Spatial satellite computing rooted in ISRO R&D research, convolutional image analysis, and multi-modal computer vision architectures."
        },
        {
          name: "Multi-Agent Systems",
          shortName: "Agentic Systems",
          score: 96,
          baseline: 65,
          category: "AI & Machine Learning",
          icon: "images/skills/AI.png",
          experience: "8+ Years",
          tags: ["Autonomous Agents", "Deterministic Guardrails", "Multi-Agent Consensus"],
          desc: "Architecting autonomous enterprise agents with deterministic verification, multi-agent protocol consensus, and dynamic self-healing execution loops."
        },
        {
          name: "Cloud (GCP & AWS)",
          shortName: "Cloud (GCP/AWS)",
          score: 90,
          baseline: 75,
          category: "Cloud & Distributed",
          icon: "images/skills/gcp.png",
          experience: "10+ Years",
          tags: ["GCP Vertex AI", "AWS S3 / EC2", "BigQuery", "Terraform", "Serverless"],
          desc: "Architecting multi-region high-availability cloud foundations, scalable AI inference clusters, and enterprise petabyte streaming backbones."
        },
        {
          name: "Distributed Storage",
          shortName: "Storage & S3",
          score: 85,
          baseline: 74,
          category: "Cloud & Distributed",
          icon: "images/skills/amazons3.svg",
          experience: "9+ Years",
          tags: ["S3 Compliance", "Tiered Storage", "Petabyte Lakes", "Blob Caching"],
          desc: "High-throughput object storage topologies, petabyte-scale streaming dataset ingestion, zero-egress caching, and compliance retention policies."
        },
        {
          name: "Zero-Trust Security",
          shortName: "Cyber Defense",
          score: 94,
          baseline: 68,
          category: "Architecture & Security",
          icon: "images/skills/AI.png",
          experience: "9+ Years",
          tags: ["Zero-Trust", "Intent-Based Security", "Clean Attack Defense", "mTLS"],
          desc: "Pioneering intent-based cybersecurity architectures, countering zero-day agentic threats, and enforcing cryptographically verifiable microsegmentation."
        },
        {
          name: "Load Simulation",
          shortName: "Load Simulation",
          score: 92,
          baseline: 70,
          category: "Distributed Systems",
          icon: "images/skills/nodejs-icon.svg",
          experience: "9+ Years",
          tags: ["HikeRunner Creator", "Stress Testing", "Latency Profiling", "JMeter"],
          desc: "Creator of the open-source HikeRunner load-testing framework; simulating hundreds of thousands of concurrent transactions for high-frequency FinTech."
        },
        {
          name: "Full-Stack & APIs",
          shortName: "Full-Stack APIs",
          score: 82,
          baseline: 78,
          category: "Software Engineering",
          icon: "images/skills/nodejs-icon.svg",
          experience: "10+ Years",
          tags: ["Node.js", "Angular", "TypeScript", "REST & gRPC", "WebSockets"],
          desc: "Low-latency API gateways, reactive component hierarchies, real-time bidirectional WebSocket synchronization, and type-safe systems."
        },
        {
          name: "Databases (SQL/NoSQL)",
          shortName: "SQL & NoSQL",
          score: 86,
          baseline: 75,
          category: "Data Architecture",
          icon: "images/skills/post_gray_sql.svg",
          experience: "10+ Years",
          tags: ["PostgreSQL", "MongoDB", "ACID Compliance", "Distributed Sharding"],
          desc: "Relational database tuning, query plan optimization, sharded document stores, and dual-layer caching strategies."
        }
      ]
    },

    aiml: {
      title: "AI & Machine Learning Specialization",
      description: "Deep dive into model architectures, autonomous multi-agent orchestration, and production AI engineering.",
      skills: [
        {
          name: "Deep Learning",
          shortName: "Deep Learning",
          score: 95,
          baseline: 70,
          category: "AI & ML",
          icon: "images/skills/Deep_Learning.png",
          experience: "10+ Years",
          tags: ["PyTorch", "TensorFlow", "Quantization", "Model Distillation"],
          desc: "Deep neural networks, PyTorch, model quantization, distributed training, and cost-efficient edge compilation."
        },
        {
          name: "NLP & LLM Systems",
          shortName: "NLP & LLMs",
          score: 94,
          baseline: 68,
          category: "AI & ML",
          icon: "images/skills/NLP.png",
          experience: "9+ Years",
          tags: ["Transformer Models", "RAG", "Embeddings", "Reasoning Chains"],
          desc: "Transformer architectures, contextual vector indexing, high-density embeddings, and semantic guardrail enforcement."
        },
        {
          name: "Computer Vision",
          shortName: "Computer Vision",
          score: 92,
          baseline: 65,
          category: "AI & ML",
          icon: "images/skills/CV.png",
          experience: "8+ Years",
          tags: ["Spatial Imagery", "Feature Extraction", "ISRO Research", "Object Tracking"],
          desc: "Spatial imagery analysis, remote sensing GIS architectures, and multi-scale object detection models."
        },
        {
          name: "Multi-Agent Systems",
          shortName: "Agentic Systems",
          score: 96,
          baseline: 62,
          category: "AI & ML",
          icon: "images/skills/AI.png",
          experience: "8+ Years",
          tags: ["Inter-Agent Protocols", "Consensus", "Deterministic Moats", "Task Decomposition"],
          desc: "Pioneering deterministic multi-agent architectures that guarantee predictable outcomes in mission-critical enterprise workflows."
        },
        {
          name: "Explainable AI (XAI)",
          shortName: "Explainable AI",
          score: 90,
          baseline: 64,
          category: "AI & ML",
          icon: "images/skills/AI.png",
          experience: "7+ Years",
          tags: ["SHAP", "LIME", "Model Attribution", "Regulatory Compliance"],
          desc: "Developing transparent decision pathways, feature importance attribution, and audit-ready machine learning frameworks."
        },
        {
          name: "Real-Time Feature Stores",
          shortName: "Feature Pipelines",
          score: 91,
          baseline: 66,
          category: "AI & ML",
          icon: "images/skills/gcp.png",
          experience: "8+ Years",
          tags: ["Feature Engineering", "Low-Latency Stores", "Drift Detection"],
          desc: "Zero-latency online feature serving, offline historical training parity, and continuous data drift monitoring."
        }
      ]
    },

    cloud: {
      title: "Cloud & Distributed Systems",
      description: "High-scale distributed infrastructure, autonomous cyber resilience, and cloud platform mastery.",
      skills: [
        {
          name: "Google Cloud (GCP)",
          shortName: "Google Cloud",
          score: 90,
          baseline: 74,
          category: "Cloud Infrastructure",
          icon: "images/skills/gcp.png",
          experience: "10+ Years",
          tags: ["GKE", "Vertex AI", "BigQuery", "Cloud Run", "VPC"],
          desc: "Enterprise GCP foundations, multi-region container deployments, Vertex AI workloads, and BigQuery analytics."
        },
        {
          name: "Amazon Web Services (AWS)",
          shortName: "AWS & S3",
          score: 88,
          baseline: 76,
          category: "Cloud Infrastructure",
          icon: "images/skills/amazons3.svg",
          experience: "10+ Years",
          tags: ["S3", "EC2", "Lambda", "DynamoDB", "CloudWatch"],
          desc: "Architecting fault-tolerant AWS environments, serverless compute, automated tiering, and edge distribution."
        },
        {
          name: "Zero-Trust Architecture",
          shortName: "Zero-Trust",
          score: 94,
          baseline: 68,
          category: "Cybersecurity",
          icon: "images/skills/AI.png",
          experience: "9+ Years",
          tags: ["Continuous Auth", "Microsegmentation", "Least Privilege"],
          desc: "Eliminating perimeter assumptions through intent verification, continuous behavioral validation, and cryptographic token attestation."
        },
        {
          name: "HikeRunner Load Testing",
          shortName: "Load Simulation",
          score: 92,
          baseline: 70,
          category: "Reliability & Perf",
          icon: "images/skills/nodejs-icon.svg",
          experience: "9+ Years",
          tags: ["HikeRunner", "Stress Profiling", "Distributed Workers"],
          desc: "Framework architect for extreme-scale distributed load simulation, throughput optimization, and bottleneck discovery."
        },
        {
          name: "Distributed Microservices",
          shortName: "Microservices",
          score: 89,
          baseline: 75,
          category: "Distributed Systems",
          icon: "images/skills/nodejs-icon.svg",
          experience: "10+ Years",
          tags: ["Event Sourcing", "gRPC", "Kafka / PubSub", "Circuit Breaking"],
          desc: "Decoupled asynchronous service meshes, resilient message queues, and high-concurrency event-driven processing."
        },
        {
          name: "Container Orchestration",
          shortName: "Kubernetes",
          score: 87,
          baseline: 72,
          category: "DevOps & Cloud",
          icon: "images/skills/gcp.png",
          experience: "8+ Years",
          tags: ["K8s", "Docker", "Helm", "GitOps", "Service Mesh"],
          desc: "Production container lifecycle management, automated horizontal pod scaling, zero-downtime blue/green rollouts."
        }
      ]
    },

    engineering: {
      title: "Software & Data Architecture",
      description: "Application engineering, databases, responsive frameworks, and native mobile technologies.",
      skills: [
        {
          name: "Node.js & Runtimes",
          shortName: "Node.js",
          score: 85,
          baseline: 78,
          category: "Full-Stack",
          icon: "images/skills/nodejs-icon.svg",
          experience: "10+ Years",
          tags: ["Event Loop", "V8 Optimization", "Express", "Streams API"],
          desc: "High-throughput asynchronous servers, streaming data pipelines, and microservice backend orchestration."
        },
        {
          name: "Angular & Frontend",
          shortName: "Angular",
          score: 80,
          baseline: 74,
          category: "Frontend",
          icon: "images/skills/Angular.svg",
          experience: "8+ Years",
          tags: ["TypeScript", "RxJS", "Component Architecture", "State Management"],
          desc: "Enterprise client architecture, reactive streams, modular dependency injection, and clean state machines."
        },
        {
          name: "Android & Mobile",
          shortName: "Android",
          score: 80,
          baseline: 70,
          category: "Mobile",
          icon: "images/skills/android.svg",
          experience: "7+ Years",
          tags: ["Kotlin", "Android SDK", "Background Sync", "Offline First"],
          desc: "Native Android applications, reactive architectural patterns, background sync services, and device sensor integration."
        },
        {
          name: "PostgreSQL & Relational",
          shortName: "PostgreSQL",
          score: 84,
          baseline: 75,
          category: "Databases",
          icon: "images/skills/post_gray_sql.svg",
          experience: "10+ Years",
          tags: ["SQL Optimization", "Partitioning", "EXPLAIN ANALYZE", "Indexes"],
          desc: "Complex analytical queries, index optimization, write-ahead logging, and transaction isolation integrity."
        },
        {
          name: "MongoDB & NoSQL",
          shortName: "MongoDB",
          score: 82,
          baseline: 73,
          category: "Databases",
          icon: "images/skills/mongodb.svg",
          experience: "8+ Years",
          tags: ["Document Models", "Aggregation Pipeline", "Sharding"],
          desc: "Flexible schema design, high-velocity document ingestion, aggregation pipelines, and distributed replication."
        },
        {
          name: "Responsive UI Architecture",
          shortName: "Bootstrap & CSS",
          score: 85,
          baseline: 77,
          category: "UI Systems",
          icon: "images/skills/bootstrap.svg",
          experience: "10+ Years",
          tags: ["Grid Systems", "WCAG AA Contrast", "CSS Variables", "Animations"],
          desc: "Crafting fluid, high-contrast, accessible interfaces that adapt flawlessly across mobile, tablet, and desktop viewports."
        }
      ]
    }
  };

  // State management
  let currentCategory = 'all';
  let showBaseline = true;
  let activeSkillIndex = 0;
  let svg = null;
  let g = null;
  let width = 520;
  let height = 480;
  let radius = 175;

  function isDarkMode() {
    return document.documentElement.classList.contains('dark-mode') || document.body.classList.contains('dark-mode');
  }

  function getThemeColors() {
    const dark = isDarkMode();
    return {
      text: dark ? '#e2e8f0' : '#1e293b',
      textMuted: dark ? '#94a3b8' : '#64748b',
      gridLines: dark ? 'rgba(148, 163, 184, 0.22)' : 'rgba(15, 23, 42, 0.12)',
      gridFill: dark ? 'rgba(15, 23, 42, 0.45)' : 'rgba(248, 250, 252, 0.65)',
      spokeLines: dark ? 'rgba(148, 163, 184, 0.25)' : 'rgba(15, 23, 42, 0.14)',
      harshStroke: dark ? '#38bdf8' : '#2563eb',
      harshFillStart: dark ? 'rgba(56, 189, 248, 0.35)' : 'rgba(37, 99, 235, 0.25)',
      harshFillEnd: dark ? 'rgba(6, 182, 212, 0.15)' : 'rgba(14, 165, 233, 0.10)',
      baselineStroke: dark ? '#64748b' : '#94a3b8',
      baselineFill: dark ? 'rgba(100, 116, 139, 0.12)' : 'rgba(148, 163, 184, 0.08)',
      nodeStroke: dark ? '#38bdf8' : '#2563eb',
      nodeFill: dark ? '#0f172a' : '#ffffff'
    };
  }

  /**
   * Initializes the D3 Radar Chart Canvas
   */
  function initRadarChart() {
    const container = document.getElementById('skillRadarChart');
    if (!container) return;

    if (typeof d3 === 'undefined') {
      console.warn('D3.js is not yet loaded, retrying in 100ms...');
      setTimeout(initRadarChart, 100);
      return;
    }

    container.innerHTML = '';

    // Create SVG with responsive viewBox
    svg = d3.select(container)
      .append('svg')
      .attr('class', 'skill-radar-svg')
      .attr('viewBox', `0 0 ${width} ${height}`)
      .attr('preserveAspectRatio', 'xMidYMid meet')
      .attr('role', 'img')
      .attr('aria-label', 'Interactive Technical Skill Proficiency Radar Chart');

    // Gradient definitions
    const defs = svg.append('defs');

    const gradient = defs.append('radialGradient')
      .attr('id', 'radarHarshGradient')
      .attr('cx', '50%')
      .attr('cy', '50%')
      .attr('r', '55%');

    gradient.append('stop')
      .attr('offset', '0%')
      .attr('stop-color', isDarkMode() ? 'rgba(56, 189, 248, 0.45)' : 'rgba(37, 99, 235, 0.35)');

    gradient.append('stop')
      .attr('offset', '100%')
      .attr('stop-color', isDarkMode() ? 'rgba(6, 182, 212, 0.15)' : 'rgba(14, 165, 233, 0.10)');

    // Drop shadow filter for nodes and active line
    const filter = defs.append('filter')
      .attr('id', 'radarGlow')
      .attr('x', '-30%')
      .attr('y', '-30%')
      .attr('width', '160%')
      .attr('height', '160%');

    filter.append('feGaussianBlur')
      .attr('stdDeviation', '3')
      .attr('result', 'coloredBlur');

    const feMerge = filter.append('feMerge');
    feMerge.append('feMergeNode').attr('in', 'coloredBlur');
    feMerge.append('feMergeNode').attr('in', 'SourceGraphic');

    // Central group translated to center of canvas
    g = svg.append('g')
      .attr('transform', `translate(${width / 2}, ${height / 2})`);

    // Draw initial chart
    renderChart(currentCategory, false);

    // Initial update of inspector
    updateInspector(RADAR_DATASETS[currentCategory].skills[0]);
  }

  /**
   * Helper to compute vertex coordinates on radar
   */
  function getCoordinates(angle, value, maxVal = 100) {
    const r = (value / maxVal) * radius;
    const x = Math.sin(angle) * r;
    const y = -Math.cos(angle) * r;
    return { x, y };
  }

  /**
   * Renders or updates the radar chart with smooth D3 transitions
   */
  function renderChart(categoryKey, animate = true) {
    if (!g) return;

    const dataObj = RADAR_DATASETS[categoryKey] || RADAR_DATASETS.all;
    const skills = dataObj.skills;
    const totalAxes = skills.length;
    const angleSlice = (Math.PI * 2) / totalAxes;
    const colors = getThemeColors();

    // Update gradient colors based on dark mode state
    d3.select('#radarHarshGradient stop:nth-child(1)')
      .attr('stop-color', colors.harshFillStart);
    d3.select('#radarHarshGradient stop:nth-child(2)')
      .attr('stop-color', colors.harshFillEnd);

    // 1. Draw Concentric Grid Rings (Levels: 20%, 40%, 60%, 80%, 100%)
    const levels = [20, 40, 60, 80, 100];
    let gridGroup = g.select('.radar-grid-layer');
    if (gridGroup.empty()) {
      gridGroup = g.append('g').attr('class', 'radar-grid-layer');
    }

    // Grid polygons
    const gridPolygons = gridGroup.selectAll('.radar-grid-polygon-bg')
      .data(levels);

    gridPolygons.enter()
      .append('polygon')
      .attr('class', 'radar-grid-polygon-bg')
      .merge(gridPolygons)
      .transition().duration(animate ? 500 : 0)
      .attr('points', function (lvl) {
        return skills.map((_, i) => {
          const pt = getCoordinates(angleSlice * i, lvl);
          return `${pt.x},${pt.y}`;
        }).join(' ');
      })
      .attr('fill', colors.gridFill)
      .attr('stroke', colors.gridLines);

    gridPolygons.exit().remove();

    // Percentage labels on vertical spoke
    const gridLabels = gridGroup.selectAll('.radar-grid-label')
      .data(levels);

    gridLabels.enter()
      .append('text')
      .attr('class', 'radar-grid-label')
      .merge(gridLabels)
      .attr('x', 6)
      .attr('y', d => -(d / 100) * radius + 4)
      .attr('fill', colors.textMuted)
      .text(d => `${d}%`);

    gridLabels.exit().remove();

    // 2. Draw Radial Spokes
    let spokesGroup = g.select('.radar-spokes-layer');
    if (spokesGroup.empty()) {
      spokesGroup = g.append('g').attr('class', 'radar-spokes-layer');
    }

    const spokes = spokesGroup.selectAll('.radar-spoke')
      .data(skills, (d, i) => `${categoryKey}-${i}`);

    spokes.enter()
      .append('line')
      .attr('class', 'radar-spoke')
      .attr('x1', 0)
      .attr('y1', 0)
      .merge(spokes)
      .transition().duration(animate ? 500 : 0)
      .attr('x2', (d, i) => getCoordinates(angleSlice * i, 100).x)
      .attr('y2', (d, i) => getCoordinates(angleSlice * i, 100).y)
      .attr('stroke', colors.spokeLines);

    spokes.exit().remove();

    // 3. Draw Industry Baseline Polygon (if enabled)
    let baselineGroup = g.select('.radar-baseline-layer');
    if (baselineGroup.empty()) {
      baselineGroup = g.append('g').attr('class', 'radar-baseline-layer');
    }

    const baselinePoints = skills.map((d, i) => {
      const pt = getCoordinates(angleSlice * i, d.baseline || 70);
      return `${pt.x},${pt.y}`;
    }).join(' ');

    let baselinePolygon = baselineGroup.select('.radar-polygon-baseline');
    if (baselinePolygon.empty()) {
      baselinePolygon = baselineGroup.append('polygon')
        .attr('class', 'radar-polygon-baseline')
        .attr('stroke', colors.baselineStroke)
        .attr('fill', colors.baselineFill);
    }

    baselinePolygon
      .transition().duration(animate ? 550 : 0)
      .attr('points', baselinePoints)
      .style('opacity', showBaseline ? 1 : 0);

    // 4. Draw Harsh Verma Skill Polygon
    let dataGroup = g.select('.radar-data-layer');
    if (dataGroup.empty()) {
      dataGroup = g.append('g').attr('class', 'radar-data-layer');
    }

    const harshPoints = skills.map((d, i) => {
      const pt = getCoordinates(angleSlice * i, d.score);
      return `${pt.x},${pt.y}`;
    }).join(' ');

    let harshPolygon = dataGroup.select('.radar-polygon-harsh');
    if (harshPolygon.empty()) {
      harshPolygon = dataGroup.append('polygon')
        .attr('class', 'radar-polygon-harsh')
        .attr('stroke', colors.harshStroke);
    }

    harshPolygon
      .transition().duration(animate ? 600 : 0)
      .attr('points', harshPoints)
      .attr('stroke', colors.harshStroke);

    // 5. Draw Vertex Nodes (Interactive Points)
    let nodesGroup = g.select('.radar-nodes-layer');
    if (nodesGroup.empty()) {
      nodesGroup = g.append('g').attr('class', 'radar-nodes-layer');
    }

    const nodes = nodesGroup.selectAll('.radar-vertex-node')
      .data(skills, (d, i) => `${categoryKey}-${d.name}`);

    const nodesEnter = nodes.enter()
      .append('circle')
      .attr('class', 'radar-vertex-node')
      .attr('r', 0)
      .attr('stroke', colors.nodeStroke)
      .attr('fill', colors.nodeFill);

    const mergedNodes = nodesEnter.merge(nodes);

    mergedNodes
      .transition().duration(animate ? 600 : 0)
      .attr('cx', (d, i) => getCoordinates(angleSlice * i, d.score).x)
      .attr('cy', (d, i) => getCoordinates(angleSlice * i, d.score).y)
      .attr('r', (d, i) => (i === activeSkillIndex ? 8 : 5))
      .attr('stroke', colors.nodeStroke)
      .attr('fill', (d, i) => (i === activeSkillIndex ? (isDarkMode() ? '#0284c7' : '#dbeafe') : colors.nodeFill));

    nodes.exit()
      .transition().duration(300)
      .attr('r', 0)
      .remove();

    // Node Event Listeners
    mergedNodes
      .on('mouseenter', function (event, d) {
        const i = skills.indexOf(d);
        highlightSkill(i);
        showTooltip(event, d);
      })
      .on('mousemove', function (event, d) {
        showTooltip(event, d);
      })
      .on('mouseleave', function () {
        hideTooltip();
      })
      .on('click', function (event, d) {
        const i = skills.indexOf(d);
        highlightSkill(i);
      });

    // 6. Draw Axis Labels
    let labelsGroup = g.select('.radar-labels-layer');
    if (labelsGroup.empty()) {
      labelsGroup = g.append('g').attr('class', 'radar-labels-layer');
    }

    const labels = labelsGroup.selectAll('.radar-axis-label')
      .data(skills, (d, i) => `${categoryKey}-${d.name}`);

    const labelsEnter = labels.enter()
      .append('text')
      .attr('class', 'radar-axis-label')
      .attr('text-anchor', 'middle')
      .attr('dy', '0.35em');

    const mergedLabels = labelsEnter.merge(labels);

    mergedLabels
      .transition().duration(animate ? 600 : 0)
      .attr('x', (d, i) => {
        const pt = getCoordinates(angleSlice * i, 116);
        return pt.x;
      })
      .attr('y', (d, i) => {
        const pt = getCoordinates(angleSlice * i, 116);
        return pt.y;
      })
      .attr('text-anchor', (d, i) => {
        const x = getCoordinates(angleSlice * i, 116).x;
        if (Math.abs(x) < 15) return 'middle';
        return x > 0 ? 'start' : 'end';
      })
      .attr('fill', colors.text)
      .text(d => `${d.shortName} (${d.score}%)`);

    labels.exit().remove();

    // Label Event Listeners
    mergedLabels
      .on('mouseenter', function (event, d) {
        const i = skills.indexOf(d);
        highlightSkill(i);
      })
      .on('click', function (event, d) {
        const i = skills.indexOf(d);
        highlightSkill(i);
      });
  }

  /**
   * Highlights a specific skill node, spoke, and updates the Live Inspector
   */
  function highlightSkill(index) {
    activeSkillIndex = index;
    const dataObj = RADAR_DATASETS[currentCategory];
    const skill = dataObj.skills[index];
    if (!skill) return;

    // Update node visual states
    g.selectAll('.radar-vertex-node')
      .classed('node-active', (d, i) => i === index)
      .attr('r', (d, i) => (i === index ? 8 : 5));

    // Update spokes
    g.selectAll('.radar-spoke')
      .classed('spoke-active', (d, i) => i === index);

    // Update labels
    g.selectAll('.radar-axis-label')
      .classed('label-active', (d, i) => i === index);

    // Update Live Inspector Panel
    updateInspector(skill);
  }

  /**
   * Updates the Capability Inspector Panel UI
   */
  function updateInspector(skill) {
    const iconEl = document.getElementById('inspectorIcon');
    const nameEl = document.getElementById('inspectorSkillName');
    const categoryEl = document.getElementById('inspectorCategory');
    const expEl = document.getElementById('inspectorExp');
    const scoreEl = document.getElementById('inspectorScore');
    const fillEl = document.getElementById('inspectorProgressFill');
    const descEl = document.getElementById('inspectorDesc');
    const tagsEl = document.getElementById('inspectorTags');
    const baselineDiffEl = document.getElementById('inspectorBaselineDiff');

    if (!nameEl) return;

    if (iconEl && skill.icon) {
      iconEl.src = skill.icon;
      iconEl.alt = skill.name;
    }
    nameEl.textContent = skill.name;
    if (categoryEl) categoryEl.textContent = skill.category;
    if (expEl) expEl.textContent = skill.experience;
    if (scoreEl) scoreEl.textContent = `${skill.score}%`;
    if (fillEl) fillEl.style.width = `${skill.score}%`;
    if (descEl) descEl.textContent = skill.desc;

    // Tags
    if (tagsEl && skill.tags) {
      tagsEl.innerHTML = skill.tags.map(t => `<span class="inspector-tag">${t}</span>`).join('');
    }

    // Baseline diff
    if (baselineDiffEl && skill.baseline) {
      const diff = skill.score - skill.baseline;
      baselineDiffEl.textContent = `+${diff}% vs Industry Principal Baseline (${skill.baseline}%)`;
    }
  }

  /**
   * Tooltip management
   */
  let tooltip = null;

  function getTooltip() {
    if (!tooltip) {
      tooltip = document.getElementById('skillRadarTooltip');
      if (!tooltip) {
        tooltip = document.createElement('div');
        tooltip.id = 'skillRadarTooltip';
        tooltip.className = 'skill-radar-tooltip';
        document.body.appendChild(tooltip);
      }
    }
    return tooltip;
  }

  function showTooltip(event, d) {
    const tt = getTooltip();
    tt.innerHTML = `<strong>${d.name}</strong> · <span style="color:#38bdf8">${d.score}%</span><br><span style="font-size:0.75rem;opacity:0.85">${d.category} · ${d.experience}</span>`;
    tt.style.left = `${event.pageX}px`;
    tt.style.top = `${event.pageY - 12}px`;
    tt.classList.add('show');
  }

  function hideTooltip() {
    const tt = getTooltip();
    if (tt) {
      tt.classList.remove('show');
    }
  }

  /**
   * Set up interactive event listeners
   */
  function setupEventListeners() {
    // 1. Domain Category Buttons
    const categoryButtons = document.querySelectorAll('.skill-cat-pill');
    categoryButtons.forEach(btn => {
      btn.addEventListener('click', function () {
        const cat = this.getAttribute('data-category');
        if (cat && RADAR_DATASETS[cat]) {
          currentCategory = cat;
          activeSkillIndex = 0;

          categoryButtons.forEach(b => b.classList.remove('active'));
          this.classList.add('active');

          renderChart(currentCategory, true);
          updateInspector(RADAR_DATASETS[currentCategory].skills[0]);
        }
      });
    });

    // 2. View Switcher (Radar vs Matrix Grid vs Dual View)
    const viewButtons = document.querySelectorAll('.skill-view-btn');
    const radarWrapper = document.getElementById('skillRadarDisplay');
    const gridWrapper = document.getElementById('skillGridDisplay');

    viewButtons.forEach(btn => {
      btn.addEventListener('click', function () {
        const mode = this.getAttribute('data-view');
        viewButtons.forEach(b => b.classList.remove('active'));
        this.classList.add('active');

        if (mode === 'radar') {
          if (radarWrapper) radarWrapper.style.display = 'block';
          if (gridWrapper) gridWrapper.style.display = 'none';
        } else if (mode === 'grid') {
          if (radarWrapper) radarWrapper.style.display = 'none';
          if (gridWrapper) gridWrapper.style.display = 'block';
        } else if (mode === 'dual') {
          if (radarWrapper) radarWrapper.style.display = 'block';
          if (gridWrapper) gridWrapper.style.display = 'block';
        }
      });
    });

    // 3. Baseline Overlay Toggle
    const baselineToggle = document.getElementById('toggleBaselineBtn');
    if (baselineToggle) {
      baselineToggle.addEventListener('click', function () {
        showBaseline = !showBaseline;
        const baselinePolygon = g.select('.radar-polygon-baseline');
        if (!baselinePolygon.empty()) {
          baselinePolygon.transition().duration(300).style('opacity', showBaseline ? 1 : 0);
        }
        this.style.opacity = showBaseline ? '1' : '0.45';
      });
    }

    // 4. Theme changes (MutationObserver on class attribute of documentElement and body)
    const observer = new MutationObserver(function () {
      if (svg) {
        renderChart(currentCategory, false);
      }
    });

    observer.observe(document.documentElement, { attributes: true, attributeFilter: ['class'] });
    observer.observe(document.body, { attributes: true, attributeFilter: ['class'] });

    // 5. Responsive window resize
    let resizeTimer = null;
    window.addEventListener('resize', function () {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(function () {
        if (svg) {
          renderChart(currentCategory, false);
        }
      }, 150);
    });
  }

  // DOMContentLoaded initialization
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      initRadarChart();
      setupEventListeners();
    });
  } else {
    initRadarChart();
    setupEventListeners();
  }
})();
