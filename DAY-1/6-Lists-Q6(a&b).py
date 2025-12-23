#Q6a Min-Max finder
#Q6b Sum of all elements in the list

#input List 
nums = list(map(int , input("Enter the list : ").split(",")))

#Q6a To find Min-Max
print("Numbers:", nums)
print("Min:", min(nums))
print("Max:", max(nums))

#Q6b To find the sum of elements 
print("Sum:", sum(nums))


'''
WORKING FOR EVERY INPUT TYPE

raw = input("Enter numbers: ")

# remove brackets and spaces
clean = raw.strip().replace('(', '').replace(')', '') \
                  .replace('[', '').replace(']', '') \
                  .replace('{', '').replace('}', '')

# split by comma or space
if ',' in clean:
    nums = list(map(int, clean.split(',')))
else:
    nums = list(map(int, clean.split()))

print("Numbers:", nums)
print("Min:", min(nums))
print("Max:", max(nums))
print("Sum:", sum(nums))

'''