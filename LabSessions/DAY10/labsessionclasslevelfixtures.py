import pytest

@pytest.fixture(scope="class")
def openbrowser():
    print("\nOpening browser")
    yield
    print("\nClosing browser")


@pytest.mark.usefixtures("openbrowser")
class TestLoginFlow:

    def test_login(self):
        print("enter the username")
        print("enter the password")
        print("click on the login button")

    def test_logout(self):
        print("user is logged out")
