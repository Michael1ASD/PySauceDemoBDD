import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class Cart(BasePage):
    shopping_cart_loc = (By.XPATH, "//a[@class='shopping_cart_link']")
    cart_continue_shopping_button = (By.XPATH, "//button[id='continue-shopping']")
    cart_checkout_button = (By.XPATH, "//button[@id='checkout']")
    checkout_first_name_loc = (By.XPATH, "//input[@id='first-name']")
    checkout_last_name_loc = (By.XPATH, "//input[@id='last-name']")
    checkout_zip_postal_code_loc = (By.XPATH, "//input[@id='postal-code']")
    checkout_continue_button_loc = (By.XPATH, "//input[@id='continue']")
    finish_checkout_button = (By.XPATH, "//button[@id='finish']")
    cancel_checkout_button = (By.XPATH, "//button[@id='cancel']")


    # Your Cart
    @allure.step("Continue shopping from cart view")
    def continue_shopping_from_cart_view(self):
        self.wait_for_element_and_click(*self.cart_continue_shopping_button)

    @allure.step("Checkout from cart view")
    def click_checkout_from_cart_view(self):
        self.wait_for_element_and_click(*self.cart_checkout_button)
        # self.click(*self.cart_checkout_button)

    # Checkout: Your Information
    def _enter_first_name(self, first_name="Jan"):
        self.input_text(*self.checkout_first_name_loc, first_name)

    def _enter_last_name(self, last_name="Kowalski"):
        self.input_text(*self.checkout_last_name_loc, last_name)

    def _enter_zip_postal_code(self, zip_postal_code="000-01"):
        self.input_text(*self.checkout_zip_postal_code_loc, zip_postal_code)

    def _click_continue_from_checkout_view(self):
        self.wait_for_element_and_click(*self.checkout_continue_button_loc)

    @allure.step("Enter checkout credentials and continue")
    def enter_checkout_credentials_and_continue(self):
        self._enter_first_name()
        self._enter_last_name()
        self._enter_zip_postal_code()
        self._click_continue_from_checkout_view()

    @allure.step("Cancel checkout")
    def cancel_checkout(self):
        self.wait_for_element_and_click(*self.cancel_checkout_button)

    # Checkout: Overview
    @allure.step("Finish checkout")
    def finish_checkout(self):
        self.wait_for_element_and_click(*self.finish_checkout_button)


