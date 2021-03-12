import time
from test_junkie.decorators import Suite, test, afterTest
from src.pages.Browser import Browser
from src.pages.page.DocumentationPage import DocumentationPage
@Suite()
class DocuamentationSuite:
    @afterTest()
    def after_test(self):
        Browser.shutdown()
    @test()
    def verify_content_anchor_links(self):
        failed_sections = []
        page = DocumentationPage().open()
        Browser.maximize()
        script = "$('#navbar').hide()"
        Browser.get_driver().execute_script(script, DocumentationPage().header.NAV_BAR.get_element())
        section_links = page.get_content_links_per_section()
        for section, links in section_links.items():
            for link in links:  # links is an array of UiObjects
                href = link.get_attribute("href")
                if page.expected_url in href:
                    link.click()
                    current_url = page.get_actual_url()
                    if href not in current_url:
                        if href.split("#")[-1] not in ["cli_run", "cli_audit", "cli_config"]:
                            # Changing CLI tabs does not change the URL thus we ignore those failures
                            failed_sections.append({section: href})
                    time.sleep(0.5)  # because page scrolls on anchor click, we pause for half a sec to avid errors
        assert not failed_sections, "Some anchor links don't work: {}".format(failed_sections)
    @test()
    def verify_navigation_links(self):
        failed_sections = []
        page = DocumentationPage().open()
        Browser.maximize()
        links = page.get_left_nav_links()
        for link in links:  # links is an array of UiObjects
            link.click()
            href = link.get_attribute("href")
            current_url = page.get_actual_url()
            if href not in current_url:
                failed_sections.append(href)
        assert not failed_sections, "Some menu links don't work: {}".format(failed_sections)