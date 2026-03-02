class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Amdeni fuli ar aris angarishze."
        else:
            self.balance -= amount

    def deposit(self, amount):
        if amount > 2500:
            return "Dzaan bevri fulia. 2500-ze naklebi."
        else:
            self.balance += amount

    def display_balance(self):
        return f"{self.owner}-s aqvs {self.balance} fuli."


bank_account = BankAccount("Nia", 100000)
print(bank_account.withdraw(100))
print(bank_account.deposit(100))
print(bank_account.withdraw(1000000))
print(bank_account.deposit(2501))
print(bank_account.display_balance())