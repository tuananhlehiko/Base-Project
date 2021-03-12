from test_junkie.decorators import test, Suite, afterTest
from src.pages.Browser import Browser
from src.pages.page.AboutPage import AboutPage
from src.pages.page.DocumentationPage import DocumentationPage
from src.pages.page.HomePage import HomePage
@Suite(parameters=[HomePage, DocumentationPage, AboutPage])
class NavigationSuite:
    @afterTest()
    def after_test(self):
        Browser.shutdown()
    @staticmethod
    def __validate_page_properties(page):
        """
        There are common validation steps in this suite,
        thus it was unified under this method.
        This method validates:
        - expected and actual page URL
        - expected and actual page Title
        Based on the Page Object definitions
        :param page: Object, any page object
        :return: None
        """
        expected_url, actual_url = page.expected_url, page.get_actual_url()
        assert expected_url in actual_url, \
            "Expected URL: {} Actual URL: {}".format(expected_url, actual_url)
        expected_title, actual_title = page.expected_title, page.get_actual_title()
        assert expected_title in actual_title, \
            "Expected Title: {} Actual Title: {}".format(expected_title, actual_title)
    @test(parameters=["logo", "documentation", "about", "get_started", "tutorials"],
          parallelized_parameters=True)
    def verify_header_navigation(self, suite_parameter, parameter):
        page = suite_parameter().open()
        page = getattr(page.header, "click_{}".format(parameter))()
        NavigationSuite.__validate_page_properties(page)
    @test(parameters=["home", "documentation", "about", "get_started", "tutorials"],
          parallelized_parameters=True)
    def verify_footer_navigation(self, suite_parameter, parameter):
        page = suite_parameter().open()
        page = getattr(page.footer, "click_{}".format(parameter))()
        NavigationSuite.__validate_page_properties(page)