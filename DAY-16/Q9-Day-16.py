#9. Make an API call to JSONPlaceholder, extract user emails, and store them in a list

import requests


try:
    resp = requests.get("https://jsonplaceholder.typicode.com/users", timeout=5)
    resp.raise_for_status()
    users = resp.json()
except Exception:
    # fallback sample data if network unavailable
    sample_response = [
        {"id":1,"email":"Sincere@april.biz"},
        {"id":2,"email":"Shanna@melissa.tv"},
        {"id":3,"email":"Nathan@yesenia.net"}
        ]

    users = sample_response

emails = [u["email"] for u in users]
print(emails)
# save to file
with open("Q9-user_emails.txt", "w") as f:
    for e in emails:
        f.write(e + "\n")