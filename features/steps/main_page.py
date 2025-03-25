from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


CART_ICON=(By.CSS_SELECTOR, "[data-test='@web/CartLink']")
SIGN_IN_BTN=(By.CSS_SELECTOR,"[data-test='@web/AccountLink']")
SIGN_IN_BTN2=(By.XPATH, "//button[@data-test='accountNav-signIn']")
SEARCH_FIELD=(By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']")
SEARCH_BTN=(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")



@given('Open target page')
def open_target_page(context):
    context.driver.get('https://www.target.com/')


@when('click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()



@when('click on sign in button')
def click_sign_in_button(context):
    context.driver.wait.until(EC.presence_of_element_located(SIGN_IN_BTN),
    message='sign in button not found')
    context.driver.find_element(*SIGN_IN_BTN).click()
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_BTN2),
    message='sign in button2 not found')
    context.driver.find_element(*SIGN_IN_BTN2).click()



@when('search for {product}')
def search_for_product(context, product):
    context.driver.wait.until(EC.presence_of_element_located(SEARCH_FIELD),
    message='search field not found')
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    context.driver.find_element(*SEARCH_BTN).click()


