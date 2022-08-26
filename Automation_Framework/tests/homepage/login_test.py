import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest


class loginTests(unittest.TestCase):

    def test_valid_login(self):
        baseURL = "https://letskodeit.com/"
        driver = webdriver.Chrome(
            "D:\Study\[FreeCourseLab.com] Udemy - Selenium WebDriver With Python 3.x - Novice To Ninja\Practice\Selenium_Course\Automation_Framework\webdriver\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        lp = LoginPage(driver)
        lp.login("test@email.com", "abcabc")

        try:
            user_icon = driver.find_element(By.XPATH, ".//button[@id='dropdownMenu1']")
            print("Element found!")
        except:
            print("Element not found!")
