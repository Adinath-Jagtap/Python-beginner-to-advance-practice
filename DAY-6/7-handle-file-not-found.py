# Q7 Handle file not found error with try-except

try:
    #opening file in read mode
    with open("DAY-6/required files/example1.txt","r") as file:
        content = file.read()
        print(content) #print the content
except FileNotFoundError : #FileNotFoundError checks
    print("File not found") #throws error when file not found