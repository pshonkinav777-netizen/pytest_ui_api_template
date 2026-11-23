import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument(r"--user-data-dir=C:\selenium_profile")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    browser.maximize_window()
    yield browser
    browser.quit
