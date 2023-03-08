"""
Locators: user profile page
"""


from selenium.webdriver.common.by import By


class UserProfilePageLocators:
    FORK_BUTTON = (By.CSS_SELECTOR, ".js-profile-editable-replace a[data-hydro-click*='follow button']")
