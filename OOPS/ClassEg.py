#class is a blueprint or template
#which describes the state/behaviour of its object
#data is put in variable
#behaviour id put in function
class Student:
    #data or the properties
    studentname = "Ravi"
    studentID = 677887
#self is used to access the attributes of the class we have defined
#it is automatically loaded
#self represents the instance of the class
#create a function to access the data
    def displaystudentdetails(self):
        print(self.studentname)
        print(self.studentID)
#create the object of the class
a = Student()
a.displaystudentdetails()












