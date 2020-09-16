class BankAccount:
    """Klasa, która posłuży do symulacji konta bankowego.
    """
    def __init__(self):
        self.balance = 0
    def desposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        if( self.amount < self.balance):
            self.balance -= amount
        else:
            print("Operation couldn't be made!")
    def __str__(self):
        return str(self.balance)
my_konto = BankAccount()
#my_konto.deposit(500)
