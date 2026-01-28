file1 = open("oscars.txt", "r")
year = input("Enter a year: ") # string
youngest = 10000
for line in file1:
    line_list = line.strip().split(",")
    if year == line_list[0]:
        print(line_list[3])
    age = int(line_list[2])
    if age < youngest:
        youngest = age
print(youngest, line_list[2], line_list[3])
file1.close()