print('======= 6-1 to 3 from dictoinaries ======')


person = {
    'first_name': 'Kashish',
    'last_name': 'Sunar',
    'age': 20,
    'city': 'Kathmandu'
}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])
print('======= the favorite number =====')
print('======= Favorite Numbers =====')
name = {
    "kashish": 18,  # Numbers don't need quotes
    "deepson": 11,
    'hari': 3,
    "kalam": 8,
    'rohan': 9  
}
for person_name, number in name.items():
    print(f"{person_name.title()}'s favorite number is {number}")
print('======= Programming Glossary =====\n')

glossary = {
    'variable': 'A container that stores data values in memory',
    'list': 'An ordered collection of items that can be modified',
    'dictionary': 'A collection of key-value pairs for storing related data',
    'loop': 'A programming structure that repeats a block of code',
    'function': 'A reusable block of code that performs a specific task'
}

# Method 1: Simple printing
for word_2, meaning in glossary.items():
    print(f"{word_2.title()}: {meaning}")

# OR Method 2: More formatted (as the exercise suggests)
for word_2, meaning in glossary.items():
    print(word_2.title())
    print(f"    {meaning}")
glossary = {
    'variable': 'A container that stores data values in memory',
    'list': 'An ordered collection of items that can be modified',
    'dictionary': 'A collection of key-value pairs for storing related data',
    'loop': 'A programming structure that repeats a block of code',
    'function': 'A reusable block of code that performs a specific task',
    'integer':'A whole number, positive or negative, without decimals',
    'string': 'A sequence of characters enclosed in quotes',
    'boolean': 'A data type that can hold one of two values: True or False',
    'tuple':'An ordered, immutable collection of items',
    'method':'A function that is associated with an object and can operate on its data'
}
for item, definition in glossary.items():
    print(f"\n{item.title()}:\n\t {definition}")
    
print('=====rivers=====\n')
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
print(rivers.values())
print('')
name1: dict[str, str] = {
    "kashish": "javascript",
    "deepson": "java",
    "hari": "c++",
    "kalam": "python",
    "rohan": "c++"
}

for person1, language in name1.items():
    if language == "c++":  # Remove .lower() since your values are already lowercase
        print(f"You aren't allowed to poll with this: {person1.title()}")
    else:
        print(f"Thank you for polling: {person1.title()}")