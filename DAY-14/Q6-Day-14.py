# 6) Find elements by class name
from bs4 import BeautifulSoup

html = """
<ul>
  <li class="item">Apple</li>
  <li class="item">Banana</li>
  <li class="item">Cherry</li>
</ul>
"""

soup = BeautifulSoup(html, "html.parser")

items = soup.find_all(class_="item")

print("Items:")
for item in items:
    print(item.text)