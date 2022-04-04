import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

letskodeitURL = "https://courses.letskodeit.com/practice"
jquerydropURL = "https://jqueryui.com/droppable/"
jquerysliderURL = "https://jqueryui.com/slider/"

driver = webdriver.Chrome()
driver.maximize_window()

# --------------- mouse hover on letskodeit ---------------
driver.get(letskodeitURL)

# find and scroll to the mouse hover button
hover_button = driver.find_element(By.ID, "mousehover")
hover_button.location_once_scrolled_into_view

# using action chains to hover on element
action = ActionChains(driver)
action.move_to_element(hover_button).perform()

# find and click on 'Top' from the drop-down menu
top_link = driver.find_element(By.XPATH, "//a[text()='Top']")
action.click(top_link).perform()  # using ActionChains b/c why not

# --------------- drag-and-drop jquery ---------------
driver.get(jquerydropURL)

# switch to the iframe and get the elements
driver.switch_to.frame(0)  # using index b/c no id available
element_source = driver.find_element(By.ID, "draggable")
element_destination = driver.find_element(By.ID, "droppable")

# perform action chains to drag and drop
# action.drag_and_drop(element_source, element_destination).perform()

# anoter way of dragging and dropping.
# clearly see why it's called action chains (one action after the other)
action.click_and_hold(element_source).move_to_element(element_destination).release().perform()

# --------------- slider jquery ---------------
driver.get(jquerysliderURL)

# switch to the iframe and get the elements
driver.switch_to.frame(0)  # using index b/c no id available
slider = driver.find_element(By.XPATH, "//div[@id='slider']/span")

# perform drag and drop by offset action to move the slider a certain amount
action.drag_and_drop_by_offset(slider, 200, 0).perform()

time.sleep(3)
driver.quit()
