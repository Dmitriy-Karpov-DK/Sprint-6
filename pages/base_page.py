from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page_locators import LocatorsBasePage


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_quest_1(self):
        self.driver.find_element(*LocatorsBasePage.QUEST_1_BUTTON).click()

    def click_quest_2(self):
        self.driver.find_element(*LocatorsBasePage.QUEST_2_BUTTON).click()

    def click_quest_3(self):
        self.driver.find_element(*LocatorsBasePage.QUEST_3_BUTTON).click()

    def click_quest_4(self):
        self.driver.find_element(*LocatorsBasePage.QUEST_4_BUTTON).click()

    def click_quest_5(self):
        self.driver.find_element(*LocatorsBasePage.QUEST_5_BUTTON).click()

    def click_quest_6(self):
        self.driver.find_element(*LocatorsBasePage.QUEST_6_BUTTON).click()

    def click_quest_7(self):
        self.driver.find_element(*LocatorsBasePage.QUEST_7_BUTTON).click()

    def click_quest_8(self):
        self.driver.find_element(*LocatorsBasePage.QUEST_8_BUTTON).click()

    def scroll_page(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    def click_order_button_header(self):
        self.driver.find_element(*LocatorsBasePage.ORDER_BUTTON_HEADER).click()

    def click_order_button_middle(self):
        self.driver.find_element(*LocatorsBasePage.ORDER_BUTTON_HEADER_NEXT).click()

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
        self.driver.find_element(*LocatorsBasePage.LOGO_SCOOTER).click()

    def click_logo_yandex(self):
        self.driver.find_element(*LocatorsBasePage.LOGO_YANDEX).click()
