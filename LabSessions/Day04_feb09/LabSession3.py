# ================================
# 1. Rectangle class
# ================================
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# ================================
# 2. Person class
# ================================
from datetime import date

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob

    def calculate_age(self):
        today = date.today()
        age = today.year - self.dob.year
        if (today.month, today.day) < (self.dob.month, self.dob.day):
            age -= 1
        return age


# ================================
# 3. Shape class with subclasses
# ================================
import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class RectangleShape(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# ================================
# 4. Vehicle class and child class
# ================================
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show_details(self):
        print("Brand:", self.brand)
        print("Speed:", self.speed)


class Car(Vehicle):
    pass


# ================================
# 5. Empty Vehicle class
# ================================
class EmptyVehicle:
    pass


# ================================
# Example Usage
# ========================
