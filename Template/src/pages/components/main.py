import re
import unittest
from selenium import webdriver
import time
from datetime import datetime
import xlsxwriter

from pages.Browser import Browser
import pages.components.page as page
from pages.components.locators import *
from pages.components.locators import CongGameLocators, MainMenuLocators
from pages.UIObject import UiObject
from pages.components.utils import *


class GameLobby(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.get_driver()
        self.driver.get(ge.DOMAIN)

    # TOP - Link url check
    def test_url_link(self):
        TEST_RESULT = [['#', 'Slug 1', 'Slug 2', 'Slug 3',
                        'Expected link', 'Actual link', 'Status']]
        TEST_DATA_HEADER = []
        start = datetime.now()
        TEST_DATA_HEADER.append(['Start', str(start).split('.')[0]])
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
            [type_all, 'Tat ca', 'type=all'],
            [type_No_hu, 'No hu', 'type=no-hu'],
            [type_Ban_ca, 'Ban Ca', 'type=ban-ca'],
            [type_Game_nhanh, 'Game nhanh', 'type=quick-game'],
            [type_Ingame, 'Ingame', 'type=ingame'],
            [type_Table_gane, 'Table game', 'type=table-games'],
            [type_Lo_de, 'Lo de', 'type=lo-de']
        ]

        List_NCC = [
            [NCC_Pragmatic, 'Pragmatic Play', 'ncc=pragmatic-play'],
            [NCC_CQ9, 'CQ9', 'ncc=cq9'],
            [NCC_Techplay, 'Techplay', 'ncc=techplay']
        ]

        List_Sort = [
            [Sort_multi, 'Nhiều người chơi', 'sx=nhieu-nguoi-choi'],
            [Sort_hot, 'Đang hot', 'sx=dang-hot'],
            [Sort_Pho_bien, 'Phổ biến', 'sx=pho-bien'],
            [Sort_new, 'Mới nhất', 'sx=moi-nhat'],
            [Sort_a_z, 'A-Z', 'sx=a-z']
        ]

        if MENU_CONG_GAME.visible():

            MENU_CONG_GAME.click()
            self.driver.implicitly_wait(30)
            time.sleep(3)
            no = 1

            # CHECK DEFAULT
            df_link = 'http://dev-ta.mooo.com/cong-game?sx=nhieu-nguoi-choi'
            lobby_domain = 'http://dev-ta.mooo.com/cong-game?'
            c_url = lobby.get_url()
            sts = 'PASSED'
            if df_link != c_url:
                lobby.screenshot_window('Default link - FAILED')
                sts = 'FAILED'
            TEST_RESULT.append(
                [no, 'default', 'default', 'default', df_link, c_url, sts])
            no += 1
            print('url', c_url)

            # CHECK CASE ONLY SORT
            TEST_RESULT.append(
                ['-', 'Sắp xếp theo', 'None', 'None', '-', '-', '-'])
            for S in List_Sort:
                S[0].click()
                expect = lobby_domain+S[2]
                actual = lobby.get_url()
                sts = 'PASSED'
                if expect != actual:
                    lobby.screenshot_window('Sort_' + S[1], ' - FAILED')
                    sts = 'FAILED'
                TEST_RESULT.append(
                    [no, S[1], '-', '-', expect, actual, sts])
                no += 1
                time.sleep(1)

            # CHECK ALL CASE
            TEST_RESULT.append(
                ['-', 'Sắp xếp theo', 'Thể loại', 'Nhà cung cấp', '-', '-', '-'])
            DATA_LINK = [0, 0, 0]

            def check_link(data):
                data_return = [no]
                if data[0] != 0:
                    expected = lobby_domain+data[0][2]
                    data_return.append(data[0][1])
                else:
                    data_return.append('-')
                if data[1] != 0:
                    expected = expected + '&' + data[1][2]
                    data_return.append(data[1][1])
                else:
                    data_return.append('-')
                if data[2] != 0:
                    expected = expected + '&' + data[2][2]
                    data_return.append(data[2][1])
                else:
                    data_return.append('-')
                data_return.append(expected)
                actual = lobby.get_url()
                data_return.append(expected)
                if actual != expected:
                    data_return.append('FAILED')
                else:
                    data_return.append('PASSED')
                return data_return

            for S in List_Sort:
                S[0].click()
                time.sleep(1)
                DATA_LINK[0] = S
                check = check_link(DATA_LINK)
                TEST_RESULT.append(check)
                for T in List_type:
                    print('------------------',str(T[1]))
                    if T[1] == 'Game nhanh' or T[1] == 'Ingame' or T[1] == 'Table game' or T[1] == 'Lo de':
                        if T[1] == 'Lo de':
                            T[0].click()
                            time.sleep(1)
                            DATA_LINK[0] = T
                            DATA_LINK[1] = 0
                            DATA_LINK[2] = 0
                            check = check_link(DATA_LINK)
                            TEST_RESULT.append(check)
                            DATA_LINK[0] = S
                        else:
                            T[0].click()
                            time.sleep(1)
                            DATA_LINK[1] = T                           
                            check = check_link(DATA_LINK)
                            TEST_RESULT.append(check)                            
                    else:
                        T[0].click()
                        time.sleep(1)
                        DATA_LINK[1] = T
                        check = check_link(DATA_LINK)
                        TEST_RESULT.append(check)
                        for N in List_type:
                            NCC_Selector.click()
                            time.sleep(2)
                            N[0].click(True)
                            time.sleep(1)
                            DATA_LINK[2] = N
                            check = check_link(DATA_LINK)
                            TEST_RESULT.append(check)
                            # UNCHECK NHÀ CUNG CẤP
                            NCC_Selector.click()
                            time.sleep(2)
                            N[0].click(True)
                            time.sleep(1)
                            DATA_LINK[2] = 0
                            check = check_link(DATA_LINK)
                            TEST_RESULT.append(check)

            end = datetime.now()
            TEST_DATA_HEADER.append(['End', str(end).split('.')[0]])
            TEST_DATA_HEADER.append(
                ['Time spend', str(end-start).split('.')[0]])
            TEST_DATA_HEADER.append(['Size', str(size)])
            # REPORT data
            name = 'Test link formats'
            report = Report(name.upper(), TEST_RESULT, TEST_DATA_HEADER)
            report.export()
            report.close()

        else:
            lobby.screenshot_window('Test Checking url link: FAILED')
            print('Login or Register button is not appear')
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
