from pages.base_page import Page
from selenium.webdriver.common.by import By

class SignInPage(Page):
    SIGN_IN_TEXT = (By.XPATH, "//*[text()='Sign into your Target account']")
    T_AND_C_LINK = (By.XPATH, "//a[text()='Target terms and conditions']")
    SIGN_IN_BTN = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
    SIGN_IN_BTN2 = (By.XPATH, "//button[@data-test='accountNav-signIn']")

    def open_sign_in_page(self):
        self.open_url('https://www.target.com/login)')
        self.click(*self.SIGN_IN_BTN)
        self.click(*self.SIGN_IN_BTN2)

    def click_t_and_c_link(self):
        self.click(*self.T_AND_C_LINK)

    def verify_t_and_c_opened(self):
        self.verify_partial_url('terms-conditions')


    def verify_sign_in_form(self):
        actual_text = self.driver.find_element(*self.SIGN_IN_TEXT).text
        expected_text = 'Sign into your Target account'
        assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'