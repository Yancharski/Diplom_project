from pages.base_page import BasePage
from selenium.webdriver.common.by import By


income_button = (By.XPATH, '/html/body/div[1]/div/main/div[2]/div[2]/div/div[12]/button')
income_fields = (By.XPATH, '/html/body/div[1]/div/main/div[2]/div[2]/div/div[5]/div/div[2]/a')
duty_field = (By.XPATH, '/html/body/div[1]/div/main/div[2]/div[2]/div/div[6]/div/div[2]/a')
balance_field = (By.CSS_SELECTOR, 'span[class="MainHexIndex_hexAmount__TAk-F"]')
language_button = (By.CSS_SELECTOR, 'button[class="Button_button__QS2NC"]')
english_language_button = (By.XPATH, '/html/body/div[1]/div/header/div[3]/span/div/div[3]')
accounts_cash_field = (By.XPATH, '/html/body/div[1]/div/main/div[2]/div[4]/table/tbody/tr[2]/td[1]/div/a/span[2]')
accounts_field = (By.XPATH, '/html/body/div[1]/div/main/div[2]/div[4]/table/tbody/tr[2]/td[2]')

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
list_of_incomes = (By.XPATH, '/html/body/div[1]/div/main/div[3]/div[2]/div[6]/div/table')
delete_income_button = (By.XPATH, '/html/body/div[1]/div/main/div[3]/div[2]/div[6]/div/table/tbody/tr[2]/td[6]/div/button[3]')
accept_delete_button = (By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/button[1]')
alert_field = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]')

add_duty_button = (By.CSS_SELECTOR, 'button[class="Button_link__5qRQJ icon _size1 color-debt _extra-space"]')
checkbox_button = (By.CSS_SELECTOR, 'label[class="inline"]')
contragent_field = (By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/button[1]')
add_contragent_field = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/div/div/button')
input_contragent_field = (By.XPATH, '/html/body/div[6]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/label/div/input')
submit_new_contragent_button = (By.XPATH, '/html/body/div[6]/div/div[2]/div/div[2]/div[2]/div/button[1]')
choose_valute_button = (By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/button[2]')
Bel_rub = (By.CSS_SELECTOR, 'button[data-curr="BYN"]')
submit_duty_button = (By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button')
list_of_duties = (By.CSS_SELECTOR, 'div[class="hex-debt scrollbar"]')
return_duty_button = (By.XPATH, '/html/body/div[1]/div/main/div[2]/div[2]/button[2]')
chosen_contragent_button = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/div/div/button[2]')
accept_return_duty_button = (By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button')
completed_duties_field = (By.XPATH, '/html/body/div[1]/div/main/div[7]')
comlete_contaragent_button = (By.CSS_SELECTOR, 'a[class="Button_link__5qRQJ hex-btn"]')
delete_contragent_button = (By.CSS_SELECTOR, 'button[class="Button_link__5qRQJ btn-icon _size2 color-danger"]')
accept_delete_contragent_button = (By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/button[1]')
close_alert_button = (By.CSS_SELECTOR, 'button[class="rc-dialog-close"]')
now_name_contragent = (By.CSS_SELECTOR, 'span[class="inline"]')
cash_in_duties = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/div/div/button[2]')
back_at_main_button = (By.CSS_SELECTOR, 'a[class="btn-icon _size2 _back"]')
error_field = (By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[1]/div[3]/div[2]')
title_of_category = (By.CSS_SELECTOR, 'div[class="title"]')


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

    @property
    def duty(self):
        return self.find_element(duty_field)

    @property
    def add_duty(self):
        return self.find_element(add_duty_button)

    @property
    def checkbox(self):
        return self.find_element(checkbox_button)

    @property
    def add_contragent(self):
        return self.find_element(add_contragent_field)

    @property
    def contragent(self):
        return self.find_element(contragent_field)

    @property
    def input_contragent(self):
        return self.find_element(input_contragent_field)

    @property
    def submit_new_contragent(self):
        return self.find_element(submit_new_contragent_button)

    @property
    def choose_valute(self):
        return self.find_element(choose_valute_button)

    @property
    def BYN(self):
        return self.find_element(Bel_rub)

    @property
    def submit_duty(self):
        return self.find_element(submit_duty_button)

    @property
    def duties_list(self):
        return self.find_element(list_of_duties)

    @property
    def return_duty(self):
        return self.find_element(return_duty_button)

    @property
    def chosen_contragent(self):
        return self.find_element(chosen_contragent_button)

    @property
    def accept_return_duty(self):
        return self.find_element(accept_return_duty_button)

    @property
    def completed_duties(self):
        return self.find_element(completed_duties_field)

    @property
    def name_of_contragent(self):
        return 'Витя'

    @property
    def comlete_contargent(self):
        return self.find_element(comlete_contaragent_button)

    @property
    def delete_contragent(self):
        return self.find_element(delete_contragent_button)

    @property
    def accept_delete_contaragent(self):
        return self.find_element(accept_delete_contragent_button)

    @property
    def close_alert(self):
        return self.find_element(close_alert_button)

    @property
    def now_name(self):
        return self.find_element(now_name_contragent)

    @property
    def duties_cash(self):
        return self.find_element(cash_in_duties)

    @property
    def balance(self):
        return self.find_element(balance_field)

    @property
    def back_to_menu(self):
        return self.find_element(back_at_main_button)

    @property
    def error(self):
        return self.find_element(error_field)

    @property
    def change_language(self):
        return self.find_element(language_button)

    @property
    def english_language(self):
        return self.find_element(english_language_button)

    @property
    def accounts_cash(self):
        return self.find_element(accounts_cash_field)

    @property
    def title_of_duty(self):
        return self.find_element(title_of_category)

    @property
    def accounts(self):
        return self.find_element(accounts_field)
