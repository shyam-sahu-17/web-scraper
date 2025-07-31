# social_scraper.py
def extract_social_links(soup):
    links = [a['href'] for a in soup.find_all('a', href=True)]
    socials = {
        "LinkedIn": [l for l in links if "linkedin.com" in l],
        "Twitter": [l for l in links if "twitter.com" in l],
        "Facebook": [l for l in links if "facebook.com" in l],
        "Instagram": [l for l in links if "instagram.com" in l],
    }
    return socials
