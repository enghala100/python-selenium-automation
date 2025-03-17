from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SIGN_IN_TEXT=(By.XPATH, "//*[text()='Sign into your Target account']")


@then('verify sign in form opened')
def verify_sign_in_form_opened(context):
    actual_text = context.driver.find_element(*SIGN_IN_TEXT).text
    expected_text = 'Sign into your Target account'
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'