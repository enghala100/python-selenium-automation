from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
PRODUCT_TEXT=(By.XPATH, "//div[@data-test='lp-resultsCount']")
ADD_CART_BTN=(By.CSS_SELECTOR,'.sc-4df0f72b-2')
ADD_CART_BTN2=(By.CSS_SELECTOR,"[data-test='content-wrapper'] [data-test='orderPickupButton']")
ADD_CART_TEXT=(By.XPATH,'//span[@class="h-text-lg"]')
CHECK_MARK = (By.CSS_SELECTOR, "[href='/icons/Checkmark.svg#Checkmark']")
#ADD_CART_TEXT=(By.CSS_SELECTOR,"[data-test='modal-drawer-heading'] .h-text-lg")

@then('verify user can see the {expected_text}')
def user_see_product(context, expected_text):
    actual_text = context.driver.find_element (*PRODUCT_TEXT).text
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'


@when('click on add to cart button')
def click_add_cart_button(context):
    context.driver.wait.until(EC.element_to_be_clickable(ADD_CART_BTN))
    context.driver.execute_script("window.scrollTo(0, 500);")
    context.driver.find_element(*ADD_CART_BTN).click()
    context.driver.wait.until(EC.element_to_be_clickable(ADD_CART_BTN2))
    context.driver.find_element(*ADD_CART_BTN2).click()


@then("verify 'added to cart' text is shown")
def verify_add_cart_text(context):
    context.driver.wait.until(EC.visibility_of_element_located(CHECK_MARK))
    element =context.driver.find_elements(*ADD_CART_TEXT)
    actual_text =element[1].text
    expected_text='Added to cart'
    assert actual_text == expected_text, f'Error. Text {expected_text} not in {actual_text}'


