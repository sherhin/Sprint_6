from pages.base_page import BasePage

from selenium.webdriver.common.by import By

class FaqPage(BasePage):
    faq = (By.CLASS_NAME, 'accordion')
    questions = (By.CLASS_NAME, 'accordion__item')

    def __init__(self, driver):
        super().__init__(driver)

    def find_questions(self):
        self.navigate()
        self.scroll_to_element(self.faq)
        print('ТУТ ВСЕ ПРОШЛО')
        questions = self.find_some_elements(self.questions)
        return questions

    # def click_first_question(self):
    #     question = self.find_questions()

