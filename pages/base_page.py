import allure
from selenium.webdriver import Remote as RemoteWebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.main_page_locators import MainPageLocators


class BasePage:
    def __init__(self, driver: RemoteWebDriver, url):
        self.driver = driver
        self.url = url

    @allure.step("Открыть страницу")
    def open_page(self):
        self.driver.get(self.url)

    def is_element_present(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))

    def is_element_clickable(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))

    def is_url_contains_text(self, url):
        WebDriverWait(self.driver, 3).until(expected_conditions.url_contains(url))

    @allure.step("Принять cookies")
    def accept_cookies(self):
        self.driver.find_element(*MainPageLocators.COOKIES_BUTTON).click()
