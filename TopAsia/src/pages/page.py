from TopAsia.src.pages.utils import Create_dir
import os
import datetime
import time


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def ScrShot(self, filename, location=''):
        """
        :param filename: String, name of image that your want to take screen
        :param location: String, the Folder of image file that you want to locate after screen shot
        :return: None
        """
        try:
            dir_img = os.getcwd()
            if location == '':
                path = dir_img + '\\TopAsia Test Results\\img'
            else:
                path = dir_img + '\\TopAsia Test Results\\' + location + '\\img'
            Create_dir(path)
            file = path + '\\' + filename + '.png'
            self.driver.get_screenshot_as_file(file)
        except Exception as e:
            print('Error: ', e)

    def get_size(self):
        try:
            return self.driver.get_window_size()
        except Exception as e:
            print('Error: ', e)

    def set_size(self, width, height):
        try:
            return self.driver.set_window_size(width, height)
        except Exception as e:
            print('Error: ', e)

    def get_url(self):
        try:
            return self.driver.current_url
        except Exception as e:
            print('Error: ', e)

    def set_url(self, link):
        try:
            return self.driver.get(link)
        except Exception as e:
            print('Error: ', e)


class HomePage(BasePage):
    pass


class GameLobbyPage(BasePage):
    pass


class GameCasinoPage(BasePage):
    pass


class ValidateData:
    # CHECKING SHOW/HIDE PASSWORD icon working or NOT
    def ShowHideButton(data, name):
        caseNo = str(data[0])
        text_input = 'SHOW PASS'
        sts = ''
        actual = ''
        notes = ''
        data[3].set_text(text_input)
        if data[4][0].visible():
            data[4][0].click()
        else:
            data[4][1].click()
            data[4][0].click()
        actual = data[3].get_attribute('type')
        if actual == data[7]:
            sts = 'PASSED'
        else:
            BasePage.ScrShot(caseNo+'_ The show password display wrong', name)
            sts = 'FAILED'
        notes = 'INPUT: ' + text_input + '\nType: ' + actual
        print('Status: \t', sts)
        print('Expected: \t', data[7])
        print('Actual: \t', actual, '\n')
        return [caseNo, data[5], text_input, data[7], actual, sts, notes]

    # CHECKING HELPTEXT
    def HelpTextCheck(data, name):
        caseNo = str(data[0])
        actual = ''
        sts = ''
        notes = ''
        actual = data[3].get_attribute('placeholder')
        if actual == data[7]:
            sts = 'PASSED'
        else:
            sts = 'FAILED'
            BasePage.ScrShot(caseNo+'_ The show password display wrong', name)
        print('Status: \t', sts)
        print('Expected: \t', data[7])
        print('Actual: \t', actual, '\n')
        return [caseNo, data[5], '-', data[7], actual, sts, notes]

    # CHECKING INVALID CASE
    def CheckINVALIDCase(data, name):
        caseNo = str(data[0])
        actual = ''
        sts = ''
        notes = ''
        if data[2] == 'INVALID-MULTI':
            for c in range(len(data[6])):
                caseNo = caseNo+'-'+str(c+1)
                data_input = 'validdata'+data[6][c]
                data[3].set_text(data_input)
                time.sleep(1)
                if data[4].visible():
                    actual = data[4].get_text()
                    if actual == data[7]:
                        sts = 'PASSED'
                    else:
                        sts = 'FAILED'
                        notes = 'Hiển thị lỗi không chính xác'
                        BasePage.ScrShot(caseNo+'_Error text is wrong', name)
                else:
                    sts = 'FAILED'
                    notes = 'Không hiển thị lỗi khi nhập ' + \
                        data[6][c]
                    BasePage.ScrShot(caseNo+'_Error text is not display', name)
        elif '-P' in data[2]:
            if data[5] == 'Mật khẩu hiện tại không đúng':
                oldpass_ = 'tuananhle2203'
                newpass_ = '123456'
                data_input = 'Oldpass: ' + oldpass_+', Password: ' + newpass_
                data[3][0].set_text(oldpass_)
                data[3][1].set_text(newpass_)
                data[3][2].set_text(newpass_)
                data[3][3].click()
                time.sleep(3)
                if data[4][0].visible():
                    actual = data[4][1].get_text()
                    if actual == data[7]:
                        sts = 'PASSED'
                    else:
                        sts = 'FAILED'
                        notes = 'Hiển thị lỗi không chính xác'
                        BasePage.ScrShot(caseNo+'_Error popup is wrong', name)
                    notes = notes + '\nCONTENT: '+actual
                    data[4][2].click()
                else:
                    actual = '-'
                    sts = 'FAILED'
                    notes = 'Error popup không hiển thị!'
                    BasePage.ScrShot(caseNo+'_Error popup not display', name)
        else:
            data_input = data[6]
            data[3].set_text(data_input)
            time.sleep(1)
            if data[4].visible():
                actual = data[4].get_text()
                if actual == data[7]:
                    sts = 'PASSED'
                else:
                    sts = 'FAILED'
                    notes = 'Hiển thị lỗi không chính xác'
                    BasePage.ScrShot(caseNo+'_Error text is wrong', name)
            else:
                sts = 'FAILED'
                notes = 'Không hiển thị lỗi'
                BasePage.ScrShot(caseNo+'_Error text is not display', name)
        print('Status: \t', sts)
        print('Expected: \t', data[7])
        print('Actual: \t', actual, '\n')
        return [caseNo, data[5], data_input, data[7], actual, sts, notes]

    # CHECKING INVALID CASE
    def CheckVALIDCase(data, name):
        caseNo = str(data[0])
        actual = ''
        sts = ''
        notes = ''
        data_input = ''
        if data[2] == 'VALID-MULTI':
            for c in range(len(data[6])):
                data_input = str(data[6][c])
                print('\n', '-'*15, ' Case: ', data_input, ': ', data[5], ' ', 15*'-')
                data[3].set_text(data_input)
                time.sleep(1)
                if data[4].visible():
                    actual = data[4].get_text()
                    sts = 'FAILED'
                    notes = 'Hiển thị lỗi khi nhập tên'
                    BasePage.ScrShot(caseNo+' Hiển thị lỗi khi nhập tên', name)
                else:
                    sts = 'PASSED'
        else:
            data[3].set_text(data[6])
            time.sleep(1)
            if data[4].visible():
                actual = data[4].get_text()
                sts = 'FAILED'
                notes = 'Hiển thị lỗi khi nhập đúng'
                BasePage.ScrShot(str(data[0])+'_Error text is display', name)
            else:
                sts = 'PASSED'
        print('Status: \t', sts)
        print('Expected: \t', data[7])
        print('Actual: \t', actual, '\n')
        return [caseNo, data[5], data_input, data[7], actual, sts, notes]
