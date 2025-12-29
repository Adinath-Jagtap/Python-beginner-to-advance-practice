# Q9 Class variables vs Instance variables

#creating Employee class
class Employee:
    # Class variable (same for all instances)
    company = "Tech Corp"
    employee_count = 0
    
    def __init__(self, name, salary): #contructor method
        # Instance variables (unique to each instance)
        self.name = name
        self.salary = salary
        Employee.employee_count += 1
    
    def display_info(self): #display method
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")
        print(f"Company: {Employee.company}")
        print(f"Total Employees: {Employee.employee_count}")

#creating objects
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

#calling functions
print("Employee 1:")
emp1.display_info()
print("\nEmployee 2:")
emp2.display_info()

# Class variable is same for both
print(f"\nCompany: {Employee.company}")
print(f"Total Employees: {Employee.employee_count}")