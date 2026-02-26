import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Test_DemoWebShop:

    def test_checkout_flow(self):

        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

        driver.maximize_window()

        # open website
        driver.get("https://demowebshop.tricentis.com/")
        time.sleep(2)

        # register
        driver.find_element(By.LINK_TEXT, "Register").click()
        time.sleep(2)
        driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "FirstName").send_keys("Test")
        driver.find_element(By.ID, "LastName").send_keys("User")

        email = "test" + str(int(time.time())) + "@gmail.com"
        driver.find_element(By.ID, "Email").send_keys(email)

        driver.find_element(By.ID, "Password").send_keys("Test@123")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("Test@123")
        driver.find_element(By.ID, "register-button").click()
        time.sleep(2)

        # continue
        driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        time.sleep(2)

        # logout
        driver.find_element(By.LINK_TEXT, "Log out").click()
        time.sleep(2)

        # login
        driver.find_element(By.LINK_TEXT, "Log in").click()
        time.sleep(2)
        driver.find_element(By.ID, "Email").send_keys(email)
        driver.find_element(By.ID, "Password").send_keys("Test@123")
        driver.find_element(By.XPATH, "//input[@value='Log in']").click()
        time.sleep(2)

        # add product
        driver.find_element(By.LINK_TEXT, "Books").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "(//input[@value='Add to cart'])[1]").click()
        time.sleep(2)

        # shopping cart
        driver.find_element(By.LINK_TEXT, "Shopping cart").click()
        time.sleep(2)

        # checkout
        driver.find_element(By.ID, "termsofservice").click()
        driver.find_element(By.ID, "checkout").click()
        time.sleep(2)

        # billing address
        Select(driver.find_element(By.ID, "BillingNewAddress_CountryId")).select_by_visible_text("India")
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Kolkata")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Salt Lake")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("700001")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("9999999999")

        # billing continue
        driver.find_element(By.XPATH, "//input[contains(@class,'new-address-next-step-button')]").click()
        time.sleep(3)

        # shipping address step (sometimes present)
        shipping_address = driver.find_elements(
            By.XPATH,
            "//input[contains(@class,'shipping-address-next-step-button')]"
        )

        if len(shipping_address) > 0:
            shipping_address[0].click()
            time.sleep(3)

        # shipping method continue
        driver.find_element(By.XPATH, "//input[contains(@class,'shipping-method-next-step-button')]").click()
        time.sleep(3)

        # payment method continue
        driver.find_element(By.XPATH, "//input[contains(@class,'payment-method-next-step-button')]").click()
        time.sleep(3)

        # payment info continue
        driver.find_element(By.XPATH, "//input[contains(@class,'payment-info-next-step-button')]").click()
        time.sleep(3)

        # confirm order
        driver.find_element(By.XPATH, "//input[contains(@class,'confirm-order-next-step-button')]").click()
        time.sleep(3)

        # finish
        driver.find_element(By.XPATH, "//input[contains(@class,'order-completed-continue-button')]").click()

        driver.close()