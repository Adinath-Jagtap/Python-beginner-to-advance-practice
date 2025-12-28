# Q3 Count lines/words in file

#reading the file and storing it in content.txt
with open("DAY-6/required files/example.txt", "r") as file:
    content = file.read()

#counting number of words
list1 = content.split()
count = len(list1)
print(count)

#counting number of lines 
list2 = content.split("\n") #use splitlines()
count2 = len(list2)
print(count2)