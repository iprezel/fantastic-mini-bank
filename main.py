import random
class Bank:
    def __init__(self, name, balance):
        self.accountNumber = self.generateAccountNumber()
        self.name = name
        self.balance = balance

    def generateAccountNumber(self):
        countryCode="PL"
        checkDigitals = str(random.randint(10,99))
        accountNumbers = ''.join(str(random.randint(0,9)) for i in range(24))
        return "{}{}{}".format(countryCode, checkDigitals, accountNumbers)
    def deposit(self,figure):
        self.balance += figure
    def withdraw(self, figure):
        if figure < 0: 
            print("Rejected, you can't withdraw non positive amount of money.")
        elif self.balance >= figure:
            self.balance -= figure
            print("Approved.")
        elif figure >= self.balance: 
            print("Rejected, not enough money in your bank account.")
        else:
            print("Invalid Operation!")
    def printInfo(self):
        print("Hi {}.\n You have ${}.\n Select option:\n 1) Deposit, 2) Withdraw, 3) Get your bank account 4) exit".format(self.name, self.balance))
    def printBankAccountNumber(self):
        print("Your bank account number: {}".format(self.accountNumber))
print("Hi this is your KKK bank!")
name = str(input("Enter your name: "))
bankApp = Bank(name, 0)
running = True
while(running):
    bankApp.printInfo()
    getInput = input("Enter option: ")
    if getInput.isnumeric() ==  False:
        continue
    getInput = int(getInput)
    if getInput == 1:
        figure = int(input("Enter the amount to deposit: ")) #to do casting 
        bankApp.deposit(figure)
    elif getInput == 2:
        figure = int(input("Enter the amount to cashed out: "))#same logic
        bankApp.withdraw(figure)
    elif getInput == 3:
        bankApp.printBankAccountNumber()
    elif getInput == 4:
        running = False