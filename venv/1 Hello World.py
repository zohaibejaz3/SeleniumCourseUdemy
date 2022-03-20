from selenium import webdriver
from selenium.webdriver.common.by import By

base_url = "https://courses.letskodeit.com/practice"
driver = webdriver.Chrome()
driver.get(base_url)

element = driver.find_element(By.ID,"openwindow")
if element is not None:
    print("Found element by ID")

element = driver.find_element(By.NAME,"show-hide")
if element is not None:
    print("Found element by name")

driver.quit()