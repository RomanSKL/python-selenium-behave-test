from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_RESULT_TEXT1 = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
SEARCH_RESULT_TEXT2 = (By.XPATH, "//*[text()='Cancel Items or Orders']")
#SEARCH_RESULT_TEXT3 = (By.CSS_SELECTOR, "div.a-row.sc-your-amazon-cart-is-empty")


@then('Verify search results for coffee are shown')  # ('Verify search results for {expected_result} are shown')
def verify_search_results(context):  # (context, expected_result)
    expected_result = '"coffee"'  # remove the row
    actual_result = context.driver.find_element(*SEARCH_RESULT_TEXT1).text
    assert expected_result == actual_result, f'Error! Actual text {actual_result} does not match expected {expected_result}'


@then('Verify that ‘Cancel Items or Orders’ text is present')
def verify_search_results(context):
    expected_result = 'Cancel Items or Orders'
    actual_result = context.driver.find_element(*SEARCH_RESULT_TEXT2).text
    assert expected_result == actual_result, f'Error! Actual text {actual_result} does not match expected {expected_result}'


@then('Verify that1 {enter}')
def shopping_cart(context, enter):
    #expected_result = 'Your Amazon Cart is empty'
    #actual_result = context.driver.find_element(*SEARCH_RESULT_TEXT3).text
    #assert expected_result == actual_result, f'Error! Actual text {actual_result} does not match expected {expected_result}'
    context.app.shopping_cart_page.shopping_cart(enter)


@then('Verify search results for {search_result} are shown')
def verify_search_results(context, search_result):
   # actual_result = context.driver.find_element(*SEARCH_RESULT_TEXT1).text
   # assert search_result == actual_result, f'Error! Actual text {actual_result} does not match expected {search_result}'
   context.app.search_result_page.verify_search_results(search_result)


