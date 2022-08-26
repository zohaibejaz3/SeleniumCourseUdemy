from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        login_link = self.driver.find_element(By.CLASS_NAME, "ast-custom-button-link")
        login_link.click()

        email_field = self.driver.find_element(By.XPATH, ".//div[@class='form-group']/input[@id='email']")
        email_field.send_keys(username)

        pass_field = self.driver.find_element(By.XPATH, ".//div[@class='form-group']/input[@id='password']")
        pass_field.send_keys(password)

        submit_btn = self.driver.find_element(By.XPATH, ".//input[@value='Login']")
        submit_btn.click()
