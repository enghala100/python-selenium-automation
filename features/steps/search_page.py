from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep



ADD_CART_BTN=(By.CSS_SELECTOR,'.sc-4df0f72b-2')
ADD_CART_BTN2=(By.CSS_SELECTOR,"[data-test='content-wrapper'] [data-test='orderPickupButton']")
ADD_CART_TEXT=(By.XPATH,'//span[@class="h-text-lg"]')
CHECK_MARK = (By.CSS_SELECTOR, "[href='/icons/Checkmark.svg#Checkmark']")
#ADD_CART_TEXT=(By.CSS_SELECTOR,"[data-test='modal-drawer-heading'] .h-text-lg")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')
PRODUCT_PRICE=(By.CSS_SELECTOR, "[data-test='current-price']")

@then('verify user can see the {expected_text}')
def user_see_product(context, expected_text):
    context.app.search_results_page.verify_search_results(expected_text)

@then('Verify {expected_text} in URL')
def verify_results_url(context, expected_text):
    context.app.search_results_page.verify_results_url(expected_text)


@when('click on add to cart button')
def click_add_cart_button(context):
    context.driver.wait.until(EC.element_to_be_clickable(ADD_CART_BTN))
    context.driver.execute_script("window.scrollTo(0, 500);")
    sleep(8)
    context.app.search_results_page.click_add_cart_button()
    context.driver.wait.until(EC.element_to_be_clickable(ADD_CART_BTN2))
    context.app.search_results_page.click_add_cart_button2()


@then("verify 'added to cart' text is shown")
def verify_add_cart_text(context):
    context.driver.wait.until(EC.visibility_of_element_located(CHECK_MARK))
    element =context.driver.find_elements(*ADD_CART_TEXT)
    actual_text =element[1].text
    expected_text='Added to cart'
    assert actual_text == expected_text, f'Error. Text {expected_text} not in {actual_text}'


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    # context.driver.execute_script("window.scrollBy(0,2000)", "")
    # sleep(2)
    # context.driver.execute_script("window.scrollBy(0,1000)", "")
    # sleep(2)

    products = context.driver.find_elements(*LISTINGS)[:8]  # [WebEl1, WebEl2, WebEl3, WebEl4]

    for product in products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        print(title)
        product.find_element(*PRODUCT_IMG)
        product.find_element(*PRODUCT_PRICE)

@when('Hover favorites icon')
def hover_fav_icon(context):
    context.app.search_results_page.hover_fav_icon()


@then('Favorites tooltip is shown')
def verify_fav_tooltip(context):
    context.app.search_results_page.verify_fav_tooltip()