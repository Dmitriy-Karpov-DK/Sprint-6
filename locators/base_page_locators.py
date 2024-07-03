from selenium.webdriver.common.by import By


class LocatorsBasePage:

    ANSWER_TO_QUEST_1 = (By.ID, 'accordion__panel-0')  # ответ на вопрос 1
    QUEST_1_BUTTON = (By.ID, 'accordion__heading-0')  # кнопка вопроса 1
    ANSWER_TO_QUEST_2 = (By.ID, 'accordion__panel-1')  # ответ на вопрос 2
    QUEST_2_BUTTON = (By.ID, 'accordion__heading-1')  # кнопка вопроса 2
    ANSWER_TO_QUEST_3 = (By.ID, 'accordion__panel-2')  # ответ на вопрос 3
    QUEST_3_BUTTON = (By.ID, 'accordion__heading-2')  # кнопка вопроса 3
    ANSWER_TO_QUEST_4 = (By.ID, 'accordion__panel-3')  # ответ на вопрос 4
    QUEST_4_BUTTON = (By.ID, 'accordion__heading-3')  # кнопка вопроса 4
    ANSWER_TO_QUEST_5 = (By.ID, 'accordion__panel-4')  # ответ на вопрос 5
    QUEST_5_BUTTON = (By.ID, 'accordion__heading-4')  # кнопка вопроса 5
    ANSWER_TO_QUEST_6 = (By.ID, 'accordion__panel-5')  # ответ на вопрос 6
    QUEST_6_BUTTON = (By.ID, 'accordion__heading-5')  # кнопка вопроса 6
    ANSWER_TO_QUEST_7 = (By.ID, 'accordion__panel-6')  # ответ на вопрос 7
    QUEST_7_BUTTON = (By.ID, 'accordion__heading-6')  # кнопка вопроса 7
    ANSWER_TO_QUEST_8 = (By.ID, 'accordion__panel-7')  # ответ на вопрос 8
    QUEST_8_BUTTON = (By.ID, 'accordion__heading-7')  # кнопка вопроса 8
    BASE_TITLE_SCOOTER = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")  # заголовок главной страницы
    ORDER_BUTTON_HEADER = (By.CLASS_NAME, 'Button_Button__ra12g')  # кнопка заказать в шапке
    ORDER_BUTTON_HEADER_NEXT = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']//button")  # кнопка заказать в середине страницы
    LOGO_SCOOTER = (By.XPATH, "//a[@href='/']")  # логотип Самокат
    LOGO_YANDEX = (By.XPATH, "//a[@href='//yandex.ru']")  # логотип Яндекс
