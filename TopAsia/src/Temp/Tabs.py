from selenium.webdriver.common.by import By
from src.pages.UIObject import UiObject

class Tabs:
    def __init__(self, container=None):
        self.__common_xpath = "{container}//div/ul[@class = 'tabs']"\
                              .format(container="" if not container else container)
    def get_active_content(self):
        return UiObject(By.XPATH, "{container}/parent::div/following-sibling::div[@id and contains(@class, 'active')]"
                        .format(container=self.__common_xpath)).get_text()
    def click_tab(self, value):
        UiObject(By.XPATH, "{container}//a[text() = '{value}']"
                 .format(container=self.__common_xpath, value=value)).click()
        return self
    def get_tab_objects(self):
        tabs = []
        elements = UiObject(By.XPATH, "{container}//a".format(container=self.__common_xpath)).get_elements()
        for element in elements:
            tabs.append(UiObject.from_web_element(element))
        return tabs