from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep

baseUrl = "https://courses.letskodeit.com/practice"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseUrl)
driver.implicitly_wait(5)

# ------------------- Getting text from element -------------------

open_tab_button = driver.find_element(By.ID, "opentab")
print("Element contains text: " + open_tab_button.text)

# ------------------- Getting value of an attribute from element -------------------

open_tab_button = driver.find_element(By.ID, "opentab")
open_tab_button.get_attribute("class")
print("Element's class text value is: " + open_tab_button.get_attribute("class"))

driver.quit()
