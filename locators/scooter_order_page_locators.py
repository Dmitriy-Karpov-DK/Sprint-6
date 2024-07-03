from selenium.webdriver.common.by import By


class LocatorsScooterOrderPage:

    FORM_ORDER_PAGE = (By.XPATH, "//div[text()='Для кого самокат']")  # форма заказа
    FIELD_INPUT_NAME = (By.XPATH, "//input[@placeholder='* Имя']")  # поле ввода Имени
    FIELD_INPUT_LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")  # поле ввода Фамилии
    FIELD_INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")  # поле ввода Адреса
    FIELD_SELECT_METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")  # поле выбора станции метро
    FIELD_INPUT_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")  # поле ввода телефона
    ORDER_NEXT_BUTTON = (By.XPATH, "//div[@class='Order_NextButton__1_rCA']//button")  # кнопка Дальше в заказе
    FORM_ORDER_PAGE_NEXT = (By.XPATH, "//div[text()='Про аренду']")  # форма заказа продолжение
    FIELD_INPUT_DATEPICKER = (By.XPATH, "//div[@class='react-datepicker__input-container']//input")  # поле ввода даты заказа
    FIELD_RENTAL_PERIOD = (By.XPATH, "//div[@class='Dropdown-root']")  # поле ввода срока аренды
    INPUT_RENTAL_PERIOD = (By.XPATH, "//div[text()='сутки']")  # выбор срока аренды (список)
    INPUT_COLOR_SCOOTER = (By.ID, 'black')  # выбор цвета самоката (чекбокс)
    FIELD_COMMENT_TO_COURIER = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")  # поле ввода комментария для курьера
    ORDER_BUTTON_FINAL = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[text()='Заказать']")  # кнопка завершить заказ
    INPUT_METRO_VALUE_1 = (By.XPATH, "//li[@data-value=1]")  # выбор станции метро
    BUTTON_POP_UP_CHECKOUT_WINDOW = (By.XPATH, "//button[text()='Да']")  # кнопка подтверждения заказа во всплывающем окне
    POP_UP_WINDOW_ORDER = (By.XPATH, "//div[text()='Хотите оформить заказ?']")  # окно подтверждения заказа
    POO_UP_WINDOW_SUCCESSFUL_ORDER = (By.XPATH, "//div[text()='Заказ оформлен']")  # окно успешеного оформления заказа
