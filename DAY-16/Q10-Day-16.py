#10. Scrape all <h1> and <h2> tags from a website and print their text content

from bs4 import BeautifulSoup
import requests

# demo HTML:
html = """
<html><body>
  <h1>Main Title</h1>
  <h2>Subheading 1</h2>
  <h2>Subheading 2</h2>
</body></html>
"""

soup = BeautifulSoup(html, "html.parser")
h1s = [h.get_text(strip=True) for h in soup.find_all("h1")]
h2s = [h.get_text(strip=True) for h in soup.find_all("h2")]
print("H1:", h1s)
print("H2:", h2s)