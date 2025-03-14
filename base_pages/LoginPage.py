from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_login(self, username):
        self.driver.find_element(By.XPATH, "//input[@id='user-name']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, "//input[@id='password']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()