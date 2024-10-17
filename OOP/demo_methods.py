"""
Create a class with name BankAccount.
Every created instance should have an owner. BankAccount("Serhat Karaarslan")
Every instance should have balance 0.0.
define a deposit methoh, with that you can add money on your balance.
define a withdraw method with that you withdraw money from your account.

"""

class BankAccount:
    def __init__(self,owner,balance = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount 
        return self.balance
    
    def withdraw(self,amount):
        self.balance -= amount
        return self.balance
    

ba = BankAccount("Serhat Karaarslan")
print(f"Owner : {ba.owner}  Balance : {ba.balance}")

ba.deposit(1000.0)
print(f"After deposit =>  Balance : {ba.balance}")

ba.withdraw(200.0)
print(f"After withdraw =>  Balance : {ba.balance}")