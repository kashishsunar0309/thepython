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