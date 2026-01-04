# 1) Make GET request to a public API — commented version
import requests

# Example public API (placeholder JSON posts)
url = "https://jsonplaceholder.typicode.com/posts/1"

# Send GET request
response = requests.get(url)

# Check status and print a short result
if response.ok:
    print("Status:", response.status_code)
    print("Response text (first 200 chars):")
    print(response.text[:200])
else:
    print("Request failed with status code:", response.status_code)