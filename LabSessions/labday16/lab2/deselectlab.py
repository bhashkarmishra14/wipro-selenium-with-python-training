import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


class Test_MultiSelect:

    def test_multiselect_deselect(self):

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

        driver.maximize_window()
        driver.get("https://trytestingthis.netlify.app/")

        time.sleep(4)

        # multiple select dropdown
        dropdown = driver.find_element(By.ID, "owc")
        sel = Select(dropdown)

        # select options
        sel.select_by_visible_text("Option 1")
        time.sleep(1)
        sel.select_by_visible_text("Option 2")
        time.sleep(1)
        sel.select_by_visible_text("Option 3")
        time.sleep(2)

        # deselect options
        # sel.deselect_by_visible_text("Option 2")
        # time.sleep(1)

        # deselect all
        sel.deselect_all()
        time.sleep(2)

        driver.quit()