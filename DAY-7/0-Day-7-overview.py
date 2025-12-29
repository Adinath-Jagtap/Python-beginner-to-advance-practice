<<<<<<< HEAD
=======
'''
DAY 7: Python OOP Basics - Classes & Objects
'''

# =============================================================================
# OBJECT-ORIENTED PROGRAMMING (OOP)
# =============================================================================
'''
OOP is a programming paradigm based on "objects" containing data and code.

Four Pillars of OOP:
1. Encapsulation - Bundling data and methods together
2. Inheritance - Creating new classes from existing ones
3. Polymorphism - Same interface, different implementations
4. Abstraction - Hiding complex implementation details

Key Concepts:
- Class: Blueprint for creating objects
- Object: Instance of a class
- Attribute: Variable belonging to a class
- Method: Function belonging to a class
'''


# =============================================================================
# CLASSES AND OBJECTS - BASICS
# =============================================================================

# --- Creating a Simple Class ---
class Dog:
    pass  # Empty class

# Create object (instance) of class
my_dog = Dog()
print(type(my_dog))  # <class '__main__.Dog'>


# --- Class with Attributes ---
class Person:
    # Class attributes (shared by all instances)
    species = "Homo sapiens"
    
    # These are just default attributes (not instance-specific)
    name = "Unknown"
    age = 0

# Create object
person1 = Person()
print(person1.name)      # "Unknown"
print(person1.species)   # "Homo sapiens"


# --- Class with Methods ---
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

# Create object and call methods
calc = Calculator()
result = calc.add(5, 3)
print(result)  # 8


# =============================================================================
# THE __init__() CONSTRUCTOR
# =============================================================================
'''
__init__() is a special method called when object is created.
- Automatically called during object creation
- Used to initialize object attributes
- 'self' refers to the instance being created
'''

# --- Basic Constructor ---
class Student:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

# Create objects with different values
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

print(student1.name)  # "Alice"
print(student2.age)   # 22


# --- Constructor with Default Parameters ---
class Book:
    def __init__(self, title, author, pages=0):
        self.title = title
        self.author = author
        self.pages = pages

book1 = Book("Python Guide", "John Doe")
book2 = Book("Data Science", "Jane Smith", 350)

print(book1.pages)  # 0 (default)
print(book2.pages)  # 350


# =============================================================================
# INSTANCE VARIABLES AND METHODS
# =============================================================================

# --- Instance Variables ---
# Variables unique to each instance
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand    # Instance variable
        self.model = model    # Instance variable
        self.year = year      # Instance variable
        self.mileage = 0      # Instance variable with default

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2021)

car1.mileage = 15000
car2.mileage = 8000

print(car1.brand, car1.mileage)  # Toyota 15000
print(car2.brand, car2.mileage)  # Honda 8000


# --- Instance Methods ---
# Methods that work with instance variables
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        """Add money to account"""
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        """Remove money from account"""
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance
    
    def get_balance(self):
        """Return current balance"""
        return self.balance

# Create and use object
account = BankAccount("Alice", 1000)
account.deposit(500)
print(account.get_balance())  # 1500
account.withdraw(200)
print(account.get_balance())  # 1300


# =============================================================================
# CLASS WITH MULTIPLE METHODS
# =============================================================================

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        """Calculate area"""
        return self.length * self.width
    
    def perimeter(self):
        """Calculate perimeter"""
        return 2 * (self.length + self.width)
    
    def is_square(self):
        """Check if rectangle is a square"""
        return self.length == self.width
    
    def scale(self, factor):
        """Scale the rectangle"""
        self.length *= factor
        self.width *= factor
    
    def display_info(self):
        """Display rectangle information"""
        print(f"Rectangle: {self.length} x {self.width}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")

# Usage
rect = Rectangle(5, 3)
print(rect.area())        # 15
print(rect.perimeter())   # 16
print(rect.is_square())   # False
rect.display_info()


# =============================================================================
# CLASS VARIABLES VS INSTANCE VARIABLES
# =============================================================================

class Employee:
    # Class variable (shared by ALL instances)
    company_name = "Tech Corp"
    employee_count = 0
    
    def __init__(self, name, salary):
        # Instance variables (unique to each instance)
        self.name = name
        self.salary = salary
        Employee.employee_count += 1  # Modify class variable
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")
        print(f"Company: {Employee.company_name}")

# Create objects
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

# Class variable is same for all instances
print(emp1.company_name)  # "Tech Corp"
print(emp2.company_name)  # "Tech Corp"
print(Employee.employee_count)  # 2

# Instance variables are different
print(emp1.name)  # "Alice"
print(emp2.name)  # "Bob"

# Modifying class variable affects all instances
Employee.company_name = "New Tech Corp"
print(emp1.company_name)  # "New Tech Corp"
print(emp2.company_name)  # "New Tech Corp"

# Modifying through instance creates new instance variable
emp1.company_name = "Different Corp"
print(emp1.company_name)  # "Different Corp" (instance variable)
print(emp2.company_name)  # "New Tech Corp" (class variable)
print(Employee.company_name)  # "New Tech Corp" (class variable)


# =============================================================================
# INHERITANCE
# =============================================================================
'''
Inheritance allows a class to inherit attributes and methods from another class.

- Parent Class (Base/Super Class): Class being inherited from
- Child Class (Derived/Sub Class): Class that inherits

Benefits:
- Code reusability
- Logical hierarchy
- Method overriding
'''

# --- Basic Inheritance ---
# Parent class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some generic sound"
    
    def info(self):
        return f"{self.name} is a {self.species}"

# Child class inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        self.name = name
        self.species = "Dog"
        self.breed = breed
    
    # Child has access to parent methods
    # Can also add its own methods
    def fetch(self):
        return f"{self.name} is fetching the ball!"

# Create child object
dog = Dog("Buddy", "Golden Retriever")
print(dog.info())        # "Buddy is a Dog" (inherited method)
print(dog.fetch())       # "Buddy is fetching the ball!" (own method)


# --- Inheritance with Multiple Classes ---
# Parent class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start(self):
        return f"{self.brand} {self.model} is starting"
    
    def stop(self):
        return f"{self.brand} {self.model} is stopping"

# Child class 1
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        self.brand = brand
        self.model = model
        self.doors = doors
    
    def honk(self):
        return "Beep beep!"

# Child class 2
class Motorcycle(Vehicle):
    def __init__(self, brand, model, has_sidecar):
        self.brand = brand
        self.model = model
        self.has_sidecar = has_sidecar
    
    def wheelie(self):
        return "Doing a wheelie!"

# Create objects
car = Car("Toyota", "Camry", 4)
bike = Motorcycle("Harley", "Davidson", False)

print(car.start())    # Inherited method
print(car.honk())     # Own method
print(bike.start())   # Inherited method
print(bike.wheelie()) # Own method


# =============================================================================
# METHOD OVERRIDING
# =============================================================================
'''
Method overriding: Child class provides its own implementation of parent's method.
- Same method name as parent
- Different implementation
- Child's version is used when called on child object
'''

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some generic animal sound"
    
    def info(self):
        return f"This is {self.name}"

# Child class overrides speak() method
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class Cow(Animal):
    def speak(self):
        return f"{self.name} says Moo!"

# Create objects
dog = Dog("Buddy")
cat = Cat("Whiskers")
cow = Cow("Bessie")

# Each uses their own overridden method
print(dog.speak())  # "Buddy says Woof!"
print(cat.speak())  # "Whiskers says Meow!"
print(cow.speak())  # "Bessie says Moo!"

# Inherited method still works
print(dog.info())   # "This is Buddy"


# =============================================================================
# THE super() FUNCTION
# =============================================================================
'''
super() allows you to call parent class methods from child class.
- Access parent's methods and constructor
- Useful when extending (not replacing) parent functionality
- Proper way to initialize parent class
'''

# --- Using super() in Constructor ---
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call parent constructor
        self.student_id = student_id
    
    def display(self):
        super().display()  # Call parent method
        print(f"Student ID: {self.student_id}")

# Create student
student = Student("Alice", 20, "S12345")
student.display()
# Output:
# Name: Alice, Age: 20
# Student ID: S12345


# --- Using super() to Extend Methods ---
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def display(self):
        print(f"Rectangle: {self.length} x {self.width}")
        print(f"Area: {self.area()}")

class ColoredRectangle(Rectangle):
    def __init__(self, length, width, color):
        super().__init__(length, width)  # Initialize parent
        self.color = color
    
    def display(self):
        super().display()  # Call parent's display
        print(f"Color: {self.color}")  # Add extra info

# Create colored rectangle
rect = ColoredRectangle(5, 3, "Red")
rect.display()
# Output:
# Rectangle: 5 x 3
# Area: 15
# Color: Red


# --- super() with Method Enhancement ---
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    
    def deposit(self, amount):
        # Add interest before depositing
        bonus = amount * self.interest_rate
        total = amount + bonus
        return super().deposit(total)  # Call parent's deposit

# Create savings account
savings = SavingsAccount("Alice", 1000, 0.05)
print(savings.balance)  # 1000
savings.deposit(100)    # Deposits 100 + 5 (5% interest)
print(savings.balance)  # 1105


# =============================================================================
# SPECIAL METHODS (MAGIC METHODS)
# =============================================================================
'''
Special methods with double underscores (dunder methods).
Allow operator overloading and special behavior.
'''

# --- __str__() and __repr__() ---
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        """String representation for users"""
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        """String representation for developers"""
        return f"Book('{self.title}', '{self.author}')"

book = Book("Python Guide", "John Doe")
print(str(book))   # 'Python Guide' by John Doe
print(repr(book))  # Book('Python Guide', 'John Doe')


# --- __len__() ---
class Playlist:
    def __init__(self):
        self.songs = []
    
    def add_song(self, song):
        self.songs.append(song)
    
    def __len__(self):
        return len(self.songs)

playlist = Playlist()
playlist.add_song("Song 1")
playlist.add_song("Song 2")
print(len(playlist))  # 2


# --- Operator Overloading ---
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Overload + operator"""
        return Point(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  # Uses __add__ method
print(p3)  # Point(4, 6)


# =============================================================================
# ENCAPSULATION - PUBLIC, PROTECTED, PRIVATE
# =============================================================================
'''
Python naming conventions for access control:
- public: normal name (accessible everywhere)
- _protected: single underscore (convention: internal use)
- __private: double underscore (name mangling, harder to access)
'''

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner           # Public
        self._account_type = "Savings"  # Protected (convention)
        self.__pin = 1234            # Private (name mangled)
    
    def get_pin(self):
        """Public method to access private variable"""
        return self.__pin
    
    def set_pin(self, new_pin):
        """Public method to modify private variable"""
        if len(str(new_pin)) == 4:
            self.__pin = new_pin
        else:
            print("PIN must be 4 digits")

account = BankAccount("Alice", 1000)
print(account.owner)          # Public: accessible
print(account._account_type)  # Protected: accessible but shouldn't
# print(account.__pin)        # Private: AttributeError

# Access private through public method
print(account.get_pin())      # 1234
account.set_pin(5678)
print(account.get_pin())      # 5678


# =============================================================================
# PROPERTY DECORATORS (@property)
# =============================================================================
'''
@property decorator creates getter, setter, and deleter methods.
Allows controlled access to attributes.
'''

class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        """Getter for radius"""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """Setter for radius"""
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")
    
    @property
    def area(self):
        """Calculated property"""
        return 3.14159 * self._radius ** 2
    
    @property
    def circumference(self):
        """Calculated property"""
        return 2 * 3.14159 * self._radius

# Usage
circle = Circle(5)
print(circle.radius)        # 5 (uses getter)
print(circle.area)          # 78.53975 (calculated)

circle.radius = 10          # Uses setter
print(circle.radius)        # 10
print(circle.area)          # 314.159

# circle.radius = -5        # ValueError


# =============================================================================
# CLASS METHODS AND STATIC METHODS
# =============================================================================

# --- @classmethod ---
# Works with class itself, not instances
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def from_string(cls, date_string):
        """Alternative constructor"""
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)
    
    @classmethod
    def today(cls):
        """Factory method"""
        import datetime
        today = datetime.date.today()
        return cls(today.year, today.month, today.day)

# Regular constructor
date1 = Date(2025, 12, 27)

# Class method as alternative constructor
date2 = Date.from_string("2025-12-27")

# Class method as factory
date3 = Date.today()


# --- @staticmethod ---
# Doesn't work with class or instance, just utility function
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def is_even(num):
        return num % 2 == 0

# Call without creating instance
print(MathOperations.add(5, 3))      # 8
print(MathOperations.is_even(10))    # True


# =============================================================================
# MULTIPLE INHERITANCE
# =============================================================================
'''
A class can inherit from multiple parent classes.
'''

class Flyer:
    def fly(self):
        return "Flying in the sky"

class Swimmer:
    def swim(self):
        return "Swimming in water"

class Duck(Flyer, Swimmer):
    def __init__(self, name):
        self.name = name
    
    def quack(self):
        return "Quack quack!"

# Duck inherits from both Flyer and Swimmer
duck = Duck("Donald")
print(duck.fly())    # From Flyer
print(duck.swim())   # From Swimmer
print(duck.quack())  # Own method


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
'''
CLASSES AND OBJECTS:
✓ Class: Blueprint for creating objects
✓ Object: Instance of a class
✓ Create class: class ClassName:
✓ Create object: obj = ClassName()

CONSTRUCTOR:
✓ __init__(self, params): Initialize object
✓ self: Refers to current instance
✓ Called automatically when object is created

VARIABLES:
✓ Instance variables: Unique to each object (self.var)
✓ Class variables: Shared by all objects (ClassName.var)

METHODS:
✓ Instance methods: Work with instance (self parameter)
✓ Class methods: Work with class (@classmethod, cls parameter)
✓ Static methods: Utility functions (@staticmethod, no self/cls)

INHERITANCE:
✓ class Child(Parent): Inherit from parent
✓ Access parent: super()
✓ Method overriding: Child redefines parent method
✓ Multiple inheritance: class Child(Parent1, Parent2)

ENCAPSULATION:
✓ public: normal_name
✓ protected: _protected_name (convention)
✓ private: __private_name (name mangling)

SPECIAL METHODS:
✓ __init__(): Constructor
✓ __str__(): String representation
✓ __len__(): Length
✓ __add__(): Operator overloading

BEST PRACTICES:
✓ Use __init__ to initialize attributes
✓ Use self for instance attributes/methods
✓ Use super() to call parent methods
✓ One class per file for large projects
✓ Use descriptive class names (PascalCase)
✓ Use @property for controlled attribute access
'''


# =============================================================================
# PRACTICE QUESTIONS
# =============================================================================
'''
1. Create class with attributes and print them
2. Create class with method that returns value
3. Create multiple objects from same class
4. Class with __init__ constructor
5. Class with instance variables and methods
6. Create class with multiple methods
7. Class inheritance (parent and child class)
8. Method overriding in child class
9. Class with class variables vs instance variables
10. Use super() in inheritance
'''

# --- Question 1: Create class with attributes and print them ---
class Car:
    brand = "Toyota"
    model = "Camry"
    year = 2020

car = Car()
print(f"Brand: {car.brand}")
print(f"Model: {car.model}")
print(f"Year: {car.year}")


# --- Question 2: Create class with method that returns value ---
class Calculator:
    def multiply(self, a, b):
        return a * b

calc = Calculator()
result = calc.multiply(5, 3)
print(f"Result: {result}")  # 15


# --- Question 3: Create multiple objects from same class ---
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Alice", 20)
student2 = Student("Bob", 22)
student3 = Student("Charlie", 21)

print(f"{student1.name} is {student1.age} years old")
print(f"{student2.name} is {student2.age} years old")
print(f"{student3.name} is {student3.age} years old")


# --- Question 4: Class with __init__ constructor ---
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        print(f"Book '{self.title}' created!")

book = Book("Python Guide", "John Doe", 350)
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Pages: {book.pages}")


# --- Question 5: Class with instance variables and methods ---
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
    
    def show_balance(self):
        print(f"{self.owner}'s balance: ${self.balance}")

account = BankAccount("Alice", 1000)
account.show_balance()
account.deposit(500)
account.withdraw(200)
account.show_balance()


# --- Question 6: Create class with multiple methods ---
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def is_square(self):
        return self.length == self.width
    
    def display_info(self):
        print(f"Length: {self.length}, Width: {self.width}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")
        print(f"Is Square: {self.is_square()}")

rect = Rectangle(5, 3)
rect.display_info()


# --- Question 7: Class inheritance (parent and child class) ---
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")

class Dog(Animal):
    def __init__(self, name, breed):
        self.name = name
        self.species = "Dog"
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} says: Woof!")

dog = Dog("Buddy", "Golden Retriever")
dog.show_info()  # Inherited method
dog.bark()       # Own method


# --- Question 8: Method overriding in child class ---
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        print(f"{self.brand} vehicle is starting")

class Car(Vehicle):
    def start(self):  # Override parent method
        print(f"{self.brand} car is starting with key")

class Bike(Vehicle):
    def start(self):  # Override parent method
        print(f"{self.brand} bike is starting with kick")

car = Car("Toyota")
bike = Bike("Honda")

car.start()   # Toyota car is starting with key
bike.start()  # Honda bike is starting with kick


# --- Question 9: Class with class variables vs instance variables ---
class Employee:
    # Class variable (shared by all instances)
    company = "Tech Corp"
    employee_count = 0
    
    def __init__(self, name, salary):
        # Instance variables (unique to each instance)
        self.name = name
        self.salary = salary
        Employee.employee_count += 1
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")
        print(f"Company: {Employee.company}")
        print(f"Total Employees: {Employee.employee_count}")

emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

print("Employee 1:")
emp1.display_info()
print("\nEmployee 2:")
emp2.display_info()

# Class variable is same for both
print(f"\nCompany: {Employee.company}")
print(f"Total Employees: {Employee.employee_count}")


# --- Question 10: Use super() in inheritance ---
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
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
>>>>>>> d2cdb0f1161fbd85058bd8c4341b00cc1e2eb9a6
