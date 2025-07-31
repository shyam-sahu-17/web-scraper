# utils.py
from bs4 import BeautifulSoup

def find_next_page(soup):
    link = soup.find('a', string=lambda t: t and 'next' in t.lower())
    if link and link.get('href'):
        return link['href']
    return None

def crawl_all_pages(base_url, fetch_function):
    current_url = base_url
    all_data = []
    visited = set()

    while current_url and current_url not in visited:
        visited.add(current_url)
        soup = fetch_function(current_url)
        data = scrape_basic_info(current_url)  # reuse existing
        all_data.append(data)
        next_url = find_next_page(soup)
        if next_url and not next_url.startswith("http"):
            from urllib.parse import urljoin
            next_url = urljoin(current_url, next_url)
        current_url = next_url

    return all_data
