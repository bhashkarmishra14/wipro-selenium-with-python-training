import pytest
from Test_SimpleFixture import api_url
#testcase 1
def testcase1():
    print("testcase1 is executed")

def testcase2():
    print("testcase2 is executed")

def test_case3():
    print("testcase3 is executed")

def test_case4():
    print("testcase4 is executed")

def test_case5():
    print("testcase5 is executed")

def test_login():
    print("Login test is executed")
def test_api(api_url):
    assert "https" in api_url