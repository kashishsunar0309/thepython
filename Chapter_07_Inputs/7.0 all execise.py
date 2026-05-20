#7-1
rental_cars= input("enter the cars name you wanna rent for month: ")
print(f"let's me see if i can find your choice {rental_cars}")
#7-2
seat=int(input("enter the number of people: "))
if seat>8:
   print("you need to wait for a table")
else:
    print("your table is ready")
#7-3
number = int(input("enter the number :"))
if number%10==0:
    print("its is multiple of 10")
else:
    print("its isn't the multiple of 10, sorry try again")
# Chapter 7 Exercises: 7-4 to 7-6
# While Loops Practice

# ==================== Exercise 7-4: Pizza Toppings ====================
# Basic while loop with quit condition

prompt = "\nPlease choose a pizza topping: "
prompt += "\n(Enter 'quit' when you're finished): "

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(f"I'll add {message} to your pizza.")


# ==================== Exercise 7-5: Movie Tickets ====================
# Using break statement to exit loop

prompt_ticket = "Please enter your age for a ticket\n"
prompt_ticket += "(Enter 'quit' to exit): "

while True:
    age_input = input(prompt_ticket)
    if age_input == 'quit':
        break
    
    age = int(age_input)
    if age < 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")


# ==================== Exercise 7-6: Three Exits ====================

# VERSION 1: Using conditional test in while statement
print("\n--- Version 1: Conditional Test ---")
active = True
while active:
    age_input_v1 = input("Enter your age (or 'quit' to exit): ")
    if age_input_v1 == 'quit':
        active = False
    else:
        age_v1 = int(age_input_v1)
        if age_v1 < 3:
            print("Free ticket!")
        elif age_v1 <= 12:
            print("Ticket: $10")
        else:
            print("Ticket: $15")


# VERSION 2: Using break statement
print("\n--- Version 2: Break Statement ---")
while True:
    age_input_v2 = input("Enter your age (or 'quit' to exit): ")
    if age_input_v2 == "quit":
        break
    
    age_v2 = int(age_input_v2)
    if age_v2 < 3:
        print("Free ticket!")
    elif age_v2 <= 12:
        print("Ticket: $10")
    else:
        print("Ticket: $15")


# VERSION 3: Using continue statement with flag
print("\n--- Version 3: Continue with Flag ---")
keep_running = True
while keep_running:
    age_input_v3 = input("Enter your age (or 'quit' to exit): ")
    
    if age_input_v3 == 'quit':
        keep_running = False
        continue
    
    age_v3 = int(age_input_v3)
    if age_v3 < 3:
        print("Free ticket!")
    elif age_v3 <= 12:
        print("Ticket: $10")
    else:
        print("Ticket: $15")


# ==================== Infinite Loop Example ====================
# Be careful with infinite loops - this one will run forever!
# Uncomment to test (use CTRL+C to stop)
"""
x = 1
while x <= 5:
    print(x)
    # Missing: x += 1 (this would fix the infinite loop)
"""
"""
Deli Sandwich Maker
A program that processes sandwich orders and moves them to finished sandwiches.
"""
#7-8
# List of sandwich orders
sandwich_orders = ["cheese", "vegetarian", "chicken", "veg+meat", "tuna"]
finished_sandwiches = []

print("=== Deli Sandwich Maker ===\n")

# Process each sandwich order
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich.title()} sandwich.")
    finished_sandwiches.append(current_sandwich)
# Display all finished sandwiches
print("\n=== Finished Sandwiches ===")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()}")
#7-9
"""
No Pastrami - Deli runs out of pastrami
"""

# Sandwich orders with pastrami
sandwich_orders = ["cheese", "pastrami", "vegetarian", "pastrami", "chicken", "veg+meat", "pastrami"]

print("Sorry! The deli has run out of pastrami.")

# Remove all pastrami
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

print(sandwich_orders)
#7-10
response = {}
polling_active = True

while polling_active:
    name = input("What is your name boss? \n")
    place = input("Which is your fav place to visit? \n")  # Changed variable name
    response[name] = place  # Store in dictionary
    
    repeat = input("Would you like to let another person respond? yes/no: ")
    if repeat == "no":
        polling_active = False

# This part is OUTSIDE the while loop (unindent it)
print("\n==== Poll Results ====")
for name, place in response.items():  # Use .items() not .title()
    print(f"{name} would like to visit {place}.")