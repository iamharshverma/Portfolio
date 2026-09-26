#!/usr/bin/env python3
"""
Generate RSS 2.0 Feed for Harsh Verma's Technical Articles & Publications.
Provides standard syndication for RSS readers (Feedly, Inoreader, NetNewsWire, etc.).
"""

import os
import sys
import html
from datetime import datetime

# Import articles from generate_blog_page
from generate_blog_page import articles_data

def format_rfc822_date(date_str, index=0):
    """Convert human dates to RFC-822 format required by RSS 2.0."""
    date_str = (date_str or "").strip()
    
    # Try exact Month Day, Year
    try:
        dt = datetime.strptime(date_str, "%B %d, %Y")
        return dt.strftime("%a, %d %b %Y 12:00:00 GMT")
    except ValueError:
        pass
        
    # Try Month Year
    try:
        dt = datetime.strptime(date_str, "%B %Y")
        # Distribute days across month to maintain chronological uniqueness
        day = min(28, max(1, 20 - (index % 15)))
        dt = dt.replace(day=day)
        return dt.strftime("%a, %d %b %Y 12:00:00 GMT")
    except ValueError:
        pass
        
    if "2026" in date_str:
        day = min(28, max(1, 25 - (index % 20)))
        return f"Wed, {day:02d} Jul 2026 12:00:00 GMT"
        
    return "Tue, 15 Jan 2026 12:00:00 GMT"

def generate_rss_xml(base_url="https://harshverma.com"):
    now_rfc = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")
    
    items_xml = []
    for idx, article in enumerate(articles_data):
        title = html.escape(article.get("title", ""))
        link = html.escape(article.get("url", ""))
        guid = link
        pub_date = format_rfc822_date(article.get("date", ""), idx)
        category = html.escape(article.get("category", "Artificial Intelligence"))
        platform = html.escape(article.get("platform_full") or article.get("platform", "Tech Publication"))
        read_time = html.escape(article.get("read_time", "5 min read"))
        description_text = html.escape(article.get("description", ""))
        tags = article.get("tags", [])
        
        tags_xml = "".join([f"\n      <category>{html.escape(t)}</category>" for t in tags if t])
        
        content_html = f"""<p>{description_text}</p>
<p><strong>Published in:</strong> {platform} • <strong>Read Time:</strong> {read_time}</p>
<p><a href="{link}" target="_blank" rel="noopener noreferrer">Read Full Article on {platform} →</a></p>"""
        
        item = f"""    <item>
      <title>{title}</title>
      <link>{link}</link>
      <guid isPermaLink="true">{guid}</guid>
      <pubDate>{pub_date}</pubDate>
      <dc:creator>Harsh Verma</dc:creator>
      <category>{category}</category>{tags_xml}
      <description>{description_text}</description>
      <content:encoded><![CDATA[{content_html}]]></content:encoded>
    </item>"""
        items_xml.append(item)
    
    feed_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" 
     xmlns:atom="http://www.w3.org/2005/Atom" 
     xmlns:content="http://purl.org/rss/1.0/modules/content/" 
     xmlns:dc="http://purl.org/dc/elements/1.1/">
  <channel>
    <title>Harsh Verma • Tech Articles &amp; AI Engineering Insights</title>
    <link>{base_url}/page-blog</link>
    <description>Technical articles, architectural deep dives on Agentic AI, Autonomous Copilots, Zero-Trust Cyber Defense, and High-Scale Enterprise Systems by Harsh Verma (Principal AI Engineer @ Palo Alto Networks, Forbes Technology Council, IEEE Senior Member).</description>
    <language>en-us</language>
    <lastBuildDate>{now_rfc}</lastBuildDate>
    <pubDate>{now_rfc}</pubDate>
    <ttl>60</ttl>
    <managingEditor>harshverma59@gmail.com (Harsh Verma)</managingEditor>
    <webMaster>harshverma59@gmail.com (Harsh Verma)</webMaster>
    <atom:link href="{base_url}/rss.xml" rel="self" type="application/rss+xml"/>
    <image>
      <url>{base_url}/images/favicon.ico</url>
      <title>Harsh Verma • Tech Articles</title>
      <link>{base_url}/page-blog</link>
    </image>
{chr(10).join(items_xml)}
  </channel>
</rss>
"""
    return feed_xml

def main():
    feed_content = generate_rss_xml()
    
    # Write rss.xml
    with open("rss.xml", "w", encoding="utf-8") as f:
        f.write(feed_content)
    print(f"Generated rss.xml with {len(articles_data)} articles ({len(feed_content)} bytes).")
    
    # Also write feed.xml for standard alias
    with open("feed.xml", "w", encoding="utf-8") as f:
        f.write(feed_content)
    print("Generated feed.xml alias successfully.")

if __name__ == "__main__":
    main()
