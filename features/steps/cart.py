from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


EMPTY_CART_TEXT=(By.CSS_SELECTOR,"[data-test='boxEmptyMsg']")



@then('your cart is empty message is shown')
def check_cart_is_empty(context):
    context.app.cart_page.cart_text()


@then('Verify cart page opens')
def verify_cart_page_opens(context):
    context.app.cart_page.verify_cart_page_opens()



