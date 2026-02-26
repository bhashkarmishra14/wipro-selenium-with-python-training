import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_AutomationPractice:
    def test_practice(self):

        # open chrome browser
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        # open application url
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        time.sleep(2)

        # suggestion class example
        # enter country name
        suggest = driver.find_element(By.ID, "autocomplete")
        suggest.send_keys("Ind")
        time.sleep(2)

        # select india from dropdown
        countries = driver.find_elements(By.CSS_SELECTOR, ".ui-menu-item div")
        for country in countries:
            if country.text == "India":
                country.click()
                break

        time.sleep(2)

        # switch window example
        # store parent window
        parent = driver.current_window_handle

        # click open window button
        driver.find_element(By.ID, "openwindow").click()
        time.sleep(2)

        # switch to child window
        windows = driver.window_handles
        driver.switch_to.window(windows[1])

        # print child window title
        print(driver.title)

        # close child window and switch back
        driver.close()
        driver.switch_to.window(parent)

        time.sleep(2)

        # switch tab example
        # open new tab
        driver.find_element(By.ID, "opentab").click()
        time.sleep(2)

        # switch to tab
        tabs = driver.window_handles
        driver.switch_to.window(tabs[1])

        # print tab title
        print(driver.title)

        # close tab and switch back
        driver.close()
        driver.switch_to.window(parent)

        time.sleep(2)

        # switch alert example
        # enter name in textbox
        name = driver.find_element(By.ID, "name")
        name.send_keys("Bhash")

        # click alert button
        driver.find_element(By.ID, "alertbtn").click()
        time.sleep(2)

        # switch to alert and print text
        alert = driver.switch_to.alert
        print(alert.text)

        # accept alert
        alert.accept()

        time.sleep(2)

        # web table example
        # get all rows and print second last row
        rows = driver.find_elements(By.XPATH, "//table[@name='courses']//tr")
        print(rows[-2].text)

        time.sleep(2)

        # web table fixed header example
        # find chennai value using xpath and print
        chennai = driver.find_element(
            By.XPATH, "//div[@class='tableFixHead']//td[text()='Chennai']"
        )
        print(chennai.text)

        time.sleep(2)

        # close browser
        driver.close()