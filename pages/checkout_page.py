from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    checkout_btn = (By.XPATH, "//button[@id='checkout']")

    def go_to_checkout(self):
        self.driver.find_element(*self.checkout_btn).click()