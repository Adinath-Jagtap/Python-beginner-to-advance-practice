# 1) Scrape webpage title 
import requests
from bs4 import BeautifulSoup

url = "https://example.com"

response = requests.get(url)
response.raise_for_status()  # raise error if request fails

soup = BeautifulSoup(response.text, "html.parser")

# Extract the <title> tag text
title = soup.title.text

print("Page title:", title)