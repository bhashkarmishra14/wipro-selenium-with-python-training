#destructors- when we want to destroy the object
#post conditions - closing of the browser , db connection closing, reusing of certain resources
#cleanup operations
#for proper memory usage destructors should be used
#when db connection has to be closed -
#free the memory (garbage collection) which is automatically collected

class Desct:
    def __init__(self):
        print("Object created")
    def __del__(self):
        print("Closing the db connection")
a = Desct()
print("End of the program")
del a
#desct in file handling

class FileHandler:
    def __init__(self, filename):
        self.file = open(filename , 'w')
        print("File is opened")
    def readfile(self, filename):
        print("Reading the file")
    def __del__(self):
        self.file.close()
        print("File closed")
f = FileHandler("text.txt")
f.readfile("text.txt")
del f
















