import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    #Element handlers
    @allure.step("Wait for element and find it")
    def find_element(self, by, value):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, value)))

    @allure.step("Click element")
    def click(self, by, value):
        element = self.find_element(by, value)
        element.click()

    @allure.step("Input text")
    def input_text(self, by, value, text):
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(text)

    @allure.step("Wait for element, find it and clear")
    def wait_for_element_and_clear(self,by,value,timeout=5):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, value))).clear()


    @allure.step("Wait for element, find it and click")
    def wait_for_element_and_click(self,by,value,timeout=5, poll_frequency=0.25):
        WebDriverWait(self.driver, timeout, poll_frequency).until(EC.element_to_be_clickable((by, value))).click()

    @allure.step("Wait for an alert and accept")
    def wait_for_alert_and_accept(self,timeout=5):
        alert = WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        alert.accept()

    def get_element_text(self,by,value):
        """
        Retrieves the text value of a web element.

        :param driver: Selenium WebDriver instance
        :param locator: Tuple with strategy and locator, e.g., (By.ID, 'element_id')
        :return: Text content of the element
        """
        element = self.driver.find_element(by, value)
        return element.text


    #Assertions
    @allure.step("Assert element is visible")
    def assert_element_visible(self,by,value,timeout=10,poll_frequency=0.25):
        try:
            webelement = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.presence_of_element_located((by, value))
            )
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.visibility_of(webelement)
            )
        except Exception as e:
            assert False, f"Element with locator ({by}, {value}) not visible: {str(e)}"

    @staticmethod
    def assert_value_in_text(value,text):
        value_str = str(value)
        if value_str not in text:
            raise AssertionError(f"Value '{value_str}' not included in the text '{text}'.")

