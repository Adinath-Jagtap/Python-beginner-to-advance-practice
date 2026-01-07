# 8. Use a lambda function to filter numbers divisible by both 3 and 5 from a list

nums = list(range(1, 101))
div_by_3_and_5 = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, nums))
print(div_by_3_and_5)  # [15, 30, 45, 60, 75, 90]