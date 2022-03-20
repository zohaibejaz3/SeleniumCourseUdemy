# ONLY USED FOR DROP-DOWNS USING 'SELECT' TAG!
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep

baseUrl = "https://courses.letskodeit.com/practice"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseUrl)
driver.implicitly_wait(5)

dropdown_element = driver.find_element(By.ID, "carselect")
sel = Select(dropdown_element)

sleep(2)
sel.select_by_index(1)
sleep(2)
sel.select_by_value("honda")
sleep(2)
sel.select_by_visible_text("BMW")
sleep(2)

driver.quit()
