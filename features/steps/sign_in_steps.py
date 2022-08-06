from behave import given, when, then, step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


RETURNS_AND_ORDERS = (By.CSS_SELECTOR, "a[href='/gp/css/order-history?ref_=nav_orders_first']")


@when('Click Amazon Orders link')
def click_orders_link(context):
    # context.driver.find_element(*RETURNS_AND_ORDERS).click()
    context.app.header.click_orders_link()


@then('Verify Sign In page is opened')
def verify_sign_in_opened(context):
    #context.driver.wait.until(
    #    EC.url_contains('https://www.amazon.com/ap/signin'),
    #    message='Sign in page never opened'
    #)
    context.app.sign_in_page.verify_sign_in_opened()



