# simple message of python
message = "hello, i am  learning python!"
print(message)
# two line of python
message_1 = "python is awesome"
print(message_1)
message_2 = "I love programming"
print(message_2)
# personal message
name = "Eric"
the_message = f"hello {name},would you like to learn some python today?"
print(the_message)
# name cases
name_1 = "ada lovelace"
print(name_1.lower())
print(name_1.upper())
print(name_1.title())
# famous quote
famous_person = "Albert Einstein"
message_4 = f'{famous_person} one said,"A person who never make a mistake never tried anything new."'
print(message_4)
# counting to twenty
for number in range(1, 22):
    print(number)

# one million
numbers = list(range(1, 101))
for number in numbers:
    print(number)
# summing a Million
numbers = list(range(1, 101))
print(f"Minimum:{min(numbers)}")
print(f"Maximum : {max(numbers)}")
print(f"Sum :{sum(numbers)}")
# ODD numbers
print("odd number\n")
odd_numbers = list(range(1, 21, 2))
for number in odd_numbers:
    print(number)
# Threes
print("three range\n")
threes = list(range(3, 31, 3))
for number in threes:
    print(number)
# cubes
print("cubes*3==\n")
cubes = []
for number in range(1, 11):
    cubes.append(number**3)
for cube in cubes:
    print(cube)
# cube comprehension
print("=== cube comprehension==\n")
cubes = [number**3 for number in range(1, 11)]
print(cubes)
# Slices
my_list = ['pizza', 'falafel', 'carrot', 'cannoli', 'ice cream', 'tiramisu']
print("The first three item in the list are:")
print(my_list[:3])
print("\n three item from the  middle list are:")
print(my_list[2:5])
print("\nThe last three item in the list are:")
print(my_list[-3:])
# My pizzas,your pizzas
pizzas = ['pepperoni', 'margherita', 'hawaiian']
friends_pizzas = pizzas.copy()
pizzas.append('veggie')
friends_pizzas.append('meat lovers')
print("MY favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("\n MY friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print(pizza)
# MORE LOOPs
foods = ['pizza', 'falafel', 'carrot', 'cannoli', 'ice cream', 'tiramisu']
print("My favorite====foods are:")
for food in foods:
    print(food)
print("\n My friend's Ram == favorite foods are:")
for food in foods:
    print(food)
