import allure
import pytest
from data import FAQ

QUESTIONS = range(0, 8)


@allure.story('Тесты раздела ответов и вопросов')
class TestFaq:

    @allure.title('Тест вопросов')
    @pytest.mark.parametrize(
        'num', QUESTIONS
    )
    def test_question_text(self, driver, num, faq_page):
        faq_page.open_page()
        faq_page.accept_cookies()
        question = FAQ.get(num)[0]
        assert faq_page.get_question_text(num) == question

    @allure.title('Тест ответов')
    @pytest.mark.parametrize(
        'num', QUESTIONS
    )
    def test_answer_text(self, driver, num, faq_page):
        faq_page.open_page()
        faq_page.accept_cookies()
        answer = FAQ.get(num)[1]
        assert faq_page.get_answer_text(num) == answer
