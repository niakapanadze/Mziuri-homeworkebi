f = open("amoc5.txt", "r")
f2 = open("amoc5(2).txt", "r")
k = f.read()
k2 = f2.read()
f.close()
f2.close()
k3 = k + k2
f3 = open("amoc5(3).txt", "w")
f3.write(k3)