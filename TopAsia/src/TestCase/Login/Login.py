import unittest
from selenium import webdriver
import time
from datetime import datetime
import xlsxwriter

from TopAsia.src.pages.Browser import Browser
import TopAsia.src.pages.page as page
from TopAsia.src.pages.page import *
from TopAsia.src.pages.locators import *
from TopAsia.src.pages.locators import LoginLocators as lg
from TopAsia.src.pages.locators import PopupLocators as pop
from TopAsia.src.pages.UIObject import UiObject
from TopAsia.src.pages.utils import *


class LoginFlow(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.get_driver()
        self.driver.get(ge.DOMAIN)

    # TOP - Link url check
    def test_Login(self):
        self.no = 1
        self.TEST_RESULT = [['#', 'Case', 'Data Input', 'Expected Error/Page link', 'Actual Error/Page link', 'Status', 'Notes']]
        self.TEST_DATA_HEADER = []
        self.name = 'LOGIN FLOW FROM HOME PAGE'
        start = datetime.now()
        self.TEST_DATA_HEADER.append(['Start', str(start).split('.')[0]])
        base = page.BasePage(self.driver)  # Khai báo base page handler
        # Chờ để tất cả element ở trang load xong
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()  # Mở full màn hình đang test
        SIZE = base.get_size()

        TEST_DATA = [
            [1, 'Data validation', 'INVALID', lg.lg_in_username, lg.lg_in_username_error, 'Không nhập tên đăng nhập', '', 'Yêu cầu nhập tên đăng nhập'],
            [2, 'Data validation', 'INVALID', lg.lg_in_username, lg.lg_in_username_error, 'Tên đăng nhập ít hơn 6 ký tự', 'abcde', 'Tên đăng nhập không hợp lệ, yêu cầu ít nhất 6 ký tự'],
            [3, 'Data validation', 'INVALID', lg.lg_in_username, lg.lg_in_username_error, 'Tên đăng nhập nhiều hơn 29 ký tự ', 'abcdefghijklnmopqrstuvwxyz1234', 'Tên đăng nhập ít hơn 30 ký tự'],
            [4, 'Data validation', 'INVALID', lg.lg_in_password, lg.lg_in_password_error, 'Mật khẩu ít hơn 6 ký tự', 'mnbvc', 'Mật khẩu không hợp lệ, yêu cầu ít nhất 6 ký tự'],
            [5, 'Data validation', 'INVALID', lg.lg_in_password, lg.lg_in_password_error, 'Mật khẩu nhiều hơn 12 ký tự ', 'sadfghjklqwer', 'Vui lòng không nhập nhiều hơn 12 ký tự'],
            [6, 'Data validation', 'INVALID', lg.lg_in_password, lg.lg_in_password_error, 'Không nhập mật khẩu', '', 'Yêu cầu nhập mật khẩu'],
            [7, 'Data validation', 'INVALID-MULTI', lg.lg_in_username, lg.lg_in_username_error, 'Tên đăng nhập với ký tự đặc biệt', '!@#$%^&*() ;:\'"`~>.<,{}[]\/-=+', 'Tên đăng nhập không chứa các ký tự đặc biệt'],
            [8, 'Data validation', 'INVALID-P', [lg.lg_in_username, lg.lg_in_password, [lg.lg_btn_login]], [pop.pop_el_is_display, pop.pop_txt_content, pop.pop_btn_confirm], 'Nhập sai tên đăng nhập', ['khongtontai', '123456'], 'Tên đăng nhập hoặc mật khẩu không đúng'],
            [9, 'Data validation', 'INVALID-P', [lg.lg_in_username, lg.lg_in_password, [lg.lg_btn_login]], [pop.pop_el_is_display, pop.pop_txt_content, pop.pop_btn_confirm], 'Nhập sai mật khẩu', ['tuananhle2203', 'khongdung'], 'Tên đăng nhập hoặc mật khẩu không đúng'],
            [10, 'Data validation', 'VALID', lg.lg_in_username, lg.lg_in_username_error, 'Tên đăng nhập = 6 ký tự', 'abcdef', ''],
            [11, 'Data validation', 'VALID', lg.lg_in_username, lg.lg_in_username_error, 'Tên đăng nhập = 29 ký tự', 'abcdefghijklnmopqrstuvwxyz123', ''],
            [12, 'Data validation', 'VALID', lg.lg_in_password, lg.lg_in_password_error, 'Mật khẩu = 6 ký tự', 'mnbvcx', ''],
            [13, 'Data validation', 'VALID', lg.lg_in_password, lg.lg_in_password_error, 'Mật khẩu = 12 ký tự', 'sadfghjklqwe', ''],
            [14, 'Navigation', 'FALSE', lg.lg_in_username, lg.lg_in_password, 'Nếu ví chính = 0, chuyển đến trang nạp tiền', ['tuananhle2603', '123456'], ge.DOMAIN + 'account/deposit'],
            [15, 'Navigation', 'TRUE', lg.lg_in_username, lg.lg_in_password, 'Nếu ví chính > 0, trở lại trang trước khi đăng nhập', ['tuananhle2603', '123456'], ge.DOMAIN + 'cong-game'],
            [16, 'Show/Hide pw', 'Hide a shown password', lg.lg_in_password, [lg.lg_ico_show_password, lg.lg_ico_hide_password], 'Click show password icon sẽ hiển thị những ký tự đã nhập', '', ''],
            [17, 'Show/Hide pw', 'Show a hidden password', lg.lg_in_password, [lg.lg_ico_show_password, lg.lg_ico_hide_password], 'Click hide password icon sẽ chuyển những ký tự hiển thị thành dấu * (hoặc chấm đen)', '', '']
        ]        

        if MainMenuLocators.mm_btn_dang_nhap.visible():
            MainMenuLocators.mm_btn_dang_nhap.click()
            self.driver.implicitly_wait(30)
            time.sleep(2)
            lg.lg_btn_login.click()
            time.sleep(2)
            Template_Report = Report_temp(self.name.upper(), self.TEST_RESULT, self.TEST_DATA_HEADER)
            # CHECK DEFAULT CASE
            for i in TEST_DATA:
                actual = ''
                sts = ''
                notes = ''
                print('\n', '-'*15, ' Case: ', str(i[0]), ': ', i[5], ' ', 15*'-')
                if i[1] == 'Data validation':
                    if 'INVALID' in i[2]:
                        if i[2] == 'INVALID-MULTI':
                            self.TEST_RESULT.append([i[0], i[5], '-', '-', '-', '-', '-'])
                            self.TEST_RESULT = self.TEST_RESULT+ValidateData.CheckINVALIDCase(i, self.name, base)
                        else:
                            self.TEST_RESULT.append(ValidateData.CheckINVALIDCase(i, self.name, base))
                    elif i[2] == 'VALID':
                        self.TEST_RESULT.append(ValidateData.CheckVALIDCase(i, self.name, base))
                elif i[1] == 'Show/Hide pw':
                    self.TEST_RESULT.append(ValidateData.ShowHideButton(i, self.name, base))
                elif i[1] == 'Navigation':
                    if i[2] == False:
                        if lg.lg_in_username.visible() == False:
                            MainMenuLocators.mm_btn_dang_nhap.click()
                            time.sleep(3)
                    else:
                        if lg.lg_in_username.visible() == False:
                            MainMenuLocators.mm_btn_cong_game.click()
                            time.sleep(5)
                            MainMenuLocators.mm_btn_dang_nhap.click()
                            time.sleep(3)
                        else:
                            DefaultLocators.df_btn_close.click()
                            MainMenuLocators.mm_btn_cong_game.click()
                            time.sleep(3)
                            MainMenuLocators.mm_btn_dang_nhap.click()
                            time.sleep(3)
                    i[3].set_text(i[6][0])
                    i[4].set_text(i[6][1])
                    time.sleep(3)
                    lg.lg_btn_login.click()
                    time.sleep(3)
                    if MainMenuLocators.mm_btn_open_dropdown.visible():
                        actual = base.get_url()
                        if actual == i[7]:
                            sts = 'PASSED'
                        else:
                            sts = 'FAILED'
                            notes = 'Login successful but link wrong'
                            base.ScrShot(str(i[0])+'_Login successful but link wrong', self.name)
                        MainMenuLocators.mm_btn_open_dropdown.click()
                        DefaultLocators.df_btn_logout.click()
                    else:
                        sts = 'FAILED'
                        notes = 'Login un-successful'
                        base.ScrShot(str(i[0])+'_Login un-successful', self.name)
                    self.TEST_RESULT.append([i[0], i[5], i[6][0]+', '+i[6][1], i[7], actual, sts, notes])

                    print('Status: \t', sts)
                    print('Expected: \t', i[7])
                    print('Actual: \t', actual, '\n')
                Template_Report = Report_temp(self.name.upper(), self.TEST_RESULT, self.TEST_DATA_HEADER)
                Template_Report.export()
                Template_Report.close()
                time.sleep(2)

            end = datetime.now()
            self.TEST_DATA_HEADER.append(['End', str(end).split('.')[0]])
            self.TEST_DATA_HEADER.append(
                ['Time spend', str(end-start).split('.')[0]])
            self.TEST_DATA_HEADER.append(['Size', str(SIZE)])
            # REPORT data

            report = Report(self.name.upper(), self.TEST_RESULT,
                            self.TEST_DATA_HEADER)
            report.export()
            report.close()

        else:
            base.ScrShot('[FAILED] '+self.name, self.name)
            # print('Login or Register button is not appear')
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
