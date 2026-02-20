class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print(self.name, self.emp_id, self.salary)


emp1 = Employee("John", 101, 50000)
emp1.display()
emp2 = Employee("Akash", 105, 70000)
emp2.display()