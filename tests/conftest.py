import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_personal_settings():
    browser.config.window_width = 1300
    browser.config.window_height = 1000
    browser.open('https://www.finam.ru/')
    browser.element('.p15x.window-close.pointer').click()
    yield
    browser.quit()
