#default methods - built in methods, user define methods - method name, method body
#parameterized methods -
#it allows the same methods to behave differently for diff input
class Calculator:
    def add(self, a, b):
        print(a + b)
c = Calculator()
c.add(10,20)
c.add(5,7)

#Default parameters
class Test:
    def run(self, browser = "chrome"):
        print("Running on",browser)
t = Test()
t.run()
t.run("Firefox")

#*args parameterized methods
class Numbers:
    def total(self , *args):
        print(sum(args))
n = Numbers()
n.total(10,20,30)
n.total(10)
n.total(10,60)


















