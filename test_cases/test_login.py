from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.ExpandedList import ExpandedList
from configurations.config import LOGIN_URL, VALID_USERNAME, VALID_PASSWORD
import pytest
import allure
import time

class TestLogin:
    invalid_username = 'Invalidusername'
    invalid_password = 'Invalidpassword'

    @allure.feature('User Login')
    @allure.story('Valid Login Title')
    def test_valid_title(self,setup):
        expected_title = 'Swag Labs'

        driver = setup
        sut = LoginPage(driver)
        sut.open_login_page(LOGIN_URL)

        if driver.title == expected_title:
            assert True
        else:
            driver.save_screenshot("..\\screenshots\\error_screenshot.png")
            assert False

    @pytest.mark.smoke
    @allure.feature('User Login')
    @allure.story('Valid login')
    def test_valid_login(self, setup):
        driver = setup

        sut = LoginPage(driver)
        sut.open_login_page(LOGIN_URL)
        sut.login(VALID_USERNAME, VALID_PASSWORD)

        sut.assert_element_visible(By.XPATH,"//div[@class='app_logo']")

    @allure.feature('User Login')
    @allure.story('Invalid username')
    def test_invalid_login_by_username(self, setup):
        driver = setup
        driver.get(LOGIN_URL)
        sut = LoginPage(driver)
        sut.login(self.invalid_username, VALID_PASSWORD)

        assert driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text == 'Epic sadface: Username and password do not match any user in this service'

    @allure.feature('User Login')
    @allure.story('Invalid password')
    def test_invalid_login_by_password(self, setup):
        driver = setup
        driver.get(LOGIN_URL)
        sut = LoginPage(driver)
        sut.login(VALID_USERNAME, self.invalid_password)

        assert driver.find_element(By.CSS_SELECTOR,"h3[data-test='error']").text == 'Epic sadface: Username and password do not match any user in this service'

    @pytest.mark.smoke
    @allure.feature('User Login')
    @allure.story('Logout')
    def test_logout(self, setup):
        driver = setup
        driver.get(LOGIN_URL)
        sut = LoginPage(driver)
        sut.login(VALID_USERNAME, VALID_PASSWORD)

        expanded_list = ExpandedList(driver)
        expanded_list.logout()

        expected_element = (By.XPATH, "//div[@class='login_logo']")
        sut.assert_element_visible(*expected_element)
