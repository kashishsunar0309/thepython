#7-1
rental_cars= input("enter the cars name you wanna rent for month: ")
print(f"let's me see if i can find your choice {rental_cars}")
#7-2
seat=int(input("enter the number of people: "))
if seat>8:
   print("you need to wait for a table")
else:
    print("your table is ready")
#7-3
number = int(input("enter the number :"))
if number%10==0:
    print("its is multiple of 10")
else:
    print("its isn't the multiple of 10, sorry try again")