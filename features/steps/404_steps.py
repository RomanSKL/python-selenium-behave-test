from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


DOG_IMG = (By.CSS_SELECTOR, "#d[alt='Dogs of Amazon']")
PRIVACY_LINK = (By.CSS_SELECTOR, "a[href='https://www.amazon.com/privacy']")


@given('Store original window')
def store_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)  # shows window
    print(context.driver.window_handles)  # shows all windows


@when('Click on a dog image')
def click_img(context):
    context.driver.find_element(*DOG_IMG).click()


@when('Switch to new window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    print("\nAfter click, windows:", context.driver.window_handles)
    all_windows = context.driver.window_handles
    context.driver.switch_to.window(all_windows[1])


@then('Verify blog is opened')
def verify_blog_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.aboutamazon.com/'))


@then('Close blog')
def close_blog(context):
    context.driver.close()


@then('Return to original window')
def return_to_original_window(context):
    context.driver.switch_to.window(context.original_window)
