#  import allure
#  from allure_commons.types import AttachmentType
from app.application import Application

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.events import EventFiringWebDriver

from support.logger import logger, MyListener

bs_user = 'romanskliarov_x8pMVg'
bs_pw = 'vnf3qwxD7hzYzkdmzqtD'


def browser_init(context, test_name):

    # context.driver = webdriver.Chrome(executable_path='/Users/skliarovrn/Desktop/GitHub repo/python-selenium-behave-test/chromedriver')
    # context.driver = webdriver.Firefox(executable_path='')
    # context.driver = webdriver.Safari()

    # HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(chrome_options=options, executable_path='/Users/skliarovrn/Desktop/GitHub repo/python-selenium-behave-test/chromedriver')


    context.driver = EventFiringWebDriver(webdriver.Chrome(executable_path='/Users/skliarovrn/Desktop/GitHub repo/python-selenium-behave-test/chromedriver'), MyListener())
    # context.driver = EventFiringWebDriver(webdriver.Chrome(chrome_options=options, executable_path='/Users/skliarovrn/Desktop/GitHub repo/python-selenium-behave-test/chromedriver'), MyListener())

    ### for browerstack ###
    # desired_cap = {
    #     'browser': 'Chrome',
    #     'os_version': 'Monterey',
    #     'os': 'OS X',
    #     'name': test_name
    # }
    # url = f'http://{bs_user}:{bs_pw}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    # context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)
    # logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'Step failed: {step}')
        print('\nStep failed: ', step)
        # Mark test case as FAILED on BrowserStack:
        # context.driver.execute_script(
        #     'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Step failed"}}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()

