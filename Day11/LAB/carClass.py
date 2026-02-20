class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}")


car1 = Car("Mercedes", "G-Wagon", 29000000)
car1.display()
