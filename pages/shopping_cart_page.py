from selenium.webdriver.common.by import By
from pages.base_page import Page


class ShoppingCartPage(Page):
    SEARCH_RESULT_TEXT3 = (By.CSS_SELECTOR, "div.a-row.sc-your-amazon-cart-is-empty")

    def shopping_cart(self, enter):
        self.verify_text(enter, *self.SEARCH_RESULT_TEXT3)
