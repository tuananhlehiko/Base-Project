from element import BasePageElement
from locators import HomePageLocators
import os


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def is_title_match(self, title):
        if title in self.driver.title:
            return True
        else:
            return False

    def is_button_appear(self, btn):
        try:
            self.driver.find_element(*btn)
            return True
        except Exception as e:
            print(e)
            return False

    def tap_button(self, btn):
        try:
            button = self.driver.find_element(*btn)
            button.click()
            return True
        except Exception as e:
            print("Error: "+e + " \n")
            return False

    def is_alert_appear(self, alert):
        try:
            self.driver.find_element(*alert)
            return True
        except Exception:
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


class HomePage(BasePage):
    def fill_text(self, textfield, text_content):
        box = self.driver.find_element(*textfield)
        box.send_keys(text_content)
