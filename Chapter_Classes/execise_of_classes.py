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
        self.odometer_reading = 0

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_new_car = Car('porsche', 'A4', 2020)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()