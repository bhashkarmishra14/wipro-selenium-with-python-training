from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open practice page
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# ---- ALERT TEST ----

# Enter name
driver.find_element(By.ID, "name").send_keys("Bhashkar")

# Click Alert button
driver.find_element(By.ID, "alertbtn").click()

# Switch to alert
alert = driver.switch_to.alert

# Print alert text
print("Alert text is:", alert.text)

# Accept alert (click OK)
alert.accept()

time.sleep(2)

# ---- CONFIRM ALERT TEST ----

# Click Confirm button
driver.find_element(By.ID, "confirmbtn").click()

confirm_alert = driver.switch_to.alert

print("Confirm text is:", confirm_alert.text)

# Dismiss alert (click Cancel)
confirm_alert.dismiss()

time.sleep(2)

driver.quit()
