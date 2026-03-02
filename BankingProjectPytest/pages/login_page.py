from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"

    BANK_MANAGER_LOGIN = (By.XPATH, "//button[@ng-click='manager()']")
    CUSTOMER_LOGIN = (By.XPATH, "//button[@ng-click='customer()']")
    CUSTOMER_DROPDOWN = (By.ID, "userSelect")
    LOGIN_BTN = (By.XPATH, "//button[text()='Login']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def login_as_manager(self):
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(self.BANK_MANAGER_LOGIN)
        ).click()

    def login_as_customer(self):
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(self.CUSTOMER_LOGIN)
        ).click()

        WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located(self.CUSTOMER_DROPDOWN)
        )

        self.driver.find_element(*self.CUSTOMER_DROPDOWN).click()
        self.driver.find_elements(By.TAG_NAME,"option")[1].click()
        self.driver.find_element(*self.LOGIN_BTN).click()