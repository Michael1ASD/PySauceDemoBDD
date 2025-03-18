from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Assertion:

    def __init__(self, driver):
        self.driver = driver

    def assert_element_visible(self, locator):
        try:
            webelement = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of(webelement)
            )
            assert webelement.is_displayed(), "Element is not visible"
        except Exception as e:
            assert False, f"Element could not be found or is not visible: {str(e)}"