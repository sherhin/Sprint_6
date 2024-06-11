import time

import pytest
from selenium import webdriver

from pages.order_page import OrderPage
from pages.base_page import BasePage
from data import Url


@pytest.fixture(scope='function')
def driver():
    """Создание вебдрайвер-клиента
    """
    driver = webdriver.Firefox()
    yield driver
    time.sleep((5))
    driver.quit()

@pytest.fixture(scope='function')
def order_page(driver):
    url_path = Url.ORDER_PATH
    return OrderPage(driver, url_path)

@pytest.fixture(scope='function')
def faq_page(driver):
    url_path = Url.MAIN_PAGE
    return BasePage(driver, url_path)