#function level set up and tear down
#these run before and after each test function
#set up at function level
import pytest


def setup_function(function):
    print("Opening the browser")
#teardown up at function level
def teardown_function(function):
    print("closing the browser")
#test case 1
@pytest.mark.sanity
def testcase1():
    print("Testcase1 is executed")
#test case 2
@pytest.mark.regression
def testcase2():
    print("Testcase2 is executed")
#test case 3
@pytest.mark.db
def testcase3():
    print("Testcase3 is executed")












