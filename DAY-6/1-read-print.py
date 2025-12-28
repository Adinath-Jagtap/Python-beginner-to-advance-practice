# Q1 Read text file and print content

#opening the example.txt file and closing it by default
with open("DAY-6/required files/example.txt", "r") as file: # "r" : reads
    content = file.read()  #reads the whole content
    print(content) #printing the result