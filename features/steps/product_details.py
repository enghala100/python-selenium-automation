from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")
SELECTED_COLOR_V2 = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent']:nth-child(3)")


@given('Open target product {product_id} page')
def open_target(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(5)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    context.driver.execute_script("window.scrollTo(0, 500);")
    expected_colors = ['Blue Tint', 'Denim Blue', 'Marine', 'Raven']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
    for color in colors:
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'


@then('Verify user can click through product colors')
def click_and_verify_colors(context):
    context.driver.execute_script("window.scrollTo(0, 500);")
    expected_colors = ['black/gum', 'dark khaki', 'grey', 'navy/tan', 'white/navy/red','white/sand/tan']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  #
    for color in colors:
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR_V2).text  # 'Color\nBlack'
        #selected_color=selected_color[2]
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'