from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AuthPage:
    def __init__(self, driver: WebDriver) -> None:
        self.__url = 'https://trello.com/u/aleksey34/boards'
        self.__driver = driver

    def go(self):
        self.__driver.get(self.__url)

    def login_as(self, email: str, password: str):
        self.__driver.find_element(
            By.CSS_SELECTOR, "#username-_r0_").send_keys(email)
        self.__driver.find_element(By.CSS_SELECTOR, "#login-submit").click()
        self.__driver.find_element(
            By.CSS_SELECTOR, "#password").send_keys(password)
        self.__driver.find_element(By.CSS_SELECTOR, "#login-submit").click()

    def get_current_url(self):
        return self.__driver.current_url
