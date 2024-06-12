import pytest
from selenium import webdriver

from pages.order_page import OrderPage
from pages.faq_page import FaqPage
from data import Url


@pytest.fixture(scope='function')
def driver():
    """Создание вебдрайвер-клиента
    """
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def order_page(driver):
    url_path = Url.ORDER_PATH
    return OrderPage(driver, url_path)


@pytest.fixture(scope='function')
def faq_page(driver):
    return FaqPage(driver)
