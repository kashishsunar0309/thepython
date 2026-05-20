# input () function works
message = input("tell me something about message:")
print(message)
# 2 example
name = input("please enter the your name:")
print(f"\n hello, {name}")
# 3
prompt = "if you share your name ,we can personalize the messsage you see"
prompt += "\n what is your first name :"
name = input(prompt)
print(f"\n hello ,{name}!")
# 4 using int()
age = int(input("how old are  you "))
print(f"age:{age}")
# 5
height = int(input("enter your heighr in cente meter: "))
print(f"height in cm is {height}")
if 170 <= height < 206:
    print("you are taller")
else:
    print("you are short")
# modules
number = int(input("enter a number, i will tell you even or odd: "))
if number % 2 == 0:
    print("even")
else:
    print("odd")
#the while loop in action execise 
current_number = 1
while current_number<=5:
    print(current_number)
    current_number +=1
#letting the user choose when to quit
prompt= "\n Tell me something , and I will repeat it back to you: "
prompt+="\n Enter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
#2 with using if statement
prompt= "\n Tell me something , and I will repeat it back to you: "
prompt+="\n Enter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
#using break to Exist a loop
prompt= "\n please tell me the name of a city you have visited : "
prompt+="\n Enter 'quit' when you finished : "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
#using continue in a loop
current_number = 0
while current_number <10:
    current_number +=1
    if current_number %2 == 0:
        continue
    print(current_number)
#moving Items from one list to Another

unconfirmed_users = ['alice','brian','candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying users : {current_user.title()}")
    confirmed_users.append(current_user)
print("\n The following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
#Removing All instance of specific value from a list
pets = ['cat','dog','mouse','rabbit','cat','cow','penguien']
print(pets)
print()
while "cat" in pets :
    pets.remove('cat')   
print("== the list of cat remove===")
print(pets)
#feeling a dictonary with user Input
responses ={}
polling_active = True
while polling_active:
    name = input("\nwhat is your name ?: ")
    response= input("\n which mountain would you like to climb someday : ")
    responses[name]=response
    repeat = input("\n would you like  to let another person respond? (yes/no):   ")
    if repeat == "no":
        polling_active =False
    print("\n == polling Results == ")
    for name, response in responses.items():
        print(f"{name} would you like to climb {response},") 