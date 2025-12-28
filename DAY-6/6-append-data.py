# Q6 Append data to existing file

#taking input
line1 = input("Enter text to append in text file: ")

#opening file in append mode
with open("DAY-6/required files/example.txt", "a+") as file:
    file.write(f"{line1}\n") #appending line text in file