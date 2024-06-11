import allure
import pytest

from data import *
from locators.order_page_locators import *
from locators.base_locators import *


@allure.story('Тесты заказа самоката')
class TestScooterOrder:
    @allure.title('Тест заказа самоката')
    @pytest.mark.parametrize('button, data', [
        (BasePageLocators.ORDER_BUTTON_HEADER, User1),
        (BasePageLocators.ORDER_BUTTON_BODY, User2)
    ])
    def test_order_scooter(self, driver, button, data, order_page):
        order_page.open_page()
        order_page.accept_cookies()
        order_page.click_to_element(button)
        order_page.client_form(data)
        order_page.rent_form(data)
        order_page.click_to_element(OrderPageLocators.BUTTON_YES)
        assert order_page.order_issued_check() == 'Посмотреть статус'