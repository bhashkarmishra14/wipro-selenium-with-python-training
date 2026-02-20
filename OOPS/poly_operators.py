#operator polymorphism means same
#operator behaves differently for diff data types or the object.
#+add numbers
#+ joins the strings
#+merges the list
#operator overloading in python
#python
'''
__add__()
__sub__()
__mul__()
__eq__()
__lt__()
__gt__()
'''
class Number:
    def __init__(self,value):
        self.value = value
    def __add__(self,other):
        return self.value + other.value
n1 = Number(10)
n2 = Number(20)
print(n1 + n2)
#now + will work for the custom object

# Operator polymorphism and operator overloading

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value


n1 = Number(10)
n2 = Number(20)

print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 == n2)
print(n1 < n2)
print(n1 > n2)




















