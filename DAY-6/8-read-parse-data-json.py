# Q8 Read JSON file and parse data

import json

with open("DAY-6/required files/data.json", "r", encoding="utf-8") as file:
    data = json.load(file)   # parsing the data

print("Parsed Data:", data)
print("Type:", type(data))

# printing values
print("Name:", data["name"])
print("Age:", data["age"])
print("Course:", data["course"])
print("Skills:", data["skills"])