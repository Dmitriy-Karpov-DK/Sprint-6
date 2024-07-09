import pytest
import allure
from pages.scooter_order_page import ScooterOrderPage
from locators.base_page_locators import LocatorsBasePage
from locators.scooter_order_page_locators import LocatorsScooterOrderPage
from constants import Constants


class TestScooterOrder:
    order_data = [
        ('Иван', 'Иванов', 'Открытое шоссе, 5 к10', '89999999999', '15.07.2024', 'звонить за 15 минут'),
        ('Вася', 'Васильев', '5-й проезд Подбельского, 4а к5', '87777777777', '14.07.2024', 'стучать три раза')
    ]

    @allure.title('Проверка кнопки Заказать в шапке')
    def test_click_button_order_header_show_page_order(self, driver):
        test_page = ScooterOrderPage(driver)
        test_page.expectation(LocatorsBasePage.BASE_TITLE_SCOOTER)
        test_page.click_order_button_header()
        assert 'Для кого самокат' in test_page.get_answer_text(LocatorsScooterOrderPage.FORM_ORDER_PAGE)

    @allure.title('Проверка кнопки Заказать в середине страницы')
    def test_click_button_order_middle_show_page_order(self, driver):
        test_page = ScooterOrderPage(driver)
        test_page.expectation(LocatorsBasePage.BASE_TITLE_SCOOTER)
        test_page.scroll_page_to_button_order()
        test_page.wait_clickability(LocatorsBasePage.ORDER_BUTTON_HEADER_NEXT)
        test_page.click_order_button_middle()
        assert 'Для кого самокат' in test_page.get_answer_text(LocatorsScooterOrderPage.FORM_ORDER_PAGE)

    @allure.title('Проверка заказа самоката')
    @pytest.mark.parametrize(
        'name, last_name, address, phone, date_order, comment_courier', order_data)
    def test_order_scooter_positive_successful(
            self, driver, name, last_name, address, phone, date_order, comment_courier):
        test_page = ScooterOrderPage(driver)
        test_page.step_order_scooter(name, last_name, address, phone, date_order, comment_courier)
        assert "Заказ оформлен" in test_page.get_answer_text(LocatorsScooterOrderPage.POO_UP_WINDOW_SUCCESSFUL_ORDER)

    @allure.title('клик по логотипу Самоката')
    def test_click_logo_scooter_show_base_page_scooter(self, driver):
        test_page = ScooterOrderPage(driver)
        test_page.expectation(LocatorsBasePage.BASE_TITLE_SCOOTER)
        test_page.click_order_button_header()
        test_page.expectation(LocatorsScooterOrderPage.FORM_ORDER_PAGE)
        test_page.click_logo_scooter()
        test_page.expectation(LocatorsBasePage.BASE_TITLE_SCOOTER)
        assert test_page.get_url() == Constants.URL

    @allure.title('клик по логотипу Яндекса')
    def test_click_logo_yandex_show_base_page_dzen(self, driver):
        test_page = ScooterOrderPage(driver)
        test_page.expectation(LocatorsBasePage.BASE_TITLE_SCOOTER)
        test_page.click_logo_yandex()
        test_page.switch_browser_window()
        test_page.expectation(LocatorsBasePage.YANDEX_PAGE)
        assert test_page.get_url() == Constants.URL_DZEN
