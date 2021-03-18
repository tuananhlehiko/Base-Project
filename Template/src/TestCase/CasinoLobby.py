import unittest
from selenium import webdriver
import time
from datetime import datetime
import xlsxwriter

from pages.Browser import Browser
import pages.page as page
from pages.locators import *
from pages.UIObject import UiObject
from pages.utils import *


class CasinoLobby(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.get_driver()
        self.driver.get(ge.DOMAIN)

    # TOP - Link url check
    def test_url_link(self):
        self.no = 1
        DATA_LINK = [0, 0, 0, 0, 0]
        TEST_RESULT = [['#', 'Slug 1', 'Slug 2', 'Slug 3', 'Slug 4',
                        'Slug 5', 'Expected link', 'Actual link', 'Status']]
        TEST_DATA_HEADER = []
        name = 'Test link formats - CASINO LOBBY'
        start = datetime.now()
        TEST_DATA_HEADER.append(['Start', str(start).split('.')[0]])
        lobby = page.GameLobbyPage(self.driver)  # Khai báo lobby page
        # Chờ để tất cả element ở trang load xong
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()  # Mở full màn hình đang test
        SIZE = lobby.get_size()

        # Variable Define
        MENU_CASINO = UiObject(*MainMenuLocators.MENU_LIVE_CASINO)
        NCC_All = UiObject(*CasinoLocators.NCC_All)
        NCC_Evolution = UiObject(*CasinoLocators.NCC_Evolution)
        NCC_Ebet = UiObject(*CasinoLocators.NCC_Ebet)
        NCC_VivoGaming = UiObject(*CasinoLocators.NCC_Vivo)
        NCC_Allbet = UiObject(*CasinoLocators.NCC_Allbet)
        NCC_HGaming = UiObject(*CasinoLocators.NCC_HGaming)

        Game_Selector = UiObject(*CasinoLocators.Game_selector)
        Game_Baccarat = UiObject(*CasinoLocators.Game_Baccarat)
        Game_Sicbo = UiObject(*CasinoLocators.Game_Sicbo)
        Game_Roulette = UiObject(*CasinoLocators.Game_Roulette)

        Sort_multi = UiObject(*CasinoLocators.Sort_Nhieu_nguoi_choi)
        Sort_hot = UiObject(*CasinoLocators.Sort_Dang_hot)
        Sort_Pho_bien = UiObject(*CasinoLocators.Sort_Pho_bien)
        Sort_new = UiObject(*CasinoLocators.Sort_Moi_nhat)
        Sort_a_z = UiObject(*CasinoLocators.Sort_a_z)

        List_Game = [
            [Game_Baccarat, 'Baccarat', 'game=baccarat'],
            [Game_Sicbo, 'Sicbo', 'game=sicbo'],
            [Game_Roulette, 'Roulette', 'game=roulette']
        ]

        List_NCC = [
            [NCC_All, 'All', 'ncc=all'],
            [NCC_Evolution, 'Evolution', 'ncc=evolution'],
            [NCC_Ebet, 'Ebet', 'ncc=ebet'],
            [NCC_VivoGaming, 'VivoGaming', 'ncc=vvgaming'],
            [NCC_Allbet, 'Allbet', 'ncc=allbet'],
            [NCC_HGaming, 'HGaming', 'ncc=hgaming']
        ]

        List_Sort = [
            [Sort_multi, 'Nhiều người chơi', 'sx=nhieu-nguoi-choi'],
            [Sort_hot, 'Đang hot', 'sx=dang-hot'],
            [Sort_Pho_bien, 'Phổ biến', 'sx=pho-bien'],
            [Sort_new, 'Mới nhất', 'sx=moi-nhat'],
            [Sort_a_z, 'A-Z', 'sx=a-z']
        ]

        # COMPARE LINK AND RETURN DATA LIST
        def check_link(data, number):
            data_return = [number]
            expected = ''
            for i in range(len(data)):
                if data[i] != 0:
                    if i == 0:
                        expected = lobby_domain+data[i][2]
                    else:
                        expected = expected + '&' + data[i][2]
                    data_return.append(data[i][1])
                else:
                    data_return.append('-')
            data_return.append(expected)
            actual = lobby.get_url()
            data_return.append(actual)
            if actual != expected:
                data_return.append('FAILED')
                # lobby.screenshot_window(str(number) + '_' + data_return[1] + '_' + data_return[2] + '_' + data_return[3]+ '_' + data_return[4]+ '_' + data_return[5])
            else:
                data_return.append('PASSED')
            print('\n', '-'*15, ' Case: ', number,
                  ': ', data_return[8], ' ', 15*'-')
            print(data_return[1], ' - ', data_return[2], ' - ',
                  data_return[3], ' - ', data_return[4], ' - ', data_return[5])
            print('Expected link: \t', data_return[6])
            print('Actual link: \t', data_return[7])
            return data_return

        # num : vị trí ở DATALINK, value:
        def click_and_check(obj, num, value=0):
            obj[0].click()
            time.sleep(0.5)
            if value == 0:
                DATA_LINK[num] = 0
            else:
                DATA_LINK[num] = obj
            check = check_link(DATA_LINK, self.no)
            self.no = self.no + 1 
            TEST_RESULT.append(check)

        if MENU_CASINO.visible():
            MENU_CASINO.click()
            self.driver.implicitly_wait(30)
            time.sleep(3)
            temp_rp = Report_temp(name.upper(), TEST_RESULT, TEST_DATA_HEADER)
            # CHECK DEFAULT CASE
            df_link = 'http://dev-ta.mooo.com/casino?sx=nhieu-nguoi-choi'
            lobby_domain = 'http://dev-ta.mooo.com/casino?'
            c_url = lobby.get_url()
            sts = 'PASSED'
            # self.no = 1
            if df_link != c_url:
                # lobby.screenshot_window('Default link - FAILED')
                sts = 'FAILED'
            TEST_RESULT.append(
                [self.no, 'default', 'default', 'default', 'default', 'default', df_link, c_url, sts])
            self.no += 1
            # print('url', c_url)

            # CHECK ONLY SORT CASE
            TEST_RESULT.append(
                ['-', 'Sắp xếp theo', 'None', 'None', 'None', 'None', '', '', ''])
            DATA_LINK = [0, 0, 0, 0, 0]
            for S in List_Sort:
                click_and_check(S, 0, 1)
                time.sleep(0.5)
            temp_rp.export()
            temp_rp.close()

            # CHECK ALL CASE FOLLOWING: SORT >> SUPPLIER >> GAME TYPE
            TEST_RESULT.append(
                ['', 'Sắp xếp theo', 'Nhà cung cấp', 'Game 1', 'Game 2', 'Game 3', '', '', ''])
            DATA_LINK = [0, 0, 0, 0, 0]
            for S in List_Sort:
                click_and_check(S, 0, 1)
                for N in List_NCC:
                    click_and_check(N, 1, 1)
                    for G in range(len(List_Game)):
                        if G == 0:
                            G1 = List_Game[G]
                            G2 = List_Game[1]
                            G3 = List_Game[2]
                        elif G == 1:
                            G1 = List_Game[G]
                            G2 = List_Game[0]
                            G3 = List_Game[2]
                        else:
                            G1 = List_Game[G]
                            G2 = List_Game[0]
                            G3 = List_Game[1]
                        # 1 GAME SELECTED
                        Game_Selector.click()
                        time.sleep(2)
                        click_and_check(G1, 2, 1)
                        # 2 GAME SELECTED
                        # Game_Selector.click()
                        click_and_check(G2, 3, 1)
                        # 3 GAME SELECTED
                        # Game_Selector.click()
                        click_and_check(G3, 4, 1)

                        # ---------------------------------------------------------
                        # UNCHECK GAME 3
                        # Game_Selector.click()
                        click_and_check(G3, 4, 0)
                        # UNCHECK GAME 2
                        # Game_Selector.click()
                        click_and_check(G2, 3, 0)
                        # UNCHECK GAME 1
                        # Game_Selector.click()
                        click_and_check(G1, 2, 0)
                        Game_Selector.click()

                        temp_rp = Report_temp(
                            name.upper(), TEST_RESULT, TEST_DATA_HEADER)
                        temp_rp.export()
                        temp_rp.close()

            # CHECK ALL CASE FOLLOWING: SORT >> GAMETYPE >> SUPPLIER
            TEST_RESULT.append(
                ['', 'Sắp xếp theo', 'Game 1', 'Thể loại', '', '', '', '', ''])
            DATA_LINK = [0, 0, 0, 0, 0]
            for S in List_Sort:
                click_and_check(S, 0, 1)
                for G in range(len(List_Game)):
                    if G == 0:
                        G1 = List_Game[G]
                        G2 = List_Game[1]
                        G3 = List_Game[2]
                    elif G == 1:
                        G1 = List_Game[G]
                        G2 = List_Game[0]
                        G3 = List_Game[2]
                    else:
                        G1 = List_Game[G]
                        G2 = List_Game[0]
                        G3 = List_Game[1]

                    # 1 GAME SELECTED
                    Game_Selector.click()
                    time.sleep(2)
                    click_and_check(G1, 1, 1)
                    for N in List_NCC:
                        click_and_check(N, 2, 1)
                    DATA_LINK[2] = 0

                    # 2 GAME SELECTED
                    Game_Selector.click()
                    time.sleep(2)
                    G1[0].click()
                    time.sleep(0.5)
                    click_and_check(G2, 2, 1)
                    for N in List_NCC:
                        click_and_check(N, 3, 1)
                    DATA_LINK[3] = 0
                    # 3 GAME SELECTED
                    # Game_Selector.click()
                    Game_Selector.click()
                    time.sleep(2)
                    G1[0].click()
                    time.sleep(0.5)
                    G2[0].click()
                    time.sleep(0.5)
                    click_and_check(G3, 3, 1)
                    for N in List_NCC:
                        click_and_check(N, 4, 1)
                    DATA_LINK[4] = 0
                    # ---------------------------------------------------------
                    # UNCHECK GAME 3
                    Game_Selector.click()
                    time.sleep(2)
                    click_and_check(G3, 3, 0)
                    for N in List_NCC:
                        click_and_check(N, 3, 1)
                    DATA_LINK[3] = 0
                    # UNCHECK GAME 2
                    Game_Selector.click()
                    time.sleep(2)
                    click_and_check(G2, 2, 0)
                    for N in List_NCC:
                        click_and_check(N, 2, 1)
                    DATA_LINK[2] = 0
                    # UNCHECK GAME 1
                    Game_Selector.click()
                    time.sleep(2)
                    click_and_check(G1, 1, 0)
                    for N in List_NCC:
                        click_and_check(N, 1, 1)

                    temp_rp = Report_temp(
                        name.upper(), TEST_RESULT, TEST_DATA_HEADER)
                    temp_rp.export()
                    temp_rp.close()
                    for N in List_NCC:
                        click_and_check(N, 1, 1)

            end = datetime.now()
            TEST_DATA_HEADER.append(['End', str(end).split('.')[0]])
            TEST_DATA_HEADER.append(
                ['Time spend', str(end-start).split('.')[0]])
            TEST_DATA_HEADER.append(['Size', str(SIZE)])
            # REPORT data

            report = Report(name.upper(), TEST_RESULT, TEST_DATA_HEADER)
            report.export()
            report.close()

        else:
            lobby.screenshot_window('Test Checking url link: FAILED')
            # print('Login or Register button is not appear')
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
