# from pages.components.element import BasePageElement
from pages.components.locators import HomePageLocators
from pages.components.locators import ge
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
                file = dir_img + '\\reports\\' + filename + '.png'
            else:
                file = dir_img + '\\' + location + '\\reports\\' + filename + '.png'
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


class HomePage(BasePage):
    def fill_text(self, textfield, text_content):
        box = self.driver.find_element(*textfield)
        box.send_keys(text_content)
