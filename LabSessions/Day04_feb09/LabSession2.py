# parent class
class SavingsAccount:
    def __init__(self, balance=0):
        self.balance = balance

    # deposit function in parent class
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Balance after deposit:", self.balance)


# child class
class InterestAccount(SavingsAccount):

    # function to add interest
    def addInterest(self, rate):
        interest = self.balance * rate / 100
        self.balance += interest
        print("Interest added:", interest)
        print("Balance after interest:", self.balance)


# creating object of child class
acc = InterestAccount(1000)

# calling parent class method
acc.deposit(500)

# calling child class method
acc.addInterest(5)
