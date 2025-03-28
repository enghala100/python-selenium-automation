from selenium.webdriver.common.by import By
from pages.base_page import Page

class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SIGN_IN_BTN = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
    SIGN_IN_BTN2 = (By.XPATH, "//button[@data-test='accountNav-signIn']")

    def search(self,product):
        self.input_text(product,*self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)

    def click_cart_icon(self):
        self.click(*self.CART_ICON)


    def click_sign_in_btn(self):
        self.click(*self.SIGN_IN_BTN)

    def click_sign_in_btn2(self):
        self.click(*self.SIGN_IN_BTN2)