from pages.bestsellers_page import BestsellersPage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_result_page import SearchResultPage
from pages.amazon_fashion_page import AmazonFashionPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.bestsellers_page = BestsellersPage(self.driver)
        self.header = Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.search_result_page = SearchResultPage(self.driver)
        self.amazon_fashion_page = AmazonFashionPage(self.driver)

