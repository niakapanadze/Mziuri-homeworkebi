file1 = open("clients.txt", "r")
file2 = open("Spain_Germany.txt", "w")
emails_2011 = []
countries = []
for line in file1:
    line_listebi = line.strip().split(";")
    name = line_listebi[0]
    email = line_listebi[1]
    country = line_listebi[2]
    year = line_listebi[3][-4:]
    if country == "Spain" or country == "Germany":
        file2.write(name + "\n")
    if year == "2011":
        emails_2011.append(email)
    if country not in countries:
        countries.append(country)
file1.close()
file2.close()
print(emails_2011)
print(countries)