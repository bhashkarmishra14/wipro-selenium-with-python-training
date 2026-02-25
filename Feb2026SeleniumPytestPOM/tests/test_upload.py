import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Test_upload:

    def test_upload(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        driver.get("https://the-internet.herokuapp.com/upload")
        driver.maximize_window()
        time.sleep(2)

        browse = driver.find_element(By.XPATH, "//input[@id='file-upload']")
        browse.send_keys("C:\\Users\\bhash\\OneDrive\\Documents\\Document2.docx")
        time.sleep(2)

        upload = driver.find_element(By.XPATH, "//input[ @ id = 'file-submit']")

        upload.click()
        time.sleep(2)
        fileupload = driver.find_element(By.XPATH, "//h3[normalize-space()='File Uploaded!']")
        assert fileupload.text == "File Uploaded!"

        time.sleep(2)
        driver.close()