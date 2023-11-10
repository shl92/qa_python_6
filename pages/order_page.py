import allure
from base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators
from data.order_page_constants import OrderPageConstants
from data.urls import URLS


class OrderPage(BasePage):

    @allure.step("Заполнить имя")
    def input_name(self, name):
        self.driver.find_element(*OrderPageLocators.INPUT_NAME).send_keys(name)

    @allure.step("Заполнить фамилию")
    def input_surname(self, surname):
        self.driver.find_element(*OrderPageLocators.INPUT_SURNAME).send_keys(surname)

    @allure.step("Заполнить адрес")
    def input_address(self, address):
        self.driver.find_element(*OrderPageLocators.INPUT_ADDRESS).send_keys(address)

    @allure.step("Выбрать станцию Лубянка")
    def choose_station_lybanka(self):
        self.driver.find_element(*OrderPageLocators.SELECT_STATION).click()
        self.driver.find_element(*OrderPageLocators.STATIONS_CHOOSE_LYBANKA).click()

    @allure.step("Заполнить телефон")
    def input_phone(self, phone):
        self.driver.find_element(*OrderPageLocators.INPUT_PHONE).send_keys(phone)

    @allure.step("Нажать кнопку 'Далее'")
    def continue_button_click(self):
        self.is_element_clickable(OrderPageLocators.CONTINUE_BUTTON)
        self.driver.find_element(*OrderPageLocators.CONTINUE_BUTTON).click()

    @allure.step("Заполнить первую форму заказа - для кого самокат")
    def fill_order_form_for_whom(self, name, surname, address, phone):
        self.input_name(name)
        self.input_surname(surname)
        self.input_address(address)
        self.choose_station_lybanka()
        self.input_phone(phone)
        self.continue_button_click()

    @allure.step("Выбрать дату")
    def input_date(self, date):
        self.driver.find_element(*OrderPageLocators.DATE_FIELD).send_keys(date)

    @allure.step("Выбрать срок аренды")
    def input_time_day(self):
        self.driver.find_element(*OrderPageLocators.TIME_RENT_FIELD).click()
        self.driver.find_element(*OrderPageLocators.TIME_RENT_CHOOSE_DAY).click()

    @allure.step("Выбрать черный цвет самоката")
    def color_choose_black(self):
        self.driver.find_element(*OrderPageLocators.COLOR_CHOOSE_BLACK).click()

    @allure.step("Заполнить комментарий")
    def input_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.INPUT_COMMENT).send_keys(comment)

    @allure.step("Нажать кнопку 'Заказать'")
    def make_order_button_click(self):
        self.is_element_clickable(OrderPageLocators.MAKE_ORDER_BUTTON)
        self.driver.find_element(*OrderPageLocators.MAKE_ORDER_BUTTON).click()

    @allure.step("Заполнить вторую форму заказа - про аренду")
    def full_order_form_about_rent(self, date_rent, comment):
        self.input_date(date_rent)
        self.input_time_day()
        self.color_choose_black()
        self.input_comment(comment)
        self.make_order_button_click()

    @allure.step("Нажать на кнопку 'Да' для оформления заказа")
    def confirm_button_click(self):
        self.is_element_clickable(OrderPageLocators.CONFIRM_BUTTON)
        self.driver.find_element(*OrderPageLocators.CONFIRM_BUTTON).click()

    @allure.step("Проверить факт оформления заказа")
    def check_order_status(self):
        temp = self.driver.find_element(*OrderPageLocators.ORDER_STATUS).text.split()[:2]
        result_order_text = ' '.join(temp)
        assert result_order_text == OrderPageConstants.ORDER_RESULT_TEXT, (
            f"Текст не совпадает. Ожидаемый текст: {result_order_text}, фактический "
            f"текст: {OrderPageConstants.ORDER_RESULT_TEXT}")

    @allure.step("Проверить переход на страницу оформления заказа")
    def check_order_page(self):
        self.is_element_present(OrderPageLocators.CONTINUE_BUTTON)
        assert self.driver.find_element(*OrderPageLocators.CONTINUE_BUTTON), "Переход на страницу заказа не произошел"

    @allure.step("Нажать на логотип 'Самокат'")
    def click_on_scooter_logo(self):
        self.is_element_clickable(MainPageLocators.LOGO_SCOOTER)
        self.driver.find_element(*MainPageLocators.LOGO_SCOOTER).click()

    @allure.step("Проверить переход на главную страницу")
    def check_current_main_page_url(self):
        current_url = self.driver.current_url
        assert current_url == URLS.MAIN_PAGE, (f"Переход на главную страницу не произошел. Ожидаемая "
                                               f"страница: {URLS.MAIN_PAGE}, фактическая страница"
                                               f" {current_url}")

    @allure.step("Нажать на логотип 'Яндекс'")
    def click_on_yandex_logo(self):
        self.is_element_clickable(MainPageLocators.LOGO_YANDEX)
        self.driver.find_element(*MainPageLocators.LOGO_YANDEX).click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Проверить переход на страницу дзена")
    def check_current_dzen_page_url(self, url):
        self.is_url_contains_text(url)
        current_url = self.driver.current_url
        assert 'dzen.ru' in current_url, f"Переход на страницу Дзена не произошел. Текущая страница: {current_url}"
