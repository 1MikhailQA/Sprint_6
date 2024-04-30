from data import Urls, ScooterOrderData1, ScooterOrderData2
from pages.base_page import BasePage
from pages.order_page import OrderScooter
import pytest
import allure

class TestOrder:
    @allure.step('Оформляем заказ на самокат, используям два сценария с разным данными')
    @pytest.mark.parametrize("order_data", [ScooterOrderData1, ScooterOrderData2])
    def test_order(self, driver, order_data):
        base_page = BasePage(driver)
        base_page.open_url(Urls.SCOOTER)

        order_page = OrderScooter(driver)
        order_page.click_order_button_top()

        order_page.set_name_input(order_data.NAME)
        order_page.set_family_input(order_data.FAMILY)
        order_page.set_address_input(order_data.ADDRESS)
        order_page.select_metro_station()
        order_page.set_phone_input(order_data.PHONE_NUMBER)
        order_page.click_next_button()
        order_page.select_date_period()
        order_page.select_rental_period()
        order_page.click_checkbox_button()
        order_page.set_comment_input(order_data.COMMENT)
        order_page.click_order_button()
        order_page.click_yes_button()
        assert order_page.is_success_message_displayed()

