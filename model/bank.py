import random
import json
from model.account import Account
class Bank:    
    def __init__(self):
        self.accounts = []
        self.readAccounts()

    def generateAccountNumber(self):
        countryCode="PL"
        checkDigitals = str(random.randint(10,99))
        accountNumbers = ''.join(str(random.randint(0,9)) for i in range(24))
        #to do check unique number
        return "{}{}{}".format(countryCode, checkDigitals, accountNumbers)
    
    def getAccount(self, account_id):
        #obsluga bledu braku konta o account_id 
        for acc in self.accounts:
            actual_id = acc.getAccountNumber()
            if account_id == actual_id:
                return acc
        print("Account doesn't exists.")
        return None
    
    def addAccount(self, acc):
        self.accounts.append(acc)

    def createAccount(self, name):
        accountId = self.generateAccountNumber()
        acc = Account(accountId, name)
        self.addAccount(acc)
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


    def readAccounts(self):
        with open("data/bankData.json", "r") as file:
            data = json.load(file)
            self.accounts = [Account(acc["id"], acc["name"], acc["balance"]) for acc in data] 

    def makeWithdraw(self, acc, figure):
        account = self.getAccount(acc)
        account.withdraw(figure)

    def printInfo(self, acc):
        account = self.getAccount(acc)
        print("Hi {}.\n You have ${}.\n Select option:\n 1) Deposit, 2) Withdraw, 3) Get your bank account 4) Make transfer 5) exit".format(account.name, account.balance))

    def printBankAccountNumber(self, acc):
        print("Your bank account number: {}".format(acc))

    def close(self):
        data = []
        for acc in self.accounts:
            data.append(acc.saveAccount())
        with open("data/bankData.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Goodbye, see you soon!")