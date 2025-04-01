from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SIGN_IN_TEXT=(By.XPATH, "//*[text()='Sign into your Target account']")


@then('verify sign in form opened')
def verify_sign_in_form_opened(context):
   context.app.sign_in_page.verify_sign_in_form()


@given('Open sign in page')
def open_sign_in_page(context):
   context.app.sign_in_page.open_sign_in_page()

@when('Click on Target terms and conditions link')
def click_target_terms_and_conditions_link(context):
   sleep(4)
   context.app.sign_in_page.click_t_and_c_link()


@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_page(context):
   context.app.sign_in_page.verify_t_and_c_opened()