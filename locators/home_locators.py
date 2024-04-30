from selenium.webdriver.common.by import By

class Home:
    BUTTON_TOP = (By.CLASS_NAME, "Button_Button__ra12g")
    BUTTON_BOTTOM = (By.XPATH, "//button[contains(@class, 'Button_UltraBig__UU3Lp')]")
    LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_SCOOTER = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    URL = ("https://qa-scooter.praktikum-services.ru/")
    URL_DZEN = ("https://dzen.ru/?yredirect=true")