import pytest
import allure
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.main_page_constants import MainPageConstants
from data.urls import URLS


@allure.feature("Проверка функционала на главной странице сайта")
class TestMainPage:

    @allure.title("Проверка блока FAQ на главной странице сайта")
    @allure.description("Находим блок FAQ на главной странице сайта, раскрываем каждый вопрос путем клика по нему, "
                        "сравниваем раскрывшийся ответ с требуемым текстом.")
    @pytest.mark.parametrize('num, answer_text',
                             [(1, MainPageConstants.ANSWER_1), (2, MainPageConstants.ANSWER_2),
                              (3, MainPageConstants.ANSWER_3), (4, MainPageConstants.ANSWER_4),
                              (5, MainPageConstants.ANSWER_5), (6, MainPageConstants.ANSWER_6),
                              (7, MainPageConstants.ANSWER_7), (8, MainPageConstants.ANSWER_8)])
    def test_faq_correct_answers(self, driver, num, answer_text):
        main_page = MainPage(driver, URLS.MAIN_PAGE)
        main_page.open_page()
        main_page.accept_cookies()
        main_page.scroll_to_end_of_page()
        main_page.check_question_equal_answer(num, answer_text)

    @allure.title("Проверка корректного перехода на страницу заказа по кнопке 'Заказать'")
    @allure.description("Открываем главную страницу сайта, нажимаем на кнопку 'Заказать', проверяем что осуществлен "
                        "переход на страницу оформления заказа.")
    @pytest.mark.parametrize('order_button_locator', [MainPageLocators.ORDER_BUTTON_HEADER,
                                                      MainPageLocators.ORDER_BUTTON_MIDDLE],
                             ids=['header_order_button', 'middle_order_button'])
    def test_order_button_move_to_order_page(self, driver, order_button_locator):
        main_page = MainPage(driver, URLS.MAIN_PAGE)
        main_page.open_page()
        main_page.accept_cookies()
        main_page.order_button_click(order_button_locator)
        order_page = OrderPage(driver, URLS.ORDER_PAGE)
        order_page.check_order_page()
