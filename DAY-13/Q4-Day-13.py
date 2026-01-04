# 4) Make POST request with data 
import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

# JSON payload to send
payload = {
    "title": "My new post",
    "body": "This is the body of the post",
    "userId": 123
}

# Send POST request with JSON (requests will set Content-Type automatically if using json=)
resp = requests.post(url, json=payload)
resp.raise_for_status()

# The API typically returns the created object (or a fake created object for test APIs)
created = resp.json()
print("Created resource ID (or reply):", created.get("id"))
print("Full response JSON:")
print(json.dumps(created, indent=2))
