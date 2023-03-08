"""
Base page functions
"""

import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url="", timeout=3):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open_page(self):
        self.browser.get(self.url)

    def get_element(self, method, selector):
        try:
            return self.browser.find_element(method, selector)
        except NoSuchElementException:
            return False

    def get_element_with_timeout(self, method, selector, timeout=3):
        try:
            return WebDriverWait(self.browser, timeout, 1, TimeoutException).until(
                EC.presence_of_element_located((method, selector)))
        except TimeoutException:
            return False

    def get_current_url(self):
        return self.browser.current_url

    def get_current_url_with_explicit_timeout(self):
        time.sleep(1)
        return self.browser.current_url

    def get_user_icon(self):
        return self.get_element(*BasePageLocators.USER_ICON)

    def get_page_title(self):
        return self.browser.title
