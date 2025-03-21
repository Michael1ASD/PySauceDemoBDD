from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.handlers import Handlers
class ExpandedList:
    burger_open_button = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    burger_close_button = (By.XPATH, "//button[@id='react-burger-cross-btn']")

    def __init__(self, driver):
        self.driver = driver
        self.handlers = Handlers(driver)

    def _expand_burger(self):
        self.driver.find_element(*self.burger_open_button).click()

    def _collapse_burger(self):
        self.driver.find_element(*self.burger_close_button).click()

    def _select_option_from_burger(self,option_key: str):
        """
        :param option_key: "All Items", "Logout", "Reset App State"

        """

        options = {"All Items" : (By.XPATH, "//a[@id='inventory_sidebar_link']]"),
                   "Logout" : (By.XPATH, "//a[@id='logout_sidebar_link']"),
                   "Reset App State" : (By.XPATH, "//a[@id='reset_sidebar_link']")
        }

        self.handlers.wait_for_element_and_click(options[option_key])

    def logout(self):
        self._expand_burger()
        self._select_option_from_burger("Logout")

    def reset_app_state(self):
        self._expand_burger()
        self._select_option_from_burger("Reset App State")