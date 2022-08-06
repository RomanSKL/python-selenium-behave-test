from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then

SEARCH_INPUT1 = (By.ID, 'hubHelpSearchInput')


@given('Open Amazon Help page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Search1 for Cancel order')
def search_amazon(context):
    context.driver.find_element(*SEARCH_INPUT1).send_keys('Cancel order', Keys.ENTER)






