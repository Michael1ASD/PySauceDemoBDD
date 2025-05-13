import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from configurations.config import LOGIN_URL, VALID_USERNAME, VALID_PASSWORD
from pages.Cart import Cart
from pages.LoginPage import LoginPage
from pages.AllItems import AllItems
from pages.ExpandedList import ExpandedList
from pages.BasePage import BasePage
from pages.ProductDetails import ProductDetails

class TestProducts():

    @allure.feature('Product details')
    @allure.story('Add product to cart from product details')
    def test_add_product_to_cart_from_product_details(self,driver,login):
        expected_confirmation_element = (By.XPATH, "//h2[text()='Thank you for your order!']")

        all_items = AllItems(driver)
        all_items.verify_cart_is_empty()
        all_items.enter_product_details_by_name("Sauce Labs Fleece Jacket")

        product_details = ProductDetails(driver)
        product_details.add_product_to_cart()

        all_items.open_cart()
        cart = Cart(driver)
        cart.checkout_from_cart_view()
        cart.enter_checkout_credentials_and_continue()
        cart.finish_checkout()

        cart.assert_element_visible(*expected_confirmation_element)


