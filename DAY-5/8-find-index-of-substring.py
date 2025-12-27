# Q8 Find index of substring in string

#take input
string = input("Input: ").lower()
substring = "python" #example

print(string.find(substring)) #returns -1 when not found
print(string.index(substring)) #returns error when not found 