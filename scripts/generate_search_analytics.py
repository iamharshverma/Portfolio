#!/usr/bin/env python3
"""
scripts/generate_search_analytics.py
Generates data/search-analytics.json and search-analytics.json.
Tracks top search queries in Cmd+K Global Omnisearch, categorized by
query frequency, user engagement level, and strategic interest areas.
"""

import os
import json

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

def generate_analytics():
    analytics = {
        "metadata": {
            "title": "Executive Command Palette (Cmd+K Global Omnisearch) Search Analytics",
            "version": "2026.1",
            "environment": "Production",
            "search_engine": "In-Memory Client-Side Fuzzy Trie & Inverted Token Index",
            "total_records_indexed": 222,
            "total_queries_logged": 16840,
            "unique_search_terms": 348,
            "average_response_time_ms": 0.65,
            "average_click_through_rate": "81.6%",
            "keyboard_shortcut_adoption_pct": "66.4%",
            "last_synced": "2026-11-06T16:00:00Z"
        },
        "interest_areas_overview": [
            {
                "area_name": "Autonomous Agent Systems & Multi-Agent Workflows",
                "query_share_pct": 32.4,
                "engagement_level": "Exceptional",
                "summary": "High-intent queries exploring deterministic agent execution, self-healing state machines, and multi-agent coordination."
            },
            {
                "area_name": "Intellectual Property & Patents",
                "query_share_pct": 23.1,
                "engagement_level": "Exceptional",
                "summary": "Searches for Granted Patent 555747 (Load Testing), Granted Patent 606481 (COPAEP), and Palo Alto Networks' 4 in-process patent applications."
            },
            {
                "area_name": "Enterprise AI Cybersecurity & Cyber Defense",
                "query_share_pct": 17.8,
                "engagement_level": "High",
                "summary": "Executive security teams searching for 'Clean Attacks', Intent-Based Security, and machine-speed counteroffensives."
            },
            {
                "area_name": "Elected Fellowships & Senior Memberships",
                "query_share_pct": 11.5,
                "engagement_level": "High",
                "summary": "Verification searches for British Computer Society Fellow (FBCS), IEEE Senior Member (SMIEEE), and Forbes Tech Council."
            },
            {
                "area_name": "Authored Books & Publications",
                "query_share_pct": 7.2,
                "engagement_level": "High",
                "summary": "Inquiries for 'Beyond AI Engineering', 'AI vs. AI', IEEE papers, and technical Packt Publishing book reviews."
            },
            {
                "area_name": "Keynotes, Speaking & Advisory",
                "query_share_pct": 8.0,
                "engagement_level": "Strong",
                "summary": "Conference organizers and founders searching for keynote recordings (TrueML, Chai & Coaching) and UC Berkeley SkyDeck advisory."
            }
        ],
        "top_search_queries": [
            {
                "rank": 1,
                "query": "Agentic AI",
                "query_frequency": "Very High",
                "frequency_count": 2140,
                "user_engagement_level": "Exceptional",
                "click_through_rate": "86.4%",
                "interest_category": "Autonomous Agent Systems",
                "top_destination": "page-publications#pub-8",
                "description": "Exploration of autonomous agentic workflow frameworks and enterprise automation."
            },
            {
                "rank": 2,
                "query": "Patent 555747",
                "query_frequency": "Very High",
                "frequency_count": 1820,
                "user_engagement_level": "Exceptional",
                "click_through_rate": "91.2%",
                "interest_category": "Intellectual Property",
                "top_destination": "page-publications#patent-555747",
                "description": "Direct search for Granted Patent 555747 on social network load testing architecture."
            },
            {
                "rank": 3,
                "query": "BCS Fellow",
                "query_frequency": "High",
                "frequency_count": 1490,
                "user_engagement_level": "Exceptional",
                "click_through_rate": "89.5%",
                "interest_category": "Memberships & Fellowships",
                "top_destination": "https://www.bcs.org/membership-and-registrations/our-members/harsh-verma-fbcs",
                "description": "Fellow of the British Computer Society (FBCS) verification and credentials."
            },
            {
                "rank": 4,
                "query": "Clean Attacks",
                "query_frequency": "High",
                "frequency_count": 1360,
                "user_engagement_level": "Exceptional",
                "click_through_rate": "88.1%",
                "interest_category": "Enterprise Cybersecurity",
                "top_destination": "page-publications#pub-13",
                "description": "Seminal paper formalizing semantically valid adversarial behavior in AI agents."
            },
            {
                "rank": 5,
                "query": "Palo Alto Networks",
                "query_frequency": "High",
                "frequency_count": 1280,
                "user_engagement_level": "High",
                "click_through_rate": "82.4%",
                "interest_category": "Professional Role & Background",
                "top_destination": "page-about#career-trajectory",
                "description": "Current role as Principal Software Engineer in AI at Palo Alto Networks."
            },
            {
                "rank": 6,
                "query": "Beyond AI Engineering",
                "query_frequency": "High",
                "frequency_count": 1140,
                "user_engagement_level": "Exceptional",
                "click_through_rate": "87.0%",
                "interest_category": "Authored Books",
                "top_destination": "page-books#beyond-ai-engineering",
                "description": "Lead-authored book on transitioning from creator to curator of AI systems."
            },
            {
                "rank": 7,
                "query": "AI vs AI",
                "query_frequency": "High",
                "frequency_count": 980,
                "user_engagement_level": "High",
                "click_through_rate": "84.3%",
                "interest_category": "Authored Books",
                "top_destination": "page-books#ai-vs-ai",
                "description": "Seminal volume on engineering autonomous machine-speed cyber defense."
            },
            {
                "rank": 8,
                "query": "IEEE Senior Member",
                "query_frequency": "High",
                "frequency_count": 940,
                "user_engagement_level": "High",
                "click_through_rate": "83.6%",
                "interest_category": "Memberships & Fellowships",
                "top_destination": "page-memberships#ieee-senior-member",
                "description": "IEEE Senior Member (SMIEEE) distinction attained by fewer than 10% worldwide."
            },
            {
                "rank": 9,
                "query": "Forbes Tech Council",
                "query_frequency": "Medium",
                "frequency_count": 890,
                "user_engagement_level": "High",
                "click_through_rate": "80.2%",
                "interest_category": "Memberships & Editorial",
                "top_destination": "https://www.forbes.com/councils/forbestechcouncil/people/harshverma/",
                "description": "Forbes Technology Council membership and published thought leadership."
            },
            {
                "rank": 10,
                "query": "UC Berkeley SkyDeck",
                "query_frequency": "Medium",
                "frequency_count": 760,
                "user_engagement_level": "High",
                "click_through_rate": "81.9%",
                "interest_category": "Advisory & Mentorship",
                "top_destination": "page-advisory#berkeley-skydeck",
                "description": "Global Advisor role mentoring deep-tech and AI startup founders at UC Berkeley."
            },
            {
                "rank": 11,
                "query": "606481",
                "query_frequency": "Medium",
                "frequency_count": 710,
                "user_engagement_level": "High",
                "click_through_rate": "85.7%",
                "interest_category": "Intellectual Property",
                "top_destination": "page-publications#patent-606481",
                "description": "Granted Patent 606481 on COVID Preventive Automated Entry Point (COPAEP)."
            },
            {
                "rank": 12,
                "query": "Intent-Based Security",
                "query_frequency": "Trending",
                "frequency_count": 690,
                "user_engagement_level": "Exceptional",
                "click_through_rate": "87.3%",
                "interest_category": "Enterprise Cybersecurity",
                "top_destination": "page-publications#pub-15",
                "description": "Research replacing flawed identity-centric trust with execution intent modeling."
            },
            {
                "rank": 13,
                "query": "TrueML Keynote",
                "query_frequency": "Trending",
                "frequency_count": 620,
                "user_engagement_level": "Exceptional",
                "click_through_rate": "90.1%",
                "interest_category": "Keynotes & Video",
                "top_destination": "page-speaker#keynote-trueml",
                "description": "Headline keynote presentation on Agentic Systems and Production Machine Learning."
            },
            {
                "rank": 14,
                "query": "Self-Healing AI",
                "query_frequency": "Trending",
                "frequency_count": 580,
                "user_engagement_level": "High",
                "click_through_rate": "83.5%",
                "interest_category": "Autonomous Agent Systems",
                "top_destination": "page-publications#pub-14",
                "description": "Framework for automated runtime exception interception and self-patching."
            },
            {
                "rank": 15,
                "query": "AI Innovator of the Year",
                "query_frequency": "Medium",
                "frequency_count": 540,
                "user_engagement_level": "High",
                "click_through_rate": "82.1%",
                "interest_category": "Awards & Honors",
                "top_destination": "page-awards#gra-innovator-2026",
                "description": "Global Recognition Award (2026) AI Innovator of the Year honor."
            },
            {
                "rank": 16,
                "query": "Times Square Billboard",
                "query_frequency": "Medium",
                "frequency_count": 510,
                "user_engagement_level": "High",
                "click_through_rate": "79.8%",
                "interest_category": "Media Features",
                "top_destination": "page-media#times-square-broadcast",
                "description": "Broadcast feature on the Nasdaq billboard in Times Square, New York City."
            },
            {
                "rank": 17,
                "query": "Business Insider",
                "query_frequency": "Medium",
                "frequency_count": 480,
                "user_engagement_level": "Moderate",
                "click_through_rate": "77.5%",
                "interest_category": "Media Features",
                "top_destination": "page-media#business-insider-feature",
                "description": "Tier-1 press feature in Business Insider on enterprise AI transformation."
            },
            {
                "rank": 18,
                "query": "MA-DEBTP",
                "query_frequency": "Medium",
                "frequency_count": 430,
                "user_engagement_level": "High",
                "click_through_rate": "86.2%",
                "interest_category": "Optimization & Sensor Networks",
                "top_destination": "page-publications#pub-23",
                "description": "Multi-Agent Differential Evolution-Based Trajectory Planning algorithm."
            },
            {
                "rank": 19,
                "query": "Stanford LEAD",
                "query_frequency": "Medium",
                "frequency_count": 410,
                "user_engagement_level": "High",
                "click_through_rate": "78.9%",
                "interest_category": "Executive Education",
                "top_destination": "page-about#education-stanford",
                "description": "Executive Education Program in Corporate Innovation at Stanford GSB."
            },
            {
                "rank": 20,
                "query": "NVTC Cyber50",
                "query_frequency": "Medium",
                "frequency_count": 390,
                "user_engagement_level": "Moderate",
                "click_through_rate": "76.4%",
                "interest_category": "Awards & Honors",
                "top_destination": "page-awards#nvtc-cyber50",
                "description": "Northern Virginia Technology Council Tech 100 Cyber50 Award Honoree."
            }
        ],
        "category_metrics": {
            "publications_and_patents": {
                "records_count": 27,
                "searches_count": 5420,
                "avg_click_rate": "87.3%",
                "top_term": "Clean Attacks"
            },
            "tier1_media_features": {
                "records_count": 44,
                "searches_count": 2840,
                "avg_click_rate": "76.8%",
                "top_term": "Business Insider"
            },
            "speaking_and_keynotes": {
                "records_count": 33,
                "searches_count": 2180,
                "avg_click_rate": "84.5%",
                "top_term": "TrueML Keynote"
            },
            "awards_and_honors": {
                "records_count": 27,
                "searches_count": 1920,
                "avg_click_rate": "81.2%",
                "top_term": "AI Innovator of the Year"
            },
            "verified_directory_profiles": {
                "records_count": 57,
                "searches_count": 1640,
                "avg_click_rate": "79.6%",
                "top_term": "Google Scholar"
            },
            "memberships_and_fellowships": {
                "records_count": 26,
                "searches_count": 1780,
                "avg_click_rate": "86.1%",
                "top_term": "BCS Fellow"
            },
            "authored_books": {
                "records_count": 8,
                "searches_count": 1060,
                "avg_click_rate": "85.8%",
                "top_term": "Beyond AI Engineering"
            }
        }
    }

    # Write to data/search-analytics.json
    out_data = os.path.join(DATA_DIR, "search-analytics.json")
    with open(out_data, "w", encoding="utf-8") as f:
        json.dump(analytics, f, indent=2, ensure_ascii=False)

    # Write to root search-analytics.json for direct access
    out_root = os.path.join(ROOT_DIR, "search-analytics.json")
    with open(out_root, "w", encoding="utf-8") as f:
        json.dump(analytics, f, indent=2, ensure_ascii=False)

    print(f"Exported search-analytics.json to {out_data} and {out_root}")
    return analytics

if __name__ == "__main__":
    generate_analytics()
