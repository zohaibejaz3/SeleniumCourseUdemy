# continuing after a long time... need to practice everything everything that came before.

# Starts off by simply finding the login link button and clicking on it.
# Then, typing in the email
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

base_URL = "https://letskodeit.teachable.com/"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(base_URL)
# driver.implicitly_wait(5) # adds wait to all of the code

# Challenge for revision: find multiple ways to get that login link
# fastest is ID:
#   ID not found

# 2nd fastest is CSS
login_element = driver.find_element(By.CSS_SELECTOR, 'a[class="navbar-link fedora-navbar-link"]')

# 3rd fastest is Xpath
login_element = driver.find_element(By.XPATH, "//a[@href=\"/sign_in\"]")

# Then the rest:
#   Name not found
#   Link text
login_element = driver.find_element(By.LINK_TEXT, "Login")
#   Partial link text
login_element = driver.find_element(By.PARTIAL_LINK_TEXT, "Logi")
#   Class name  # cant put two class names!!
# login_element = driver.find_element(By.CLASS_NAME, "fedora-navbar-link")  # gets the wrong thing on navbar
#   Tag mame
# login_element = driver.find_element(By.TAG_NAME, "a") # gets a random link

login_element.click()

wait = WebDriverWait(driver, 10, 1, [ElementNotVisibleException, NoSuchElementException, ElementNotSelectableException])

email_text_box = wait.until(EC.presence_of_element_located((By.ID, "email")))

email_text_box.send_keys("hi hi")

time.sleep(5)

driver.quit()
