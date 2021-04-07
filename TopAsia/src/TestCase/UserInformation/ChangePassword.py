from selenium import webdriver
import time, unittest, xlsxwriter, re
from datetime import datetime

from TopAsia.src.pages.Browser import Browser
from TopAsia.src.pages.page import *
from TopAsia.src.pages.locators import *
from TopAsia.src.pages.UIObject import UiObject
from TopAsia.src.pages.utils import *


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
        base = BasePage(self.driver)  # Khai báo base page handler
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()  # Mở full màn hình đang test
        SIZE = base.get_size()

        # Variable Define
        MENU_DANG_KY = UiObject(*MainMenuLocators.MENU_DANG_KY)

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

        drop_username = UiObject(*UserInfoLocator.drop_username)
        
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
            [10, 'Data validation', 'VALID', chg_new_pass, chg_new_pass_error, 'Mật khẩu mới nhiều hơn 12 ký tự ', 'abcdefhhiyz1234', ''],
            [11, 'Data validation', 'VALID', chg_new_pass, chg_new_pass_error, 'Mật khẩu mới = 12 ký tự', 'abcdefhhi123', ''],
            [12, 'Data validation', 'VALID-MULTI', chg_new_pass, chg_new_pass_error, 'Mật khẩu mới với ký tự đặc biệt', ['!@#$%^&*', '() ;:\'"', '`~>.<,{}', '[]\/-=+'], ''],
            [13, 'Data validation', 'INVALID-DUP', chg_new_pass, chg_new_pass_error, 'Mật khẩu mới trùng với mật khẩu cũ', '123456', 'Vui lòng nhập mật khẩu không trùng với mật khẩu cũ'],
            [14, 'Data validation', 'VALID', chg_re_new_pass, chg_re_new_pass_error, 'Mật khẩu nhập lại trùng khớp', '123456', ''],
            [15, 'Data validation', 'INVALID-P', [chg_cur_pass, chg_new_pass, chg_re_new_pass, chg_confirm], [popup_error, popup_error_content, popup_error_btn_confirm], 'Mật khẩu hiện tại không đúng', '1234567', 'Mật khẩu hiện tại không đúng. Vui lòng thử lại'],
            [16, 'Show/Hide pw', 'SHOW', chg_cur_pass, [show_cur_pass, hide_cur_pass], 'Click show/hide password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '', 'text'],
            [17, 'Show/Hide pw', 'HIDE', chg_cur_pass, [hide_cur_pass, show_cur_pass], 'Click show/hide password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '', 'password'],
            [18, 'Show/Hide pw', 'SHOW', chg_new_pass, [show_new_pass, hide_new_pass], 'Click show/hide nhập lại password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '', 'text'],
            [19, 'Show/Hide pw', 'HIDE', chg_new_pass, [hide_new_pass, show_new_pass], 'Click show/hide nhập lại password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '', 'password'],
            [20, 'Show/Hide pw', 'SHOW', chg_re_new_pass, [show_re_new_pass, hide_re_new_pass], 'Click show/hide nhập lại password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '', 'text'],
            [21, 'Show/Hide pw', 'HIDE', chg_re_new_pass, [hide_re_new_pass, show_re_new_pass], 'Click show/hide nhập lại password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '', 'password'],
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
            self.TEST_DATA_HEADER.append(['Account Test', 'Username: ' + 'tuananhle' + self.now+', pass: 123456'])
        if drop_username.visible():
            base.set_url(self.infopage)
            time.sleep(3)
            tab_changepass.click()
            time.sleep(3)
            chg_confirm.click()
            self.driver.implicitly_wait(30)
            Template_Report = Report_temp(self.name.upper(), self.TEST_RESULT, self.TEST_DATA_HEADER)
            for i in TEST_DATA:
                print('\n', '-'*15, ' Case: ', str(i[0]), ': ', i[5], ' ', 15*'-')                
                if chg_new_pass.visible() == False:
                    base.set_url(self.infopage)
                    tab_changepass.click
                    time.sleep(3)
                if i[1] == 'Data validation':
                    if 'INVALID' in i[2]:
                        if i[2] == 'INVALID-MULTI':
                            self.TEST_RESULT.append([i[0], i[5], '-', '-', '-', '-', '-'])
                        if i[2] == 'INVALID-DUP':
                            chg_cur_pass.set_text(i[6])                            
                        self.TEST_RESULT.append(ValidateData.CheckINVALIDCase(i,self.name))
                    elif i[2] == 'VALID':
                        if i[2] == 'VALID-MULTI':
                            self.TEST_RESULT.append([i[0], i[5], '-', '-', '-', '-', '-'])
                        self.TEST_RESULT.append(ValidateData.CheckVALIDCase(i,self.name))

                elif i[1] == 'Show/Hide pw':
                    self.TEST_RESULT.append(ValidateData.ShowHideButton(i, self.name, base))

                elif i[1] == 'Helptext':
                    self.TEST_RESULT.append(ValidateData.HelpTextCheck(i, self.name, base))
               
                Template_Report = Report_temp(self.name.upper(), self.TEST_RESULT, self.TEST_DATA_HEADER)
                Template_Report.export()
                Template_Report.close()
                time.sleep(1)

            end = datetime.now()
            self.TEST_DATA_HEADER.append(['End', str(end).split('.')[0]])
            self.TEST_DATA_HEADER.append(['Time spend', str(end-start).split('.')[0]])
            self.TEST_DATA_HEADER.append(['Size', str(SIZE)])
            # REPORT data
            report = Report(self.name.upper(), self.TEST_RESULT, self.TEST_DATA_HEADER)
            report.export()
            report.close()
        else:
            base.ScrShot('Test Checking url link: FAILED')
        self.driver.implicitly_wait(30)
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()