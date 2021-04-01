# from Template.src.pages.locators import SignupLocators, MainMenuLocators
import unittest
from selenium import webdriver
import time
from datetime import datetime
import xlsxwriter
import re

from pages.Browser import Browser
import pages.page as page
from pages.locators import *
from pages.UIObject import UiObject
from pages.utils import *


class SignupFlow(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.get_driver()
        self.driver.get(ge.DOMAIN)

    # TOP - Link url check
    def test_Signup(self):
        self.no = 1
        self.TEST_RESULT = [['#', 'Case', 'Data Input',
                             'Expected Error/Page link', 'Actual Error/Page link', 'Status', 'Notes']]
        self.TEST_DATA_HEADER = []
        self.name = 'SIGN UP FLOW FROM HOME PAGE'
        start = datetime.now()
        self.TEST_DATA_HEADER.append(['Start', str(start).split('.')[0]])
        base = page.BasePage(self.driver)  # Khai báo base page handler
        # Chờ để tất cả element ở trang load xong
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()  # Mở full màn hình đang test
        SIZE = base.get_size()

        # Variable Define
        MENU_CONG_GAME = UiObject(*MainMenuLocators.MENU_CONG_GAME)
        MENU_DANG_KY = UiObject(*MainMenuLocators.MENU_DANG_KY)
        MENU_USER_INFO_DROP = UiObject(*MainMenuLocators.MENU_USER_INFO_DROP)

        username = UiObject(*SignupLocators.username)
        password = UiObject(*SignupLocators.password)
        re_password = UiObject(*SignupLocators.re_password)
        phoneno = UiObject(*SignupLocators.phoneno)
        username_error = UiObject(*SignupLocators.username_error)
        password_error = UiObject(*SignupLocators.password_error)
        re_password_error = UiObject(*SignupLocators.re_password_error)
        phoneno_error = UiObject(*SignupLocators.phoneno_error)
        show_pass = UiObject(*SignupLocators.show_pass)
        hide_pass = UiObject(*SignupLocators.hide_pass)
        show_repass = UiObject(*SignupLocators.show_repass)
        hide_repass = UiObject(*SignupLocators.hide_repass)
        btn_register = UiObject(*SignupLocators.btn_register)
        btn_close = UiObject(*SignupLocators.btn_close)
        btn_agree = UiObject(*SignupLocators.btn_agree)
        invite_code = UiObject(*SignupLocators.invite_code)

        popup_error = UiObject(*SignupLocators.popup_error)
        popup_error_title = UiObject(*SignupLocators.popup_error_title)
        popup_error_content = UiObject(*SignupLocators.popup_error_content)
        popup_error_btn_confirm = UiObject(
            *SignupLocators.popup_error_btn_confirm)

        drop_logout = UiObject(*UserInfoLocator.drop_logout)

        TEST_DATA = [
            [1, 'Data validation', 'INVALID', username, username_error,
                'Không nhập tên đăng nhập', '', 'Vui lòng nhập tên đăng nhập'],
            [2, 'Data validation', 'INVALID', username, username_error,
                'Tên đăng nhập ít hơn 6 ký tự', 'abcde', 'Tên đăng nhập tối thiểu 6 ký tự'],
            [3, 'Data validation', 'VALID', username, username_error,
                'Tên đăng nhập = 6 ký tự', 'abcdef', ''],
            [4, 'Data validation', 'INVALID', username, username_error, 'Tên đăng nhập nhiều hơn 29 ký tự ',
                'abcdefghijklnmopqrstuvwxyz1234', 'Tên đăng nhập tối đa 29 ký tự'],
            [5, 'Data validation', 'VALID', username, username_error,
                'Tên đăng nhập = 29 ký tự', 'abcdefghijklnmopqrstuvwxyz123', ''],
            [6, 'Data validation', 'INVALID-MULTI', username, username_error,
                'Tên đăng nhập với ký tự đặc biệt', '!@#$%^&*() ;:\'"`~>.<,{}[]\/-=+', 'Tên đăng nhập không chứa các ký tự đặc biệt'],
            [7, 'Data validation', 'INVALID', password, password_error,
                'Không nhập mật khẩu', '', 'Vui lòng nhập mật khẩu'],
            [8, 'Data validation', 'INVALID', password, password_error,
                'Mật khẩu ít hơn 6 ký tự', 'mnbvc', 'Mật khẩu tối thiểu 6 ký tự'],
            [9, 'Data validation', 'VALID', password,
                password_error, 'Mật khẩu = 6 ký tự', 'mnbvcx', ''],
            [10, 'Data validation', 'INVALID', password, password_error,
                'Mật khẩu nhiều hơn 12 ký tự ', 'sadfghjklqwer', 'Mật khẩu tối đa 12 ký tự'],
            [11, 'Data validation', 'VALID', password, password_error,
                'Mật khẩu = 12 ký tự', 'sadfghjklqwe', ''],
            [12, 'Data validation', 'INVALID-P', password, password_error,
                'Tài khoản đã tồn tại', '-', 'Tài khoản đã tồn tại'],
            [13, 'Data validation', 'INVALID', re_password, re_password_error,
                'Mật khẩu nhập lại không trùng khớp', 'khongtrung', 'Mật khẩu nhập lại không trùng khớp'],
            [14, 'Data validation', 'VALID', re_password, re_password_error,
                'Mật khẩu nhập lại trùng khớp', '123456', ''],
            [15, 'Data validation', 'INVALID', phoneno,
                phoneno_error, 'Không nhập số điện thoại', '', 'Vui lòng nhập số điện thoại'],
            [16, 'Data validation', 'INVALID', phoneno, phoneno_error, 'Số điện thoại ít hơn 10 ký tự',
                '123456789', 'Số điện thoại yêu cầu tối thiểu 10 ký tự'],
            [17, 'Data validation', 'VALID', phoneno, phoneno_error,
                'Số điện thoại nhiều hơn 11 ký tự', '123456789145', ''],
            [18, 'Data validation', 'VALID', phoneno, phoneno_error,
                'Số điện thoại có 10 ký tự', '1234567890', ''],
            [19, 'Data validation', 'VALID', phoneno, phoneno_error,
                'Số điện thoại có 11 ký tự', '12345678901', ''],
            [20, 'Data validation', 'INVALID', phoneno, phoneno_error, 'Nhập chữ ở trường số điện thoại',
                '12345abcdef', 'Số điện thoại yêu cầu tối thiểu 10 ký tự'],
            [21, 'Data validation', 'VALID', phoneno, phoneno_error,
                'Nhập chữ ở trường số điện thoại', '0935770998haha', ''],
            [22, 'Navigation', '0', username, password,
                'Đăng ký khi uncheck Tôi đồng ý...', [
                    'tuananhle_', '123456'], 'http://dev-ta.mooo.com'],
            [23, 'Navigation', '1', username, password, 'Đăng ký khi check Tôi đồng ý... Chuyển đến trang nạp tiền nếu đăng nhập thành công', [
                'tuananhle_', '123456'], 'http://dev-ta.mooo.com/account/deposit'],
            [24, 'Show/Hide pw', 'SHOW', password, show_pass,
                'Click show/hide password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '-', '-'],
            [25, 'Show/Hide pw', 'HIDE', password, hide_pass,
                'Click show/hide password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '-', '-'],
            [26, 'Show/Hide pw', 'SHOW', password, show_repass,
                'Click show/hide nhập lại password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '-', '-'],
            [27, 'Show/Hide pw', 'HIDE', password, hide_repass,
                'Click show/hide nhập lại password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '-', '-'],
            [28, 'Helptext', 'TEXT', username, None,
                'Tên đăng nhập', '', 'Tên đăng nhập'],
            [29, 'Helptext', 'TEXT', password, None, 'Mật khẩu', '', 'Mật khẩu'],
            [30, 'Helptext', 'TEXT', re_password, None,
                'Nhập lại mật khẩu', '', 'Nhập lại mật khẩu'],
            [31, 'Helptext', 'TEXT', phoneno, None,
                'Số điện thoại', '', 'Số điện thoại'],
            [32, 'Helptext', 'TEXT', invite_code, None,
                'Mã giới thiệu (Nếu có)', '', 'Mã giới thiệu (Nếu có)'],
        ]

        # COMPARE LINK AND RETURN DATA LIST
        if MENU_DANG_KY.visible():
            MENU_DANG_KY.click()
            self.driver.implicitly_wait(30)
            time.sleep(10)
            btn_register.click()
            time.sleep(3)
            self.driver.implicitly_wait(30)
            temp_rp = Report_temp(
                self.name.upper(), self.TEST_RESULT, self.TEST_DATA_HEADER)
            # CHECK DEFAULT CASE
            for i in TEST_DATA:
                print('\n', '-'*15, ' Case: ',
                      str(i[0]), ': ', i[5], ' ', 15*'-')
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
                            if i[5] == 'Tên đăng nhập đã tồn tại':
                                username_ = 'tuananhle2203'
                                password_ = '123456'

                                data_input = 'Username: ' + username_+', Password: ' + password_
                                username.set_text(username_)
                                password.set_text(password_)
                                re_password.set_text(password_)
                                phoneno.set_text('0935770998')
                                # time.sleep(2)
                                btn_agree.click()
                                btn_register.click()
                                time.sleep(3)
                                print('hereeeee')
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
                    if username.visible() == False:
                        MENU_DANG_KY.click()
                        time.sleep(3)
                    text_input = 'SHOW PASS'
                    type_hidden = 'password'
                    type_shown = 'text'
                    if i[2] == 'SHOW':
                        i[3].set_text(text_input)
                        if show_pass.visible():
                            show_pass.click()
                            actual = password.get_attribute('type')
                            if actual == type_shown:
                                sts = 'PASSED'
                            else:
                                base.screenshot_window(
                                    str(i[0])+'_ The show password display wrong', self.name)
                                sts = 'FAILED'
                            notes = 'INPUT: ' + text_input + '\nType: ' + actual
                        else:
                            hide_pass.click()
                            show_pass.click()
                            actual = password.get_attribute('type')
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
                        if hide_pass.visible():
                            hide_pass.click()
                            actual = password.get_attribute('type')
                            if actual == type_hidden:
                                sts = 'PASSED'
                            else:
                                base.screenshot_window(
                                    str(i[0])+'_ The show password display wrong', self.name)
                                sts = 'FAILED'
                            notes = 'INPUT: ' + text_input + '\nType: ' + actual
                        else:
                            show_pass.click()
                            hide_pass.click()
                            actual = password.get_attribute('type')
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
                    if username.visible() == False:
                        MENU_DANG_KY.click()
                        time.sleep(3)
                    else:
                        btn_close.click()
                        MENU_DANG_KY.click()
                        time.sleep(3)
                    now = re.sub(
                        '[ :-]', '', str(datetime.now()).split('.')[0])
                    username.set_text(i[6][0] + now)
                    password.set_text(i[6][0])
                    re_password.set_text(i[6][0])
                    phoneno.set_text('0935770998')
                    # time.sleep(2)
                    if i[2] == '0':
                        btn_register.click()
                        if btn_register.visible():
                            actual = base.get_url()
                            if actual == i[7]:
                                sts = 'PASSED'
                            else:
                                sts = 'FAILED'
                                notes = 'Link is wrong'
                                base.screenshot_window(
                                    str(i[0])+'_Link is wrong', self.name)
                        else:
                            sts = 'FAILED'
                            notes = 'Do not stand on register when register without tick "Tôi đồng ý ..."'
                            base.screenshot_window(
                                str(i[0])+'_Do not stand on register', self.name)
                    else:
                        btn_agree.click()
                        btn_register.click()
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
                        [i[0], i[5], i[6][0]+now+', '+i[6][1], i[7], actual, sts, notes])

                elif i[1] == 'Helptext':
                    if username.visible() == False:
                        MENU_DANG_KY.click()
                        time.sleep(3)
                    actual = i[3].get_attribute('placeholder')
                    if actual == i[7]:
                        sts = 'PASSED'
                    else:
                        sts = 'FAILED'
                        base.screenshot_window(
                                    str(i[0])+'_ The show password display wrong', self.name)
                    self.TEST_RESULT.append(
                            [i[0], i[5], '-', i[7], actual, sts, notes])

                    pass
                print('Status: \t', sts)
                print('Expected: \t', i[7])
                print('Actual: \t', actual, '\n')
                temp_rp = Report_temp(
                    self.name.upper(), self.TEST_RESULT, self.TEST_DATA_HEADER)
                temp_rp.export()
                temp_rp.close()
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
            base.screenshot_window('Test Checking url link: FAILED')
            # print('Login or Register button is not appear')
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
