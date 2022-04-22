from pages.base_page import BasePage
from selenium.webdriver.common.by import By


income_button = (By.XPATH, '/html/body/div[1]/div/main/div[2]/div[2]/div/div[12]/button')
categories_field = (By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div[1]/button[2]')
add_category_button = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/div/div/button[1]')
input_category_field = (By.CSS_SELECTOR, 'input[placeholder="Название категории"]')
list_of_catigories = (By.CLASS_NAME, 'hex-select-list')
salary_category = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/div/div/button[2]')
date_today = (By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[3]/div/div/button')
today_button = (By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div/div/div[3]')
count_button = (By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div[1]/button[1]')
cash_category = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/div/div/button[2]')
input_currency_field = (By.CSS_SELECTOR, 'input[class="currency"]')
submit_income_button = (By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div[6]/button[2]')
income_fields = (By.XPATH, '/html/body/div[1]/div/main/div[2]/div[2]/div/div[5]/div/div[2]/a')
list_of_incomes = (By.XPATH, '/html/body/div[1]/div/main/div[3]/div[2]/div[6]/div/table')
delete_income_button = (By.XPATH, '/html/body/div[1]/div/main/div[3]/div[2]/div[6]/div/table/tbody/tr[2]/td[6]/div/button[3]')
accept_delete_button = (By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/button[1]')
alert_field = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]')
#alert_field = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div[1]')


class CommonPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.email_field = self.find_element(email_field)


    @property
    def income(self):
        return self.find_element(income_button)

    @property
    def add_category(self):
        return self.find_element(add_category_button)

    @property
    def input_category(self):
        return self.find_element(input_category_field)

    @property
    def categories(self):
        return self.find_element(categories_field)

    @property
    def categories_list(self):
        return self.find_element(list_of_catigories)

    @property
    def salary(self):
        return self.find_element(salary_category)

    @property
    def today(self):
        return self.find_element(today_button)

    @property
    def date_picker(self):
        return self.find_element(date_today)

    @property
    def count(self):
        return self.find_element(count_button)

    @property
    def cash(self):
        return self.find_element(cash_category)

    @property
    def input_currency(self):
        return self.find_element(input_currency_field)

    @property
    def submit_income(self):
        return self.find_element(submit_income_button)

    @property
    def income_field(self):
        return self.find_element(income_fields)

    @property
    def income_list(self):
        return self.find_element(list_of_incomes)

    @property
    def delete_income(self):
        return self.find_element(delete_income_button)

    @property
    def accept_delete(self):
        return self.find_element(accept_delete_button)

    @property
    def alert(self):
        return self.find_element(alert_field)
