def divide(a = 1, b = 1):
    try:
        answer = a / b
        return answer
    except ZeroDivisionError:
        return "Division by zero can't happen."
    except ValueError:
        return "Enter only numbers"

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print(divide(a, b))