from selenium.webdriver.common.by import By


class OrderPageLocators:
    INPUT_NAME = (By.XPATH, "//input[contains(@placeholder, 'Имя')]")
    INPUT_SURNAME = (By.XPATH, "//input[contains(@placeholder, 'Фамилия')]")
    INPUT_ADDRESS = (By.XPATH, "//input[contains(@placeholder, 'Адрес')]")
    SELECT_STATION = (By.XPATH, "//input[contains(@placeholder, 'Станция')]")
    STATIONS_CHOOSE_LYBANKA = (By.XPATH, "//ul[@class='select-search__options']/li//div[text()='Лубянка']")
    INPUT_PHONE = (By.XPATH, "//input[contains(@placeholder, 'Телефон')]")
    CONTINUE_BUTTON = (By.XPATH, "//button[text()='Далее']")
    DATE_FIELD = (By.XPATH, "//input[contains(@placeholder, 'Когда')]")
    TIME_RENT_FIELD = (By.XPATH, "//span[@class='Dropdown-arrow']")
    TIME_RENT_CHOOSE_DAY = (By.XPATH, "(//div[@class='Dropdown-option'])[1]")
    COLOR_CHOOSE_BLACK = (By.ID, "black")
    INPUT_COMMENT = (By.XPATH, "//input[contains(@placeholder, 'Комментарий')]")
    MAKE_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    ORDER_STATUS = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")
