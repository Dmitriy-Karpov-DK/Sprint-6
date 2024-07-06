import pytest
import allure
from locators.base_page_locators import LocatorsBasePage
from pages.base_page import BasePage


class TestScooterClikQuests:
    data_quest = [
        (LocatorsBasePage.QUEST_1_BUTTON, LocatorsBasePage.ANSWER_TO_QUEST_1,
         'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
        (LocatorsBasePage.QUEST_2_BUTTON, LocatorsBasePage.ANSWER_TO_QUEST_2,
         'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями,'
         ' можете просто сделать несколько заказов — один за другим.'),
        (LocatorsBasePage.QUEST_3_BUTTON, LocatorsBasePage.ANSWER_TO_QUEST_3,
         'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. '
         'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру.'
         ' Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
        (LocatorsBasePage.QUEST_4_BUTTON, LocatorsBasePage.ANSWER_TO_QUEST_4,
         'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
        (LocatorsBasePage.QUEST_5_BUTTON, LocatorsBasePage.ANSWER_TO_QUEST_5,
         'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
        (LocatorsBasePage.QUEST_6_BUTTON, LocatorsBasePage.ANSWER_TO_QUEST_6,
         'Самокат приезжает к вам с полной зарядкой.'
         ' Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
        (LocatorsBasePage.QUEST_7_BUTTON, LocatorsBasePage.ANSWER_TO_QUEST_7,
         'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
        (LocatorsBasePage.QUEST_8_BUTTON, LocatorsBasePage.ANSWER_TO_QUEST_8,
         'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
    ]

    @allure.title('Проверка ответов на вопросы в футере')
    @pytest.mark.parametrize('quest, answer, text_answer', data_quest)
    def test_click_question_1_show_answer(self, quest, answer, text_answer, driver):
        test_page = BasePage(driver)
        test_page.expectation(LocatorsBasePage.BASE_TITLE_SCOOTER)
        test_page.scroll_page()
        test_page.expectation(LocatorsBasePage.QUEST_1_BUTTON)
        test_page.wait_clickability(quest)
        test_page.click_method(quest)
        assert test_page.get_answer_text(answer) == text_answer
