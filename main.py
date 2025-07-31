# main.py
import csv
import json
from scraper import scrape_basic_info

results = [scrape_basic_info(url) for url in valid_urls]

# Save as CSV
with open('output/companies.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

# Save as JSON
with open('output/companies.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=4)
