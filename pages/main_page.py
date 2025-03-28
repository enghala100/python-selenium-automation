from pages.base_page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):
    SEARCH_FIELD = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']")
    def open_main_page(self):
        self.open_url(self.base_url)
        self.wait_until_clickable(*self.SEARCH_FIELD)