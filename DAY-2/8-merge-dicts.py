#Q8 Merge two dictionaries

# --- Merging Dictionaries ---
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"b": 5, "e": 6}                    

#more methods are lists in the DAY-2 overview 
#merging 3 dictionaries
merged = {**dict1, **dict2, **dict3}         # Later dicts override earlier ones

#printing result
print(merged)