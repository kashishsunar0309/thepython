class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sit(self):
        print(f"{self.name} is a now sitting.")
    def rool_over(self):
        print(f"{self.name} roolled over! ")
my_dog = Dog('Willie',6)
your_dog = Dog('lucy',3)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
#multiple Instance
print(f"\n Your dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age}years old.")
your_dog.sit
#working with classes and instances
#The car class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
#setting a default value of a attribute
class car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        return f"{self.make}{self.model}{self.year}"
    def read_odometer(self):
        print(f"This car has {self.odometer_reading}miles on it.")
my_new_car1 = car('bmw','m4','2022')
print(my_new_car1.get_descriptive_name())
my_new_car1.read_odometer()