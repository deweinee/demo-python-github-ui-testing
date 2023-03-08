"""
Tests: user profile
"""

import pytest

from config.settings import ALIEN_PROFILE
from pages.user_profile_page import UserProfilePage


@pytest.mark.no_credentials_required
class TestUserProfileUnauthorizedUser:
    def test_follow_button_should_redirect_to_login(self, browser_scope_function, url=ALIEN_PROFILE):
        """
        Unauthorized user should be redirected to login page after clicking 'follow' button
        """
        page = UserProfilePage(browser_scope_function, url)
        page.open_page()
        page.click_follow_button()
        page_url = page.get_current_url_with_explicit_timeout()
        assert "github.com/login" in page_url, f"Page url should contain github.com/login but is in fact {page_url}"
