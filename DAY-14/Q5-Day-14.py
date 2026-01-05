# 5) Extract data using CSS selectors
from bs4 import BeautifulSoup

html = """
<div class="card">
  <h2>Product A</h2>
  <p class="price">₹500</p>
</div>
"""

soup = BeautifulSoup(html, "html.parser")

# CSS selector for class
price = soup.select_one(".price").text

print("Price:", price)