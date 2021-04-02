import unittest
from selenium import webdriver
import time
from datetime import datetime
import xlsxwriter
import re

from TopAsia.src.pages.Browser import Browser
import TopAsia.src.pages.page as page
from TopAsia.src.pages.locators import *
from TopAsia.src.pages.UIObject import UiObject
from TopAsia.src.pages.utils import *


class UpdateUserInformation(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.get_driver()
        self.driver.get(ge.DOMAIN)

    # TOP - Link url check
    def test_Update_User_Information(self):
        self.now = ''
        self.no = 1
        self.infopage = 'http://dev-ta.mooo.com/account/infomation'
        self.TEST_RESULT = [['#', 'Case', 'Data Input',
                             'Expected Error/Page link', 'Actual Error/Page link', 'Status', 'Notes']]
        self.TEST_DATA_HEADER = []
        self.name = 'CHANGE USER INFO FLOW'
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
        MENU_DANG_NHAP = UiObject(*MainMenuLocators.MENU_DANG_NHAP)
        MENU_USER_INFO_DROP = UiObject(*MainMenuLocators.MENU_USER_INFO_DROP)

        input_username = UiObject(*LoginLocators.input_username)
        input_password = UiObject(*LoginLocators.input_password)
        btn_login = UiObject(*LoginLocators.btn_login)

        username = UiObject(*SignupLocators.username)
        password = UiObject(*SignupLocators.password)
        re_password = UiObject(*SignupLocators.re_password)
        phoneno = UiObject(*SignupLocators.phoneno)
        btn_agree = UiObject(*SignupLocators.btn_agree)
        btn_register = UiObject(*SignupLocators.btn_register)

        info_name = UiObject(*UserInfoLocator.info_name)
        info_email = UiObject(*UserInfoLocator.info_email)
        info_phone = UiObject(*UserInfoLocator.info_phone)

        info_name_error = UiObject(*UserInfoLocator.info_name_error)
        info_email_error = UiObject(*UserInfoLocator.info_email_error)
        info_email_authen = UiObject(*UserInfoLocator.info_email_authen)
        info_phone_authen = UiObject(*UserInfoLocator.info_phone_authen)
        info_confirm = UiObject(*UserInfoLocator.info_confirm)
        popup_cf = UiObject(*UserInfoLocator.popup_cf)

        drop_logout = UiObject(*UserInfoLocator.drop_logout)
        drop_username = UiObject(*UserInfoLocator.drop_username)
        txt_username = UiObject(*UserInfoLocator.txt_username)

        TEST_DATA = [
            [1, 'Data validation', 'INVALID', info_name, info_name_error,
                'Không nhập họ và tên', '', 'Vui lòng nhập họ và tên'],
            [2, 'Data validation', 'INVALID', info_name, info_name_error,
                'Nhập họ và tên ít hơn 6 ký tự', 'abcde', 'Họ và tên tối thiểu 6 ký tự'],
            [3, 'Data validation', 'VALID', info_name, info_name_error,
                'Nhập họ và tên = 6 ký tự', 'abcdef', ''],
            [4, 'Data validation', 'INVALID', info_name, info_name_error, 'Họ và tên nhiều hơn 29 ký tự ',
                'abcdefghijklnmopqrstuvwxyz1234', 'Họ và tên ít hơn 30 ký tự'],
            [5, 'Data validation', 'VALID', info_name, info_name_error,
                'Họ và tên = 29 ký tự', 'abcdefghijklnmopqrstuvwxyz123', ''],
            [6, 'Data validation', 'VALID-MULTI', info_name, info_name_error,
                'Họ và tên với ký tự đặc biệt', ['!@#$%^&*() ;:\'"`', '~>.<,{}[]\/-=+'], ''],
            [7, 'Clickable', '0', info_email, info_email_authen,
                'Không nhập email', '', ''],
            [8, 'Data validation', 'VALID', info_email,
                info_email_error, 'Không nhập email', '', ''],
            [9, 'Data validation', 'INVALID-MULTI', info_email, info_email_error, 'Nhập email chứa ký tự đặc biệt',
                '!@#$%^&*() ;:\'"`~>.<,{}[]\/-=+ấáđêế', 'Địa chỉ email không hợp lệ'],
            [10, 'Data validation', 'VALID', info_email, info_email_error,
                'Nhập email hợp lệ', '', ''],
            [11, 'Data validation', 'INVALID-F', info_email, info_email_error, 'Nhập email không đúng format',
                ['anh.le', '@', 'hikosolution', '.com'], 'Địa chỉ email không hợp lệ'],
            [12, 'Clickable', '1', info_email, info_email_authen,
                'Nhập email hợp lệ', '', ''],
            [13, 'Clickable', '1-P', info_email, info_email_authen,
                'Click xác thực email bật pop Xác thực email', '', ''],
            [14, 'Clickable', '1-P', info_phone, info_phone_authen,
                'Click xác thực email bật pop Xác thực số điện thoại', '', ''],
            [15, 'Helptext', 'TEXT', info_name, None,
                'Họ và Tên', '', 'Nhập họ và tên'],
            [16, 'Helptext', 'TEXT', info_email, None,
                'Email', '', 'Nhập email của bạn'],
            [17, 'Function', 'NAMECHANGE', info_name, info_confirm,
                'Đổi Họ tên thành công sẽ hiển thị trên Menu', 'Lê Tuấn Anh', 'Nhập lại mật khẩu'],
        ]

        # COMPARE LINK AND RETURN DATA LIST
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
            info_confirm.click()
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
                                data_input = 'anh.letuan' + \
                                    str(i[6][c])+'@hikosolution.com'
                                print('\n', '-'*15, ' Case: ',
                                      data_input, ': ', i[5], ' ', 15*'-')
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

                        elif '-F' in i[2]:
                            self.TEST_RESULT.append(
                                [i[0], i[5], "-", '-', '-', '-', '-'])
                            for st in range(len(i[6])):
                                tem = [i for i in i[6]]
                                tem.pop(st)
                                email_ = ''
                                for e in tem:
                                    email_ += e
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
                                            str(i[0])+'_Error text is wrong', self.name)
                                else:
                                    sts = 'FAILED'
                                    notes = 'Không hiển thị lỗi'
                                    base.screenshot_window(
                                        str(i[0])+'_Error text is not display', self.name)
                                self.TEST_RESULT.append(
                                    [str(i[0])+'-'+str(st+1), 'Thiếu ' + i[6][st], data_input, i[7], actual, sts, notes])
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
                    elif 'VALID' in i[2]:
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
                                    base.screenshot_window(
                                        str(i[0])+'_'+str(c+1)+' Hiển thị lỗi khi nhập tên', self.name)
                                else:
                                    sts = 'PASSED'
                                self.TEST_RESULT.append(
                                    [str(i[0])+'-'+str(c+1), i[5], data_input, str(i[6][c]), actual, sts, notes])
                        
                        else:
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
                elif i[1] == 'Clickable':
                    email = 'hiko'+self.now+'@hikosolution.com'
                    if i[2] == '0':
                        i[3].set_text(email)
                        if i[3].clickable():
                            sts = 'FAILED'
                            notes = 'Có thể click khi chưa nhập email'
                        else:
                            sts = 'PASSED'
                        self.TEST_RESULT.append(
                            [i[0], i[5], i[6], '', actual, sts, notes])
                    elif '1' in i[2]:
                        if i[2] == '1':
                            i[3].set_text(email)
                            if i[3].clickable():
                                sts = 'PASSED'
                            else:
                                sts = 'FAILED'
                                notes = 'Không thể click khi nhập email'
                            self.TEST_RESULT.append(
                                [i[0], i[5], i[6], '', actual, sts, notes])
                        else:
                            if i[0] == 13:
                                i[3].set_text(email)
                            if i[4].clickable():
                                i[4].click()
                                if popup_cf.visible():
                                    sts = 'PASSED'
                                else:
                                    sts = 'FAILED'
                                    notes = 'Không hiển thị popup khi click Xác nhận email'
                            else:
                                sts = 'FAILED'
                                notes = 'Không thể click để hiển thị popup khi điền email đúng format'
                            self.TEST_RESULT.append(
                                [i[0], i[5], i[6], '', actual, sts, notes])

                elif i[1] == 'Helptext':
                    if drop_username.visible() == False:
                        MENU_DANG_NHAP.click()
                        input_username.set_text('tuananhle'+self.now)
                        input_password.set_text('123456')
                        btn_login.click
                        base.set_url(self.infopage)
                        time.sleep(2)

                    actual = i[3].get_attribute('placeholder')
                    if actual == i[7]:
                        sts = 'PASSED'
                    else:
                        sts = 'FAILED'
                        base.screenshot_window(
                            str(i[0])+'_ The show info_email display wrong', self.name)
                    self.TEST_RESULT.append(
                        [i[0], i[5], '-', i[7], actual, sts, notes])

                elif i[1] == 'Function':
                    if i[2] == 'NAMECHANGE':
                        nametochange = i[6]+self.now
                        info_name.set_text(nametochange)
                        info_confirm.click()
                        time.sleep(3)
                        name1 = txt_username.get_text()
                        name2 = drop_username.get_text()
                        actual = name2 + ', '+name1
                        if name1 == nametochange.upper() and name2 == nametochange.upper():
                            sts = 'PASSED'
                        else:
                            sts = 'FAILED'
                            notes = actual
                            base.screenshot_window(
                            str(i[0])+'_ The name display is wrong', self.name)
                        self.TEST_RESULT.append(
                        [i[0], i[5], nametochange, '-', actual, sts, notes])
                    pass

                print('Status: \t', sts)
                print('Expected: \t', i[7])
                print('Actual: \t', actual, '\n')
                # print(self.TEST_RESULT)
                # print(self.TEST_DATA_HEADER)
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
