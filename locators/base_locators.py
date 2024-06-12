from selenium.webdriver.common.by import By


class BasePageLocators:
    ACCEPT_COOKIES = (By.XPATH, "//button[contains(@id,'confirm-button')]")
    LOGO_YANDEX = (By.XPATH, "//img[@alt='Yandex']")
    LOGO_SCOOTER = (By.XPATH, "//img[@alt='Scooter']")
    ORDER_BUTTON_HEADER = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    ORDER_BUTTON_BODY = (By.XPATH, "//button[contains(@class,'Button_UltraBig')]")


class DzenLocators:
    DZEN_LOGO = (By.XPATH, "//a[@data-testid='logo']")