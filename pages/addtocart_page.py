from selenium.webdriver.common.by import By


class AddtocartPage:

    def __init__(self, driver):
        self.driver = driver

    add_to_cart = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    cart_icon = (By.XPATH, "//span[@class='shopping_cart_badge']")

    def add_product_to_cart(self):
        self.driver.find_element(*self.add_to_cart).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()