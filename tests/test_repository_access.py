import pytest

from config.settings import (ALIEN_PRIVATE_REPOSITORY,
                             ALIEN_PRIVATE_REPOSITORY_SHARED,
                             ALIEN_PUBLIC_REPOSITORY, PASSWORD,
                             USER_PRIVATE_REPOSITORY, USER_PUBLIC_REPOSITORY)
from pages.repository_page import RepositoryPage


@pytest.mark.no_credentials_required
@pytest.mark.usefixtures("browser_scope_class")
class TestRepositoryAccessUnauthorisedUser:
    def test_access_should_be_successful(self, browser_scope_class, url=ALIEN_PUBLIC_REPOSITORY):
        page = RepositoryPage(browser_scope_class, url)
        page.open_page()
        assert page.get_readme_element(), "Readme.md is not present but should be"

    def test_access_should_be_denied(self, browser_scope_class, url=ALIEN_PRIVATE_REPOSITORY):
        page = RepositoryPage(browser_scope_class, url)
        page.open_page()
        page_title = page.get_page_title()
        assert "Page not found" in page_title, f"Page title should be 'Page not found' but is in fact {page_title}"


@pytest.mark.skipif(PASSWORD == "", reason="no credentials provided in config/settings.py")
@pytest.mark.usefixtures("ui_login")
@pytest.mark.usefixtures("browser_scope_class")
class TestRepositoryAccessLoggedInUser:
    @pytest.mark.parametrize('url', [
        pytest.param(USER_PUBLIC_REPOSITORY, id='user\'s public repository'),
        pytest.param(USER_PRIVATE_REPOSITORY, id='user\'s private repository'),
        pytest.param(ALIEN_PUBLIC_REPOSITORY, id='alien public repository'),
        pytest.param(ALIEN_PRIVATE_REPOSITORY_SHARED, id='alien private repository with shared access'),
    ])
    def test_access_should_be_successful(self, browser_scope_class, url):
        page = RepositoryPage(browser_scope_class, url)
        page.open_page()
        assert page.get_readme_element(), "Readme.md is not present but should be"

    def test_access_should_be_denied(self, browser_scope_class, url=ALIEN_PRIVATE_REPOSITORY):
        page = RepositoryPage(browser_scope_class, url)
        page.open_page()
        page_title = page.get_page_title()
        assert "Page not found" in page_title, f"Page title should be 'Page not found' but is in fact {page_title}"
