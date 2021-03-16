import unittest
from selenium import webdriver
import time

from pages.Browser import Browser
import pages.components.page as page
from pages.components.locators import ge
from pages.components.locators import HomePageLocators
from pages.UIObject import UiObject


class Homepage_Test(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.get_driver()
        self.driver.get(ge.DOMAIN)

    # TEST LOGIN VALID ACCOUNT
    def test_Login_with_valid_account(self):
        home = page.HomePage(self.driver)
        self.driver.implicitly_wait(30)
        time.sleep(5)

        self.driver.maximize_window()
        LOGIN = UiObject(*HomePageLocators.btn_login)
        REGISTER = UiObject(*HomePageLocators.btn_register)
        USERNAME = UiObject(*HomePageLocators.txt_username)
        PASSWORD = UiObject(*HomePageLocators.txt_password)
        LOGIN_FULL = UiObject(*HomePageLocators.btn_login_full)
        LOGOUT = UiObject(*HomePageLocators.btn_logout)

        if LOGIN.visible() and REGISTER.visible():
            LOGIN.click(*HomePageLocators.btn_login)
            time.sleep(5)

            USERNAME.set_text('jimbi011234')
            PASSWORD.set_text('123456')
            LOGIN_FULL.click()
            time.sleep(5)
            assert LOGOUT.visible, 'Login is failed'
            home.screenshot_window('Test LOGIN - PASSED')
            print('SUCCESSFUL TO LOGIN TO WEB')
        else:
            print('Login or Register button is not appear')
        self.driver.implicitly_wait(10)
        time.sleep(5)

    # # TEST CASE 1
    # def test_Protected_is_activated(self):
    #     home = page.homePage(self.driver)
    #     assert home.is_title_match(), "About us title does't match."
    #     assert home.is_passster_form_appear(
    #     ), 'Passter-form is not appear, Page is not protected'
    #     self.driver.implicitly_wait(10)
    #     assert not home.is_main_content_appear()
    #     time.sleep(5)

    # # TEST CASE 2
    # def test_Valid_Password(self):
    #     home = page.homePage(self.driver)
    #     assert home.is_title_match(), "About us title does't match."
    #     assert home.is_passster_form_appear(
    #     ), 'Passter-form is not appear, Page is not protected'
    #     home.fill_password('YmeseTest')
    #     self.driver.implicitly_wait(10)
    #     assert not home.is_main_content_appear()
    #     time.sleep(5*60)
    #     assert not home.is_main_content_appear()
    #     # time.sleep(15*60)
    #     # assert not home.is_main_content_appear()
    #     # time.sleep(30*60)
    #     # assert not home.is_main_content_appear()
    #     # time.sleep(60*60)
    #     # assert not home.is_main_content_appear()
    #     self.driver.refresh()
    #     assert home.is_title_match()
    #     self.driver.implicitly_wait(10)
    #     assert not home.is_main_content_appear()
    #     home.submit_password('YmeseTest')
    #     self.driver.implicitly_wait(10)
    #     assert home.is_main_content_appear()
    #     time.sleep(5)

    # # TEST CASE 3
    # def test_Invalid_Password(self):
    #     home = page.homePage(self.driver)
    #     assert home.is_title_match(), "About us title does't match."
    #     assert home.is_passster_form_appear(
    #     ), 'Passter-form is not appear, Page is not protected'
    #     home.submit_password('YmeseTest_wrong')
    #     self.driver.implicitly_wait(10)
    #     assert home.is_alert_appear()
    #     assert not home.is_main_content_appear()
    #     time.sleep(5*60)
    #     assert not home.is_main_content_appear()
    #     # time.sleep(15*60)
    #     # assert not home.is_main_content_appear()
    #     # time.sleep(30*60)
    #     # assert not home.is_main_content_appear()
    #     # time.sleep(60*60)
    #     # assert not home.is_main_content_appear()
    #     self.driver.refresh()
    #     assert home.is_title_match()
    #     self.driver.implicitly_wait(10)
    #     assert not home.is_main_content_appear()
    #     time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
