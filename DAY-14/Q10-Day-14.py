# 10) Scrape multiple pages in loop — commented version
import requests
from bs4 import BeautifulSoup

base_url = "https://jsonplaceholder.typicode.com/posts/{}"

for post_id in range(1, 6):  # simulate pagination
    url = base_url.format(post_id)
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    print(f"Post {post_id} title:", data["title"])