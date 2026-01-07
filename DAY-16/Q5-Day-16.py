# 5. Create a parent class Vehicle and a child class Car with method overriding

class Vehicle:
    def __init__(self, make, year):
        self.make = make
        self.year = year
    def start(self):
        return f"{self.make} ({self.year}) engine started."

class Car(Vehicle):
    def __init__(self, make, year, doors):
        super().__init__(make, year)
        self.doors = doors
    def start(self):  # overriding
        base = super().start()
        return f"{base} Car with {self.doors} doors is ready."

v = Vehicle("Generic", 2010)
c = Car("Toyota", 2022, 4)
print(v.start())
print(c.start())