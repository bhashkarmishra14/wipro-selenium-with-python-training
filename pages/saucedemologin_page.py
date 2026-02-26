from selenium.webdriver.common.by import By


class LoginSaucePage:

    def __init__(self, driver):
        self.driver = driver

    username_input = (By.XPATH, "//input[@id='user-name']")
    password_input = (By.XPATH, "//input[@id='password']")
    login_button = (By.XPATH, "//input[@id='login-button']")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()