x = int(input("enter the value of x: "))
y = int(input("enter the valuue of y: "))
oper = input("enter the sign of operator : ")
if oper == "+":
    print(x+y)
elif oper == "-":
    print(x-y)
    
elif oper == "*":
    print(x*y)
elif oper == "/":
    if y != 0:
        print(x/y)
    else:
        print("It is infinite so that doesn't appear")
else:
    print("Invalid operator")
