class Ticket:
    def __init__(self, movie_name, movie_ticket_price, ticket_amount, language = "Geo"):
        self.movie_name = movie_name
        self.movie_ticket_price = movie_ticket_price
        self.ticket_amount = ticket_amount
        self.language = language
    def __str__(self):
        return f"Es aris filmi. Saxelia - {self.movie_name}. :)"

class User:
    def __init__(self, username, money_balance):
        self.username = username
        self.money_balance = money_balance
    def __str__(self):
        return f"Momxmareblis saxeli aris - {self.username}. Da balancze tanxa aris - {self.money_balance}. :)"
    def deposit(self, money_to_deposit):
        self.money_balance += money_to_deposit
    def tickets(self, other):
        if self.ticket_amount.__lt__(other.ticket_amount):
            return "Pirveli filmis biletebi ufro mnakalebia vidre meore filmis biletebi. :)"
        elif other.ticket_amount.__lt__(self.ticket_amount):
            return "Meore filmis biletebi ufro naklebia vidre pirveli filmis biletebi. :)"
        else:
            return "Pirvel da meore films erti raodenobis biletebi darchat. :)"
        if self.ticket_amount > 10:
            return "Pirveli filmis biletebis raodenoba 10ze metia. :)"
        elif self.ticket_amount < 10:
            return "Pirveli filmis biletebis raodenoba naklebia 10ze. :)"
        else:
            return "Pirveli filmistvis darcha 10 bileti. :)"
        if other.ticket_amount > 5:
            return "Meore filmis biletebis raodenoba 5ze metia. :)"
        elif other.ticket_amount < 5:
            return "Meore filmis biletebis raodenoba naklebia 5ze. :)"
        else:
            return "Meore filmistvis darcha 5 bileti. :)"
    def __add__(self, other):
        a = self.ticket_amount + other.ticket_amount
        return f"Orive films ertad aqvs - {a} raodenobis bileti. :)"
    def buy_tickets(self, buy_ticket_amount, ticket):
        if buy_ticket_amount * self.movie_ticket_price <= self.money_balance and buy_ticket_amount <= self.ticket_amount:
            self.money_balance -= buy_ticket_amount * self.movie_ticket_price
            self.ticket_amount -= buy_ticket_amount
            return f"Tqven sheisyidet - {buy_ticket_amount} bileti. :)"
        elif buy_ticket_amount * self.movie_ticket_price > self.money_balance:
            return "Ver moxerxda shesyidva imitom rom sakmarisi tanxa ar aris balance-ze. :("
        else:
            return "Ver moxerxda shesyidva radgan amdeni biketi ar aris. :("


movie1 = Ticket("filmi1", 20, 15, "Eng")
movie2 = Ticket("filmi2", 30, 23)
user1 = User("Nia", 200)
print(user1)
print(movie1)
print(user1.buy_tickets(movie1, 3))