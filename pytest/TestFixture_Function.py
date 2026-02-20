#scope is run before and after every function
import pytest
@pytest.mark.usefixtures("openbrowser")
def test_login():
    print("enter the username")
    print("enter the password")
    print("click on the login button")
@pytest.mark.usefixtures("closebrowser")
def test_logout():
    print("user is logged out")
#try fixtures at class level
#try fixtures at module level
#try fixtures at session level












