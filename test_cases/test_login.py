import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.LoginPage import LoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogMaker



class TestLogin:
    LOGIN_URL = ReadConfig.get_login_page_url()
    VALID_USERNAME = 'standard_user'
    VALID_PASSWORD = 'secret_sauce'
    INVALID_USERNAME = 'Invalidusername'
    INVALID_PASSWORD = 'Invalidpassword'
    logger = LogMaker.log_gen()



    def test_valid_title(self,setup):
        self.logger.info("**************test_valid_title")
        self.driver = setup
        self.driver.get(self.LOGIN_URL)
        actual_title = self.driver.title
        expected_title = 'Swag Labs1'

        if actual_title == expected_title:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot("..\\screenshots\\error_screenshot.png")
            self.driver.close()
            assert False

    def test_valid_login(self, setup):
        self.driver = setup
        self.driver.get(self.LOGIN_URL)
        self.login_page = LoginPage(self.driver)
        self.login_page.enter_login(self.VALID_USERNAME)
        self.login_page.enter_password(self.VALID_PASSWORD)
        self.login_page.click_login()

        assert self.driver.find_element(By.XPATH, "//div[@class='app_logo']").is_displayed()

        self.driver.close()

    def test_invalid_login_by_username(self, setup):
        self.driver = setup
        self.driver.get(self.LOGIN_URL)
        self.login_page = LoginPage(self.driver)
        self.login_page.enter_login(self.INVALID_USERNAME)
        self.login_page.enter_password(self.VALID_PASSWORD)
        self.login_page.click_login()

        assert self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text == 'Epic sadface: Username and password do not match any user in this service'

        self.driver.close()

    def test_invalid_login_by_password(self, setup):
        self.driver = setup
        self.driver.get(self.LOGIN_URL)
        self.login_page = LoginPage(self.driver)
        self.login_page.enter_login(self.VALID_USERNAME)
        self.login_page.enter_password(self.INVALID_PASSWORD)
        self.login_page.click_login()

        assert self.driver.find_element(By.CSS_SELECTOR,"h3[data-test='error']").text == 'Epic sadface: Username and password do not match any user in this service'

        self.driver.close()


# BASE_URL = 'https://www.saucedemo.com/'
# USERNAME_FIELD_LOC = (By.XPATH, "//input[@id='user-name']")
# PASSWORD_FIELD_LOC = (By.XPATH, "//input[@id='password']")
# LOGIN_PAGE_BANNER_LOC = (By.XPATH, "//div[@class='login_logo']")
# LOGIN_PAGE_TITLE_EXPECTED = 'Swag Labs'
# LOGIN_BUTTON_LOC = (By.XPATH, "//input[@id='login-button']")

# ERROR_WRONG_LOGIN_EXPECTED = 'Epic sadface: Username and password do not match any user in this service'
# ERROR_LOC = (By.CSS_SELECTOR, "h3[data-test='error']")
# SHOPPING_CART_NUMBER_LOC = (By.XPATH, "//span[@class='shopping_cart_badge']")
# LEFT_MENU_BURGER_OPEN_BUTTON = (By.XPATH, "//button[@id='react-burger-menu-btn']")
# LEFT_MENU_BURGER_CLOSE_BUTTON = (By.XPATH, "//button[@id='react-burger-cross-btn']")
# LOGOUT_BUTTON = (By.XPATH, "//a[@id='logout_sidebar_link']")
# ALL_ITEMS_BUTTON = (By.XPATH, "//a[@id='inventory_sidebar_link']")
# SHOPPING_CART_LOC = (By.XPATH, "//a[@class='shopping_cart_link']")
# LEFT_MENU_BURGER_RESET_APP_STATUS_BUTTON = (By.XPATH, "//a[@id='reset_sidebar_link']")
# SORT_PRODUCTS_DROPDOWN = (By.XPATH, "//select[@class='product_sort_container']")
# FACEBOOK_LOGO_LOC = (By.XPATH, "//a[@data-test = 'social-facebook']")
# X_LOGO_LOC = (By.XPATH, "//a[@data-test = 'social-twitter']")
# LINKEDIN_LOGO_LOC = (By.XPATH, "//a[@data-test = 'social-linkedin']")
#
# SORTING_METHODS_DICT = {"NAME ASC" : "Name (A to Z)", "NAME DESC" : "Name (Z to A)", "PRICE ASC" : "Price  (low to high)", "PRICE DESC" : "Price  (high to low)"}