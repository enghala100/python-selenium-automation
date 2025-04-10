from selenium.webdriver.common.by import By
from pages.base_page import Page

class CartPage(Page):
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")

    def cart_text(self):
        self.verify_text('Your cart is empty', *self.EMPTY_CART_TEXT)


    def verify_cart_page_opens(self):
        self.verify_url(f'{self.base_url}cart')  # 'https://www.target.com/' + 'cart'