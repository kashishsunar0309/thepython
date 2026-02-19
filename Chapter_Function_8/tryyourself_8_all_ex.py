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
# 8-6: City and Country
def city_country(city, country):
    return f"{city.title()}, {country.title()}"

print(city_country("mumbai", "india"))
print(city_country("hongkong", "china"))
print(city_country("santiago", "chile"))


# 8-7: Make Album
def make_album(artist_name, album_title, songs=None):
    album = {
        'artist': artist_name,
        'title': album_title
    }
    if songs:
        album['songs'] = songs
    return album

print(make_album('Kashish', 'Desi Girl'))
print(make_album('Ram', 'All Girls Are Same'))
print(make_album('Arijit', 'Aashiqui', songs=12))


# 8-8: User Albums
def make_album1(artist_name, album_title, songs=None):
    album = {
        'artist': artist_name,
        'title': album_title
    }
    if songs:
        album['songs'] = songs
    return album

while True:
    print("\n--- Album Entry ---")
    artist = input("Enter artist name (or 'q' to quit): ")
    if artist == 'q':
        break

    title = input("Enter album title (or 'q' to quit): ")
    if title == 'q':
        break

    print(make_album(artist, title))