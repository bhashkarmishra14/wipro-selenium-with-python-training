class Vehicle:
    def start(self):
        print("Vehicle Started")
class Bike(Vehicle):
    def ride(self):
        print("Bike is Riding")
b1 = Bike()
b1.start()
b1.ride()
