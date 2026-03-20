#random standard library
from random import choice
player = ['kashish','ram','shyam','deepson','tara','kalam']
first_up = choice(player)
first_up
'''from the_car import Car
my_new_car = Car('audi','a4',2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()'''
# from here below that import multiple class from a module
"""
from the_car import Car, ElectricCar
my_mustang = Car('FORD',"mustang",2005)
print(my_mustang.get_descriptive_name())
my_leaf = ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())
"""
"""
print("===== 9-10 =====")
from the_car import Restaurant
restaurant = Restaurant("The Pizza Place", "Italian")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
"""
# Import only the Admin class from our new module
"""
from the_car import Admin
my_admin = Admin('Sienna', 'Miller', 32, 's.miller@example.com', 'London')
# Show the profile (from User class)
my_admin.describe_user()
# Show the privileges (from Privileges class via the Admin class)
my_admin.privileges.show_privileges()
"""
"""
from the_car import Admin
the_boss = Admin('Dominic', 'Stone', 35, 'd.stone@admin.com', 'Chicago')
# This call works because of the inheritance across modules!
the_boss.describe_user()
the_boss.privileges.show_privileges()
"""
