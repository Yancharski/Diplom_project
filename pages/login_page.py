from pages.base_page import BasePage
from selenium.webdriver.common.by import By


email_input = (By.ID, 'loginform-username')
password_input = (By.ID, 'loginform-password')
submit_button = (By.CSS_SELECTOR, 'button[type="submit"]')


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.email_field = self.find_element(email_field)

    def open(self):
        self.driver.get('https://new.cubux.net/login')
        self.email_field.send_keys('vladyancharski@gmail.com')
        self.pass_field.send_keys('FcJunior27')
        self.submit.click()

    @property
    def email_field(self):
        return self.find_element(email_input)

    @property
    def pass_field(self):
        return self.find_element(password_input)

    @property
    def submit(self):
        return self.find_element(submit_button)
