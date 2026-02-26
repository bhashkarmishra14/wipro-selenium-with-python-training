from selenium.webdriver.common.by import By


from selenium.webdriver.common.by import By


class FillInfoPage:

    def __init__(self, driver):
        self.driver = driver

    first_name = (By.XPATH, "//input[@id='first-name']")
    last_name = (By.XPATH, "//input[@id='last-name']")
    postal_code = (By.XPATH, "//input[@id='postal-code']")
    continue_btn = (By.XPATH, "//input[@id='continue']")

    def fill_info(self, first, last, postal):
        self.driver.find_element(*self.first_name).send_keys(first)
        self.driver.find_element(*self.last_name).send_keys(last)
        self.driver.find_element(*self.postal_code).send_keys(postal)

    def click_continue(self):
        self.driver.find_element(*self.continue_btn).click()