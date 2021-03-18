from selenium.webdriver.common.by import By
from src.pages.UIObject import UiObject
class PageFooter:
    COPYRIGHT = UiObject(By.XPATH, "//div[@class='footer-copyright']/div")
    HOME_LINK = UiObject(By.XPATH, "//a[text() = 'Home']")
    GET_STARTED_LINK = UiObject(By.XPATH, "//a[text() = 'Get Started']")
    TUTORIALS_LINK = UiObject(By.XPATH, "//a[text() = 'Tutorials']")
    DOCUMENTATION_LINK = UiObject(By.XPATH, "//a[text() = 'Documentation']")
    ABOUT_LINK = UiObject(By.XPATH, "//a[text() = 'About']")
    def __init__(self):
        pass
    @staticmethod
    def click_sponsor_logo(value):
        element = UiObject(By.XPATH, "//img[@alt='{}']/parent::a".format(value))
        stripped = element.get_attribute("href").split("//")[-1].split("/")
        domain = stripped[0]
        directory = stripped[-1] if len(stripped) > 1 else ""
        element.click()
        from src.pages.BasePage import BasePage
        return BasePage(domain=domain, title=None, directory=directory)

    @staticmethod
    def click_external_link(value):
        element = UiObject(By.XPATH, "//a[contains(text(), '{}')]".format(value))
        stripped = element.get_attribute("href").split("//")[-1].split("/")
        domain = stripped[0]
        directory = stripped[-1] if len(stripped) > 1 else ""
        element.click()
        from src.pages.BasePage import BasePage
        return BasePage(domain=domain, title=None, directory=directory)

    @staticmethod
    def get_copy_right_msg():
        return PageFooter.COPYRIGHT.get_text()

    @staticmethod
    def click_home():
        PageFooter.HOME_LINK.click()
        from src.pages.page.HomePage import HomePage
        return HomePage()

    @staticmethod
    def click_get_started():
        PageFooter.GET_STARTED_LINK.click()
        from src.pages.page.GetStartedPage import GetStartedPage
        return GetStartedPage()

    @staticmethod
    def click_tutorials():
        PageFooter.TUTORIALS_LINK.click()
        from src.pages.page.TutorialsPage import TutorialsPage
        return TutorialsPage()

    @staticmethod
    def click_documentation():
        PageFooter.DOCUMENTATION_LINK.click()
        from src.pages.page.DocumentationPage import DocumentationPage
        return DocumentationPage()

    @staticmethod
    def click_about():
        PageFooter.ABOUT_LINK.click()
        from src.pages.page.AboutPage import AboutPage
        return AboutPage()