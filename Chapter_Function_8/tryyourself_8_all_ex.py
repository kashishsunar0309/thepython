#8-1 ex tryyourself
def display_message():
    print("I am learning about functions in Python.")
display_message()

#8-2 ex tryyourself
def fav_book(title):
    print(f"One of my favorite books is {title}.")
fav_book("Alice in Wonderland")
#8-3 ex tryyourself
def make_shirt(size,message):
    print(f"the t-shirt size is {size} and color is {message}")
make_shirt("large","hello world!")
    
#8-4
def make_shirt1(size="large",message="I love python"):
    print(f"the sixe is {size} and {message}")
make_shirt1()
make_shirt1(size="medium")
make_shirt1(size="small", message="Go Python!")
#8-5
def describe_city(city,country="USA"):
    print(f"{city} is in {country}.")
describe_city(city="Texas")
describe_city(city="new york")
describe_city(city="Rejkjavik",country="Iceland")
    