# dynamic_scraper.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def scrape_with_selenium(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get(url)
    driver.implicitly_wait(10)  # wait for JS to render
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    return soup
