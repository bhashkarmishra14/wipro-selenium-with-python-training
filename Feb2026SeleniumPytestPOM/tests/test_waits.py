import time
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Test_Keyboard:

    def test_keyboard(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.maximize_window()

        # global wait
        driver.implicitly_wait(2)

        # explicit wait
        radio_btn = driver.find_element(By.XPATH, "(//input[@value='radio2'])[1]")
        wait = WebDriverWait(driver, timeout=2)
        wait.until(lambda _: radio_btn.is_displayed())

        # fluent wait
        errors = [NoSuchElementException, ElementNotInteractableException]
        wait = WebDriverWait(driver, timeout=2, poll_frequency=.2, ignored_exceptions=errors)
        wait.until(lambda _: radio_btn.is_displayed())

        radio_btn.click()

        driver.close()