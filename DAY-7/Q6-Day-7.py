# Q6 Create class with multiple methods

class Student:
    def __init__(self,id,name,age): #contructor
        self.id = id
        self.name = name
        self.age = age 
    
    def display(self): #display function
        print("Id:",self.id)
        print("Name:",self.name)
        print("Age:",self.age)

    def is_voter(self): #is_voter method/function to find whether student is eligible or not.
        if self.age >= 18 :
            print(self.name,"is eligible to vote.")
        else:
            print(self.name,"is not eligible to vote.")

#creating objects 
student1 = Student(1,"Ram",20)
student2 = Student(2,"Laxman",18)
student3 = Student(3,"Sita",17)

#calling methods
student1.display()
student1.is_voter()
print("-------------------------------------------------------")
student2.display()
student2.is_voter()
print("-------------------------------------------------------")
student3.display()
student3.is_voter()
print("-------------------------------------------------------")