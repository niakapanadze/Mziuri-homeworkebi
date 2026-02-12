import math
try:
    a = int(input("Enter number1: "))
    b = int(input("Enter number2: "))
    c = int(input("Enter number3: "))
    if a == 0:
        print("a can't be zero")
    else:
        y = b * b - 4 * a * c
        if y > 0:
            x1 = (-b + math.sqrt(y)) / (2*a)
            x2 = (-b - math.sqrt(y)) / (2*a)
            print("sqrt1: ", x1, " and sqrt2: ", x2)
        elif y == 0:
            x = -b / (2*a)
            print("aqrt: ", x)
        else:
            print("there is no sqrt")
except ValueError:
    print("only numbers")