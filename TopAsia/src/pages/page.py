from TopAsia.src.pages.locators import ge
from TopAsia.src.pages.utils import Create_dir
import os


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
                path = dir_img +'\\'+ ge.ProjectName +'\\Test Results\\img'
            else:
                path = dir_img +'\\'+ ge.ProjectName +'\\Test Results\\' + location + '\\img'
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
        text_input = 'SHOW PASS'
        type_hidden = 'password'
        type_shown = 'text'        
        sts = ''
        actual = ''
        notes = ''
        if data[2] == 'SHOW':
            data[3].set_text(text_input)
            if data[4][0].visible():
                data[4][0].click()
                actual = data[3].get_attribute('type')
                if actual == type_shown:
                    sts = 'PASSED'
                else:
                    BasePage.ScrShot(str(data[0])+'_ The show password display wrong', name)
                    sts = 'FAILED'
                notes = 'INPUT: ' + text_input + '\nType: ' + actual
            else:
                data[4][1].click()
                data[4][0].click()
                actual = data[3].get_attribute('type')
                if actual == type_shown:
                    sts = 'PASSED'
                else:
                    BasePage.ScrShot(str(data[0])+'_ The show password display wrong', name)
                    sts = 'FAILED'
                notes = 'INPUT: ' + text_input + '\nType: ' + actual
            return [data[0], data[5], text_input, type_shown, actual, sts, notes]
        else:
            data[3].set_text(text_input)
            if data[4][0].visible():
                data[4][0].click()
                actual = data[3].get_attribute('type')
                if actual == type_hidden:
                    sts = 'PASSED'
                else:
                    BasePage.ScrShot(str(data[0])+'_ The show password display wrong', name)
                    sts = 'FAILED'
                notes = 'INPUT: ' + text_input + '\nType: ' + actual
            else:
                data[4][1].click()
                data[4][0].click()
                actual = data[3].get_attribute('type')
                if actual == type_hidden:
                    sts = 'PASSED'
                else:
                    BasePage.ScrShot(str(data[0])+'_ The show password display wrong', name)
                    sts = 'FAILED'
                notes = 'INPUT: ' + text_input + '\nType: ' + actual
            return [data[0], data[5], text_input, type_hidden, actual, sts, notes]
            
