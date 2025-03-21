from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Handlers:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_and_clear(self,element,timeout=5):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(element)).clear()

    def wait_for_element_and_click(self,element,timeout=5, poll_frequency=0.25):
        WebDriverWait(self.driver, timeout, poll_frequency).until(EC.element_to_be_clickable(element)).click()

