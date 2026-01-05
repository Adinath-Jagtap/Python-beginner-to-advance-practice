# 8) Handle request errors — commented version
import requests
from bs4 import BeautifulSoup

url = "https://example.com/invalid"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    print("Page fetched successfully")
except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.RequestException as e:
    print("Other request error:", e)