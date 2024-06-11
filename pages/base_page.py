import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Url
from locators.base_locators import BasePageLocators

class BasePage:
    def __init__(self, driver, url_path=''):
        self.driver = driver
        url = Url.MAIN_PAGE
        self.url = url + url_path

    def open_page(self):
        url = self.url
        self.driver.get(url)


    @allure.step('Текущий URL')
    def get_url(self):
        return self.driver.current_url

    def accept_cookies(self):
        return self.click_to_element(BasePageLocators.ACCEPT_COOKIES)

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


    def switch_tab(self, locator):
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))



    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        print(element)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

