while True:
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        answer = num1 / num2
        print("Num1 diveded by num2:", answer)
        break
    except ValueError:
        print("Enter only numbers")
    except ZeroDivisionError:
        print("Division by zero can't happen")