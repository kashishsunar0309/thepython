class Car():
    def __init__(self,brand,year,price):
        self.brand = brand
        self.year = year
        self.price = price
s = Car(['BMW',"Feraeri","Mercedes","Bugatti"],[2022,2019,2014,2015],['95k$','145k$','245k$','650k$'])
index = int(input("Enter the index (0-3):"))
print(s.brand[index])
print(s.year[index])
print(s.price[index])
