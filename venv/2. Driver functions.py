from selenium import webdriver
from selenium.webdriver.common.by import By

base_url = "https://courses.letskodeit.com/practice"
driver = webdriver.Chrome()

driver.maximize_window()

driver.get(base_url)

title = driver.title
print("Title of the webpage is: " + title)

current_url = driver.current_url
print("URL of the webpage is: " + current_url)

print("Refreshing page...")
driver.refresh()

print("Refreshing page again...")
driver.get(driver.current_url)

driver.get("https://courses.letskodeit.com/login")
current_url = driver.current_url
print("URL of the webpage is: " + current_url)

print("Going back...")
driver.back()

print("Going forward...")
driver.forward()

pagesource = driver.page_source

driver.quit()
