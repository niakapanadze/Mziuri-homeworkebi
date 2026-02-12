try:
    f = open("myresult.txt")
except FileNotFoundError:
    print("mtresult.txt doesn't exist")