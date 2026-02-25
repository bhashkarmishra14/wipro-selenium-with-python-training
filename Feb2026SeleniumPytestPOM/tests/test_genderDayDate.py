import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_gender_day_date:

    def test_gender_day_date(self):

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

        driver.maximize_window()
        driver.get("https://testautomationpractice.blogspot.com/")

        time.sleep(2)

        # Gender
        driver.find_element(By.XPATH, "//input[@id='male']").click()

        #DayCheckbox
        driver.find_element(By.XPATH, "//input[@id='monday']").click()

        #Date Picker
        date_box = driver.find_element(By.XPATH, "//input[@id='datepicker']")
        date_box.clear()
        date_box.send_keys("02/23/2026")   # MM/DD/YYYY format

        time.sleep(2)

        # Assertions
        assert driver.find_element(By.XPATH, "//input[@id='male']").is_selected()
        assert driver.find_element(By.XPATH, "//input[@id='monday']").is_selected()

        driver.quit()