# Q3 Create multiple objects from same class

#creating a class of named Car
class Car:
    fuel_type = "petrol"
    wheels = 4

#creating multiple objects of same class
Toyota = Car()
Honda = Car()
Maruthi = Car()

#printing the attributes of each object
print(Toyota.fuel_type,Toyota.wheels)
print(Honda.fuel_type,Honda.wheels)
print(Maruthi.fuel_type,Maruthi.wheels)

#changing the attributes values of objects
Maruthi.fuel_type = "Electric"
Honda.wheels = 2

#printing the attributes values of objects after changing values
print(Toyota.fuel_type,Toyota.wheels)
print(Honda.fuel_type,Honda.wheels)
print(Maruthi.fuel_type,Maruthi.wheels)