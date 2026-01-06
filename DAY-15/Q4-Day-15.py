# 4) Extract all URLs from text
import re

text = "Visit https://example.com or http://sub.example.org/page?q=1. Also check www.example.com (no scheme)."
# Simple URL extractor for http/https; optionally capture www.* without scheme too
url_pattern = r"(https?://[^\s,]+|www\.[^\s,]+)"

urls = re.findall(url_pattern, text)
print("URLs extracted:", urls)