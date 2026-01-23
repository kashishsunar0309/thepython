# Names
# store names of friends in a list
names = ['Alice', 'Bob', 'Charlie', 'Diana']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# greetings
names = ['Alice', 'Bob', 'Charlie', 'Diana']
print(f"hello,{names[0]}! how are you today?")
print(f"hello,{names[1]}! how are you today?")
print(f"hello,{names[2]}! how are you today?")
print(f"hello,{names[3]}! how are you today?")

# your ownlist
# list of favorite transportation
cars = ['Tesla', 'BMW', 'Audi', 'Toyota']
print(f"I love this {cars[0]}! car for automation")
print(f"I love this {cars[1]}! car for engine&style")
print(f"I love this {cars[2]}! car for looks")
print(f"I love this {cars[3]}! car for strong body part")

# changing guest list
guests = ['Albert Einstein', 'Marie Curie', 'Lenardo da vinci']
# print who cannot make it
print(f"\n {guests[1]} can't make the dinner.")
# replace the guest
guests[1] = 'Isaac Newton'
# print new invitation
print(f"\n Dear {guests[0]},you are invited for dinner!")
print(f"\n Dear {guests[1]},you are invited for dinner!")
print(f"\n Dear {guests[2]},you are invited for dinner!")
# add guest
guests.insert(0, 'Nikola Tesla')
guests.insert(2, 'ada lovelace')
guests.append("Stephen Hawking")
for guest in guests:
    print(f"\n Dear {guest},you are invited to dinner!")
    # shrinking guest list
    guests = ['Nikola Tesla', 'Albert Einstein', 'Marie Curie',
              'Lenardo da vinci', 'Isaac Newton', 'Stephen Hawking']
# remove guests until only two remaining guests
while len(guests) > 2:
    removed_guests = guests.pop(2)
    print(f"Sorry {removed_guests},I can't invite you to dinner.")
    # remaining guests
    print(f"\n Dear {guests[0]},you are still invited for dinner!")
    print(f"Dear {guests[1]},you are still invited for dinner!")
# final list of guest who are invited
print(f"Final guest list: {guests}")
# buffet
buffet_foods = ('pizza', 'pasta', 'salad', 'soup', 'bread')
print("The buffet offers:")
for food in buffet_foods:
    print(f"-{food}")
print("\n Trying to change an item....")
# Try to modify one item (this will cause an error)
try:
    buffet_foods[0] = 'burger'
except TypeError as e:
    print(f"Error:{e}")
print("Tuples are immutable and cannot be modified!")
# Replace the menu by rewriting the tuple
print('\n The resturant is changing its menu...')
buffet_foods = ('tacos', 'burritos', 'salad', 'soup', 'rice')
print('\n The new buffet foods:')
for food in buffet_foods:
    print(f"-{food}")
# code review
x = 5
y = 10
if x > y:
    print("\n x is greater")
else:
    print("\n y is greater")
# condition Tests
# test 1:String equality(True)
car = 'subaru'
print('\n Is car == "subaru"? I predict True.')
print(car == 'subaru')
# TESt 2:String inequality(False)
print("\n Is car == 'audi' ? I predict  False.")
print(car == 'audi')
# test 3:String equality with different case(False)
print("\n Is car == 'Subaru'? I predict False.")
print(car == "Subaru")
# test 4:String inequality(True)
print("\n Is car ==\== 'Toyota'? I predict True.")
print(car != 'toyota')
# Test5: Numerical equality (True)
age = 25
print("\n Is age = 25? I predict True.")
print(age == 25)
# Test6 : Numerical inequality (False)
age = 25
print("\n Is age = 30? I predict False.")
print(age == 30)
# Test 7 : Greater than (True)
print("\n Is age>20? I predict True.")
print(age > 20)
# Test 8 : less  than (False)
print("\n Is age>20? I predict False .")
print(age < 20)
# Test 7 : Greater than or equal to (True)
print("\n Is age>=25? I predict True.")
print(age >= 25)
# Test 10: less than or equal to (False)
print("\n Is age <= 20? I predict false")
print(age <= 20)
# More condition
# Test for equality and inequality with strings.
name = "Alice"
print("string equality: name == 'Alice'..", name == 'Alice')
print("string inequality: name != 'Bob'..", name != 'Bob')
# TESt using the lower () method
city = "New York"
print("/n Using lower(): city.lower() == 'new york',,", city.lower() == 'new york')
print("/n Case sensitive: city == 'new york',,", city == 'new york')
# Number tests
num1 = 15
num2 = 20
print("\n Equality : num1 == 15?", num1 == 15)
print("\n INequality : num1 != 20?", num2 != 20)
print("\n Greater than : num2 > 15?", num2 > 15)
print("\n Less  than : num1 < 20?", num1 < 20)
print("\n Greater than or equal to: num2 >= 15?", num2 >= 15)
print("\n Less  than or equal to: num1 <= 20?", num1 <= 20)
# TEST using 'and' keyword
age = 25
income = 5000
print("\n Using 'and':age > 18 and income> 40000?", age > 18 and income > 40000)
print("\n Using 'and':age > 30 and income> 40000?", age > 30 and income > 40000)

# TEST using 'OR' keyword
print("\n Using 'or':age > 30 or income> 40000?", age > 30 or income > 40000)
print("\n Using 'or':age > 30 or income> 40000?", age > 30 or income > 30000)
# Test whether an item is in a list
fruits = ['apple', 'banana', 'orange']
print("\n Item in list: 'apple' in fruits?", 'apple' in fruits)
print("\n Item in list: 'grape' in fruits?", 'grape' in fruits)
# Test whether an item is in not a list
print("\n Item not in list: 'grape' not in fruits?", 'grape'not in fruits)
print("\n Item not in list: 'apple' not in fruits?", 'apple'not in fruits)
