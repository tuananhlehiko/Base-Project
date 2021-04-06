from selenium import webdriver
import time
import unittest
import xlsxwriter
import re
import random
from datetime import datetime

from TopAsia.src.pages.Browser import Browser
from TopAsia.src.pages.page import *
from TopAsia.src.pages.locators import *
from TopAsia.src.pages.locators import RechargeLocators as rl
from TopAsia.src.pages.UIObject import UiObject
from TopAsia.src.pages.utils import *


class RechargeBanksFlow(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.get_driver()
        self.driver.get(ge.DOMAIN)

    def test_RechargeBankFlow(self):
        self.now = ''
        self.no = 1
        self.workingPage = 'http://dev-ta.mooo.com/account/deposit'
        self.TEST_RESULT = [['#', 'Case', 'Data Input', 'Expected Error/Page link', 'Actual Error/Page link', 'Status', 'Notes']]
        self.TEST_DATA_HEADER = []
        self.name = 'Recharge using Banks'

        start = datetime.now()
        self.TEST_DATA_HEADER.append(['Start', str(start).split('.')[0]])
        base = BasePage(self.driver)  # Khai báo base page handler
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()  # Mở full màn hình đang test
        SIZE = base.get_size()

        # DATA TEST
        TEST_DATA = [
            [1, 'Data validation', 'INVALID', rl.in_amount, rl.in_amount_error, 'Không nhập số tiền', '', 'Vui lòng nhập số tiền'],
            [2, 'Data validation', 'INVALID', rl.in_amount, rl.in_amount_error, 'Nhập tiền ít hơn 50K', '49', 'Số tiền nạp tối thiểu là 50 K'],
            [3, 'Data validation', 'VALID', rl.in_amount, rl.in_amount_error, 'Nhập tiền bằng 50K', '50', ''],
            [4, 'Data validation', 'INVALID', rl.in_amount, rl.in_amount_error, 'Nhập tiền nhiều hơn 1.000.000K', '1000001', 'Số tiền nạp tối đa là 1.000.000 K'],
            [5, 'Data validation', 'VALID', rl.in_amount, rl.in_amount_error, 'Nhập tiền bằng 1.000.000K', '1000000', ''],
            [6, 'Data validation', 'VALID-RAN', rl.in_amount, rl.in_amount_error, 'Nhập tiền lớn hơn 50k nhỏ hơn 1.000.000k', [50, 1000000], ''],
            [7, 'Data validation', 'INVALID', rl.in_amount, rl.in_amount_error, 'Nhập chữ ở ô số tiền', 'Numberofmoney', 'Vui lòng nhập số tiền'],
            [8, 'Data validation', 'CHECK-1-1', rl.in_amount, rl.out_amount, 'Số tiền hiển thị phải tương đương với số tiền nhập', [50, 1000000], ''],
            [9, 'Data validation', 'INVALID', rl.in_name, rl.in_name_error, 'Không nhập tên người gửi', '', 'Vui lòng nhập tên người gửi'],
            [10, 'Data validation', 'VALID', rl.in_name, rl.in_name_error, 'Nhập tên người gửi', 'Tuấn Anh @ 123', ''],
            [11, 'Data validation', 'VALID', rl.in_code, rl.in_code_error, 'Không nhập mã giao dịch', '', ''],
            [12, 'Data validation', 'VALID', rl.in_code, rl.in_code_error, 'Nhập mã giao dịch', 'CODE123456789', ''],
            [13, 'Copy', 'UI', [rl.copy_owner_btn, rl.copy_number_btn, rl.copy_place_btn], [rl.copy_owner_text, rl.copy_number_text, rl.copy_place_text], 'Các nút COPY chuyển sang COPIED khi click và chuyển về COPY khi click nút COPY khác', '', ''],
            [14, 'Copy', 'FUNC', [rl.copy_owner_btn, rl.copy_number_btn, rl.copy_place_btn], None, 'Nội dung được copy vào clipboard khi click COPY', '', ''],
            [15, 'Helptext', 'TEXT', rl.in_amount, None, 'Nhập số tiền', '', 'Nhập số tiền'],
            [16, 'Helptext', 'TEXT', rl.in_name, None, 'Nhập tên người gửi', '', 'Nhập tên người gửi'],
            [17, 'Helptext', 'TEXT-MULTI', rl.in_code, None, 'Nhập mã giao dịch', rl.data_helptext, ''],
        ]

        # RUNNING TEST
        if MainMenuLocators.MENU_DANG_KY.visible():
            MainMenuLocators.MENU_DANG_KY.click()
            self.driver.implicitly_wait(30)
            time.sleep(5)
            self.now = re.sub('[ :-]', '', str(datetime.now()).split('.')[0])
            account_test = 'tuananhle' + self.now
            SignupLocators.username.set_text('tuananhle' + self.now)
            SignupLocators.password.set_text('123456')
            SignupLocators.re_password.set_text('123456')
            SignupLocators.phoneno.set_text('0935770998')
            SignupLocators.btn_agree.click()
            SignupLocators.btn_register.click()
            time.sleep(2)
            if SignupLocators.popup_error.visible():
                SignupLocators.popup_error_btn_confirm.click()
                SignupLocators.btn_close.click()
                if MainMenuLocators.MENU_DANG_NHAP.visible():
                    MainMenuLocators.MENU_DANG_NHAP.click()
                    account_test = 'tuananhle20210405110106'
                    LoginLocators.input_username.set_text(account_test)
                    LoginLocators.input_password.set_text('123456')
                    LoginLocators.btn_login.click()
                    time.sleep(2)
            self.TEST_DATA_HEADER.append(['Account Test', 'Username: ' + account_test + ', pass: 123456'])
        if UserInfoLocator.drop_username.visible():
            base.set_url(self.workingPage)
            time.sleep(3)
            rl.first_100.click()
            rl.rc_bank.click()
            time.sleep(1)
            rl.bank_Selector.click()
            rl.bank_Vietcombank.click()
            rl.in_amount.set_text('999999999')
            rl.in_name.set_text('LE TUAN ANH')
            rl.in_code.set_text('CODE123456789')
            rl.TAO_PHIEU_NAP.click()
            self.driver.implicitly_wait(30)
            Template_Report = Report_temp(self.name.upper(), self.TEST_RESULT, self.TEST_DATA_HEADER)
            for method in rl.data_listBankMethod:
                rl.data_listBankMethod[method].click()
                for bank in rl.data_listBanks:
                    rl.bank_Selector.click()
                    rl.data_listBanks[bank].click()
                    self.TEST_RESULT.append(['Case: '+method + ' '+bank, '', '', '', '', '', ''])
                    print('\n', '-'*15, ' Recharge method: ', method, ', Bank: ', bank, ' ', 15*'-')

                    for i in TEST_DATA:
                        print('\n', '-'*15, ' Case: ', str(i[0]), ': ', i[5], ' ', 15*'-')
                        if rl.bank_Selector.visible() == False:
                            base.set_url(self.workingPage)
                            if rl.first_100.visible():
                                rl.first_100.click()
                            rl.rc_bank.click()
                            time.sleep(1)
                            rl.bank_Selector.click()
                            rl.bank_Vietcombank.click()
                            rl.in_amount.set_text('456')
                            rl.in_name.set_text('LE TUAN ANH')
                            rl.in_code.set_text('CODE123456789')
                            rl.TAO_PHIEU_NAP.click()
                            time.sleep(3)
                        if i[1] == 'Data validation':
                            if 'INVALID' in i[2]:
                                if i[2] == 'INVALID-MULTI':
                                    self.TEST_RESULT.append([i[0], i[5], '-', '-', '-', '-', '-'])

                                self.TEST_RESULT.append(ValidateData.CheckINVALIDCase(i, self.name))
                            elif 'VALID' in i[2]:
                                if i[2] == 'VALID-MULTI':
                                    self.TEST_RESULT.append([i[0], i[5], '-', '-', '-', '-', '-'])
                                if i[2] == 'VALID-RAN':
                                    i[6] = random.randrange(i[6][0], i[6][1])
                                self.TEST_RESULT.append(ValidateData.CheckVALIDCase(i, self.name))
                            elif 'CHECK' in i[2]:
                                self.TEST_RESULT.append(ValidateData.CheckInputCase(i, self.name))
                        elif i[1] == 'Show/Hide pw':
                            self.TEST_RESULT.append(ValidateData.ShowHideButton(i, self.name))

                        elif i[1] == 'Helptext':
                            if i[2] == 'TEXT-MULTI':
                                i[7] = rl.data_helptext[method][bank]
                            self.TEST_RESULT.append(ValidateData.HelpTextCheck(i, self.name))

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
