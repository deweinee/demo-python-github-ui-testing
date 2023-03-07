"""
Locators: base page
"""

from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, "header .details-overlay img.avatar")
