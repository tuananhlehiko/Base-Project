from pages.components.locators import CongGameLocators, MainMenuLocators
import unittest
from selenium import webdriver
import time

from pages.Browser import Browser
import pages.components.page as page
from pages.components.locators import *
from pages.UIObject import UiObject


class GameLobby(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.get_driver()
        self.driver.get(ge.DOMAIN)

    # TOP - Link url check
    def test_url_link(self):
        lobby = page.GameLobbyPage(self.driver)  # Khai báo lobby page
        # Chờ để tất cả element ở trang load xong
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()  # Mở full màn hình đang test
        size = lobby.get_size()
        print('Full window size:', size, '\n')
        # lobby.set_size(1024, 768)

        # Variable Define
        MENU_CONG_GAME = UiObject(*MainMenuLocators.MENU_CONG_GAME)
        type_all = UiObject(*CongGameLocators.Type_All)
        type_No_hu = UiObject(*CongGameLocators.Type_No_hu)
        type_Ban_ca = UiObject(*CongGameLocators.Type_Ban_ca)
        type_Lo_de = UiObject(*CongGameLocators.Type_Lo_de)
        type_Ingame = UiObject(*CongGameLocators.Type_Ingame)
        type_Table_gane = UiObject(*CongGameLocators.Type_Table_game)
        type_Game_nhanh = UiObject(*CongGameLocators.Type_Game_nhanh)

        NCC_Selector = UiObject(*CongGameLocators.NCC_selector)
        NCC_Techplay = UiObject(*CongGameLocators.NCC_btn_Techplay)
        NCC_Pragmatic = UiObject(*CongGameLocators.NCC_btn_PragmaticPlay)
        NCC_CQ9 = UiObject(*CongGameLocators.NCC_btn_CQ9)

        Sort_multi = UiObject(*CongGameLocators.Sort_Nhieu_nguoi_choi)
        Sort_hot = UiObject(*CongGameLocators.Sort_Dang_hot)
        Sort_Pho_bien = UiObject(*CongGameLocators.Sort_Pho_bien)
        Sort_new = UiObject(*CongGameLocators.Sort_Moi_nhat)
        Sort_a_z = UiObject(*CongGameLocators.Sort_a_z)

        List_type = [
            [type_all, 'Tất cả', 'all'],
            [type_No_hu, 'Nổ hũ', 'no-hu'],
            [type_Ban_ca, 'Bắn cá', 'ban-ca'],
            [type_Lo_de, 'Lô đề', 'lo-de'],
            [type_Ingame, 'Ingame', 'ingame'],
            [type_Table_gane, 'Table game', 'table-games'],
            [type_Game_nhanh, 'Game nhanh', 'quick-game']
        ]

        List_NCC = [
            [NCC_Pragmatic, 'Pragmatic Play', 'pragmatic-play'],
            [NCC_CQ9, 'CQ9', 'cq9'],
            [NCC_Techplay, 'Techplay', 'techplay']
        ]

        List_Sort = [
            [Sort_multi, 'Nhiều người chơi', 'nhieu-nguoi-choi'],
            [Sort_hot, 'Đang hot', 'dang-hot'],
            [Sort_Pho_bien, 'Phổ biến', 'pho-bien'],
            [Sort_new, 'Mới nhất', 'moi-nhat'],
            [Sort_a_z, 'A-Z', 'a-z']
        ]
        TEST_RESULT = [['#', 'Slug 1', 'Slug 2', 'Slug 3',
                        'Expected link', 'Actual link', 'Status']]
        if MENU_CONG_GAME.visible():
            MENU_CONG_GAME.click()
            self.driver.implicitly_wait(30)
            time.sleep(3)

            df_link = 'http://dev-ta.mooo.com/cong-game?sx=nhieu-nguoi-choi'
            lobby_domain = 'http://dev-ta.mooo.com/cong-game?'
            c_url = lobby.get_url()
            TEST_RESULT.append(
                [1, 'default', 'default', 'default', df_link, c_url, ''])
            print('url', c_url)
            for S in List_Sort:
                S[0].click()
                expect = lobby_domain+'sx='+S[2]
                actual = lobby.get_url()
                sts = 'PASSED'
                if expect != actual:
                    lobby.screenshot_window('Sort', S[1], ' - FAILED')
                    sts = 'FAILED'
                TEST_RESULT.append(
                    [1, S[1], 'none', 'none', expect, actual, sts])
            for T in TEST_RESULT:
                print(T[4], '\t')
                print(T[5], '\t')
                print(T[6], '\n')
                # text = ''
                # for t in T:
                #     text = str(t)+' '
                # print(text)
        else:
            lobby.screenshot_window('Test Checking url link: FAILED')
            print('Login or Register button is not appear')
        self.driver.implicitly_wait(30)

    # TEST LOGIN VALID ACCOUNT - Fabet
    # def test_Login_with_valid_account(self):
    #     home = page.HomePage(self.driver)
    #     self.driver.implicitly_wait(30)
    #     # time.sleep(5)

    #     self.driver.maximize_window()
    #     size = home.get_size()
    #     print('Full window size:',size,'\n')
    #     home.set_size(1024, 768)

    #     LOGIN = UiObject(*HomePageLocators.btn_login)
    #     REGISTER = UiObject(*HomePageLocators.btn_register)
    #     USERNAME = UiObject(*HomePageLocators.txt_username)
    #     PASSWORD = UiObject(*HomePageLocators.txt_password)
    #     LOGIN_FULL = UiObject(*HomePageLocators.btn_login_full)
    #     LOGOUT = UiObject(*HomePageLocators.btn_logout)

    #     if LOGIN.visible() and REGISTER.visible():
    #         LOGIN.click()
    #         time.sleep(5)

    #         USERNAME.set_text('jimbi011234')
    #         PASSWORD.set_text('123456')
    #         LOGIN_FULL.click()
    #         time.sleep(5)
    #         assert LOGOUT.visible, 'Login is failed'
    #         home.screenshot_window('Test LOGIN - PASSED')
    #         print('SUCCESSFUL TO LOGIN TO WEB')
    #     else:
    #         print('Login or Register button is not appear')
    #     self.driver.implicitly_wait(10)
    #     time.sleep(5)

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
