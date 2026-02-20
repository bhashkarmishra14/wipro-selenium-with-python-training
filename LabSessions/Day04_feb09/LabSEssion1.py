# create Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print("Title  :", self.title)
        print("Author :", self.author)


# creating 3 book objects
b1 = Book("Python Basics", "Guido van Rossum")
b2 = Book("Clean Code", "Robert C. Martin")
b3 = Book("AI Fundamentals", "Andrew Ng")

# displaying book details
b1.display()
b2.display()
b3.display()

# create Rectangle class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = length * width
        self.perimeter = 2 * (length + width)

    def display(self):
        print("Length     :", self.length)
        print("Width      :", self.width)
        print("Area       :", self.area)
        print("Perimeter  :", self.perimeter)


# creating object
r1 = Rectangle(20, 4)

# displaying rectangle details
r1.display()







