from pages.login_page import LoginPage
from pages.common_page import CommonPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import allure


@allure.feature('Teams')
@allure.story('Make a team')
def test_make_a_team(driver):
    login_page = LoginPage(driver)
    login_page.open()
    common_page = CommonPage(driver)
    common_page.three_humans.click()
    common_page.make_a_team.click()
    common_page.input_team_name.send_keys('Team from dream 1')
    common_page.submit_new_team.click()
    common_page.three_humans.click()
    assert 'Team from dream 1' in common_page.teams_container.text


@allure.feature('Teams')
@allure.story('Switch team')
def test_switch_team(driver):
    login_page = LoginPage(driver)
    login_page.open()
    common_page = CommonPage(driver)
    common_page.three_humans.click()
    common_page.dream_team.click()
    assert 'Dream Team' in common_page.name_of_user.text


@allure.feature('Teams')
@allure.story('Income in team')
def test_income_in_team(driver):
    login_page = LoginPage(driver)
    login_page.open()
    common_page = CommonPage(driver)
    common_page.three_humans.click()
    common_page.dream_team.click()
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
    sleep(3)
    assert '155' in common_page.income_field.text


@allure.feature('Teams')
@allure.story('Income in team and check other team')
def test_income_in_team_and_check_other_team(driver):
    login_page = LoginPage(driver)
    login_page.open()
    common_page = CommonPage(driver)
    common_page.three_humans.click()
    common_page.team_from_dream.click()
    sleep(3)
    assert '0' in common_page.income_field.text

