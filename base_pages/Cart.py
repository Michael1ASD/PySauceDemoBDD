from selenium import webdriver
from selenium.webdriver.common.by import By


class Cart:
    shopping_cart_loc = (By.XPATH, "//a[@class='shopping_cart_link']")
    continue_shopping_button = (By.XPATH, "//button[id='continue-shopping']")
    checkout_button = (By.XPATH, "//button[id='checkout']")

    def __init__(self, driver):
        self.driver = driver

    def continue_shopping(self, username):
        username_loc = (By.XPATH, "//input[@id='user-name']")
        self.driver.find_element(self.continue_shopping_button).click()

    def checkout(self, username):
        username_loc = (By.XPATH, "//input[@id='user-name']")
        self.driver.find_element(self.checkout_button).click()
#
#     def enter_login(self, username):
#         username_loc = (By.XPATH, "//input[@id='user-name']")
#         self.driver.find_element(*username_loc).clear()
#         self.driver.find_element(*username_loc).send_keys(username)
#
#     def enter_password(self, password):
#         password_loc = (By.XPATH, "//input[@id='password']")
#         self.driver.find_element(*password_loc).clear()
#         self.driver.find_element(*password_loc).send_keys(password)
#
#     def click_login(self):
#         login_button = (By.XPATH, "//input[@id='login-button']")
#         self.driver.find_element(*login_button).click()
#
#     def login(self, username, password):
#         self.enter_login(username)
#         self.enter_password(password)
#         self.click_login()
#
#
# #LOCATORS
# BASE_URL = 'https://www.saucedemo.com/'
# USERNAME_FIELD_LOC = (By.XPATH, "//input[@id='user-name']")
# PASSWORD_FIELD_LOC = (By.XPATH, "//input[@id='password']")
# LOGIN_PAGE_BANNER_LOC = (By.XPATH, "//div[@class='login_logo']")
# LOGIN_PAGE_TITLE_EXPECTED = 'Swag Labs'
# LOGIN_BUTTON_LOC = (By.XPATH, "//input[@id='login-button']")
# APP_LOGO_LOC = (By.XPATH, "//div[@class='app_logo']")
# APP_LOGO_EXPECTED = 'Swag Labs'
# ERROR_WRONG_LOGIN_EXPECTED = 'Epic sadface: Username and password do not match any user in this service'
# ERROR_LOC = (By.CSS_SELECTOR, "h3[data-test='error']")
# SHOPPING_CART_NUMBER_LOC = (By.XPATH, "//span[@class='shopping_cart_badge']")
# LEFT_MENU_BURGER_OPEN_BUTTON = (By.XPATH, "//button[@id='react-burger-menu-btn']")
# LEFT_MENU_BURGER_CLOSE_BUTTON = (By.XPATH, "//button[@id='react-burger-cross-btn']")
# LOGOUT_BUTTON = (By.XPATH, "//a[@id='logout_sidebar_link']")
# ALL_ITEMS_BUTTON = (By.XPATH, "//a[@id='inventory_sidebar_link']")
# shopping_cart_loc = (By.XPATH, "//a[@class='shopping_cart_link']")
# LEFT_MENU_BURGER_RESET_APP_STATUS_BUTTON = (By.XPATH, "//a[@id='reset_sidebar_link']")
# SORT_PRODUCTS_DROPDOWN = (By.XPATH, "//select[@class='product_sort_container']")
# FACEBOOK_LOGO_LOC = (By.XPATH, "//a[@data-test = 'social-facebook']")
# X_LOGO_LOC = (By.XPATH, "//a[@data-test = 'social-twitter']")
# LINKEDIN_LOGO_LOC = (By.XPATH, "//a[@data-test = 'social-linkedin']")
#
# SORTING_METHODS_DICT = {"NAME ASC" : "Name (A to Z)", "NAME DESC" : "Name (Z to A)", "PRICE ASC" : "Price  (low to high)", "PRICE DESC" : "Price  (high to low)"}