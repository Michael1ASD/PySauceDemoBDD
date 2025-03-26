import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.custom_logger import LogMaker
from base_pages.LoginPage import LoginPage
from base_pages.AllItems import AllItems
from base_pages.Cart import Cart
from base_pages.ExpandedList import ExpandedList
from utilities.assertions import Assertion
from configurations.config import LOGIN_URL, VALID_USERNAME, VALID_PASSWORD

class TestCheckout:
    valid_username = 'standard_user'
    valid_password = 'secret_sauce'
    logger = LogMaker.log_gen()

    @pytest.mark.smoke
    def test_verify_successful_checkout(self, setup):
        self.driver = setup
        login_page = LoginPage(self.driver)
        login_page.open_login_page(LOGIN_URL)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        all_items = AllItems(self.driver)
        all_items.verify_cart_is_empty()
        all_items.add_product_to_cart_by_name("Sauce Labs Bike Light")
        all_items.open_cart()

        cart = Cart(self.driver)
        cart.click_checkout_from_cart_view()
        cart.enter_checkout_credentials_and_continue()
        cart.finish_checkout()

        verification = Assertion(self.driver)
        verification.assert_element_visible((By.XPATH, "//h2[text()='Thank you for your order!']"))

        self.expanded_list = ExpandedList(self.driver)
        self.expanded_list.logout()
        self.driver.close()


