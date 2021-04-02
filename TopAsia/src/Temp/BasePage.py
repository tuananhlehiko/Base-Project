from src.pages.Browser import Browser

class BasePage:
    def __init__(self, domain, directory, title):
        """
        This class will be inherited by all of the Page Objects
        :param domain: STRING, Base domain of the website aka "https://test-junkie.com"
                               Base domain & expected URL will be used to open this page
        :param directory: STRING, expected URL of the page that is inheriting this class aka:
                                  "/documentation/" or "/get-started/"
        :param title: STRING, expected Title of the page that is inheriting this class
        """
        self.__title = title
        self.__directory = directory
        self.__domain = domain
        self.__expected_url = "{domain}{directory}".format(
            domain=domain, directory=directory)

    @property
    def expected_directory(self):
        return self.__directory

    @property
    def expected_domain(self):
        return self.__domain

    @property
    def expected_title(self):
        return self.__title

    @property
    def expected_url(self):
        return self.__expected_url

    @staticmethod
    def get_actual_title():
        return Browser.get_driver().title

    @staticmethod
    def get_actual_url():
        return Browser.get_driver().current_url

    def open(self, **kwargs):
        """
        This method will open the page which inherited BasePage
        :return: self (Page Object which inherited BasePage will be returned)
        """
        Browser.get_driver().get(self.expected_url)
        return self
