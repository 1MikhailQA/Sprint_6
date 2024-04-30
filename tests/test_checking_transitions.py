from data import Urls
from pages.base_page import BasePage
from pages.checking_transitions_page import CheckingTransitions
from locators.home_locators import Home
import allure


class TestChecking:
    @allure.step('Кликаем на логотипы и проверяем url')
    def test_checking(self, driver):
        base_page = BasePage(driver)
        base_page.open_url(Urls.SCOOTER)

        checking_transitions_page = CheckingTransitions(driver)
        checking_transitions_page.click_order_button_top()

        checking_transitions_page.click_logo_scooter()
        assert driver.current_url == Home.URL

        checking_transitions_page.click_logo_yandex()
        assert driver.current_url == Home.URL_DZEN

