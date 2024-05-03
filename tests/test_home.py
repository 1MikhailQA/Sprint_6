from data import Urls
from pages.home_page import OrderButton, OrderButton2
import allure


class TestHome:
    @allure.step('Кликаем на кнопку "заказать" вверху')
    def test_order_button_top(self, driver):
        home_page = OrderButton(driver)
        home_page.open_url(Urls.SCOOTER)
        home_page.click_order_button_top()

    @allure.step('Кликаем на кнопку "заказать" внизу')
    def test_order_button_bottom(self, driver):
        home_page = OrderButton2(driver)
        home_page.open_url(Urls.SCOOTER)
        home_page.click_order_button_bottom()