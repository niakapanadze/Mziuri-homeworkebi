f = open("titaniki.txt", "r")
female = 0
male = 0
people = 0
female_survived = 0
female_not_survived = 0
male_survived = 0
male_not_survived = 0
class1 = 0
class2 = 0
class3 = 0
class1_procenti = 0
class2_procenti = 0
class3_procenti = 0
class1_price = 0
class2_price = 0
class3_price = 0
f.readline
for line in f:
    people += 1
    linebi = line.strip().split(",")
    if linebi[4] == "female":
        female += 1
        if linebi[1] == "0":
            female_not_survived += 1
        elif linebi[1] == "1":
            female_survived += 1
    elif linebi[4] == "male":
        male += 1
        if linebi[1] == "0":
            male_not_survived += 1
        elif linebi[1] == "1":
            male_survived += 1
    if linebi[2] == "1":
        class1 += 1
        class1_price += float(linebi[9])
    elif linebi[2] == "2":
        class2 += 1
        class2_price += float(linebi[9])
    else:
        class3 += 1
        class3_price += float(linebi[9])


print("Amount of females -- ", female)
print("Amount of males -- ", male)
female_procenti = female * 100 / people
print("Females -- ", female_procenti, "%")
male_procenti = male * 100 / people
print("Males -- ", male_procenti, "%")
print("Amount of females survived-- ", female_survived)
print("Amount of males survived-- ", male_survived)
print("Amount of females which did not survive-- ", female_not_survived)
print("Amount of males which did not survive-- ", male_not_survived)

female_survived_procenti = female_survived * 100 / female
print("Females survived -- ", female_survived_procenti, "%")
female_not_survived_procenti = female_not_survived * 100 / female
print("Females which did not survive -- ", female_not_survived_procenti, "%")

male_survived_procenti = male_survived * 100 / male
print("Males survived -- ", male_survived_procenti, "%")
male_not_survived_procenti = male_not_survived * 100 / male
print("Males which did not survive -- ", male_not_survived_procenti, "%")

print("Amount of first class passengers -- ", class1)
print("Amount of second class passengers -- ", class2)
print("Amount of third class passengers -- ", class3)

class1_procenti = class1 * 100 / people
print("First class passengers -- ", class1_procenti, "%")
class2_procenti = class2 * 100 / people
print("Second class passengers -- ", class2_procenti, "%")
class3_procenti = class3 * 100 / people
print("Third class passengers -- ", class3_procenti, "%")

price1 = class1_price / class1
price2 = class2_price / class2
price3 = class3_price / class3
print("sashvalo class1 -- ", price1)
print("sashvalo class2 -- ", price2)
print("sashvalo class3 -- ", price3)
print(price1, price2, price3)
#linebi[9] gavyo class1
print(class1, class2, class3)


#'r', 'w', 'a', 'r+', 'a+'

#შექმნის ახალ ფაილს თვითონ და ჩაწერს მაგ რაღაცას

#listს dictში keyდ ვერ გამოვიყენებთ. და tupleს კი. კიდე tupleში არ იცვლება და listში კი იცვლება და append შეიძლება

#key