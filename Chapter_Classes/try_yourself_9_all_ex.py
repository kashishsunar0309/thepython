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