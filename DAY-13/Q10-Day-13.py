# 10) Work with API that requires authentication 
import requests
from requests.auth import HTTPBasicAuth

# ----- Method A: API key via header (common pattern) -----
api_url = "https://api.example.com/v1/resource"  # replace with real API
api_key = "YOUR_API_KEY_HERE"   # <- never commit real keys to public repos!

headers = {
    "Authorization": f"Bearer {api_key}",   # or "Api-Key": api_key depending on API
    "Accept": "application/json",
    "User-Agent": "PracticeScript/1.0"
}

# Example call (commented out because api.example.com is placeholder)
# resp = requests.get(api_url, headers=headers)
# resp.raise_for_status()
# print(resp.json())

# ----- Method B: Basic Auth (username/password) -----
auth_url = "https://httpbin.org/basic-auth/user/passwd"
username = "user"
password = "passwd"

# Use HTTPBasicAuth helper
try:
    resp2 = requests.get(auth_url, auth=HTTPBasicAuth(username, password))
    resp2.raise_for_status()
    print("Basic auth succeeded, response JSON:")
    print(resp2.json())
except requests.HTTPError as e:
    print("Auth failed:", e)

# NOTE: For OAuth flows, you'd typically obtain an access token first and then include it as a Bearer token in headers.