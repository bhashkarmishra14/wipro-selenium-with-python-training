from pages.login_page import LoginPage
from pages.manager_page import ManagerPage
from pages.customer_page import CustomerPage


def test_login(driver):
    login = LoginPage(driver)
    login.open()
    login.login_as_manager()


def test_add_customer(driver):
    login = LoginPage(driver)
    manager = ManagerPage(driver)

    login.open()
    login.login_as_manager()
    manager.add_customer()


def test_open_account(driver):
    login = LoginPage(driver)
    manager = ManagerPage(driver)

    login.open()
    login.login_as_manager()
    manager.open_account()

def test_deposit_withdraw_validate_balance(driver):
    login = LoginPage(driver)
    customer = CustomerPage(driver)

    login.open()
    login.login_as_customer()

    customer.deposit(5000)
    customer.withdraw(2000)

    balance = customer.get_balance()
    assert balance != ""