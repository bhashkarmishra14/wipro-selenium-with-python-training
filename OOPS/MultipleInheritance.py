# multiple Inheritance is 2 parent and one child class
class Parent1:
    pass

class Parent2:
    pass

class child(Parent1,Parent2):
    pass
class Father :
    def deriving(self):
        print("Father has the skill to drive")


class mother:
    def cooking(self):
        print("Mother has the skill to cook")

class Child (Father,mother):
    def bothskills(self):
        print("Child have skill of study")
        print("Child has both skills of driving and cooking")

c= Child()
c.deriving()
c.cooking()
c.bothskills()