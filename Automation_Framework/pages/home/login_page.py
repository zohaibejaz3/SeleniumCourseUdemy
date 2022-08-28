from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):
    _login_link = "ast-custom-button-link"
    _email_field = ".//div[@class='form-group']/input[@id='email']"
    _pass_field = ".//div[@class='form-group']/input[@id='password']"
    _submit_btn = ".//input[@value='Login']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # def get_login_link(self):
    #     return self.driver.find_element(By.CLASS_NAME, self._login_link)
    #
    # def get_email_field(self):
    #     return self.driver.find_element(By.XPATH, self._email_field)
    #
    # def get_pass_field(self):
    #     return self.driver.find_element(By.XPATH, self._pass_field)
    #
    # def get_submit_btn(self):
    #     return self.driver.find_element(By.XPATH, self._submit_btn)

    def click_login_link(self):
        self.elementClick(self._login_link, locatorType="class")

    def enter_email(self, email):
        self.sendKeys(email, self._email_field, locatorType="xpath")

    def enter_pass(self, password):
        self.sendKeys(password, self._pass_field, locatorType="xpath")

    def click_submit_btn(self):
        self.elementClick(self._submit_btn, locatorType="xpath")

    def login(self, username, password):
        self.click_login_link()
        self.enter_email(username)
        self.enter_pass(password)
        self.click_submit_btn()
