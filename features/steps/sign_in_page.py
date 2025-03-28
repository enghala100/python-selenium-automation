from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SIGN_IN_TEXT=(By.XPATH, "//*[text()='Sign into your Target account']")


@then('verify sign in form opened')
def verify_sign_in_form_opened(context):
   context.app.sign_in_page.verify_sign_in_form_opened()