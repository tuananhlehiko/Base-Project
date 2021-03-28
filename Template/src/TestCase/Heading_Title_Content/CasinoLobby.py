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
        self.cur_position = 0
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
            # [Game_Sicbo, 'Sicbo', 'type=sicbo'],
            [Game_Roulette, 'Roulette', 'type=roulette']
        ]

        List_NCC = [
            [NCC_All, 'All', 'ncc=all'],
            [NCC_Evolution, 'Evolution', 'ncc=evo'],
            [NCC_Ebet, 'Ebet', 'ncc=ebet'],
            [NCC_VivoGaming, 'VivoGaming', 'ncc=vivo'],
            [NCC_Allbet, 'Allbet', 'ncc=allbet'],
            [NCC_HGaming, 'HGaming', 'ncc=hogaming']
        ]

        List_Sort = [
            [Sort_multi, 'Nhiều Người Chơi', 'sx=most-played'],
            [Sort_hot, 'Đang Hot', 'sx=hot'],
            [Sort_Pho_bien, 'Phổ Biến', 'sx=popular'],
            [Sort_new, 'Mới Nhất', 'sx=new'],
            # [Sort_a_z, 'A-Z', 'sx=name']
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
            # RULE 1
            if len(NCC) > 0 or len(SORT) > 0:
                expected = expected + 'Top'
            # RULE 2, 3
            if len(NCC) > 0 or len(SORT) > 0:
                listgame = UiObject(*CasinoLocators.List_Game)
                if listgame.visible():
                    number_of_game = len(listgame.get_elements())
                else:
                    number_of_game = 0
                if number_of_game > 1:
                    expected = expected + ' ' + \
                        str(number_of_game) + ' Trò Chơi'
            # RULE 4
            if len(TYPE) > 0:
                if len(TYPE) > 1:
                    for t in range(len(TYPE)):
                        if t == 0:
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
                    expected = 'Live Casino Online'
                # RULE 5
                if len(SORT) > 0:
                    expected = expected + ' ' + SORT[0][1]
                # RULE 6 & 7
                if len(NCC) > 0:
                    if NCC[0][2] == 'ncc=all':
                        expected = expected + ' Của Live Casino'
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
        def click_and_check(obj, value=True, isAdded=True):
            obj[0].click()
            time.sleep(0.5)
            if value == False:
                DATA_LINK[self.cur_position] = 0
            else:
                DATA_LINK[self.cur_position] = obj
            check = check_link(DATA_LINK, self.no)
            if isAdded == True:
                self.cur_position += 1
            else:
                self.cur_position -= 1
                if self.cur_position < 0:
                    self.cur_position = 0
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
                ['-', 'Case chỉ có nhà cung cấp', '', '', '', '', '', '', ''])
            DATA_LINK = [0, 0, 0, 0, 0]
            for S in List_NCC:
                click_and_check(S)
                self.cur_position -= 1
                time.sleep(0.5)
            temp_rp.export()
            temp_rp.close()

            # CHECK ALL CASE FOLLOWING: SORT >> SUPPLIER >> GAME TYPE
            # TEST_RESULT.append(['', 'Nhà cung cấp', 'Sắp xếp theo', 'Game 1', 'Game 2', 'Game 3', '', '', ''])
            DATA_LINK = [0, 0, 0, 0, 0]
            for N in List_NCC:
                click_and_check(N)
                for S in List_Sort:
                    click_and_check(S)
                    for G in range(len(List_Game)):
                        List_Game_B = [x for x in List_Game]
                        List_Game_B.pop(G)                        
                        Game_Selector.click()
                        click_and_check(List_Game[G])
                        for SG in List_Game_B:
                            click_and_check(SG)
                            time.sleep(1)
                        # ---------------------------------------------------------
                        # UNCHECK GAME 3
                        # Game_Selector.click()
                        for SG in List_Game_B:
                            click_and_check(SG,False,False)
                            time.sleep(1)
                        click_and_check(List_Game[G],False,False)
                        Game_Selector.click()
                        self.cur_position -= 1
                        temp_rp = Report_temp(
                            name.upper(), TEST_RESULT, TEST_DATA_HEADER)
                        temp_rp.export()
                        temp_rp.close()
                    self.cur_position -= 1
                self.cur_position -= 1

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
