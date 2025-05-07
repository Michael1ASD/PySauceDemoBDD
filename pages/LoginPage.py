import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from configurations.config import LOGIN_URL
from pages.BasePage import BasePage
import allure

class LoginPage(BasePage):
    username_loc = (By.XPATH, "//input[@id='user-name']")
    password_loc = (By.XPATH, "//input[@id='password']")
    login_button_loc = (By.XPATH, "//input[@id='login-button']")

    @allure.step("Open login page")
    def open_login_page(self, url=LOGIN_URL):
        self.driver.get(url)

    def _enter_login(self, username):
        self.input_text(*self.username_loc, username)

    def _enter_password(self, password):
        self.input_text(*self.password_loc, password)

    def _click_login(self):
        self.click(*self.login_button_loc)

    @allure.step("Login")
    def login(self, username, password):
        self._enter_login(username)
        self._enter_password(password)
        self._click_login()

        try:
            self.wait_for_alert_and_accept()
        except TimeoutException:
            pass