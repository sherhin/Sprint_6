import pytest
from conftest import driver_client
from pages.faq_page import FaqPage


class TestFaq:

    def test_click(self, driver_client):
        faq = FaqPage(driver_client)
        print(faq.find_questions())

