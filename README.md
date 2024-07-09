# SEO Performance Analyzer

Empower your digital marketing strategy with data-driven insights! This Python tool harnesses the power of Google Search Console to analyze your website's SEO performance, revealing hidden opportunities for growth.

## Features

* **Keyword Performance Tracking:** Monitor how your target keywords rank over time, identifying top performers and areas for improvement.
* **Organic Traffic Analysis:** Visualize the flow of organic search traffic to your website, uncovering trends and peak performing periods.
* **Top Queries Identification:** Discover the most popular search terms driving users to your site, guiding content creation and optimization efforts.
* **Click-Through Rate (CTR) Analysis:** Assess the effectiveness of your search snippets in attracting clicks, highlighting areas for refinement.
* **Customizable Reports:** Easily generate comprehensive SEO reports tailored to your specific needs, facilitating data-driven decision-making.

## Why Choose Data-Driven SEO?

In the ever-evolving landscape of digital marketing, data is your most valuable asset. By leveraging insights from Google Search Console, you can:

* **Make Informed Decisions:** Base your SEO strategy on concrete data, not guesswork.
* **Uncover Hidden Opportunities:** Identify untapped potential for improved keyword rankings and increased organic traffic.
* **Measure Your Success:** Track the impact of your SEO efforts over time and refine your approach accordingly.

## Getting Started

1. **Prerequisites:**
   * Python 3.x installed
   * Google Search Console API credentials 
   * Required Python libraries (install using `pip install -r requirements.txt`)

2. **Configuration:**
   * Open `config.py` and replace the placeholders with:
     * Your Google Search Console API credentials (JSON file).
     * Your website property URI (e.g., 'sc-domain:example.com').
     * The desired date range for analysis (start and end dates).

3. **Usage:**
   * Run `python seo_analyzer.py`
   * The script will fetch data from Google Search Console, analyze it, and generate a report in the `reports` folder.

## Code Overview (seo_analyzer.py)

```python
import os
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import config

SCOPES = ['[https://www.googleapis.com/auth/webmasters.readonly](https://www.googleapis.com/auth/webmasters.readonly)']

# Initialize credentials and service (using values from config.py)
credentials = ServiceAccountCredentials.from_json_keyfile_name(config.CREDENTIALS_FILE, scopes=SCOPES)
service = build('webmasters', 'v3', credentials=credentials)

# Fetch and process data (using config.SITE_URL and date range from config.py)
# ... (Rest of the code for fetching, analyzing, and reporting - see full code below)
