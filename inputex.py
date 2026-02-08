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
