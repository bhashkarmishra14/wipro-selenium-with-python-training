import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_SauceDemo:

    def test_saucedemo(self):

        # url and login credentials
        url = "https://www.saucedemo.com/"
        username = "standard_user"
        password = "secret_sauce"

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

        driver.maximize_window()

        try:

            # open website and login
            driver.get(url)
            time.sleep(5)
            driver.find_element(By.ID, "user-name").send_keys(username)
            driver.find_element(By.ID, "password").send_keys(password)
            driver.find_element(By.ID, "login-button").click()
            time.sleep(5)

            # add product to cart
            driver.find_element(By.XPATH, "(//button[contains(text(),'Add to cart')])[1]").click()
            time.sleep(5)

            # go to cart page
            driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
            time.sleep(4)

            # start checkout
            driver.find_element(By.ID, "checkout").click()
            time.sleep(4)

            # enter checkout details
            driver.find_element(By.ID, "first-name").send_keys("Bhashkar")
            driver.find_element(By.ID, "last-name").send_keys("Mishra")
            driver.find_element(By.ID, "postal-code").send_keys("226001")
            driver.find_element(By.ID, "continue").click()
            time.sleep(5)

            # finish checkout
            driver.find_element(By.ID, "finish").click()
            time.sleep(5)

            # verify order completed
            assert "checkout-complete" in driver.current_url
            print("Checkout completed successfully")

        except Exception as e:
            print("Error occurred:", e)

        finally:
            driver.quit()