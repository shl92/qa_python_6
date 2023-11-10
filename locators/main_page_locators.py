from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTIONS_TEMPLATE = (By.XPATH, "(//div[@role='heading'])[{}]")
    ANSWERS_TEMPLATE = (By.XPATH, "(//div[@role='region'])[{}]")
    LOGO_YANDEX = (By.XPATH, "//a[contains(@class, 'LogoYandex')]")
    LOGO_SCOOTER = (By.XPATH, "//a[contains(@class, 'LogoScooter')]")
    ORDER_BUTTON_HEADER = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[1]")
    ORDER_BUTTON_MIDDLE = (By.XPATH, "//button[contains(@class, 'Button_Middle')]")
    COOKIES_BUTTON = (By.ID, "rcc-confirm-button")
