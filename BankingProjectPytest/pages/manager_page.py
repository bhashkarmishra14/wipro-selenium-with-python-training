from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class ManagerPage:

    ADD_CUSTOMER_TAB = (By.XPATH, "//button[@ng-click='addCust()']")
    OPEN_ACCOUNT_TAB = (By.XPATH, "//button[@ng-click='openAccount()']")

    FIRSTNAME = (By.XPATH, "//input[@ng-model='fName']")
    LASTNAME = (By.XPATH, "//input[@ng-model='lName']")
    POSTCODE = (By.XPATH, "//input[@ng-model='postCd']")
    ADD_BTN = (By.XPATH, "//button[@type='submit']")

    CUSTOMER_DROPDOWN = (By.ID, "userSelect")
    ACCOUNT_DROPDOWN = (By.ID, "currency")
    PROCESS_BTN = (By.XPATH, "//button[contains(text(),'Process')]")

    def __init__(self, driver):
        self.driver = driver

    def add_customer(self):
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(self.ADD_CUSTOMER_TAB)
        ).click()

        WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located(self.FIRSTNAME)
        )

        self.driver.find_element(*self.FIRSTNAME).send_keys("John")
        self.driver.find_element(*self.LASTNAME).send_keys("Wick")
        self.driver.find_element(*self.POSTCODE).send_keys("700001")
        self.driver.find_element(*self.ADD_BTN).click()

        self.driver.switch_to.alert.accept()

    def open_account(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.OPEN_ACCOUNT_TAB)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CUSTOMER_DROPDOWN)
        )

        # select customer
        Select(self.driver.find_element(*self.CUSTOMER_DROPDOWN)) \
            .select_by_index(1)

        # select currency
        Select(self.driver.find_element(*self.ACCOUNT_DROPDOWN)) \
            .select_by_visible_text("Dollar")

        self.driver.find_element(*self.PROCESS_BTN).click()

        # wait for alert safely
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()