# Q2 Count occurrences of character in string

#input from user
string1 = str(input("Enter the sstring: "))
lower = string1.lower()

counted_list = []
#counting frequency each character
print("Frequency of each character: ") 
for i in lower :
    if i in counted_list:
        continue
    else:
        print(i,":",lower.count(i))
        counted_list.append(i)