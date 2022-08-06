from selenium.webdriver.common.by import By
from pages.base_page import Page


class BestsellersPage(Page):
    TOP_LINKS = (By.CSS_SELECTOR, '#zg_header a')
    HEADER = (By.CSS_SELECTOR, '#zg_banner_text')

    def open_bestsellers(self):
        self.open_page('gp/bestsellers/?ref_=nav_cs_bestsellers')

    def verify_links_present(self, expected_amount):
        best_sellers_links = self.driver.find_elements(*self.TOP_LINKS)
        assert len(best_sellers_links) == int(expected_amount), \
            f'Expected {expected_amount} links, but got {len(best_sellers_links)}'
