from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    def verify_sign_in_opened(self):
        self.verify_url_contains_query('https://www.amazon.com/ap/signin')


    # context.driver.wait.until(
    #     EC.url_contains('https://www.amazon.com/ap/signin'),
    #     message='Sign in page never opened'