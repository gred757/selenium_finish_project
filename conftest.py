import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    user_lang = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_lang})
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    print("\nStart test \nlang: {}".format(user_lang))
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nEnd test")
    browser.quit()


