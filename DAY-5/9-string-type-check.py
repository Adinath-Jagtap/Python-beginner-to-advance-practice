# Q9 Check if string contains only digits

#function for checking whether it is digits only or not
def digits_check(str):
    return str.isdigit()

#input
string1 = input("Enter your numberic password: ")

#function call and printing result
if digits_check(string1):
    print("Yes the password is numberic only")
else:
    print("try again")