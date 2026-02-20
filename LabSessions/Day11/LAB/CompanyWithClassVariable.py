class Company:
    company_name = "Wipro"

    def __init__(self, employee_name):
        self.employee_name = employee_name

    def display(self):
        print(self.employee_name, "works at", Company.company_name)


c1 = Company("Bhashkar")
c1.display()
