"""
Locators: login page
"""

from selenium.webdriver.common.by import By


class LoginPageLocators:
    USER_LOGIN = (By.CSS_SELECTOR, "#login_field")
    USER_PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".auth-form-body input[type='submit']")
    LOGIN_ERROR = (By.CSS_SELECTOR, "#js-flash-container > .flash-error div")
