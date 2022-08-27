from selenium.webdriver.common.by import By


class LoginPage:
    _login_link = "ast-custom-button-link"
    _email_field = ".//div[@class='form-group']/input[@id='email']"
    _pass_field = ".//div[@class='form-group']/input[@id='password']"
    _submit_btn = ".//input[@value='Login']"

    def __init__(self, driver):
        self.driver = driver

    def get_login_link(self):
        return self.driver.find_element(By.CLASS_NAME, self._login_link)

    def get_email_field(self):
        return self.driver.find_element(By.XPATH, self._email_field)

    def get_pass_field(self):
        return self.driver.find_element(By.XPATH, self._pass_field)

    def get_submit_btn(self):
        return self.driver.find_element(By.XPATH, self._submit_btn)

    def click_login_link(self):
        self.get_login_link().click()

    def enter_email(self, email):
        self.get_email_field().send_keys(email)

    def enter_pass(self, password):
        self.get_pass_field().send_keys(password)

    def click_submit_btn(self):
        self.get_submit_btn().click()

    def login(self, username, password):
        self.click_login_link()
        self.enter_email(username)
        self.enter_pass(password)
        self.click_submit_btn()
