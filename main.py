class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self,figure):
        self.balance += figure
    def withdraw(self, figure):
        #you can't cash out not positive number
        if self.balance < figure:
            print("Rejected, not enough money in your bank account")
        else:
            self.balance -= figure
    def printInfo(self):
        print("Hi {}.\n You have ${}.\n Select option:\n 1) Deposit, 2) Withdraw, 3) Exit".format(self.name, self.balance))

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
        running = False