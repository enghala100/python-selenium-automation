from selenium.webdriver.common.by import By
from pages.base_page import Page

class CartPage(Page):
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    def cart_text(self):
        actual_text = self.driver.find_element(*self.EMPTY_CART_TEXT).text
        expected_text = 'Your cart is empty'
        assert actual_text == expected_text, f'Error. Text {expected_text} not in {actual_text}'