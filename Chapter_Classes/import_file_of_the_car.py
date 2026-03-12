'''from the_car import Car
my_new_car = Car('audi','a4',2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()'''
# from here below that import multiple class from a module
from the_car import Car, ElectricCar
my_mustang = Car('FORD',"mustang",2005)
print(my_mustang.get_descriptive_name())
my_leaf = ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())