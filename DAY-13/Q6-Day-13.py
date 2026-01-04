# 6) Extract specific data from nested JSON
# Example nested JSON structure (simulate a response)
response_json = {
    "user": {
        "id": 10,
        "name": "Asha",
        "profile": {
            "email": "asha@example.com",
            "address": {
                "city": "Mumbai",
                "zipcode": "400001"
            }
        },
        "posts": [
            {"id": 1, "title": "First"},
            {"id": 2, "title": "Second"}
        ]
    }
}

# Extract nested values safely using .get() or try/except
user = response_json.get("user", {})
email = user.get("profile", {}).get("email")
city = user.get("profile", {}).get("address", {}).get("city")
first_post_title = None
posts = user.get("posts", [])
if posts:
    first_post_title = posts[0].get("title")

print("Email:", email)
print("City:", city)
print("First post title:", first_post_title)
