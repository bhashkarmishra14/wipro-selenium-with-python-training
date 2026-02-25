import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Test_DatePicker:

    def test_calendar_pickup(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        # open website
        driver.get("https://rsuitejs.com/components/date-picker/")
        time.sleep(3)

        # click date picker input
        driver.find_element(By.XPATH, "(//input[contains(@class,'rs-input')])[1]").click()
        time.sleep(4)

        # select date 15
        driver.find_element(By.XPATH, "//span[text()='15']").click()
        time.sleep(4)

        # close browser
        driver.close()