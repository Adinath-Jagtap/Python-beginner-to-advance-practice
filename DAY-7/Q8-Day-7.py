# Q8 Method overriding in child class

#creating Vehicle class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self): #method
        print(f"{self.brand} vehicle is starting")

#creating Car class that inheritance Vehicle class
class Car(Vehicle):
    def start(self):  # Override parent method
        print(f"{self.brand} car is starting with key")

#creating Bike class that inheritance Vehicle class
class Bike(Vehicle):
    def start(self):  # Override parent method
        print(f"{self.brand} bike is starting with kick")

#creating object
car = Car("Toyota")
bike = Bike("Honda")

car.start()   # Toyota car is starting with key
bike.start()  # Honda bike is starting with kick