class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid Balance")


acc = BankAccount(10000)
print("Balance:", acc.get_balance())
acc.set_balance(20000)
print("Updated Balance:", acc.get_balance())

