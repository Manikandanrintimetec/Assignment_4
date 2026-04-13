import requests
from bs4 import BeautifulSoup

class Scraper:

    def fetch_article(self, url):
        try:
            res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(res.text, "html.parser")

            paragraphs = soup.find_all("p")
            text = " ".join([p.get_text() for p in paragraphs])

            return text

        except Exception as e:
            print("Scraping error:", e)
            return ""