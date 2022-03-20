# find the login button, click it. Then add an email and possword, click login.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

baseUrl = "https://courses.letskodeit.com/"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseUrl)

# wait until the element has been found
driver.implicitly_wait(5)

login_link = driver.find_element(By.XPATH, "//a[@href=\"/login\"]")
login_link.click()

email_input = driver.find_element(By.ID, "email")
email_input.send_keys("wrong.person11@email.com")

password_input = driver.find_element(By.ID, "password")
password_input.send_keys("password123")

time.sleep(3)

email_input.clear()

time.sleep(3)

email_input.send_keys("correct.person22@email.com")

time.sleep(1)

login_button = driver.find_element(By.CSS_SELECTOR, "input[type=\"submit\"]")
login_button.click()

time.sleep(3)

driver.quit()
