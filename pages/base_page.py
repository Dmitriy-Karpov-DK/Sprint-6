from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page_locators import LocatorsBasePage


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_method(self, locator):
        self.driver.find_element(*locator).click()

    def send_keys_method(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    def scroll_page(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    def click_order_button_header(self):
        self.click_method(LocatorsBasePage.ORDER_BUTTON_HEADER)

    def click_order_button_middle(self):
        self.click_method(LocatorsBasePage.ORDER_BUTTON_HEADER_NEXT)

    def scroll_page_to_button_order(self):
        element = self.driver.find_element(*LocatorsBasePage.ORDER_BUTTON_HEADER_NEXT)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def expectation(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator))

    def wait_clickability(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator))

    def click_logo_scooter(self):
        self.click_method(LocatorsBasePage.LOGO_SCOOTER)

    def click_logo_yandex(self):
        self.click_method(LocatorsBasePage.LOGO_YANDEX)

    def get_answer_text(self, locator):
        return self.driver.find_element(*locator).text

    def switch_browser_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def get_url(self):
        get_url = self.driver.current_url
        return get_url
