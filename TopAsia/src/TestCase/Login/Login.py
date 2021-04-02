import unittest
from selenium import webdriver
import time
from datetime import datetime
import xlsxwriter

from TopAsia.src.pages.Browser import Browser
import TopAsia.src.pages.page as page
from TopAsia.src.pages.locators import *
from TopAsia.src.pages.UIObject import UiObject
from TopAsia.src.pages.utils import *


class LoginFlow(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.get_driver()
        self.driver.get(ge.DOMAIN)

    # TOP - Link url check
    def test_Login(self):
        self.no = 1
        self.TEST_RESULT = [['#', 'Case', 'Data Input','Expected Error/Page link', 'Actual Error/Page link', 'Status', 'Notes']]
        self.TEST_DATA_HEADER = []
        self.name = 'LOGIN FLOW FROM HOME PAGE'
        start = datetime.now()
        self.TEST_DATA_HEADER.append(['Start', str(start).split('.')[0]])
        base = page.BasePage(self.driver)  # Khai báo base page handler
        # Chờ để tất cả element ở trang load xong
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()  # Mở full màn hình đang test
        SIZE = base.get_size()

        # Variable Define
        MENU_CONG_GAME = UiObject(*MainMenuLocators.MENU_CONG_GAME)
        MENU_DANG_NHAP = UiObject(*MainMenuLocators.MENU_DANG_NHAP)
        MENU_USER_INFO_DROP = UiObject(*MainMenuLocators.MENU_USER_INFO_DROP)

        input_username = UiObject(*LoginLocators.input_username)
        input_password = UiObject(*LoginLocators.input_password)
        text_error_username = UiObject(*LoginLocators.text_error_username)
        text_error_password = UiObject(*LoginLocators.text_error_password)
        btn_show_password = UiObject(*LoginLocators.btn_show_password)
        btn_hide_password = UiObject(*LoginLocators.btn_hide_password)
        btn_login = UiObject(*LoginLocators.btn_login)
        btn_close = UiObject(*LoginLocators.btn_close)

        popup_error = UiObject(*LoginLocators.popup_error)
        popup_error_title = UiObject(*LoginLocators.popup_error_title)
        popup_error_content = UiObject(*LoginLocators.popup_error_content)
        popup_error_btn_confirm = UiObject(*LoginLocators.popup_error_btn_confirm)

        drop_logout = UiObject(*UserInfoLocator.drop_logout)

        TEST_DATA = [
            [1, 'Data validation', 'INVALID-C', input_username, text_error_username,
                'Không nhập tên đăng nhập', '', 'Vui lòng nhập tên đăng nhập'],
            [2, 'Data validation', 'INVALID', input_username, text_error_username,
                'Tên đăng nhập ít hơn 6 ký tự', 'abcde', 'Tên đăng nhập tối thiểu 6 ký tự'],
            [3, 'Data validation', 'VALID', input_username,
                text_error_username, 'Tên đăng nhập = 6 ký tự', 'abcdef', ''],
            [4, 'Data validation', 'INVALID', input_username, text_error_username,
                'Tên đăng nhập nhiều hơn 30 ký tự ', 'abcdefghijklnmopqrstuvwxyz', 'Tên đăng nhập tối đa 30 ký tự'],
            [5, 'Data validation', 'VALID', input_username, text_error_username,
                'Tên đăng nhập = 30 ký tự', 'abcdefghijklnmopqrstuvwxyz1234', ''],
            [6, 'Data validation', 'INVALID-MULTI', input_username, text_error_username, 'Tên đăng nhập với ký tự đặc biệt',
                '!@#$%^&*() ;:\'"`~>.<,{}[]\/-=+', 'Vui lòng nhập tên đăng nhập không chứa ký tự đặc biệt'],
            [7, 'Data validation', 'INVALID-C', input_password, text_error_password,
                'Không nhập mật khẩu', '', 'Vui lòng nhập mật khẩu'],
            [8, 'Data validation', 'INVALID', input_password, text_error_password,
                'Mật khẩu ít hơn 6 ký tự', 'mnbvc', 'Mật khẩu tối thiểu 6 ký tự'],
            [9, 'Data validation', 'VALID', input_password,
                text_error_password, 'Mật khẩu = 6 ký tự', 'mnbvcx', ''],
            [10, 'Data validation', 'INVALID', input_password, text_error_password,
                'Mật khẩu nhiều hơn 12 ký tự ', 'sadfghjklqwer', 'Mật khẩu tối đa 12 ký tự'],
            [11, 'Data validation', 'VALID', input_password,
                text_error_password, 'Mật khẩu = 12 ký tự', 'sadfghjklqwe', ''],
            [12, 'Data validation', 'INVALID-P', input_username, input_password,
                'Nhập sai tên đăng nhập', '', 'Sai tên đăng nhập hoặc mật khẩu'],
            [13, 'Data validation', 'INVALID-P', input_username, input_password,
                'Nhập sai mật khẩu', '', 'Sai tên đăng nhập hoặc mật khẩu'],
            [14, 'Show/Hide pw', 'SHOW', input_password, btn_show_password,
                'Click show/hide password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '', ''],
            [15, 'Show/Hide pw', 'HIDE', input_password, btn_hide_password,
                'Click show/hide password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '', ''],
            [15, 'Navigation', '0', input_username, input_password, 'Nếu ví chính = 0, chuyển đến trang nạp tiền', [
                'tuananhle2603', '123456'], 'http://dev-ta.mooo.com/account/deposit'],
            [16, 'Navigation', '1', input_username, input_password, 'Nếu ví chính > 0, trở lại trang trước khi đăng nhập', [
                'tuananhle2603', '123456'], 'http://dev-ta.mooo.com/cong-game'],
            # [17,'Session','SESSION','Đăng nhập ở 1 trình duyệt khác sẽ log out ở trình duyệt cũ','','',]
        ]

        # COMPARE LINK AND RETURN DATA LIST
        if MENU_DANG_NHAP.visible():
            MENU_DANG_NHAP.click()
            self.driver.implicitly_wait(30)
            time.sleep(10)
            btn_login.click()
            time.sleep(3)
            self.driver.implicitly_wait(30)
            temp_rp = Report_temp(
                self.name.upper(), self.TEST_RESULT, self.TEST_DATA_HEADER)
            # CHECK DEFAULT CASE
            for i in TEST_DATA:
                actual = ''
                sts = ''
                notes = ''
                if i[1] == 'Data validation':
                    if 'INVALID' in i[2]:
                        if i[2] == 'INVALID-MULTI':
                            self.TEST_RESULT.append(
                                [i[0], i[5], i[6], '-', '-', '-', '-'])
                            for c in range(len(i[6])):
                                data_input = 'validdata'+i[6][c]
                                i[3].set_text(data_input)
                                time.sleep(1)
                                if i[4].visible():
                                    actual = i[4].get_text()
                                    if actual == i[7]:
                                        sts = 'PASSED'
                                    else:
                                        sts = 'FAILED'
                                        notes = 'Hiển thị lỗi không chính xác'
                                        base.screenshot_window(
                                            str(i[0])+'_'+str(c+1)+'_Error text is wrong', self.name)
                                else:
                                    sts = 'FAILED'
                                    notes = 'Không hiển thị lỗi khi nhập ' + \
                                        i[6][c]
                                    base.screenshot_window(
                                        str(i[0])+'_'+str(c+1)+'_Error text is not display', self.name)
                                self.TEST_RESULT.append(
                                    [str(i[0])+'-'+str(c+1), i[5], data_input, i[7], actual, sts, notes])
                        elif '-P' in i[2]:
                            if i[0] == 12:
                                username = 'khongtontai'
                                password = '123456'
                            elif i[0] == 12:
                                username = 'tuananhle2203'
                                password = 'khongdung'
                            data_input = 'Username: ' + username+', Password: ' + password
                            i[3].set_text(username)
                            i[4].set_text(password)
                            btn_login.click()
                            time.sleep(3)
                            if popup_error.visible():
                                actual = popup_error_content.get_text()
                                if actual == i[7]:
                                    sts = 'PASSED'
                                else:
                                    sts = 'FAILED'
                                    notes = 'Hiển thị lỗi không chính xác'
                                    base.screenshot_window(
                                        str(i[0])+'_Error popup is wrong', self.name)
                                notes = notes + '\nTITLE: '+popup_error_title.get_text()
                                notes = notes + '\nCONTENT: '+popup_error_content.get_text()
                                popup_error_btn_confirm.click()

                            else:
                                actual = '-'
                                sts = 'FAILED'
                                notes = 'Popup error không hiện'
                                base.screenshot_window(
                                    str(i[0])+'_Error popup not display', self.name)
                            self.TEST_RESULT.append(
                                [i[0], i[5], data_input, i[7], actual, sts, notes])
                        else:
                            i[3].set_text(i[6])
                            time.sleep(1)
                            if i[4].visible():
                                actual = i[4].get_text()
                                if actual == i[7]:
                                    sts = 'PASSED'
                                else:
                                    sts = 'FAILED'
                                    notes = 'Hiển thị lỗi không chính xác'
                                    base.screenshot_window(
                                        str(i[0])+'_Error text is wrong', self.name)
                            else:
                                sts = 'FAILED'
                                notes = 'Không hiển thị lỗi'
                                base.screenshot_window(
                                    str(i[0])+'_Error text is not display', self.name)
                            self.TEST_RESULT.append(
                                [i[0], i[5], i[6], i[7], actual, sts, notes])
                    elif i[2] == 'VALID':
                        i[3].set_text(i[6])
                        time.sleep(1)
                        if i[4].visible():
                            actual = i[4].get_text()
                            sts = 'FAILED'
                            notes = 'Hiển thị lỗi khi nhập đúng'
                            base.screenshot_window(
                                str(i[0])+'_Error text is display', self.name)
                        else:
                            sts = 'PASSED'
                        self.TEST_RESULT.append(
                            [i[0], i[5], i[6], i[7], actual, sts, notes])

                elif i[1] == 'Show/Hide pw':
                    text_input = 'SHOW PASS'
                    type_hidden = 'password'
                    type_shown = 'text'
                    if i[2] == 'SHOW':
                        i[3].set_text(text_input)
                        if btn_show_password.visible():
                            btn_show_password.click()
                            actual = input_password.get_attribute('type')
                            if actual == type_shown:
                                sts = 'PASSED'
                            else:
                                base.screenshot_window(
                                    str(i[0])+'_ The show password display wrong', self.name)
                                sts = 'FAILED'
                            notes = 'INPUT: ' + text_input + '\nType: ' + actual
                        else:
                            btn_hide_password.click()
                            btn_show_password.click()
                            actual = input_password.get_attribute('type')
                            if actual == type_shown:
                                sts = 'PASSED'
                            else:
                                base.screenshot_window(
                                    str(i[0])+'_ The show password display wrong', self.name)
                                sts = 'FAILED'
                            notes = 'INPUT: ' + text_input + '\nType: ' + actual
                        self.TEST_RESULT.append(
                            [i[0], i[5], text_input, type_shown, actual, sts, notes])
                    else:
                        i[3].set_text(text_input)
                        if btn_hide_password.visible():
                            btn_hide_password.click()
                            actual = input_password.get_attribute('type')
                            if actual == type_hidden:
                                sts = 'PASSED'
                            else:
                                base.screenshot_window(
                                    str(i[0])+'_ The show password display wrong', self.name)
                                sts = 'FAILED'
                            notes = 'INPUT: ' + text_input + '\nType: ' + actual
                        else:
                            btn_show_password.click()
                            btn_hide_password.click()
                            actual = input_password.get_attribute('type')
                            if actual == type_hidden:
                                sts = 'PASSED'
                            else:
                                base.screenshot_window(
                                    str(i[0])+'_ The show password display wrong', self.name)
                                sts = 'FAILED'
                            notes = 'INPUT: ' + text_input + '\nType: ' + actual
                        self.TEST_RESULT.append(
                            [i[0], i[5], text_input, type_hidden, actual, sts, notes])

                elif i[1] == 'Navigation':
                    if i[2] == '0':
                        if input_username.visible() == False:
                            MENU_DANG_NHAP.click()
                            time.sleep(3)

                    if i[2] == "1":
                        if input_username.visible() == False:
                            MENU_CONG_GAME.click()
                            time.sleep(3)
                            MENU_DANG_NHAP.click()
                            time.sleep(3)
                        else:
                            btn_close.click()
                            MENU_CONG_GAME.click()
                            time.sleep(3)
                            MENU_DANG_NHAP.click()
                            time.sleep(3)
                    i[3].set_text(i[6][0])
                    i[4].set_text(i[6][1])
                    time.sleep(3)
                    btn_login.click()
                    if MENU_USER_INFO_DROP.visible():
                        actual = base.get_url()
                        if actual == i[7]:
                            sts = 'PASSED'
                        else:
                            sts = 'FAILED'
                            notes = 'Login successful but link wrong'
                            base.screenshot_window(
                                str(i[0])+'_Login successful but link wrong', self.name)
                        MENU_USER_INFO_DROP.click()
                        drop_logout.click()
                    else:
                        sts = 'FAILED'
                        notes = 'Login un-successful'
                        base.screenshot_window(
                            str(i[0])+'_Login un-successful', self.name)
                    self.TEST_RESULT.append(
                        [i[0], i[5], i[6][0]+', '+i[6][1], i[7], actual, sts, notes])

                print('\n', '-'*15, ' Case: ',
                      str(i[0]), ': ', i[5], ' ', 15*'-')
                print('Status: \t', sts)
                print('Expected: \t', i[7])
                print('Actual: \t', actual, '\n')
                temp_rp = Report_temp(
                    self.name.upper(), self.TEST_RESULT, self.TEST_DATA_HEADER)
                temp_rp.export()
                temp_rp.close()
                time.sleep(2)
                print('input_username.visible(): ', input_username.visible())
                print('input_password.visible(): ', input_password.visible())
                print('btn_login.visible(): ', btn_login.visible())

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
            base.screenshot_window('Test Checking url link: FAILED')
            # print('Login or Register button is not appear')
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
