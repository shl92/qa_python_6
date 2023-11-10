import pytest
import allure
from pages.main_page import MainPage
from data.urls import URLS
from data.order_page_constants import OrderPageConstants
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators


@allure.feature("Проверка функционала на странице оформления заказа")
class TestOrderPage:

    @allure.title("Проверка корректного оформления заказа")
    @allure.description("Открываем главную страницу сайта, нажимаем на кнопку 'Заказать', переходим на страницу "
                        "оформления заказа, последовательно заполняем все поля двух форм для оформления заказа, "
                        "проверяем наличие фразы об успешном оформлении заказа. ")
    @pytest.mark.parametrize('example', [OrderPageConstants.order_1, OrderPageConstants.order_2])
    def test_make_order_success_order(self, driver, example):
        main_page = MainPage(driver, URLS.MAIN_PAGE)
        main_page.open_page()
        main_page.order_button_click(MainPageLocators.ORDER_BUTTON_HEADER)
        order_page = OrderPage(driver, URLS.ORDER_PAGE)
        order_page.fill_order_form_for_whom(example['name'], example['surname'], example['address'], example['phone'])
        order_page.full_order_form_about_rent(example['date'], example['comment'])
        order_page.confirm_button_click()
        order_page.check_order_status()

    @allure.title("Проверка корректного перехода на главную страницу через логотип самоката")
    @allure.description("Открываем страницу оформления заказа, нажимаем на логотип самоката, проверяем факт перехода "
                        "на главную страницу сайта.")
    def test_scooter_logo_correct_switch_to_main_page(self, driver):
        order_page = OrderPage(driver, URLS.ORDER_PAGE)
        order_page.open_page()
        order_page.click_on_scooter_logo()
        order_page.check_current_main_page_url()

    @allure.title("Проверка корректного перехода на страницу 'Яндекс-дзен' через логотип яндекса")
    @allure.description("Открываем страницу оформления заказа, нажимаем на логотип яндекса, проверяем факт перехода "
                        "на страницу 'Яндекс-дзен'.")
    def test_yandex_logo_link_correct_switch_to_dzen_page(self, driver):
        order_page = OrderPage(driver, URLS.ORDER_PAGE)
        order_page.open_page()
        order_page.click_on_yandex_logo()
        order_page.check_current_dzen_page_url(URLS.DZEN_PAGE)
