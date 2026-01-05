# 4) Scrape data from HTML table — commented version
from bs4 import BeautifulSoup

html = """
<table>
  <tr><th>Name</th><th>Score</th></tr>
  <tr><td>Alice</td><td>85</td></tr>
  <tr><td>Bob</td><td>92</td></tr>
</table>
"""

soup = BeautifulSoup(html, "html.parser")

rows = soup.find_all("tr")

print("Table data:")
for row in rows:
    cols = row.find_all("td")
    if cols:
        print(cols[0].text, cols[1].text)
