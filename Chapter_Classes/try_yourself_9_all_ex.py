# Exercise 9-1 & 9-2: Restaurant Class

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, amount):
        self.number_served += amount


# Exercise 9-1: Single instance
print("=== Exercise 9-1 ===")
restaurant = Restaurant("The Golden Fork", "Italian")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Exercise 9-2: Three instances
print("\n=== Exercise 9-2 ===")
restaurant1 = Restaurant("Sakura Garden", "Japanese")
restaurant2 = Restaurant("Spice Route", "Indian")
restaurant3 = Restaurant("Le Petit Bistro", "French")

restaurant1.describe_restaurant()
print()
restaurant2.describe_restaurant()
print()
restaurant3.describe_restaurant()


# Exercise 9-4: Number Served
print("\n=== Exercise 9-4 ===")
restaurant = Restaurant("The Golden Fork", "Italian")
print(f"Customers served so far: {restaurant.number_served}")

restaurant.set_number_served(42)
print(f"After setting directly: {restaurant.number_served}")

restaurant.increment_number_served(75)
print(f"After a busy day (+75 customers): {restaurant.number_served}")


# Exercise 9-3: User Class

class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print("\nUser Profile:")
        print(f"  Name:     {self.first_name} {self.last_name}")
        print(f"  Age:      {self.age}")
        print(f"  Email:    {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        print(f"Welcome back, {self.first_name}! Great to see you.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


print("\n=== Exercise 9-3 ===")
user1 = User("Alice", "Johnson", 28, "alice@email.com", "New York")
user2 = User("Carlos", "Martinez", 35, "carlos@email.com", "Los Angeles")
user3 = User("Priya", "Patel", 22, "priya@email.com", "Chicago")

for user in [user1, user2, user3]:
    user.describe_user()
    user.greet_user()

# Exercise 9-5: Login Attempts
print("\n=== Exercise 9-5 ===")
user = User("Alice", "Johnson", 28, "alice@email.com", "New York")

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts after 3 increments: {user.login_attempts}")

user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts after 2 more: {user.login_attempts}")

user.reset_login_attempts()
print(f"Login attempts after reset: {user.login_attempts}")

#9-6
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type = 'Ice Cream'):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = []
    def display_flavors(self):
        print(f"WELCOME to {self.restaurant_name}!")
        print("We currently have the following flavors available ")
        for flavor in self.flavors:
            print(f"- {flavor}")
print()
print("=== Exercise 9-6: Ice Cream Stand ===")
my_stand = IceCreamStand('Chilly Treats')
my_stand.flavors = ["Madagascar Vanilla", "Midnight Chocolate", "Rocky Road", "Mango Sorbet"]
my_stand.display_flavors()

#9-7
class Admin(User):
    def __init__(self,first_name,last_name,age,email,location):
        super().__init__(first_name,last_name,age,email,location)
        self.privelages = [
            "can add post", 
            "can delete post", 
            "can ban user", 
            "can reset passwords"
        ]
    def show_privileges(self):
        print(f"\n Adminstritive Privages {self.first_name}:")
        for privilege in self.privelages:
            print(f"-{privilege}")
print("\n=== Exercise 9-7: Admin ===")
admin_user = Admin("Dominic", "Stone", 32, "d.stone@system.com", "London")
admin_user.describe_user()
admin_user.show_privileges()
#9-8
class Privileges:
    def __init__(self,privileges=[]):
        self.privileges = privileges if privileges else[
        "can add post","can delete post","can ban user"]
    def show_privileges(self):
        print("\n Privileges: ")
        for privilege in self.privileges:
            print(f"- {privilege}")
class Admin1(User):
    def __init__(self,first_name,last_name,age,email,location):
        super().__init__(first_name,last_name,age,email,location)
        self.privileges = Privileges()
#== Testing c0de ===
print('\n --- Execise 9-8: Privileges class---')
new_admin = Admin1('sarah','conor',45,'ram@gmail.com','new-delhi')
new_admin.privileges.show_privileges()
#9-9
class Battery:
    def __init__(self,battery_size =40):
        self.battery_size = battery_size
    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")
    def upgrade_battery(self):
        if self.battery_size <65:
            print("Upgrading the battery to 65 KWH.")
            self.battery_size = 65
        else:
            print("Battery is already upgraded. ")
class ElectriCar(Restaurant):
    def __init__(self,make,model,year):
        self.battery = Battery()
#====Testing 9-9 ======
print("\n === Execise 9-9 : Battery Upgrade ===")
my_tesla = ElectriCar("Tesla",'Model-3',2024)
print("Checking range with default battery: ")
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
print("Checking range after upgrade.")
my_tesla.battery.get_range()
#9-13 Dice project using class
'''from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        number = randint(1, self.sides)
        print(number)
        
my_die = Die(6)
print("Rolling 10 times:")
for i in range(10): 
    my_die.roll_die()
    ''' 
    # I make that class comment because it need to use of
    # import in top show for execise i used here in all ex like {9-13 to 9-15}
#9-14 This project is for lottery ticket from python using classes
'''
from random import choice
pool = [12,34,54,23,65,76,56,'A','B','C','D','E']
winning_ticket = []
for i in range(4):
    pulled_item = choice(pool)
    winning_ticket.append(pulled_item)
print(f"Any ticket matching {winning_ticket} wins a prize! ")
'''
#9-15 loterry analysis in how many time i get lottery using classes
"""from random import choice
pool = [1,2,3,4,5,6,7,8,9,"a",'b','c','d','e','f']
my_ticket = [2,5,'f','c']
count = 0
won = False
while not won :
    count = count+1
    current_draw = []
    for i in range(4):
        current_draw.append(choice(pool))
    if current_draw == my_ticket:
        won = True
print(f"It took {count} tries to win! ")"""