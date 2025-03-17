from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

PRODUCT_TEXT=(By.XPATH, "//div[@data-test='lp-resultsCount']")



@then('verify user can see the {expected_text}')
def user_see_product(context, expected_text):
    actual_text = context.driver.find_element (*PRODUCT_TEXT).text
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'





