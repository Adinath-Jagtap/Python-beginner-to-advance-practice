# Q4 Copy content from one file to another

#reading the file and storing it in content
with open("DAY-6/required files/example.txt", "r") as file:
    content = file.read()

#writing the file content in content.txt
with open("DAY-6/required files/example-Q4.txt", "w+") as file:
    file.write(content)