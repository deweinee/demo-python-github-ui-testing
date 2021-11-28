from locators.repository_page_locators import RepositoryPageLocators
from pages.base_page import BasePage


class RepositoryPage(BasePage):
    def __init__(self, browser, url, timeout=3):
        super().__init__(browser, url, timeout)
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def get_readme_element(self):
        return self.get_element(*RepositoryPageLocators.README_MD)
