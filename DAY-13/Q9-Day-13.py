# 9) Add query parameters to request 
import requests

url = "https://jsonplaceholder.typicode.com/comments"

# Query parameters provided via params= (requests will encode them into the URL)
params = {
    "postId": 1,     # filter comments for postId=1
    "_limit": 5      # some APIs support pagination or limiting
}

resp = requests.get(url, params=params)
resp.raise_for_status()
print("Request URL (with params):", resp.url)
print("Number of returned items:", len(resp.json()))