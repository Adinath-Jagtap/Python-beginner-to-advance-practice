#Q5 Function to check string is palindrome

#function for checking string is palindrome or not.
def checker(str):
    str = str.lower()
    reversed_str = str[::-1]
    if (reversed_str == str):
        print(str,"is a palindrome.") #result
    else:
        print(str,"is not a palindrome.") #result

#input and function call
string = str(input("Enter the string: "))
checker(string)