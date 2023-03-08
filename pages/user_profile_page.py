"""
User profile page functions
"""

from locators.user_profile_page_locators import UserProfilePageLocators
from pages.base_page import BasePage


class UserProfilePage(BasePage):
    def __init__(self, browser, url, timeout=3):
        super().__init__(browser, url, timeout)
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def click_follow_button(self):
        self.get_element(*UserProfilePageLocators.FORK_BUTTON).click()
