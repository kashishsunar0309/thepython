# Exercise 9-1 & 9-2: Restaurant Class

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")


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


# Exercise 9-3: User Class

class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    def describe_user(self):
        print("\nUser Profile:")
        print(f"  Name:     {self.first_name} {self.last_name}")
        print(f"  Age:      {self.age}")
        print(f"  Email:    {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        print(f"Welcome back, {self.first_name}! Great to see you.")


print("\n=== Exercise 9-3 ===")
user1 = User("Alice", "Johnson", 28, "alice@email.com", "New York")
user2 = User("Carlos", "Martinez", 35, "carlos@email.com", "Los Angeles")
user3 = User("Priya", "Patel", 22, "priya@email.com", "Chicago")

for user in [user1, user2, user3]:
    user.describe_user()
    user.greet_user()
