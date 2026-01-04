# 5) Handle API errors with try-except
import requests

url = "https://jsonplaceholder.typicode.com/invalid-endpoint"  # intentionally wrong

try:
    resp = requests.get(url, timeout=5)
    resp.raise_for_status()  # raises requests.HTTPError for 4xx/5xx
    data = resp.json()
    print("Success:", data)
except requests.exceptions.HTTPError as e:
    print("HTTP error occurred:", e)            # e.g., 404 Not Found
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.RequestException as e:
    print("Some other requests error occurred:", e)