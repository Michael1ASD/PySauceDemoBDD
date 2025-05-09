import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage

class ExpandedList(BasePage):
    burger_open_button = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    burger_close_button = (By.XPATH, "//button[@id='react-burger-cross-btn']")

    def _expand_burger(self):
        self.wait_for_element_and_click(*self.burger_open_button)

    def _collapse_burger(self):
        self.wait_for_element_and_click(*self.burger_close_button)

    @allure.step("Select option from burger menu")
    def _select_option_from_burger(self,option_key: str):
        """
        :param option_key: "All Items", "Logout", "Reset App State"

        """

        options = {"All Items" : (By.XPATH, "//a[@id='inventory_sidebar_link']]"),
                   "Logout" : (By.XPATH, "//a[@id='logout_sidebar_link']"),
                   "Reset App State" : (By.XPATH, "//a[@id='reset_sidebar_link']")
        }

        self.wait_for_element_and_click(*options[option_key])

    @allure.step("Go to All items")
    def display_all_items(self):
        self._expand_burger()
        self._select_option_from_burger("All Items")

    @allure.step("Logout")
    def logout(self):
        self.reset_app_state()
        self._select_option_from_burger("Logout")

    @allure.step("Reset app state")
    def reset_app_state(self):
        self._expand_burger()
        self._select_option_from_burger("Reset App State")