from pages.base_page import BasePage
from locators.base_page_locators import LocatorsBasePage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestScooterClikQuests:

    def test_click_question_1_show_answer(self, driver):
        base_page1 = BasePage(driver)
        base_page1.expectation(LocatorsBasePage.BASE_TITLE_SCOOTER)
        base_page1.scroll_page()
        base_page1.wait_clickability(LocatorsBasePage.QUEST_1_BUTTON)
        base_page1.click_quest_1()
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LocatorsBasePage.ANSWER_TO_QUEST_1))

    def test_click_question_2_show_answer(self, driver):
        base_page1 = BasePage(driver)
        base_page1.expectation(LocatorsBasePage.BASE_TITLE_SCOOTER)
        base_page1.scroll_page()
        base_page1.wait_clickability(LocatorsBasePage.QUEST_2_BUTTON)
        base_page1.click_quest_2()
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LocatorsBasePage.ANSWER_TO_QUEST_2))

    def test_click_question_3_show_answer(self, driver):
        base_page1 = BasePage(driver)
        base_page1.expectation(LocatorsBasePage.BASE_TITLE_SCOOTER)
        base_page1.scroll_page()
        base_page1.wait_clickability(LocatorsBasePage.QUEST_3_BUTTON)
        base_page1.click_quest_3()
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LocatorsBasePage.ANSWER_TO_QUEST_3))

    def test_click_question_4_show_answer(self, driver):
        base_page1 = BasePage(driver)
        base_page1.expectation(LocatorsBasePage.BASE_TITLE_SCOOTER)
        base_page1.scroll_page()
        base_page1.wait_clickability(LocatorsBasePage.QUEST_4_BUTTON)
        base_page1.click_quest_4()
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LocatorsBasePage.ANSWER_TO_QUEST_4))

    def test_click_question_5_show_answer(self, driver):
        base_page1 = BasePage(driver)
        base_page1.expectation(LocatorsBasePage.BASE_TITLE_SCOOTER)
        base_page1.scroll_page()
        base_page1.wait_clickability(LocatorsBasePage.QUEST_5_BUTTON)
        base_page1.click_quest_5()
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LocatorsBasePage.ANSWER_TO_QUEST_5))

    def test_click_question_6_show_answer(self, driver):
        base_page1 = BasePage(driver)
        base_page1.expectation(LocatorsBasePage.BASE_TITLE_SCOOTER)
        base_page1.scroll_page()
        base_page1.wait_clickability(LocatorsBasePage.QUEST_6_BUTTON)
        base_page1.click_quest_6()
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LocatorsBasePage.ANSWER_TO_QUEST_6))

    def test_click_question_7_show_answer(self, driver):
        base_page1 = BasePage(driver)
        base_page1.expectation(LocatorsBasePage.BASE_TITLE_SCOOTER)
        base_page1.scroll_page()
        base_page1.wait_clickability(LocatorsBasePage.QUEST_7_BUTTON)
        base_page1.click_quest_7()
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LocatorsBasePage.ANSWER_TO_QUEST_7))

    def test_click_question_8_show_answer(self, driver):
        base_page1 = BasePage(driver)
        base_page1.expectation(LocatorsBasePage.BASE_TITLE_SCOOTER)
        base_page1.scroll_page()
        base_page1.wait_clickability(LocatorsBasePage.QUEST_8_BUTTON)
        base_page1.click_quest_8()
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LocatorsBasePage.ANSWER_TO_QUEST_8))
