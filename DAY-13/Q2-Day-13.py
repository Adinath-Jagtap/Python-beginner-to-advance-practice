# 2) Parse JSON response from API
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

# GET and parse JSON
resp = requests.get(url)
resp.raise_for_status()  # raise HTTPError for bad responses

data = resp.json()  # convert JSON body into Python dict/list
print("Parsed JSON keys:", list(data.keys()))
print("Title:", data.get("title"))
print("Body (first 100 chars):", data.get("body")[:100])
