import json
import re

with open('media_data.json', 'r') as f:
    media_items = json.load(f)

print(f"Loaded {len(media_items)} items from media_data.json.")

# Default featured items list (can be altered or cleared by user in browser via localStorage)
default_featured_ids = [
    "media-times-square-nyc",
    "media-business-insider-agentic",
    "media-berkeley-skydeck-genai",
    "media-hackernoon-interview-agentic",
    "media-usa-today-cybersecurity",
    "media-yahoo-finance-cloud-sec"
]

header_part = """<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-30250521-4"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'UA-30250521-4');
    </script>
    <meta charset="UTF-8">
    <title>Harsh Verma | Media, Press Features &amp; Keynote Appearances</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Explore 37+ media features, tier-1 press articles, keynote addresses, podcast interviews, and Times Square NYC broadcasts featuring Harsh Verma across Business Insider, USA Today, Yahoo Finance, HackerNoon, UC Berkeley SkyDeck, and Spotify." />
    <meta name="keywords" content="Harsh Verma, Media Coverage, Press Features, Business Insider, USA Today, Yahoo Finance, HackerNoon, UC Berkeley SkyDeck, Forttuna Global 100, Times Square NYC, Podcasts, Keynotes, Enterprise AI, Cybersecurity" />
    <meta content="Harsh Verma" name="author" />
    <meta property="og:title" content="Harsh Verma | Media, Press Features &amp; Keynote Appearances" />
    <meta property="og:description" content="Explore 37+ media features, tier-1 press articles, keynote addresses, podcast interviews, and Times Square NYC broadcasts featuring Harsh Verma." />
    <!-- favicon -->
    <link rel="shortcut icon" href="images/favicon_new.ico">
    <!-- Bootstrap -->
    <link href="css/bootstrap.min.css" rel="stylesheet" type="text/css" />
    <!-- Icons -->
    <link href="css/materialdesignicons.min.css" rel="stylesheet" type="text/css" />
    <!-- Main css File -->
    <link href="css/style.css" rel="stylesheet" type="text/css" />
    <!-- Dark Mode css File -->
    <link href="css/dark-mode.css" rel="stylesheet" type="text/css" />
    <!-- Chart.js for interactive graphs & analytics -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
    <script src="js/dark-mode.js"></script>
    
    <style>
        /* Modern Media Page Dedicated Styles */
        .media-hero-section {
            position: relative;
            background: linear-gradient(135deg, #090e1a 0%, #0f172a 50%, #1e1b4b 100%);
            padding: 130px 0 85px;
            overflow: hidden;
            color: #ffffff;
        }
        .media-hero-bg-overlay {
            position: absolute;
            inset: 0;
            background-image: radial-gradient(circle at 15% 30%, rgba(37, 99, 235, 0.18) 0%, transparent 50%),
                              radial-gradient(circle at 85% 70%, rgba(245, 158, 11, 0.15) 0%, transparent 50%);
            pointer-events: none;
        }
        .media-hero-section::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 40px;
            background: linear-gradient(to top, #f8fafc, transparent);
            pointer-events: none;
        }
        body.dark-mode .media-hero-section::after {
            background: linear-gradient(to top, #0f172a, transparent);
        }

        .media-hero-badge-pill {
            background: linear-gradient(135deg, rgba(37, 99, 235, 0.25) 0%, rgba(147, 51, 234, 0.35) 100%);
            border: 1px solid rgba(96, 165, 250, 0.5);
            color: #93c5fd;
            font-size: 13px;
            font-weight: 700;
            letter-spacing: 1px;
            text-transform: uppercase;
            padding: 6px 18px;
            border-radius: 30px;
            display: inline-block;
        }

        /* Stats Ribbon */
        .media-stats-box {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 20px;
            padding: 24px 20px;
            box-shadow: 0 15px 35px -5px rgba(15, 23, 42, 0.08);
            margin-top: -45px;
            position: relative;
            z-index: 10;
            transition: all 0.3s ease;
        }
        body.dark-mode .media-stats-box {
            background: #1e293b;
            border-color: #334155;
            box-shadow: 0 15px 35px -5px rgba(0, 0, 0, 0.4);
        }
        .media-stat-item {
            text-align: center;
            padding: 8px 6px;
            cursor: pointer;
            transition: transform 0.2s ease;
            border-radius: 12px;
        }
        .media-stat-item:hover {
            transform: translateY(-3px);
            background: rgba(37, 99, 235, 0.04);
        }
        body.dark-mode .media-stat-item:hover {
            background: rgba(255, 255, 255, 0.04);
        }
        .media-stat-number {
            font-size: 30px;
            font-weight: 800;
            line-height: 1.1;
            margin-bottom: 4px;
            letter-spacing: -0.5px;
            background: linear-gradient(135deg, #2563eb 0%, #d97706 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .media-stat-label {
            font-size: 12px;
            color: #64748b;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        body.dark-mode .media-stat-label {
            color: #94a3b8;
        }

        /* Interactive Analytics Dashboard */
        .analytics-panel {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 20px;
            padding: 28px 24px;
            margin-bottom: 32px;
            box-shadow: 0 10px 30px rgba(15, 23, 42, 0.05);
            transition: all 0.3s ease;
        }
        body.dark-mode .analytics-panel {
            background: #1e293b;
            border-color: #334155;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        }
        .chart-card {
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 16px;
            padding: 20px;
            height: 100%;
            display: flex;
            flex-direction: column;
            transition: all 0.25s ease;
        }
        .chart-card:hover {
            border-color: #3b82f6;
            box-shadow: 0 6px 20px rgba(37, 99, 235, 0.08);
        }
        body.dark-mode .chart-card {
            background: #0f172a;
            border-color: #334155;
        }
        body.dark-mode .chart-card:hover {
            border-color: #60a5fa;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
        }
        .chart-title {
            font-size: 14.5px;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 6px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        body.dark-mode .chart-title {
            color: #f8fafc;
        }
        .chart-subtitle {
            font-size: 12px;
            color: #64748b;
            margin-bottom: 14px;
        }
        body.dark-mode .chart-subtitle {
            color: #94a3b8;
        }
        .chart-canvas-wrap {
            position: relative;
            flex-grow: 1;
            min-height: 220px;
            width: 100%;
        }

        /* Spotlight Landmark Banner */
        .spotlight-banner {
            background: linear-gradient(135deg, #1e1b4b 0%, #172554 50%, #090e1a 100%);
            border: 2px solid #f59e0b;
            border-radius: 20px;
            padding: 30px;
            margin-bottom: 35px;
            position: relative;
            overflow: hidden;
            box-shadow: 0 20px 40px -10px rgba(245, 158, 11, 0.2);
        }
        .spotlight-banner-badge {
            background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
            color: #ffffff;
            font-size: 11.5px;
            font-weight: 800;
            letter-spacing: 1px;
            text-transform: uppercase;
            padding: 4px 14px;
            border-radius: 20px;
            display: inline-block;
            margin-bottom: 12px;
        }

        /* Search & Filter Bar */
        .search-container {
            position: relative;
            max-width: 680px;
            margin: 0 auto 24px;
        }
        .search-input-field {
            width: 100%;
            padding: 15px 22px 15px 50px;
            border-radius: 50px;
            border: 1.5px solid #cbd5e1;
            font-size: 15.5px;
            background: #ffffff;
            color: #1e293b;
            box-shadow: 0 4px 18px rgba(15, 23, 42, 0.05);
            transition: all 0.25s ease;
        }
        .search-input-field:focus {
            outline: none;
            border-color: #2563eb;
            box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.18);
        }
        .search-icon-inside {
            position: absolute;
            left: 20px;
            top: 50%;
            transform: translateY(-50%);
            color: #94a3b8;
            font-size: 20px;
            pointer-events: none;
        }
        .search-clear-btn {
            position: absolute;
            right: 18px;
            top: 50%;
            transform: translateY(-50%);
            background: #e2e8f0;
            border: none;
            width: 26px;
            height: 26px;
            border-radius: 50%;
            display: none;
            align-items: center;
            justify-content: center;
            color: #475569;
            cursor: pointer;
            transition: background 0.2s;
        }
        .search-clear-btn:hover {
            background: #cbd5e1;
            color: #0f172a;
        }

        .filter-pill-row {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            justify-content: center;
            margin-bottom: 16px;
        }
        .btn-filter-pill {
            background: #ffffff;
            border: 1px solid #cbd5e1;
            color: #475569;
            padding: 8px 18px;
            border-radius: 30px;
            font-size: 13.5px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }
        .btn-filter-pill:hover {
            background: #f1f5f9;
            color: #1e293b;
            border-color: #94a3b8;
        }
        .btn-filter-pill.active {
            background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
            color: #ffffff !important;
            border-color: #2563eb;
            box-shadow: 0 4px 14px rgba(37, 99, 235, 0.3);
        }
        .btn-filter-pill.btn-filter-featured.active {
            background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
            color: #ffffff !important;
            border-color: #f59e0b;
            box-shadow: 0 4px 14px rgba(245, 158, 11, 0.35);
        }
        .filter-count-badge {
            background: rgba(0, 0, 0, 0.08);
            padding: 2px 7px;
            border-radius: 12px;
            font-size: 11.5px;
        }
        .btn-filter-pill.active .filter-count-badge {
            background: rgba(255, 255, 255, 0.25);
            color: #ffffff;
        }

        /* Topic Quick Pills */
        .topic-pill-row {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            justify-content: center;
            margin-bottom: 24px;
        }
        .btn-topic-pill {
            background: transparent;
            border: 1px dashed #cbd5e1;
            color: #64748b;
            padding: 5px 14px;
            border-radius: 20px;
            font-size: 12.5px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .btn-topic-pill:hover {
            background: #f1f5f9;
            color: #0f172a;
            border-color: #3b82f6;
        }
        .btn-topic-pill.active {
            background: #eff6ff;
            color: #1d4ed8;
            border: 1px solid #3b82f6;
            font-weight: 700;
        }

        /* View Mode Controls */
        .view-controls-bar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 12px;
            margin-bottom: 24px;
            padding: 12px 18px;
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 14px;
        }
        body.dark-mode .view-controls-bar {
            background: #1e293b;
            border-color: #334155;
        }

        /* Card Architecture */
        .media-card {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 18px;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            height: 100%;
            position: relative;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            box-shadow: 0 4px 16px rgba(15, 23, 42, 0.04);
        }
        .media-card:hover {
            transform: translateY(-6px);
            box-shadow: 0 20px 35px -10px rgba(15, 23, 42, 0.12), 0 8px 16px -6px rgba(15, 23, 42, 0.06) !important;
            border-color: rgba(37, 99, 235, 0.4);
        }

        /* Starred / Featured Card Styling */
        .media-card.is-featured-card {
            border: 2px solid #f59e0b !important;
            box-shadow: 0 12px 30px -5px rgba(245, 158, 11, 0.22) !important;
        }
        .featured-ribbon-badge {
            position: absolute;
            top: 10px;
            left: 10px;
            background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
            color: #ffffff;
            font-size: 11px;
            font-weight: 800;
            letter-spacing: 0.5px;
            text-transform: uppercase;
            padding: 3px 10px;
            border-radius: 12px;
            z-index: 9;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
            display: none;
            align-items: center;
            gap: 4px;
        }
        .media-card.is-featured-card .featured-ribbon-badge {
            display: inline-flex;
        }

        /* Star Button on Each Card */
        .btn-star-card {
            position: absolute;
            top: 10px;
            right: 10px;
            z-index: 10;
            width: 36px;
            height: 36px;
            border-radius: 50%;
            border: 1px solid rgba(255, 255, 255, 0.45);
            background: rgba(15, 23, 42, 0.8);
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            color: #cbd5e1;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
            cursor: pointer;
            transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
            box-shadow: 0 4px 12px rgba(0,0,0,0.25);
            outline: none !important;
        }
        .btn-star-card:hover {
            background: #f59e0b;
            color: #ffffff;
            transform: scale(1.15);
            border-color: #fbbf24;
            box-shadow: 0 0 16px rgba(245, 158, 11, 0.6);
        }
        .media-card.is-featured-card .btn-star-card {
            background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
            color: #ffffff;
            border-color: #fde047;
            box-shadow: 0 0 14px rgba(245, 158, 11, 0.55);
        }

        .media-header-badge {
            position: relative;
            width: 100%;
            height: 185px;
            background: #090e1a;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .media-header-badge img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center;
            display: block;
            transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .media-card:hover .media-header-badge img {
            transform: scale(1.05);
        }
        .media-type-pill {
            position: absolute;
            bottom: 10px;
            right: 12px;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 0.5px;
            text-transform: uppercase;
            box-shadow: 0 4px 12px rgba(0,0,0,0.4);
            z-index: 5;
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
        }
        .media-year-pill {
            position: absolute;
            top: 10px;
            left: 12px;
            background: rgba(15, 23, 42, 0.88);
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.25);
            color: #f8fafc;
            padding: 3px 10px;
            border-radius: 12px;
            font-size: 11px;
            font-weight: 600;
            z-index: 5;
        }
        .media-card.is-featured-card .media-year-pill {
            left: auto;
            right: 54px;
        }
        .media-outlet-overlay {
            position: absolute;
            bottom: 10px;
            left: 12px;
            background: rgba(15, 23, 42, 0.88);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #93c5fd;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 0.5px;
            text-transform: uppercase;
            padding: 3px 10px;
            border-radius: 6px;
            z-index: 5;
        }

        .media-card-body {
            padding: 22px 20px 20px;
            display: flex;
            flex-direction: column;
            flex-grow: 1;
        }
        .media-item-title {
            font-size: 18px;
            font-weight: 700;
            line-height: 1.35;
            color: #0f172a;
            margin-bottom: 10px;
            transition: color 0.2s ease;
        }
        .media-card:hover .media-item-title {
            color: #2563eb;
        }
        body.dark-mode .media-item-title {
            color: #f8fafc;
        }
        body.dark-mode .media-card:hover .media-item-title {
            color: #60a5fa;
        }

        .media-quote-box {
            background: #f8fafc;
            border-left: 3px solid #3b82f6;
            padding: 8px 12px;
            border-radius: 0 8px 8px 0;
            font-style: italic;
            font-size: 13px;
            color: #475569;
            line-height: 1.45;
            margin-bottom: 12px;
        }
        body.dark-mode .media-quote-box {
            background: #0f172a;
            border-color: #60a5fa;
            color: #cbd5e1;
        }

        .media-summary-text {
            font-size: 13.5px;
            color: #64748b;
            line-height: 1.55;
            margin-bottom: 14px;
            flex-grow: 1;
        }
        body.dark-mode .media-summary-text {
            color: #94a3b8;
        }

        .media-tags-wrap {
            display: flex;
            flex-wrap: wrap;
            gap: 5px;
            margin-bottom: 16px;
        }
        .media-tag-chip {
            background: #f1f5f9;
            color: #475569;
            border: 1px solid #e2e8f0;
            font-size: 11px;
            font-weight: 600;
            padding: 3px 8px;
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.2s;
        }
        .media-tag-chip:hover {
            background: #e0e7ff;
            color: #3730a3;
            border-color: #c7d2fe;
        }
        body.dark-mode .media-tag-chip {
            background: #0f172a;
            color: #cbd5e1;
            border-color: #334155;
        }
        body.dark-mode .media-tag-chip:hover {
            background: #1e3a8a;
            color: #93c5fd;
            border-color: #60a5fa;
        }

        .media-actions-bar {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: auto;
            padding-top: 14px;
            border-top: 1px solid #f1f5f9;
        }
        body.dark-mode .media-actions-bar {
            border-top-color: #334155;
        }

        .btn-media-primary {
            background: #f8fafc;
            color: #1e293b;
            border: 1px solid #cbd5e1;
            font-size: 12.5px;
            font-weight: 600;
            padding: 6px 12px;
            border-radius: 8px;
            display: inline-flex;
            align-items: center;
            gap: 5px;
            transition: all 0.2s ease;
            text-decoration: none;
        }
        .btn-media-primary:hover {
            background: #2563eb;
            color: #ffffff !important;
            border-color: #2563eb;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25);
        }
        body.dark-mode .btn-media-primary {
            background: #1e293b;
            color: #f1f5f9;
            border-color: #475569;
        }
        body.dark-mode .btn-media-primary:hover {
            background: #2563eb;
            color: #ffffff !important;
            border-color: #2563eb;
        }

        .btn-cite-media {
            background: transparent;
            border: 1px dashed #cbd5e1;
            color: #64748b;
            font-size: 12px;
            font-weight: 600;
            padding: 6px 10px;
            border-radius: 8px;
            display: inline-flex;
            align-items: center;
            gap: 4px;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .btn-cite-media:hover {
            background: #f1f5f9;
            color: #1e293b;
            border-color: #94a3b8;
        }
        body.dark-mode .btn-cite-media {
            border-color: #475569;
            color: #94a3b8;
        }
        body.dark-mode .btn-cite-media:hover {
            background: #334155;
            color: #f8fafc;
        }

        /* Compact Timeline List Mode */
        .media-list-mode .media-card-col {
            flex: 0 0 100%;
            max-width: 100%;
        }
        .media-list-mode .media-card {
            flex-direction: row;
        }
        .media-list-mode .media-header-badge {
            width: 260px;
            height: auto;
            min-height: 180px;
            flex-shrink: 0;
        }
        @media (max-width: 768px) {
            .media-list-mode .media-card {
                flex-direction: column;
            }
            .media-list-mode .media-header-badge {
                width: 100%;
                height: 180px;
            }
        }

        /* Dark Mode Overrides */
        body.dark-mode .media-card {
            background: #1e293b;
            border-color: #334155;
        }
        body.dark-mode .media-card:hover {
            border-color: #38bdf8;
            box-shadow: 0 20px 35px -10px rgba(0, 0, 0, 0.6) !important;
        }
        body.dark-mode .btn-filter-pill {
            background: #1e293b;
            border-color: #334155;
            color: #cbd5e1;
        }
        body.dark-mode .btn-filter-pill:hover {
            background: #334155;
            color: #93c5fd;
            border-color: #3b82f6;
        }
        body.dark-mode .btn-filter-pill.active {
            background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
            color: #ffffff !important;
            border-color: #2563eb;
        }
        body.dark-mode .search-input-field {
            background: #1e293b;
            border-color: #334155;
            color: #f8fafc;
        }
        body.dark-mode .search-input-field:focus {
            border-color: #38bdf8;
            box-shadow: 0 0 0 4px rgba(56, 189, 248, 0.2);
        }

        /* Navbar Header & Nav Link Visibility */
        .navbar-custom {
            background-color: rgba(255, 255, 255, 0.96) !important;
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            box-shadow: 0 4px 20px rgba(15, 23, 42, 0.06);
            border-bottom: 1px solid rgba(226, 232, 240, 0.8);
            padding: 16px 0;
            transition: all 0.3s ease;
        }
        .navbar-custom .navigation .navbar-nav-link .nav-item .nav-link {
            color: #334155 !important;
            font-weight: 600;
            font-size: 14.5px;
            transition: color 0.2s ease;
        }
        .navbar-custom .navigation .navbar-nav-link .nav-item:hover .nav-link,
        .navbar-custom .navigation .navbar-nav-link .nav-item.active .nav-link {
            color: #2563eb !important;
            font-weight: 700;
        }
        body.dark-mode .navbar-custom {
            background-color: rgba(11, 15, 25, 0.96) !important;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
        }
        body.dark-mode .navbar-custom .navigation .navbar-nav-link .nav-item .nav-link {
            color: #cbd5e1 !important;
        }
        body.dark-mode .navbar-custom .navigation .navbar-nav-link .nav-item:hover .nav-link,
        body.dark-mode .navbar-custom .navigation .navbar-nav-link .nav-item.active .nav-link {
            color: #60a5fa !important;
        }

        /* Toast notification */
        #citeToast {
            position: fixed;
            bottom: 25px;
            right: 25px;
            z-index: 9999;
            background: #1e1b4b;
            color: #ffffff;
            padding: 14px 22px;
            border-radius: 12px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
            border: 1px solid #4338ca;
            display: none;
            align-items: center;
            gap: 10px;
            font-size: 14px;
            font-weight: 600;
        }
    </style>
    <!-- HV AI Copilot Styles -->
    <link rel="stylesheet" href="css/hv-copilot.css" />
    <!-- HV Executive Keynote Hub & Speaking Booking Flow Styles -->
    <link rel="stylesheet" href="css/hv-keynote-hub.css" />
</head>

<body>
    <!-- Navbar Start -->
    <nav class="navbar navbar-expand-lg fixed-top navbar-custom navbar-light sticky" id="navbar">
        <div class="container">
            <a class="navbar-brand brand-logo-wrap" href="index" title="Harsh Verma - Home">
                <span class="brand-monogram-emblem">
                    <svg class="brand-logo-svg" width="34" height="34" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <defs>
                            <linearGradient id="hvNavGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                                <stop offset="0%" stop-color="#1e40af" />
                                <stop offset="55%" stop-color="#2563eb" />
                                <stop offset="100%" stop-color="#4f46e5" />
                            </linearGradient>
                            <linearGradient id="hvNavAccentGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                                <stop offset="0%" stop-color="#38bdf8" />
                                <stop offset="100%" stop-color="#818cf8" />
                            </linearGradient>
                        </defs>
                        <rect width="40" height="40" rx="10" fill="url(#hvNavGrad)" />
                        <rect x="0.75" y="0.75" width="38.5" height="38.5" rx="9.25" stroke="rgba(255,255,255,0.22)" stroke-width="1.5" />
                        <path d="M11 12V28M11 20H19M19 12V28" stroke="#ffffff" stroke-width="2.75" stroke-linecap="round" stroke-linejoin="round"/>
                        <path d="M23 12L28.5 28L34 12" stroke="url(#hvNavAccentGrad)" stroke-width="2.75" stroke-linecap="round" stroke-linejoin="round"/>
                        <circle cx="34" cy="12" r="1.75" fill="#38bdf8" />
                    </svg>
                </span>
                <span class="brand-name-text">
                    <span class="brand-first-name">Harsh</span><span class="brand-last-name">Verma</span>
                </span>
            </a>

            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
                <i class="mdi mdi-menu"></i>
            </button>

            <div class="collapse navbar-collapse" id="navbarCollapse">
                <ul class="navbar-nav ml-auto navbar-center" id="mySidenav">
                    <li class="nav-item">
                        <a class="nav-link" href="page-about">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="page-publications">Publications</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="page-awards">Awards</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="page-memberships">Memberships</a>
                    </li>
                    <li class="nav-item active">
                        <a class="nav-link" href="page-media">Media</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="page-events">Speaker</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="page-books">Books</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="page-blog">Blog</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="javascript:void(0)" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            More <i class="mdi mdi-chevron-down nav-dropdown-arrow"></i>
                        </a>
                        <div class="dropdown-menu dropdown-menu-right nav-custom-dropdown" aria-labelledby="navbarDropdown">
                            <div class="nav-dropdown-header">
                                <span>Extended Portfolios &amp; Hubs</span>
                            </div>
                            <a class="dropdown-item nav-dropdown-item" href="page-portfolio">
                                <div class="dropdown-item-icon bg-soft-info"><i class="mdi mdi-cube-outline"></i></div>
                                <div class="dropdown-item-content">
                                    <span class="dropdown-item-title">Portfolio Projects</span>
                                    <span class="dropdown-item-desc">Architectures, agent frameworks &amp; systems</span>
                                </div>
                            </a>
                            <a class="dropdown-item nav-dropdown-item" href="page-social">
                                <div class="dropdown-item-icon bg-soft-success"><i class="mdi mdi-share-variant"></i></div>
                                <div class="dropdown-item-content">
                                    <span class="dropdown-item-title">Social &amp; Routine <span class="badge badge-pill badge-primary ml-1" style="font-size: 10px;">Feed</span></span>
                                    <span class="dropdown-item-desc">LinkedIn &amp; Instagram routine updates</span>
                                </div>
                            </a>
                            <a class="dropdown-item nav-dropdown-item" href="page-about#verified-profiles">
                                <div class="dropdown-item-icon bg-soft-warning"><i class="mdi mdi-shield-account-outline"></i></div>
                                <div class="dropdown-item-content">
                                    <span class="dropdown-item-title">38 Verified Profiles Hub</span>
                                    <span class="dropdown-item-desc">Academic, editorial &amp; executive registries</span>
                                </div>
                            </a>
                            <div class="dropdown-divider my-2"></div>
                            <a class="dropdown-item nav-dropdown-item" href="index#contact">
                                <div class="dropdown-item-icon bg-soft-danger"><i class="mdi mdi-email-outline"></i></div>
                                <div class="dropdown-item-content">
                                    <span class="dropdown-item-title">Contact Harsh</span>
                                    <span class="dropdown-item-desc">Advisory, keynotes &amp; consultations</span>
                                </div>
                            </a>
                        </div>
                    </li>
                </ul>

                <ul class="top-right list-unstyled list-inline mb-0 ml-lg-3 nav-social d-flex align-items-center">
                    <li class="list-inline-item mr-2">
                        <a href="https://scholar.google.com/citations?hl=en&user=zSt9oRMAAAAJ" target="_blank" class="nav-social-btn" title="Google Scholar (22+ Papers)">
                            <i class="mdi mdi-school"></i>
                        </a>
                    </li>
                    <li class="list-inline-item mr-2">
                        <a href="https://www.linkedin.com/in/harshverma59/" target="_blank" class="nav-social-btn" title="LinkedIn Profile">
                            <i class="mdi mdi-linkedin"></i>
                        </a>
                    </li>
                    <li class="list-inline-item mr-2">
                        <a href="https://www.instagram.com/iamharshverma/" target="_blank" class="nav-social-btn" title="Instagram Profile">
                            <i class="mdi mdi-instagram"></i>
                        </a>
                    </li>
                    <li class="list-inline-item mr-2">
                        <a href="https://github.com/iamharshverma" target="_blank" class="nav-social-btn" title="GitHub Profile">
                            <i class="mdi mdi-github-face"></i>
                        </a>
                    </li>
                    <li class="list-inline-item">
                        <button type="button" class="theme-toggle-btn" id="theme-toggle" aria-label="Toggle dark mode" title="Toggle theme">
                            <svg class="icon-moon" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
                            <svg class="icon-sun" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
                        </button>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <!-- Navbar End -->

    <!-- Hero Header Start -->
    <section class="media-hero-section">
        <div class="media-hero-bg-overlay"></div>
        <div class="container position-relative" style="z-index: 2;">
            <div class="row justify-content-center text-center">
                <div class="col-lg-10">
                    <span class="media-hero-badge-pill mb-3">
                        <i class="mdi mdi-newspaper-variant-outline mr-1"></i> PRESS &amp; BROADCAST ARCHIVE
                    </span>
                    <h1 class="display-4 font-weight-bold mb-3 text-white">Media Features, Press &amp; Thought Leadership</h1>
                    <p class="lead text-light mb-4" style="max-width: 820px; margin: 0 auto; opacity: 0.92; font-size: 17px; line-height: 1.6;">
                        A curated archive of <strong>37+</strong> international press coverages, keynote symposiums, executive podcasts, Times Square NYC billboard features, and technical interviews shaping enterprise AI architecture and cybersecurity.
                    </p>
                    <div class="d-flex justify-content-center flex-wrap gap-2 text-muted" style="gap: 12px; font-size: 13.5px;">
                        <span class="badge badge-pill badge-dark px-3 py-2 border border-secondary"><i class="mdi mdi-check-decagram text-primary mr-1"></i> Business Insider</span>
                        <span class="badge badge-pill badge-dark px-3 py-2 border border-secondary"><i class="mdi mdi-check-decagram text-primary mr-1"></i> USA Today</span>
                        <span class="badge badge-pill badge-dark px-3 py-2 border border-secondary"><i class="mdi mdi-check-decagram text-primary mr-1"></i> Yahoo Finance</span>
                        <span class="badge badge-pill badge-dark px-3 py-2 border border-secondary"><i class="mdi mdi-check-decagram text-primary mr-1"></i> HackerNoon</span>
                        <span class="badge badge-pill badge-dark px-3 py-2 border border-secondary"><i class="mdi mdi-check-decagram text-warning mr-1"></i> Times Square NYC</span>
                        <span class="badge badge-pill badge-dark px-3 py-2 border border-secondary"><i class="mdi mdi-check-decagram text-info mr-1"></i> Berkeley SkyDeck</span>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- Hero Header End -->

    <!-- Main Content Section -->
    <section class="section" style="padding-top: 0; padding-bottom: 90px;">
        <div class="container">
            <!-- Stats Ribbon with Quick-Filter Actions -->
            <div class="media-stats-box">
                <div class="row">
                    <div class="col-6 col-lg-3 media-stat-item border-right" onclick="setTypeFilter('all', document.querySelector('.btn-filter-pill'))" title="Click to view all media">
                        <div class="media-stat-number" id="totalMediaStat">37+</div>
                        <div class="media-stat-label">Total Media Features</div>
                    </div>
                    <div class="col-6 col-lg-3 media-stat-item border-right" onclick="setFeaturedOnlyFilter()" title="Click to view starred / featured cards">
                        <div class="media-stat-number" style="background: linear-gradient(135deg, #f59e0b, #d97706); -webkit-background-clip: text; -webkit-text-fill-color: transparent;" id="ribbonFeaturedCount">6</div>
                        <div class="media-stat-label">⭐ Pinned / Featured Picks</div>
                    </div>
                    <div class="col-6 col-lg-3 media-stat-item border-right" onclick="setTypeFilter('podcast', document.querySelector('.btn-filter-pill[data-type=\\'podcast\\']'))" title="Click to filter podcasts & keynotes">
                        <div class="media-stat-number">14+</div>
                        <div class="media-stat-label">Podcasts &amp; Keynotes</div>
                    </div>
                    <div class="col-6 col-lg-3 media-stat-item" onclick="setTypeFilter('press', document.querySelector('.btn-filter-pill[data-type=\\'press\\']'))" title="Click to filter tier-1 press">
                        <div class="media-stat-number" style="background: linear-gradient(135deg, #0ea5e9, #2563eb); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">100M+</div>
                        <div class="media-stat-label">Estimated Global Reach</div>
                    </div>
                </div>
            </div>

            <div class="mt-4"></div>

            <!-- Interactive Media & Impact Analytics Hub -->
            <div class="analytics-panel">
                <div class="d-flex align-items-center justify-content-between flex-wrap mb-3">
                    <div>
                        <h4 class="font-weight-bold mb-1 d-flex align-items-center" style="color: #0f172a;">
                            <i class="mdi mdi-chart-timeline-variant text-primary mr-2" style="font-size: 24px;"></i>
                            Media Intelligence &amp; Impact Analytics
                        </h4>
                        <p class="text-muted mb-0" style="font-size: 13.5px;">Interactive visualizations breaking down publication distribution, core research domains, and longitudinal reach velocity.</p>
                    </div>
                    <div class="mt-2 mt-md-0 d-flex align-items-center" style="gap: 8px;">
                        <span class="badge badge-light border text-muted px-2 py-1 small"><i class="mdi mdi-cursor-default-click-outline mr-1 text-primary"></i> Click any graph segment to filter cards below</span>
                        <button type="button" class="btn btn-sm btn-outline-secondary" onclick="toggleAnalyticsDashboard()" id="btnToggleAnalytics">
                            <i class="mdi mdi-chevron-up" id="toggleAnalyticsIcon"></i> Collapse
                        </button>
                    </div>
                </div>

                <div id="analyticsCollapseContainer">
                    <div class="row">
                        <!-- Chart 1: Format Distribution -->
                        <div class="col-lg-4 col-md-6 mb-4 mb-lg-0">
                            <div class="chart-card">
                                <div class="chart-title">
                                    <span><i class="mdi mdi-chart-donut text-primary mr-1"></i> Media by Format</span>
                                    <span class="badge badge-primary badge-pill font-weight-normal" style="font-size: 11px;">5 Formats</span>
                                </div>
                                <div class="chart-subtitle">Press, podcasts, keynotes &amp; interviews</div>
                                <div class="chart-canvas-wrap">
                                    <canvas id="mediaFormatChart"></canvas>
                                </div>
                            </div>
                        </div>

                        <!-- Chart 2: Research & Topic Domains -->
                        <div class="col-lg-4 col-md-6 mb-4 mb-lg-0">
                            <div class="chart-card">
                                <div class="chart-title">
                                    <span><i class="mdi mdi-chart-bar text-info mr-1"></i> Research &amp; Topic Pillars</span>
                                    <span class="badge badge-info badge-pill font-weight-normal" style="font-size: 11px;">Core Focus</span>
                                </div>
                                <div class="chart-subtitle">Key architectural &amp; industry topics</div>
                                <div class="chart-canvas-wrap">
                                    <canvas id="topicDomainChart"></canvas>
                                </div>
                            </div>
                        </div>

                        <!-- Chart 3: Longitudinal Coverage Velocity -->
                        <div class="col-lg-4 col-md-12">
                            <div class="chart-card">
                                <div class="chart-title">
                                    <span><i class="mdi mdi-trending-up text-warning mr-1"></i> Multi-Year Momentum</span>
                                    <span class="badge badge-warning badge-pill font-weight-normal" style="font-size: 11px;">2018–2026</span>
                                </div>
                                <div class="chart-subtitle">Annual volume &amp; tier-1 press velocity</div>
                                <div class="chart-canvas-wrap">
                                    <canvas id="timelineGrowthChart"></canvas>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Spotlight Landmark Banner -->
            <div class="spotlight-banner">
                <div class="row align-items-center">
                    <div class="col-lg-8">
                        <span class="spotlight-banner-badge"><i class="mdi mdi-star mr-1"></i> FEATURED LANDMARK SPOTLIGHT</span>
                        <h3 class="text-white font-weight-bold mb-2">Times Square NYC Broadcast &amp; Forttuna Global 100 Power List</h3>
                        <p class="text-light mb-3" style="opacity: 0.9; font-size: 14.5px; line-height: 1.6;">
                            Harsh Verma was inducted into the <strong>Forttuna Global 100: The Power List 2026</strong> alongside international industry leaders, broadcast across the giant Nasdaq &amp; Times Square billboards in New York City, and syndicated on <em>Business Insider</em>.
                        </p>
                        <div class="d-flex flex-wrap" style="gap: 10px;">
                            <a href="https://global100.forttuna.com/the-power-list-2026-honorees/profile?name=harsh-verma" target="_blank" rel="noopener noreferrer" class="btn btn-sm btn-warning font-weight-bold px-3 py-2">
                                <i class="mdi mdi-account-star mr-1"></i> View Global 100 Profile
                            </a>
                            <a href="https://markets.businessinsider.com/news/stocks/the-forttuna-group-announces-the-anniversary-edition-of-forttuna-global-100-the-power-list-2026-celebrating-leadership-beyond-boundaries-1036222228" target="_blank" rel="noopener noreferrer" class="btn btn-sm btn-outline-light font-weight-bold px-3 py-2">
                                <i class="mdi mdi-newspaper mr-1"></i> Read on Business Insider
                            </a>
                            <a href="https://global100.forttuna.com/the-power-list-2026-memories" target="_blank" rel="noopener noreferrer" class="btn btn-sm btn-outline-warning font-weight-bold px-3 py-2">
                                <i class="mdi mdi-camera mr-1"></i> Times Square Footage
                            </a>
                        </div>
                    </div>
                    <div class="col-lg-4 text-center mt-4 mt-lg-0">
                        <img src="images/media/timessquare_forttuna_badge.svg" alt="Times Square Forttuna Global 100" class="img-fluid rounded shadow-lg border border-warning" style="max-height: 190px;" />
                    </div>
                </div>
            </div>

            <!-- Search & Filtering Section -->
            <div class="search-container">
                <i class="mdi mdi-magnify search-icon-inside"></i>
                <input type="text" id="mediaSearchInput" class="search-input-field" placeholder="Search by publication, title, podcast topic, keynote, or keyword..." oninput="handleSearchInput(this.value)" />
                <button type="button" id="clearSearchBtn" class="search-clear-btn" onclick="clearSearch()" title="Clear search">
                    <i class="mdi mdi-close"></i>
                </button>
            </div>

            <!-- Primary Type Filter Pills -->
            <div class="filter-pill-row">
                <button type="button" class="btn-filter-pill active" onclick="setTypeFilter('all', this)">
                    <i class="mdi mdi-view-grid"></i> All Media <span class="filter-count-badge">37</span>
                </button>
                <button type="button" class="btn-filter-pill btn-filter-featured" id="filterPillFeatured" onclick="setTypeFilter('featured', this)">
                    <i class="mdi mdi-star text-warning"></i> ⭐ Featured &amp; Pinned <span class="filter-count-badge" id="featuredBadgeCount">6</span>
                </button>
                <button type="button" class="btn-filter-pill" data-type="press" onclick="setTypeFilter('press', this)">
                    <i class="mdi mdi-newspaper"></i> Top Tier Press <span class="filter-count-badge">12</span>
                </button>
                <button type="button" class="btn-filter-pill" data-type="podcast" onclick="setTypeFilter('podcast', this)">
                    <i class="mdi mdi-podcast"></i> Podcasts &amp; Shows <span class="filter-count-badge">8</span>
                </button>
                <button type="button" class="btn-filter-pill" data-type="keynote" onclick="setTypeFilter('keynote', this)">
                    <i class="mdi mdi-presentation"></i> Keynotes &amp; Talks <span class="filter-count-badge">6</span>
                </button>
                <button type="button" class="btn-filter-pill" data-type="interview" onclick="setTypeFilter('interview', this)">
                    <i class="mdi mdi-microphone-variant"></i> In-Depth Interviews <span class="filter-count-badge">8</span>
                </button>
                <button type="button" class="btn-filter-pill" data-type="institutional" onclick="setTypeFilter('institutional', this)">
                    <i class="mdi mdi-school"></i> Institutional <span class="filter-count-badge">3</span>
                </button>
            </div>

            <!-- Quick Topic Pills -->
            <div class="topic-pill-row">
                <span class="text-muted font-weight-bold mr-2 align-self-center" style="font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px;">Topic Quick-Filter:</span>
                <button type="button" class="btn-topic-pill active" onclick="setTopicFilter('all', this)">All Topics</button>
                <button type="button" class="btn-topic-pill" onclick="setTopicFilter('Agentic Security', this)">Agentic Security &amp; AI</button>
                <button type="button" class="btn-topic-pill" onclick="setTopicFilter('Global 100', this)">Global 100 &amp; Times Square</button>
                <button type="button" class="btn-topic-pill" onclick="setTopicFilter('Production AI', this)">Production AI &amp; Reliability</button>
                <button type="button" class="btn-topic-pill" onclick="setTopicFilter('Palo Alto Networks', this)">Palo Alto Networks</button>
                <button type="button" class="btn-topic-pill" onclick="setTopicFilter('Zero Trust', this)">Zero Trust &amp; Identity</button>
                <button type="button" class="btn-topic-pill" onclick="setTopicFilter('Spotify', this)">Spotify &amp; Podcasts</button>
            </div>

            <!-- Controls bar: Results count & View toggle & Pin Sort & Reset/Clear Pin buttons -->
            <div class="view-controls-bar">
                <div class="d-flex align-items-center flex-wrap" style="gap: 12px;">
                    <span class="font-weight-bold mr-2" style="font-size: 14.5px;">Showing <span id="visibleCount" class="text-primary font-weight-bold">37</span> of 37 Media Features</span>
                    <span class="badge badge-warning text-dark font-weight-bold px-2 py-1" style="font-size: 12px;" id="pinnedStatusBadge">
                        <i class="mdi mdi-pin mr-1"></i> <span id="pinnedStatusText">Pinned Cards On Top (6)</span>
                    </span>
                </div>
                <div class="d-flex align-items-center flex-wrap" style="gap: 10px;">
                    <!-- Pin Management Actions -->
                    <div id="pinActionButtons" class="d-flex align-items-center" style="gap: 8px;">
                        <button type="button" class="btn btn-sm btn-outline-danger" id="btnClearPins" onclick="clearAllFeatured()" title="Clear all pinned cards to 0">
                            <i class="mdi mdi-star-off-outline mr-1"></i> Clear Pins (<span id="btnClearPinCount">6</span>)
                        </button>
                        <button type="button" class="btn btn-sm btn-outline-warning text-dark font-weight-bold" id="btnRestoreDefaults" onclick="restoreDefaultFeatured()" title="Restore curated 6 editorial highlights">
                            <i class="mdi mdi-restore mr-1"></i> Restore Top 6 Picks
                        </button>
                    </div>

                    <div class="d-flex align-items-center">
                        <label for="sortSelect" class="small text-muted font-weight-bold mr-2 mb-0">Sort By:</label>
                        <select id="sortSelect" class="form-control form-control-sm" style="width: auto; border-radius: 8px;" onchange="applySorting(this.value)">
                            <option value="featured">Pinned on Top &amp; Newest First</option>
                            <option value="newest">Chronological (Newest 2026 First)</option>
                            <option value="outlet">Outlet (A - Z)</option>
                            <option value="title">Title (A - Z)</option>
                        </select>
                    </div>

                    <div class="btn-group btn-group-sm" role="group">
                        <button type="button" id="gridModeBtn" class="btn btn-outline-primary active" onclick="setViewMode('grid')" title="Card Grid View">
                            <i class="mdi mdi-view-grid"></i>
                        </button>
                        <button type="button" id="listModeBtn" class="btn btn-outline-primary" onclick="setViewMode('list')" title="Compact Timeline Mode">
                            <i class="mdi mdi-view-list"></i>
                        </button>
                    </div>
                </div>
            </div>

            <!-- Media Grid Container -->
            <div class="row" id="mediaGridContainer">
"""

card_elements = []

for item in media_items:
    mid = item['id']
    mtype = item['type']
    mtype_label = item.get('type_label', 'Press')
    myear = item['year']
    moutlet = item['outlet']
    mtitle = item['title']
    msummary = item['summary']
    mquote = item.get('quote', '')
    micon = item.get('icon_svg', 'business_insider_badge.svg')
    mhighlight = item.get('highlight', '')
    topics = item.get('topics', [])
    links = item.get('links', [])
    primary_url = item.get('primary_url', '#')

    # Color themes for badges
    tier_bg = "rgba(37, 99, 235, 0.9)"
    tier_color = "#ffffff"
    if mtype == 'press':
        tier_bg = "rgba(14, 116, 144, 0.95)"
    elif mtype == 'podcast':
        tier_bg = "rgba(225, 29, 72, 0.95)"
    elif mtype == 'keynote':
        tier_bg = "rgba(124, 58, 237, 0.95)"
    elif mtype == 'interview':
        tier_bg = "rgba(5, 150, 105, 0.95)"
    elif mtype == 'institutional':
        tier_bg = "rgba(217, 119, 6, 0.95)"

    search_keywords = f"{mtitle} {moutlet} {msummary} {myear} {mtype_label} {' '.join(topics)} {mquote}".lower()
    search_keywords = re.sub(r'[^a-z0-9 ]', ' ', search_keywords)

    topic_chips_html = "".join([f'<span class="media-tag-chip" onclick="filterByTag(\'{t}\')">{t}</span>' for t in topics])

    links_html = ""
    for l in links:
        icon_cls = l.get('icon', 'mdi-open-in-new')
        links_html += f'<a href="{l["url"]}" target="_blank" rel="noopener noreferrer" class="btn-media-primary"><i class="mdi {icon_cls}"></i> {l["label"]}</a>'

    esc_title = mtitle.replace('"', '&quot;').replace("'", "&#39;")
    esc_outlet = moutlet.replace('"', '&quot;').replace("'", "&#39;")
    esc_year = myear

    quote_html = f'<div class="media-quote-box">"{mquote}"</div>' if mquote else ''

    card_html = f"""
                <!-- Item: {mtitle} -->
                <div class="col-lg-4 col-md-6 mb-4 media-card-col" 
                     id="col-{mid}"
                     data-id="{mid}"
                     data-type="{mtype}" 
                     data-year="{myear}"
                     data-outlet="{moutlet.lower()}"
                     data-title="{mtitle.lower()}"
                     data-search="{search_keywords}">
                    <div class="media-card" id="card-{mid}">
                        <span class="featured-ribbon-badge">
                            <i class="mdi mdi-star"></i> Featured Highlight
                        </span>
                        <button type="button" class="btn-star-card" onclick="toggleFeatureCard(event, '{mid}')" title="Click to star / feature this card on top" aria-label="Feature card">
                            <i class="mdi mdi-star-outline" id="star-icon-{mid}"></i>
                        </button>
                        <div class="media-header-badge">
                            <img src="images/media/{micon}" alt="{esc_title}" loading="lazy" />
                            <span class="media-type-pill" style="background: {tier_bg}; color: {tier_color};">{mtype_label}</span>
                            <span class="media-year-pill">{myear}</span>
                            <span class="media-outlet-overlay">{moutlet}</span>
                        </div>
                        <div class="media-card-body">
                            <h3 class="media-item-title">{mtitle}</h3>
                            {quote_html}
                            <div class="media-tags-wrap">
                                {topic_chips_html}
                            </div>
                            <div class="media-actions-bar">
                                {links_html}
                                <button type="button" class="btn-cite-media" onclick="openMediaCiteModal('{esc_title}', '{esc_outlet}', '{esc_year}', '{primary_url}')" title="Copy Press Citation">
                                    <i class="mdi mdi-format-quote-close"></i> Cite
                                </button>
                            </div>
                        </div>
                    </div>
                </div>"""
    card_elements.append(card_html)

cards_full_html = "\n".join(card_elements)

footer_part = """
            </div> <!-- /row -->

            <!-- Empty State / No Results Container -->
            <div id="noMediaFound" class="text-center py-5" style="display: none;">
                <div class="py-4 px-3" style="max-width: 600px; margin: 0 auto; background: rgba(241, 245, 249, 0.6); border-radius: 20px; border: 1.5px dashed #cbd5e1;">
                    <i class="mdi mdi-star-off-outline text-warning" style="font-size: 54px;"></i>
                    <h4 class="font-weight-bold mt-2" id="noMediaTitle">No matching media features found</h4>
                    <p class="text-muted" id="noMediaDesc">Try adjusting your keyword search or resetting active filters.</p>
                    <div id="noMediaActions" class="mt-3 d-flex justify-content-center flex-wrap" style="gap: 10px;">
                        <button type="button" class="btn btn-primary btn-sm px-4 py-2" onclick="clearSearch()">
                            <i class="mdi mdi-refresh mr-1"></i> Reset All Filters
                        </button>
                    </div>
                </div>
            </div>

            <!-- Press & Media Kit Banner -->
            <div class="mt-5 p-4 rounded-lg bg-light border text-center text-md-left d-md-flex align-items-center justify-content-between" style="border-radius: 16px;">
                <div class="mb-3 mb-md-0">
                    <h4 class="font-weight-bold mb-1">Journalist, Conference Organizer or Podcast Host?</h4>
                    <p class="text-muted mb-0" style="font-size: 14.5px;">Looking for official speaker bios, high-res portraits, executive quotes, or keynote bookings?</p>
                </div>
                <div>
                    <a href="index#contact" class="btn btn-primary px-4 py-2 font-weight-bold">
                        <i class="mdi mdi-email-outline mr-1"></i> Request Press / Interview
                    </a>
                </div>
            </div>

        </div> <!-- /container -->
    </section>

    <!-- Citation Modal -->
    <div class="modal fade" id="mediaCiteModal" tabindex="-1" role="dialog" aria-labelledby="mediaCiteModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content" style="border-radius: 16px; overflow: hidden;">
                <div class="modal-header bg-dark text-white">
                    <h5 class="modal-title font-weight-bold" id="mediaCiteModalLabel">
                        <i class="mdi mdi-format-quote-open text-warning mr-1"></i> Media &amp; Press Citation
                    </h5>
                    <button type="button" class="close text-white" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body p-4">
                    <h6 class="font-weight-bold text-primary mb-1" id="modalMediaTitle">Feature Title</h6>
                    <p class="small text-muted mb-3" id="modalMediaOutletYear">Outlet • Year</p>

                    <label class="font-weight-bold small text-muted text-uppercase">Standard Media Reference (APA / Press Format)</label>
                    <div class="p-3 bg-light rounded border mb-3 font-monospace small" id="modalApaFormat" style="white-space: pre-wrap; font-family: monospace; font-size: 12.5px;"></div>

                    <label class="font-weight-bold small text-muted text-uppercase">Direct URL</label>
                    <div class="p-2 bg-light rounded border text-truncate small font-monospace" id="modalUrlFormat" style="font-family: monospace;"></div>
                </div>
                <div class="modal-footer bg-light">
                    <button type="button" class="btn btn-secondary btn-sm" data-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary btn-sm font-weight-bold" onclick="copyCitationText()">
                        <i class="mdi mdi-content-copy mr-1"></i> Copy Citation
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- Toast Notification -->
    <div id="citeToast">
        <i class="mdi mdi-check-circle-outline text-warning" style="font-size: 20px;"></i>
        <span id="toastMessage">Citation copied to clipboard!</span>
    </div>

    <!-- Footer Start -->
    <footer class="footer bg-light">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-12 text-center">
                    <a href="index" class="footer-logo brand-logo-wrap font-weight-bold d-inline-flex justify-content-center align-items-center" style="text-decoration: none;">
                        <span class="brand-monogram-emblem">
                            <svg class="brand-logo-svg" width="38" height="38" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <defs>
                                    <linearGradient id="hvFootGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                                        <stop offset="0%" stop-color="#1e40af" />
                                        <stop offset="55%" stop-color="#2563eb" />
                                        <stop offset="100%" stop-color="#4f46e5" />
                                    </linearGradient>
                                    <linearGradient id="hvFootAccentGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                                        <stop offset="0%" stop-color="#38bdf8" />
                                        <stop offset="100%" stop-color="#818cf8" />
                                    </linearGradient>
                                </defs>
                                <rect width="40" height="40" rx="10" fill="url(#hvFootGrad)" />
                                <rect x="0.75" y="0.75" width="38.5" height="38.5" rx="9.25" stroke="rgba(255,255,255,0.22)" stroke-width="1.5" />
                                <path d="M11 12V28M11 20H19M19 12V28" stroke="#ffffff" stroke-width="2.75" stroke-linecap="round" stroke-linejoin="round"/>
                                <path d="M23 12L28.5 28L34 12" stroke="url(#hvFootAccentGrad)" stroke-width="2.75" stroke-linecap="round" stroke-linejoin="round"/>
                                <circle cx="34" cy="12" r="1.75" fill="#38bdf8" />
                            </svg>
                        </span>
                        <span class="brand-name-text">
                            <span class="brand-first-name">Harsh</span><span class="brand-last-name">Verma</span>
                        </span>
                    </a>
                    <p class="para-desc mx-auto mt-4 text-black" style="max-width: 650px;">
                        Principal Software Engineer in AI @ Palo Alto Networks • Forbes Technology Council Member • IEEE Senior Member • Stanford GSB Scholar
                    </p>
                    <ul class="list-unstyled mb-0 mt-4 social-icon">
                        <li class="list-inline-item mr-1"><a href="https://scholar.google.com/citations?hl=en&user=zSt9oRMAAAAJ" target="_blank" class="rounded-circle" title="Google Scholar"><i class="mdi mdi-school"></i></a></li>
                        <li class="list-inline-item mr-1"><a href="https://www.linkedin.com/in/harshverma59/" target="_blank" class="rounded-circle" title="LinkedIn"><i class="mdi mdi-linkedin"></i></a></li>
                        <li class="list-inline-item mr-1"><a href="https://github.com/iamharshverma" target="_blank" class="rounded-circle" title="GitHub"><i class="mdi mdi-github-face"></i></a></li>
                        <li class="list-inline-item mr-1"><a href="https://medium.com/@harshverma59" target="_blank" class="rounded-circle" title="Medium"><i class="mdi mdi-medium"></i></a></li>
                        <li class="list-inline-item mr-1"><a href="https://twitter.com/harshverma59" target="_blank" class="rounded-circle" title="Twitter"><i class="mdi mdi-twitter"></i></a></li>
                        <li class="list-inline-item mr-1"><a href="https://www.instagram.com/aiwithharsh/" target="_blank" class="rounded-circle" title="Instagram"><i class="mdi mdi-instagram"></i></a></li>
                    </ul>
                </div>
            </div>
        </div>
    </footer>
    <footer class="footer footer-bar bg-black">
        <div class="container text-foot text-center">
            <p class="mb-0 text-white-50">&copy; <script>document.write(new Date().getFullYear())</script> Harsh Verma. All rights reserved.</p>
        </div>
    </footer>
    <!-- Footer End -->

    <!-- Back to top -->
    <a href="#" class="back-to-top" id="back-to-top"> 
        <i class="mdi mdi-chevron-up"> </i> 
    </a>

    <!-- JavaScript -->
    <script src="js/jquery.min.js"></script>
    <script src="js/bootstrap.bundle.min.js"></script>
    <script src="js/feather.min.js"></script>
    <script src="js/app.js"></script>

    <script>
        var currentType = 'all';
        var currentTopic = 'all';
        var searchQuery = '';
        var activeCitationText = '';
        var defaultFeaturedIds = [
            "media-times-square-nyc",
            "media-business-insider-agentic",
            "media-berkeley-skydeck-genai",
            "media-hackernoon-interview-agentic",
            "media-usa-today-cybersecurity",
            "media-yahoo-finance-cloud-sec"
        ];
        var featuredCards = [];

        // Global Chart Instances
        var formatChartInstance = null;
        var topicChartInstance = null;
        var growthChartInstance = null;

        // Initialize Starred / Featured Cards from LocalStorage
        function initFeaturedCards() {
            try {
                var stored = localStorage.getItem('harshverma_featured_media_cards');
                if (stored !== null) {
                    featuredCards = JSON.parse(stored);
                } else {
                    featuredCards = defaultFeaturedIds.slice();
                    localStorage.setItem('harshverma_featured_media_cards', JSON.stringify(featuredCards));
                }
            } catch (e) {
                featuredCards = defaultFeaturedIds.slice();
            }
            updateFeaturedUI();
        }

        function updateFeaturedUI() {
            // Update individual cards UI state & star icons
            var allCols = document.querySelectorAll('.media-card-col');
            allCols.forEach(function(col) {
                var cid = col.getAttribute('data-id');
                var card = document.getElementById('card-' + cid);
                var starIcon = document.getElementById('star-icon-' + cid);
                var isFeatured = featuredCards.indexOf(cid) !== -1;

                if (isFeatured) {
                    if (card) card.classList.add('is-featured-card');
                    if (starIcon) {
                        starIcon.className = 'mdi mdi-star';
                        starIcon.style.color = '#ffffff';
                    }
                } else {
                    if (card) card.classList.remove('is-featured-card');
                    if (starIcon) {
                        starIcon.className = 'mdi mdi-star-outline';
                        starIcon.style.color = '';
                    }
                }
            });

            // Update Counts across pills, ribbons and badges
            var count = featuredCards.length;
            var badge = document.getElementById('featuredBadgeCount');
            if (badge) badge.innerText = count;
            var ribbon = document.getElementById('ribbonFeaturedCount');
            if (ribbon) ribbon.innerText = count;

            var clearBtn = document.getElementById('btnClearPins');
            var btnClearPinCount = document.getElementById('btnClearPinCount');
            var restoreBtn = document.getElementById('btnRestoreDefaults');
            var pinnedStatusText = document.getElementById('pinnedStatusText');
            var pinnedStatusBadge = document.getElementById('pinnedStatusBadge');

            if (btnClearPinCount) btnClearPinCount.innerText = count;

            if (count > 0) {
                if (clearBtn) clearBtn.style.display = 'inline-flex';
                if (pinnedStatusBadge) {
                    pinnedStatusBadge.className = 'badge badge-warning text-dark font-weight-bold px-2 py-1';
                    pinnedStatusBadge.style.display = 'inline-flex';
                }
                if (pinnedStatusText) pinnedStatusText.innerText = 'Pinned Cards On Top (' + count + ')';
            } else {
                if (clearBtn) clearBtn.style.display = 'none';
                if (pinnedStatusBadge) {
                    pinnedStatusBadge.className = 'badge badge-secondary text-light font-weight-normal px-2 py-1';
                }
                if (pinnedStatusText) pinnedStatusText.innerText = 'No Pinned Cards';
            }

            // Reapply current sorting to hoist pinned items to top
            var sortSelect = document.getElementById('sortSelect');
            if (sortSelect) applySorting(sortSelect.value);
        }

        function toggleFeatureCard(event, id) {
            if (event) event.stopPropagation();
            var index = featuredCards.indexOf(id);

            if (index !== -1) {
                featuredCards.splice(index, 1);
                showToast("Unpinned card (" + featuredCards.length + " pinned remaining)");
            } else {
                featuredCards.push(id);
                showToast("⭐ Pinned to Top Spotlight (" + featuredCards.length + " pinned)!");
            }

            try {
                localStorage.setItem('harshverma_featured_media_cards', JSON.stringify(featuredCards));
            } catch (e) {}

            updateFeaturedUI();
            filterMedia();
        }

        // Clear all pins down to 0
        function clearAllFeatured() {
            featuredCards = [];
            try {
                localStorage.setItem('harshverma_featured_media_cards', JSON.stringify(featuredCards));
            } catch (e) {}
            updateFeaturedUI();
            filterMedia();
            showToast("Cleared all pinned cards (0 pinned)");
        }

        // Restore curated 6 editorial highlights
        function restoreDefaultFeatured() {
            featuredCards = defaultFeaturedIds.slice();
            try {
                localStorage.setItem('harshverma_featured_media_cards', JSON.stringify(featuredCards));
            } catch (e) {}
            updateFeaturedUI();
            filterMedia();
            showToast("Restored 6 Landmark Editorial Highlights ⭐");
        }

        function setFeaturedOnlyFilter() {
            setTypeFilter('featured', document.getElementById('filterPillFeatured'));
            window.scrollTo({ top: document.querySelector('.search-container').offsetTop - 90, behavior: 'smooth' });
        }

        function handleSearchInput(val) {
            searchQuery = val.toLowerCase().trim();
            var clearBtn = document.getElementById('clearSearchBtn');
            if (searchQuery.length > 0) {
                clearBtn.style.display = 'flex';
            } else {
                clearBtn.style.display = 'none';
            }
            filterMedia();
        }

        function clearSearch() {
            document.getElementById('mediaSearchInput').value = '';
            document.getElementById('clearSearchBtn').style.display = 'none';
            searchQuery = '';
            setTypeFilter('all', document.querySelector('.btn-filter-pill'));
            setTopicFilter('all', document.querySelector('.btn-topic-pill'));
            filterMedia();
        }

        function setTypeFilter(type, btn) {
            currentType = type;
            document.querySelectorAll('.btn-filter-pill').forEach(function(b) {
                b.classList.remove('active');
            });
            if (btn) btn.classList.add('active');
            filterMedia();
        }

        function setTopicFilter(topic, btn) {
            currentTopic = topic;
            document.querySelectorAll('.btn-topic-pill').forEach(function(b) {
                b.classList.remove('active');
            });
            if (btn) btn.classList.add('active');
            filterMedia();
        }

        function filterByTag(tag) {
            document.getElementById('mediaSearchInput').value = tag;
            handleSearchInput(tag);
            window.scrollTo({ top: document.querySelector('.search-container').offsetTop - 90, behavior: 'smooth' });
        }

        function filterMedia() {
            var cards = document.querySelectorAll('.media-card-col');
            var count = 0;

            cards.forEach(function(card) {
                var cardType = card.getAttribute('data-type');
                var cardId = card.getAttribute('data-id');
                var cardSearch = card.getAttribute('data-search');

                var matchesType = true;
                if (currentType === 'featured') {
                    matchesType = (featuredCards.indexOf(cardId) !== -1);
                } else if (currentType !== 'all') {
                    matchesType = (cardType === currentType);
                }

                var matchesTopic = (currentTopic === 'all') || (cardSearch.indexOf(currentTopic.toLowerCase()) !== -1);
                var matchesQuery = (searchQuery === '') || (cardSearch.indexOf(searchQuery) !== -1);

                if (matchesType && matchesTopic && matchesQuery) {
                    card.style.display = '';
                    count++;
                } else {
                    card.style.display = 'none';
                }
            });

            var visibleCountEl = document.getElementById('visibleCount');
            if (visibleCountEl) visibleCountEl.innerText = count;

            var empty = document.getElementById('noMediaFound');
            var emptyTitle = document.getElementById('noMediaTitle');
            var emptyDesc = document.getElementById('noMediaDesc');
            var emptyActions = document.getElementById('noMediaActions');

            if (count === 0) {
                if (currentType === 'featured' && featuredCards.length === 0) {
                    if (emptyTitle) emptyTitle.innerText = "No Featured Cards Currently Pinned";
                    if (emptyDesc) emptyDesc.innerHTML = "You haven't starred any media cards yet (0 pinned). Click the ⭐ star on any card to pin it on top, or restore the curated top 6 highlights below.";
                    if (emptyActions) {
                        emptyActions.innerHTML = '<button type="button" class="btn btn-warning btn-sm px-3 py-2 mr-2 font-weight-bold text-dark" onclick="restoreDefaultFeatured()"><i class="mdi mdi-star mr-1"></i> Restore Top 6 Picks</button><button type="button" class="btn btn-primary btn-sm px-3 py-2" onclick="setTypeFilter(\\'all\\', document.querySelector(\\'.btn-filter-pill\\'))"><i class="mdi mdi-view-grid mr-1"></i> View All Media</button>';
                    }
                } else {
                    if (emptyTitle) emptyTitle.innerText = "No matching media features found";
                    if (emptyDesc) emptyDesc.innerText = "Try adjusting your keyword search or resetting active filters.";
                    if (emptyActions) {
                        emptyActions.innerHTML = '<button type="button" class="btn btn-primary btn-sm px-4 py-2 mt-2" onclick="clearSearch()"><i class="mdi mdi-refresh mr-1"></i> Reset All Filters</button>';
                    }
                }
                if (empty) empty.style.display = 'block';
            } else {
                if (empty) empty.style.display = 'none';
            }
        }

        function setViewMode(mode) {
            var container = document.getElementById('mediaGridContainer');
            var gridBtn = document.getElementById('gridModeBtn');
            var listBtn = document.getElementById('listModeBtn');

            if (mode === 'list') {
                container.classList.add('media-list-mode');
                listBtn.classList.add('active');
                gridBtn.classList.remove('active');
            } else {
                container.classList.remove('media-list-mode');
                gridBtn.classList.add('active');
                listBtn.classList.remove('active');
            }
        }

        function applySorting(criteria) {
            var container = document.getElementById('mediaGridContainer');
            var cards = Array.from(document.querySelectorAll('.media-card-col'));

            cards.sort(function(a, b) {
                var idA = a.getAttribute('data-id');
                var idB = b.getAttribute('data-id');
                var isFeatA = featuredCards.indexOf(idA) !== -1;
                var isFeatB = featuredCards.indexOf(idB) !== -1;

                if (criteria === 'featured') {
                    // Pinned cards ALWAYS on top!
                    if (isFeatA && !isFeatB) return -1;
                    if (!isFeatA && isFeatB) return 1;
                    
                    // Inside same pin state, sort newest first
                    var yearA = parseInt(a.getAttribute('data-year')) || 2026;
                    var yearB = parseInt(b.getAttribute('data-year')) || 2026;
                    return yearB - yearA;
                } else if (criteria === 'newest') {
                    var yearA = parseInt(a.getAttribute('data-year')) || 2026;
                    var yearB = parseInt(b.getAttribute('data-year')) || 2026;
                    return yearB - yearA;
                } else if (criteria === 'outlet') {
                    return a.getAttribute('data-outlet').localeCompare(b.getAttribute('data-outlet'));
                } else if (criteria === 'title') {
                    return a.getAttribute('data-title').localeCompare(b.getAttribute('data-title'));
                }
                return 0;
            });

            cards.forEach(function(c) { container.appendChild(c); });
        }

        function toggleAnalyticsDashboard() {
            var collapse = document.getElementById('analyticsCollapseContainer');
            var icon = document.getElementById('toggleAnalyticsIcon');
            var btn = document.getElementById('btnToggleAnalytics');
            if (collapse.style.display === 'none') {
                collapse.style.display = 'block';
                icon.className = 'mdi mdi-chevron-up';
                btn.innerHTML = '<i class="mdi mdi-chevron-up" id="toggleAnalyticsIcon"></i> Collapse';
            } else {
                collapse.style.display = 'none';
                icon.className = 'mdi mdi-chevron-down';
                btn.innerHTML = '<i class="mdi mdi-chevron-down" id="toggleAnalyticsIcon"></i> Expand Analytics';
            }
        }

        function openMediaCiteModal(title, outlet, year, url) {
            document.getElementById('modalMediaTitle').innerText = title;
            document.getElementById('modalMediaOutletYear').innerText = outlet + " • " + year;
            
            var citation = outlet + ". (" + year + "). " + title + ". Retrieved from " + url;
            document.getElementById('modalApaFormat').innerText = citation;
            document.getElementById('modalUrlFormat').innerText = url;
            
            activeCitationText = citation;
            $('#mediaCiteModal').modal('show');
        }

        function copyCitationText() {
            if (!activeCitationText) return;
            if (navigator.clipboard) {
                navigator.clipboard.writeText(activeCitationText).then(function() {
                    showToast("Citation copied to clipboard!");
                    $('#mediaCiteModal').modal('hide');
                }).catch(function() {
                    prompt("Copy Citation:", activeCitationText);
                });
            } else {
                prompt("Copy Citation:", activeCitationText);
            }
        }

        function showToast(msg) {
            var toast = document.getElementById('citeToast');
            document.getElementById('toastMessage').innerText = msg;
            toast.style.display = 'flex';
            setTimeout(function() {
                toast.style.display = 'none';
            }, 3200);
        }

        // ==========================
        // Chart.js Visual Analytics
        // ==========================
        function initMediaCharts() {
            var isDark = document.documentElement.classList.contains('dark-mode') || (document.body && document.body.classList.contains('dark-mode'));
            var textColor = isDark ? '#94a3b8' : '#64748b';
            var gridColor = isDark ? 'rgba(255, 255, 255, 0.08)' : 'rgba(0, 0, 0, 0.06)';

            // 1. Format Distribution Doughnut Chart
            var ctxFormat = document.getElementById('mediaFormatChart');
            if (ctxFormat) {
                if (formatChartInstance) formatChartInstance.destroy();
                formatChartInstance = new Chart(ctxFormat, {
                    type: 'doughnut',
                    data: {
                        labels: ['Top Tier Press (12)', 'Podcasts (8)', 'In-Depth Interviews (8)', 'Keynotes (6)', 'Institutional (3)'],
                        datasets: [{
                            data: [12, 8, 8, 6, 3],
                            backgroundColor: [
                                '#0284c7', // Cyan / Blue for Press
                                '#e11d48', // Red for Podcasts
                                '#059669', // Emerald for Interviews
                                '#7c3aed', // Purple for Keynotes
                                '#d97706'  // Amber for Institutional
                            ],
                            borderWidth: 2,
                            borderColor: isDark ? '#0f172a' : '#ffffff'
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        cutout: '68%',
                        plugins: {
                            legend: {
                                position: 'bottom',
                                labels: {
                                    boxWidth: 12,
                                    padding: 10,
                                    color: textColor,
                                    font: { size: 11, weight: '600' }
                                }
                            },
                            tooltip: {
                                callbacks: {
                                    label: function(item) {
                                        return ' ' + item.label + ' • Click to filter';
                                    }
                                }
                            }
                        },
                        onClick: function(evt, elements) {
                            if (elements && elements.length > 0) {
                                var idx = elements[0].index;
                                var typeMap = ['press', 'podcast', 'interview', 'keynote', 'institutional'];
                                var targetType = typeMap[idx];
                                var targetBtn = document.querySelector('.btn-filter-pill[data-type="' + targetType + '"]');
                                setTypeFilter(targetType, targetBtn);
                                showToast("Filtered by format: " + targetType.toUpperCase());
                            }
                        }
                    }
                });
            }

            // 2. Topic & Research Domains Horizontal Bar Chart
            var ctxTopic = document.getElementById('topicDomainChart');
            if (ctxTopic) {
                if (topicChartInstance) topicChartInstance.destroy();
                topicChartInstance = new Chart(ctxTopic, {
                    type: 'bar',
                    data: {
                        labels: ['Agentic Security', 'Cybersecurity', 'Production AI', 'Mentorship & Growth', 'Big Data & Cloud'],
                        datasets: [{
                            label: 'Features Count',
                            data: [14, 11, 8, 7, 6],
                            backgroundColor: [
                                '#2563eb',
                                '#0ea5e9',
                                '#8b5cf6',
                                '#10b981',
                                '#f59e0b'
                            ],
                            borderRadius: 6
                        }]
                    },
                    options: {
                        indexAxis: 'y',
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: { display: false },
                            tooltip: {
                                callbacks: {
                                    label: function(item) {
                                        return ' ' + item.raw + ' Features • Click to filter';
                                    }
                                }
                            }
                        },
                        scales: {
                            x: {
                                grid: { color: gridColor },
                                ticks: { color: textColor, font: { size: 11 } }
                            },
                            y: {
                                grid: { display: false },
                                ticks: { color: textColor, font: { size: 11, weight: '600' } }
                            }
                        },
                        onClick: function(evt, elements) {
                            if (elements && elements.length > 0) {
                                var idx = elements[0].index;
                                var topics = ['Agentic Security', 'Zero Trust', 'Production AI', 'Career Strategy', 'Big Data'];
                                setTopicFilter(topics[idx], null);
                                showToast("Filtered by topic: " + topics[idx]);
                            }
                        }
                    }
                });
            }

            // 3. Multi-Year Trajectory & Coverage Velocity Line Chart
            var ctxGrowth = document.getElementById('timelineGrowthChart');
            if (ctxGrowth) {
                if (growthChartInstance) growthChartInstance.destroy();
                growthChartInstance = new Chart(ctxGrowth, {
                    type: 'line',
                    data: {
                        labels: ['2018', '2019', '2021', '2022', '2023', '2024', '2025', '2026'],
                        datasets: [{
                            label: 'Cumulative Reach & Impact',
                            data: [1, 3, 6, 11, 16, 24, 31, 37],
                            fill: true,
                            borderColor: '#f59e0b',
                            backgroundColor: isDark ? 'rgba(245, 158, 11, 0.15)' : 'rgba(245, 158, 11, 0.12)',
                            tension: 0.38,
                            pointBackgroundColor: '#f59e0b',
                            pointBorderColor: '#ffffff',
                            pointRadius: 4,
                            pointHoverRadius: 7
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: { display: false },
                            tooltip: {
                                callbacks: {
                                    label: function(item) {
                                        return ' ' + item.raw + ' Total Features by ' + item.label;
                                    }
                                }
                            }
                        },
                        scales: {
                            x: {
                                grid: { color: gridColor },
                                ticks: { color: textColor, font: { size: 11 } }
                            },
                            y: {
                                grid: { color: gridColor },
                                ticks: { color: textColor, font: { size: 11 } }
                            }
                        }
                    }
                });
            }
        }

        // On DOM Loaded
        document.addEventListener('DOMContentLoaded', function() {
            initFeaturedCards();
            initMediaCharts();

            // Observe dark mode toggles to refresh chart themes
            var observer = new MutationObserver(function(mutations) {
                mutations.forEach(function(m) {
                    if (m.attributeName === 'class') {
                        setTimeout(initMediaCharts, 100);
                    }
                });
            });
            if (document.body) observer.observe(document.body, { attributes: true });
            observer.observe(document.documentElement, { attributes: true });
            window.addEventListener('themeChanged', function() {
                setTimeout(initMediaCharts, 100);
            });
        });
    </script>
    <!-- HV Booking Flow & Keynote Hub Engine -->
    <script src="js/hv-booking-flow.js"></script>
    <!-- HV AI Copilot Assistant Engine -->
    <script src="js/hv-copilot.js"></script>
</body>
</html>
"""

full_html = header_part + cards_full_html + footer_part

with open('page-media.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print(f"page-media.html regenerated successfully! File size: {len(full_html)} bytes.")
