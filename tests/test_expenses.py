from pages.login_page import LoginPage
from pages.common_page import CommonPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
import allure


@allure.feature('Expenses')
@allure.story('Expense add')
def test_add_expenses(driver):
    login_page = LoginPage(driver)
    login_page.open()
    common_page = CommonPage(driver)
    common_page.expenses.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.select_account
        )
    )
    common_page.select_account.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.cash
        )
    )
    common_page.cash.click()
    common_page.select_category.click()
    common_page.auto_category.click()
    common_page.date_picker.click()
    common_page.today.click()
    common_page.input_currency.send_keys('95')
    common_page.submit_income.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.expenses_field
        )
    )
    common_page.expenses_field.click()
    strings_list = ['95', 'Авто', 'Наличные деньги', str(date.today().year), str(date.today().month),
                    str(date.today().day)]
    strings_in_text = [x in common_page.income_list.text for x in strings_list]
    assert all(strings_in_text)


@allure.feature('Expenses')
@allure.story('Expenses check on main page')
def test_check_expense(driver):
    login_page = LoginPage(driver)
    login_page.open()
    common_page = CommonPage(driver)
    common_page.expenses_field.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.back_to_menu
        )
    )
    common_page.back_to_menu.click()
    assert '95' in common_page.expenses_field.text


@allure.feature('Expenses')
@allure.story('Expense delete')
def test_delete_expense(driver):
    login_page = LoginPage(driver)
    login_page.open()
    common_page = CommonPage(driver)
    common_page.expenses_field.click()
    common_page.delete_income.click()
    strings_list = ['95', 'Авто', 'Наличные деньги', str(date.today().year), str(date.today().month),
                    str(date.today().day)]
    common_page.accept_delete.click()
    strings_in_text = [x in common_page.income_list.text for x in strings_list]
    assert not all(strings_in_text)


@allure.feature('Expenses')
@allure.story('Expense add without all values')
def test_add_expenses_without_all(driver):
    login_page = LoginPage(driver)
    login_page.open()
    common_page = CommonPage(driver)
    common_page.expenses.click()
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


@allure.feature('Expenses')
@allure.story('Expense add only with account')
def test_add_expenses_with_account(driver):
    login_page = LoginPage(driver)
    login_page.open()
    common_page = CommonPage(driver)
    common_page.expenses.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.select_account
        )
    )
    common_page.select_account.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.cash
        )
    )
    common_page.cash.click()
    common_page.submit_income.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.alert
        )
    )
    assert 'Выберите категорию' in common_page.alert.text


@allure.feature('Expenses')
@allure.story('Expense add without currency')
def test_add_expenses_with_account_n_category(driver):
    login_page = LoginPage(driver)
    login_page.open()
    common_page = CommonPage(driver)
    common_page.expenses.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.select_account
        )
    )
    common_page.select_account.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.cash
        )
    )
    common_page.cash.click()
    common_page.select_category.click()
    common_page.auto_category.click()
    common_page.submit_income.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.alert
        )
    )
    assert 'Укажите сумму' in common_page.alert.text


@allure.feature('Expenses')
@allure.story('Expense add with incorrect value')
def test_add_expenses_with_incorrect_value(driver):
    login_page = LoginPage(driver)
    login_page.open()
    common_page = CommonPage(driver)
    common_page.expenses.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.select_account
        )
    )
    common_page.select_account.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.cash
        )
    )
    common_page.cash.click()
    common_page.select_category.click()
    common_page.auto_category.click()
    common_page.input_currency.send_keys('Fifty')
    common_page.submit_income.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.alert
        )
    )
    assert 'Укажите сумму' in common_page.alert.text


@allure.feature('Expenses')
@allure.story('add category in expense')
def test_add_category_expenses(driver):
    login_page = LoginPage(driver)
    login_page.open()
    common_page = CommonPage(driver)
    common_page.expenses.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.select_category
        )
    )
    common_page.select_category.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.auto_category
        )
    )
    common_page.add_category.click()
    common_page.input_category.send_keys('Courses')
    common_page.submit_new_category.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.select_category
        )
    )
    common_page.select_category.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.auto_category
        )
    )
    assert 'Courses' in common_page.categories_list.text
