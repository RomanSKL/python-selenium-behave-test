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



# HW6 Scenario 2


@given('Open Amazon T&C page')
def open_privacy_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)
    print(context.driver.window_handles)


@when('Click on Amazon Privacy Notice link')
def click_privacy_link(context):
    context.driver.find_element(*PRIVACY_LINK).click()


@when('Switch to the newly opened window')
def switch_window2(context):
    context.driver.wait.until(EC.new_window_is_opened)
    print("\nAfter click, windows:", context.driver.window_handles)
    all_windows = context.driver.window_handles
    context.driver.switch_to.window(all_windows[1])


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ'))


@then('User can close new window and switch back to original')
def return_to_window1(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)
