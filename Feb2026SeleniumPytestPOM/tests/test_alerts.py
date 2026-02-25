import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Test_Alerts:

    def test_alerts(self):

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        time.sleep(4)
        #simple alert with ok button only
        #switch the control to alert
        simplealt = driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']")
        simplealt.click()
        alt = driver.switch_to.alert
        alt.accept() #click on the accept button

        confalt = driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Confirm']")
        confalt.click()
        alt = driver.switch_to.alert
        alt.dismiss()  # click on the cancel button

        promptalt = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']")
        promptalt.click()
        alt = driver.switch_to.alert
        alerttext = alt.text
        print(alerttext)
        alt.send_keys("test hello")
        alt.accept()
        time.sleep(2)
        driver.close()# click on the accept button
















