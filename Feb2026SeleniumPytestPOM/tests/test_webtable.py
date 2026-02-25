from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


class Test_Webtable:

    def test_webtable(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://the-internet.herokuapp.com/tables")

        # no of rows
        rows = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr")
        for i in rows:
            print(i.text)

        time.sleep(2)

        # no of columns
        cols = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr[1]/td")
        for i in cols:
            print(i.text)

        time.sleep(2)

        # fetch cell data
        celldata = driver.find_element(By.XPATH, "//table[@id='table1']/tbody/tr[3]/td[4]")
        print("Cell Value:", celldata.text)

        # correct assertion
        assert "$100.00" in celldata.text

        driver.quit()