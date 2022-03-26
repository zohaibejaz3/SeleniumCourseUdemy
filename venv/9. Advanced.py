import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

expedia_URL = "https://www.expedia.com/"
letskodeit_URL = "https://courses.letskodeit.com/practice"

driver = webdriver.Chrome()
driver.maximize_window()

# ----------------- Executing Javascript to scroll the webpage -----------------
driver.get(letskodeit_URL)

# scroll to the bottom
driver.execute_script("window.scrollBy(0, 1000);")  # these values are pixels
time.sleep(2)

# scroll to the top
driver.execute_script("window.scrollBy(0, -1000);")
time.sleep(2)

# scroll into view using JS
mouse_hover_element = driver.find_element(By.ID, "mousehover")
driver.execute_script("arguments[0].scrollIntoView(true);", mouse_hover_element)  # scroll until element in view
time.sleep(2)
driver.execute_script("window.scrollBy(0, -100);")  # so element is not hidden by banner
time.sleep(2)

# resetting the scroll by going to the top again
time.sleep(2)
driver.execute_script("window.scrollBy(0, -1000);")

# Selenium way
time.sleep(2)
location = mouse_hover_element.location_once_scrolled_into_view # location from top-left corner
print(f"Location: {location}")

time.sleep(2)
# driver.quit()

# everything else works on the expedia website
driver.get(expedia_URL)
# ----------------- Executing Javascript to get size -----------------
# Some things can't be done with Selenium, so we may want to use JS

height = driver.execute_script("return window.innerHeight;")
width = driver.execute_script("return window.innerWidth;")

print(f"Window height = {height}\nWindow width = {width}")

# select the flight tab
driver.find_element(By.XPATH, "//a[@aria-controls='wizard-flight-pwa']").click()

# ----------------- Auto-fill example using name of cities -----------------

# LIST IS BROKEN! FOR SOME REASON AUTO-COMPLETE LIST DOESNT SHOW UP, BUT I GET THE IDEA

user_input_city = "New York"

# click the textbox
driver.find_element(By.XPATH, "//button[@aria-label='Leaving from']").click()
city_name = driver.find_element(By.XPATH, "//input[@placeholder='Where are you leaving from?']")
city_name.send_keys(user_input_city)

try:
    airport_name = driver.find_element(By.XPATH, "//button[@aria-label='LaGuardia Airport (LGA)']")
except NoSuchElementException:
    try:
        print("Failed to select airport name. Taking screenshot...")
        driver.save_screenshot("airport_name_FAILED.png")
    except IsADirectoryError:
        print("Failed to save screenshot")

time.sleep(5)

# ----------------- Select a user input date -----------------

# same month 1-31
user_input_date = "25"

# click on the departing date button
driver.find_element(By.ID, "d1-btn").click()

driver.find_element(By.XPATH,
                    f"//div[@class='uitk-date-picker-menu-months-container']/div[position()=1]//button[@data-day='{user_input_date}']").click()

time.sleep(5)

# ----------------- END -----------------

driver.close()
