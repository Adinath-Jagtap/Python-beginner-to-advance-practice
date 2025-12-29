# Q5 Class with instance variables and methods

#creating class Student 
class Student:
    def __init__(self,id,name,age): #contructor
        self.id = id
        self.name = name
        self.age = age 
    
    def display(self): #display function
        print("Id:",self.id)
        print("Name:",self.name)
        print("Age:",self.age)

#creating objects 
student1 = Student(1,"Ram",20)
student2 = Student(2,"Laxman",18)
student3 = Student(3,"Sita",17)

#calling display function/method
student1.display()
print("_____________________________________")
student2.display()
print("_____________________________________")
student3.display()
print("_____________________________________")