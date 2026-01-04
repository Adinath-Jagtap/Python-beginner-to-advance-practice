# 3) Add headers to API request
import requests

url = "https://httpbin.org/headers"  # httpbin will echo headers back

# Custom headers (example: include a custom header and Accept)
headers = {
    "User-Agent": "MyPracticeScript/1.0",
    "X-My-Header": "PracticeValue",
    "Accept": "application/json"
}

resp = requests.get(url, headers=headers)
resp.raise_for_status()
print("Server received headers:")
print(resp.json()["headers"])
