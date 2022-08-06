from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from pages.base_page import Page


class AmazonFashionPage(Page):
    NEW_ARRIVALS = (By.CSS_SELECTOR, "a[href*='/New-Arrivals/']")
    IMAGE = (By.CSS_SELECTOR, "img[src*='https://m.media-amazon.com/images/']")
    DEPARTMENTS = (By.ID, 'searchDropdownBox')
    SUB_NAV_DEP = (By.CSS_SELECTOR, "[data-category='videogames']")

    def open_amazon_fashion(self):
        self.open_page('gp/product/B074TBCSC8')

    def hover_over_new_arrivals(self):
        actions = ActionChains(self.driver)
        new_arrivals = self.find_element(*self.NEW_ARRIVALS)
        actions.move_to_element(new_arrivals)
        actions.perform()

    def select_department(self):
        select = Select(self.find_element(*self.DEPARTMENTS))
        select.select_by_value('search-alias=videogames')

    def verify_image(self):
        self.wait_for_element_appear(*self.IMAGE)

    def verify_selected_department(self):
        self.wait_for_element_appear(*self.SUB_NAV_DEP)
