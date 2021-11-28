import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as c_options
from selenium.webdriver.firefox.options import Options as f_options

from config.settings import LOGIN, PASSWORD
from pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Browser name")


def _browser(request):
    """
    basis for webdriver browser fixtures
    so it would be possible to use them with different scopes in the same runtime

    """
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_options = c_options()
        chrome_options.add_argument("--window-size=1200,800")
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        firefox_options = f_options()
        firefox_options.add_argument("--width=1200")
        firefox_options.add_argument("--height=800")
        browser = webdriver.Firefox(options=firefox_options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def browser_scope_function(request):
    """
    webdriver browser fixture when it's needed fresh for every function

    """
    yield from _browser(request)


@pytest.fixture(scope="class")
def browser_scope_class(request):
    """
    webdriver browser fixture when it's needed ones for a class
    in order to avoid unnecessary waste of time
    (for instance, test TestRepositoryAccessLoggedInUser)

    """
    yield from _browser(request)


@pytest.fixture(scope="class")
def ui_login(browser_scope_class, login=LOGIN, password=PASSWORD):
    """
    fixture for user log in

    for a real project it might be better to create new users with new repositories every time and delete it all after
    but for this small demo existing users and repos will do

    """
    page = LoginPage(browser_scope_class)
    page.open_page()
    page.login(login, password)
