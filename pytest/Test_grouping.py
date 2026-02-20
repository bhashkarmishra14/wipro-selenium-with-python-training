#grouping - set of test cases run together - issue fix in that module
import pytest

#testcase 1
def testcase1():
    print("testcase1 is executed")
#testcase 2
@pytest.mark.sanity
def testcase2():
    print("testcase2 is executed")
#testcase 3
@pytest.mark.regression
def testcase3():
    print("testcase3 is executed")




















