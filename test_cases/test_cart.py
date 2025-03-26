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


class TestCart:
    logger = LogMaker.log_gen()

    # @pytest.fixture("setup", params=["chrome","edge","firefox"])
    # @pytest.mark.parametrize("setup", [])
    def test_verify_cart_counter_visible(self, setup):
        shopping_cart_counter = (By.XPATH, "//span[@class='shopping_cart_badge']")

        self.logger.info("***test_verify_cart_counter_visible***")
        self.driver = setup
        login_page = LoginPage(self.driver)
        login_page.open_login_page(LOGIN_URL)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        all_items = AllItems(self.driver)
        all_items.verify_cart_is_empty()
        all_items.add_product_to_cart_by_name("Sauce Labs Backpack")

        assertion = Assertion(self.driver)
        assertion.assert_element_visible(shopping_cart_counter)

    @pytest.mark.smoke
    def test_verify_product_visible_in_cart(self, setup):
        expected_product = (By.XPATH,"//div[@class='inventory_item_name' and contains(text(), 'Sauce Labs Backpack')]")

        self.logger.info("***verify_product_visible_in_cart***")
        self.driver = setup
        login_page = LoginPage(self.driver)
        login_page.open_login_page(LOGIN_URL)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        all_items = AllItems(self.driver)
        all_items.verify_cart_is_empty()
        all_items.add_product_to_cart_by_name("Sauce Labs Backpack")
        all_items.open_cart()

        assertion = Assertion(self.driver)
        assertion.assert_element_visible(expected_product)

