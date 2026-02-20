#used inside the class
#it will run for every class defination

class Testclass:
    #class level set up
    def setup_class(cls):
        print("API Authorization needed with username and password")
    def teardown_class(cls):
        print("API Authorization closed")
    def setup_method(method):
        print("opening the browser")
        #teardown up at function level
    def teardown_method(method):
        print("closing the browser")
    #test case 1
    def testcase1(self):
        print("Testcase1 is executed")
    #test case 2
    def testcase2(self):
        print("Testcase2 is executed")
    #test case 3
    def testcase3(self):
        print("Testcase3 is executed")

class Testclass2:
    # test case 1
    def testcase1(self):
        print("Testcase1 is executed")

    # test case 2
    def testcase2(self):
        print("Testcase2 is executed")

    # test case 3
    def testcase3(self):
        print("Testcase3 is executed")








