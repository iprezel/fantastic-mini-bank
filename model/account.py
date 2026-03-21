class Account:
    def __init__(self, accountId, name, balance=0):
        self.accountNumber = accountId
        self.name = name
        self.balance = balance
    def deposit(self,figure):
        self.balance += figure
    def withdraw(self, figure):
        if figure < 0: 
            print("Rejected, you can't withdraw non positive amount of money.")
        elif self.balance >= figure:
            self.balance -= figure
            print("Approved.")
            return 1
        elif figure >= self.balance: 
            print("Rejected, not enough money in your bank account.")
        else:
            print("Invalid Operation!")
        return -1
