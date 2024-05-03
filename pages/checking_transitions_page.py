from locators.home_locators import Home
from locators.order_locators import Order
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
import allure
from data import Urls


class CheckingTransitions(BasePage):
    @allure.step('Кликаем на кнопку "заказать" вверху')
    def click_order_button_top(self):
        button = self.wait_and_find_element(*Home.BUTTON_TOP)
        button.click()
        element = self.wait_and_find_element(*Order.ORDER_HEADER)
        assert element.is_displayed()

    @allure.step('Кликаем на логотип "Самокат"')
    def click_logo_scooter(self):
        logo_scooter = self.wait_and_find_element(*Home.LOGO_SCOOTER)
        logo_scooter.click()

    @allure.step('Кликаем на логотип "Яндекс"')
    def click_logo_yandex(self):
        logo_yandex = self.wait_and_find_element(*Home.YANDEX_SCOOTER)
        logo_yandex.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        expected_url_dzen = Urls.DZEN
        WebDriverWait(self.driver, 10).until(lambda driver: self.driver.current_url == expected_url_dzen)
