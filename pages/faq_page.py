from pages.base_page import BasePage

from selenium.webdriver.common.by import By
from locators.faq_page_locators import FaqPageLocators

class FaqPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def scroll_to_last_question(self):
        self.navigate()
        last_question = self.format_locators(FaqPageLocators.QUESTION_LOCATOR, 6)
        print(last_question)
        return self.scroll_to_element(last_question)

    def get_answer_text(self, num):
        self.scroll_to_last_question()
        locator_q_formatted = self.format_locators(FaqPageLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(FaqPageLocators.ANSWER_LOCATOR, num)
        print(locator_q_formatted)
        self.click_to_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)

