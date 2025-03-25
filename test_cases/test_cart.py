import time

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

    def test_verify_cart_counter_visible(self, setup):
        shopping_cart_counter = (By.XPATH, "//span[@class='shopping_cart_badge']")

        self.logger.info("***test_verify_cart_counter_visible***")
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.open_login_page(LOGIN_URL)
        self.login_page.login(VALID_USERNAME, VALID_PASSWORD)

        all_items = AllItems(self.driver)
        all_items.verify_cart_is_empty()
        all_items.add_product_to_cart_by_name("Sauce Labs Backpack")

        self.assertion = Assertion(self.driver)
        self.assertion.assert_element_visible(shopping_cart_counter)

    def test_verify_product_visible_in_cart(self, setup):
        expected_product = (By.XPATH,"//div[@class='inventory_item_name' and contains(text(), 'Sauce Labs Backpack')]")

        self.logger.info("***verify_product_visible_in_cart***")
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.open_login_page(LOGIN_URL)
        self.login_page.login(VALID_USERNAME, VALID_PASSWORD)

        self.all_items = AllItems(self.driver)
        self.all_items.verify_cart_is_empty()
        self.all_items.add_product_to_cart_by_name("Sauce Labs Bike Light")
        self.all_items.open_cart()

        self.assertion = Assertion(self.driver)
        self.assertion.assert_element_visible(expected_product)

