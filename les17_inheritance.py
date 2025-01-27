#Create a hierarchy of classes representing different types of bank accounts. Start
#with a base class called BankAccount. Then, create two subclasses,
#SavingsAccount and CheckingAccount. Each subclass should inherit from the
#BankAccount class
from math import remainder


#    The BankAccount class should have the following attributes and methods:
#       ○ Attributes: account_number, balance
#       ○ Methods: __init__ (constructor), deposit, withdraw, and get_balance

#    The SavingsAccount class should inherit from BankAccount and have an
#    additional attribute interest_rate. Override the deposit method to add
#    interest to the balance when a deposit is made

#    The CheckingAccount class should inherit from BankAccount and have an
#    additional attribute overdraft_fee. Override the withdraw method to deduct
#    the overdraft fee if a withdrawal causes the balance to go below zero

class BankAccount:
    def __init__(self,account_number,balance):
        self.number = account_number
        self.balance = balance
    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("Deposit is not positive ")
        self.balance += amount
    def withdraw(self,amount):
        if amount > self.balance:
            raise TypeError("You can not withdraw an amount that is greater than your balance")
        self.balance -= int(amount)
    def get_balance(self):
        return self.balance


class SavingAccount(BankAccount):
    def __init__(self,account_number,balance,interest_rate):
        self.interest = interest_rate
        super().__init__(account_number,balance)
    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("Deposit is not positive ")
        self.balance += amount + amount // 100 * self.interest
        print(f"{self.number} account balance was replenished by {amount} dollars")
class CheckingAccount(BankAccount):
    def __init__(self,account_number,balance,overdraft_fee):
        self.overdraft = overdraft_fee
        super().__init__(account_number,balance)
    def withdraw(self,amount):
        remainder = 0
        percent = 0
        if amount > self.balance:
            remainder = amount - self.balance
            percent = remainder * self.overdraft // 100
        self.balance -= amount #+ self.overdraft
        print(f"your balance is {self.balance}, you take overdraft {remainder} dollar and u will give back {remainder + percent} dollars")

user1 = CheckingAccount("4123 6352 9990 1234",5000,100)
user1.withdraw(100)
user2 = SavingAccount("5296 4200 9625 1555", 10000, 2)
user2.deposit(1500)
#print(user2.get_balance())






