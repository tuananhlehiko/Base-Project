from locators import HomePageLocators
import unittest
from selenium import webdriver
import page
import time


class Homepage_Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path="D:\Developer\Webdriver\chromedriver.exe")
        self.driver.get('https://v2.fabet.info/')

    # TEST LOGIN VALID ACCOUNT
    def test_Login_with_valid_account(self):
        home = page.HomePage(self.driver)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        if home.is_button_appear(HomePageLocators.btn_login) == False:
            print('- The login button is not appear')
        if home.is_button_appear(HomePageLocators.btn_register) == False:
            print('- The register button is not appear')
        if home.is_button_appear(HomePageLocators.btn_login) and home.is_button_appear(HomePageLocators.btn_register):
            home.tap_button(HomePageLocators.btn_login)
            time.sleep(5)
            home.fill_text(HomePageLocators.txt_username, 'jimbi011234')
            home.fill_text(HomePageLocators.txt_password, '123456')
            home.tap_button(HomePageLocators.btn_login_full)
            time.sleep(5)
            assert home.is_button_appear(
                HomePageLocators.btn_logout), 'Login is failed'
            home.screenshot_window('Test LOGIN - PASSED')
            print('SUCCESSFUL TO LOGIN TO WEB')
        else:
            print('Login or Register button is not appear')

        self.driver.implicitly_wait(10)
        # assert not home.is_main_content_appear()
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
