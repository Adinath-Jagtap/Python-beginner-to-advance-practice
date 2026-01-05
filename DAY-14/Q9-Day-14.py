# 9) Extract specific div content 
from bs4 import BeautifulSoup

html = """
<div id="profile">
  <h1>Adinath</h1>
  <p>AI & Data Science Student</p>
</div>
"""

soup = BeautifulSoup(html, "html.parser")

profile_div = soup.find("div", id="profile")

print("Profile content:")
print(profile_div.text.strip())