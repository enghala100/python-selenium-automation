from pages.base_page import Page
from selenium.webdriver.common.by import By

class SignInPage(Page):
    SIGN_IN_TEXT = (By.XPATH, "//*[text()='Sign into your Target account']")

    def verify_sign_in_form(self):
        actual_text = self.driver.find_element(*self.SIGN_IN_TEXT).text
        expected_text = 'Sign into your Target account'
        assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'