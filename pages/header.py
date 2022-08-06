from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from pages.base_page import Page


class Header(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    SEARCH_INPUT3 = (By.CSS_SELECTOR, 'span.nav-cart-icon.nav-sprite')
    RETURNS_AND_ORDERS = (By.CSS_SELECTOR, "a[href='/gp/css/order-history?ref_=nav_orders_first']")
    FLAG = (By.CSS_SELECTOR, '.icp-nav-flag-us')
    SPANISH_LANG = (By.CSS_SELECTOR, "[href='#switch-lang=es_US']")
    DEPARTMENT_SELECT = (By.ID, 'searchDropdownBox')
    DEPARTMENT_SUB_NAV = (By.CSS_SELECTOR, "[data-category='{SUBSTRING}']")

    def get_dept_sub_nav_locator(self, department):
        return [self.DEPARTMENT_SUB_NAV[0], self.DEPARTMENT_SUB_NAV[1].replace('{SUBSTRING}', department)]

    def search_amazon(self, any_word):
        self.input_text(any_word, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)

    def click_cart_icon(self):
        self.click(*self.SEARCH_INPUT3)

    def click_orders_link(self):
        self.click(*self.RETURNS_AND_ORDERS)

    def hover_lang(self):
        actions = ActionChains(self.driver)
        flag = self.find_element(*self.FLAG)
        actions.move_to_element(flag)
        actions.perform()

    def verify_spanish_lang(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)

    def select_dept(self, alias):
        department_select = self.find_element(*self.DEPARTMENT_SELECT)
        select = Select(department_select)
        select.select_by_value(f'search-alias={alias}')

    def verify_department(self, department):
        department_locator = self.get_dept_sub_nav_locator(department)
        self.wait_for_element_appear(*department_locator)

