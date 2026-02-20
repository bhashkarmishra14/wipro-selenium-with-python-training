class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display_balance(self):
        print("Balance:", self.balance)


acc1 = BankAccount("Bhashkar", 10000000000)
acc1.deposit(900000000)
acc1.withdraw(7000987000)
acc1.display_balance()
