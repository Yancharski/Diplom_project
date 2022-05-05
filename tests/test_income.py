import pytest
from pages.login_page import LoginPage
from pages.common_page import CommonPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from time import sleep
from datetime import date
import allure


@allure.feature('Income')
@allure.story('Income category add')
@pytest.mark.skip
def test_add_category(driver):
    name = 'Some_category'
    login_page = LoginPage(driver)
    login_page.open()
    common_page = CommonPage(driver)
    common_page.income.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.categories
        )
    )
    common_page.categories.click()
    common_page.add_category.click()
    common_page.input_category.send_keys(name + Keys.ENTER)
    common_page.categories.click()
    assert name in common_page.categories_list.text

@allure.feature('Income')
@allure.story('Income add')
def test_add_income(driver):
    login_page = LoginPage(driver)
    login_page.open()
    common_page = CommonPage(driver)
    common_page.income.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.categories
        )
    )
    common_page.categories.click()
    common_page.salary.click()
    common_page.date_picker.click()
    common_page.today.click()
    common_page.count.click()
    common_page.cash.click()
    common_page.input_currency.send_keys('155')
    common_page.submit_income.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.income_field
        )
    )
    sleep(0.5)
    common_page.income_field.click()
    strings_list = ['+ 155', 'Зарплата', 'Наличные деньги', str(date.today().year), str(date.today().month), str(date.today().day)]
    strings_in_text = [x in common_page.income_list.text for x in strings_list]
    assert all(strings_in_text)


@allure.feature('Income')
@allure.story('Income in balance')
def test_compare_income_in_balance(driver):
    login_page = LoginPage(driver)
    login_page.open()
    common_page = CommonPage(driver)
    common_page.income_field.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.back_to_menu
        )
    )
    common_page.back_to_menu.click()
    assert '155' in common_page.balance.text


@allure.feature('Income')
@allure.story('Income delete')
def test_delete_income(driver):
    login_page = LoginPage(driver)
    login_page.open()
    common_page = CommonPage(driver)
    common_page.income_field.click()
    common_page.delete_income.click()
    common_page.accept_delete.click()
    sleep(0.5)
    strings_list = ['+ 155', 'Зарплата', 'Наличные деньги', str(date.today().year), str(date.today().month), str(date.today().day)]
    strings_in_text = [x in common_page.income_list.text for x in strings_list]
    assert not all(strings_in_text)


@allure.feature('Income')
@allure.story('Income without all values')
def test_add_income_without_values(driver):
    login_page = LoginPage(driver)
    login_page.open()
    common_page = CommonPage(driver)
    common_page.income.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.submit_income
        )
    )
    common_page.submit_income.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.alert
        )
    )
    assert 'Выберите счёт' in common_page.alert.text


@allure.feature('Income')
@allure.story('Income only with count')
def test_add_income_with_count(driver):
    login_page = LoginPage(driver)
    login_page.open()
    common_page = CommonPage(driver)
    common_page.income.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.categories
        )
    )
    common_page.count.click()
    common_page.cash.click()
    common_page.submit_income.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.alert
        )
    )
    assert 'Выберите категорию' in common_page.alert.text


@allure.feature('Income')
@allure.story('Income only with count and type of income')
def test_add_income_without_currency(driver):
    login_page = LoginPage(driver)
    login_page.open()
    common_page = CommonPage(driver)
    common_page.income.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.categories
        )
    )
    common_page.count.click()
    common_page.cash.click()
    common_page.categories.click()
    common_page.salary.click()
    common_page.submit_income.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.alert
        )
    )
    assert 'Укажите сумму' in common_page.alert.text


@allure.feature('Income')
@allure.story('Income with incorrect values')
def test_add_income_witn_incorrect_values(driver):
    login_page = LoginPage(driver)
    login_page.open()
    common_page = CommonPage(driver)
    common_page.income.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.categories
        )
    )
    common_page.count.click()
    common_page.cash.click()
    common_page.categories.click()
    common_page.salary.click()
    common_page.input_currency.send_keys('Hello world')
    common_page.submit_income.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.alert
        )
    )
    assert 'Укажите сумму' in common_page.alert.text
