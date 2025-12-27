# Q1 Convert string to uppercase/lowercase

#taking input
name = input("Enter the string: ")

#knowing the conversion type
type = input("Choose string to be converted into up:uppercase or low:lowercase :-")

#converting the string
if type == "up" or type == "uppercase":
    print(name.upper())
elif type == "low" or type == "lowercase":
    print(name.lower())
else:
    print("lowercase:",name.lower())
    print("uppercase:",name.upper())
