#Q10 Function to generate random password

#importing required modules or libaries
import random #for random choosing a element
import string #used to create characters

#password generating function
def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password

#taking input
num = int(input("Enter how many digit or long password u need: "))

#calling the function 
if (str(num) == ""):
    Generated_Password =  generate_password()
else:
    Generated_Password =  generate_password(num)

#printing the result
print(Generated_Password)