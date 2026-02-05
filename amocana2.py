f = open("amoc2.txt", "r")
count = 0
for i in f:
    for j in i:
        count += 1
print(count)
print(f)
f.close()