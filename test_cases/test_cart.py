import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.LoginPage import LoginPage
from pages.AllItems import AllItems
from pages.Cart import Cart
from pages.ExpandedList import ExpandedList
from configurations.config import LOGIN_URL, VALID_USERNAME, VALID_PASSWORD


class TestCart:

    @allure.feature('Cart')
    @allure.story('Cart counter')
    def test_verify_cart_counter_visible(self, setup):
        shopping_cart_counter = (By.XPATH, "//span[@class='shopping_cart_badge']")

        driver = setup
        sut = LoginPage(driver)
        sut.open_login_page(LOGIN_URL)
        sut.login(VALID_USERNAME, VALID_PASSWORD)

        all_items = AllItems(driver)
        all_items.verify_cart_is_empty()
        all_items.add_product_to_cart_by_name("Sauce Labs Backpack")

        sut.assert_element_visible(*shopping_cart_counter)

    @pytest.mark.smoke
    @allure.feature('Cart')
    @allure.story('Product in cart')
    def test_verify_product_visible_in_cart(self, setup):
        expected_product = (By.XPATH,"//div[@class='inventory_item_name' and contains(text(), 'Sauce Labs Backpack')]")

        driver = setup
        sut = LoginPage(driver)
        sut.open_login_page(LOGIN_URL)
        sut.login(VALID_USERNAME, VALID_PASSWORD)

        all_items = AllItems(driver)
        all_items.verify_cart_is_empty()
        all_items.add_product_to_cart_by_name("Sauce Labs Backpack")
        all_items.open_cart()

        sut.assert_element_visible(*expected_product)


