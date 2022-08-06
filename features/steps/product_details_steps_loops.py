from behave import given, when, then, step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "#inline-twister-expander-content-color_name li[class*='desktop']")
COLOR_NAME = (By.ID, 'inline-twister-expanded-dimension-text-color_name')


@given('Open Amazon product {product_id} page')
def open_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@then('Verify user can click through colors')
def verify_clicking_colors(context):
    expected_colors = ['Navy', 'Black', 'Solid Black']
    actual_colors = []

    color_options = context.driver.find_elements(*COLOR_OPTIONS)
    for option in color_options:
        context.driver.wait.until(EC.element_to_be_clickable(COLOR_OPTIONS), message='Some Option not clickable')
        option.click()
        # sleep(1)
        color_name = context.driver.find_element(*COLOR_NAME).text
        actual_colors += [color_name]

    assert actual_colors == expected_colors, f'Error! Expected {expected_colors}, but got {actual_colors}'

