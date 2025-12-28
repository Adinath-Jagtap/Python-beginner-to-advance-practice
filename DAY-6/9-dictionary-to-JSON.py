# Q9 Write Dictionary to JSON

import json

# Sample JSON
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "hobbies": ["reading", "coding"]
}

# Write to file
with open("DAY-6/required files/data-Q9.json", "w") as file:
    json.dump(data, file, indent=4)