# seeing the world
print("===seeing the world===\n")
# created list of place to visit
places = ["Japan", "New Zealand", 'Iceland', 'Peru', "Norway"]
# print original list
print("origianl list.")
print(places)
# print in alphabetic order (without modifying)
print("\n Alphabetic order:")
print(sorted(places))
# show original order is unchanged
print('\n Original order (unchange):')
print(places)
# print in reserve-alphabetic order (without modifying)
print("\n reverse-Alphabetic order:")
print(sorted(places, reverse='True'))
# show original order is still unchange
print("\n Original order(still unchange):")
print(places)
# Reserve the list (modifies the list)
places.reverse()
print("\nReverse list:")
print(places)
# sort alphabetic (modified the list)
places.sort()
print("\n sorted alphabetically:")
print(places)
# sort reverse-alphabetic (modified the list)
print("\n sorted reverse-alpha*betic:")
print(places)
print("\n"+"="*50+"/n")
# moutian list
mountains = ["Everest", "K2", "matterhorn", "killimanjaro"]
# append()
mountains.append("Mont Blanc")
print("\n After append('Mont Blansc'):")
print(mountains)
# insert()
mountains.insert(0, 'fuji')
print("\n After insert(0,'fuji':")
print(mountains)
# remove()-remove specific item
mountains.remove("K2")
print("\n After remove('K2'):")
print(mountains)
# pop()-remove and return last item {doudt}
popped = mountains.pop()
print(f"\n After pop(removed'{popped}'):")
print(mountains)
# pop(index)remove at specific index
popped_index = mountains.pop(2)
print(f"\n After pop(2)(removed'{popped_index}')")
print(mountains)
# sort()-sort permanently
mountains.sort()
print("\nAfter sort():")
print(mountains)
# sort (reverse=True)-sort in reverse
mountains.sort(reverse=True)
print("\nAfter sort(reverse=True):")
print(mountains)
# len()-get length
print(f"\n Length og list:{len(mountains)}")
print("\n"+"="*50+"\n")
# International Error
print("=== The Country:International Error===\n")
test_list = ["apple", "banana", "cherry"]
print("Test list:", test_list)
# International Error -Trying to access index that doesn't exist {doudt}
try:
    print("\n Trying to access index 5...")
    print(test_list[5])  # this will cause an IndexError
except IndexError as e:
    print(f"IndexError occurred:{e}")
    print("Corrected:Accessing Valid index [1]:", test_list[1])
    print("\n"+"="*100 + "\n")
# Pizzas
print("==== The resautrant food: Pizzas====\n")
pizzas = ["pepperoni", "margherita", "hawaiian"]
for pizza in pizzas:
    print(f"I like{pizza}pizza.")
print("\nI really love pizzas!")
print("\n"+"-"*20 + "\n")
# Animals
print("=== Animals ===\n")
animals = ["dog", "cat", "rabbit"]
for animal in animals:
    print(f"A {animal} would make a great pet.")
print("\nAny of these animals would make a great pet!")
print("\n" + "="*50 + "\n")
num = []
a = int(input('enter the number: '))
num.append(a)
b = int(input('enter the number: '))
num.append(b)
print(sum(num))
