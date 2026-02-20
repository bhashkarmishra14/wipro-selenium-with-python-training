class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "Fail"


s1 = Student("Rahul", 85)
print("Grade:", s1.get_grade())
s2 = Student("Rohan", 30)
print("Grade:", s2.get_grade())
s3 = Student("Rohit", 50)
print("Grade:", s3.get_grade())