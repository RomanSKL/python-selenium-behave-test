from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then, step
from time import sleep


SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
SEARCH_INPUT3 = (By.CSS_SELECTOR, 'span.nav-cart-icon.nav-sprite')

PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
CART = (By.ID, 'nav-cart-count')
PRODUCT_NAME = (By.ID, 'productTitle')

HAM_MENU_BTN = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, 'td.navFooterDescItem a')


SOME_THINGS_LINKS = (By.CSS_SELECTOR, 'div.a-box-inner')


# moved to search_result_steps
# SEARCH_RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")

@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_main_page()
  #   context.driver.get('https://www.amazon.com/')


# @when('Search for coffee')
# def search_amazon(context):
    # context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('coffee')
    # context.driver.find_element(By.ID, 'nav-search-submit-button').click()

@when('Search for {any_word}') # @when('Search for coffee')
def search_amazon(context, any_word):   # def search_amazon(context):
   # context.driver.find_element(*SEARCH_INPUT).send_keys(any_word)  # send_keys('coffee')
   # context.driver.find_element(*SEARCH_BTN).click()
   context.app.header.search_amazon(any_word)


# @then('Verify search results for coffee are shown')
# def verify_search_results(context):
    # expected_result = '"coffee"'
    # actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    # assert expected_result == actual_result, f'Error! Actual text {actual_result} does not match expected {expected_result}'


# moved to search_result_steps
# @then('Verify search results for coffee are shown')
# def verify_search_results(context):
    # expected_result = '"coffee"'
    # actual_result = context.driver.find_element(*SEARCH_RESULT_TEXT).text
    # assert expected_result == actual_result, f'Error! Actual text {actual_result} does not match expected {expected_result}'


@when('Click cart icon')
def click_cart_icon(context):
    # context.driver.find_element(*SEARCH_INPUT3).click()
    context.app.header.click_cart_icon()

# Scenario: User can add a product to the card
@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(1)


@when('Open cart page')
def open_cart_page(context):
    context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')


@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    actual_text = context.driver.find_element(*CART).text
    assert expected_count == actual_text, f'Expected {expected_count}, but got {actual_text}'


@then('Verify hamburger menu btn present')
def verify_ham_menu(context):
    elements = context.driver.find_elements(*HAM_MENU_BTN)
    assert len(elements) == 1, f'Error: Expected 1 item, but got {len(elements)}'


@then('Verify there are {expected_amount} footer links')
def verify_footer_links_count(context, expected_amount):
    expected_amount = int(expected_amount)  # '38' => 38

    footer_links = context.driver.find_elements(*FOOTER_LINKS)  # [Webelement1, Webelement2, ..]

    assert len(footer_links) == expected_amount, f'Expected {expected_amount} links, but got {len(footer_links)}'


# HW4!


'''@when('Store product name')
def get_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Current product: {context.product_name}')


@then('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*PRODUCT_NAME).text
    assert context.product_name == actual_name, f'Expected {context.product_name}, but got {actual_name}'
    assert context.product_name[:30] in actual_name'''


@given('Open Customer Service page')
def open_customer_service_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@then('Confirm {expected_amount} some things you can do here links')
def verify_some_things_links_(context, expected_amount):
    expected_amount = int(expected_amount)
    some_things_links = context.driver.find_elements(*SOME_THINGS_LINKS)
    assert len(some_things_links) == expected_amount, f'Expected {expected_amount} links, but got {len(some_things_links)}'


# Feature: Amazon Sign In tests
SIGN_IN_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-inner")

@when ('Click on button from SignIn popup')
def click_sign_in_btn(context):
    sign_in_btn = context.driver.wait.until(
        EC.element_to_be_clickable(SIGN_IN_BTN), 'Sign in btn not clickable'
    )
    sign_in_btn.click()


SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
PRODUCT_TITLE = (By.CSS_SELECTOR, 'h2 span.a-text-normal')
PRODUCT_IMG = (By.CSS_SELECTOR, ".s-image[data-image-latency='s-product-image']")


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)
    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Error! Title should not be blank'  # <= the same title != ''
        product.find_element(*PRODUCT_IMG)



@then('SignIn popup is present')
def verify_signin_popup_present(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_BTN), 'Sign in btn not clickable')


@when('Wait for {seconds} seconds')
def wait_sec(context, seconds):
    sleep(int(seconds)) # "5" => 5


@then('SignIn popup disappears')
def verify_signin_popup_not_present(context):
    context.driver.wait.until_not(EC.element_to_be_clickable(SIGN_IN_BTN), 'Sign in btn did not disappear')

# Scenario: User can see language options
@when('Hover over language options')
def hover_lang(context):
    context.app.header.hover_lang()


@then('Verify Spanish option present')
def verify_spanish_lang(context):
    context.app.header.verify_spanish_lang()


# Scenario: User can select and search in a department
@when('Select department by {alias}')
def select_dept(context, alias):
    context.app.header.select_dept(alias)


@then('Verify {department} department is selected')
def verify_department(context, department):
    context.app.header.verify_department(department)
