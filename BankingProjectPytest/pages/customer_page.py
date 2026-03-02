from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CustomerPage:

    DEPOSIT_TAB = (By.XPATH, "//button[@ng-click='deposit()']")
    WITHDRAW_TAB = (By.XPATH, "//button[@ng-click='withdrawl()']")
    AMOUNT_FIELD = (By.XPATH, "//input[@ng-model='amount']")
    SUBMIT_BTN = (By.XPATH, "//button[@type='submit']")
    BALANCE = (By.XPATH, "(//strong[@class='ng-binding'])[2]")

    def __init__(self, driver):
        self.driver = driver

    def deposit(self, amount):
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(self.DEPOSIT_TAB)
        ).click()

        WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located(self.AMOUNT_FIELD)
        )

        self.driver.find_element(*self.AMOUNT_FIELD).send_keys(str(amount))
        self.driver.find_element(*self.SUBMIT_BTN).click()

    def withdraw(self, amount):
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(self.WITHDRAW_TAB)
        ).click()

        WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located(self.AMOUNT_FIELD)
        )

        self.driver.find_element(*self.AMOUNT_FIELD).send_keys(str(amount))
        self.driver.find_element(*self.SUBMIT_BTN).click()

    def get_balance(self):
        return self.driver.find_element(*self.BALANCE).text