# from Template.src.pages.locators import LoginLocators, MainMenuLocators
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


class LoginFlow(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.get_driver()
        self.driver.get(ge.DOMAIN)

    # TOP - Link url check
    def test_Login(self):
        self.no = 1
        self.TEST_RESULT = [['#', 'Case', 'Data Input',
                             'Expected Error/Page link', 'Actual Error/Page link', 'Status', 'Notes']]
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
        MENU_DANG_NHAP = UiObject(*MainMenuLocators.MENU_DANG_NHAP)

        input_username = UiObject(*LoginLocators.input_username)
        input_password = UiObject(*LoginLocators.input_password)
        text_error_username = UiObject(*LoginLocators.text_error_username)
        text_error_password = UiObject(*LoginLocators.text_error_password)
        btn_show_password = UiObject(*LoginLocators.btn_show_password)
        btn_hide_password = UiObject(*LoginLocators.btn_hide_password)
        btn_login = UiObject(*LoginLocators.btn_login)

        popup_error = UiObject(*LoginLocators.popup_error)
        popup_error_title = UiObject(*LoginLocators.popup_error_title)
        popup_error_content = UiObject(*LoginLocators.popup_error_content)
        popup_error_btn_confirm = UiObject(
            *LoginLocators.popup_error_btn_confirm)

        TEST_DATA = [
            [1, 'Data validation', 'INVALID-C', input_username, text_error_username,
                'Không nhập tên đăng nhập', '', 'Vui lòng nhập tên đăng nhập'],
            [2, 'Data validation', 'INVALID', input_username, text_error_username,
                'Tên đăng nhập ít hơn 6 ký tự', 'abcde', 'Tên đăng nhập tối thiểu 6 ký tự'],
            [3, 'Data validation', 'VALID', input_username,
                text_error_username, 'Tên đăng nhập = 6 ký tự', 'abcdef', ''],
            [4, 'Data validation', 'INVALID', input_username, text_error_username,
                'Tên đăng nhập nhiều hơn 30 ký tự ', 'abcde fghij klnmo pqrst uvwxy z', 'Tên đăng nhập tối đa 30 ký tự'],
            [5, 'Data validation', 'VALID', input_username, text_error_username,
                'Tên đăng nhập = 30 ký tự', 'abcde fghij klnmo pqrst uvwxyz', ''],
            [6, 'Data validation', 'INVALID-MULTI', input_username, text_error_username, 'Tên đăng nhập với ký tự đặc biệt',
                ['!','@','#','$','%','^','&','*','(',')',' ',';',':',"'",'"','`','~','>','.','<','{','}','[',']','\\',',','/','-','=','+'], 'Vui lòng nhập tên đăng nhập không chứa ký tự đặc biệt'],
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
            [13, 'Data validation', 'INVALID-P', btn_login, input_username,
                input_password, 'Nhập sai mật khẩu', '', 'Sai tên đăng nhập hoặc mật khẩu'],
            # [14,'Hide pw','CLICK',btn_show_password, input_password,'Click show/hide password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi','',''],
            # [15,'Show pw','CLICK',btn_hide_password, input_password,'Click show/hide password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi','',''],
            # [15,'Navigation','NAVIGATE-0', btn_login,'-','Nếu ví chính = 0, chuyển đến trang nạp tiền','',''],
            # [16,'Navigation','NAVIGATE-1', btn_login,'-','Nếu ví chính > 0, trở lại trang trước khi đăng nhập','',''],
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
                    print(i[0])
                    print(i[1])
                    print(i[2])
                    print(i[3])
                    print(i[4])
                    print(i[5])
                    print(i[6])
                    if 'INVALID' in i[2]:
                        if i[2] == 'INVALID-MULTI':
                            self.TEST_RESULT.append(
                                [i[0], i[5], i[6], '-', '-', '-', '-'])
                            for c in len(i[6]):
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
                            base.set_url(*ge.DOMAIN)
                            self.driver.implicitly_wait(30)
                            MENU_DANG_NHAP.click()
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
                            notes = 'Hiển thị lỗi không chính xác'                            
                        self.TEST_RESULT.append(
                            [i[0], i[5], i[6], i[7], actual, sts, notes])
                print('\n', '-'*15, ' Case: ',
                      str(i[0]), ': ', i[5], ' ', 15*'-')
                print('Status: \t', sts)
                print('Expected link: \t', i[7])
                print('Actual link: \t', actual, '\n')
                temp_rp = Report_temp(
                    self.name.upper(), self.TEST_RESULT, self.TEST_DATA_HEADER)
                temp_rp.export()
                temp_rp.close()
                print('input_username.visible(): ',input_username.visible())
                print('input_password.visible(): ',input_password.visible())
                if input_username.visible():
                    input_username.set_text('')
                if input_password.visible():
                    input_password.set_text('')

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
            lobby.screenshot_window('Test Checking url link: FAILED')
            # print('Login or Register button is not appear')
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
