# 7) Scrape image URLs
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
soup = BeautifulSoup(requests.get(url).text, "html.parser")

images = soup.find_all("img")

print("Image URLs:")
for img in images:
    print(img.get("src"))
