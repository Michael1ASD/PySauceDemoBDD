import unittest
from unittest.mock import MagicMock
from pages.Cart import Cart

class TestClass(unittest.TestCase):
    def test_return_cart_totalnet_value(self):
        driver_mock = MagicMock()
        obj = Cart(driver_mock)
        obj.get_element_text = MagicMock(return_value="123.45")
        result = obj.return_cart_totalnet_value()
        self.assertEqual(result, "123.45")

if __name__ == '__main__':
    unittest.main()