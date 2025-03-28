from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


CELLS=(By.CSS_SELECTOR,'.cell-item-content')



@given('Open target circle page')
def open_circle_page(context):
    context.driver.get('https://www.target.com/circle')
    context.driver.wait.until(
        EC.visibility_of_element_located(CELLS),
        message='cells not found')



@then('verify User can see at lease {cells_amount} cells in circle page')
def user_see_circle_page_cells(context, cells_amount):
    cells=context.driver.find_elements(*CELLS)
    cells_amount=int(cells_amount)
    assert cells_amount <= len(cells),f'{cells_amount} cells should be greater than {cells} cells'
