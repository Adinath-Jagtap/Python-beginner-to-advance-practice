# Q7 Class inheritance (parent and child class)

class Person: #creating a class Person
    def display(self):
        print("I am a person")

class Student(Person): #creating a class Student that inherit class Person
    def study(self):
        print("Student is studying")

s = Student() #creating object

#calling functions
s.display()   # inherited from Person
s.study()     # own method