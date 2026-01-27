car = 'subaru'
print("Is Car == 'subaru'? i predict true")
print(car == 'subaru')  # that the string which we declare in car string so,
# that why it is True
print("\n Is car == 'audi'? I predict False")
print(car == 'audi')  # why False because the car name in car is subaru so,
# audi isn't in car string so that why its print False
# 2
food = 'Rice'
print("Is food == 'Rice'? i predict true")
print(food == 'Rice')
print("\n Is food == 'rice'? I predict False")
# False became that case sensitive so that why complier give False
print(food == 'rice')
# 3
book = 'atomic habit'
print("Is book is 'atomic habit ? i predict True")
print(book == 'atomic habit')
print("\n Is book is == 'dopamine detox'? i predict False")
print(book == 'dopamine detox')
print()
# 4
game = 'free fire'
print(game.upper() == "FREE FIRE")
print(game == 'FREE FIRE')
# 5
game = "FREE FIRE"
print(game.lower() == 'free fire')
print(game == 'free fire')
print()
print("==== 5.2 ===== question")
tvshows = 'MR.ROBOT'
print(tvshows == "MR.ROBOT")  # equality
print(tvshows == 'prison break')  # unequality
print(tvshows.lower() == 'mr.robot')
# numerical
age = 30
print(age != 35)
print(age == 35)
print(age > 40)
print(age < 40)
print(age >= 40)
print(age <= 40)
print()
# and/or
age_1 = 34
age_2 = 25
print(age_1 >= 30 and age_2 <= 30)  # true
print(age_1 >= 56 and age_2 <= 56)  # false
print(age_1 >= 70 or age_2 <= 20)  # false
print(age_1 >= 56 or age_2 <= 56)  # true
print()
# test inlist
print("===== the Tvshows ====")
tvshow = ['prison break', 'money heist', 'breaking bad', "mr.robot",]
print('money heist' in tvshow)
show = "viking"
if show not in tvshow:
    print(f"{show.title()},this tvshow the user doesn't see yet")
