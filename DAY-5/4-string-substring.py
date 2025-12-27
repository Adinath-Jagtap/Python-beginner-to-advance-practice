# Q4 Check if string starts/ends with substring

#input
string = input("Enter the string: ").lower()

#substring example
substring = "python"

#checking whether the substring is at start or end of string
start = string.startswith(substring)
end = string.endswith(substring)

#for every possible result
if start == True and end == True:
    print(substring,"is at start and end of input string")
elif start == True :
    print(substring,"is at start of input string")
elif end == True :
    print(substring,"is at end of input string")
else :
    print(substring,"is not at start or end of string")