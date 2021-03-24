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


class CasinoLobbyHeadingTitle(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.get_driver()
        self.driver.get(ge.DOMAIN)

    # TOP - Link url check
    def test_Heading_Title_Content(self):
        self.no = 1
        self.lobby_domain = 'http://dev-ta.mooo.com/live-casino?'
        DATA_LINK = [0, 0, 0, 0, 0]
        TEST_RESULT = [['#', 'Slug 1', 'Slug 2', 'Slug 3', 'Slug 4',
                        'Slug 5', 'Expected link', 'Actual link', 'Status']]
        TEST_DATA_HEADER = []
        name = 'HEADING TITLE CONTENT - CASINO LOBBY'
        start = datetime.now()
        TEST_DATA_HEADER.append(['Start', str(start).split('.')[0]])
        lobby = page.GameCasinoPage(self.driver)  # Khai báo lobby page
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
            [Game_Baccarat, 'Baccarat', 'type=baccarat'],
            [Game_Sicbo, 'Sicbo', 'type=sicbo'],
            [Game_Roulette, 'Roulette', 'type=roulette']
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
            [Sort_multi, 'Nhiều Người Chơi', 'sx=nhieu-nguoi-choi'],
            [Sort_hot, 'Đang Hot', 'sx=dang-hot'],
            [Sort_Pho_bien, 'Phổ Biến', 'sx=pho-bien'],
            [Sort_new, 'Mới Nhất', 'sx=moi-nhat'],
            [Sort_a_z, 'A-Z', 'sx=a-z']
        ]

        # COMPARE LINK AND RETURN DATA LIST
        def check_link(data, number):
            expected = ''
            TYPE = []
            NCC = []
            SORT = []
            data_return = [self.no]
            self.no += 1
            for i in data:
                if i != 0:
                    if 'type' in i[2]:
                        TYPE.append(i)
                    if 'ncc' in i[2]:
                        NCC.append(i)
                    if 'sx' in i[2]:
                        SORT.append(i)

            # print('TYPE: ', TYPE)
            # print('NCC: ', NCC)
            # print('SORT: ', SORT)
            # RULE 1
            if len(NCC) > 0 or len(SORT) > 0:
                expected = expected + 'Top'

            # RULE 2, 3
            if len(NCC) > 0 or len(SORT) > 0:
                listgame = UiObject(*CasinoLocators.List_Game)
                number_of_game = len(listgame.get_elements())
                # number_of_game = 79

                if number_of_game > 1:
                    expected = expected + ' ' + \
                        str(number_of_game) + ' Trò Chơi'
            # RULE 4
            if len(TYPE) > 0:
                if len(TYPE) > 1:
                    for t in range(len(TYPE)):
                        if t ==0:
                            expected = expected + ' ' + TYPE[t][1]
                        else:
                            expected = expected + ', ' + TYPE[t][1]
                else:
                    if TYPE[0][2] == 'type=all':
                        expected = expected + ' Cổng Game'
                    else:
                        expected = expected + ' ' + TYPE[0][1]
                if len(NCC) == 0 and len(SORT) == 0:
                    expected = expected + ' Online'
                # RULE 5
                if len(SORT) > 0:
                    expected = expected + ' ' + SORT[0][1]
                # RULE 6 & 7
                if len(NCC) > 0:
                    if NCC[0][2] == 'ncc=all':
                        expected = expected + ' Live Casino'
                    else:
                        expected = expected + ' Của ' + NCC[0][1]
            else:
                if len(NCC) == 0 and len(SORT) == 0:
                    expected = expected + 'Online Live Casino'
                # RULE 5
                if len(SORT) > 0:
                    expected = expected + ' ' + SORT[0][1]
                # RULE 6 & 7
                if len(NCC) > 0:
                    if NCC[0][2] == 'ncc=all':
                        expected = expected + ' Live Casino'
                    else:
                        expected = expected + ' Của ' + NCC[0][1]

            for t in TYPE:
                data_return.append(t[1])
            if len(TYPE) > 0:
                if len(NCC) != 0:
                    data_return.append(NCC[0][1])
                if len(SORT) != 0:
                    data_return.append(SORT[0][1])
            else:
                if len(NCC) != 0:
                    data_return.append(NCC[0][1])
                    if len(SORT) != 0:
                        data_return.append(SORT[0][1])
                else:
                    if len(SORT) != 0:
                        data_return.append(SORT[0][1])

            while len(data_return) < 6:
                data_return.append('-')
            data_return.append(expected)
            actual = UiObject(*CasinoLocators.List_Game_Heading).get_text()
            data_return.append(actual)
            if actual != expected:
                data_return.append('FAILED')
                # lobby.screenshot_window(str(number) + '_' + data_return[1] + '_' + data_return[2] + '_' + data_return[3]+ '_' + data_return[4]+ '_' + data_return[5])
            else:
                data_return.append('PASSED')
            print('\n', '-'*15, ' Case: ', number,
                  ': ', data_return[6], ' ', 15*'-')
            print(data_return[1], ' - ', data_return[2],
                  ' - ', data_return[3], ' - ', data_return[4], ' - ', data_return[5], ' - ')
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
            TEST_RESULT.append(check)

        if MENU_CASINO.visible():
            MENU_CASINO.click()
            self.driver.implicitly_wait(30)
            time.sleep(3)
            temp_rp = Report_temp(name.upper(), TEST_RESULT, TEST_DATA_HEADER)

            # CHECK DEFAULT CASE            
            check = check_link(DATA_LINK, self.no)
            TEST_RESULT.append(check)

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
            # TEST_RESULT.append(['', 'Sắp xếp theo', 'Nhà cung cấp', 'Game 1', 'Game 2', 'Game 3', '', '', ''])
            DATA_LINK = [0, 0, 0, 0, 0]
            for S in List_Sort:
                DATA_LINK[1] = List_NCC[0]
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
                        List_NCC[0][0].click()

                        temp_rp = Report_temp(
                            name.upper(), TEST_RESULT, TEST_DATA_HEADER)
                        temp_rp.export()
                        temp_rp.close()

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
