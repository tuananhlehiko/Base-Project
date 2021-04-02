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


class ChangePasswordFlow(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.get_driver()
        self.driver.get(ge.DOMAIN)

    def test_ChangePasswordFlow(self):
        self.now = ''
        self.no = 1
        self.infopage = 'http://dev-ta.mooo.com/account/infomation'
        self.TEST_RESULT = [['#', 'Case', 'Data Input', 'Expected Error/Page link', 'Actual Error/Page link', 'Status', 'Notes']]
        self.TEST_DATA_HEADER = []
        self.name = 'CHANGE USER PASSWORD'

        start = datetime.now()
        self.TEST_DATA_HEADER.append(['Start', str(start).split('.')[0]])
        base = page.BasePage(self.driver)  # Khai báo base page handler
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()  # Mở full màn hình đang test
        SIZE = base.get_size()

        # Variable Define
        MENU_DANG_KY = UiObject(*MainMenuLocators.MENU_DANG_KY)
        MENU_USER_INFO_DROP = UiObject(*MainMenuLocators.MENU_USER_INFO_DROP)

        # USER INFO LOCATOR
        tab_changepass = UiObject(*UserInfoLocator.tab_changepass)
        chg_cur_pass = UiObject(*UserInfoLocator.chg_cur_pass)
        chg_cur_pass_error = UiObject(*UserInfoLocator.chg_cur_pass_error)
        chg_new_pass = UiObject(*UserInfoLocator.chg_new_pass)
        chg_new_pass_error = UiObject(*UserInfoLocator.chg_new_pass_error)
        chg_re_new_pass = UiObject(*UserInfoLocator.chg_re_new_pass)
        chg_re_new_pass_error = UiObject(*UserInfoLocator.chg_re_new_pass_error)
        chg_confirm = UiObject(*UserInfoLocator.chg_confirm)

        popup_error = UiObject(*UserInfoLocator.popup_error)
        popup_error_content = UiObject(*UserInfoLocator.popup_error_content)
        popup_error_btn_confirm = UiObject(*UserInfoLocator.popup_error_btn_confirm)

        show_cur_pass = UiObject(*UserInfoLocator.show_cur_pass)
        hide_cur_pass = UiObject(*UserInfoLocator.hide_cur_pass)
        show_new_pass = UiObject(*UserInfoLocator.show_new_pass)
        hide_new_pass = UiObject(*UserInfoLocator.hide_new_pass)
        show_re_new_pass = UiObject(*UserInfoLocator.show_re_new_pass)
        hide_re_new_pass = UiObject(*UserInfoLocator.hide_re_new_pass)

        drop_logout = UiObject(*UserInfoLocator.drop_logout)
        drop_username = UiObject(*UserInfoLocator.drop_username)
        # txt_username = UiObject(*UserInfoLocator.txt_username)

        # input_username = UiObject(*LoginLocators.input_username)
        # input_password = UiObject(*LoginLocators.input_password)
        # btn_login = UiObject(*LoginLocators.btn_login)
        # SIGN-UP LOCATOR
        username = UiObject(*SignupLocators.username)
        password = UiObject(*SignupLocators.password)
        re_password = UiObject(*SignupLocators.re_password)
        phoneno = UiObject(*SignupLocators.phoneno)
        btn_agree = UiObject(*SignupLocators.btn_agree)
        btn_register = UiObject(*SignupLocators.btn_register)

        # DATA TEST
        TEST_DATA = [
            [1, 'Data validation', 'INVALID', chg_cur_pass, chg_cur_pass_error, 'Không nhập mật khẩu hiện tại', '', 'Vui lòng nhập mật khẩu hiện tại'],
            [2, 'Data validation', 'INVALID', chg_cur_pass, chg_cur_pass_error, 'Mật khẩu hiện tại ít hơn 6 ký tự', 'abcde', 'Mật khẩu hiện tại không hợp lệ, yêu cầu ít nhất 6 ký tự.'],
            [3, 'Data validation', 'VALID', chg_cur_pass, chg_cur_pass_error, 'Mật khẩu hiện tại = 6 ký tự', 'abcdef', ''],
            [4, 'Data validation', 'VALID', chg_cur_pass, chg_cur_pass_error, 'Mật khẩu hiện tại nhiều hơn 12 ký tự ', 'abcdefghiyz1234', ''],
            [5, 'Data validation', 'VALID', chg_cur_pass, chg_cur_pass_error, 'Mật khẩu hiện tại = 12 ký tự', 'abcdefghi123', ''],
            [6, 'Data validation', 'VALID-MULTI', chg_cur_pass, chg_cur_pass_error, 'Mật khẩu hiện tại với ký tự đặc biệt', ['!@#$%^&*', '() ;:\'"', '`~>.<,{}', '[]\/-=+'], ''],
            [7, 'Data validation', 'INVALID', chg_new_pass, chg_new_pass_error, 'Không nhập mật khẩu mới', '', 'Vui lòng nhập mật khẩu mới'],
            [8, 'Data validation', 'INVALID', chg_new_pass, chg_new_pass_error, 'Mật khẩu mới ít hơn 6 ký tự', 'abcde', 'Mật khẩu mới không hợp lệ, yêu cầu ít nhất 6 ký tự.'],
            [9, 'Data validation', 'VALID', chg_new_pass, chg_new_pass_error, 'Mật khẩu mới = 6 ký tự', 'abcdef', ''],
            [10, 'Data validation', 'VALID', chg_new_pass, chg_new_pass_error, 'Mật khẩu mới nhiều hơn 12 ký tự ', 'abcdefghiyz1234', ''],
            [11, 'Data validation', 'VALID', chg_new_pass, chg_new_pass_error, 'Mật khẩu mới = 12 ký tự', 'abcdefghi123', ''],
            [12, 'Data validation', 'VALID-MULTI', chg_new_pass, chg_new_pass_error, 'Mật khẩu mới với ký tự đặc biệt', ['!@#$%^&*', '() ;:\'"', '`~>.<,{}', '[]\/-=+'], ''],
            [13, 'Data validation', 'INVALID-DUP', chg_new_pass, chg_new_pass_error, 'Mật khẩu mới trùng với mật khẩu cũ', '123456', 'Vui lòng nhập mật khẩu không trùng với mật khẩu cũ'],
            [14, 'Data validation', 'VALID', chg_re_new_pass, chg_re_new_pass_error, 'Mật khẩu nhập lại trùng khớp', '123456', ''],
            [15, 'Data validation', '', chg_cur_pass, chg_new_pass, 'Mật khẩu hiện tại không đúng', '1234567', 'Mật khẩu hiện tại không đúng. Vui lòng thử lại'],
            [16, 'Show/Hide pw', 'SHOW', chg_cur_pass, [show_cur_pass, hide_cur_pass], 'Click show/hide password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '', ''],
            [17, 'Show/Hide pw', 'HIDE', chg_cur_pass, [hide_cur_pass, show_cur_pass], 'Click show/hide password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '', ''],
            [18, 'Show/Hide pw', 'SHOW', chg_new_pass, [show_new_pass, hide_new_pass], 'Click show/hide nhập lại password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '', ''],
            [19, 'Show/Hide pw', 'HIDE', chg_new_pass, [hide_new_pass, show_new_pass], 'Click show/hide nhập lại password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '', ''],
            [20, 'Show/Hide pw', 'SHOW', chg_re_new_pass, [show_re_new_pass, hide_re_new_pass], 'Click show/hide nhập lại password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '', ''],
            [21, 'Show/Hide pw', 'HIDE', chg_re_new_pass, [hide_re_new_pass, show_re_new_pass], 'Click show/hide nhập lại password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '', ''],
            [22, 'Helptext', 'TEXT', chg_cur_pass, None, 'Nhập mật khẩu hiện tại', '', 'Nhập mật khẩu hiện tại'],
            [23, 'Helptext', 'TEXT', chg_new_pass, None, 'Nhập mật khẩu mới', '', 'Nhập mật khẩu mới'],
            [24, 'Helptext', 'TEXT', chg_re_new_pass, None, 'Nhập lại mật khẩu mới', '', 'Nhập lại mật khẩu mới'],
        ]

        # RUNNING TEST
        if MENU_DANG_KY.visible():
            MENU_DANG_KY.click()
            self.driver.implicitly_wait(30)
            time.sleep(5)
            self.now = re.sub('[ :-]', '', str(datetime.now()).split('.')[0])
            username.set_text('tuananhle' + self.now)
            password.set_text('123456')
            re_password.set_text('123456')
            phoneno.set_text('0935770998')
            btn_agree.click()
            btn_register.click()
            time.sleep(2)
            self.TEST_DATA_HEADER.append(
                ['Account Test', 'Username: ' + 'tuananhle' + self.now+', pass: 123456'])
        if drop_username.visible():
            base.set_url(self.infopage)
            time.sleep(3)
            tab_changepass.click()
            time.sleep(3)
            chg_confirm.click()
            self.driver.implicitly_wait(30)
            temp_rp = Report_temp(
                self.name.upper(), self.TEST_RESULT, self.TEST_DATA_HEADER)
            # CHECK DEFAULT CASE
            for i in TEST_DATA:
                print('\n', '-'*15, ' Case: ', str(i[0]), ': ', i[5], ' ', 15*'-')
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
                                        base.screenshot_window(str(i[0])+'_'+str(c+1)+'_Error text is wrong', self.name)
                                else:
                                    sts = 'FAILED'
                                    notes = 'Không hiển thị lỗi khi nhập ' + \
                                        i[6][c]
                                    base.screenshot_window(str(i[0])+'_'+str(c+1)+'_Error text is not display', self.name)
                                self.TEST_RESULT.append([str(i[0])+'-'+str(c+1), i[5], data_input, i[7], actual, sts, notes])
                        elif '-P' in i[2]:
                            if i[5] == 'Mật khẩu hiện tại không đúng':
                                oldpass_ = 'tuananhle2203'
                                newpass_ = '123456'

                                data_input = 'Oldpass: ' + oldpass_+', Password: ' + newpass_
                                chg_cur_pass.set_text(oldpass_)
                                chg_new_pass.set_text(newpass_)
                                chg_re_new_pass.set_text(newpass_)
                                # phoneno.set_text('0935770998')
                                # time.sleep(2)
                                chg_confirm.click()
                                # btn_register.click()
                                time.sleep(3)
                                print('hereeeee')
                                if popup_error.visible():
                                    actual = popup_error_content.get_text()
                                    if actual == i[7]:
                                        sts = 'PASSED'
                                    else:
                                        sts = 'FAILED'
                                        notes = 'Hiển thị lỗi không chính xác'
                                        base.screenshot_window(str(i[0])+'_Error popup is wrong', self.name)
                                    notes = notes + '\nTITLE: '+popup_error_title.get_text()
                                    notes = notes + '\nCONTENT: '+popup_error_content.get_text()
                                    popup_error_btn_confirm.click()

                                else:
                                    actual = '-'
                                    sts = 'FAILED'
                                    notes = 'Popup error không hiện'
                                    base.screenshot_window(str(i[0])+'_Error popup not display', self.name)
                                self.TEST_RESULT.append([i[0], i[5], data_input, i[7], actual, sts, notes])
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
                                    base.screenshot_window(str(i[0])+'_Error text is wrong', self.name)
                            else:
                                sts = 'FAILED'
                                notes = 'Không hiển thị lỗi'
                                base.screenshot_window(str(i[0])+'_Error text is not display', self.name)
                            self.TEST_RESULT.append([i[0], i[5], i[6], i[7], actual, sts, notes])
                    elif i[2] == 'VALID':
                        if i[2] == 'VALID-MULTI':
                            self.TEST_RESULT.append(
                                [i[0], i[5], '-', '-', '-', '-', '-'])
                            for c in range(len(i[6])):
                                data_input = str(i[6][c])
                                print('\n', '-'*15, ' Case: ',
                                      data_input, ': ', i[5], ' ', 15*'-')
                                i[3].set_text(data_input)
                                time.sleep(1)
                                if i[4].visible():
                                    actual = i[4].get_text()
                                    sts = 'FAILED'
                                    notes = 'Hiển thị lỗi khi nhập tên'
                                    base.screenshot_window(str(i[0])+'_'+str(c+1)+' Hiển thị lỗi khi nhập tên', self.name)
                                else:
                                    sts = 'PASSED'
                                self.TEST_RESULT.append([str(i[0])+'-'+str(c+1), i[5], data_input, str(i[6][c]), actual, sts, notes])
                        else:
                            i[3].set_text(i[6])
                            time.sleep(1)
                            if i[4].visible():
                                actual = i[4].get_text()
                                sts = 'FAILED'
                                notes = 'Hiển thị lỗi khi nhập đúng'
                                base.screenshot_window(str(i[0])+'_Error text is display', self.name)
                            else:
                                sts = 'PASSED'
                            self.TEST_RESULT.append([i[0], i[5], i[6], i[7], actual, sts, notes])

                elif i[1] == 'Show/Hide pw':
                    if chg_new_pass.visible() == False:
                        base.set_url(self.infopage)
                        tab_changepass.click
                        time.sleep(3)
                    text_input = 'SHOW PASS'
                    type_hidden = 'password'
                    type_shown = 'text'
                    if i[2] == 'SHOW':
                        i[3].set_text(text_input)
                        if i[4][0].visible():
                            i[4][0].click()
                            actual = password.get_attribute('type')
                            if actual == type_shown:
                                sts = 'PASSED'
                            else:
                                base.screenshot_window(str(i[0])+'_ The show password display wrong', self.name)
                                sts = 'FAILED'
                            notes = 'INPUT: ' + text_input + '\nType: ' + actual
                        else:
                            i[4][1].click()
                            i[4][0].click()
                            actual = password.get_attribute('type')
                            if actual == type_shown:
                                sts = 'PASSED'
                            else:
                                base.screenshot_window(str(i[0])+'_ The show password display wrong', self.name)
                                sts = 'FAILED'
                            notes = 'INPUT: ' + text_input + '\nType: ' + actual
                        self.TEST_RESULT.append([i[0], i[5], text_input, type_shown, actual, sts, notes])
                    else:
                        i[3].set_text(text_input)
                        if i[4][0].visible():
                            i[4][0].click()
                            actual = password.get_attribute('type')
                            if actual == type_hidden:
                                sts = 'PASSED'
                            else:
                                base.screenshot_window(str(i[0])+'_ The show password display wrong', self.name)
                                sts = 'FAILED'
                            notes = 'INPUT: ' + text_input + '\nType: ' + actual
                        else:
                            i[4][1].click()
                            i[4][0].click()
                            actual = password.get_attribute('type')
                            if actual == type_hidden:
                                sts = 'PASSED'
                            else:
                                base.screenshot_window(str(i[0])+'_ The show password display wrong', self.name)
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
                                base.screenshot_window(str(i[0])+'_Link is wrong', self.name)
                        else:
                            sts = 'FAILED'
                            notes = 'Do not stand on register when register without tick "Tôi đồng ý ..."'
                            base.screenshot_window(str(i[0])+'_Do not stand on register', self.name)
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
                                base.screenshot_window(str(i[0])+'_Login successful but link wrong', self.name)
                            MENU_USER_INFO_DROP.click()
                            drop_logout.click()
                        else:
                            sts = 'FAILED'
                            notes = 'Login un-successful'
                            base.screenshot_window(
                                str(i[0])+'_Login un-successful', self.name)
                    self.TEST_RESULT.append([i[0], i[5], i[6][0]+now+', '+i[6][1], i[7], actual, sts, notes])
                elif i[1] == 'Helptext':
                    if username.visible() == False:
                        MENU_DANG_KY.click()
                        time.sleep(3)
                    actual = i[3].get_attribute('placeholder')
                    if actual == i[7]:
                        sts = 'PASSED'
                    else:
                        sts = 'FAILED'
                        base.screenshot_window(str(i[0])+'_ The show password display wrong', self.name)
                    self.TEST_RESULT.append([i[0], i[5], '-', i[7], actual, sts, notes])

                    pass
                print('Status: \t', sts)
                print('Expected: \t', i[7])
                print('Actual: \t', actual, '\n')
                temp_rp = Report_temp(self.name.upper(), self.TEST_RESULT, self.TEST_DATA_HEADER)
                temp_rp.export()
                temp_rp.close()
                time.sleep(2)

            end = datetime.now()
            self.TEST_DATA_HEADER.append(['End', str(end).split('.')[0]])
            self.TEST_DATA_HEADER.append(['Time spend', str(end-start).split('.')[0]])
            self.TEST_DATA_HEADER.append(['Size', str(SIZE)])
            # REPORT data
            report = Report(self.name.upper(), self.TEST_RESULT, self.TEST_DATA_HEADER)
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
