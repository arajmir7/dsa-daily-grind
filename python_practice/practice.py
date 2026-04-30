class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.amount += amount

class SavingAccount(BankAccount):
    def add_interest(self):
        self.balance += self.balance * 0.5
 
