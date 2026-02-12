try:
    a = int(input("Enter number1: "))
    b = int(input("Enter number2: "))
    c = int(input("Enter number3: "))
    if a + b > c and a + c > b and b + c > a:
        average = (a + b + c) / 3
        print("Average of these numbers: ", average)
    else:
        raise ValueError("Error")
except:
    print("Error2. ar aris samkutxedi")