from pages.locators import ge
from pages.utils import Create_dir
import os


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def is_title_match(self, title):
        if title in self.driver.title:
            return True
        else:
            return False

    def screenshot_window(self, filename, location=''):
        try:
            dir_img = os.getcwd()
            if location == '':
                path = dir_img + '\\reports'
            else:
                path = dir_img + '\\reports\\' + location
                
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
