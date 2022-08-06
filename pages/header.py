from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from pages.base_page import Page


class Header(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')

    def search_amazon(self, any_word):
        self.input_text(any_word, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)

