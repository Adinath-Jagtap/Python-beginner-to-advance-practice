# 3. Sort a dictionary by its values in descending order and print the top 3 items

sample = {"apple": 5, "banana": 12, "cherry": 3, "date": 20, "elderberry": 9}

top3 = sorted(sample.items(), key=lambda kv: kv[1], reverse=True)[:3]
print("Top 3:", top3)