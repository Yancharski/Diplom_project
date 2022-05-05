from pages.login_page import LoginPage
from pages.common_page import CommonPage
import allure


@allure.feature('Logout')
@allure.story('Check_logout')
def test_check_logout(driver):
    login_page = LoginPage(driver)
    login_page.open()
    common_page = CommonPage(driver)
    common_page.personal_account.click()
    common_page.logout.click()
    assert login_page.email_field.is_displayed()
