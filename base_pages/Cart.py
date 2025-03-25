from selenium import webdriver
from selenium.webdriver.common.by import By


class Cart:
    shopping_cart_loc = (By.XPATH, "//a[@class='shopping_cart_link']")
    cart_continue_shopping_button = (By.XPATH, "//button[id='continue-shopping']")
    cart_checkout_button = (By.XPATH, "//button[@id='checkout']")
    checkout_first_name_loc = (By.XPATH, "//input[@id='first-name']")
    checkout_last_name_loc = (By.XPATH, "//input[@id='last-name']")
    checkout_zip_postal_code_loc = (By.XPATH, "//input[@id='postal-code']")
    checkout_continue_button_loc = (By.XPATH, "//input[@id='continue']")
    finish_checkout_button = (By.XPATH, "//button[@id='finish']")
    cancel_checkout_button = (By.XPATH, "//button[@id='cancel']")

    def __init__(self, driver):
        self.driver = driver

    # Your Cart
    def continue_shopping_from_cart_view(self):
        self.driver.find_element(self.cart_continue_shopping_button).click()

    def click_checkout_from_cart_view(self):
        self.driver.find_element(*self.cart_checkout_button).click()

    # Checkout: Your Information
    def _enter_first_name(self, first_name="Jan"):
        self.driver.find_element(*self.checkout_first_name_loc).send_keys(first_name)

    def _enter_last_name(self, last_name="Kowalski"):
        self.driver.find_element(*self.checkout_last_name_loc).send_keys(last_name)

    def _enter_zip_postal_code(self, zip_postal_code="000-01"):
        self.driver.find_element(*self.checkout_zip_postal_code_loc).send_keys(zip_postal_code)

    def _click_continue_from_checkout_view(self):
        self.driver.find_element(*self.checkout_continue_button_loc).click()

    def enter_checkout_credentials_and_continue(self):
        self._enter_first_name()
        self._enter_last_name()
        self._enter_zip_postal_code()
        self._click_continue_from_checkout_view()

    def cancel_checkout(self):
        self.driver.find_element(*self.cancel_checkout_button).click()

    # Checkout: Overview
    def finish_checkout(self):
        self.driver.find_element(*self.finish_checkout_button).click()



