from selenium.webdriver.common.by import By

class Order:
    ORDER_HEADER = (By.CLASS_NAME, "Order_Header__BZXOb")
    NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    FAMILY_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION = (By.CSS_SELECTOR, '[placeholder="* Станция метро"]')
    STATION = (By.CSS_SELECTOR, 'div.Order_Text__2broi')
    PHONE_NUMBER = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.CSS_SELECTOR, 'button.Button_Button__ra12g.Button_Middle__1CSJM')
    DATE = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
    CALENDAR = (By.XPATH, "//div[contains(@class, 'react-datepicker__day') and @aria-label='Choose воскресенье, 5-е мая 2024 г.']")
    RENTAL_PERIOD = (By.XPATH, "//div[@class='Dropdown-placeholder' and text()='* Срок аренды']")
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[@class='Dropdown-option'and text()='сутки']")
    SCOOTER_COLOR = (By.XPATH, "//input[@id='black' and contains(@class, 'Checkbox_Input__14A2w')]")
    COMMENT = (By.CSS_SELECTOR, 'input[placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.CSS_SELECTOR, 'button.Button_Middle__1CSJM:nth-child(2)')
    BUTTON_YES = (By.XPATH, '//button[contains(text(), "Да")]')
    SUCCESS_MESSAGE = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and contains(text(), 'Посмотреть статус')]")

