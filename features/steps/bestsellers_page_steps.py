from behave import *
from selenium.webdriver.common.by import By
from time import sleep


TOP_LINKS = (By.CSS_SELECTOR, '#zg_header a')
HEADER = (By.CSS_SELECTOR, '#zg_banner_text')


@given('Open Best Sellers')
def open_amazon_best_seller(context):
    # context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
    context.app.bestsellers_page.open_bestsellers()


@then('Confirm {expected_amount} best sellers links')
def verify_best_sellers_links_(context, expected_amount):
    # best_sellers_links = context.driver.find_elements(*TOP_LINKS)
    # assert len(best_sellers_links) == int(expected_amount), f'Expected {expected_amount} links, but got {len(best_sellers_links)}'
    context.app.bestsellers_page.verify_links_preset(expected_amount)


@then('User can click through top links and verify correct page opens')
def click_thru_top(context):
    top_links = context.driver.find_elements(*TOP_LINKS)  # [WebEl1, WebEl2, WebEl3,...]

    for x in range(len(top_links)):  # From 0 to 4
        link_to_click = context.driver.find_elements(*TOP_LINKS)[x]  # page reloading every time you click on link
        link_text = link_to_click.text
        link_to_click.click()
        sleep(1)
        header_text = context.driver.find_element(*HEADER).text
        assert link_text in header_text, f'Expected {link_text} to be in {header_text}'