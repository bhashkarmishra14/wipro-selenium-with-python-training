import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


class Test_DropDown:

    def test_dropdown(self):

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

        driver.maximize_window()
        driver.get("https://trytestingthis.netlify.app/")

        time.sleep(4)

        # single select dropdown
        dropdown = driver.find_element(By.ID, "option")
        sel = Select(dropdown)

        # select one option
        sel.select_by_visible_text("Option 1")

        time.sleep(2)
        driver.quit()