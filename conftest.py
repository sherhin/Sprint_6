import time

import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver_client():
    """Создание вебдрайвер-клиента
    """
    driver = webdriver.Firefox()
    yield driver
    time.sleep(10)
    driver.quit()
