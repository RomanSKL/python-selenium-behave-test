from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultPage(Page):
    SEARCH_RESULT_TEXT1 = (By.XPATH, "//span[@class='a-color-state a-text-bold']")

    def verify_search_results(self, search_result):
        self.verify_text(search_result, *self.SEARCH_RESULT_TEXT1)

