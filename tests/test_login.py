"""
Tests: login
"""

import pytest

from config.settings import LOGIN, PASSWORD
from pages.login_page import LoginPage


class TestLogin:
    @pytest.mark.xfail
    @pytest.mark.smoke
    def test_should_be_successful_login(self, browser_scope_function, login=LOGIN, password=PASSWORD):
        page = LoginPage(browser_scope_function)
        page.open_page()
        page.login(login, password)
        assert page.get_user_icon(), "User icon is not present, log in might have failed"

    @pytest.mark.no_credentials_required
    @pytest.mark.smoke
    @pytest.mark.parametrize('password', [
        pytest.param('', id='empty password'),
        pytest.param('incorrect_password', id='incorrect_password'),
    ])
    def test_login_incorrect_password(self, browser_scope_function, password, login=LOGIN):
        page = LoginPage(browser_scope_function)
        page.open_page()
        page.login(login, password)
        assert page.get_login_error(), "Log in error is not present but should be"
