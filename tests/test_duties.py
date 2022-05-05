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


@allure.feature('Duties')
@allure.story('Duty add')
@pytest.mark.skip
def test_add_duty(driver):
    login_page = LoginPage(driver)
    login_page.open()
    common_page = CommonPage(driver)
    common_page.duty.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.add_duty
        )
    )
    common_page.add_duty.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.checkbox
        )
    )
    common_page.checkbox.click()
    common_page.contragent.click()
    common_page.add_contragent.click()
    common_page.input_contragent.send_keys(common_page.name_of_contragent)
    common_page.submit_new_contragent.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.choose_valute
        )
    )
    sleep(0.5)
    common_page.choose_valute.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.BYN
        )
    )
    common_page.BYN.click()
    common_page.input_currency.send_keys('200')
    common_page.submit_duty.click()
    sleep(5)
    strings_list = ['200', common_page.name_of_contragent]
    strings_in_text = [x in common_page.duties_list.text for x in strings_list]
    assert all(strings_in_text)


@allure.feature('Duties')
@allure.story('Duty add in balance')
def test_add_duty_balance(driver):
    login_page = LoginPage(driver)
    login_page.open()
    common_page = CommonPage(driver)
    common_page.duty.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.back_to_menu
        )
    )
    common_page.back_to_menu.click()
    assert '200' in common_page.balance.text



@allure.feature('Duties')
@allure.story('Duty return')
@pytest.mark.skip
def test_return_duty(driver):
    login_page = LoginPage(driver)
    login_page.open()
    common_page = CommonPage(driver)
    common_page.duty.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.return_duty
        )
    )
    common_page.return_duty.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.checkbox
        )
    )
    common_page.checkbox.click()
    common_page.contragent.click()
    common_page.BYN.click()
    common_page.choose_valute.click()
    common_page.chosen_contragent.click()
    common_page.input_currency.send_keys('200')
    common_page.accept_return_duty.click()
    assert common_page.name_of_contragent in common_page.completed_duties.text


@allure.feature('Duties')
@allure.story('Contragent_delete')
def test_delete_duty(driver):
    login_page = LoginPage(driver)
    login_page.open()
    common_page = CommonPage(driver)
    common_page.duty.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.return_duty
        )
    )
    common_page.comlete_contargent.click()
    name = common_page.now_name.text
    common_page.delete_contragent.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.accept_delete_contaragent
        )
    )
    common_page.accept_delete_contaragent.click()
    common_page.close_alert.click()
    assert not name in common_page.completed_duties.text


@allure.feature('Duties')
@allure.story('Duty add without all')
def test_add_duty_without_all(driver):
    login_page = LoginPage(driver)
    login_page.open()
    common_page = CommonPage(driver)
    common_page.duty.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.add_duty
        )
    )
    common_page.add_duty.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.checkbox
        )
    )
    common_page.checkbox.click()
    common_page.submit_duty.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.alert
        )
    )
    assert 'Выберите валюту' in common_page.alert.text


@allure.feature('Duties')
@allure.story('Duty add only with valute')
def test_add_duty_with_valute(driver):
    login_page = LoginPage(driver)
    login_page.open()
    common_page = CommonPage(driver)
    common_page.duty.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.add_duty
        )
    )
    common_page.add_duty.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.checkbox
        )
    )
    common_page.checkbox.click()
    common_page.choose_valute.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.BYN
        )
    )
    common_page.BYN.click()
    common_page.submit_duty.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.alert
        )
    )
    assert 'Укажите контрагента' in common_page.alert.text


@allure.feature('Duties')
@allure.story('Duty add only with valute and contragent')
def test_add_duty_with_valute_n_contragent(driver):
    login_page = LoginPage(driver)
    login_page.open()
    common_page = CommonPage(driver)
    common_page.duty.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.add_duty
        )
    )
    common_page.add_duty.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.checkbox
        )
    )
    common_page.checkbox.click()
    common_page.choose_valute.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.BYN
        )
    )
    common_page.BYN.click()
    common_page.contragent.click()
    common_page.chosen_contragent.click()
    common_page.submit_duty.click()
    assert 'Необходимо указать значение' in common_page.error.text


@allure.feature('Duties')
@allure.story('Duty add with incorrect value')
def test_add_duty_with_incorrect_value(driver):
    login_page = LoginPage(driver)
    login_page.open()
    common_page = CommonPage(driver)
    common_page.duty.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.add_duty
        )
    )
    common_page.add_duty.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.checkbox
        )
    )
    common_page.checkbox.click()
    common_page.choose_valute.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            common_page.BYN
        )
    )
    common_page.BYN.click()
    common_page.contragent.click()
    common_page.chosen_contragent.click()
    common_page.input_currency.send_keys('')
    common_page.submit_duty.click()
    assert 'Необходимо указать значение' in common_page.error.text

