from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class ProductDetails(BasePage):
    add_to_cart_button = (By.XPATH, "//button[@id='add-to-cart']")
    remove_from_cart_button = (By.XPATH, "//button[@id='remove']")

    def add_product_to_cart(self):
        self.wait_for_element_and_click(*self.add_to_cart_button)

    def remove_product_from_cart(self):
        self.wait_for_element_and_click(*self.remove_from_cart_button)
