from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ExpandedList:

    def __init__(self, driver):
        self.driver = driver

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
        options = {"logout_button" : (By.XPATH, "//a[@id='logout_sidebar_link']"),
                   "all_items_button" : (By.XPATH, "//a[@id='inventory_sidebar_link']"),
                   "reset_app_status_button" : (By.XPATH, "//a[@id='reset_sidebar_link']")
        }

        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(options[option_key])).click()

    def logout(self):
        self.expand_burger()
        self.select_option_from_burger("logout_button")

    def reset_app_state(self):
        self.expand_burger()
        self.select_option_from_burger("reset_app_status_button")



# BASE_URL = 'https://www.saucedemo.com/'
# USERNAME_FIELD_LOC = (By.XPATH, "//input[@id='user-name']")
# PASSWORD_FIELD_LOC = (By.XPATH, "//input[@id='password']")
# LOGIN_PAGE_BANNER_LOC = (By.XPATH, "//div[@class='login_logo']")
# LOGIN_PAGE_TITLE_EXPECTED = 'Swag Labs'
# LOGIN_BUTTON_LOC = (By.XPATH, "//input[@id='login-button']")

# ERROR_WRONG_LOGIN_EXPECTED = 'Epic sadface: Username and password do not match any user in this service'
# ERROR_LOC = (By.CSS_SELECTOR, "h3[data-test='error']")
# SHOPPING_CART_NUMBER_LOC = (By.XPATH, "//span[@class='shopping_cart_badge']")



# SHOPPING_CART_LOC = (By.XPATH, "//a[@class='shopping_cart_link']")
# SORT_PRODUCTS_DROPDOWN = (By.XPATH, "//select[@class='product_sort_container']")
# FACEBOOK_LOGO_LOC = (By.XPATH, "//a[@data-test = 'social-facebook']")
# X_LOGO_LOC = (By.XPATH, "//a[@data-test = 'social-twitter']")
# LINKEDIN_LOGO_LOC = (By.XPATH, "//a[@data-test = 'social-linkedin']")
#
# SORTING_M