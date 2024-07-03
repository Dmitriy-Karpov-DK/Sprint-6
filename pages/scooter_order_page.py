from locators.scooter_order_page_locators import LocatorsScooterOrderPage
from pages.base_page import BasePage


class ScooterOrderPage(BasePage):

    def input_name(self, name):
        self.driver.find_element(*LocatorsScooterOrderPage.FIELD_INPUT_NAME).send_keys(name)

    def input_last_name(self, last_name):
        self.driver.find_element(*LocatorsScooterOrderPage.FIELD_INPUT_LAST_NAME).send_keys(last_name)

    def input_address(self, address):
        self.driver.find_element(*LocatorsScooterOrderPage.FIELD_INPUT_ADDRESS).send_keys(address)

    def select_metro(self):
        self.driver.find_element(*LocatorsScooterOrderPage.FIELD_SELECT_METRO).click()
        self.driver.find_element(*LocatorsScooterOrderPage.INPUT_METRO_VALUE_1).click()

    def input_phone(self, phone):
        self.driver.find_element(*LocatorsScooterOrderPage.FIELD_INPUT_PHONE).send_keys(phone)

    def click_button_order_next(self):
        self.driver.find_element(*LocatorsScooterOrderPage.ORDER_NEXT_BUTTON).click()

    def input_datepicker(self, date_order):
        self.driver.find_element(*LocatorsScooterOrderPage.FIELD_INPUT_DATEPICKER).click()
        self.expectation(LocatorsScooterOrderPage.FIELD_INPUT_DATEPICKER)
        self.driver.find_element(*LocatorsScooterOrderPage.FIELD_INPUT_DATEPICKER).send_keys(date_order)
        self.driver.find_element(*LocatorsScooterOrderPage.FORM_ORDER_PAGE_NEXT).click()

    def select_rental_period(self):
        self.driver.find_element(*LocatorsScooterOrderPage.FIELD_RENTAL_PERIOD).click()
        self.driver.find_element(*LocatorsScooterOrderPage.INPUT_RENTAL_PERIOD).click()

    def input_color_scooter(self):
        self.driver.find_element(*LocatorsScooterOrderPage.INPUT_COLOR_SCOOTER).click()

    def input_comment_to_courier(self, comment_courier):
        self.driver.find_element(*LocatorsScooterOrderPage.FIELD_COMMENT_TO_COURIER).send_keys(comment_courier)

    def click_button_final_order(self):
        self.driver.find_element(*LocatorsScooterOrderPage.ORDER_BUTTON_FINAL).click()

    def click_button_pop_up_window_order(self):
        self.driver.find_element(*LocatorsScooterOrderPage.BUTTON_POP_UP_CHECKOUT_WINDOW).click()

    def step_order_scooter(self, driver, name, last_name, address, phone, date_order, comment_courier):
        base_page2 = ScooterOrderPage(driver)
        base_page2.click_order_button_header()
        base_page2.input_name(name)
        base_page2.input_last_name(last_name)
        base_page2.input_address(address)
        base_page2.select_metro()
        base_page2.input_phone(phone)
        base_page2.click_button_order_next()
        base_page2.expectation(LocatorsScooterOrderPage.FORM_ORDER_PAGE_NEXT)
        base_page2.input_datepicker(date_order)
        base_page2.select_rental_period()
        base_page2.input_color_scooter()
        base_page2.input_comment_to_courier(comment_courier)
        base_page2.expectation(LocatorsScooterOrderPage.ORDER_BUTTON_FINAL)
        base_page2.click_button_final_order()
        base_page2.expectation(LocatorsScooterOrderPage.POP_UP_WINDOW_ORDER)
        base_page2.click_button_pop_up_window_order()
