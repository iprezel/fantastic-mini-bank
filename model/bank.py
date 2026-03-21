import random
from model.account import Account
class Bank:    
    def __init__(self):
        self.accounts = {}

    def generateAccountNumber(self):
        countryCode="PL"
        checkDigitals = str(random.randint(10,99))
        accountNumbers = ''.join(str(random.randint(0,9)) for i in range(24))
        return "{}{}{}".format(countryCode, checkDigitals, accountNumbers)
    
    def getAccount(self, account_id):
        return self.accounts.get(account_id)
    
    def createAccount(self, name):
        accountId = self.generateAccountNumber()
        self.accounts[accountId] = Account(accountId, name)
        return accountId

    def tranfer(self, from_id, to_id,amount):
        if amount <= 0: 
            print("We can't transfer non-positive amount.")
            return
        sender = self.getAccount(from_id)
        receiver = self.getAccount(to_id)
        if sender or receiver not in self.accounts:
            print("The sender or/and receiver don't exists.")
        check = sender.withdraw(amount)
        if check == -1:
            print("Aborting the tranfer operation.")
        receiver.deposit(amount)

    def makeDeposit(self, acc, figure):
        account = self.getAccount(acc)
        account.deposit(figure)

    def makeWithdraw(self, acc, figure):
        account = self.getAccount(acc)
        account.withdraw(figure)

    def printInfo(self, acc):
        account = self.getAccount(acc)
        print("Hi {}.\n You have ${}.\n Select option:\n 1) Deposit, 2) Withdraw, 3) Get your bank account 4) exit".format(account.name, account.balance))

    def printBankAccountNumber(self, acc):
        print("Your bank account number: {}".format(acc))