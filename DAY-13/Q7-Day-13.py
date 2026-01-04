# 7) Make multiple API calls in a loop (with basic rate-limit handling)
import requests
import time

base_url = "https://jsonplaceholder.typicode.com/posts/{}"
ids_to_fetch = [1, 2, 3, 4, 5]

results = []
for idx in ids_to_fetch:
    try:
        resp = requests.get(base_url.format(idx), timeout=5)
        if resp.status_code == 429:
            # Example: API says too many requests — backoff then retry once
            print("Rate limited. Sleeping for 2s then retrying...")
            time.sleep(2)
            resp = requests.get(base_url.format(idx), timeout=5)

        resp.raise_for_status()
        results.append(resp.json())
        print("Fetched id", idx)
    except requests.RequestException as e:
        print("Failed to fetch id", idx, ":", e)
    # polite pause between calls to avoid hammering the API
    time.sleep(0.2)

print("Fetched", len(results), "items")
