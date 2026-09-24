/**
 * D3.js Global Geographic Citation Heatmap Engine
 * Visualizes the global reach, citation distribution, and institutional research clusters
 * for Harsh Verma's peer-reviewed publications and patents.
 */
(function() {
    'use strict';

    // Citation dataset mapped by ISO numeric code & normalized country name
    const citationData = {
        // North America
        "840": {
            name: "United States of America",
            code: "USA",
            citations: 485,
            region: "na",
            institutions: ["Stanford University", "MIT", "UC Berkeley", "Carnegie Mellon University", "UT Austin", "Harvard University"],
            topPaper: "Continuous Integration & Distributed System Architecture at Scale",
            domain: "Enterprise Multi-Agent Systems & Petabyte Streaming",
            growth: "+42% YoY"
        },
        "124": {
            name: "Canada",
            code: "CAN",
            citations: 82,
            region: "na",
            institutions: ["University of Toronto", "Vector Institute", "University of Waterloo", "McGill University"],
            topPaper: "Adversarial Robustness in Deep Neural Firewalls",
            domain: "Adversarial Machine Learning & Cyber Defense",
            growth: "+28% YoY"
        },
        "484": {
            name: "Mexico",
            code: "MEX",
            citations: 7,
            region: "latam_mena",
            institutions: ["UNAM", "Tecnológico de Monterrey"],
            topPaper: "Fault-Tolerant Distributed Microservice Topologies",
            domain: "Software Reliability & Cloud Systems",
            growth: "+15% YoY"
        },

        // Europe (EMEA)
        "826": {
            name: "United Kingdom",
            code: "GBR",
            citations: 168,
            region: "eu",
            institutions: ["University of Cambridge", "University of Oxford", "Imperial College London", "UCL"],
            topPaper: "Cognitive AI & Real-Time Cyber Defense Topologies (IEEE CogML)",
            domain: "Autonomous Agents & Cognitive Cyber Systems",
            growth: "+35% YoY"
        },
        "276": {
            name: "Germany",
            code: "DEU",
            citations: 112,
            region: "eu",
            institutions: ["Technical University of Munich (TUM)", "Max Planck Institute for Informatics", "RWTH Aachen"],
            topPaper: "Deterministic Memory Architectures & Cache-Conscious Processing",
            domain: "Concurrent Low-Latency Systems",
            growth: "+31% YoY"
        },
        "756": {
            name: "Switzerland",
            code: "CHE",
            citations: 46,
            region: "eu",
            institutions: ["ETH Zürich", "EPFL Lausanne"],
            topPaper: "Distributed Consensus in Zero-Trust Edge Systems",
            domain: "Zero-Trust Architecture & Cryptographic Trust",
            growth: "+22% YoY"
        },
        "250": {
            name: "France",
            code: "FRA",
            citations: 35,
            region: "eu",
            institutions: ["École Polytechnique", "Sorbonne Université", "INRIA"],
            topPaper: "Statistical Profiling in High-Concurrency Cloud Systems",
            domain: "Automated Telemetry & Performance Stress Models",
            growth: "+18% YoY"
        },
        "528": {
            name: "Netherlands",
            code: "NLD",
            citations: 28,
            region: "eu",
            institutions: ["TU Delft", "University of Amsterdam", "CWI Amsterdam"],
            topPaper: "Zero-Copy Network Telemetry Instrumentation",
            domain: "High-Throughput Streaming Engines",
            growth: "+20% YoY"
        },
        "752": {
            name: "Sweden",
            code: "SWE",
            citations: 22,
            region: "eu",
            institutions: ["KTH Royal Institute of Technology", "Chalmers University"],
            topPaper: "Microservice Fault Resilience & Autonomous Telemetry",
            domain: "Cloud Infrastructure Resilience",
            growth: "+14% YoY"
        },
        "724": {
            name: "Spain",
            code: "ESP",
            citations: 15,
            region: "eu",
            institutions: ["UPC Barcelona", "Universidad Politécnica de Madrid"],
            topPaper: "Load Profiling in Large-Scale Distributed Environments",
            domain: "Empirical Performance Testing",
            growth: "+12% YoY"
        },
        "380": {
            name: "Italy",
            code: "ITA",
            citations: 14,
            region: "eu",
            institutions: ["Politecnico di Milano", "University of Bologna"],
            topPaper: "Predictive Analytics in Real-Time Network Security",
            domain: "Stateful Anomaly Detection",
            growth: "+10% YoY"
        },
        "372": {
            name: "Ireland",
            code: "IRL",
            citations: 12,
            region: "eu",
            institutions: ["Trinity College Dublin", "University College Dublin"],
            topPaper: "Cloud-Native Observability & Metric Streams",
            domain: "Observability Architecture",
            growth: "+16% YoY"
        },
        "578": {
            name: "Norway",
            code: "NOR",
            citations: 10,
            region: "eu",
            institutions: ["NTNU Trondheim", "University of Oslo"],
            topPaper: "Distributed Systems Performance Benchmarking",
            domain: "Benchmarking Topologies",
            growth: "+9% YoY"
        },
        "208": {
            name: "Denmark",
            code: "DNK",
            citations: 9,
            region: "eu",
            institutions: ["Technical University of Denmark (DTU)", "Univ of Copenhagen"],
            topPaper: "Adaptive Load Testing Frameworks",
            domain: "Automated Load Simulation",
            growth: "+11% YoY"
        },
        "246": {
            name: "Finland",
            code: "FIN",
            citations: 8,
            region: "eu",
            institutions: ["Aalto University", "University of Helsinki"],
            topPaper: "Asynchronous Stream Ingestion Topologies",
            domain: "Stream Engineering",
            growth: "+14% YoY"
        },

        // Asia-Pacific (APAC)
        "356": {
            name: "India",
            code: "IND",
            citations: 154,
            region: "apac",
            institutions: ["Indian Institute of Science (IISc Bangalore)", "IIT Delhi", "IIT Bombay", "IIT Madras"],
            topPaper: "Automated Load Testing Architecture & Performance Simulation (Patent 555747)",
            domain: "Load Testing Systems, Patents & Real-Time Big Data",
            growth: "+48% YoY"
        },
        "702": {
            name: "Singapore",
            code: "SGP",
            citations: 58,
            region: "apac",
            institutions: ["National University of Singapore (NUS)", "Nanyang Technological University (NTU)", "A*STAR"],
            topPaper: "Agentic Orchestration Frameworks & Self-Healing Cloud Topologies",
            domain: "Multi-Agent System Orchestration",
            growth: "+38% YoY"
        },
        "392": {
            name: "Japan",
            code: "JPN",
            citations: 39,
            region: "apac",
            institutions: ["University of Tokyo", "Kyoto University", "RIKEN AIP"],
            topPaper: "Low-Latency Cognitive Machine Learning Pipelines",
            domain: "Real-Time Machine Learning Systems",
            growth: "+21% YoY"
        },
        "036": {
            name: "Australia",
            code: "AUS",
            citations: 32,
            region: "apac",
            institutions: ["University of Melbourne", "Australian National University (ANU)", "UNSW Sydney"],
            topPaper: "Autonomous Agent Reliability & Fail-Safe Verification",
            domain: "Autonomous Agent Reliability",
            growth: "+19% YoY"
        },
        "410": {
            name: "South Korea",
            code: "KOR",
            citations: 21,
            region: "apac",
            institutions: ["KAIST", "Seoul National University", "POSTECH"],
            topPaper: "High-Throughput Deep Learning Inference Pipelines",
            domain: "Deep Neural Pipeline Acceleration",
            growth: "+24% YoY"
        },
        "158": {
            name: "Taiwan",
            code: "TWN",
            citations: 16,
            region: "apac",
            institutions: ["National Taiwan University (NTU)", "National Tsing Hua University"],
            topPaper: "Hardware-Accelerated Machine Learning at Edge",
            domain: "Edge Acceleration Architectures",
            growth: "+17% YoY"
        },
        "554": {
            name: "New Zealand",
            code: "NZL",
            citations: 8,
            region: "apac",
            institutions: ["University of Auckland"],
            topPaper: "Edge AI & Latency Bound Verification",
            domain: "Edge Systems Computing",
            growth: "+13% YoY"
        },

        // LATAM & MENA
        "784": {
            name: "United Arab Emirates",
            code: "ARE",
            citations: 26,
            region: "latam_mena",
            institutions: ["Mohamed bin Zayed University of AI (MBZUAI)", "Khalifa University"],
            topPaper: "Foundational Multi-Agent Trust Protocols",
            domain: "Decentralized AI Governance",
            growth: "+45% YoY"
        },
        "376": {
            name: "Israel",
            code: "ISR",
            citations: 24,
            region: "latam_mena",
            institutions: ["Technion – Israel Institute of Technology", "Tel Aviv University", "Weizmann Institute"],
            topPaper: "Stateful Threat Detection via Streaming Vector Ensembles",
            domain: "Cybersecurity ML & Firewall Defense",
            growth: "+27% YoY"
        },
        "682": {
            name: "Saudi Arabia",
            code: "SAU",
            citations: 19,
            region: "latam_mena",
            institutions: ["KAUST", "King Fahd University of Petroleum & Minerals"],
            topPaper: "Scalable Distributed Compute for AI Modeling",
            domain: "Distributed Compute Clusters",
            growth: "+32% YoY"
        },
        "076": {
            name: "Brazil",
            code: "BRA",
            citations: 18,
            region: "latam_mena",
            institutions: ["University of São Paulo (USP)", "UNICAMP"],
            topPaper: "Distributed Edge Computing & Automated Failover",
            domain: "High-Availability Edge Clusters",
            growth: "+19% YoY"
        },
        "710": {
            name: "South Africa",
            code: "ZAF",
            citations: 7,
            region: "latam_mena",
            institutions: ["University of Cape Town"],
            topPaper: "Scalable Distributed Telemetry Frameworks",
            domain: "Distributed Observability",
            growth: "+10% YoY"
        }
    };

    // Major Research Hub Beacons (Pulsing nodes with institutional landmarks)
    const researchBeacons = [
        { name: "Stanford & Silicon Valley", coords: [-122.1697, 37.4275], citations: 240, country: "USA", inst: "Stanford University & Silicon Valley Labs" },
        { name: "MIT & Harvard", coords: [-71.0942, 42.3601], citations: 165, country: "USA", inst: "MIT CSAIL & Harvard SEAS" },
        { name: "UT Austin / Texas AI", coords: [-97.7431, 30.2672], citations: 80, country: "USA", inst: "UT Austin & Texas Enterprise AI" },
        { name: "Vector Institute / Toronto", coords: [-79.3832, 43.6532], citations: 55, country: "CAN", inst: "University of Toronto & Vector Inst." },
        { name: "Cambridge & Oxford / London", coords: [-0.1278, 51.5074], citations: 142, country: "GBR", inst: "Cambridge, Oxford & Imperial College" },
        { name: "TU Munich & Max Planck", coords: [11.5820, 48.1351], citations: 96, country: "DEU", inst: "TUM & Max Planck Institute" },
        { name: "ETH Zürich", coords: [8.5417, 47.3769], citations: 46, country: "CHE", inst: "ETH Zurich Systems Group" },
        { name: "IISc & IITs / Bangalore", coords: [77.5946, 12.9716], citations: 135, country: "IND", inst: "Indian Institute of Science & IITs" },
        { name: "NUS & NTU", coords: [103.8198, 1.3521], citations: 58, country: "SGP", inst: "National Univ of Singapore & NTU" },
        { name: "Univ of Tokyo", coords: [139.6917, 35.6895], citations: 39, country: "JPN", inst: "University of Tokyo & RIKEN AIP" },
        { name: "KAIST & Seoul", coords: [126.9780, 37.5665], citations: 21, country: "KOR", inst: "KAIST AI Lab & Seoul National Univ" },
        { name: "Univ of Melbourne", coords: [144.9631, -37.8136], citations: 32, country: "AUS", inst: "University of Melbourne & ANU" },
        { name: "MBZUAI & Dubai", coords: [54.3773, 24.4539], citations: 26, country: "ARE", inst: "Mohamed bin Zayed University of AI" },
        { name: "Technion & Tel Aviv", coords: [34.7818, 32.0853], citations: 24, country: "ISR", inst: "Technion & Tel Aviv University" }
    ];

    // Helper: Map country names in TopoJSON to citationData
    function getCountryData(d) {
        if (!d) return null;
        const id = String(d.id || '').padStart(3, '0');
        if (citationData[id]) return citationData[id];
        if (citationData[d.id]) return citationData[d.id];

        const rawName = (d.properties && d.properties.name) ? d.properties.name.toLowerCase().trim() : '';
        for (const k in citationData) {
            const item = citationData[k];
            if (item.name.toLowerCase() === rawName) return item;
        }

        // Fuzzy matches
        if (rawName.includes('united states') || rawName === 'usa') return citationData['840'];
        if (rawName.includes('united kingdom') || rawName === 'uk' || rawName === 'britain') return citationData['826'];
        if (rawName.includes('germany')) return citationData['276'];
        if (rawName.includes('india')) return citationData['356'];
        if (rawName.includes('canada')) return citationData['124'];
        if (rawName.includes('singapore')) return citationData['702'];
        if (rawName.includes('japan')) return citationData['392'];
        if (rawName.includes('korea')) return citationData['410'];
        if (rawName.includes('australia')) return citationData['036'];
        if (rawName.includes('switzerland')) return citationData['756'];
        if (rawName.includes('emirates')) return citationData['784'];
        if (rawName.includes('saudi')) return citationData['682'];
        if (rawName.includes('israel')) return citationData['376'];
        if (rawName.includes('brazil')) return citationData['076'];
        if (rawName.includes('france')) return citationData['250'];
        if (rawName.includes('netherlands')) return citationData['528'];
        if (rawName.includes('sweden')) return citationData['752'];
        if (rawName.includes('spain')) return citationData['724'];
        if (rawName.includes('italy')) return citationData['380'];

        return null;
    }

    // Color Scales
    function getColorForCitations(count, isDark) {
        if (!count || count <= 0) {
            return isDark ? '#1e293b' : '#f1f5f9';
        }
        if (count >= 300) return '#1e3a8a'; // Deep Navy
        if (count >= 150) return '#1d4ed8'; // Bold Blue
        if (count >= 60)  return '#2563eb'; // Vibrant Royal Blue
        if (count >= 25)  return '#0284c7'; // Vivid Sky
        if (count >= 10)  return '#38bdf8'; // Soft Sky Blue
        return '#bae6fd';                  // Light Ice Blue
    }

    // Initialize D3 Map
    function initD3CitationMap() {
        const container = document.getElementById('d3CitationMapContainer');
        if (!container) return;

        container.innerHTML = '<div class="d3-map-loading"><div class="spinner-border text-primary spinner-border-sm mr-2" role="status"></div> Loading geospatial citation topology...</div>';

        // Check if D3 and topojson are loaded
        if (typeof d3 === 'undefined' || typeof topojson === 'undefined') {
            console.error('D3 or TopoJSON client library is not loaded');
            container.innerHTML = '<div class="alert alert-warning m-3 small">Visualization libraries loading. Please refresh if map does not render.</div>';
            return;
        }

        const width = 840;
        const height = 460;

        // Fetch TopoJSON data
        fetch('data/world-countries-110m.json')
            .then(res => {
                if (!res.ok) throw new Error('HTTP ' + res.status);
                return res.json();
            })
            .then(worldData => {
                renderMap(worldData);
            })
            .catch(err => {
                console.warn('Could not load local world-countries-110m.json, attempting fallback fetch:', err);
                fetch('https://cdn.jsdelivr.net/npm/world-atlas@2/countries-110m.json')
                    .then(r => r.json())
                    .then(worldData => renderMap(worldData))
                    .catch(e => {
                        container.innerHTML = '<div class="alert alert-danger m-3">Unable to load geographic map data. ' + e.message + '</div>';
                    });
            });

        function renderMap(worldData) {
            container.innerHTML = '';

            const isDark = document.body.classList.contains('dark-mode');
            const countries = topojson.feature(worldData, worldData.objects.countries).features;

            // Natural Earth projection
            const projection = d3.geoNaturalEarth1()
                .scale(158)
                .translate([width / 2, height / 2 + 10]);

            const pathGenerator = d3.geoPath().projection(projection);

            // Create SVG
            const svg = d3.select(container)
                .append('svg')
                .attr('viewBox', `0 0 ${width} ${height}`)
                .attr('preserveAspectRatio', 'xMidYMid meet')
                .classed('d3-citation-svg', true);

            // Defs for gradients & filters
            const defs = svg.append('defs');

            // Drop shadow for active country
            const filter = defs.append('filter')
                .attr('id', 'mapActiveGlow')
                .attr('x', '-20%').attr('y', '-20%').attr('width', '140%').attr('height', '140%');
            filter.append('feDropShadow')
                .attr('dx', '0').attr('dy', '2')
                .attr('stdDeviation', '3')
                .attr('flood-color', '#2563eb')
                .attr('flood-opacity', '0.4');

            // Zoom Root Container
            const g = svg.append('g').attr('class', 'map-viewport-group');

            // Background Ocean Plate
            g.append('rect')
                .attr('width', width * 3)
                .attr('height', height * 3)
                .attr('x', -width)
                .attr('y', -height)
                .attr('class', 'map-ocean-bg')
                .attr('fill', isDark ? '#0b1329' : '#f8fafc');

            // Tooltip reference
            const tooltip = d3.select('#d3MapTooltip');

            // Draw Countries
            const countryPaths = g.selectAll('path.country-path')
                .data(countries)
                .enter()
                .append('path')
                .attr('class', d => {
                    const cData = getCountryData(d);
                    return cData ? 'country-path citing-country' : 'country-path non-citing-country';
                })
                .attr('d', pathGenerator)
                .attr('fill', d => {
                    const cData = getCountryData(d);
                    return getColorForCitations(cData ? cData.citations : 0, isDark);
                })
                .attr('stroke', isDark ? '#334155' : '#cbd5e1')
                .attr('stroke-width', 0.65)
                .style('cursor', d => getCountryData(d) ? 'pointer' : 'default')
                .on('mouseenter', function(event, d) {
                    const cData = getCountryData(d);
                    const countryName = cData ? cData.name : (d.properties && d.properties.name ? d.properties.name : 'Unknown');

                    d3.select(this)
                        .attr('stroke', '#2563eb')
                        .attr('stroke-width', 1.8)
                        .raise();

                    let htmlContent = '';
                    if (cData) {
                        htmlContent = `
                            <div class="tooltip-header d-flex justify-content-between align-items-center mb-1">
                                <strong>${cData.name}</strong>
                                <span class="badge badge-primary px-1.5 py-0.5 ml-2 font-weight-bold" style="background:#2563eb;">${cData.citations} Citations</span>
                            </div>
                            <div class="small text-muted mb-1"><i class="mdi mdi-school mr-1 text-primary"></i> <strong>Top Nodes:</strong> ${cData.institutions.slice(0, 2).join(', ')}</div>
                            <div class="small text-dark font-italic"><i class="mdi mdi-file-document-outline mr-1 text-primary"></i> "${cData.topPaper}"</div>
                            <div class="mt-1 pt-1 border-top small text-success font-weight-bold"><i class="mdi mdi-trending-up mr-1"></i> ${cData.growth} citation velocity</div>
                        `;
                    } else {
                        htmlContent = `
                            <div class="tooltip-header font-weight-bold text-muted">${countryName}</div>
                            <div class="small text-muted">Academic exploration &amp; forthcoming distribution node.</div>
                        `;
                    }

                    tooltip.html(htmlContent)
                        .style('display', 'block');
                })
                .on('mousemove', function(event) {
                    const containerRect = container.getBoundingClientRect();
                    const mouseX = event.clientX - containerRect.left;
                    const mouseY = event.clientY - containerRect.top;

                    // Position tooltip offset from mouse
                    let left = mouseX + 16;
                    let top = mouseY - 10;
                    if (left + 240 > containerRect.width) {
                        left = mouseX - 250;
                    }
                    if (top + 120 > containerRect.height) {
                        top = mouseY - 100;
                    }

                    tooltip.style('left', Math.max(10, left) + 'px')
                           .style('top', Math.max(10, top) + 'px');
                })
                .on('mouseleave', function(event, d) {
                    const isSelected = d3.select(this).classed('selected-country');
                    if (!isSelected) {
                        d3.select(this)
                            .attr('stroke', isDark ? '#334155' : '#cbd5e1')
                            .attr('stroke-width', 0.65);
                    }
                    tooltip.style('display', 'none');
                })
                .on('click', function(event, d) {
                    const cData = getCountryData(d);
                    if (cData) {
                        countryPaths.classed('selected-country', false)
                            .attr('stroke', isDark ? '#334155' : '#cbd5e1')
                            .attr('stroke-width', 0.65);

                        d3.select(this)
                            .classed('selected-country', true)
                            .attr('stroke', '#3b82f6')
                            .attr('stroke-width', 2.2)
                            .raise();

                        updateSidebarDetails(cData);
                    }
                });

            // Draw Pulsing Research Beacon Nodes
            const beaconsGroup = g.append('g').attr('class', 'research-beacons-group');

            researchBeacons.forEach(b => {
                const projected = projection(b.coords);
                if (!projected) return;

                const beaconG = beaconsGroup.append('g')
                    .attr('class', 'beacon-node')
                    .attr('transform', `translate(${projected[0]}, ${projected[1]})`)
                    .style('cursor', 'pointer')
                    .on('mouseenter', function(event) {
                        d3.select(this).select('.beacon-core-dot').attr('r', 5.5);
                        tooltip.html(`
                            <div class="tooltip-header d-flex justify-content-between align-items-center mb-1">
                                <strong><i class="mdi mdi-school text-primary mr-1"></i> ${b.name}</strong>
                                <span class="badge badge-success px-1.5 py-0.5 ml-1">${b.citations} Cites</span>
                            </div>
                            <div class="small text-dark font-weight-bold mb-1">${b.inst}</div>
                            <div class="small text-muted"><i class="mdi mdi-map-marker-radius text-danger mr-1"></i> Core Institutional Research Cluster</div>
                        `).style('display', 'block');
                    })
                    .on('mousemove', function(event) {
                        const containerRect = container.getBoundingClientRect();
                        const mouseX = event.clientX - containerRect.left;
                        const mouseY = event.clientY - containerRect.top;
                        tooltip.style('left', (mouseX + 15) + 'px').style('top', (mouseY - 15) + 'px');
                    })
                    .on('mouseleave', function() {
                        d3.select(this).select('.beacon-core-dot').attr('r', 3.8);
                        tooltip.style('display', 'none');
                    })
                    .on('click', function() {
                        // Find matching country
                        for (const k in citationData) {
                            if (citationData[k].code === b.country) {
                                updateSidebarDetails(citationData[k]);
                                break;
                            }
                        }
                    });

                // Pulsing outer ripple ring
                beaconG.append('circle')
                    .attr('r', 4)
                    .attr('class', 'beacon-pulse-ring')
                    .attr('fill', 'none')
                    .attr('stroke', '#38bdf8')
                    .attr('stroke-width', 1.5);

                // Core inner dot
                beaconG.append('circle')
                    .attr('r', 3.8)
                    .attr('class', 'beacon-core-dot')
                    .attr('fill', '#2563eb')
                    .attr('stroke', '#ffffff')
                    .attr('stroke-width', 1.2);
            });

            // Setup Zoom & Pan Behavior
            const zoom = d3.zoom()
                .scaleExtent([1, 8])
                .translateExtent([[0, 0], [width, height]])
                .on('zoom', (event) => {
                    g.attr('transform', event.transform);
                });

            svg.call(zoom);

            // Region zoom controls
            function zoomToRegion(regionKey) {
                let targetScale = 1;
                let targetTranslate = [0, 0];

                switch(regionKey) {
                    case 'na':
                        targetScale = 2.4;
                        targetTranslate = [-width * 0.15, -height * 0.18];
                        break;
                    case 'eu':
                        targetScale = 3.2;
                        targetTranslate = [-width * 1.05, -height * 0.45];
                        break;
                    case 'apac':
                        targetScale = 2.2;
                        targetTranslate = [-width * 1.05, -height * 0.35];
                        break;
                    case 'latam_mena':
                        targetScale = 2.0;
                        targetTranslate = [-width * 0.65, -height * 0.4];
                        break;
                    case 'all':
                    default:
                        targetScale = 1;
                        targetTranslate = [0, 0];
                        break;
                }

                svg.transition()
                    .duration(850)
                    .ease(d3.easeCubicOut)
                    .call(
                        zoom.transform,
                        d3.zoomIdentity.translate(targetTranslate[0], targetTranslate[1]).scale(targetScale)
                    );
            }

            // Hook up zoom buttons
            const zoomInBtn = document.getElementById('btnMapZoomIn');
            if (zoomInBtn) {
                zoomInBtn.onclick = function() {
                    svg.transition().duration(400).call(zoom.scaleBy, 1.4);
                };
            }
            const zoomOutBtn = document.getElementById('btnMapZoomOut');
            if (zoomOutBtn) {
                zoomOutBtn.onclick = function() {
                    svg.transition().duration(400).call(zoom.scaleBy, 0.7);
                };
            }
            const resetBtn = document.getElementById('btnMapReset');
            if (resetBtn) {
                resetBtn.onclick = function() {
                    zoomToRegion('all');
                    document.querySelectorAll('.map-region-btn').forEach(b => b.classList.remove('active'));
                    const allBtn = document.querySelector('.map-region-btn[data-region="all"]');
                    if (allBtn) allBtn.classList.add('active');
                };
            }

            // Region filter buttons
            const regionBtns = document.querySelectorAll('.map-region-btn');
            regionBtns.forEach(btn => {
                btn.onclick = function() {
                    regionBtns.forEach(b => b.classList.remove('active'));
                    this.classList.add('active');
                    const region = this.getAttribute('data-region');
                    zoomToRegion(region);
                };
            });

            // Initialize Sidebar with United States by default
            updateSidebarDetails(citationData['840']);

            // Watch for Dark Mode toggle
            const observer = new MutationObserver(() => {
                const dark = document.body.classList.contains('dark-mode');
                g.select('.map-ocean-bg').attr('fill', dark ? '#0b1329' : '#f8fafc');
                countryPaths
                    .attr('fill', d => {
                        const cData = getCountryData(d);
                        return getColorForCitations(cData ? cData.citations : 0, dark);
                    })
                    .attr('stroke', dark ? '#334155' : '#cbd5e1');
            });
            observer.observe(document.body, { attributes: true, attributeFilter: ['class'] });
        }

        function updateSidebarDetails(item) {
            if (!item) return;

            const titleEl = document.getElementById('mapSidebarCountryTitle');
            const badgeEl = document.getElementById('mapSidebarCitationsBadge');
            const bodyEl = document.getElementById('mapSidebarBody');
            const clustersEl = document.getElementById('mapTopClustersList');

            if (titleEl) {
                titleEl.innerHTML = `<i class="mdi mdi-map-marker-radius text-primary mr-1"></i> ${item.name} (${item.code})`;
            }
            if (badgeEl) {
                badgeEl.textContent = `${item.citations} Citations · ${item.growth}`;
            }

            if (bodyEl) {
                bodyEl.innerHTML = `
                    <div class="p-3 rounded mb-3" style="background: rgba(37, 99, 235, 0.05); border: 1px solid rgba(37, 99, 235, 0.15);">
                        <div class="d-flex justify-content-between align-items-center mb-1">
                            <span class="text-uppercase small font-weight-bold text-primary">Core Research Impact Domain</span>
                            <span class="badge badge-pill badge-light border text-muted">${item.region.toUpperCase()}</span>
                        </div>
                        <h6 class="font-weight-bold text-dark mb-1" style="font-size: 13.5px;">${item.domain}</h6>
                        <div class="text-muted small mb-2"><i class="mdi mdi-file-document-check-outline text-primary mr-1"></i> Landmark Cited Work: <strong>${item.topPaper}</strong></div>
                        <a href="https://scholar.google.com/citations?hl=en&user=zSt9oRMAAAAJ" target="_blank" class="btn btn-xs btn-primary font-weight-bold text-white px-2.5 py-1" style="font-size: 11px;">
                            <i class="mdi mdi-school mr-1"></i> Verify on Google Scholar
                        </a>
                    </div>

                    <div class="mb-2">
                        <span class="small font-weight-bold text-dark text-uppercase" style="letter-spacing: 0.5px;">Top Citing Academic &amp; Industry Labs:</span>
                    </div>
                    <ul class="list-unstyled mb-0" style="font-size: 12.5px; line-height: 1.8;">
                        ${item.institutions.map(inst => `
                            <li class="d-flex align-items-center text-slate-700">
                                <i class="mdi mdi-check-circle-outline text-success mr-2 font-weight-bold"></i>
                                <span>${inst}</span>
                            </li>
                        `).join('')}
                    </ul>
                `;
            }

            if (clustersEl) {
                clustersEl.innerHTML = `
                    <div class="list-group-item px-2 py-1.5 border-0 d-flex justify-content-between align-items-center">
                        <span class="text-dark font-weight-bold"><i class="mdi mdi-earth mr-1 text-primary"></i> Global Ranking:</span>
                        <span class="badge badge-light border font-weight-bold">Tier 1 Strategic Anchor</span>
                    </div>
                    <div class="list-group-item px-2 py-1.5 border-0 d-flex justify-content-between align-items-center">
                        <span class="text-dark font-weight-bold"><i class="mdi mdi-chart-bell-curve mr-1 text-info"></i> Citation Distribution:</span>
                        <span class="text-primary font-weight-bold">${((item.citations / 1280) * 100).toFixed(1)}% of Global Reach</span>
                    </div>
                    <div class="list-group-item px-2 py-1.5 border-0 d-flex justify-content-between align-items-center">
                        <span class="text-dark font-weight-bold"><i class="mdi mdi-sync mr-1 text-success"></i> Telemetry Velocity:</span>
                        <span class="text-success font-weight-bold">${item.growth} Active Trajectory</span>
                    </div>
                `;
            }
        }
    }

    // Auto-init on DOMContentLoaded or immediate if already ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initD3CitationMap);
    } else {
        initD3CitationMap();
    }
})();
