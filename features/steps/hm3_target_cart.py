from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target page')
def open_target_page(context):
    context.driver.get('https://www.target.com/')
sleep(3)


@when('click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()


@then('your cart is empty message is shown')
def check_cart_is_empty(context):
    actual_text=context.driver.find_element(By.CSS_SELECTOR,"[data-test='boxEmptyMsg']").text
    expected_text='Your cart is empty'
    assert actual_text == expected_text, f'Error. Text {expected_text} not in {actual_text}'

@when('click on sign in button')
def click_sign_in_button(context):
    context.driver.find_element(By.CSS_SELECTOR,"[data-test='@web/AccountLink']").click()
    context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
    sleep(5)


@then('verify sign in form opened')
def verify_sign_in_form_opened(context):
    actual_text = context.driver.find_element(By.XPATH, "//*[text()='Sign into your Target account']").text
    expected_text = 'Sign into your Target account'
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'