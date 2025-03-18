from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self, url):
        self.driver.get(url)

    def enter_login(self, username):
        username_loc = (By.XPATH, "//input[@id='user-name']")
        self.driver.find_element(*username_loc).clear()
        self.driver.find_element(*username_loc).send_keys(username)

    def enter_password(self, password):
        password_loc = (By.XPATH, "//input[@id='password']")
        self.driver.find_element(*password_loc).clear()
        self.driver.find_element(*password_loc).send_keys(password)

    def click_login(self):
        login_button = (By.XPATH, "//input[@id='login-button']")
        self.driver.find_element(*login_button).click()

    def login(self, username, password):
        self.enter_login(username)
        self.enter_password(password)
        self.click_login()