class BankAccount:
    """Klasa, która posłuży do symulacji konta bankowego.
    """

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if(amount < self.balance):
            self.balance -= amount
        else:
            print("Operation couldn't be made!")

    def __str__(self):
        return str(self.balance)


my_konto = BankAccount()
print("Account balance at the start:", my_konto)
my_konto.deposit(500)
print("Account balance before the try of withdraw 600 from the deposit:", my_konto)
my_konto.withdraw(600)
print("Account balance before the try of withdraw 300 from the deposit:", my_konto)
my_konto.withdraw(300)
print("Account balance after the withdraw:", my_konto)
