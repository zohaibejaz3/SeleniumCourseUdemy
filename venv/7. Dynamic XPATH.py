import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

baseUrl = "https://courses.letskodeit.com/courses"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseUrl)
driver.implicitly_wait(5)

user_input = "Selenium WebDriver With Java"

to_find = "//h4[@class='dynamic-heading' and contains(text(),'{0}')]"
# to_find = f"//h4[@class='dynamic-heading' and contains(text(),'{user_input}')]"

search_box = driver.find_element(By.XPATH, "//input[@id='search']")
search_box.send_keys(user_input)
search_box.send_keys('\n')
sleep(5)

course_XPATH = to_find.format(user_input)
# course_XPATH = to_find

try:
    course_element = driver.find_element(By.XPATH, course_XPATH)
    print("Element found")
except selenium.common.exceptions.NoSuchElementException:
    print("No such element found")

course_element.click()
sleep(5)

driver.quit()
