import time
from selenium import webdriver
from selenium.webdriver.common.by import By

baseURL = "https://courses.letskodeit.com/practice"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseURL)

# scroll down to bottom
driver.execute_script("window.scrollBy(0, 1500);")

# switch to iframe using ID
driver.switch_to.frame('courses-iframe')
# using the same method, you can switch it with name, as well as, number.
# first ifrome starts at 0, the 1, 2, and so on depending the number of iframes.

# doing stuff inside the iframe
driver.find_element(By.CSS_SELECTOR, "input#search").send_keys('Python')
time.sleep(3)

# scroll to the top
driver.execute_script("window.scrollBy(0, -1500)")

# switching back the focus and entering name
driver.switch_to.default_content()
driver.find_element(By.XPATH, "//input[@placeholder='Enter Your Name']").send_keys("Test Successful")

#NOTE: ONLY NEED TO USE switch_to.alert when the popup is JS.
#      if it's CSS or HTML then use find_element

# clicking on the alert button and handling the JS popup
driver.find_element(By.ID, "alertbtn").click()
time.sleep(2)
alert_popup = driver.switch_to.alert
alert_popup.accept()

# entering the name again
driver.find_element(By.XPATH, "//input[@placeholder='Enter Your Name']").send_keys("Test Successful")

# clicking on the confirm button and handling the JS popup
driver.find_element(By.ID, 'confirmbtn').click()
time.sleep(2)
confirm_button = driver.switch_to.alert
confirm_button.dismiss()

# wait some time and close the browser
time.sleep(2)
driver.quit()
