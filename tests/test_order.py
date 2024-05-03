from data import Urls, ScooterOrderData1, ScooterOrderData2
from pages.order_page import OrderScooter
import pytest
import allure

class TestOrder:
    @allure.step('Оформляем заказ на самокат, используя два сценария с разным данными')
    @pytest.mark.parametrize("order_data", [ScooterOrderData1, ScooterOrderData2])
    def test_order(self, driver, order_data):
        order_page = OrderScooter(driver)
        order_page.open_url(Urls.SCOOTER)
        order_page.click_order_button_top()
        order_page.fill_order_fields(order_data)
        order_page.click_order_button()
        order_page.click_yes_button()
        assert order_page.is_success_message_displayed()

