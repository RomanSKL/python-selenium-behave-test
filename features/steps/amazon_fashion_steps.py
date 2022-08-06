from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then, step
from time import sleep


@given('Open Amazon Fashion page')
def open_amazon_fashion(context):
    context.app.amazon_fashion_page.open_amazon_fashion()


@when('Hover over New Arrivals')
def hover_over_new_arrivals(context):
    context.app.amazon_fashion_page.hover_over_new_arrivals()


@when('Select Video Games department')
def select_department(context):
    context.app.amazon_fashion_page.select_department()


@then('Verify images')
def verify_image(context):
    context.app.amazon_fashion_page.verify_image()


@then('Verify user is on Video Games department')
def verify_selected_department(context):
    context.app.amazon_fashion_page.verify_selected_department()
