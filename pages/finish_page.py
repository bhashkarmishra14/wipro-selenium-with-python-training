from selenium.webdriver.common.by import By


class FinishPage:

    def __init__(self, driver):
        self.driver = driver

    finish_btn = (By.XPATH, "//button[@id='finish']")

    def click_finish(self):
        self.driver.find_element(*self.finish_btn).click()