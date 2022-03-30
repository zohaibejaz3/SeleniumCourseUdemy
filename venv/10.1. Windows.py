from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Selenium assigns each window a handle which is a string.
# That is how Selenium can differenciate between windows

baseURL = "https://courses.letskodeit.com/practice"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseURL)

# find and click the open window button
driver.find_element(By.ID, "openwindow").click()

# assign and print the parent handle
parent_handle = driver.current_window_handle
print(f"Parent Handle: {parent_handle}")

# assign and print all handles
all_handles = driver.window_handles
for handle in all_handles:
    print(f"Handle: {handle}")

# iterate over handles to find and switch to the new handle
for handle in all_handles:
    if handle != parent_handle:
        driver.switch_to.window(handle)
        print(f"Switched to: {handle}")
        driver.find_element(By.CSS_SELECTOR, "input#search").send_keys("Python")
        time.sleep(3)
        driver.close() # close the window that has focus

# switch back to the original window
driver.switch_to.window(parent_handle)
print(f"Switched to: {driver.current_window_handle}")

# close all the windows
driver.quit()
