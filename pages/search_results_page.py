from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
    ADD_CART_BTN = (By.CSS_SELECTOR, '.sc-4df0f72b-2')
    ADD_CART_BTN2 = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [data-test='orderPickupButton']")

    def verify_search_results(self, expected_text):
        self.verify_partial_text(expected_text, *self.SEARCH_RESULTS_TEXT)

    def verify_results_url(self, expected_partial_url):
         self.verify_partial_url(expected_partial_url)

    def click_add_cart_button(self):
         self.click(*self.ADD_CART_BTN)

    def click_add_cart_button2(self):
        self.click(*self.ADD_CART_BTN2)
