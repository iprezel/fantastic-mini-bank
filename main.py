import random
import os 
from model.bank import Bank

print("Hi this is your KKK bank!")
name = str(input("Enter your name: "))
bankApp = Bank()
acc_id = bankApp.createAccount(name)
running = True
while(running):
    bankApp.printInfo(acc_id)
    getInput = input("Enter option: ")
    if getInput.isnumeric() ==  False:
        continue
    getInput = int(getInput)
    if getInput == 1:
        figure = int(input("Enter the amount to deposit: ")) 
        bankApp.makeDeposit(acc_id, figure)
    elif getInput == 2:
        figure = int(input("Enter the amount to cashed out: "))
        bankApp.makeWithdraw(acc_id, figure)
    elif getInput == 3:
        bankApp.printBankAccountNumber(acc_id)
    elif getInput == 4:
        bankApp.close()
        running = False