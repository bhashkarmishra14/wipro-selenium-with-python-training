class Person:
    def show(self):
        print("I am a Person")


class Employee(Person):
    def work(self):
        print("I am an Employee")


class Manager(Employee):
    def manage(self):
        print("I am a Manager")


m1 = Manager()
m1.show()
m1.work()
m1.manage()
