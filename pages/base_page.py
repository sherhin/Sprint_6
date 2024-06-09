import time

from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from  selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url='https://qa-scooter.praktikum-services.ru/'):
        self.driver.get(url)

    def find_element_with_wait(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_to_element(self, locator):
        self.find_element_with_wait(locator).click()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text


    def format_locators(self, locator, num):
        method, locator = locator
        format_locator = locator.format(num)

        return method, format_locator



    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        print(element)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)


    def find_some_elements(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            print(f'Elements with locator {locator} not found within {timeout}')
            return None


    def put_cursor(self, element):
        action = ActionChains(driver=self.driver)
        element = action.move_to_element(element)
        return element

