#constructors - first function of the class when an object of the class is created
#syntax __init__()
#we can parametrize the constructors
#self is mandatory
#constructor overloading is not supported directly
class student:
    def __init__(self):
        print("Constructor is called")
    def addsum(self):
        print("Adding 2 numbers")
s1 = student()
s1.addsum()
#parametrized constructors
#self.name is a instance variable or a global variable (belongs to object)
#name is a local parameter(exists inside the method)
#if we dont assign it to the self.name the object will not remember the value
class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):
        print(self.name, self.salary)
e1 = employee("Harsha" , 50000)
e2 = employee("Ravi" , 790000)
e1.display()
e2.display()

#using * args in constructor
#constructors overloading is supported by *args keyword
#we can pass any numbers of parameters to the constructors using *args
class Numbers:
    def __init__(self , *args):
        self.values = args
n = Numbers(10,20,30)
print(n.values)
m = Numbers(3,4)
print(m.values)
p = Numbers(3)
print(p.values)

#Parent and child constructors
#super keyword for accessing parent constructor data

class Parent:
    def __init__(self):
        print("I am the parent constructor")

class Child1(Parent):
    def __init__(self):
        super().__init__()
        print("I am the child1 constructor")
c = Child1()

class Child2(Child1):
    def __init__(self):
        super().__init__()
        print("I am the child2 constructor")
c = Child2()














