from locators.home_locators import Home
from locators.order_locators import Order
from pages.base_page import BasePage
import allure

class OrderScooter(BasePage):
    def click_order_button_top(self):
        button = self.wait_and_find_element(*Home.BUTTON_TOP)
        button.click()
        element = self.wait_and_find_element(*Order.ORDER_HEADER)
        assert element.is_displayed()

    def set_name_input(self, name):
        name_input = self.wait_and_find_element(*Order.NAME_INPUT)
        name_input.send_keys(name)

    def set_family_input(self, family):
        family_input = self.wait_and_find_element(*Order.FAMILY_INPUT)
        family_input.send_keys(family)

    def set_address_input(self, address):
        address_input = self.wait_and_find_element(*Order.ADDRESS_INPUT)
        address_input.send_keys(address)

    def select_metro_station(self):
        station_list = self.wait_and_find_element(*Order.METRO_STATION)
        station_list.click()
        station = self.wait_and_find_element(*Order.STATION)
        station.click()

    def set_phone_input(self, phone):
        phone_input = self.wait_and_find_element(*Order.PHONE_NUMBER)
        phone_input.send_keys(phone)

    def click_next_button(self):
        next_button = self.wait_and_find_element(*Order.NEXT_BUTTON)
        next_button.click()

    def select_date_period(self):
        date = self.wait_and_find_element(*Order.DATE)
        date.click()
        calendar = self.wait_and_find_element(*Order.CALENDAR)
        calendar.click()

    def select_rental_period(self):
        rental = self.wait_and_find_element(*Order.RENTAL_PERIOD)
        rental.click()
        time = self.wait_and_find_element(*Order.RENTAL_PERIOD_OPTION)
        time.click()

    def click_checkbox_button(self):
        checkbox_button = self.wait_and_find_element(*Order.SCOOTER_COLOR)
        checkbox_button.click()

    def set_comment_input(self, comment):
        comment_input = self.wait_and_find_element(*Order.COMMENT)
        comment_input.send_keys(comment)

    def click_order_button(self):
        order_button = self.wait_and_find_element(*Order.ORDER_BUTTON)
        order_button.click()

    def click_yes_button(self):
        yes_button = self.wait_and_find_element(*Order.BUTTON_YES)
        yes_button.click()

    def is_success_message_displayed(self):
        element = self.wait_and_find_element(*Order.SUCCESS_MESSAGE)
        return element.is_displayed()






