# 2) Extract all links (<a href>) — commented version
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
soup = BeautifulSoup(requests.get(url).text, "html.parser")

# Find all anchor tags
links = soup.find_all("a")

print("All links found:")
for link in links:
    print(link.get("href"))