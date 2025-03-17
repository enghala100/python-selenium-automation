from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CART_ICON=(By.CSS_SELECTOR, "[data-test='@web/CartLink']")
SIGN_IN_BTN=(By.CSS_SELECTOR,"[data-test='@web/AccountLink']")
SIGN_IN_BTN2=(By.XPATH, "//button[@data-test='accountNav-signIn']")
SEARCH_FIELD=(By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']")
SEARCH_BTN=(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
ADD_CART_BTN=(By.CSS_SELECTOR,'.sc-4df0f72b-2')
ADD_CART_BTN2=(By.CSS_SELECTOR,"[data-test='content-wrapper'] [data-test='orderPickupButton']")
ADD_CART_TEXT=(By.XPATH,'//span[@class="h-text-lg"]')


@given('Open target page')
def open_target_page(context):
    context.driver.get('https://www.target.com/')


@when('click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(5)


@when('click on sign in button')
def click_sign_in_button(context):
    context.driver.find_element(*SIGN_IN_BTN).click()
    sleep(3)
    context.driver.find_element(*SIGN_IN_BTN2).click()
    sleep(5)


@when('search for {product}')
def search_for_product(context, product):
    sleep(2)
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    context.driver.find_element(*SEARCH_BTN).click()


@when('click on add to cart button')
def click_add_cart_button(context):
    sleep(15)
    context.driver.find_element(*ADD_CART_BTN).click()
    sleep(1)
    context.driver.find_element(*ADD_CART_BTN2).click()


@then("verify 'added to cart' text is shown")
def verify_add_cart_text(context):
    sleep(5)
    element =context.driver.find_elements(*ADD_CART_TEXT)
    actual_text = element[1].text
    expected_text='Added to cart'
    assert actual_text == expected_text, f'Error. Text {expected_text} not in {actual_text}'