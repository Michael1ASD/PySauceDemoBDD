from selenium import webdriver
from selenium.webdriver.common.by import By


class Cart:
    shopping_cart_loc = (By.XPATH, "//a[@class='shopping_cart_link']")
    continue_shopping_button = (By.XPATH, "//button[id='continue-shopping']")
    checkout_button = (By.XPATH, "//button[id='checkout']")

    def __init__(self, driver):
        self.driver = driver

    def continue_shopping(self):
        self.driver.find_element(self.continue_shopping_button).click()

    def checkout(self):
        self.driver.find_element(self.checkout_button).click()