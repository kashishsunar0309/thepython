# The Car class
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


# Instance as Attribute
class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery.")
    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")
        
        
# Inheritance
#9-10 Import file of Restaurant
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()  # composition
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
    def open_restaurant(self):
        print(f"{self.restaurant_name}is now open !")
    def set_number_served(self,number):
        self.number_served = number
    def increment_number_served(self,amount):
        self.number_served += amount
#9-11 User_Admin for import file
class User:
    """A simple model of a user profile."""
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\nUser: {self.first_name} {self.last_name}")
        print(f"  Age: {self.age}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting."""
        print(f"Welcome back, {self.first_name}!")

class Privileges:
    """A class to store an administrator's privileges."""
    def __init__(self, privileges=None):
        if privileges is None:
            self.privileges = [
                "can add post", 
                "can delete post", 
                "can ban user"
            ]
        else:
            self.privileges = privileges

    def show_privileges(self):
        """Display the privileges in this class."""
        print("\nAdministrator Privileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")

class Admin(User):
    def __init__(self, first_name, last_name, age, email, location):
        super().__init__(first_name, last_name, age, email, location)
        self.privileges = Privileges()
