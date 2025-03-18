import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogMaker
from base_pages.LoginPage import LoginPage
from base_pages.ExpandedList import ExpandedList
from test_cases.assertions import Assertion


class TestLogin:
    login_url = ReadConfig.get_login_page_url()
    valid_username = 'standard_user'
    valid_password = 'secret_sauce'
    invalid_username = 'Invalidusername'
    invalid_password = 'Invalidpassword'
    logger = LogMaker.log_gen()

    def test_valid_title(self,setup):
        self.logger.info("***test_valid_title***")
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.open_login_page(self.login_url)

        actual_title = self.driver.title
        expected_title = 'Swag Labs'

        if actual_title == expected_title:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot("..\\screenshots\\error_screenshot.png")
            self.driver.close()
            assert False


    def test_valid_login(self, setup):
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.open_login_page(self.login_url)
        self.login_page.login(self.valid_username, self.valid_password)

        expected_element = (By.XPATH, "//div[@class='app_logo']")
        visibility_tester = Assertion(self.driver)
        visibility_tester.assert_element_visible(expected_element)

        self.expanded_list = ExpandedList(self.driver)
        self.expanded_list.logout()
        self.driver.close()

    def test_invalid_login_by_username(self, setup):
        self.driver = setup
        self.driver.get(self.login_url)
        self.login_page = LoginPage(self.driver)
        self.login_page.login(self.invalid_username, self.valid_password)

        assert self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text == 'Epic sadface: Username and password do not match any user in this service'

        self.driver.close()

    def test_invalid_login_by_password(self, setup):
        self.driver = setup
        self.driver.get(self.login_url)
        self.login_page = LoginPage(self.driver)
        self.login_page.login(self.valid_username, self.invalid_password)
        self.login_page.click_login()

        assert self.driver.find_element(By.CSS_SELECTOR,"h3[data-test='error']").text == 'Epic sadface: Username and password do not match any user in this service'

        self.driver.close()

    def test_logout(self, setup):
        self.driver = setup
        self.driver.get(self.login_url)
        self.login_page = LoginPage(self.driver)
        self.login_page.login(self.valid_username, self.valid_password)
        self.expanded_list = ExpandedList(self.driver)
        self.expanded_list.logout()

        expected_element = (By.XPATH, "//div[@class='login_logo']")
        visibility_tester = Assertion(self.driver)
        visibility_tester.assert_element_visible(expected_element)

        self.driver.close()

