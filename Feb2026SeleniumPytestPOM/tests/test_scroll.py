import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Test_Scroll:

    def test_scroll(self):

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

        driver.get("https://www.amazon.in/")
        time.sleep(4)
        amz = driver.find_element(By.XPATH, "//a[normalize-space()='Amazon Pay on Merchants']")
        driver.execute_script("arguments[0].scrollIntoView();", amz)
        time.sleep(2)
        amz.click()
        #vertical up scroll -  x coordinate should be zero
        driver.execute_script("window.scrollBy(0, -1000)")
        #vertical down scroll
        driver.execute_script("window.scrollBy(0, 5000)")
        # assert "Amazon India (@amazondotin) • Instagram photos and videos" in driver.title
        driver.close()