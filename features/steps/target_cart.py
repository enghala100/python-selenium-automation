from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


EMPTY_CART_TEXT=(By.CSS_SELECTOR,"[data-test='boxEmptyMsg']")



@then('your cart is empty message is shown')
def check_cart_is_empty(context):
    actual_text=context.driver.find_element(*EMPTY_CART_TEXT).text
    expected_text='Your cart is empty'
    assert actual_text == expected_text, f'Error. Text {expected_text} not in {actual_text}'


