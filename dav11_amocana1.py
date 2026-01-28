f = open("amocana1.txt", "r")
for line in f:
    num = int(line.strip())
    print(num*num)
f.close()