# Sample data
nums = [2, 7, 11, 15]
target = 9

# Use a dictionary to store seen numbers
seen = {}

for i, num in enumerate(nums):
    needed = target - num
    if needed in seen:
        print("Indices:", seen[needed], i)
        print("Values:", needed, num)
        break
    seen[num] = i
