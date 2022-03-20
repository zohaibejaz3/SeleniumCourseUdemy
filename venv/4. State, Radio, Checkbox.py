import time

from selenium import webdriver
from selenium.webdriver.common.by import By

baseUrl = "https://courses.letskodeit.com/practice"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseUrl)
driver.implicitly_wait(5)

# ------------------- Enable/Disable -------------------

disable_button = driver.find_element(By.ID, "disabled-button")
# disable_button.click()
enable_button = driver.find_element(By.ID, "enabled-button")
textbox = driver.find_element(By.ID, "enabled-example-input")

if textbox.is_enabled():
    print("textbox is enabled")
    textbox.send_keys("Heyyyy")
    time.sleep(3)
else:
    print("textbox is disabled")
    enable_button.click()
    textbox.send_keys("Heyyyy")
    time.sleep(3)

# ------------------- Radio Buttons -------------------
list_radio_buttons = driver.find_elements(By.XPATH, "//input[@name='cars' and @type='radio']")

for radio_button in list_radio_buttons:
    if not radio_button.is_selected():
        radio_button.click()
        time.sleep(2)

# ------------------- Checkboxes -------------------
list_checkboxes = driver.find_elements(By.XPATH, "//input[@name='cars' and @type='checkbox']")

for checkbox in list_checkboxes:
    if not checkbox.is_selected():
        checkbox.click()
        time.sleep(2)

driver.quit()
