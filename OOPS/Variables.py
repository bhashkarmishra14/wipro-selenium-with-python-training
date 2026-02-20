#variables = used to store the data
#instance variables - global variables at class level
#local variable- inside the method only

#instance variables example
class Student:
    #calss variable
    school = "St Joseph Convent"
    def __init__(self,name, marks):
        self.name = name #instance variable or global variable
        self.marks = marks #instance variable or global variable
    def show(self):
        schoolcity = "Banglore" #local variable- scope is inside the method
        print(self.marks, self.name)
        print(schoolcity)
        print(self.school)
s1 = Student("Harsha", 90)
s2 = Student("Amit", 80)

s1.show()
s2.show()

class Employee:
    company = "Wipro"
e1 = Employee()
e2 = Employee()
print(e1.company)
print(e2.company)







