'''
DAY 7: Python Object-Oriented Programming (OOP) Basics
'''

# =============================================================================
# WHAT IS OOP?
# =============================================================================
'''
Object-Oriented Programming (OOP) is a programming paradigm based on "objects"
which contain data (attributes) and code (methods).

Key Concepts:
- Class: Blueprint for creating objects
- Object: Instance of a class
- Attribute: Data stored in class/object
- Method: Function defined in a class

Benefits:
- Code reusability
- Better organization
- Easier maintenance
- Real-world modeling
- Encapsulation of data
'''


# =============================================================================
# CLASSES AND OBJECTS
# =============================================================================

# --- Basic Class Definition ---
class Dog:
    """A simple Dog class"""
    pass

# Create object (instance)
my_dog = Dog()
print(type(my_dog))  # <class '__main__.Dog'>


# --- Class with Attributes ---
class Car:
    """Car class with attributes"""
    # Class attribute (shared by all instances)
    wheels = 4
    
# Create objects
car1 = Car()
car2 = Car()

print(car1.wheels)  # 4
print(car2.wheels)  # 4

# Modify class attribute
Car.wheels = 6
print(car1.wheels)  # 6
print(car2.wheels)  # 6


# --- Instance Attributes ---
class Person:
    """Person class with instance attributes"""
    pass

# Add attributes to instance
person1 = Person()
person1.name = "Alice"
person1.age = 25

person2 = Person()
person2.name = "Bob"
person2.age = 30

print(person1.name)  # Alice
print(person2.name)  # Bob


# =============================================================================
# __init__ METHOD (Constructor)
# =============================================================================
'''
__init__ is a special method called when object is created.
Used to initialize object attributes.
'''

# --- Basic Constructor ---
class Person:
    def __init__(self, name, age):
        """Initialize person with name and age"""
        self.name = name  # Instance attribute
        self.age = age

# Create objects
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1.name)  # Alice
print(person2.age)   # 30


# --- Constructor with Default Values ---
class Student:
    def __init__(self, name, age=18, grade="A"):
        self.name = name
        self.age = age
        self.grade = grade

student1 = Student("Alice")
student2 = Student("Bob", 20)
student3 = Student("Charlie", 19, "B")

print(student1.age)    # 18 (default)
print(student2.age)    # 20
print(student3.grade)  # B


# --- Understanding 'self' ---
'''
'self' represents the instance of the class.
- Must be first parameter in instance methods
- Used to access instance attributes and methods
- Can be named anything, but 'self' is convention
'''

class Example:
    def __init__(self, value):
        self.value = value  # self refers to current instance
    
    def show(self):
        print(self.value)  # Access instance attribute

obj = Example(10)
obj.show()  # 10


# =============================================================================
# INSTANCE METHODS
# =============================================================================
'''
Methods are functions defined inside a class.
Instance methods operate on instance data.
'''

# --- Basic Instance Methods ---
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        """Calculate area"""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate perimeter"""
        return 2 * (self.width + self.height)
    
    def display(self):
        """Display rectangle info"""
        print(f"Width: {self.width}, Height: {self.height}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")

# Usage
rect = Rectangle(5, 3)
print(rect.area())       # 15
print(rect.perimeter())  # 16
rect.display()


# --- Methods with Parameters ---
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        """Deposit money"""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount")
    
    def withdraw(self, amount):
        """Withdraw money"""
        if amount > self.balance:
            print("Insufficient funds")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount")
    
    def get_balance(self):
        """Get current balance"""
        return self.balance

# Usage
account = BankAccount("Alice", 1000)
account.deposit(500)    # Deposited $500. New balance: $1500
account.withdraw(200)   # Withdrew $200. New balance: $1300
print(account.get_balance())  # 1300


# --- Methods Calling Other Methods ---
class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, value):
        self.result += value
        return self
    
    def subtract(self, value):
        self.result -= value
        return self
    
    def multiply(self, value):
        self.result *= value
        return self
    
    def reset(self):
        self.result = 0
        return self
    
    def get_result(self):
        return self.result

# Method chaining
calc = Calculator()
result = calc.add(10).multiply(5).subtract(20).get_result()
print(result)  # 30


# =============================================================================
# CLASS ATTRIBUTES vs INSTANCE ATTRIBUTES
# =============================================================================

class Employee:
    # Class attribute (shared by all instances)
    company = "TechCorp"
    employee_count = 0
    
    def __init__(self, name, salary):
        # Instance attributes (unique to each instance)
        self.name = name
        self.salary = salary
        Employee.employee_count += 1  # Modify class attribute

# Create employees
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

# Access class attribute
print(emp1.company)  # TechCorp
print(emp2.company)  # TechCorp
print(Employee.company)  # TechCorp

# Access instance attributes
print(emp1.name)     # Alice
print(emp2.salary)   # 60000

# Modify class attribute
Employee.company = "NewTech"
print(emp1.company)  # NewTech
print(emp2.company)  # NewTech

# Count employees
print(Employee.employee_count)  # 2


# --- Instance Attribute Shadows Class Attribute ---
class Example:
    value = 10  # Class attribute

obj1 = Example()
obj2 = Example()

print(obj1.value)  # 10 (from class)
print(obj2.value)  # 10 (from class)

# Create instance attribute (shadows class attribute for this instance)
obj1.value = 20
print(obj1.value)  # 20 (from instance)
print(obj2.value)  # 10 (still from class)
print(Example.value)  # 10 (class attribute unchanged)


# =============================================================================
# CLASS METHODS
# =============================================================================
'''
Class methods work with class attributes.
Defined using @classmethod decorator.
First parameter is 'cls' (refers to class, not instance).
'''

class Student:
    school_name = "ABC School"  # Class attribute
    student_count = 0
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        Student.student_count += 1
    
    @classmethod
    def change_school(cls, new_school):
        """Change school name for all students"""
        cls.school_name = new_school
    
    @classmethod
    def get_student_count(cls):
        """Get total number of students"""
        return cls.student_count
    
    @classmethod
    def from_string(cls, student_string):
        """Alternative constructor from string"""
        name, grade = student_string.split(",")
        return cls(name, int(grade))

# Usage
student1 = Student("Alice", 10)
student2 = Student("Bob", 11)

print(Student.school_name)  # ABC School
Student.change_school("XYZ School")
print(student1.school_name)  # XYZ School

print(Student.get_student_count())  # 2

# Alternative constructor
student3 = Student.from_string("Charlie,12")
print(student3.name)   # Charlie
print(student3.grade)  # 12


# =============================================================================
# STATIC METHODS
# =============================================================================
'''
Static methods don't access instance or class attributes.
Defined using @staticmethod decorator.
No 'self' or 'cls' parameter.
Used for utility functions related to the class.
'''

class MathOperations:
    @staticmethod
    def add(a, b):
        """Add two numbers"""
        return a + b
    
    @staticmethod
    def multiply(a, b):
        """Multiply two numbers"""
        return a * b
    
    @staticmethod
    def is_even(num):
        """Check if number is even"""
        return num % 2 == 0

# Usage (no need to create instance)
print(MathOperations.add(5, 3))        # 8
print(MathOperations.multiply(4, 5))   # 20
print(MathOperations.is_even(10))      # True

# Can also call from instance (but not recommended)
math = MathOperations()
print(math.add(2, 3))  # 5


# --- When to Use Each ---
class Example:
    class_var = "class"
    
    def instance_method(self):
        """Use when you need access to instance data"""
        return self.instance_var
    
    @classmethod
    def class_method(cls):
        """Use when you need access to class data"""
        return cls.class_var
    
    @staticmethod
    def static_method():
        """Use when you don't need instance or class data"""
        return "independent function"


# =============================================================================
# ENCAPSULATION (Public, Protected, Private)
# =============================================================================
'''
Encapsulation is hiding internal details and providing public interface.

Naming Conventions:
- public: normal_attribute (accessible everywhere)
- protected: _protected_attribute (convention: internal use)
- private: __private_attribute (name mangling applied)
'''

# --- Public Attributes ---
class PublicExample:
    def __init__(self):
        self.public_var = "I'm public"

obj = PublicExample()
print(obj.public_var)  # Accessible
obj.public_var = "Modified"  # Can modify


# --- Protected Attributes (Convention) ---
class ProtectedExample:
    def __init__(self):
        self._protected_var = "I'm protected (by convention)"

obj = ProtectedExample()
print(obj._protected_var)  # Still accessible (Python doesn't enforce)
# But convention says: don't access from outside


# --- Private Attributes (Name Mangling) ---
class PrivateExample:
    def __init__(self):
        self.__private_var = "I'm private"
    
    def get_private(self):
        """Public method to access private attribute"""
        return self.__private_var
    
    def set_private(self, value):
        """Public method to modify private attribute"""
        self.__private_var = value

obj = PrivateExample()
# print(obj.__private_var)  # AttributeError
print(obj.get_private())    # I'm private (through method)

# Name mangling: still accessible but discouraged
print(obj._PrivateExample__private_var)  # I'm private


# --- Practical Encapsulation Example ---
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner           # Public
        self._account_number = None  # Protected
        self.__balance = balance     # Private
    
    def deposit(self, amount):
        """Public method to deposit"""
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        """Public method to withdraw"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
    
    def get_balance(self):
        """Public method to view balance"""
        return self.__balance
    
    def __calculate_interest(self):
        """Private method (internal use only)"""
        return self.__balance * 0.05

# Usage
account = BankAccount("Alice", 1000)
print(account.owner)           # Alice (public)
account.deposit(500)           # OK (public method)
print(account.get_balance())   # 1500 (through public method)
# print(account.__balance)     # AttributeError (private)


# =============================================================================
# PROPERTY DECORATORS (Getters and Setters)
# =============================================================================
'''
Properties allow controlled access to attributes.
Makes private attributes accessible like public attributes.
'''

# --- Without Properties (Manual Getters/Setters) ---
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            raise ValueError("Age must be positive")

person = Person("Alice", 25)
print(person.get_age())  # 25
person.set_age(26)
print(person.get_age())  # 26


# --- With Properties (Pythonic Way) ---
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property
    def age(self):
        """Getter for age"""
        return self.__age
    
    @age.setter
    def age(self, age):
        """Setter for age"""
        if age > 0 and age < 120:
            self.__age = age
        else:
            raise ValueError("Age must be between 0 and 120")
    
    @age.deleter
    def age(self):
        """Deleter for age"""
        print("Deleting age")
        del self.__age

# Usage (looks like accessing public attribute)
person = Person("Alice", 25)
print(person.age)      # 25 (calls getter)
person.age = 26        # Calls setter
print(person.age)      # 26
# person.age = -5      # ValueError
del person.age         # Calls deleter


# --- Read-Only Property ---
class Circle:
    def __init__(self, radius):
        self.__radius = radius
    
    @property
    def radius(self):
        return self.__radius
    
    @property
    def area(self):
        """Read-only property (no setter)"""
        return 3.14159 * self.__radius ** 2
    
    @property
    def circumference(self):
        """Read-only property"""
        return 2 * 3.14159 * self.__radius

circle = Circle(5)
print(circle.area)            # 78.53975
print(circle.circumference)   # 31.4159
# circle.area = 100           # AttributeError (no setter)


# --- Computed Properties ---
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @property
    def area(self):
        """Computed on access"""
        return self.width * self.height
    
    @property
    def perimeter(self):
        """Computed on access"""
        return 2 * (self.width + self.height)

rect = Rectangle(5, 3)
print(rect.area)       # 15
rect.width = 10        # Modify width
print(rect.area)       # 30 (automatically updated)


# =============================================================================
# __str__ and __repr__ METHODS
# =============================================================================
'''
__str__: Human-readable string representation
__repr__: Developer-friendly representation (for debugging)
'''

# --- Without __str__ and __repr__ ---
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 25)
print(person)  # <__main__.Person object at 0x...>


# --- With __str__ ---
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        """Return string for end users"""
        return f"{self.name}, {self.age} years old"

person = Person("Alice", 25)
print(person)         # Alice, 25 years old
print(str(person))    # Alice, 25 years old


# --- With __repr__ ---
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        """Return string for developers"""
        return f"Person(name='{self.name}', age={self.age})"

person = Person("Alice", 25)
print(repr(person))   # Person(name='Alice', age=25)
print([person])       # [Person(name='Alice', age=25)]


# --- With Both ---
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        """User-friendly"""
        return f"{self.name}, {self.age} years old"
    
    def __repr__(self):
        """Developer-friendly"""
        return f"Person('{self.name}', {self.age})"

person = Person("Alice", 25)
print(str(person))    # Alice, 25 years old
print(repr(person))   # Person('Alice', 25)
print(person)         # Alice, 25 years old (uses __str__)


# =============================================================================
# SPECIAL/MAGIC METHODS (Dunder Methods)
# =============================================================================
'''
Special methods start and end with double underscores (__).
Allow customization of built-in behavior.
'''

# --- Arithmetic Operators ---
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Enable + operator"""
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Enable - operator"""
        return Point(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """Enable * operator"""
        return Point(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)

p3 = p1 + p2      # Calls __add__
print(p3)         # Point(4, 6)

p4 = p2 - p1      # Calls __sub__
print(p4)         # Point(2, 2)

p5 = p1 * 3       # Calls __mul__
print(p5)         # Point(3, 6)


# --- Comparison Operators ---
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        """Enable == operator"""
        return self.age == other.age
    
    def __lt__(self, other):
        """Enable < operator"""
        return self.age < other.age
    
    def __le__(self, other):
        """Enable <= operator"""
        return self.age <= other.age
    
    def __gt__(self, other):
        """Enable > operator"""
        return self.age > other.age
    
    def __ge__(self, other):
        """Enable >= operator"""
        return self.age >= other.age
    
    def __str__(self):
        return f"{self.name} ({self.age})"

p1 = Person("Alice", 25)
p2 = Person("Bob", 30)
p3 = Person("Charlie", 25)

print(p1 == p3)  # True
print(p1 < p2)   # True
print(p2 > p1)   # True


# --- Container Methods ---
class Basket:
    def __init__(self):
        self.items = []
    
    def __len__(self):
        """Enable len() function"""
        return len(self.items)
    
    def __getitem__(self, index):
        """Enable indexing basket[0]"""
        return self.items[index]
    
    def __setitem__(self, index, value):
        """Enable assignment basket[0] = value"""
        self.items[index] = value
    
    def __contains__(self, item):
        """Enable 'in' operator"""
        return item in self.items
    
    def add(self, item):
        self.items.append(item)

basket = Basket()
basket.add("apple")
basket.add("banana")
basket.add("orange")

print(len(basket))        # 3
print(basket[0])          # apple
basket[1] = "grape"       # Modify
print(basket[1])          # grape
print("apple" in basket)  # True


# --- Callable Objects ---
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        """Make object callable like function"""
        return x * self.factor

multiply_by_5 = Multiplier(5)
print(multiply_by_5(10))  # 50
print(multiply_by_5(3))   # 15


# --- Context Manager ---
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """Called when entering 'with' block"""
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Called when exiting 'with' block"""
        if self.file:
            self.file.close()

# Usage
with FileManager("test.txt", "w") as f:
    f.write("Hello, World!")


# =============================================================================
# CLASS INHERITANCE (Will be covered in OOP Advanced)
# =============================================================================
'''
Brief preview - detailed in next lesson:

class Parent:
    def method(self):
        pass

class Child(Parent):  # Child inherits from Parent
    def method(self):
        pass
'''


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
'''
CLASSES & OBJECTS:
✓ Class: Blueprint for objects
✓ Object: Instance of a class
✓ __init__: Constructor to initialize objects
✓ self: Reference to current instance

ATTRIBUTES:
✓ Class attributes: Shared by all instances
✓ Instance attributes: Unique to each instance
✓ Access with dot notation: object.attribute

METHODS:
✓ Instance methods: Operate on instance (self)
✓ Class methods: Operate on class (@classmethod, cls)
✓ Static methods: Independent utility (@staticmethod)

ENCAPSULATION:
✓ Public: normal_name (accessible everywhere)
✓ Protected: _name (convention: internal use)
✓ Private: __name (name mangling)
✓ Use @property for controlled access

SPECIAL METHODS:
✓ __init__: Constructor
✓ __str__: String representation (user)
✓ __repr__: String representation (developer)
✓ __add__, __sub__: Arithmetic operators
✓ __eq__, __lt__: Comparison operators
✓ __len__, __getitem__: Container methods
✓ __call__: Make object callable

BEST PRACTICES:
- Use meaningful class and method names
- Keep classes focused (single responsibility)
- Use properties instead of getters/setters
- Implement __str__ and __repr__ for debugging
- Use private attributes for internal data
- Document classes and methods with docstrings
- Follow naming conventions (PascalCase for classes)
'''