#write a program to create a class for an employee - with data - emp id , emp name , emp  dept and create function to display the data with 2 objects
# create a class for Employee
class Employee:

    # constructor to assign data
    def __init__(self, emp_id, emp_name, emp_dept):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_dept = emp_dept

    # function to display employee details
    def displayemployeedetails(self):
        print("Employee ID   :", self.emp_id)
        print("Employee Name :", self.emp_name)
        print("Department    :", self.emp_dept)


# creating two objects
e1 = Employee(123456, "Ravi", "Software Testing")
e2 = Employee(123457, "Anita", "HR")

# displaying details
e1.displayemployeedetails()
e2.displayemployeedetails()
