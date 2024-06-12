import allure

from pages.base_page import BasePage
from locators.faq_page_locators import FaqPageLocators


class FaqPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Скролл к последнему вопросу')
    def scroll_to_last_question(self):
        self.open_page()
        last_question = self.format_locators(FaqPageLocators.QUESTION_LOCATOR, 7)
        return self.scroll_to_element(last_question)

    @allure.step('Получение текста ответа')
    def get_answer_text(self, num):
        self.scroll_to_last_question()
        locator_q_formatted = self.format_locators(FaqPageLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(FaqPageLocators.ANSWER_LOCATOR, num)
        self.click_to_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Получение текста вопроса')
    def get_question_text(self, num):
        self.scroll_to_last_question()
        locator_q_formatted = self.format_locators(FaqPageLocators.QUESTION_LOCATOR, num)
        self.click_to_element(locator_q_formatted)
        return self.get_text_from_element(locator_q_formatted)