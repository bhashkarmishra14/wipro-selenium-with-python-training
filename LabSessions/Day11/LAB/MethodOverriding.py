class Parent:
    def show(self):
        print("Parent Method")


class Child(Parent):
    def show(self):
        super().show()
        print("Child Method")


c = Child()
c.show()
