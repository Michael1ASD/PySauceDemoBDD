from selenium import webdriver
from selenium.webdriver.common.by import By
from configurations.config import LOGIN_URL


class LoginPage:
    username_loc = (By.XPATH, "//input[@id='user-name']")
    password_loc = (By.XPATH, "//input[@id='password']")
    login_button_loc = (By.XPATH, "//input[@id='login-button']")

    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self, url=LOGIN_URL):
        self.driver.get(url)

    def _enter_login(self, username):
        self.driver.find_element(*self.username_loc).clear()
        self.driver.find_element(*self.username_loc).send_keys(username)

    def _enter_password(self, password):
        self.driver.find_element(*self.password_loc).clear()
        self.driver.find_element(*self.password_loc).send_keys(password)

    def _click_login(self):
        self.driver.find_element(*self.login_button_loc).click()

    def login(self, username, password):
        self._enter_login(username)
        self._enter_password(password)
        self._click_login()