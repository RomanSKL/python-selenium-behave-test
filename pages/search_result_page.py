from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultPage(Page):
    SEARCH_RESULT_TEXT1 = (By.XPATH, "//span[@class='a-color-state a-text-bold']")

    def verify_search_results(self, search_result):
        self.verify_text(search_result, *self.SEARCH_RESULT_TEXT1)
    #    actual_result = self.driver.find_element(*self.SEARCH_RESULT_TEXT1).text
    #    assert search_result == actual_result, \
    #        f'Error! Actual text {actual_result} does not match expected {search_result}'
