#Q5a String Reverser
#Q5b Palindrome Checker

#input string
string = str(input("Enter the string : "))

#reversing the string - Q5a
reversed_string = string[::-1]
print("Reversed String is : ",reversed_string)

#check whether palindrome or not - Q5b
if string.lower() == reversed_string.lower() :
    print(string + " is palindrome")
else:
    print(string + " is not a palindrome")