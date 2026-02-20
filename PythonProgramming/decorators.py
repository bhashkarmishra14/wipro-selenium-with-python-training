#decorators - wrapper function around the functions are called as decorators
#decorator
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner
def vanillacake():
    print("I am the vanilla cake")
def strawberrycake():
    print("I am the strowberry cake")
vanillacake()
strawberrycake()



















