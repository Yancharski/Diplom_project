import pytest
from pages.login_page import LoginPage
from pages.common_page import CommonPage
import allure


@allure.feature('Languages')
@allure.story('Change language to English')
def test_change_language(driver):
    login_page = LoginPage(driver)
    login_page.open()
    common_page = CommonPage(driver)
    cash_in_rus = common_page.accounts_cash.text
    common_page.change_language.click()
    common_page.english_language.click()
    assert cash_in_rus != common_page.accounts_cash.text


@allure.feature('Languages')
@allure.story('Change language to English and watch categories')
def test_change_language_category(driver):
    login_page = LoginPage(driver)
    login_page.open()
    common_page = CommonPage(driver)
    common_page.duty.click()
    duty_in_rus = common_page.title_of_duty.text
    common_page.change_language.click()
    common_page.english_language.click()
    assert duty_in_rus != common_page.title_of_duty.text

