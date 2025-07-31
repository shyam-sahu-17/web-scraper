# scraper.py
import requests
from bs4 import BeautifulSoup
import re

def scrape_basic_info(url):
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')

        title = soup.title.string.strip() if soup.title else "N/A"
        emails = set(re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", res.text))
        phones = set(re.findall(r"\+?\d[\d\-\s]{8,}\d", res.text))

        return {
            "Company Name": title,
            "Website": url,
            "Email(s)": list(emails),
            "Phone(s)": list(phones)
        }

    except Exception as e:
        return {
            "Company Name": "Error",
            "Website": url,
            "Error": str(e)
        }
