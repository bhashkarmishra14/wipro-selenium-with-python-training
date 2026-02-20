# =========================
# LAB 1: Method Overriding
# =========================
class Employee:
    def calculate_salary(self):
        return 30000

class Manager(Employee):
    def calculate_salary(self):
        return 30000 + 10000

print("Lab 1:")
emp = Manager()
print(emp.calculate_salary())


# ==================================
# LAB 2: Polymorphism using Function
# ==================================
class Dog:
    def speak(self):
        print("Dog barks")

class Cat:
    def speak(self):
        print("Cat meows")

class Cow:
    def speak(self):
        print("Cow moos")

def animal_sound(obj):
    obj.speak()

print("\nLab 2:")
animal_sound(Dog())
animal_sound(Cat())
animal_sound(Cow())


# =====================================
# LAB 3: Multilevel Inheritance
# =====================================
class Vehicle:
    def fuel_type(self):
        print("Generic fuel")

class Car(Vehicle):
    def fuel_type(self):
        print("Petrol or Diesel")

class ElectricCar(Car):
    def fuel_type(self):
        print("Electric")

print("\nLab 3:")
Vehicle().fuel_type()
Car().fuel_type()
ElectricCar().fuel_type()


# =========================
# LAB 4: Operator Overloading
# =========================
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return self.balance + other.balance

    def __gt__(self, other):
        return self.balance > other.balance

print("\nLab 4:")
a1 = BankAccount(5000)
a2 = BankAccount(7000)
print(a1 + a2)
print(a1 > a2)


# ==================================
# LAB 6: Multiple Inheritance & MRO
# ==================================
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass

print("\nLab 6:")
d = D()
d.show()
print(D.mro())


# =====================================
# LAB 7: Polymorphism with Exceptions
# =====================================
class Calculator:
    def divide(self, a, b):
        return a / b

class SafeCalculator(Calculator):
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Cannot divide by zero"

print("\nLab 7:")
safe = SafeCalculator()
print(safe.divide(10, 2))
print(safe.divide(10, 0))


# =====================================
# LAB 8: Real-Time Payment System
# =====================================
class Payment:
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")

class NetBanking(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Net Banking")

def process_payment(payment, amount):
    payment.pay(amount)

print("\nLab 8:")
process_payment(CreditCard(), 500)
process_payment(UPI(), 300)
process_payment(NetBanking(), 1000)
