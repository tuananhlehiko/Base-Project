from selenium.webdriver.common.by import By
from src.pages.UiObject import UiObject
class PageHeader:
    HOME_LINK = UiObject(By.XPATH, "//ul[2]/li/a[text() = 'HOME']")
    GET_STARTED_LINK = UiObject(By.XPATH, "//ul[2]/li/a[text() = 'GET STARTED']")
    TUTORIALS_LINK = UiObject(By.XPATH, "//ul[2]/li/a[text() = 'TUTORIALS']")
    DOCUMENTATION_LINK = UiObject(By.XPATH, "//ul[2]/li/a[text() = 'DOCUMENTATION']")
    ABOUT_LINK = UiObject(By.XPATH, "//ul[2]/li/a[text() = 'ABOUT']")
    LOGO = UiObject(By.XPATH, "//img[@title = 'Test Junkie logo']/parent::a")
    NAV_BAR = UiObject(By.XPATH, "//div[@class = 'navbar-fixed']")
    def __init__(self):
        pass
    @staticmethod
    def click_home():
        PageHeader.HOME_LINK.click()
        from src.pages.home.HomePage import HomePage
        return HomePage()
    @staticmethod
    def click_get_started():
        PageHeader.GET_STARTED_LINK.click()
        from src.pages.get_started.GetStartedPage import GetStartedPage
        return GetStartedPage()
    @staticmethod
    def click_tutorials():
        PageHeader.TUTORIALS_LINK.click()
        from src.pages.tutorials.TutorialsPage import TutorialsPage
        return TutorialsPage()
    @staticmethod
    def click_documentation():
        PageHeader.DOCUMENTATION_LINK.click()
        from src.pages.documentation.DocumentationPage import DocumentationPage
        return DocumentationPage()
    @staticmethod
    def click_about():
        PageHeader.ABOUT_LINK.click()
        from src.pages.about.AboutPage import AboutPage
        return AboutPage()
    @staticmethod
    def click_logo():
        PageHeader.LOGO.click()
        from src.pages.home.HomePage import HomePage
        return HomePage()