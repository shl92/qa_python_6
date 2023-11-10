import allure
from locators.main_page_locators import MainPageLocators
from base_page import BasePage


class MainPage(BasePage):

    @allure.step("Проскролить страницу вниз")
    def scroll_to_end_of_page(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    @allure.step("Найти и нажать на вопрос из FAQ")
    def find_question_and_click(self, num):
        method, locator = MainPageLocators.QUESTIONS_TEMPLATE
        locator = locator.format(num)
        self.is_element_present((method, locator))
        self.driver.find_element(method, locator).click()

    @allure.step("Найти ответ FAQ")
    def find_answer_text(self, num):
        method, locator = MainPageLocators.ANSWERS_TEMPLATE
        locator = locator.format(num)
        self.is_element_present((method, locator))
        return self.driver.find_element(method, locator).text

    @allure.step("Проверить соответствие ответа ожидаемому ответу")
    def check_question_equal_answer(self, num, correct_answer):
        self.find_question_and_click(num)
        found_answer = self.find_answer_text(num)
        assert found_answer == correct_answer, (f"Текст не совпадает, нашлось: {found_answer}, "
                                                f"должно быть: {correct_answer}")

    @allure.step("Нажать на кнопку 'Заказать'")
    def order_button_click(self, order_button_locator):
        self.is_element_clickable(order_button_locator)
        self.driver.find_element(*order_button_locator).click()
