import time

from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url='https://qa-scooter.praktikum-services.ru/'):
        self.driver.get(url)

    def find_element(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print(f'Element with locator {locator} not found within {timeout}')
            return None

    def click_element(self, locator, timeout):
        element = self.find_element(locator, timeout)
        if element:
            element.click()
        else:
            print(f'Failed to click element with locator {locator}')


    def scroll_to_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)


    def find_some_elements(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            print(f'Elements with locator {locator} not found within {timeout}')
            return None

