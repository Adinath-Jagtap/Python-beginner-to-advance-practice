#Q10 Use super() in inheritance

#creating Person class
class Person:
    def __init__(self, name, age): #contructor
        self.name = name
        self.age = age
    
    def display(self): #display method
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person): #class Student inherit class Person
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)  # Call parent constructor
        self.student_id = student_id
        self.grade = grade
    
    def display(self):
        super().display()  # Call parent method
        print(f"Student ID: {self.student_id}")
        print(f"Grade: {self.grade}")

class Teacher(Person):
    def __init__(self, name, age, employee_id, subject):
        super().__init__(name, age)  # Call parent constructor
        self.employee_id = employee_id
        self.subject = subject
    
    def display(self):
        super().display()  # Call parent method
        print(f"Employee ID: {self.employee_id}")
        print(f"Subject: {self.subject}")

print("Student Information:")
student = Student("Alice", 20, "S12345", "A")
student.display()

print("\nTeacher Information:")
teacher = Teacher("Mr. Smith", 35, "T98765", "Mathematics")
teacher.display()