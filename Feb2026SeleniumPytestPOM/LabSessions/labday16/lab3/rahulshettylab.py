import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_Greenkart:

    def test_greenkart(self):

        # url
        url = "https://rahulshettyacademy.com/seleniumPractise/#/"

        # vegetables to add
        items_needed = ["Beans", "Tomato", "Beetroot"]

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

        driver.maximize_window()

        try:

            # open website
            driver.get(url)
            time.sleep(3)

            # get all products
            products = driver.find_elements(By.CSS_SELECTOR, "h4.product-name")

            for i in range(len(products)):

                name = products[i].text.split("-")[0].strip()

                if name in items_needed:
                    driver.find_elements(
                        By.XPATH,
                        "//div[@class='product-action']/button"
                    )[i].click()
                    time.sleep(1)

            # open cart
            driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
            time.sleep(1)

            # proceed to checkout
            driver.find_element(
                By.XPATH,
                "//button[contains(text(),'PROCEED TO CHECKOUT')]"
            ).click()
            time.sleep(2)

            # place order
            driver.find_element(By.XPATH, "//button[contains(text(),'Place Order')]").click()
            time.sleep(2)

            # select country
            driver.find_element(By.TAG_NAME, "select").click()
            driver.find_element(By.XPATH, "//option[text()='India']").click()
            time.sleep(1)

            # agree terms
            driver.find_element(By.CLASS_NAME, "chkAgree").click()
            time.sleep(1)

            #finish order
            driver.find_element(By.XPATH, "//button[contains(text(),'Proceed')]").click()
            time.sleep(2)

            print("Order completed successfully")

        except Exception as e:
            print("Error occurred:", e)

        finally:
            driver.quit()