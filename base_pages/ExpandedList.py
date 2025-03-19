from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.handlers import Handlers
class ExpandedList:

    def __init__(self, driver):
        self.driver = driver
        self.handlers = Handlers(driver)

    def expand_burger_list(self):
        burger_open_button = (By.XPATH, "//button[@id='react-burger-menu-btn']")
        self.driver.find_element(*burger_open_button).click()

    def close_burger_list(self):
        burger_close_button = (By.XPATH, "//button[@id='react-burger-cross-btn']")
        self.driver.find_element(*burger_close_button).click()

    def expand_burger(self):
        burger_open_button = (By.XPATH, "//button[@id='react-burger-menu-btn']")
        self.driver.find_element(*burger_open_button).click()

    def collapse_burger(self):
        burger_close_button = (By.XPATH, "//button[@id='react-burger-cross-btn']")
        self.driver.find_element(*burger_close_button).click()

    def select_option_from_burger(self,option_key):
        """
        :param option_key: "logout_button"
                           "all_items_button",
                           "reset_app_status_button"
        """

        options = {"logout_button" : (By.XPATH, "//a[@id='logout_sidebar_link']"),
                   "all_items_button" : (By.XPATH, "//a[@id='inventory_sidebar_link']"),
                   "reset_app_status_button" : (By.XPATH, "//a[@id='reset_sidebar_link']")
        }

        self.handlers.wait_for_element_and_click(options[option_key])

    def logout(self):
        self.expand_burger()
        self.select_option_from_burger("logout_button")

    def reset_app_state(self):
        self.expand_burger()
        self.select_option_from_burger("reset_app_status_button")