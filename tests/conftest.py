import pytest

from utility.webdriver import WebDriver


@pytest.fixture(scope='session')
def browser():
    driver = WebDriver().driver
    driver.maximize_window()
    yield
    driver.quit()




