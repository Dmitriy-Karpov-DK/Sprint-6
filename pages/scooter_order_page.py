import allure

from locators.scooter_order_page_locators import LocatorsScooterOrderPage
from pages.base_page import BasePage


class ScooterOrderPage(BasePage):

    @allure.step('Ввод Имени')
    def input_name(self, name):
        self.send_keys_method(LocatorsScooterOrderPage.FIELD_INPUT_NAME, name)

    @allure.step('Ввод Фамилии')
    def input_last_name(self, last_name):
        self.send_keys_method(LocatorsScooterOrderPage.FIELD_INPUT_LAST_NAME, last_name)

    @allure.step('Ввод адреса')
    def input_address(self, address):
        self.send_keys_method(LocatorsScooterOrderPage.FIELD_INPUT_ADDRESS, address)

    @allure.step('Выбор станции метро')
    def select_metro(self):
        self.click_method(LocatorsScooterOrderPage.FIELD_SELECT_METRO)
        self.click_method(LocatorsScooterOrderPage.INPUT_METRO_VALUE_1)

    @allure.step('Ввод номера тедефона')
    def input_phone(self, phone):
        self.send_keys_method(LocatorsScooterOrderPage.FIELD_INPUT_PHONE, phone)

    @allure.step('Клик по кнопке формы заказа Далее')
    def click_button_order_next(self):
        self.click_method(LocatorsScooterOrderPage.ORDER_NEXT_BUTTON)

    @allure.step('Выбор даты заказа')
    def input_datepicker(self, date_order):
        self.click_method(LocatorsScooterOrderPage.FIELD_INPUT_DATEPICKER)
        self.expectation(LocatorsScooterOrderPage.FIELD_INPUT_DATEPICKER)
        self.send_keys_method(LocatorsScooterOrderPage.FIELD_INPUT_DATEPICKER, date_order)
        self.click_method(LocatorsScooterOrderPage.FORM_ORDER_PAGE_NEXT)

    @allure.step('Выбор срока аренды')
    def select_rental_period(self):
        self.click_method(LocatorsScooterOrderPage.FIELD_RENTAL_PERIOD)
        self.click_method(LocatorsScooterOrderPage.INPUT_RENTAL_PERIOD)

    @allure.step('Выбор цвета самоката')
    def input_color_scooter(self):
        self.click_method(LocatorsScooterOrderPage.INPUT_COLOR_SCOOTER)

    @allure.step('Ввод комментария для курьера')
    def input_comment_to_courier(self, comment_courier):
        self.send_keys_method(LocatorsScooterOrderPage.FIELD_COMMENT_TO_COURIER, comment_courier)

    @allure.step('клик по кнопке Заказать в форме заказа')
    def click_button_final_order(self):
        self.click_method(LocatorsScooterOrderPage.ORDER_BUTTON_FINAL)

    @allure.step('клик по кнопке Да подтверждения заказа')
    def click_button_pop_up_window_order(self):
        self.click_method(LocatorsScooterOrderPage.BUTTON_POP_UP_CHECKOUT_WINDOW)

    @allure.step('шаги для заполнения и подтверждения формы заказа')
    def step_order_scooter(self, name, last_name, address, phone, date_order, comment_courier):
        self.click_order_button_header()
        self.input_name(name)
        self.input_last_name(last_name)
        self.input_address(address)
        self.select_metro()
        self.input_phone(phone)
        self.click_button_order_next()
        self.expectation(LocatorsScooterOrderPage.FORM_ORDER_PAGE_NEXT)
        self.input_datepicker(date_order)
        self.select_rental_period()
        self.input_color_scooter()
        self.input_comment_to_courier(comment_courier)
        self.expectation(LocatorsScooterOrderPage.ORDER_BUTTON_FINAL)
        self.click_button_final_order()
        self.expectation(LocatorsScooterOrderPage.POP_UP_WINDOW_ORDER)
        self.click_button_pop_up_window_order()
