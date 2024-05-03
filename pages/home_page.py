from locators.home_locators import Home
from locators.order_locators import Order
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
import allure

@allure.step('Кликаем на кнопку "заказать" вверху и проверяем наличие на странице заголовка')
class OrderButton(BasePage):
    def click_order_button_top(self):
        button = self.wait_and_find_element(*Home.BUTTON_TOP)
        button.click()
        element = self.wait_and_find_element(*Order.ORDER_HEADER)
        assert element.is_displayed()


@allure.step('Кликаем на кнопку "заказать" внизу и проверяем наличие на странице заголовка')
class OrderButton2(BasePage):
    def click_order_button_bottom(self):
        button = self.wait_and_find_element(*Home.BUTTON_BOTTOM)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        action = ActionChains(self.driver)
        action.move_to_element(button).perform()
        self.click_element_with_retry(button)

        element = self.wait_and_find_element(*Order.ORDER_HEADER)
        assert element.is_displayed()
