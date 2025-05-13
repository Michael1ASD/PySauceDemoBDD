import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.AllItems import AllItems
from pages.Cart import Cart
from pages.ExpandedList import ExpandedList
from configurations.config import LOGIN_URL, VALID_USERNAME, VALID_PASSWORD


class TestCart:

    @allure.feature('Cart')
    @allure.story('Cart counter')
    def test_verify_cart_counter_visible(self, driver, login):
        shopping_cart_counter = (By.XPATH, "//span[@class='shopping_cart_badge']")

        all_items = AllItems(driver)
        all_items.verify_cart_is_empty()
        all_items.add_product_to_cart_by_name("Sauce Labs Backpack")

        all_items.assert_element_visible(*shopping_cart_counter)

    @pytest.mark.smoke
    @allure.feature('Cart')
    @allure.story('Verify total value of cart')
    def test_total_cart_value(self, driver, login):

        all_items = AllItems(driver)
        all_items.verify_cart_is_empty()
        all_items.add_product_to_cart_by_name("Sauce Labs Backpack")
        expected_backpack_price = all_items.return_price_by_product_name("Sauce Labs Backpack")
        expected_backpack_tax = Cart.calculate_tax_value(expected_backpack_price)

        all_items.add_product_to_cart_by_name("Sauce Labs Bolt T-Shirt")
        expected_t_shirt_price = all_items.return_price_by_product_name("Sauce Labs Bolt T-Shirt")
        expected_t_shirt_tax = Cart.calculate_tax_value(expected_t_shirt_price)

        all_items.add_product_to_cart_by_name("Sauce Labs Bike Light")
        expected_bike_light_price = all_items.return_price_by_product_name("Sauce Labs Bike Light")
        expected_bike_light_tax = Cart.calculate_tax_value(expected_bike_light_price)

        expected_totalnet_value = round(float(expected_backpack_price) + float(expected_t_shirt_price) + float(expected_bike_light_price),2)
        expected_tax_value = round(float(expected_backpack_tax) + float(expected_t_shirt_tax) + float(expected_bike_light_tax),2)
        expected_total_value = round(expected_totalnet_value + expected_tax_value,2)

        all_items.open_cart()
        cart = Cart(driver)
        cart.checkout_from_cart_view()
        cart.enter_checkout_credentials_and_continue()

        actual_totalnet_value = cart.return_cart_totalnet_value()
        actual_totaltax_value = cart.return_cart_totaltax_value()
        actual_total_value = cart.return_cart_total_value()

        cart.assert_value_in_text(expected_totalnet_value, actual_totalnet_value)
        cart.assert_value_in_text(expected_tax_value, actual_totaltax_value)
        cart.assert_value_in_text(expected_total_value, actual_total_value)