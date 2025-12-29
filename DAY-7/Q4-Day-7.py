# Q4 Class with init constructor

#creating a class named Student
class Student:
    def __init__(self, name, age): #__init__ is contructor of class
        self.name = name
        self.age = age

#creating objects
s1 = Student("Raj", 20)
s2 = Student("Rahul", 22)

#printing attributes
print(s1.name, s1.age)
print(s2.name, s2.age)