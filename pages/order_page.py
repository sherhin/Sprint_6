import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from locators.base_locators import *


class OrderPage(BasePage):

    @allure.step('Заполнение формы "Для кого самокат"')
    def client_form(self, data):
        self.add_text_to_element(OrderPageLocators.NAME_INPUT, data.name)
        self.add_text_to_element(OrderPageLocators.SURNAME_INPUT, data.surname)
        self.add_text_to_element(OrderPageLocators.ADRESS_INPUT, data.address)
        self.add_text_to_element(OrderPageLocators.UNDEGROUND_INPUT, data.underground)
        self.click_to_element(OrderPageLocators.SELECT_UNDEGROUND)
        self.add_text_to_element(OrderPageLocators.PHONE_NUMBER_INPUT, data.number)
        self.click_to_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Заполнение формы "Про аренду"')
    def rent_form(self, data):
        self.add_text_to_element(OrderPageLocators.DATE_INPUT, data.date)
        self.click_to_element(OrderPageLocators.SELECT_COLOR_GREY)
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD_ONE_DAY)
        self.add_text_to_element(OrderPageLocators.COMMENT_INPUT, data.comment)
        self.click_to_element(OrderPageLocators.BUTTON_ORDER)

    @allure.step('Проверка успешного оформления заказа')
    def order_issued_check(self):
        return self.get_text_from_element(OrderPageLocators.ORDER_STATUS)

    @allure.step('Переход по лого Яндекс')
    def click_on_yandex_logo(self):
        self.click_to_element(BasePageLocators.LOGO_SCOOTER)

    @allure.step('Переход по лого Самокат')
    def click_on_scooter_logo(self):
        self.click_to_element(BasePageLocators.LOGO_YANDEX)
        self.switch_tab(DzenLocators.DZEN_LOGO)