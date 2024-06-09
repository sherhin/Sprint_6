import pytest
from conftest import driver_client
from pages.faq_page import FaqPage
from pages.data import FAQ

QUESTIONS = range(0, 9)
class TestFaq:

    @pytest.mark.parametrize(
        'num', QUESTIONS
    )
    def test_question_and_answers(self, driver_client, num):
        faq_page = FaqPage(driver_client)
        answer = FAQ.get(num)[1]
        assert faq_page.get_answer_text(num) == answer, faq_page.get_answer_text(num)

