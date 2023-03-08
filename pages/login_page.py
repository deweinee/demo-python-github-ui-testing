"""
Login page functions
"""

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, browser, url="https://github.com/login", timeout=2):
        super().__init__(browser, url, timeout)
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def login(self, login, password):
        self.get_element(*LoginPageLocators.USER_LOGIN).send_keys(login)
        self.get_element(*LoginPageLocators.USER_PASSWORD).send_keys(password)
        self.get_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def get_login_error(self):
        return self.get_element(*LoginPageLocators.LOGIN_ERROR)
