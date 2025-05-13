from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage


class AllItems(BasePage):
    shopping_cart_counter = (By.XPATH, "//span[@class='shopping_cart_badge']")
    shopping_cart_loc = (By.XPATH, "//a[@class='shopping_cart_link']")


    def open_all_items_page(self):
        self.driver.get("https://www.saucedemo.com/inventory.html")

    def verify_cart_is_empty(self):
        is_invisible = WebDriverWait(self.driver, 1).until(EC.invisibility_of_element_located(self.shopping_cart_counter))
        assert is_invisible, f"Cart is not empty"

    def open_cart(self):
        self.click(*self.shopping_cart_loc)

    def add_product_to_cart_by_name(self, product_name: str):
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

    def enter_product_details_by_name(self, product_name: str):
        """
        Opens product details based on its name displayed on the page.

        Args:
            product_name (str): The name of the product as displayed in the inventory items.
                                It should match exactly with the displayed text in the application.

        Example:
            item = AllItems(driver)
            item.add_product_to_cart_by_name("Sauce Labs Backpack")
        """

        product_name_xpath = f"//div[@class='inventory_item_name ' and text()='{product_name}']"
        product_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, product_name_xpath)))
        product_element.click()

    def return_price_by_product_name(self, product_name: str) -> str:
        """
        Retrieves the price of a product based on its name.

        The method searches for the product element on the page using the product name,
        then locates and returns the price text associated with that product.

        Args:
            product_name (str): The name of the product to look for.

        Returns:
            str: The price of the product, e.g., "$29.99".

        Raises:
            TimeoutException: If the product is not found within the specified wait time.
        """

        product_name_xpath = f"//div[@class='inventory_item_name ' and text()='{product_name}']"
        product_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, product_name_xpath)))
        price_element = product_element.find_element(By.XPATH, ".//ancestor::div[@class='inventory_item']//div[@class='inventory_item_price']")
        price_element_text = price_element.text
        clean_price_element_text = price_element_text.replace("$","")
        return clean_price_element_text

