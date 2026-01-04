# 8) Save API response to JSON file 
import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
resp = requests.get(url)
resp.raise_for_status()

data = resp.json()  # usually a list for this endpoint

# Save to file with pretty formatting
out_path = "api_posts.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Saved {len(data)} items to {out_path}")
