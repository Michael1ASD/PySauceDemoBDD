from selenium import webdriver
from selenium.webdriver.common.by import By


class AllItems:

    def __init__(self, driver):
        self.driver = driver

    def open_all_items_page(self, url):
        self.driver.get(url)

    def enter_login(self, username):
        username_loc = (By.XPATH, "//input[@id='user-name']")
        self.driver.find_element(*username_loc).clear()
        self.driver.find_element(*username_loc).send_keys(username)

    def enter_password(self, password):
        password_loc = (By.XPATH, "//input[@id='password']")
        self.driver.find_element(*password_loc).clear()
        self.driver.find_element(*password_loc).send_keys(password)

    def click_login(self):
        login_button = (By.XPATH, "//input[@id='login-button']")
        self.driver.find_element(*login_button).click()

    def logout(self):

        # ARRANGE
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(BASE_URL)
        driver.find_element(*USERNAME_FIELD_LOC).send_keys(USERNAME_VALID)
        driver.find_element(*PASSWORD_FIELD_LOC).send_keys(PASSWORD_VALID)
        driver.find_element(*LOGIN_BUTTON_LOC).click()

        # ACT
        driver.find_element(*LEFT_MENU_BURGER_OPEN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()
        actual_title = driver.title

        # ASSERT
        assert actual_title == LOGIN_PAGE_TITLE_EXPECTED, f"Expected title '{LOGIN_PAGE_TITLE_EXPECTED}', but got '{actual_title}'"

        # TEARDOWN
        driver.quit()


# SORTING_METHODS_DICT = {"NAME ASC" : "Name (A to Z)", "NAME DESC" : "Name (Z to A)", "PRICE ASC" : "Price  (low to high)", "PRICE DESC" : "Price  (high to low)"}