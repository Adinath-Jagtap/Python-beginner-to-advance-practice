# 3) Extract all paragraph text
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
soup = BeautifulSoup(requests.get(url).text, "html.parser")

paragraphs = soup.find_all("p")

print("Paragraph texts:")
for p in paragraphs:
    print(p.text.strip())