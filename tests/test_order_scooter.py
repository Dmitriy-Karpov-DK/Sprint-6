import pytest
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from pages.scooter_order_page import ScooterOrderPage
from locators.base_page_locators import LocatorsBasePage
from locators.scooter_order_page_locators import LocatorsScooterOrderPage
from constants import Constants


class TestScooterOrder:
    order_data = [
        ('Иван', 'Иванов', 'Открытое шоссе, 5 к10', '89999999999', '15.07.2024', 'звонить за 15 минут'),
        ('Вася', 'Васильев', '5-й проезд Подбельского, 4а к5', '87777777777', '14.07.2024', 'стучать три раза')
    ]

    def test_click_button_order_header_show_page_order(self, driver):
        base_page1 = BasePage(driver)
        base_page1.expectation(LocatorsBasePage.BASE_TITLE_SCOOTER)
        base_page1.click_order_button_header()
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LocatorsScooterOrderPage.FORM_ORDER_PAGE))

    def test_click_button_order_middle_show_page_order(self, driver):
        base_page1 = BasePage(driver)
        base_page1.expectation(LocatorsBasePage.BASE_TITLE_SCOOTER)
        base_page1.scroll_page_to_button_order()
        base_page1.wait_clickability(LocatorsBasePage.ORDER_BUTTON_HEADER_NEXT)
        base_page1.click_order_button_middle()
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LocatorsScooterOrderPage.FORM_ORDER_PAGE))

    @pytest.mark.parametrize(
        'name, last_name, address, phone, date_order, comment_courier', order_data)
    def test_order_scooter_positive_successful(
            self, driver, name, last_name, address, phone, date_order, comment_courier):
        ScooterOrderPage.step_order_scooter(self, driver, name, last_name, address, phone, date_order, comment_courier)
        assert "Заказ оформлен" in WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LocatorsScooterOrderPage.POO_UP_WINDOW_SUCCESSFUL_ORDER)
        ).text

    def test_click_logo_scooter_show_base_page_scooter(self, driver):
        base_page1 = BasePage(driver)
        base_page1.click_order_button_header()
        base_page1.click_logo_scooter()
        assert driver.current_url == Constants.URL

    def test_click_logo_yandex_show_base_page_dzen(self, driver):
        base_page1 = BasePage(driver)
        base_page1.expectation(LocatorsBasePage.BASE_TITLE_SCOOTER)
        base_page1.click_logo_yandex()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == Constants.URL_DZEN
