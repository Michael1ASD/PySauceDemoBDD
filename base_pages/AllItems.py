from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AllItems:
    shopping_cart_counter = (By.XPATH, "//span[@class='shopping_cart_badge']")
    shopping_cart_loc = (By.XPATH, "//a[@class='shopping_cart_link']")

    def __init__(self, driver):
        self.driver = driver

    def open_all_items_page(self):
        self.driver.get("https://www.saucedemo.com/inventory.html")

    def verify_cart_is_empty(self):
        is_invisible = WebDriverWait(self.driver, 1).until(EC.invisibility_of_element_located(self.shopping_cart_counter))
        assert is_invisible, f"Cart is not empty"

    def open_cart(self):
        self.driver.find_element(*self.shopping_cart_loc).click()

    def add_product_to_cart_by_name(self, product_name):
        """
        Adds a product to the shopping cart based on its name displayed on the page.

        Args:
            product_name (str): The name of the product as displayed in the inventory items.
                                It should match exactly with the displayed text in the application.

        Example:
            item = AllItems(driver)
            item.add_product_to_cart_by_name("Sauce Labs Backpack")
        """

        product_name_xpath = f"//div[@class='inventory_item_name ' and text()='{product_name}']"
        product_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, product_name_xpath)))
        add_to_cart_button = product_element.find_element(By.XPATH, ".//ancestor::div[@class='inventory_item']//button[contains(text(), 'Add to cart')]")
        add_to_cart_button.click()

    def return_price_by_product_name(self, product_name):
        """
        Adds a product to the shopping cart based on its name displayed on the page.

        Args:
            product_name (str): The name of the product as displayed in the inventory items.
                                It should match exactly with the displayed text in the application.

        Example:
            item = AllItems(driver)
            item.add_product_to_cart_by_name("Sauce Labs Backpack")
        """

        product_name_xpath = f"//div[@class='inventory_item_name ' and text()='{product_name}']"
        product_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, product_name_xpath)))
        price_element = product_element.find_element(By.XPATH, ".//ancestor::div[@class='inventory_item']//div[@class='inventory_item_price']")
        return price_element.text
