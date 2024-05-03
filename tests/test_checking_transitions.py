from data import Urls
from pages.checking_transitions_page import CheckingTransitions
import allure


class TestChecking:
    @allure.step('Кликаем на логотип Scooter и проверяем URL')
    def test_checking_scooter_logo(self, driver):
        checking_transitions_page = CheckingTransitions(driver)

        checking_transitions_page.open_url(Urls.SCOOTER)

        checking_transitions_page.click_order_button_top()

        checking_transitions_page.click_logo_scooter()
        assert driver.current_url == Urls.SCOOTER

    @allure.step('Кликаем на логотип Яндекса и проверяем URL')
    def test_checking_yandex_logo(self, driver):
        checking_transitions_page = CheckingTransitions(driver)

        checking_transitions_page.open_url(Urls.SCOOTER)

        checking_transitions_page.click_order_button_top()

        checking_transitions_page.click_logo_yandex()
        assert driver.current_url == Urls.DZEN

