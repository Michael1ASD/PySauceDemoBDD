from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Handlers:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_and_click(self,element):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(element)).click()
