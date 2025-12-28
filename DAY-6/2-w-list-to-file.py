# Q2 Write list to file (one item per line)

# taking input of sentance
list1 = list(input("Text to write in file: ").split())

#opening example.txt in writing mode
with open("DAY-6/required files/example.txt", "w+") as file:
    for i in list1:
        file.write(f"{i}\n") #printing on seperate line

#printing done when content is written
print("DONE")    

#opening the txt file and printing content of text file
with open("DAY-6/required files/example.txt", "r") as file:
    content = file.read()
    print(content)