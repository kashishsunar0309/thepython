class Car():
    def __init__(self,brand,year,price):
        self.brand = brand
        self.year = year
        self.price = price
s = Car(['BMW',"Feraeri","Mercedes","Bugatti"],[2022,2019,2014,2015],['95k$','145k$','245k$','650k$'])
print("Please, Search Name detail like : BMW,Feraeri,Mercedes,Bugatti other aren't available in stock for now")
car_name = input("Enter the name of car: ").lower()
brand_name = [b.lower() for b in s.brand ]#new_list = [expression for item in iterable]

if car_name in brand_name:
    search = brand_name.index(car_name)#index for search string in list
    print("Brand:",s.brand[search])
    print("Year: ",s.year[search])
    print("Price: ",s.price[search])
else:
    print("Car haven't in stock. Thank you for Visit Our sites")