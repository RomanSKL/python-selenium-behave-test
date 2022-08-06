from behave import given, when, then, step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "#inline-twister-expander-content-color_name li[class*='desktop']")
COLOR_NAME = (By.ID, 'inline-twister-expanded-dimension-text-color_name')

PRODUCT = (By.CSS_SELECTOR, "#inline-twister-expander-content-color_name li[class*='desktop']")
COLORS = (By.ID, 'inline-twister-expanded-dimension-text-color_name')
PRODUCT2 = (By.CSS_SELECTOR, "#inline-twister-expander-content-color_name li[class*='desktop']")
COLORS2 = (By.ID, 'inline-twister-expanded-dimension-text-color_name')


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

    #  for option in color_options[:3]:


@given('Open Jeans {product} page')
def open_jeans_page(context, product):
    context.driver.get(f'https://www.amazon.com/dp/{product}/')


@then('Verify ability to select colors')
def select_colors(context):
    expected_result = ['Light Wash', 'Black', 'Blue, Over Dye', 'Bright White']
    actual_result = []

    jeans = context.driver.find_element(*PRODUCT)
    for i in jeans[:4]:
        context.driver.wait.until(EC.element_to_be_clickable(PRODUCT), message='Some Option not clickable')
        i.click()
        # sleep(1)
        names = context.driver.find_element(*COLORS).text
        actual_result += [names]

    assert actual_result == expected_result, f'ERROR! Expected {expected_result}, but we got {actual_result}'


@given('Open sweater page')
def sweater_page(context):
    context.driver.get('https://www.amazon.com/dp/B081YS2F7N?th=1&psc=1')


@then('Verify user able to select colors')
def colors(context):
    expected_result = ['Black', 'Army Green', 'Blue']
    actual_result = []

    sweaters = context.driver.find_element(*PRODUCT2)
    for i in sweaters[:3]:
        i.click()
        sleep(1)
        name = context.driver.find_element(*COLORS2).text
        actual_result += [name]
    assert actual_result == expected_result, f'ERROR! Expected {expected_result}, but we got {actual_result}'


