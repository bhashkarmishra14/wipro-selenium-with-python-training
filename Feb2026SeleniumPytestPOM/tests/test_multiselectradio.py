import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Test_MultiSelectRadio:

    def test_multiradio(self):

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")

        # get all checkboxes (find_elements → list)
        checkbox_list = driver.find_elements(
            By.XPATH, "//input[@type='checkbox']"
        )

        count = len(checkbox_list)
        print("Total checkboxes:", count)

        # click checkboxes one by one
        for i in checkbox_list:
            time.sleep(1)
            i.click()

        # close current browser
        driver.close()