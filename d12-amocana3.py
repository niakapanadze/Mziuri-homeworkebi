list1 = [1, 2, 3]
try:
    print(list1[5])
except IndexError:
    print("It is not in the list")